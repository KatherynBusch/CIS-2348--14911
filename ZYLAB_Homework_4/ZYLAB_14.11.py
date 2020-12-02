Katheryn Busch PSID: 1868948
def selection_sort_descend_trace(lst):
    for k in range(len(lst) - 1):
        valueLarge = k
        for w in range(k + 1, len(lst)):
            if lst[w] > lst[valueLarge]:
                valueLarge = w
        lst[k], lst[valueLarge] = lst[valueLarge], lst[k]
        for y in lst:
            print(y, end=' ')
        print()
    return lst
if __name__ == '__main__':
    numbers = [int(y) for y in input().split()]
    selection_sort_descend_trace(numbers)
