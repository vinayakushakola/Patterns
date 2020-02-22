print("Pattern 1")
for i in range(1,5):
    for j in range(i):
        print("* ", end="")
    print()

print("Patttern 2")
for i in range(1,5):
    for j in range(5-i):
        print("* ", end="")
    print()

print("Pattern 3")
for i in range(1,5):
    for j in range(4-i):
        print(end="  ")
    for k in range(i):
        print("* ",end="")
    print()

print("Pattern 4")
for i in range(1,5):
    for j in range(i-1):
        print(end="  ")
    for k in range(5-i):
        print("* ",end="")
    print()

print("Pattern 5")
for i in range(1,5):
    for j in range(i):
        print("* ",end="")
    print()
for i in range(1,4):
    for j in range(4-i):
        print("* ", end="")
    print()

print("Pattern 6")
for i in range(1,5):
    for j in range(4-i):
        print(end="  ")
    for k in range(i):
        print("* ",end="")
    print()
for i in range(1,4):
    for j in range(i):
        print(end="  ")
    for k in range(4-i):
        print("* ",end="")
    print()

print("Pattern 7")
for i in range(1,5):
    for j in range(4-i):
        print(end="  ")
    for k in range(i):
        print("*   ",end="")
    print()

print("Pattern 8")
for i in range(1,5):
    for j in range(i-1):
        print(end="  ")
    for k in range(5-i):
        print("*   ", end="")
    print()

print("Pattern 9")
for i in range(1,5):
    for j in range(4-i):
        print(end="  ")
    for k in range(i):
        print("*   ",end="")
    print()
for i in range(1,4):
    for j in range(i):
        print(end="  ")
    for k in range(4-i):
        print("*   ", end="")
    print()

print("Pattern 10")
star = 1
for i in range(1,5):
    for j in range(4-i):
        print(end="  ")
    for k in range(star):
        print("* ", end="")
    print()
    star += 2

print("Pattern 11")
star = 7
for i in range(1,5):
    for j in range(i-1):
        print(end="  ")
    for k in range(star):
        print("* ",end="")
    print()
    star -= 2

print("Pattern 12")
star = 1
for i in range(1,5):
    for j in range(4-i):
        print(end="  ")
    for k in range(star):
        print("* ", end="")
    print()
    star += 2
star2 = 5
for i in range(1,4):
    for j in range(i):
        print(end="  ")
    for k in range(star2):
        print("* ", end="")
    print()
    star2 -= 2

print("Pattern 13")
for i in range(1,5):
    for j in range(i-1):
        print(end="  ")
    for k in range(5-i):
        print(" *  ", end="")
    print()
star3 = 2
for i in range(1,4):
    for j in range(3-i):
        print(end="  ")
    for k in range(star3):
        print(" *  ", end="")
    print()
    star3 += 1

print("Pattern 14")
starr1 = 7
for i in range(1,5):
    for j in range(i-1):
        print(end="  ")
    for k in range(starr1):
        print("* ", end="")
    print()
    starr1 -= 2
starr2 = 3
for i in range(1,4):
    for j in range(3-i):
        print(end="  ")
    for k in range(starr2):
        print("* ",end="")
    print()
    starr2 += 2

print("Pattern 15")
for i in range(1,6):
    for j in range(1,i+1):
        if j%2 == 0:
            if i==2 or i==4:
                print("* ", end="")
            else:
                print(end="  ")
        else:
            if i==1 or i==3 or i==5:
                print("* ", end="")
            else:
                print(end="  ")
    print()
for i in range(1,5):
    for j in range(5-i):
        if j%2 == 0:
            if i==4 or i==2:
                print("* ",end="")
            else:
                print(end="  ")
        else:
            if i==1 or i==3:
                print("* ",end="")
            else:
                print(end="  ")
    print()
