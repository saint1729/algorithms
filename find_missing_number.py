import random
import time


def find_missing_element_1(l):
    n = len(l) + 1
    s1 = sum(l)
    s2 = (n * (n + 1)) // 2
    return s2 - s1


def find_missing_element_2(l):
    s = set(l)
    for i, x in enumerate(l):
        if i + 1 not in s:
            return i + 1
    return -1


def find_missing_element_3(l):
    ans, n = 0, len(l) + 1
    for i, x in enumerate(l):
        ans = ans ^ (i + 1) ^ x
    return ans ^ n


if __name__ == "__main__":
    # a = [1, 2, 2, 1, 3, 4, 4, 3, 5]

    n = 100000
    a = [i + 1 for i in range(n)]
    a.remove(random.randint(1, n))

    start_time1 = time.time()
    print(find_missing_element_1(a))
    end_time1 = time.time()
    print(end_time1 - start_time1)

    start_time2 = time.time()
    print(find_missing_element_2(a))
    end_time2 = time.time()
    print(end_time2 - start_time2)

    start_time3 = time.time()
    print(find_missing_element_3(a))
    end_time3 = time.time()
    print(end_time3 - start_time3)
