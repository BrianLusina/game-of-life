from .patterns import Pattern


class LifeGrid:
    """
    This takes care of 2 specific tasks:
    1. Evolving the grid to the next generation
    2. Providing a string representation of the grid

    """

    def __init__(self, pattern: Pattern):
        """Initializes a life grid and takes a pattern instance"""
        self.pattern = pattern

    def evolve(self):
        """Checks the currently alive cells and their neighbours to determine the next generation of alive cells"""
        pass

    def as_string(self, bbox):
        """Provides a way to represent the grid as a string that can be displayed in a terminal window.
        Args:
            bbox: Bounding box for the life grid. This box defines which part of the grid to display in the terminal
            window.
        """
        pass

    def __str__(self):
        pass
