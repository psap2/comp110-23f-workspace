"""CQ07 Test."""

__author__ = "730651920"

from lessons.CQ07.point import Point

new_point: Point = Point(5.0, 4.0)

print(new_point.scale_by(3))
print(new_point.scale(3))