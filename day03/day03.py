
import re

def preprocess(fname):
    with open(fname, "r") as f:
        txt = f.read()
    return txt

def part1(txt):
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    nums = re.findall(pattern, txt)
    sum = 0

    for num in nums:
        sum += int(num[0]) * int(num[1])

    return sum

def part2(txt):
    do_split = txt.split("do()")
    sum = 0

    for parts in do_split:
        dont_split = parts.split("don't()")
        sum += part1(dont_split[0])

    return sum

if __name__ == "__main__":

    txt_example = preprocess("day03_example.txt")
    part2_example = preprocess("day03_part2_example.txt")

    part1_example_sol = part1(txt_example)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 161

    reports = preprocess("day03_input.txt")

    part1_sol = part1(reports)
    print(f"Part 1 solution: {part1_sol}")

    part2_example_sol = part2(part2_example)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 48

    part2_sol = part2(reports)
    print(f"Part 2 solution: {part2_sol}")