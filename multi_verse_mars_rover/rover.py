from dataclasses import dataclass
from typing import List


@dataclass
class Rover:
    x_coord: int
    y_coord: int
    orientation: str
    route: List[str]
    is_lost: bool

    def move_forward(self):
        # Could this be done using trig?
        if self.orientation == "W":
            self.x_coord -= 1
        if self.orientation == "E":
            self.x_coord += 1
        if self.orientation == "S":
            self.y_coord -= 1
        if self.orientation == "N":
            self.y_coord += 1

    def move_backward(self):
        # Very much a repeat of the above, but it was easier than calculating
        # the previous position of the rover before it fell off the cliff :)
        if self.orientation == "W":
            self.x_coord += 1
        if self.orientation == "E":
            self.x_coord -= 1
        if self.orientation == "S":
            self.y_coord += 1
        if self.orientation == "N":
            self.y_coord -= 1

    def rotate_clockwise(self) -> None:
        # Could this function be done using maths or a circular list?
        # This code is also very similar to the rotate_anti_clockwise() function.
        if self.orientation == "N":
            self.orientation = "E"
            return
        if self.orientation == "E":
            self.orientation = "S"
            return
        if self.orientation == "S":
            self.orientation = "W"
            return
        if self.orientation == "W":
            self.orientation = "N"
            return

    def rotate_anti_clockwise(self) -> None:
        if self.orientation == "N":
            self.orientation = "W"
            return
        if self.orientation == "W":
            self.orientation = "S"
            return
        if self.orientation == "S":
            self.orientation = "E"
            return
        if self.orientation == "E":
            self.orientation = "N"
            return

    def is_lost_to_string(self) -> str:
        if self.is_lost is True:
            return "LOST"
        else:
            return ""
