"""Working with classes.

.. versionadded:: 2014-12-09
.. moduleauthor:: Michael Kotzjan

"""

class Cargo:
    """Class for cargo

    Args:
      idnumber (int): Cargo ID
      description (string): Cargo description
      weight (int): Cargo weight
      location (string): Location of the cargo

    Attributes:
      idnumber (int): Cargo ID
      description (string): Cargo description
      weight (int): Cargo weight
      location (string): Location of the cargo

    .. versionadded:: 2014-12-09
    """

    def __init__(self, idnumber, description, weight, location):
        self.idnumber = idnumber
        self.description = description
        self.weight = weight
        self.location = location

    def __repr__(self):
        return "Cargo(idnumber=%s, description=%s, weight=%s, location=%s)"\
               % (self.idnumber, self.description, self.weight, self.location)

class MeansOfTransport:
    """Class for transportation

    Args:
      location (string): location
      cargocapacaty (int): max cargo capacaty

    Attributes:
      location (string): location
      cargocapacaty (int): max cargo capacaty
      cargo (list): cargo objects

    .. versionadded:: 2014-12-09
    """

    def __init__(self, location, cargocapacaty):
        self.location = location
        self.cargocapacaty = cargocapacaty
        self.cargo = []


    def move(self, destination):
        location = self.location
        self.location = destination
        return "Moves from %s to %s" % (location, self.location)


    def cargo_weight(self):
        result = 0
        for cargo in self.cargo:
            result += cargo.weight
        return result


    def add_cargo(self, new_cargo):
        weight = self.cargo_weight()
        if weight + new_cargo.weight <= self.cargocapacaty:
            if self.location == new_cargo.location:
                if new_cargo not in self.cargo:
                    self.cargo.append(new_cargo)
                    return True
        return False


    def unload_cargo(self, cargo_id):
        for cargo in self.cargo:
            if cargo.idnumber == cargo_id:
                self.cargo.remove(cargo)
                return True
        return None


    def list_cargo(self):
        out = ""
        for cargo in self.cargo:
            out += "Description: " + cargo.description + "\n"
            out += "Weight: " + cargo.weight + "\n\n"
        return out


class Ship(MeansOfTransport):
    """Class for ships

    Args:
      name (string): name of ship
      location (string): location
      cargocapacaty (int): max cargo capacaty

    Attributes:
      name (string): name of ships
      location (string): location
      cargocapacaty (int): max cargo capacaty

    .. versionadded:: 2014-12-09
    """

    def __init__(self, name, location, cargocapacaty):
        self.name = name
        super().__init__(location, cargocapacaty)


    def __str__(self):
        return "Name: %s\nLocation: %s\nCargocapacaty: %s" % (self.name,\
                                                            self.location,\
                                                            self.cargocapacaty)


class CargoShip(Ship):
    """Class for cargoship

    Args:
      name (string): name of ship
      location (string): location
      cargocapacaty (int): max cargo capacaty
      fuel_amount (int): fuel_amount

    Attributes:
      name (string): name of ships
      location (string): location
      cargocapacaty (int): max cargo capacaty
      fuel_amount (int): fuel_amount

    .. versionadded:: 2014-12-09
    """

    def __init__(self, name, location, cargocapacaty, fuel_amount):
        self.fuel_amount = fuel_amount
        super().__init__(name, location, cargocapacaty)


    def __str__(self):
        return "Name: %s\nLocation: %s\nCargocapacaty: %s\nFuelAmount: %s"\
               % (self.name, self.location, self.cargocapacaty,\
                  self.fuel_amount)


class SailingShip(Ship):
    """Class for sailingship

    Args:
      name (string): name of ship
      location (string): location
      cargocapacaty (int): max cargo capacaty
      mast_count (int): count of masts

    Attributes:
      name (string): name of ships
      location (string): location
      cargocapacaty (int): max cargo capacaty
      mast_count (int): count of masts

    .. versionadded:: 2014-12-09
    """

    def __init__(self, name, location, cargocapacaty, mast_count):
        self.mast_count = mast_count
        super().__init__(name, location, cargocapacaty)


    def __str__(self):
        return "Name: %s\nLocation: %s\nCargocapacaty: %s\nMastCount: %s"\
               % (self.name, self.location, self.cargocapacaty,\
                  self.mast_count)


