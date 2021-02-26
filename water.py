examples = [
  ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
  ([4,2,0,3,2,5], 9)
]

def trapped_water(heights):
    total = 0
    walls = []
    for i, h in enumerate(heights):
        for w_h in range(h):
            try:
                total += i - 1 - walls[w_h]
                walls[w_h] = i
            except:
                walls.append(i)
    return total

for heigths, expected in examples:
    result =  trapped_water(heigths)
    if result == expected:
        print(f"Example {heigths} success")
    else:
        print(f"Example {heigths} failure, expected: {expected}, result: {result}")

