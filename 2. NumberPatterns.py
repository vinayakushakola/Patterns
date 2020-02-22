print("Pattern 1")
for i in range(1, 5):
    for j in range(i):
        print(f'{i} ', end="")
    print()

print("Pattern 2")
for i in range(1, 5):
    for j in range(i):
        print(f'{j+1} ', end="")
    print()

print("Pattern 3")
for i in range(1,6):
    for j in range(5-i):
        print(end=" ")
    for k in range(i):
        print(f'{i} ', end="")
    print()
space = 1
for i in range(4,0,-1):
    for j in range(space):
        print(end=" ")
    for k in range(i):
        print(f'{i} ',end="")
    print()
    space += 1
print()

print("Pattern 4")
number = 1
for i in range(1,5):
    for j in range(i):
        print(f'{number} ', end="")
        number += 1
    print()

print("Pattern 5")
number = 1
for i in range(1,5):
    for j in range(i):
        print(f'{number} ', end="")
        number += 1
    print()
number2 = 4
number3 = 2
number4 = 1
for i in range(1,4):
    for j in range(4-i):
        if i == 1:
            print(f'{number2} ', end="")
            number2 += 1
        elif i==2:
            print(f'{number3} ', end="")
            number3 += 1
        elif i == 3:
            print(f'{number4} ', end="")
    print()

print("Pattern 6")
number = 1
for i in range(1,5):
    for k in range(4-i):
        print(end="  ")
    for j in range(i):
        print(f'{number} ', end="")
        number += 1
    print()
number2 = 4
number3 = 2
number4 = 1
for i in range(1,4):
    for k in range(i):
        print(end="  ")
    for j in range(4-i):
        if i == 1:
            print(f'{number2} ', end="")
            number2 += 1
        elif i==2:
            print(f'{number3} ', end="")
            number3 += 1
        elif i == 3:
            print(f'{number4} ', end="")
    print()

print("Pattern 7")
number = 1
for i in range(1,5):
    for k in range(4-i):
        print(end="  ")
    for j in range(i):
        print(f' {number}  ', end="")
        number += 1
    print()
number2 = 4
number3 = 2
number4 = 1
for i in range(1,4):
    for k in range(i):
        print(end="  ")
    for j in range(4-i):
        if i == 1:
            print(f' {number2}  ', end="")
            number2 += 1
        elif i==2:
            print(f' {number3}  ', end="")
            number3 += 1
        elif i == 3:
            print(f' {number4}  ', end="")
    print()

print("Pattern 8")
