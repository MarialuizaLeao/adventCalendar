get_opposite_direction = {
    "vertical up": "vertical down",
    "vertical down": "vertical up",
    "horizontal right": "horizontal left",
    "horizontal left": "horizontal right",
    "right_diagonal_up": "left_diagonal_down",
    "right_diagonal_down": "left_diagonal_up",
    "left_diagonal_up": "right_diagonal_down",
    "left_diagonal_down": "right_diagonal_up"
}

get_direction_operation = {
    "vertical up": (-1, 0),
    "vertical down": (1, 0),
    "horizontal right": (0, 1),
    "horizontal left": (0, -1),
    "right_diagonal_up": (-1, 1),
    "right_diagonal_down": (1, 1),
    "left_diagonal_up": (-1, -1),
    "left_diagonal_down": (1, -1)
}

def get_antennas_dirrection(antenna1: tuple, antenna2: tuple) -> str:
    if antenna1[0] == antenna2[0]:
        if antenna1[1] < antenna2[1]:
            return "horizontal right"
        return "horizontal"
    if antenna1[1] == antenna2[1]:
        if antenna1[0] < antenna2[0]:
            return "vertical down"
        return "vertical up"
    if antenna1[0] < antenna2[0] and antenna1[1] < antenna2[1]:
        return "right_diagonal_down"
    if antenna1[0] > antenna2[0] and antenna1[1] < antenna2[1]:
        return "right_diagonal_up"
    if antenna1[0] < antenna2[0] and antenna1[1] > antenna2[1]:
        return "left_diagonal_down"
    if antenna1[0] > antenna2[0] and antenna1[1] > antenna2[1]:
        return "left_diagonal_up"

def are_antennas_in_line(antenna1: tuple, antenna2: tuple) -> bool:
    if antenna1[0] == antenna2[0] or antenna1[1] == antenna2[1] or (antenna1[0] < antenna2[0] and antenna1[1] < antenna2[1]) or (antenna1[0] < antenna2[0] and antenna1[1] > antenna2[1]):
        return True
    return False

def get_antennas_distance(antenna1: tuple, antenna2: tuple) -> tuple:
    return abs(antenna1[0] - antenna2[0]), abs(antenna1[1] - antenna2[1])

def is_in_map(point: tuple, map_dimensions: tuple) -> bool:
    if point[0] >= 0 and point[0] < map_dimensions[0] and point[1] >= 0 and point[1] < map_dimensions[1]:
        return True
    return False

def get_next_point(point: tuple, distance: tuple, direction: str) -> tuple:
    multipliers = get_direction_operation[direction]
    return (point[0] + multipliers[0] * distance[0], point[1] + multipliers[1] * distance[1])

def get_antinodes_pt2(antenna1: tuple,antenna2: tuple, direction: str, distance: tuple, map_dimensions: tuple) -> set:
    result = set()
    point = get_next_point(antenna1, distance, direction)
    while is_in_map(point, map_dimensions):
        result.add(point)
        point = get_next_point((point[0],point[1]), distance, direction)
    opposite_direction = get_opposite_direction[direction]
    point = get_next_point(antenna1, distance, opposite_direction)
    while is_in_map(point, map_dimensions):
        result.add(point)
        point = get_next_point(point, distance, opposite_direction)
    point = get_next_point(antenna2, distance, direction)
    while is_in_map(point, map_dimensions):
        result.add(point)
        point = get_next_point((point[0],point[1]), distance, direction)
    opposite_direction = get_opposite_direction[direction]
    point = get_next_point(antenna2, distance, opposite_direction)
    while is_in_map(point, map_dimensions):
        result.add(point)
        point = get_next_point(point, distance, opposite_direction)
    return result
        
def get_antinodes_pt1(antenna1: tuple,antenna2: tuple, direction: str, distance: tuple, map_dimensions: tuple) -> set:
    result = set()
    point = get_next_point(antenna2, distance, direction)
    if is_in_map(point, map_dimensions):
        result.add(point)
    opposite_direction = get_opposite_direction[direction]
    point = get_next_point(antenna1, distance, opposite_direction)
    if is_in_map(point, map_dimensions):
        result.add(point)
    return result

def get_all_antinodes(antenna1: tuple, antenna2: tuple, pt: int, map_dimensions) -> tuple:
    distance_in_line, distance_in_column = get_antennas_distance(antenna1, antenna2)
    direction = get_antennas_dirrection(antenna1, antenna2)
    if pt == 1:
        return get_antinodes_pt1(antenna1, antenna2, direction, (distance_in_line, distance_in_column), map_dimensions)
    return get_antinodes_pt2(antenna1, antenna2, direction, (distance_in_line, distance_in_column), map_dimensions)

def get_antennas_antinodes(antennas: list, map_dimensions: tuple, pt: int) -> int:
    valid_antinodes = set()
    checked_antennas = set()
    for antenna in antennas:
        for other_antenna in antennas:
            if antenna == other_antenna or (antenna, other_antenna) in checked_antennas or (other_antenna, antenna) in checked_antennas:
                continue
            if are_antennas_in_line(antenna, other_antenna):
                all_antinode = get_all_antinodes(antenna, other_antenna, pt, map_dimensions)
                for antinode in all_antinode:
                    valid_antinodes.add(antinode)
            checked_antennas.add((antenna, other_antenna))
                        
    return valid_antinodes

def solve(filename: str, pt: int) -> int:
    antennas, map_dimensions = get_input(filename)
    without_repeated_antinodes = set()
    for frequency in antennas:
        antinodes  =  get_antennas_antinodes(antennas[frequency], map_dimensions, pt)
        for antinode in antinodes:
            without_repeated_antinodes.add(antinode)
    return len(without_repeated_antinodes)        

def get_input(filename: str) -> tuple:
    with open(filename) as f:   # Open the file
        lines = f.readlines()
        
    antennas = dict()
     
    i = 0 # Line number
    for line in lines:
        line = line.strip()
        j = 0 # Column number
        for char in line:
            if char == ".":  # Skip the dots
                j += 1
                continue
            if char in antennas:
                antennas[char].append((i, j))  # The points are represented as (line, column)
            else:
                antennas[char] = [(i, j)]
            j += 1
        i += 1
        
    return antennas, (i, j)

def main():
    
    assert solve("test.txt",1) == 2
    assert solve("test2.txt",1) == 4
    assert solve("test3.txt",1) == 4
    assert solve("test1.txt",1) == 14
    print(f"Part 1: {solve("input.txt",1)}")
    assert(solve("test4.txt",2) == 9)
    assert(solve("test1.txt",2) == 34)
    print(f"Part 2: {solve("input.txt",2)}")
    
if __name__ == "__main__":
    main()