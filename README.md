## Background
A command line tool for determining if a list of Mars rover's routes will cause them to fall off a grid and get lost. 

## prerequisites
- Docker (Sorry, I know it's not free anymore)

## installation and run instructions
This uses a simple docker container to help run the code. It must be built first. 
1. Build Docker image
```bash
docker build -t mars_rover_way_finder --rm .
```
2. Run Docker image. This will start a shell in the container and allow you to run the command and tests.
```bash
docker run -it --name app --rm mars_rover_way_finder
```

## Running the script
From within the container:
```bash
python -m multi_verse_mars_rover.main --file_path input_example.txt --grid_x_max 4 --grid_y_max 8
```
The file path is to the rover input file. It should contain the rover details.
The other inputs are the grid max and grid y for inputting the grid. See the above command which will contain sample input.

## Running the tests

From within the container:
```bash
python -m pytest
```

## Development
This project uses [poetry](https://python-poetry.org/) to help manage packages and virtual envs. Please have this installed on your local python if you wish to develop the project further.

### Update lock file
Remember to do this if any packages are installed. The deployed, working version of the code generates its requirements from a .txt file and does not use poetry.
 `poetry export -f requirements.txt --output requirements.txt --dev --without-hashes`


## Assumptions
- The rover will never start of grid

## Things to improve
- Make instruction logic more extendable
- Reduce code duplication in the 'Rover' class.
- Talk to product manager about input data. It is hard to use as it is not a well known data standard. Maybe this could be standardised making it easier to develop on a share with others.