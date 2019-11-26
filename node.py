from math import sqrt


class Node:
    def __init__(self, vertex, coords, distance = 0, prev_vertex = None):
        self.vertex = vertex
        self.coords = coords
        self.start_distance = distance
        self.heuristic = 0
        self.f_value = 0
        self.prev_vertex = prev_vertex
        
    def config(self, g_coords):
        self.set_heuristic(g_coords)
        self.set_f_value(g_coords)
        
    def set_heuristic(self, g_coords):
        self.heuristic = h(self.coords, g_coords)
        
    def set_f_value(self, g_coords):
        self.f_value = f_value(self.start_distance, self.coords, g_coords)
        
    def __repr__(self):
        return '\nVertex: ' + str(self.vertex) + ', G_distance: ' + str(self.start_distance) + ', Heuristic: ' + str(self.heuristic) + ', F_value: ' + str(self.f_value)

        
def f_value(total_weight, v_coord, g_coord):
    heuristic = h(v_coord, g_coord)
    return total_weight + heuristic


def h(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)