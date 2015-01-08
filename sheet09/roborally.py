import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARN)


class Space:
    left_trans = dict(N="W", E="N", S="E", W="S")
    move_xy = dict(N=(0, 1), E=(1, 0), S=(0, -1), W=(-1, 0))

    def to_left(dir):
        return Space.left_trans[dir]

    to_left = staticmethod(to_left)

    def to_back(dir):
        return Space.left_trans[Space.left_trans[dir]]

    to_back = staticmethod(to_back)

    def to_right(dir):
        return Space.left_trans[Space.left_trans[Space.left_trans[dir]]]

    to_right = staticmethod(to_right)

    def neighbour(pos, dir):
        return(pos[0] + Space.move_xy[dir][0],
               pos[1] + Space.move_xy[dir][1])

    neighbour = staticmethod(neighbour)


class Factory(Space):

    """The factory contains the static layout of the floor as well as the agents.
       It can add new features to places, but this should only be done in the
       beginning.
       Apart from that the factory senses collisions between agents and
       dispatches the methods call to apply the different factory elements.
    """

    def __init__(self, cols=5, rows=5, installs=()):
        """Inserts objects in 'installs' according to their position in a dict
        """
        self.agents = []
        self.rows = rows
        self.cols = cols
        self.elem_move = 0
        self.reg_phase = 0
        self.floor = dict()
        self.floor['before'] = dict()  # ordinary elements
        self.floor['after'] = dict()  # after tentative move, i.e., walls
        self.floor['last'] = dict()   # after move completed, i.e., pits
        self.init_floor(cols, rows, installs)

    def init_floor(self, cols, rows, installs):
        """Insert pits around the floor
        """
        for i in range(cols + 2):
            for j in (0, rows + 1):
                self.floor['last'][(i, j)] = [Pit(i, j)]
        for i in (0, cols + 1):
            for j in range(1, cols + 1):
                self.floor['last'][(i, j)] = [Pit(i, j)]
        for obj in installs:
            self.install(obj)

    def install(self, obj):
        """Install an object in the right queue
           and trigger the insertion of adjecent, symmetric walls
        """
        if isinstance(obj, Robot):
            self.agents.append(obj)
        elif isinstance(obj, Wall):
            self.floor['after'][obj.pos] = self.floor[
                'after'].get(obj.pos, []) + [obj]
            self.install_adjacent_wall(obj, Space.neighbour(obj.pos, obj.dir))
        elif isinstance(obj, Pit):
            self.floor['last'][obj.pos] = self.floor[
                'last'].get(obj.pos, []) + [obj]
        else:
            self.floor['before'][obj.pos] = self.floor[
                'before'].get(obj.pos, []) + [obj]

    def install_adjacent_wall(self, wall, adjpos):
        for adjel in self.floor['after'].get(adjpos, []):
            if isinstance(adjel, Wall) \
                    and adjel.dir == Space.to_back(wall.dir):
                return
        self.install(Wall(adjpos[0], adjpos[1], Space.to_back(wall.dir)))

    def occupied(self, pos, virtual=False):
        """Checks for agents in this field and returns them"""
        result = []
        for a in self.agents:
            if a.pos == pos and (not a.virtual or virtual):
                result.append(a)
        return result

    def collision(self, agent):
        """Returns all agents that collide with 'agent'.
        """
        result = self.occupied(agent.pos)
        if agent in result:
            result.remove(agent)
        else:
            result = []
        return result

    def apply(self, steps=("before", "after", "last")):
        """Apply all elements to all agents at a place."""
        if type(steps) is str:
            steps = (steps,)
        for step in steps:
            for agent in self.agents:
                for elem in self.floor[step].get(agent.pos, []):
                    elem.apply_element(agent, self)

    def exec_reg_phase(self, reg_phase, cmdlist):
        """Execute one register phase."""
        self.reg_phase = reg_phase
        logging.info("*** Starting register phase %s" % reg_phase)
        self.elem_move = 0
        for cmd in cmdlist:
            cmd(self)
        for self.elem_move in range(1, 7):
            self.apply()
            self.resolve_conflicts()

    def resolve_conflicts(self):
        """Resolve all conflicts created by collosions.
           Simply send all agents a "resolve" message!
        """
        for a in self.agents:
            a.resolve(self)


