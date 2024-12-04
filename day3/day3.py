import re

def part1(line: str) -> int:
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    result = 0
    for match in matches:
        numbers = re.findall(r'[0-9]{1,3}', match)
        result += int(numbers[0]) * int(numbers[1])
    return result

def part2(filename: str) -> int:

    with open(filename) as f:   # Open the file
        lines = f.readlines()   # Read the lines
        
    result = 0
    enabled = True
    
    for line in lines:

        while len(line) > 0:
            
            dont = re.search("don't\(\)", line)
            do = re.search("do\(\)", line)
            
            if dont is None and do is None:
                if enabled: result += part1(line)
                line = ""
            # If only has do
            elif dont is None:
                if enabled: result += part1(line[: do.span()[0]])
                line = line[do.span()[1]:]
                enabled = True
            # If only has don't
            elif do is None:
                if enabled: result += part1(line[: dont.span()[0]])
                line = line[dont.span()[1]:]
                enabled = False
            else:
                # If do comes before don't
                if do.span()[0] < dont.span()[0]:
                    if enabled: result += part1(line[: do.span()[0]])
                    result += part1(line[do.span()[1]: dont.span()[0]])
                    line = line[dont.span()[1]:]
                    enabled = False
                # If don't comes before do
                else:
                    if enabled: result += part1(line[: dont.span()[0]])
                    
                    line = line[do.span()[1]:]
                    enabled = True
        
    return result

def test(filename: str, expected: int):
    result = part2(filename)
    assert result == expected, f"Result for test {filename} was {result} but the expected value is {expected}"

def main():
    
    with open("input.txt") as f:   # Open the file
        lines = f.readlines()   # Read the lines
    result = 0
    for line in lines:
        result += part1(line)
    print(f"Part 1: {result}")
    
    test("test.txt",48)  
    test("line_1.txt",8621928)
    test("line_2.txt",17778504)
    test("line_3.txt",15995726)
    test("line_4.txt",11538422)
    test("test_2.txt",26400432)
    print(f"Part 2: {part2("input.txt")}") 

            
if __name__ == "__main__":
    main()