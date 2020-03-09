import time


def sum_recursive(x, y):
    if x == 0:
        return y
    else:
        return (1 + sum_recursive(x - 1, y))


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    start = time.time()
    s = sum_recursive(n1, n2)
    end = time.time()
    print(f"Sum of {n1} and {n2} is {s}")
    print(f"Time taken is {end-start}")
