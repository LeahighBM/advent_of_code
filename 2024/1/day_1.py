# DAY 1 PART 1
with open('puzzle_input.txt', 'r') as file:
    data = file.read()

split_data = data.split()

list_1 = []
list_2 = []
for x in range(len(split_data)):
    if x % 2 == 0:
        list_1.append(int(split_data[x]))
    else:
        list_2.append(int(split_data[x]))

list_1.sort()
list_2.sort()

diff_list = []
for i in range(len(list_1)):
    diff_list.append(abs(list_2[i] - list_1[i]))

print(f"Day 1 Part 1 answer: {sum(diff_list)}")
        
# DAY 1 PART 2
similarity_list = []
for i in list_1:
    similarity_list.append(i * list_2.count(i))

print(f"Day 1 Part 2 answer: {sum(similarity_list)}")


