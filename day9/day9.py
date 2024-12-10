def get_input(filename: str) -> tuple:
    free_space = []
    files = []
    with open(filename) as f:
        line = f.readline().strip()
    index = 0
    for i in range(len(line)):
        if i % 2 == 0:
            files.append((index, int(line[i])))
            index += 1
        else:
            free_space.append(int(line[i]))
    return files, free_space

def get_individual_blocks(files, free_space):
    blocks = []
    ids = []
    for i in range(len(files)):
        blocks.extend([files[i][1]] * files[i][1])
        ids.extend([files[i][0]] * files[i][1])
        if i < len(free_space):
            blocks.extend([0] * free_space[i])
            ids.extend([-1] * free_space[i])
    return blocks, ids

def move_files(blocks, ids, files, free_space):
    for i in range(len(blocks) - 1, -1, -1):
        if ids[i] != -1:
            for j in range(i):
                if ids[j] == -1:
                    blocks[j], blocks[i] = blocks[i], blocks[j]
                    ids[j], ids[i] = ids[i], ids[j]
                    break
    return blocks, ids

def move_files_whole(blocks, ids, files, free_space):
    files.sort(key=lambda x: -x[0])  # Sort files by decreasing file ID number
    for file_id, file_size in files:
        moved = False
        for i in range(len(blocks) - file_size + 1):
            if all(ids[j] == -1 for j in range(i, i + file_size)):
                # Ensure the file is moved to the left
                original_positions = [j for j in range(len(blocks)) if ids[j] == file_id]
                if i < original_positions[0]:
                    # Move the file to the leftmost free space
                    for pos in original_positions:
                        ids[pos] = -1
                    for j in range(i, i + file_size):
                        ids[j] = file_id
                    moved = True
                    break
    return blocks, ids

def get_filesystem_checksum(blocks, ids):
    result = 0
    for i in range(len(ids)):
        if ids[i] != -1:
            result += (i * ids[i])
    return result

def part1(filename: str) -> int:
    files, free_space = get_input(filename)
    blocks, ids = get_individual_blocks(files, free_space)
    blocks, ids = move_files(blocks, ids, files, free_space)
    return get_filesystem_checksum(blocks, ids)

def part2(filename: str) -> int:
    files, free_space = get_input(filename)
    blocks, ids = get_individual_blocks(files, free_space)
    blocks, ids = move_files_whole(blocks, ids, files, free_space)
    return get_filesystem_checksum(blocks, ids)

def main():
    assert part1("test.txt") == 1928
    print(f"Part 1: {part1('input.txt')}")
    assert part2("test.txt") == 2858
    print(f"Part 2: {part2('input.txt')}")

if __name__ == "__main__":
    main()