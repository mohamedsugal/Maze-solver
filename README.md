# Maze-solver
This repository contains code for finding a path in a maze using the BFS & DFS algorithms. I used Pillow image processing library to draw the path and display it. 

<img width="1118" alt="maze_res" src="https://user-images.githubusercontent.com/32971892/161399657-bc3d9fd9-be26-45da-8394-adcc66e44897.png">

### How to run the code 
1. Clone the repository.
2. Install Pillow. Below command can be used for macOS, Linux, & Windows
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
or visited Pillow website from this [Pillow install](https://pillow.readthedocs.io/en/stable/installation.html).
3. run the program 
```
python3 maze.py
```
4. Pillow will displays two images. First image is the path BFS took to find the ending point, and second image is the path DFS took to find the ending point. 

### BFS (Breadth First Search) Algorithm
```python
def BFS(start):
  visited = set([start])
  queue = collections.deque([start])
  
  while queue:
    v = queue.popleft()
    for w in self.graph[v]:
      if w not in visited:
        visited.add(w)
        queue.append(w)
```

### DFS (Depth First Search) Algorithm
#### Recursive implementation
```python
def dfs_util(n: int):
  visited = set()
  
  def dfs(adjacency, i: int) -> None:
    visited.add(i)
    for neighbor in adjacency[i]:
      if neighbor not in visited:
        dfs(neighbor)
  
  for i in range(n):
    if i not in visited:
      dfs(i)
```
#### Iterative implementation
```python
def dfs(start):
  visited = set([start])
  stack = [start]
  
  while stack:
    v = stack.pop()
    if v in visited:
      continue
    visited.add(v)
    for w in self.graph[v]:
      if w not in visited:
        stack.append(w)
        stack.append(w)
```
