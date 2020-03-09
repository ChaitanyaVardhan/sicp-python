import time


def sum_iterative(x, y):
    if x == 0:
        return y
    else:
        return sum_iterative(x - 1, y + 1)


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    start = time.time()
    s = sum_iterative(n1, n2)
    end = time.time()
    print(f"Sum of {n1} and {n2} is {s}")
    print(f"Time taken is {end-start}")
