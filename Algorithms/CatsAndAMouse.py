def catsAndMouse(x,y,z):
    print(['Cat A', 'Cat B', 'Mouse C'][0 if abs(x - z) < abs(y - z) else 1 if abs(x - z) > abs(y - z) else 2])



catsAndMouse(1,2,3)
