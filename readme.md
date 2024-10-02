# Conway's Game of Life

Conway's Game of Life is a simple simulation of an ecosystem. It consists of a grid of cells, each of which can be either alive or dead. The state of each cell is determined by the following rules:

- any live cell with fewer than two live neighbors dies, as if by under-population.
- any live cell with two or three live neighbors lives on to the next generation.
- any live cell with more than three live neighbors dies, as if by overpopulation.
- any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Why?
This is an exploration of Python

## Setup
The requirements are listed in the `requirements.txt` file and can be installed with
```bash
pip install -r requirements.txt
```

## Running the app
The application can be run with
```bash
python main.py
```

