examples = [
  ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
  ([4,2,0,3,2,5], 9)
]

def trim_zeros(row):
    row_string = "".join([str(x) for x in row])
    row_clean = row_string.strip("0")
    return row_clean

def count_water(row):
    clean = trim_zeros(row)
    total = 0
    for h in clean:
        if h == "0":
            total += 1
    return total

def trapped_water(heights):
    max_h = max(heights)
    total_water = 0
    for i in range(max_h):
        total_water += count_water(heights)
        for j, h in enumerate(heights):
            if h > 0:
                heights[j] -= 1
    return total_water

for heigths, expected in examples:
    result =  trapped_water(heigths)
    if result == expected:
        print(f"Example {heigths} success")
    else:
        print(f"Example {heigths} failure, expected: {expected}, result: {result}")

