from multi_verse_mars_rover.main import rover_has_gone_off_grid, create_rovers_from_file_string


def test_it_can_determine_rover_has_gone_off_grid_on_y_axis():
    x_max = 10
    y_max = 5
    rover_coord = (6, 9)
    assert rover_has_gone_off_grid(x_max, y_max, rover_coord) is True


def test_it_can_determine_rover_has_gone_off_grid_on_x_axis():
    x_max = 10
    y_max = 5
    rover_coord = (11, 4)
    assert rover_has_gone_off_grid(x_max, y_max, rover_coord) is True


def test_it_can_determine_rover_has_not_gone_off_grid():
    x_max = 10
    y_max = 5
    rover_coord = (2, 4)
    assert rover_has_gone_off_grid(x_max, y_max, rover_coord) is False


def test_it_create_rovers_from_file_string():
    file_string = "(2, 3, E) LFRFF\n(0, 2, N) FFLFRFF"
    expected = create_rovers_from_file_string(file_string)

    assert expected[0].x_coord == 2
    assert expected[0].y_coord == 3
    assert expected[0].orientation == "E"
    assert expected[0].route == list("LFRFF")

    assert expected[1].x_coord == 0
    assert expected[1].y_coord == 2
    assert expected[1].orientation == "N"
    assert expected[1].route == list("FFLFRFF")