class Thing(Space):

    """Each thing has a position on the floor"""

    def __init__(self, x, y, **kw):
        self.pos = (x, y)


class OrientedThing(Thing):

    """Anything oriented using cardinal directions (N, E, S, W)"""

    def __init__(self, x, y, dir="N", **kw):
        super().__init__(x, y, **kw)
        self.dir = dir


class TurnableThing(OrientedThing):

    """Anything turnable"""

    def rotate_left(self, *rest):
        self.dir = Space.to_left(self.dir)
        logging.info("rotate_left: %s facing now %s" %
                     (self, self.dir))

    def u_turn(self, *rest):
        self.dir = Space.to_back(self.dir)
        logging.info("u_turn: %s facing now %s" %
                     (self, self.dir))

    def rotate_right(self, *rest):
        self.dir = Space.to_right(self.dir)
        logging.info("rotate_right: %s facing now %s" %
                     (self, self.dir))


class MoveableThing(TurnableThing):

    """Anything moveable"""

    def __init__(self, x, y, dir="N", **kw):
        super().__init__(x, y, dir, **kw)
        self.lastconf = None  # last configuration, i.e. pos and dir

    def startmove(self, dir, factory):
        """Starts movement, which may cause chain reaction,
           and which needs a resolution afterwards.
           The factory will handle that!
        """
        logging.info("startmove: %s wants to go from %s to %s" %
                     (self, self.pos, Space.neighbour(self.pos, dir)))
        self.move(dir, factory)
        factory.resolve_conflicts()
        factory.apply('last')  # check for pits!

    def move(self, dir, factory):
        """Passive or active movement to a neighboring field.
           Is blocked immediately by walls.
           Other robots are pushed.
           Collisions are handled as in the transport case, i.e.,
           resolve is called afterwards.
        """
        logging.info("move: try move of %s from %s to %s" %
                     (self, self.pos, Space.neighbour(self.pos, dir)))
        # try to move into direction dir
        oldpos = self.pos
        self.lastconf = (self.pos, self.dir)
        self.pos = Space.neighbour(self.pos, dir)
        factory.apply('after')  # check for walls
        if oldpos == self.pos:
            # if stopped by a wall, give up
            logging.info("move: %s cannot move because of an obstacle" % self)
            self.lastconf = None
            return
        for collider in factory.collision(self):
            # if collision with another robot, push
            collider.move(dir, factory)

    def transport(self, dir, factory):
        """Transport on a conveyor belt without collision checks"""
        self.lastconf = (self.pos, self.dir)
        self.pos = Space.neighbour(self.pos, dir)
        logging.info("transport: %s to %s" % (self, self.pos))
        factory.apply('after')  # check for walls!

    def resolve(self, factory):
        """Is called after every robot has been transported or moved"""
        collider = factory.collision(self)
        if collider:
            for a in collider + [self]:
                a.retract(factory)
        self.lastconf = None

    def retract(self, factory):
        """There was a collision, so we have to retract the bot
           to the last position
        """
        if self.lastconf:
            self.pos = self.lastconf[0]
            self.dir = self.lastconf[1]
            self.lasctconf = None
            logging.info("retract: send %s back to %s" % (self, self.pos))
            for a in factory.collision(self):
                a.retract(factory)


class Robot(MoveableThing):

    """A robot is a movable thing with extra attributes. It has the ability to
    move one, two, or three fields per phase, turn 90 degrees left or right,
    turn 180 degrees, or move backwards one field.

    >>> r = Robot(1, 2, "N", "FooBar")
    >>> r.pos, r.damage
    ((1, 2), 0)

    """

    def __init__(self, x, y, dir="N", name="", **kw):
        super().__init__(x, y, dir, **kw)
        self.name = name
        self.damage = 0
        self.lives = 3
        self.alive = True
        self.virtual = False
        logging.info("init: %s starts at %s with orientation %s" %
                     (self, self.pos, self.dir))

    def __str__(self):
        return self.name.upper()

    def onestep(self, forward, factory):
        """active execution of one step (forward or backward)"""
        forb = "forward"
        if not forward:
            forb = "backward"
        logging.info("onestep: %s wants to make 1 step %s (dir=%s)" %
                     (self, forb, self.dir))
        if not self.alive:
            logging.info("onestep: %s is dead and cannot move" % self)
            return
        if forward:
            self.startmove(self.dir, factory)
        else:
            self.startmove(Space.to_back(self.dir), factory)

    def move1(self, factory):
        logging.info("MOVE1 command: %s" % self)
        self.onestep(True, factory)

    def move2(self, factory):
        logging.info("MOVE2 command: %s" % self)
        self.onestep(True, factory)
        self.onestep(True, factory)

    def move3(self, factory):
        logging.info("MOVE3 command: %s" % self)
        self.onestep(True, factory)
        self.onestep(True, factory)
        self.onestep(True, factory)

    def backup(self, factory):
        logging.info("BACKUP command: %s" % self)
        self.onestep(False, factory)

    # rotate commands are implemented in turnable object


