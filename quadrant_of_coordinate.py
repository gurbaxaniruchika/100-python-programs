x, y = map(int,input("Insert the value for variable x and y: ").split())

if x > 0 and y > 0:
    print(f"Point ({x}, {y}) lie in the first quadrant.")
elif x < 0 and y > 0:
    print(f"Point ({x}, {y}) lie in the second quadrant.")
elif x < 0 and y < 0:
    print(f"Point ({x}, {y}) lie in the third quadrant.")
elif x > 0 and y < 0:
    print(f"Point ({x}, {y}) lie in the fourth quadrant.")
elif y == 0:
    print(f"Point ({x}, {y}) lie on the X axis")
elif x == 0:
    print(f"Point ({x}, {y}) lie on the Y axis")
