# DAY 2 PART 1

with open("puzzle_input.txt", "r") as file:
    data = file.readlines()

unsafe = 0
for i in range(len(data)):

    l = data[i].split()
    l = [int(num) for num in l]

    if sorted(l, reverse=True) == l:
        print(f"List {l} is decreasing")
    elif sorted(l) == l:
        print(f"List {l} is increasing")
    else:
        print(f"List {l} is unsafe")
        unsafe += 1
        continue # skip further processing if unsafe

    # this is admittedly gnarly af... but it works
    for i in range(len(l)):
        try:
            if abs(int(l[i]) - int(l[i+1])) > 0 and abs(int(l[i]) - int(l[i+1])) <= 3:
                pass
            else:
                unsafe += 1
                break
        except IndexError:
            pass
    

safe = len(data) - unsafe
print(safe)


