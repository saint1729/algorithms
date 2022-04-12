

def get_odd_element_1(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1

    print(d)

    for k in d.keys():
        if d[k] % 2 == 1:
            return k
    return -1


def get_odd_element_2(l):
    ans = 0
    for i in l:
        ans ^= i
    return ans


if __name__ == "__main__":
    # a = [1, 2, 2, 1, 3, 4, 4, 3, 5]
    a = [7, 1, 6, 4, 2, 3]
    # print(get_odd_element_1(a))
    print(get_odd_element_2(a))