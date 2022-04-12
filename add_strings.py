import time


def add_strings_1(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    ans = ""

    while (i > -1) or (j > -1):
        a = 0 if i < 0 else int(num1[i])
        b = 0 if j < 0 else int(num2[j])
        c = a + b + carry
        ans += str(c % 10)
        carry = c // 10
        i -= 1
        j -= 1

    ans = ans + str(carry) if carry != 0 else ans

    return ans[::-1]


def add_strings_2(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    ans = []

    while (i > -1) or (j > -1):
        a = 0 if i < 0 else int(num1[i])
        b = 0 if j < 0 else int(num2[j])
        c = a + b + carry
        ans.append(str(c % 10))
        carry = c // 10
        i -= 1
        j -= 1

    if carry != 0:
        ans.append(str(carry))

    return "".join(ans[::-1])


if __name__ == "__main__":
    n = 1000000

    a = "".join(["5" for _ in range(n)])

    start_time1 = time.time()
    add_strings_1(a, a)
    end_time1 = time.time()
    print(end_time1 - start_time1)

    start_time2 = time.time()
    add_strings_2(a, a)
    end_time2 = time.time()
    print(end_time2 - start_time2)


