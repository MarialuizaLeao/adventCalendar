import re
import math

def get_middle_page(pages: list) -> str:
    return int(pages[math.floor(len(pages)/2)])

def is_valid_print_order(ordering_rules: dict, print_order: list) -> bool:
    
    for i in range(len(print_order)):
        page = print_order[i]
        # If the page is in the ordering rules, then we need to check if any of the pages that should come after it are before it
        if page in ordering_rules:
            pages_before = print_order[:i]
            for next_page in ordering_rules[page]:
                if next_page in pages_before:
                    return i-1
    return -1

def get_valid_order(x_needs_to_be_before: dict, print_order: list) -> list:

    while is_valid_print_order(x_needs_to_be_before, print_order) != -1:
        smaller_before_index = len(print_order)
        invalid_index = is_valid_print_order(x_needs_to_be_before, print_order)
        if print_order[invalid_index] in x_needs_to_be_before:
            need_to_be_before_list = x_needs_to_be_before[print_order[invalid_index]]
            need_to_be_before_list = [x for x in need_to_be_before_list if x in print_order]
            for need_to_be_before in need_to_be_before_list:
                index = print_order.index(need_to_be_before)
                if index < smaller_before_index:
                    smaller_before_index = index
        print_order.insert(smaller_before_index + 1, print_order.pop(invalid_index))

    return print_order

def parse_input(lines: list) -> tuple:
    x_needs_to_be_before = {}
    pages_print_order = []
    lenght =  len(lines)
    i = 0
    while lines[i] != "\n":
        first_page, second_page = lines[i].strip().split("|")
        if first_page not in x_needs_to_be_before:
            x_needs_to_be_before[first_page] = []
            x_needs_to_be_before[first_page].append(second_page)
        else:
            x_needs_to_be_before[first_page].append(second_page)
        i += 1
    i += 1
    while i < lenght:
        pages_print_order.append(lines[i].strip().split(","))
        i += 1
    return x_needs_to_be_before, pages_print_order

def main():
    with open("./input.txt") as f:   # Open the file
        lines = f.readlines()
    
    x_needs_to_be_before, pages_print_order = parse_input(lines)
        
    valid_print_orders = []
    invalid_print_orders = []
    
    # Split between valid and invalid print orders
    for print_order in pages_print_order:
        if is_valid_print_order(x_needs_to_be_before, print_order) == -1:
            valid_print_orders.append(print_order)
        else:
            invalid_print_orders.append(print_order)

    # Part 1
    result_1 = 0
    for valid_order in valid_print_orders:
        result_1 += get_middle_page(valid_order)
    print(f"Part 1: {result_1}")
    
    # Part 2
    result_2 = 0
    for invalid_order in invalid_print_orders:
        valid_order = get_valid_order(x_needs_to_be_before, invalid_order)
        result_2 += get_middle_page(valid_order)
    print(f"Part 2: {result_2}")
            
if __name__ == "__main__":
    main()