class FactoryElement(Thing):

    """This is a factory element. You need to specify in which register phase
       and which element move the element will be active. This can be done on a
       per class or per instance base. The main method to specify is the acton
       method.

       Element moves can be:
       0: the robots move
       1: express conveyor belts move one step
       2: express conveyor belts and normal conveyor belts move one step
       3: pushers push
       4: gears turn
       5: crushers crush  -- have to be implemented!
       6: one way portals -- have to be implemented!
       7: (was 6!) lasers fire (board mounted and robot lasers)
       8: (was 7!) repair and checkpoint actions
    """

    active_reg_phases = {1, 2, 3, 4, 5}
    active_elem_moves = {}

    def apply_element(self, agent, factory):

        if (factory.elem_move in self.active_elem_moves and
                factory.reg_phase in self.active_reg_phases and
                agent.alive):
            self.acton(agent, factory)

    def acton(self, agent, factory):
        raise NotImplementedError("acton must be defined")


class Pit(FactoryElement):
    active_elem_moves = {0, 1, 2, 3, 4, 5, 6, 7}

    def acton(self, agent, factory):
        agent.alive = False
        agent.lives -= 1
        agent.virtual = True
        logging.info("%s fell into a pit at %s" % (agent, agent.pos))
        agent.pos = None


class OrientedFactoryElement(FactoryElement):

    def __init__(self, x, y, dir="N", **kw):
        self.dir = dir
        super().__init__(x, y, **kw)


class Wall(OrientedFactoryElement):
    active_elem_moves = {0, 1, 2, 3, 4, 5, 6, 7}

    def acton(self, agent, factory):
        if agent.lastconf:
            if agent.lastconf[0] == Space.neighbour(self.pos, self.dir):
                agent.pos = agent.lastconf[0]
                agent.dir = agent.lastconf[1]
                agent.lastconf = None
                logging.info("%s bumped into a wall and is back at %s" %
                             (agent, agent.pos))


class Pusher(OrientedFactoryElement):

    """Pusher pushes an agent and all others in line one step

       >>> f = Factory(2, 2, installs=(Robot(1, 1, "S", "T"),))
       >>> f.install(Pusher(1, 1, dir='E', reg_phases={2, 5}))
       >>> f.install(Robot(2, 1, "E", "X"))
       >>> f.exec_reg_phase(1,())
       >>> f.agents[0].pos, f.agents[0].dir
       ((1, 1), 'S')
       >>> f.exec_reg_phase(2,())
       >>> f.agents[0].pos, f.agents[1].pos
       ((2, 1), None)

    """
    active_elem_moves = {3}

    def __init__(self, x, y, reg_phases=set(), **kw):
        super().__init__(x, y, **kw)
        self.active_reg_phases = reg_phases

    def acton(self, agent, factory):
        logging.info("PUSHER: push %s at %s into dir %s" %
                     (agent, self.pos, self.dir))
        agent.move(self.dir, factory)


class Gear(FactoryElement):

    """Gear turns robot on the spot

       >>> f = Factory(2, 2, installs=(Robot(1, 1, "S", "T"), Gear(1, 1)))
       >>> f.exec_reg_phase(1,())
       >>> f.agents[0].pos, f.agents[0].dir
       ((1, 1), 'W')

    """
    active_elem_moves = {4}

    def __init__(self, x, y, clockwise=True, **kw):
        super().__init__(x, y, **kw)
        self.clockwise = clockwise

    def acton(self, agent, factory):
        if self.clockwise:
            logging.info("GEAR: turn %s clockwise at %s" % (agent, self.pos))
            agent.rotate_right()
        else:
            logging.info("GEAR: turn %s counter-clockwise at %s" %
                         (agent, self.pos))
            agent.rotate_left()


