for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            left = not (x or y or z)
            right = not x and not y and not z
            result = left == right
            if result:
                print(f"При x={x}, y={y}, z={z}: Верно")
            else:
                print(f"При x={x}, y={y}, z={z}: Не верно")