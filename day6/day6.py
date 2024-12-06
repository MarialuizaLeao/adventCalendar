
# Define the class guard
class Guard:
    def __init__(self, initial_position):
        self.facing_direction = 0
        self.current_position = initial_position
        
    def turn_right_90_degrees(self):
        self.facing_direction = (self.facing_direction + 90) % 360
     
    def next_step(self):
        # Walk up
        if self.facing_direction == 0:
            return [self.current_position[0] - 1, self.current_position[1]]
        # Walk right
        elif self.facing_direction == 90:
            return [self.current_position[0], self.current_position[1] + 1]
        # Walk down
        elif self.facing_direction == 180:
            return [self.current_position[0] + 1, self.current_position[1]]
        # Walk left
        elif self.facing_direction == 270:
            return [self.current_position[0], self.current_position[1] - 1] 
        
    def step_forward(self, steps):
        # Walk up
        self.current_position = self.next_step()
        
    def copy(self):
        new_guard = Guard(self.current_position[0], self.current_position[1])
        new_guard.facing_direction = self.facing_direction
        return new_guard    

def is_guard_on_map(map_dimentions: tuple, guard_position: tuple) -> bool:
    return guard_position[0] >= 0 and guard_position[0] < map_dimentions[0] and guard_position[1] >= 0 and guard_position[1] < map_dimentions[1]

def can_guard_step_forward(map_dimentions: tuple, guard: Guard, obstacles: set) -> int:
    next_position = guard.next_step()
    if is_guard_on_map(map_dimentions, next_position):
        if (next_position[0],next_position[1]) in obstacles :
            return 0
        else:
            return 1
    return -1

def part1(obstacles: set, guard_initial_position: tuple, map_dimentions: tuple) -> tuple:
    guard = Guard(guard_initial_position)
    guard_visited = set()
    loop_positions = set()
    guard_visited.add(guard_initial_position)
    loop_positions.add((guard_initial_position, guard.facing_direction))
    while True:
        while can_guard_step_forward(map_dimentions, guard, obstacles) == 1:
            guard.step_forward(1)
            guard_visited.add(tuple(guard.current_position))
            if (tuple(guard.current_position), guard.facing_direction) in loop_positions:
                return set()
            loop_positions.add((tuple(guard.current_position), guard.facing_direction))
        if can_guard_step_forward(map_dimentions, guard, obstacles) == -1:
            break
        else:
            guard.turn_right_90_degrees()
    return guard_visited

def part2(obstacles: list, guard_initial_position: tuple, map_dimentions: tuple) -> int:
    loop_count = 0
    loop_positions = set()
    
    for i in range(map_dimentions[0]):
        for j in range(map_dimentions[1]):
            if (i,j) not in obstacles:
                obstacles.add((i,j))
                visited_positions = part1(obstacles, guard_initial_position, map_dimentions)
                if len(visited_positions) == 0:
                    loop_count += 1
                    loop_positions.add((i,j))
                obstacles.remove((i,j))

    return loop_count
         
def main():
    
    guard_initial_position = None
    obstacles = set()
    
    with open("input.txt") as f:   # Open the file
        lines = f.readlines()
        
    row = len(lines)
    col = len(lines[0].strip())
    map_dimensions = (row, col)
    for i in range(row):
        line = lines[i].strip()
        for j in range(col):
            if line[j] == '^':
                guard_initial_position = (i,j)
            if line[j] == '#':
                obstacles.add((i,j))
    
    print(f"Part 1: {len(part1(obstacles, guard_initial_position, map_dimensions))}")
    print(f"Part 2: {part2(obstacles, guard_initial_position, map_dimensions)}")
    
if __name__ == "__main__":
    main()