import random


def bruteforce_solution(numbers):  # O(N^2)
    n = len(numbers)
    result = [1] * n
    for i, x in enumerate(numbers):
        for di in [1, -1]:
            step = 1
            while 0 <= i + di * step < n and numbers[i + di * step] < x:
                result[i] += 1
                step += 1

    return result


def stack_solution(numbers):  # O(N)
    n = len(numbers)
    result = [n] * n
    st = []
    for i, x in enumerate(numbers):
        while st and x > numbers[st[-1]]:
            result[st.pop()] -= (n - i)
        st.append(i)
    st.clear()
    for i, x in reversed(list(enumerate(numbers))):
        while st and x > numbers[st[-1]]:
            result[st.pop()] -= (i + 1)
        st.append(i)
    return result


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)]
    # arr = [3, 4, 1, 6, 2]
    s1, s2 = bruteforce_solution(arr), stack_solution(arr)
    print(s1 == s2)
    print(s1)
    print(s2)
