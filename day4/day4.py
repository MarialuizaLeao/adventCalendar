def find_direction(point1: tuple, point2: tuple) -> int:
    # 0: up, 1: down, 2: left, 3: right, 4: diagonal_left_down, 5: diagonal_right_down, 6: diagonal_left_up, 7: diagonal_right_down
    # If the points are in the same row
    if point1[0] == point2[0]:
        # If the second point is to the right of the first point
        if point1[1] > point2[1]:
            return 3
        else:
            return 4
    # If the points are in the same column
    elif point1[1] == point2[1]:
        # If the second point is below the first point
        if point1[0] > point2[0]:
            return 1
        else:
            return 0
    # If the second point is to the right of the first point
    elif point1[1] < point2[1]:
        # If the second point is below the first point
        if point1[0] < point2[0]:
            return 5
        else:
            return 7
    # If the second point is to the left of the first point
    else:
        # If the second point is below the first point
        if point1[0] < point2[0]:
            return 6
        else:
            return 2  

def next(letter: str) -> str:
    if letter == "X":
        return "M"
    elif letter == "M":
        return "A"
    elif letter == "A":
        return "S"

def valid_direction(point1: tuple, point2: tuple, direction: int) -> bool:
    if direction == -1:
        return True
    else:
        return find_direction(point1, point2) == direction

def find_adjacent(matrix: list, point: tuple, letter: str, dir) -> tuple:
    result = []
    for i in range(point[0] - 1, point[0] + 2):
        for j in range(point[1] - 1, point[1] + 2):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                continue
            if matrix[i][j] == letter:
                if valid_direction(point, (i,j), dir): result.append(((i, j),find_direction(point, (i,j))))
    return result

def part1(word: str, matrix: list) -> int:
    
    search_space = []
    results = set()
        
    # Find the coordinates of the first letter
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[0]:
                search_space.append((word[0],[(i, j)], -1))
                
    while len(search_space) > 0:
        prev_letter, point_list, dir = search_space.pop(0)
        next_letter = next(prev_letter)
        if len(point_list) == len(word):
            results.add((tuple(point_list),dir))
        adjacents = find_adjacent(matrix, point_list[-1], next_letter, dir)
        for adjacent in adjacents:
            search_space.append((next_letter, point_list + [adjacent[0]], adjacent[1]))
            
    return results

def part2(matrix: list) -> int:
    word_occurrences = part1("MAS", matrix)
    
    diagonal_word_occurrences = list()
    results = list()

    # Remove non diagonal results
    for word_occurrence in word_occurrences:
        if word_occurrence[1] not in [0,1,4,3]:
            diagonal_word_occurrences.append(word_occurrence)
            
    for i in range(len(diagonal_word_occurrences)):
        for j in range(i+1, len(diagonal_word_occurrences)):
            if diagonal_word_occurrences[i][0][1] == diagonal_word_occurrences[j][0][1]:
                results.append((diagonal_word_occurrences[i],diagonal_word_occurrences[j]))
                
    return len(results)

def main():
    matrix = []

    with open("./input.txt") as f:   # Open the file
        lines = f.readlines()   # Read the lines
    
    for line in lines:
        matrix.append(list(line.strip()))
    
    print(f"Part 1: {len(part1("XMAS", matrix))}")
    print(f"Part 1: {part2(matrix)}")


if __name__ == "__main__":
    main()