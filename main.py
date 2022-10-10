numbers = [5, 20, 30, 30, 50]
changed = 0
delval = int(input('Enter the deletion value: '))
for i in range(len(numbers)):
    try:
        numbers.remove(delval)
        changed = 1
    except ValueError:
        if changed == 0:
            numbers.clear()


# ******************************
# Make your Code
# ******************************

print(numbers)