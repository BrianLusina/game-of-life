import unittest
from golife.grid import LifeGrid
from golife.patterns import Pattern


class LifeGridTestCase(unittest.TestCase):
    def test_oscillator_pattern(self):
        """should return the same pattern of cells when evolve is called twice on the same set of cells"""
        blinker = Pattern("Blinker", {(2, 1), (2, 2), (2, 3)})
        grid = LifeGrid(blinker)

        # evolve the grid
        grid.evolve()

        # check the state of the cells
        expected_first_generation_cells = {(1, 2), (2, 2), (3, 2)}
        actual_first_generation_cells = blinker.alive_cells
        self.assertEqual(expected_first_generation_cells, actual_first_generation_cells)

        # evolve cells again
        grid.evolve()

        expected_second_generation_cells = {(2, 1), (2, 2), (2, 3)}
        actual_second_generation_cells = blinker.alive_cells

        self.assertEqual(
            expected_second_generation_cells, actual_second_generation_cells
        )

    def test_as_string(self):
        """should return the representation of the grid as a string in a bounding box"""
        blinker = Pattern("Blinker", {(2, 1), (2, 2), (2, 3)})
        grid = LifeGrid(blinker)

        expected_grid_before_evolution = (
            " Blinker  \n. . . . .\n. . . . .\n. ♥ ♥ ♥ .\n. . . . .\n. . . . ."
        )
        actual_as_string_before_evolution = grid.as_string((0, 0, 5, 5))
        self.assertEqual(
            expected_grid_before_evolution, actual_as_string_before_evolution
        )

        # evolve the grid
        grid.evolve()
        expected_grid_after_evolution = (
            " Blinker  \n. . . . .\n. . ♥ . .\n. . ♥ . .\n. . ♥ . .\n. . . . ."
        )
        actual_as_string_after_evolution = grid.as_string((0, 0, 5, 5))
        self.assertEqual(
            expected_grid_after_evolution, actual_as_string_after_evolution
        )


if __name__ == "__main__":
    unittest.main()
