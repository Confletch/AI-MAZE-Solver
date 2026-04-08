from maze import Maze
from solver import Solver
from terminalOutput import TerminalOutput


def choose_maze():
    # maze files which the user can pick from for running the search methods
    maze_files = [
        "mazes/maze1.txt",
        "mazes/maze2.txt",
        "mazes/maze3.txt",
        "mazes/maze4.txt"
    ]

    # provides the list of mazes the user can choose from
    # and take's their input (must be a valid choice)
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

    maze = Maze(maze_file) # creates the maze object
    output = TerminalOutput() # creates an object to handle printing the maze and results
    solver = Solver(maze) # creates the solver object

    # prints the origional maze before solving
    # just so the user can see a nice before and after
    print("\nOriginal Maze:")
    output.display_maze(maze.grid)

    # runs all three search algorithms and stores each result
    results = [
        solver.bfs(),
        solver.greedy(),
        solver.astar()
    ]

    # goes through each search algorithms results
    for result in results:
        print(f"\n{result['algorithm']} Results:")

        # if path was found, shows the explored nodes, final path, and stats from search
        if result["path_found"]:
            output.display_explored_nodes(
                maze.grid,
                result["explored_nodes"],
                result["path"]
            )
            print()

            # shows the explored nodes
            output.display_explored_only(
                maze.grid,
                result["explored_nodes"],
                result["path"]
            )
            print()

            output.display_solution(maze.grid, result["path"]) # shows the final path only
            output.display_stats(result) # shows the stats from the algorithm
        else:
            # shows if there was no found path
            # still shows the explored nodes just no path
            print("No path found.")
            output.display_explored_nodes(
                maze.grid,
                result["explored_nodes"]
            )
            output.display_stats(result) # still shows the stats from search

    # simple summary table to show comparision of all three algorithms
    output.display_comparison_summary(results)

if __name__ == "__main__":
    main()
