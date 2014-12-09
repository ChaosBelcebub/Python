"""Working with classes.

.. versionadded:: 2014-12-04
.. moduleauthor:: CBA

This module implements a class hierarchy of geometric 2D objects. The classes
defined below show basic techniques needed when working with classes, objects,
etc.

References:
  .. [1] Lecture slides at
     http://www.informatik.uni-freiburg.de/~ki/teaching/ws1415/info1/lecture.html

"""

from math import pi


class TwoDObject:

    """Generic class for two dimensional geometric objects.

    We assume that each such object has a unique anchor point.
    The class has a counter that keeps track how many objects have been
    created.

    Args:
      x (float, optional): x-value of the anchor point, defaults to 0.0.
      y (float, optional): y-value of the anchor point, defaults to 0.0.

    Attributes:
      x (float): x-value of the anchor point.
      y (float): y-value of the anchor point.

    Class Attributes:
      counter (int): Counter for the objects generated.

    Examples:

      >>> a = TwoDObject()
      >>> pos = a.x, a.y
      >>> pos
      (0.0, 0.0)
      >>> repr(a)
      'TwoDObject(x=0.0, y=0.0)'
      >>> b = TwoDObject(x=0.0, y=0.0)
      >>> a == b
      False

    .. versionadded:: 2014-12-04
    """

    counter = 0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        TwoDObject.counter += 1

    def __repr__(self):
        return "TwoDObject(x=%s, y=%s)" % (self.x, self.y)


class Circle(TwoDObject):

    """Circles.

    Args:
      x (float, optional): x-value of the anchor point, defaults to 0.0.
      y (float, optional): y-value of the anchor point, defaults to 0.0.
      radius (float, optional): Radius of the circle, defaults to 0.0.

    Attributes:
      x
      y
      radius

    Methods:
      area: Calculate area.
      change_size

    Examples:

      >>> a = Circle(radius=2.0)
      >>> a
      Circle(x=0.0, y=0.0, radius=2.0)
      >>> a.area()   # doctest: +ELLIPSIS
      12.566...

    .. versionadded:: 2014-12-04
    """

    def __init__(self, x=0.0, y=0.0, radius=1.0):
        self.radius = radius
        super().__init__(x, y)

    def area(self):
        """Calculate the area of the circle."""
        return pi * (self.radius ** 2)

    def change_size(self, percent):
        """Change the size of the circle in percent.

        Operation does not change the anchor.

        Args:
          percent (float): the percentage by which we change the size.

        """
        self.radius *= (percent / 100.0)

    def __repr__(self):
        return "Circle(x=%s, y=%s, radius=%s)" % (self.x, self.y, self.radius)


class Rectangle(TwoDObject):

    """Axis-aligned rectangles.

    An instance of this class represents a rectangle with the following
    corners: (x, y), (x, y+height), (x+width, y+height), and (x+width, y).

    Args:
      x (float, optional): x-value of the anchor point, defaults to 0.0.
      y (float, optional): y-value of the anchor point, defaults to 0.0.
      height (float, optional): height of the rectangle, defaults to 1.0.
      width (float, optional): width of the rectangle, defaults to 1.0.

    Attributes:
      x
      y
      heigth
      width

    Examples:

      >>> a = Rectangle(height=2.0, width=4.0)
      >>> a.stretch_height(200)
      >>> a
      Rectangle(x=0.0, y=0.0, height=4.0, width=4.0)

    .. versionadded:: 2014-12-04
    """

    def __init__(self, x=0.0, y=0.0, height=1.0, width=1.0):
        self.height = height
        self.width = width
        super().__init__(x, y)

    def area(self):
        """Calculate the area of the rectangle."""
        return self.height * self.width

    def change_size(self, percent):
        """Change the size of the rectangle in percent.

        Operation does not change the anchor.

        Args:
          percent (float): the percentage by which we change the size.

        """
        self.height *= (percent / 100.0)
        self.width *= (percent / 100.0)

    def stretch_height(self, percent):
        """Stretch height of the rectangle.

        Operation does not change the anchor.

        Args:
          percent (float): the percentage by which we change the height.

        """
        self.height *= (percent / 100.0)

    def stretch_width(self, percent):
        """Stretch width of the rectangle.

        See Also:
          stretch_height

        """
        self.width *= (percent / 100.0)

    def __repr__(self):
        return ("Rectangle(x=%s, y=%s, height=%s, width=%s)" %
                (self.x, self.y, self.height, self.width))


class Square(Rectangle):

    """Axis-aligned squares.

    Args:
      x (float, optional): x-value of the anchor point, defaults to 0.0.
      y (float, optional): y-value of the anchor point, defaults to 0.0.
      side (float, optional): Length of one side of the square,
        defaults to 1.0.

    Attributes:
      x
      y
      height (float): height of the square.
      width (float): width of the square.

    Examples:

      >>> a = Square(side=3.1)
      >>> a.stretch_width(200)
      >>> a
      Square(x=0.0, y=0.0, side=6.2)

    .. versionadded:: 2014-12-04
    """

    def __init__(self, x=0.0, y=0.0, side=1.0):
        super().__init__(x, y, side, side)

    def change_size(self, percent):
        super().change_size(percent)

    stretch_height = change_size
    stretch_width = change_size

    def __repr__(self):
        return "Square(x=%s, y=%s, side=%s)" % (self.x, self.y, self.height)


class Rhombus(Rectangle):
  """ Axis-aligned rectangles.

  An instance of this class represents a rhombus with the following
  corners: (width/2+x, y), (x, height/2+y), (-(width/2)+x, y),
  and (x, -(height/2)+y).

  Args:
    x (float, optional):
def _test():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    _test()
