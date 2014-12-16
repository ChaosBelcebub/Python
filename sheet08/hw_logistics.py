"""Working with classes.

.. versionadded:: 2014-12-12
.. moduleauthor:: Tim Schulte

This module implements two classes for exercise sheet 8. The classes
defined below serve as the starting point for your own extensions.

References:
  .. [1] Lecture slides at
     http://www.informatik.uni-freiburg.de/~ki/teaching/ws1415/info1/lecture.html

"""


class Cargo:

    """Generic class for Cargo objects that can be transported between locations.

    Args:
      idnumber (int): the cargo's identification number
      description (string): describing the cargo content
      weight (int): representing the cargo's physical weight in kilogram
      location (string): the cargo's current physical location

    Attributes:
      idnumber
      decription
      weight
      location

    Examples:

      >>> c = Cargo(idnumber=1, description="metal",
      ...           weight=500, location="Freiburg")
      >>> c
      Cargo(idnumber=1, description='metal', weight=500, location='Freiburg')

    """

    def __init__(self, idnumber, description, weight, location):
        self._idnumber = idnumber
        self.description = description
        self._weight = weight
        self._location = location
        self._history = ""

    def update_location(self, location):
        self._history += self._location + " to " + location + "\n"
        self._location = location

    def get_idnumber(self):
        return self._idnumber

    def get_weight(self):
        return self._weight

    def get_location(self):
        return self._location

    def get_history(self):
        return self._history

    idnumber = property(get_idnumber)
    weight = property(get_weight)
    location = property(get_location, update_location)
    history = property(get_history)

    def __repr__(self):
        return ("Cargo(idnumber=%s, description=%r, weight=%s, location=%r)" %
                (self._idnumber, self.description,
                 self._weight, self._location))


class MeansOfTransport:

    """Generic class for objects that can transport cargo between locations.

    Args:
      location (string): the transport object's current physical location
      cargocapacity (int): the maximum total weight of the cargo in kilogram

    Attributes:
      location
      cargocapacity
      cargo (list): contains all cargo objects currently transported

    Methods:
      move: Move from current location to target location
      cargo_weight: Return the total weight of all cargo objects
                    in the cargo list
      add_cargo: Add a cargo object to the cargo list, if cargocapacity is not
                 exceeded, cargo object is at same location and not already
                 in cargo list
      unload_cargo: Unload a cargo specified by idnumber from cargo list and
                    return it to caller; return None in case of failure
      list_cargo: Prints a human readable description of the cargo list

    Examples:

      >>> t = MeansOfTransport(location="Freiburg", cargocapacity=50000)
      >>> t.location
      'Freiburg'
      >>> log = t.move("Bielefeld")
      >>>
      >>> t.location
      'Bielefeld'

    """

    def __init__(self, location, cargocapacity):
        self.location = location
        self.cargocapacity = cargocapacity
        self.cargo = []

    def __str__(self):
        return "location: {}\ncargocapacity: {}".format(
            self.location, self.cargocapacity)

    def move(self, destination):
        """Move from current location to target location."""
        oldlocation = self.location
        self.location = destination
        for c in self.cargo:
            c.location = destination
        return "Moves from {} to {}".format(oldlocation, destination)

    def cargo_weight(self):
        """Return the total weight of all cargo objects in the cargo list"""
        total_weight = 0
        for c in self.cargo:
            total_weight += c.weight
        return total_weight

    def add_cargo(self, new_cargo):
        """Add a cargo object to the cargo list, if cargocapacity is not
           exceeded, cargo object is at same location and not already in
           cargo list."""
        if (self.cargo_weight() + new_cargo.weight <= self.cargocapacity
           and self.location == new_cargo.location
           and new_cargo.idnumber not in [c.idnumber for c in self.cargo]):
            self.cargo.append(new_cargo)

    def unload_cargo(self, cargo_id):
        """Unload a cargo specified by idnumber from cargo list and
           return it to caller; return None in case of failure."""
        for c in self.cargo:
            if c.idnumber == cargo_id:
                self.cargo.remove(c)
                return c
        return None

    def list_cargo(self):
        """Prints a human readable description of the cargo list."""
        print("Cargo contains:")
        for c in self.cargo:
            print("{:<20}: {:>8}kg".format(c.description, c.weight))


def test_update_location():
    t1 = MeansOfTransport("Freiburg", 20)
    t2 = MeansOfTransport("Freiburg", 30)
    c1 = Cargo(1, "Bananas", 5, "Freiburg")
    c2 = Cargo(2, "Ananas", 5, "Freiburg")
    c3 = Cargo(3, "Wasser", 5, "Freiburg")
    c4 = Cargo(4, "Elfenbein", 5, "Freiburg")
    c5 = Cargo(5, "BigMacs", 5, "Freiburg")
    t1.add_cargo(c1)
    t1.add_cargo(c2)
    t2.add_cargo(c3)
    t2.add_cargo(c4)
    t2.add_cargo(c5)
    t1.move("Basel")
    t1.unload_cargo(1)
    t1.move("New York")
    t1.unload_cargo(2)
    t2.move("Berlin")
    t2.unload_cargo(3)
    t2.move("Stockholm")
    t2.unload_cargo(4)
    t2.move("Winterwunderland")
    t2.unload_cargo(5)
    assert c1.location == "Basel"
    assert c2.location == "New York"
    assert c3.location == "Berlin"
    assert c4.location == "Stockholm"
    assert c5.location == "Winterwunderland"


def test_history():
    t1 = MeansOfTransport("Freiburg", 20)
    t2 = MeansOfTransport("Freiburg", 30)
    c1 = Cargo(1, "Bananas", 5, "Freiburg")
    c2 = Cargo(2, "Ananas", 5, "Freiburg")
    c3 = Cargo(3, "Wasser", 5, "Freiburg")
    c4 = Cargo(4, "Elfenbein", 5, "Freiburg")
    c5 = Cargo(5, "BigMacs", 5, "Freiburg")
    t1.add_cargo(c1)
    t1.add_cargo(c2)
    t2.add_cargo(c3)
    t2.add_cargo(c4)
    t2.add_cargo(c5)
    t1.move("Basel")
    t1.unload_cargo(1)
    t1.move("New York")
    t1.unload_cargo(2)
    t2.move("Berlin")
    t2.unload_cargo(3)
    t2.move("Stockholm")
    t2.unload_cargo(4)
    t2.move("Winterwunderland")
    t2.unload_cargo(5)
    assert c1.history == "Freiburg to Basel\n"
    assert c2.history == "Freiburg to Basel\nBasel to New York\n"
    assert c3.history == "Freiburg to Berlin\n"
    assert c4.history == "Freiburg to Berlin\nBerlin to Stockholm\n"
    assert c5.history == "Freiburg to Berlin\nBerlin to Stockholm\n" + \
                         "Stockholm to Winterwunderland\n"

if __name__ == "__main__":
    test_update_location()
    test_history()
