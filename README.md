# Route Planner
Route Planner Project using A* algorithm, Udacity Data Structures and Algorithms Nanodegrees.


## A * algorithm
This Route planner was built based on A star algorithm, that is a mix of 2 other algorithms
- Uniform Cost Search
- Best First Search

The Graph is denoted as M through the notebook:

- Graph representation used here is adjacency lists
- M.intersections: contains the list of nodes as x,y positions
- M.roads: contains a list of the adjacencies of each node

Graph visualization example:
<img src="images/graph.png" height="500"/>


Our Node consist of the following fields
```python3
def __init__(self, vertex, coords, distance = 0, prev_vertex = None):
    self.vertex = vertex
    self.coords = coords
    self.start_distance = distance
    self.heuristic = 0
    self.f_value = 0
    self.prev_vertex = prev_vertex
```
- Vertex: id [0, len(graph)]
- coords: x, y positions
- start_distance = the distance traveled by the node from start, being for the start node 0
- heuristic = h function result
- f_value = f_value function result
- previous_vertex = as in Dijkstras you get the prev_vertex and when you get the goal re build it back to the start node.

The heuristic function built is pretty simple, just the distance between two points.
```python3
h = lambda a, b: sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
``` 

The f value function as should be, the distance traveled plus the heuristic of the node
```python3
def f_value(total_weight, v_coord, g_coord):
    heuristic = h(v_coord, g_coord)
    return total_weight + heuristic
```


Shortest Path function:
```python3
def shortest_path(M, start, goal):
    g_coords = M.intersections[goal]
    
    open_v, closed_v = {}, {}
    current, node = init(start, M.intersections[start], g_coords)
    
    while current is not goal:
        for vertex in M.roads[current]:
            if closed_v.get(vertex) is not None: continue
                
            v_open_node = open_v.get(vertex, None) 
            new_node = get_new_node(node, vertex, M.intersections[vertex], g_coords)
            
            if v_open_node is None or new_node.f_value < v_open_node.f_value:
                open_v[vertex] = new_node
        
        current, node = update_defaults(node, open_v, closed_v, current)
    closed_v[current] = node
    
    return build_from_closed(goal, closed_v)
```

The previous function returns a list with the path traveled

### Example:
```python3
def display_shortest_path(start, goal):
    path = shortest_path(map_40, start, goal)
    print(path)
    show_map(map_40, start=start, goal=goal, path=path)

display_shortest_path(5, 3)
```

<img src="images/path.png" alt="Path from 5 to 3 node" height="500"/>
