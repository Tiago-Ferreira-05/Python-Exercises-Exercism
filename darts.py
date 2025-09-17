def score(x, y):
    shot = x**2 + y**2

    target = {10: 1, 5: 5**2, 1: 10**2}

    for points, area in target.items():
        if shot <= area:
            return points
        
    return 0
