# DAY 1 PART 1
with open('puzzle_input.txt', 'r') as f:
    data = f.readlines()

all_nums = ""
list_of_nums = []
for string in data:
    for char in string:
        if char.isnumeric():
            all_nums += char

    all_nums.rstrip()
    # want first and last number only
    num = all_nums[0] + all_nums[-1]
    list_of_nums.append(int(num)) 
    all_nums = ""  

print(f"Day 1 Part 1 answer: {sum(list_of_nums)}")

# DAY 1 PART 2
with open('puzzle_input.txt', 'r') as ff:
    data2 = ff.readlines()
    
nums_dict ={
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9"
} 

holder_of_all_numbers = ""
list_of_valid_nums = []
for string in data2:
    for i in range(len(string)):
        if string[i].isnumeric():
            holder_of_all_numbers += string[i]
        else:
            for k,v in nums_dict.items():
                if string[i:].startswith(k):
                    holder_of_all_numbers += v

    num = holder_of_all_numbers[0] + holder_of_all_numbers[-1]
    list_of_valid_nums.append(int(num))
    holder_of_all_numbers = ""

print(f"Day 1 Part 2 answer: {sum(list_of_valid_nums)}")