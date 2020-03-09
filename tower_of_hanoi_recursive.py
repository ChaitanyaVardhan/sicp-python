def move(x, src, spare, target):
    if x < 2:
        disc = src.pop()
        target.append(disc)
        return
    move(x - 1, src, target, spare)
    move(1, src, spare, target)    
    move(x - 1, spare, src, target)


if __name__ == "__main__":
    count = int(input())
    peg1 = []
    for i in range(count):
        peg1.append(i + 1)
    peg2 = []
    peg3 = []
    print(f"Before move")
    print(f"peg1: {peg1}")
    print(f"peg2: {peg2}")
    print(f"peg3: {peg3}")
    n = len(peg1)
    move(n, peg1, peg2, peg3)
    print(f"After move")
    print(f"peg1: {peg1}")
    print(f"peg2: {peg2}")
    print(f"peg3: {peg3}")
    
