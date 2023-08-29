"""Generating .dxf files with warious flatpattenrs."""
import math


class Miter:
    """
    Making a flatpattern for a miter segment of a pipe bend.
    ...

    Attributes
    ----------

    bend_radius : int|float
        inside radius of the miter bend

    bend_angle : int|float
        total angle of the bend

    pipe_radius : int|float
        pipe radius

    n_segment : int
        number of segments the miter bend is divided in
    """

    def __init__(
        self, bend_radius, bend_angle, pipe_radius, miter_segments, pattern_segments
    ) -> None:
        self.bend_radius = bend_radius
        self.bend_angle = bend_angle
        self.pipe_radius = pipe_radius
        self.miter_segments = miter_segments
        self.pattern_segments = pattern_segments

    def __repr__(self):
        return f"{self.__class__.__name__}({self.bend_radius},\
            {self.pipe_radius}, {self.miter_segments})"

    def curvepoints(self) -> list:
        """Generate (x, y) coordinates for the points making the lines of the flatpattern"""
        points = []
        segment_length = (2 * math.pi * self.pipe_radius) / self.pattern_segments
        for i in range(self.pattern_segments + 1):
            x = i * segment_length
            miter_angle = self.bend_angle / (2 * (self.miter_segments - 1))
            segment_angle = i * (2 * math.pi / self.pattern_segments)
            offset = self.pipe_radius * math.cos(segment_angle)
            adjecent_side = self.bend_radius + self.pipe_radius + offset
            y = math.tan(math.radians(miter_angle)) * adjecent_side
            points.append((x, y))
        return points

    def end_segment(self) -> list:
        points = self.curvepoints()
        return points + [(points[-1][0], 0), (0, 0)]

    def full_segment(self) -> list:
        points = self.curvepoints()
        return points + mirror_axis(points[::-1], 'y')

    def objects(self) -> tuple[list]:
        return ([],)

def output_dxf(object) -> None:
    """Make a dxf file with the patterns from (x, y) coordinates"""
    pass


def mirror_axis(line: list, axis: str, offset: int | float = 0):
    """Mirror x (leftmost) or y (rightmost) axis"""
    print(f"axis = {axis}")
    if axis == "x":
        print("running x")
        return [(2 * offset - x, y) for x, y in line]
    else:
        print("running y")
        return [(x, 2 * offset - y) for x, y in line]


def x_arround_circle(radius, num_points):
    points = []
    for i in range(num_points + 1):
        angle = i * (2 * math.pi / num_points)
        y = radius + (radius * math.cos(angle))
        x = math.tan(math.radians(15)) * (y + 40)
        points.append(x)
    return points


for p in x_arround_circle(10, 6):
    print(p)

miter = Miter(40, 90, 10, 4, 6)
for x, y in miter.curvepoints():
    print(y)
