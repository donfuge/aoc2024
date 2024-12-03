import numpy as np

def preprocess(fname):
    with open(fname, "r") as f:
        lines = f.readlines()

    reports = []
    for line in lines:
        reports.append(np.asarray(line.strip().split(" "), dtype="int"))
    return reports

def is_safe(report):
    differences = np.diff(report)
    reports_increasing = np.all(differences > 0)
    reports_decreasing = np.all(differences < 0)
    reports_diff_at_most_three = np.all(np.abs(differences) <= 3)
    reports_diff_at_least_one = np.all(np.abs(differences) >= 1)
    return (reports_increasing | reports_decreasing) & reports_diff_at_least_one & reports_diff_at_most_three

def part1(reports):
    safe_reports = 0
    for report in reports:
        safe_reports += is_safe(report)
    return safe_reports

def part2(reports):
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
        else:
            for skipidx in range(len(report)):
                if is_safe(np.delete(report, skipidx)):
                    safe_reports += 1
                    break
    return safe_reports

if __name__ == "__main__":

    reports_example = preprocess("day02_example.txt")

    part1_example_sol = part1(reports_example)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 2

    reports = preprocess("day02_input.txt")

    part1_sol = part1(reports)
    print(f"Part 1 solution: {part1_sol}")

    part2_example_sol = part2(reports_example)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 4

    part2_sol = part2(reports)
    print(f"Part 2 solution: {part2_sol}")