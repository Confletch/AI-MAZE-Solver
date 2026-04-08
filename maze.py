class Maze:
    def __init__(self, filename):
        self.grid = self.load_maze(filename) # load maze file
        self.validate_maze() # make sure the maze follows the requirements
        self.start = self.find_position("S") # find the start position (S)
        self.end = self.find_position("E") # find the end position (E)

    def load_maze(self, filename):
        grid = [] # list will store each row of the maze

        # open file and read through line by line
        with open(filename, "r") as file:
            for line in file:
                line = line.rstrip("\n") # remove nreline character from end of each line
                if line != "": # ignore blank lines
                    # converts each line into a list of characters
                    # so each cell can be accessed seperately
                    grid.append(list(line))
        # return the completed maze grid            
        return grid

    # go through each row in the maze
    # go through every column in the maze
    # return matched symbols,,, return its position as (row,col)
    def find_position(self, symbol):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == symbol:
                    return (row, col)
        return None # return none if no symbol is found

    def validate_maze(self):
        # makes sure the maze is not empty
        if not self.grid:
            raise ValueError("Maze file is empty.")

        # run all validation checks
        self.check_rectangular()
        self.check_valid_characters()
        self.check_start_and_end()
        self.check_border_walls()
        
    def check_rectangular(self):
        row_length = len(self.grid[0]) # gets length of the first row
        # makes sure every row has the same length
        for row in self.grid:
            if len(row) != row_length:
                raise ValueError("Maze is not rectangular.")

    def check_valid_characters(self):
        allowed = {"#", " ", "S", "E"} # list of allowed characters in the maze
        # check every cell in the maze
        for row in self.grid:
            for cell in row:
                # if a character isn't allowed, print error
                if cell not in allowed:
                    raise ValueError(f"Invalid character: {cell}")

    def check_start_and_end(self):
        start_count = sum(row.count("S") for row in self.grid) # counts the S within the maze
        end_count = sum(row.count("E") for row in self.grid) # counts the E within the maze

        # ensure there is only one start (S) and end (E)
        if start_count != 1:
            raise ValueError("Maze must have one 'S'")
        if end_count != 1:
            raise ValueError("Maze must have one 'E'")

    # get total nuber or rows and columns
    def check_border_walls(self):
        rows = len(self.grid)
        cols = len(self.grid[0])

        # check the top and bottom row
        for c in range(cols):
            if self.grid[0][c] != "#" or self.grid[rows - 1][c] != "#":
                raise ValueError("Top/Bottom borders must be walls")
        # check the left and righ side of each row
        for r in range(rows):
            if self.grid[r][0] != "#" or self.grid[r][cols - 1] != "#":
                raise ValueError("Side borders must be walls")
