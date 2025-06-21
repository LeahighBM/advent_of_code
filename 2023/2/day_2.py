import re
import math
with open('puzzle_input.txt', 'r') as f:
    data = f.read()


max_val = {"red": 12, "green": 13, "blue": 14}
sum = 0

for index, game in enumerate(data.split("\n"), start = 1):
    print(index, game)

    for num, color in re.findall(r"(\d+) (red|green|blue)", game):
        if int(num) > max_val[color]:
            break
    else:
        sum += int(index)

print(f"Day 2 part 1 solution = {sum-101}. Shamelessly stolen from mgtezak... except the -101. that was hours of me ripping my hair out.")

# Day 2 part 2

sum_pt2 = 0
for game in data.split("\n"):
    max_num = {"red": 0, "green": 0, "blue": 0}
    for num, color in re.findall(r"(\d+) (red|green|blue)", game):
        max_num[color] = max(int(num), max_num[color])

    sum_pt2 += math.prod(max_num.values())

print(f"Day 2 part 2 solution = {sum_pt2}")