class Conveyor(OrientedFactoryElement):

    """Conveyor transport robots one step

       >>> f = Factory(2, 2, installs=(Robot(1, 1, "S", "T"),
       ... Conveyor(1, 1, "N")))
       >>> f.exec_reg_phase(1,())
       >>> f.agents[0].pos, f.agents[0].dir
       ((1, 2), 'S')
       >>> f.install(Robot(1, 1, "W", "X"))
       >>> f.exec_reg_phase(1,())
       >>> f.agents[0].pos, f.agents[0].dir, f.agents[1].pos, f.agents[1].dir
       ((1, 2), 'S', (1, 1), 'W')

    """

    active_elem_moves = {2}

    def __init__(self, x, y, dir, **kw):
        super().__init__(x, y, **kw)
        self.dir = dir

    def acton(self, agent, factory):
        logging.info("CONVEYOR: transport %s into dir %s" % (agent, self.dir))
        agent.transport(self.dir, factory)


class TurningConveyor(Conveyor):

    """Note: The TurningConveyor element is the one BEFORE
       the actual corner element, because the rules state that the
       robot is turned immediately after landing on the
       corner place coming from a conveyor belt element.

       >>> f = Factory(2, 2, installs=(Robot(1, 1, "S", "T"),))
       >>> f.install(TurningConveyor(1, 1, dir="N"))
       >>> f.exec_reg_phase(1,())
       >>> f.agents[0].pos, f.agents[0].dir
       ((1, 2), 'W')
    """

    active_elem_moves = {2}

    def __init__(self, x, y, clockwise=True, **kw):
        super().__init__(x, y, **kw)
        self.clockwise = clockwise

    def acton(self, agent, factory):
        if self.clockwise:
            logging.info("TCONV: turn %s clockwise at %s" % (agent, self.pos))
            agent.rotate_right()
        else:
            logging.info("GEAR: turn %s counter-clockwise at %s" %
                         (agent, self.pos))
            agent.rotate_left()
        super().acton(agent, factory)


class Crusher():

    """Crushers destroy robots, when the crushers are active.

    >>> r = Robot(1, 2, "S", "T")
    >>> f = Factory(2, 2, installs=(r,))
    >>> f.install(Crusher(1, 1, reg_phases={3, 4}))
    >>> f.exec_reg_phase(1,(r.move1,))
    >>> r.pos, r.alive
    ((1, 1), True)
    >>> f.exec_reg_phase(2,())
    >>> r.pos, r.alive
    ((1, 1), True)
    >>> f.exec_reg_phase(3,())
    >>> r.pos, r.alive
    (None, False)


    """

    def __init__(self, x, y, reg_phases={}, **kw):
        pass


class OneWayPortal():

    """OneWayPortal are elements that teleport robots to a target place
       become active in the element move phase 6

    >>> r = Robot(1, 1, "E", "Rob")
    >>> t = Robot(3, 3, "S", "Tom")\
    >>> f = Factory(3, 3, installs=(r, t))
    >>> f.install(OneWayPortal(1, 1, target=(3, 3)))
    >>> f.install(Wall(3, 2, dir='N'))
    >>> f.exec_reg_phase(1, ())
    >>> r.pos, t.pos
    ((1, 1), (3, 3))
    >>> f.install(OneWayPortal(3, 3, target=(3, 2)))
    >>> f.exec_reg_phase(2, ())
    >>> r.pos, t.pos
    ((3, 3), (3, 2))
    """

    def __init__(self, x, y, target=(0, 0), **kw):
        pass


if __name__ == "__main__":
    import doctest
    logging.getLogger().setLevel(logging.INFO)
    doctest.testmod()

    if (False):
        logging.getLogger().setLevel(logging.INFO)
        t = Robot(3, 1, "N", "Twonky")
        s = Robot(2, 2, "S", "Spinbot")
        h = Robot(3, 2, "E", "HulkX90")
        fac = Factory(3, 3, installs=(Wall(3, 3, "N"), Pit(2, 3),
                                      Gear(1, 2, True), t, s, h))
        fac.exec_reg_phase(1, (t.move2,))
        fac.exec_reg_phase(2, (t.rotate_left, h.rotate_right))
        fac.exec_reg_phase(3, (t.move2, h.move1, s.move2))
