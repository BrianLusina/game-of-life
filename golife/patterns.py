from typing import Set, Tuple
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
