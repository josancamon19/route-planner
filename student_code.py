from node import Node, f_value, h

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

def init(start, coords, g_coords):
    node = Node(start, coords , 0)
    node.config(g_coords)
    return start, node

def get_new_node(node, v, v_coords, g_coords):
    v_distance = node.start_distance + h(v_coords, node.coords)
    new_node = Node(v, v_coords, v_distance, node.vertex)
    new_node.config(g_coords)
    return new_node

def update_defaults(node, opened, closed, current):
    closed[current] = node
    new_current = min(opened, key = lambda i: opened[i].f_value)
    new_node = opened[new_current]
    del opened[new_current]
    return new_current, new_node

def build_from_closed(goal, closed):
    path = [goal]
    previous = closed[goal].prev_vertex
    while previous:
        path.append(previous)
        previous = closed[previous].prev_vertex
    return list(reversed(path))
    
