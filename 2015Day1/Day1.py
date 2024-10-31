print("\n-----2015 AoC Day One-------")

file = open(r'2015Day1\Input.txt')
contents = file.read()
pos = 0
instruction = 0
basement = False

for char in contents:
    instruction = instruction + 1
    if char == '(':
        pos = pos + 1
    else:
        pos = pos - 1
    if pos == -1 and basement == False:
        basement = True
        print(f'First in basement at {instruction}')
        
print(f"Finish on follor {pos}")
