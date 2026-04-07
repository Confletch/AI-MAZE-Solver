import time
import heapq
from collections import deque


class Solver:
    def __init__(self, maze):
        self.maze = maze

    def bfs(self):
        start_time = time.perf_counter()

        start = self.maze.start
        end = self.maze.end

        queue = deque([start])
        visited = {start}
        came_from = {}
        explored_nodes = []

        while queue:
            current = queue.popleft()
            explored_nodes.append(current)

            if current == end:
                path = self.reconstruct_path(came_from, start, end)
                return self.build_result("BFS", path, explored_nodes, start_time)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return self.fail_result("BFS", explored_nodes, start_time)

    def greedy(self):
        start_time = time.perf_counter()

        start = self.maze.start
        end = self.maze.end

        pq = []
        heapq.heappush(pq, (self.heuristic(start, end), start))

        visited = {start}
        came_from = {}
        explored_nodes = []

        while pq:
            _, current = heapq.heappop(pq)
            explored_nodes.append(current)

            if current == end:
                path = self.reconstruct_path(came_from, start, end)
                return self.build_result("Greedy Best-First Search", path, explored_nodes, start_time)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    heapq.heappush(pq, (self.heuristic(neighbor, end), neighbor))

        return self.fail_result("Greedy Best-First Search", explored_nodes, start_time)

    def astar(self):
        start_time = time.perf_counter()

        start = self.maze.start
        end = self.maze.end

        pq = []
        heapq.heappush(pq, (0, start))

        came_from = {}
        g_score = {start: 0}
        visited = set()
        explored_nodes = []

        while pq:
            _, current = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)
            explored_nodes.append(current)

            if current == end:
                path = self.reconstruct_path(came_from, start, end)
                return self.build_result("A* Search", path, explored_nodes, start_time)

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    came_from[neighbor] = current
                    f_score = tentative_g + self.heuristic(neighbor, end)
                    heapq.heappush(pq, (f_score, neighbor))

        return self.fail_result("A* Search", explored_nodes, start_time)

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
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, pos):
        r, c = pos
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_valid_move(nr, nc):
                neighbors.append((nr, nc))

        return neighbors

    def is_valid_move(self, r, c):
        rows = len(self.maze.grid)
        cols = len(self.maze.grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        return self.maze.grid[r][c] != "#"

    def reconstruct_path(self, came_from, start, end):
        path = []
        current = end

        while current != start:
            path.append(current)
            current = came_from[current]

        path.append(start)
        path.reverse()
        return path