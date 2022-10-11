def isPalindrome(s):
    # Dry Run -> civic

    # 1st Pointer-Start
    i = 0  # 0
    # 2nd Pointer-End
    j = len(s) - 1  # 5 - 1 = 4

    # c-0 i=1 v=2 i=3 c=4

    while i < j:
        # while 2 == 2:
        if s[i] != s[j]:
            # if v == v:
            return False
        i += 1  # c i v +
        j -= 1  # v i c -
    return True


t = int(input())
for i in range(t):
    s = str(input())
    print(isPalindrome(s))
