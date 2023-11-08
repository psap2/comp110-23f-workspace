"""Point class."""

from __future__ import annotations


class Point:
    """Class used to create points through attributes."""
    x: float
    y: float

    def __init__(self, input_x: float, input_y: float) -> None:
        """Constructor or init method."""
        self.x = input_x
        self.y = input_y
        pass

    def scale_by(self, factor: int) -> None:
        """Method to update the x and y with the factor."""
        self.x = self.x * factor
        self.y = self.y * factor
        
    def scale(self, factor: int) -> Point:
        """Return a new Point with x and y attributes."""
        scale_point: Point = Point(self.x * factor, self.y * factor)
        return scale_point
    
        
