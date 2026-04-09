class TerminalOutput:
    def display_maze(self, grid):
        # prints each row of the maze
        for row in grid:
            print("".join(row))

    def display_explored_nodes(self, grid, explored_nodes, path=None):
        maze_copy = [row[:] for row in grid] # makes a copy of the maze to prevent effecting the original

        # marks all explored nodes with "*"
        # but never replaces the S or E 
        for r, c in explored_nodes:
            if maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "*"

        # if final path exists, mark it with "."
        # overwriting any "*" for path cells
        if path:
            for r, c in path:
                if maze_copy[r][c] not in ("S", "E"):
                    maze_copy[r][c] = "."
        # prints the maze with explored nodes and final path together
        print("Explored Nodes + Final Path:")
        self.display_maze(maze_copy)

    def display_explored_only(self, grid, explored_nodes, path):
        maze_copy = [row[:] for row in grid] # makes copy to not damage the original
        path_set = set(path) # converts path list to a set for quicker checking

        # marks explored nodes with "*"
        # but also doesn't mark the nodes that are part of final path
        for r, c in explored_nodes:
            if (r, c) not in path_set and maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "*"

        print("Explored Nodes ONLY:") # print maze showing only explored nodes
        self.display_maze(maze_copy)

    def display_solution(self, grid, path):
        maze_copy = [row[:] for row in grid] # makes copy so original is not damaged

        # marks the final path with "."
        # leaves the start and end symbols
        for r, c in path:
            if maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "."

        print("Final Path:") # prints the maze showing only final path
        self.display_maze(maze_copy)
        
    # prints the stats for one algorithm
    def display_stats(self, result):
        print("\nStatistics:")
        print(f"Algorithm: {result['algorithm']}")
        print(f"Path Positions: {len(result['path'])}")
        print(f"Path Length: {result['path_length']}")
        print(f"Nodes Explored: {result['nodes_explored']}")
        print(f"Runtime: {result['runtime']:.6f} seconds")
    # prints a summary table comparing all algorithms
    def display_comparison_summary(self, results):
        print("\n" + "=" * 60)
        print("COMPARISON SUMMARY")
        print("=" * 60)
        # prints table headings
        print(f"{'Algorithm':<28}{'Path':<10}{'Nodes':<10}{'Runtime'}")
        print("-" * 60)

        # prints a row for each algorithms reults
        for r in results:
            print(
                f"{r['algorithm']:<28}"
                f"{r['path_length']:<10}"
                f"{r['nodes_explored']:<10}"
                f"{r['runtime']:.6f}s"
            )

        print("=" * 60)
