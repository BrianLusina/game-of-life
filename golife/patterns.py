"""
Used for Patterns that will hold the name of a pattern and the co-ordinates of a live cells
"""
from typing import Set, Tuple, List, Dict
from dataclasses import dataclass


@dataclass
class Pattern:
    """
    Holds the pattern information

    Args:
        name (str): Name of the pattern
        alive_cells (set):
        The set of tuples that will allow usage of set operations to determine the cells that will
        be alive in the next generation.
        Each tuple represents the coordinate of an alive cell in the life grid.
    """

    name: str
    alive_cells: Set[Tuple[int, int]]

    @classmethod
    def from_toml(cls, name: str, toml_data: Dict[str, List]) -> "Pattern":
        """Factory method to create an instance of Pattern provided a name and toml data with the grid for the living
        cells
        Args:
            name (str): name of the pattern
            toml_data: grid for the living cells
        Returns:
            Pattern: instance of pattern class
        """
        return cls(
            name=name, alive_cells={tuple(cell) for cell in toml_data["alive_cells"]}
        )
