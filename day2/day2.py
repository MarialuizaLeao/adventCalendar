def is_safe(input: list, can_remove_item=False) -> tuple:
    # Check if list is all increasing or decreasing
    result = (0,0)
    if all((x < y and abs(x-y) >= 1 and abs(x-y) <= 3) for x, y in zip(input, input[1:])) or all((x > y  and abs(x-y) >= 1 and abs(x-y) <= 3) for x, y in zip(input, input[1:])):
        return (1,1)
    else:
        for i in range(len(input)):
            temp = input.copy()
            temp.pop(i)
            if all((x < y and abs(x-y) >= 1 and abs(x-y) <= 3) for x, y in zip(temp, temp[1:])) or all((x > y  and abs(x-y) >= 1 and abs(x-y) <= 3) for x, y in zip(temp, temp[1:])):
                return (0,1)
    return (0,0)

def main():
    with open("./input.txt") as f:   # Open the file
        lines = f.readlines()   # Read the lines

    safe_part_1 = 0   # Initialize the safe variable
    safe_part_2 = 0   # Initialize the safe variable

    for line in lines:
        line = line.split()   # Split the line
        out1, out2 = is_safe([int(x) for x in line])
        safe_part_1 += out1
        safe_part_2 += out2
            
    print(f"Part 1: {safe_part_1}")   # Print safe
    print(f"Part 2: {safe_part_2}")   # Print safe

if __name__ == "__main__":
    main()

            