from multi_verse_mars_rover.main import run

# This is not quite a real acceptance test as entry point is not the command line like a real user
def test_when_i_input_the_grid_and_rover_movements_i_can_see_it_has_gone_off_grid(tmpdir, capsys):
    file = tmpdir / "rover_details.txt"
    file_contents = "(2, 3, E) LFRFF\n(0, 2, N) FFLFRFF"
    file.write_text(file_contents, "UTF-8")
    run(file, grid_x_max=4, grid_y_max=8)

    captured = capsys.readouterr()
    assert captured.out == "(4, 4, E) \n(0, 4, W) LOST\n"
