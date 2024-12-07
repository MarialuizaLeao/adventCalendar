
def get_result(number1, number2, operation) -> int:
    if operation == "+":
        return number1 + number2
    elif operation == "*":
        return number1 * number2
    
def get_append_result(number1, number2) -> int:
    return int(str(number1) + str(number2))
    
def part1(input: dict) -> int:
    result = list()
    for key in input:
        numbers = input[key]
        to_try = []
        to_try.append(numbers)
        goal_result = key
        while len(to_try) > 0:
            numbers = to_try.pop(0)
            if len(numbers) == 2:
                sum = get_result(numbers[0], numbers[1], "+")
                multiplication = get_result(numbers[0], numbers[1], "*")
                if sum == goal_result or multiplication == goal_result:
                    result.append(key)
                    break
            else:
                sum = get_result(numbers[0], numbers[1], "+")
                multiplication = get_result(numbers[0], numbers[1], "*")
                to_try.append([sum] + numbers[2:])
                to_try.append([multiplication] + numbers[2:])
            
    return result

def part2(input: dict) -> int:
    result = list()
    for key in input:
        numbers = input[key]
        to_try = []
        to_try.append(numbers)
        goal_result = key
        while len(to_try) > 0:
            numbers = to_try.pop(0)
            if len(numbers) == 2:
                sum = get_result(numbers[0], numbers[1], "+")
                multiplication = get_result(numbers[0], numbers[1], "*")
                concatenation = get_append_result(numbers[0], numbers[1])
                if sum == goal_result or multiplication == goal_result or concatenation == goal_result:
                    result.append(key)
                    break
            else:
                sum = get_result(numbers[0], numbers[1], "+")
                multiplication = get_result(numbers[0], numbers[1], "*")
                concatenation = get_append_result(numbers[0], numbers[1])
                to_try.append([concatenation] + numbers[2:])
                to_try.append([sum] + numbers[2:])
                to_try.append([multiplication] + numbers[2:])
                
            
    return result

def main():
    
    input = dict()
    
    with open("input.txt") as f:   # Open the file
        lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            result = line.split(":")[0]
            numbers = line.split(":")[1].split(" ")[1:]
            input[int(result)] =  [int(x) for x in numbers]
    
    part1_result = part1(input)
    result_1 = 0
    for key in part1_result:
        input.pop(key)
        result_1 += key
            
    print(f"Part 1: {result_1}")
    
    part2_result = part2(input)
    result = 0
    for key in part2_result:
        input.pop(key)
        result += key  
        
    print(f"Part 2: {result_1 + result}")      
    
if __name__ == "__main__":
    main()