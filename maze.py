class Maze:
    def __init__(self, filename):
        self.grid = self.load_maze(filename)
        self.validate_maze()
        self.start = self.find_position("S")
        self.end = self.find_position("E")

    def load_maze(self, filename):
        grid = []

        with open(filename, "r") as file:
            for line in file:
                line = line.rstrip("\n")
                if line != "":
                    grid.append(list(line))

        return grid

    def find_position(self, symbol):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == symbol:
                    return (row, col)
        return None

    def validate_maze(self):
        if not self.grid:
            raise ValueError("Maze file is empty.")

        self.check_rectangular()
        self.check_valid_characters()
        self.check_start_and_end()
        self.check_border_walls()

    def check_rectangular(self):
        row_length = len(self.grid[0])
        for row in self.grid:
            if len(row) != row_length:
                raise ValueError("Maze is not rectangular.")

    def check_valid_characters(self):
        allowed = {"#", " ", "S", "E"}
        for row in self.grid:
            for cell in row:
                if cell not in allowed:
                    raise ValueError(f"Invalid character: {cell}")

    def check_start_and_end(self):
        start_count = sum(row.count("S") for row in self.grid)
        end_count = sum(row.count("E") for row in self.grid)

        if start_count != 1:
            raise ValueError("Maze must have one 'S'")
        if end_count != 1:
            raise ValueError("Maze must have one 'E'")

    def check_border_walls(self):
        rows = len(self.grid)
        cols = len(self.grid[0])

        for c in range(cols):
            if self.grid[0][c] != "#" or self.grid[rows - 1][c] != "#":
                raise ValueError("Top/Bottom borders must be walls")

        for r in range(rows):
            if self.grid[r][0] != "#" or self.grid[r][cols - 1] != "#":
                raise ValueError("Side borders must be walls")