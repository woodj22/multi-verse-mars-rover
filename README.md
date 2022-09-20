## Background
A tool for determining if a list of Mars rovers routes will cause them to fall off a grid and get lost. 

## prerequisites
- Docker (Sorry, I know it's not free anymore)

## installation instructions and run

1. Build Docker image
```bash
docker build -t mars_rover_way_finder --rm .
```
2. Run Docker image. This will start a shell in the container
```bash
docker run -it --name app --rm mars_rover_way_finder
```

## Running the script
From within the container:
```bash
python -m multi_verse_mars_rover.main --file_path input_example.txt --grid_x_max 4 --grid_y_max 8
```
The inputs to the file is a file path, of which the file contains the rover details and the grid x and y max that make up the grid that the rover can drive off. 

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


## What would I do better next time
- Make instruction logic more extendable
- Implement a more 'mathematical' way of controlling the rover