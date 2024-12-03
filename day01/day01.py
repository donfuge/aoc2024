import numpy as np

def preprocess(fname):
    data = np.loadtxt(fname)
    left_list = data[:,0]
    right_list = data[:,1]
    return left_list, right_list

def part1(left_list, right_list):
    left_list = np.sort(left_list)
    right_list = np.sort(right_list)
    return int(sum(np.abs(left_list - right_list)))

def part2(left_list, right_list):
    unique, counts = np.unique(right_list, return_counts=True)
    multiplicity_table = dict(zip(unique, counts))
    dist = 0
    for lval in left_list:
        if lval in unique:
            dist += lval * multiplicity_table[lval]

    return int(dist)

if __name__ == "__main__":

    left_list_example, right_list_example = preprocess("day01_example.txt")

    part1_example_sol = part1(left_list_example, right_list_example)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 11

    left_list, right_list = preprocess("day01_input.txt")

    part1_sol = part1(left_list, right_list)
    print(f"Part 1 solution: {part1_sol}")

    part2_example_sol = part2(left_list_example, right_list_example)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 31

    part2_sol = part2(left_list, right_list)
    print(f"Part 2 solution: {part2_sol}")