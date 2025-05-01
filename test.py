import math
from collections import defaultdict

def parse_segments(data):
    n = int(data[0])
    segments = []
    for i in range(1, n + 1):
        x1, y1, x2, y2 = map(int, data[i].split())
        segments.append(((x1, y1), (x2, y2)))
    return segments

def angle(origin, point):
    """Return angle from origin to point, in radians."""
    dx, dy = point[0] - origin[0], point[1] - origin[1]
    return math.atan2(dy, dx)

def build_ordered_graph(segments):
    graph = defaultdict(list)
    edges = set()
    for a, b in segments:
        graph[a].append(b)
        graph[b].append(a)
        edges.add((a, b))
        edges.add((b, a))  # for directed edges
    # Sort neighbors counterclockwise by angle for each node
    for node in graph:
        graph[node].sort(key=lambda pt: angle(node, pt))
    return graph, edges

def next_ccw_neighbor(graph, current, previous):
    """Find the next vertex counterclockwise from previous around current."""
    neighbors = graph[current]
    if previous not in neighbors:
        return None
    idx = neighbors.index(previous)
    return neighbors[(idx - 1) % len(neighbors)]

def trace_face(graph, used_edges, start, next_node):
    face = [start]
    current, previous = start, next_node
    while True:
        face.append(previous)
        used_edges.add((current, previous))
        next_node = next_ccw_neighbor(graph, previous, current)
        if next_node is None or next_node == start:
            break
        current, previous = previous, next_node
    if face[0] == face[-1] and len(face) >= 4:
        return face[:-1]  # remove duplicated last
    return None

def find_faces(graph, all_edges):
    used_edges = set()
    faces = []
    for a, neighbors in graph.items():
        for b in neighbors:
            if (a, b) not in used_edges:
                face = trace_face(graph, used_edges, a, b)
                if face:
                    norm = normalize_cycle(face)
                    if norm not in faces:
                        faces.append(norm)
    return faces

def normalize_cycle(cycle):
    """Normalize cycle to prevent duplicates (rotate & reverse)"""
    n = len(cycle)
    rots = [tuple(cycle[i:] + cycle[:i]) for i in range(n)]
    revs = [tuple(reversed(c)) for c in rots]
    return min(rots + revs)

def polygon_area(poly):
    area = 0.0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

# === Input Example ===
raw_data = [
    "6",
    "0 0 0 1",
    "0 1 1 1",
    "0 0 1 0",
    "1 0 2 0",
    "1 1 2 0",
    "1 0 1 1"
]

segments = parse_segments(raw_data)
graph, edge_set = build_ordered_graph(segments)
faces = find_faces(graph, edge_set)

areas = [polygon_area(face) for face in faces]
squared_sum = sum(area**2 for area in areas)

# === Output ===
print("Polygons found:")
for i, face in enumerate(faces):
    print(f"Polygon {i+1}: {list(face)} | Area: {areas[i]}")

print(f"\nSum of squared areas: {squared_sum}")