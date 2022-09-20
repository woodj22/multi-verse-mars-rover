from multi_verse_mars_rover.rover import Rover
import pytest


def test_it_can_move_rover_east_along_horizontal_axis():
    rover = Rover(x_coord=2, y_coord=3, orientation="E", route=[], is_lost=False)
    rover.move_forward()
    assert rover.x_coord == 3


def test_it_can_move_rover_west_along_horizontal_axis():
    rover = Rover(x_coord=2, y_coord=3, orientation="W", route=[], is_lost=False)
    rover.move_forward()
    assert rover.x_coord == 1


def test_it_can_move_rover_north_along_vertical_axis():
    rover = Rover(x_coord=2, y_coord=3, orientation="N", route=[], is_lost=False)
    rover.move_forward()
    assert rover.y_coord == 4


def test_it_can_move_rover_south_along_vertical_axis():
    rover = Rover(x_coord=2, y_coord=3, orientation="S", route=[], is_lost=False)
    rover.move_forward()
    assert rover.y_coord == 2


@pytest.mark.parametrize("test_input, expected", [("N", "E"), ("E", "S"), ("S", "W"), ("W", "N")])
def test_it_rotates_clockwise(test_input, expected):
    rover = Rover(x_coord=2, y_coord=3, orientation=test_input, route=[], is_lost=False)
    rover.rotate_clockwise()
    assert rover.orientation == expected


@pytest.mark.parametrize("test_input, expected", [("N", "W"), ("W", "S"), ("S", "E"), ("E", "N")])
def test_it_rotates_anti_clockwise(test_input, expected):
    rover = Rover(x_coord=2, y_coord=3, orientation=test_input, route=[], is_lost=False)
    rover.rotate_anti_clockwise()
    assert rover.orientation == expected