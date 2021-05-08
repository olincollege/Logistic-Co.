"""
Test Logisti-Co model functions.
"""

import pytest
import pygame
from game_model import (
    Package,
    ColorPackage,
    Tower,
    ColorTower,
    Factory,
    Generator,
)

# Define sets of test cases.
package_move_cases = [
    # test moving 1 pixel over in positive x direction
    (0, 0, [(0,0),(10,0)],   (1,0)),
    # test moving 1 pixel over in positive y direction
    (0, 0, [(0,0),(0,10)],   (0,1)),
    # test moving 1 pixel over in negative x direction
    (0, 0, [(0,0),(-10,0)],   (-1,0)),
    # test moving 1 pixel over in negative y direction
    (0, 0, [(0,0),(0,-10)],   (0,-1)),
    # test no moving on provided path
    (0, 0, [(0,0),(0,0)],   (0,0)),
]
@pytest.mark.parametrize("x_pos, y_pos, path, output",package_move_cases)
def test_package_move(x_pos, y_pos, path, output):
    """
    Test movement of Package class.

    Args:
        x_pos: the x-axis location of the package in pixels
        y_pos: the y-axis location of the package in pixels
        path: a list of tuple coordinates depicting the pixel waypoints the
              package should reach.
        output: expected output of the function.
    """
    package = Package(x_pos, y_pos, path)
    package.move()
    assert package.location == output


# Define sets of test cases.
package_no_move_cases = [
    # test no moving on provided path was unsuccessful on path of length 1
    (0, 0, [(0,0)],   False),
    # test no moving on provided path was successful on path of length 2
    (0, 0, [(0,0),(0,0)],   True),
    # test moving 1 pixel over in positive x direction was successful
    (0, 0, [(0,0),(10,0)],   True),
    # test moving 1 pixel over in positive y direction was successful
    (0, 0, [(0,0),(0,10)],   True),
    # test moving 1 pixel over in negative x direction was successful
    (0, 0, [(0,0),(-10,0)],   True),
    # test moving 1 pixel over in negative y direction was successful
    (0, 0, [(0,0),(0,-10)],   True),
]
@pytest.mark.parametrize("x_pos, y_pos, path, output",package_no_move_cases)
def test_package_no_move(x_pos, y_pos, path, output):
    """
    Test movement of Package class.

    Args:
        x_pos: the x-axis location of the package in pixels
        y_pos: the y-axis location of the package in pixels
        path: a list of tuple coordinates depicting the pixel waypoints the
              package should reach.
        output: expected output of the function.
    """
    package = Package(x_pos, y_pos, path)
    assert package.move() == output

############ CONSTRUCTION BELOW ################
# Define sets of test cases.
tower_update_ready_cases = [
    # test rate of 1 is True after 100 cycles.FileNotFoundError()
    (100, 1, True),
    # test rate of 100 is False after one cycle.
    (1, 100, False),
    # test rate of 0 is always True after 100 cycles.
    (100, 0, True),

]
# pylint: disable=no-member
pygame.init()
_ = pygame.display.set_mode([1, 1])

@pytest.mark.parametrize("update_count, rate, output", tower_update_ready_cases)
def test_tower_update_ready(update_count, rate, output):
    """
    Test reset timer on Tower class.

    Args:
        update_count: the number of game ticks which the game is simulated.
        rate: the rate at which the tower can process Package classes.
        output: expected output of the function.
    """
    tower = Tower(0, 0, rate, 10)
    for _ in range(update_count):
        tower.update_ready()
    assert tower.ready == output

# # Define sets of test cases.
# factory_update_robots_cases = [
#     # test
#     (amount_robot,amount_packages,[(x,y)],[(a,b)],robot_rate,cycle_count, output)

#     #
# ]

# @pytest.mark.parametrize("tower_count,output", factory_update_robots_cases)
# def test_factory_update_robots(tower_count,output):
#     """

#     Args:
#         output: expected output of the function.
#     """
#     factory = Factory(tower_count)
#     assert factory. == output
