import time
import heapq
from collections import deque


class Solver:
    def __init__(self, maze):
        self.maze = maze # stores the maze object so the solver can use it

    # BFS Section
    def bfs(self):
        start_time = time.perf_counter() # start timer for bfs
        # get the start and end position of the maze
        start = self.maze.start
        end = self.maze.end

        queue = deque([start]) # bfs starts adding the start position to queue
        visited = {start} # tracks visited positions so no repeates
        
        # helps store where each node came from
        # so later it can help with rebuilding once path is found
        came_from = {}
        explored_nodes = [] # stores the order of the explored nodes

        # continues until there are no more nodes left in queue
        while queue:
            current = queue.popleft() # removes first node from queue
            explored_nodes.append(current) # adds it to explored list

            # once the end is reached rebuild the path and return results
            if current == end:
                path = self.reconstruct_path(came_from, start, end)
                return self.build_result("BFS", path, explored_nodes, start_time)

            # check all valid neighboring positions
            for neighbor in self.get_neighbors(current):
                # only processes a neighbor if it has not yet been visited
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

        # if loop ends without finding the end, return failed results
        return self.fail_result("BFS", explored_nodes, start_time)


    # GREEDY Section
    def greedy(self):
        start_time = time.perf_counter() # start timer for greedy
        # get the start and end position of the maze
        start = self.maze.start
        end = self.maze.end

        # greedy uses a priority queue
        # the node with the lowest heuristic value will be explored
        pq = []
        heapq.heappush(pq, (self.heuristic(start, end), start))

        visited = {start} # keeps track of visited positions
        came_from = {} # stores the parent of each node for reconstructing the path
        explored_nodes = [] # stores all explored nodes

        # continues while nodes are still in the priority queue
        while pq:
            _, current = heapq.heappop(pq) # pop node with smallest heuristic value
            explored_nodes.append(current) # add it to explored list

            # if node is the end, rebuild and return the path
            if current == end:
                path = self.reconstruct_path(came_from, start, end)
                return self.build_result("Greedy Best-First Search", path, explored_nodes, start_time)

            # check all neighboring positions that are valid
            for neighbor in self.get_neighbors(current):
                # only adds neighbors that haven't been visited
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    heapq.heappush(pq, (self.heuristic(neighbor, end), neighbor)) # use heuristic as the priority

        # if no solution is found, return failed results
        return self.fail_result("Greedy Best-First Search", explored_nodes, start_time)

        # A* Section
    def astar(self):
        start_time = time.perf_counter() # start timer for A*
        # get the start and end position of the maze
        start = self.maze.start
        end = self.maze.end

        pq = [] # A* uses priority queue
        heapq.heappush(pq, (0, start))

        came_from = {} # store parent relationships for path reconstruction
        g_score = {start: 0} # g_score stores the cost from the start node to each node
        visited = set() # tracks nodes that have already been fully processed
        explored_nodes = [] # stores all explored nodes

        # continues until priority queue is empty
        while pq:
            _, current = heapq.heappop(pq) # remove node with smallest f-score

            # if this node was already processed,, skip it
            if current in visited:
                continue

            visited.add(current) # mark node as visited
            explored_nodes.append(current) # add it to explored nodes list

            # if current node is the end, rebuild and return the path
            if current == end:
                path = self.reconstruct_path(came_from, start, end)
                return self.build_result("A* Search", path, explored_nodes, start_time)

            # check all neighboring positions
            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1 # since moves cost 1,, add 1 to current g-score

                # update neighbor if it is new
                # or if the path is better than a previous one
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    came_from[neighbor] = current
                    f_score = tentative_g + self.heuristic(neighbor, end) # f_score is g_score + heuristic
                    heapq.heappush(pq, (f_score, neighbor)) # add neighbor to the priority queue

        # if end isn't reached, return failure results
        return self.fail_result("A* Search", explored_nodes, start_time)

        # build and return dictionary containing sucessful search results
    def build_result(self, name, path, explored, start_time):
        return {
            "algorithm": name,
            "path_found": True,
            "path": path,
            "path_length": len(path) - 1,
            "nodes_explored": len(explored),
            "explored_nodes": explored,
            "runtime": time.perf_counter() - start_time
        }

    # build and return dictionary for failed search attempts
    def fail_result(self, name, explored, start_time):
        return {
            "algorithm": name,
            "path_found": False,
            "path": [],
            "path_length": 0,
            "nodes_explored": len(explored),
            "explored_nodes": explored,
            "runtime": time.perf_counter() - start_time
        }

    def heuristic(self, a, b):
        # uses Manhattan distance:
        # row difference + column difference
        # estimates how far one point is from another
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, pos):
        r, c = pos # seperate curr position into row and column
        # these are the four possible movement directions:
        # up, down, left, right
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = [] # stores valid neighboring positions here

        # try each direction
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # only add position if a valid move
            if self.is_valid_move(nr, nc):
                neighbors.append((nr, nc))
        # return all valid neighbors
        return neighbors

    def is_valid_move(self, r, c):
        # get maze directions
        rows = len(self.maze.grid)
        cols = len(self.maze.grid[0])
    # makes sure the position is within maze boundaries
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        # return True if cell is not a wall
        return self.maze.grid[r][c] != "#"

    def reconstruct_path(self, came_from, start, end):
        path = [] # list stores final path
        current = end # start at end position

        # move backwords through the came_from dictionary
        # until the start is reached
        while current != start:
            path.append(current)
            current = came_from[current]

        path.append(start) # add start position
        path.reverse() # reverse list so it goes from start to end
        return path
