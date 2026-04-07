from maze import Maze
from solver import Solver
from terminalOutput import TerminalOutput


def choose_maze():
    maze_files = [
        "mazes/maze1.txt",
        "mazes/maze2.txt",
        "mazes/maze3.txt",
        "mazes/maze4.txt"
    ]

    print("Available Mazes:")
    for i, maze_file in enumerate(maze_files, start=1):
        print(f"{i}. {maze_file}")

    while True:
        choice = input("\nSelect a maze by number: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(maze_files):
                return maze_files[choice - 1]

        print("Invalid choice. Please try again.")


def main():
    maze_file = choose_maze()
    print(f"\nSelected Maze: {maze_file}")

    maze = Maze(maze_file)
    output = TerminalOutput()
    solver = Solver(maze)

    print("\nOriginal Maze:")
    output.display_maze(maze.grid)

    results = [
        solver.bfs(),
        solver.greedy(),
        solver.astar()
    ]

    for result in results:
        print(f"\n{result['algorithm']} Results:")

        if result["path_found"]:
            output.display_explored_nodes(
                maze.grid,
                result["explored_nodes"],
                result["path"]
            )
            print()

            output.display_explored_only(
                maze.grid,
                result["explored_nodes"],
                result["path"]
            )
            print()

            output.display_solution(maze.grid, result["path"])
            output.display_stats(result)
        else:
            print("No path found.")
            output.display_explored_nodes(
                maze.grid,
                result["explored_nodes"]
            )
            output.display_stats(result)

    output.display_comparison_summary(results)


if __name__ == "__main__":
    main()