class TerminalOutput:
    def display_maze(self, grid):
        for row in grid:
            print("".join(row))

    def display_explored_nodes(self, grid, explored_nodes, path=None):
        maze_copy = [row[:] for row in grid]

        for r, c in explored_nodes:
            if maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "*"

        if path:
            for r, c in path:
                if maze_copy[r][c] not in ("S", "E"):
                    maze_copy[r][c] = "."

        print("Explored Nodes + Final Path:")
        self.display_maze(maze_copy)

    def display_explored_only(self, grid, explored_nodes, path):
        maze_copy = [row[:] for row in grid]
        path_set = set(path)

        for r, c in explored_nodes:
            if (r, c) not in path_set and maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "*"

        print("Explored Nodes ONLY:")
        self.display_maze(maze_copy)

    def display_solution(self, grid, path):
        maze_copy = [row[:] for row in grid]

        for r, c in path:
            if maze_copy[r][c] not in ("S", "E"):
                maze_copy[r][c] = "."

        print("Final Path:")
        self.display_maze(maze_copy)

    def display_stats(self, result):
        print("\nStatistics:")
        print(f"Algorithm: {result['algorithm']}")
        print(f"Path Positions: {len(result['path'])}")
        print(f"Path Length: {result['path_length']}")
        print(f"Nodes Explored: {result['nodes_explored']}")
        print(f"Runtime: {result['runtime']:.6f} seconds")

    def display_comparison_summary(self, results):
        print("\n" + "=" * 60)
        print("COMPARISON SUMMARY")
        print("=" * 60)

        print(f"{'Algorithm':<28}{'Path':<10}{'Nodes':<10}{'Runtime'}")
        print("-" * 60)

        for r in results:
            print(
                f"{r['algorithm']:<28}"
                f"{r['path_length']:<10}"
                f"{r['nodes_explored']:<10}"
                f"{r['runtime']:.6f}s"
            )

        print("=" * 60)