def test_cargo_weight():
    CargoShip1 = CargoShip("Destiny", "Hamburg", 50, 50)
    CargoShip2 = CargoShip("Victoria", "Hamburg", 30, 60)
    SailingShip1 = SailingShip("Emanuela", "Hamburg", 25, 3)
    SailingShip2 = SailingShip("Liselotte", "Hamburg", 50, 6)
    Cargo1 = Cargo(1, "Bananen", 10, "Hamburg")
    Cargo2 = Cargo(2, "Schokolade", 5, "Hamburg")
    Cargo3 = Cargo(3, "Eier", 2, "Hamburg")
    CargoShip1.add_cargo(Cargo1)
    CargoShip1.add_cargo(Cargo3)
    CargoShip2.add_cargo(Cargo2)
    SailingShip1.add_cargo(Cargo1)
    SailingShip1.add_cargo(Cargo2)
    SailingShip1.add_cargo(Cargo3)
    SailingShip2.add_cargo(Cargo1)
    SailingShip2.add_cargo(Cargo2)
    assert CargoShip1.cargo_weight() == 12
    assert CargoShip2.cargo_weight() == 5
    assert SailingShip1.cargo_weight() == 17
    assert SailingShip2.cargo_weight() == 15
    

def test_add_cargo():
    CargoShip1 = CargoShip("Destiny", "Hamburg", 50, 50)
    CargoShip2 = CargoShip("Victoria", "Hamburg", 30, 60)
    SailingShip1 = SailingShip("Emanuela", "Hamburg", 25, 3)
    SailingShip2 = SailingShip("Liselotte", "Hamburg", 50, 6)
    Cargo1 = Cargo(1, "Bananen", 10, "Hamburg")
    Cargo2 = Cargo(2, "Schokolade", 5, "Hamburg")
    Cargo3 = Cargo(3, "Eier", 2, "Hamburg")
    CargoShip1.add_cargo(Cargo1)
    CargoShip1.add_cargo(Cargo2)
    CargoShip1.add_cargo(Cargo3)
    CargoShip2.add_cargo(Cargo1)
    CargoShip2.add_cargo(Cargo2)
    CargoShip2.add_cargo(Cargo3)
    SailingShip1.add_cargo(Cargo1)
    SailingShip1.add_cargo(Cargo2)
    SailingShip1.add_cargo(Cargo3)
    SailingShip2.add_cargo(Cargo1)
    SailingShip2.add_cargo(Cargo2)
    SailingShip2.add_cargo(Cargo3)

    Cargo4 = Cargo(4, "Kuchen", 5, "Berlin")
    Cargo5 = Cargo(5, "Wein", 20, "Hamburg")
    assert CargoShip1.add_cargo(Cargo1) == False
    assert CargoShip2.add_cargo(Cargo4) == False
    assert SailingShip1.add_cargo(Cargo5) == False
    assert SailingShip2.add_cargo(Cargo5) == True


def test_unload_cargo():
    CargoShip1 = CargoShip("Destiny", "Hamburg", 50, 50)
    CargoShip2 = CargoShip("Victoria", "Hamburg", 30, 60)
    SailingShip1 = SailingShip("Emanuela", "Hamburg", 25, 3)
    SailingShip2 = SailingShip("Liselotte", "Hamburg", 50, 6)
    Cargo1 = Cargo(1, "Bananen", 10, "Hamburg")
    Cargo2 = Cargo(2, "Schokolade", 5, "Hamburg")
    Cargo3 = Cargo(3, "Eier", 2, "Hamburg")
    CargoShip1.add_cargo(Cargo1)
    CargoShip1.add_cargo(Cargo2)
    CargoShip1.add_cargo(Cargo3)
    CargoShip2.add_cargo(Cargo1)
    CargoShip2.add_cargo(Cargo2)
    CargoShip2.add_cargo(Cargo3)
    SailingShip1.add_cargo(Cargo1)
    SailingShip1.add_cargo(Cargo2)
    SailingShip1.add_cargo(Cargo3)
    SailingShip2.add_cargo(Cargo1)
    SailingShip2.add_cargo(Cargo2)
    SailingShip2.add_cargo(Cargo3)
    


def test_move():
    CargoShip1 = CargoShip("Destiny", "Hamburg", 50, 50)
    CargoShip2 = CargoShip("Victoria", "Hamburg", 30, 60)
    SailingShip1 = SailingShip("Emanuela", "Hamburg", 25, 3)
    SailingShip2 = SailingShip("Liselotte", "Hamburg", 50, 6)
    Cargo1 = Cargo(1, "Bananen", 10, "Hamburg")
    Cargo2 = Cargo(2, "Schokolade", 5, "Hamburg")
    Cargo3 = Cargo(3, "Eier", 2, "Hamburg")
    CargoShip1.add_cargo(Cargo1)
    CargoShip1.add_cargo(Cargo2)
    CargoShip1.add_cargo(Cargo3)
    CargoShip2.add_cargo(Cargo1)
    CargoShip2.add_cargo(Cargo2)
    CargoShip2.add_cargo(Cargo3)
    SailingShip1.add_cargo(Cargo1)
    SailingShip1.add_cargo(Cargo2)
    SailingShip1.add_cargo(Cargo3)
    SailingShip2.add_cargo(Cargo1)
    SailingShip2.add_cargo(Cargo2)
    SailingShip2.add_cargo(Cargo3)


if __name__ == "__main__":
    test_cargo_weight()
    test_add_cargo()
    test_unload_cargo()
    test_move()
