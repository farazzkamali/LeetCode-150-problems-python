
def hIndex(citations):
    citations.sort(reverse=True)
    n = len(citations)

    for i in range(n):
        if citations[i] <= i:
            return i

    return n


arr_o = [1, 2, 3, 0, 5]
arr_o.sort(reverse=True)
print(hIndex([1, 2, 3, 0, 5]))
print(arr_o)
