import argparse
from typing import Tuple, List
from multi_verse_mars_rover.rover import Rover


def rover_has_gone_off_grid(x_max: int, y_max: int, rover_coord: Tuple[int, int]) -> bool:
    if x_max < rover_coord[0] or rover_coord[0] < 0 or y_max < rover_coord[1] or rover_coord[1] < 0:
        return True
    return False


def create_rovers_from_file_string(rover_details: str) -> List[Rover]:
    # This function is pretty nasty because it is overly complex.
    # Would be nice to figure out a better interface between file input and dataclass
    rover_inputs = rover_details.split("\n")
    rovers = []
    for rover in rover_inputs:
        positions, route = rover.split(") ", -1)
        x_coord, y_coord, orientation = positions.replace("(", "").split(",")
        rovers.append(
            Rover(x_coord=int(x_coord),
                  y_coord=int(y_coord),
                  orientation=orientation.replace(" ", ""),
                  route=list(route),
                  is_lost=False
                  )
        )
    return rovers


def run(file_path: str, grid_x_max: int, grid_y_max: int):

    with open(file_path, "r") as file:
        rover_details = file.read()

    rovers = create_rovers_from_file_string(rover_details)
    #  How is this code extendable? i.e. What would happen if we added an LL instruction? or a 50% L instruction?
    for rover in rovers:
        for instruction in rover.route:
            if instruction == "L":
                rover.rotate_anti_clockwise()
            elif instruction == "R":
                rover.rotate_clockwise()
            elif instruction == "F":
                rover.move_forward()
            if rover_has_gone_off_grid(grid_x_max, grid_y_max, (rover.x_coord, rover.y_coord)):
                rover.is_lost = True
                rover.move_backward()
                break

        # Very unuseful output without reading the code. It could be clearer but I would check with my product manager on output specifications to get it right. and maybe wrap it in a founction.
        print(f"({rover.x_coord}, {rover.y_coord}, {rover.orientation}) {rover.is_lost_to_string()}")


parser = argparse.ArgumentParser(description='Check if a rover will fall off a grid')
parser.add_argument("--file_path", type=str, required=True)
parser.add_argument("--grid_x_max", type=int, required=True)
parser.add_argument("--grid_y_max", type=int, required=True)
if __name__ == "__main__":
    # this piece is untested, even by acceptance test
    args = parser.parse_args()
    run(args.file_path, args.grid_x_max, args.grid_y_max)
