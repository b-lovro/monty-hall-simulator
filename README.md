# Monty Hall Problem Simulator

## Overview

The Monty Hall problem is a famous probability puzzle named after the host of the American television game show "Let's Make a Deal," Monty Hall. The problem is a probability puzzle based on a game show scenario where a contestant is presented with three doors. Behind one of the doors is a car (the prize), and behind the other two doors are goats. The contestant chooses one of the doors, say Door A. Monty, who knows what is behind each door, opens another door, say Door B, which has a goat behind it. Monty then offers the contestant a choice: stick with the original choice (Door A) or switch to the remaining unopened door (Door C). The puzzle is to determine if the contestant should stick with the initial choice or switch doors to maximize the chance of winning the car.

## Project Description

This project provides a Python simulation of the Monty Hall problem using PySimpleGUI for the graphical interface. The simulation allows users to play the game interactively and visualize the results. The code is organized into a class-based structure, encapsulating the game logic within a `Game` class. The graphical interface shows three doors, allows the user to select a door, and decide whether to switch after one door with a goat is revealed.

## Features

- Interactive simulation of the Monty Hall problem.
- Graphical interface using PySimpleGUI.
- Visualization of game results over multiple iterations.
- Easy to start a new game or exit the application.
- Base64 encoded images are used for the doors to ensure the application is self-contained.

## Installation

### Prerequisites

- Python 
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/b-lovro/monty-hall-simulator.git
   cd monty-hall-simulator
   ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

#### Note:
  When this code was written, PySimpleGUI was still free. However, as of now, PySimpleGUI offers a 30-day free trial period. You may need to purchase a license to continue using it beyond the trial period.

3. Run the application

    ```python
    python monty_hall_simulator.py
    ```