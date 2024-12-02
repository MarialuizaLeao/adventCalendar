def part_1(col_1: list, col_2: list) -> int:
    frequecy = {}   # Initialize the frequency dictionary
    result = 0   # Initialize the result

    for i in range(len(col_1)):
        if col_2[i] in frequecy:
            frequecy[col_2[i]] += 1   # Increment the frequency
        else:
            frequecy[col_2[i]] = 1   # Initialize the frequency

    for number in col_1:
        if str(number) not in frequecy:
            multiplier = 0
        else:
            multiplier = frequecy[str(number)]
        result = result + ( int(number) * multiplier )   # Calculate the result
    return result

def part_2(col_1: list, col_2: list) -> int:
    col_1.sort()   # Sort the first column
    col_2.sort()   # Sort the second column
    diff = 0   # Initialize the difference
    for i in range(len(col_1)):
        diff += abs(int(col_1[i]) - int(col_2[i]))
    return diff

def main():
    col_1 = []
    col_2 = []

    with open("./input.txt") as f:   # Open the file
        lines = f.readlines()   # Read the lines

    # Loop through the lines
    for line in lines:
        col_1.append(line.split()[0])   # Append the first column to col_1
        col_2.append(line.split()[1])   # Append the second column to col_2

    print("Part 1: ", part_1(col_1, col_2))   # Print the result of part 1
    print("Part 2: ", part_2(col_1, col_2))   # Print the result of part 2

if __name__ == "__main__":
    main()