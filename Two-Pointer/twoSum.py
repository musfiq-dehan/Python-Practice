def twoSum(arr, target):
    # arr = [10, 20, 30, 40]
    #        i            j
    #        0    1   2   3
    # target = 50
    # target = 30

    i = 0
    j = len(arr) - 1  # 4 - 1 = 3

    while i < j:
        # 0 < 3
        # 0 < 2
        # 0 < 1
        sums = arr[i] + arr[j]
        # 50 = 10 + 40 = target=50

        # 50 = 10 + 40 > target=30
        # 40 = 10 + 30 > target=30
        # 30 = 10 + 20 = target=30
        if sums == target:  # 50 == 50 -> True # 30 == 30 -> True
            print(f"arr[i] = {arr[i]}, arr[j] = {arr[j]}")
            print(f"i = {i}, j = {j}")
            return True
        elif sums < target:
            i += 1
        else:
            j -= 1  # 3-1=2-1=1
    return False


t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    target = int(input())
    print(twoSum(arr, target))
