import collections
from typing import List, Tuple, Set
from PIL import Image, ImageDraw
import time


def read_maze_from_file(f):
    maze = list()
    with open(f) as file:
        for line in file:
            maze.append(list(line.rstrip()))
    return maze


def print_maze(maze: List[str]) -> None:
    for row in maze:
        for cell in row:
            print(cell, end=" ")
        print()


def BFS(maze: List[str], start: Tuple, end: Tuple) -> List[Tuple]:
    queue = collections.deque([start])
    visited, path = set(), []
    while queue:
        path = [queue.popleft()] if queue[0] == start else queue.popleft()
        front = path[-1]
        if front == end:
            return path
        # Get all the legal adjacent cells
        for adj in get_adjacent(maze, front, visited):
            new_path = list(path)
            new_path.append(adj)
            queue.append(new_path)
            visited.add(front)
    return path

def DFS(maze, start, end):
    stack = [start]
    visited = set()
    while stack: 
        path = [stack.pop()] if stack[-1] == start else stack.pop()
        front = path[-1]
        if front in visited: 
            continue
        if front == end: 
            return path
        visited.add(front)
        for adj in get_adjacent(maze, front, visited):
            new_path = list(path)
            new_path.append(adj)
            stack.append(new_path)
    return path
    


def get_adjacent(maze: List[str], cell: Tuple, visited: Set) -> List[Tuple]:
    rows, cols = len(maze), len(maze[0])
    adjacent = []
    for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        r, c = cell[0] + direction[0], cell[1] + direction[1]
        if r < 0 or c < 0 or r == rows or c == cols or \
                (r, c) in visited or maze[r][c] == "#":
            continue
        adjacent.append((r, c))
    return adjacent


def find_points(maze: List[str]) -> List[Tuple]:
    points = []
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                points.append((r, c))
            if maze[r][c] == 'E':
                points.append((r, c))
    return points


def print_path(maze: List[str], path: List[Tuple]) -> None:
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) in path and maze[r][c] != 'S' and maze[r][c] != 'E':
                print("+", end=" ")
            else:
                print(maze[r][c], end=" ")
        print()

def draw_maze(maze: List[str], file, start: Tuple, end: Tuple) -> None:
    cell_size = 50
    cell_border = 2
    img = Image.new("RGBA", (len(maze[0]) * cell_size, len(maze) * cell_size), "black")
    draw = ImageDraw.Draw(img)

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) == start:
                fill = (255, 0, 0)
            elif (r, c) == end:
                fill = (0, 0, 255)
            elif maze[r][c] == "#":
                fill = (25,25,112)
            else:
                fill = (212, 97, 85)
            draw.rectangle(
                ([(c * cell_size + cell_border, r * cell_size + cell_border),
                  ((c + 1) * cell_size - cell_border, (r + 1) * cell_size - cell_border)]),
                fill=fill
            )
    img.save(file)


def draw_path(maze: List[str], path: List[Tuple], file: str, start: Tuple, end: Tuple) -> None:
    cell_size = 50
    cell_border = 2
    img = Image.new("RGBA", (len(maze[0]) * cell_size, len(maze) * cell_size), "black")
    draw = ImageDraw.Draw(img)

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) == start:
                fill = (255, 0, 0)
            elif (r, c) == end:
                fill = (0, 0, 255)
            elif maze[r][c] == "#":
                fill = (13, 30, 68)
            elif (r, c) in path and (r, c) != start and (r, c) != end:
                fill = (200, 235, 113)
            else:
                fill = (212, 97, 85)
            draw.rectangle(
                ([(c * cell_size + cell_border, r * cell_size + cell_border),
                  ((c + 1) * cell_size - cell_border, (r + 1) * cell_size - cell_border)]),
                fill=fill
            )
    img.save(file)


if __name__ == "__main__":
    maze = read_maze_from_file('./mazes/maze4.txt')
    point = find_points(maze)
    
    bfs_start_time = time.time()
    bfs_path = BFS(maze, point[0], point[1])        
    bfs_end_time = time.time()
    
    dfs_start_time = time.time()
    dfs_path = DFS(maze, point[0], point[1])
    dfs_end_time = time.time()
    
    print("BFS distance:", len(bfs_path))
    print("Time taken:", bfs_end_time-bfs_start_time, "secs")
    
    print("DFS distance:", len(dfs_path))
    print("Time taken:", dfs_end_time-dfs_start_time, "secs")

    draw_path(maze, bfs_path, "bfs_maze.png", point[0], point[1])
    image = Image.open('bfs_maze.png')
    image.show(title="BFS")

    time.sleep(1)

    draw_path(maze, dfs_path, "dfs_maze.png", point[0], point[1])
    image = Image.open('dfs_maze.png')
    image.show(title="DFS")
    
