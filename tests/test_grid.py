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


if __name__ == "__main__":
    unittest.main()
