# Katheryn Busch PSID: 1868948
# Coding Problem #2 CIS 2348 Homework 2
def checkPalindrome(s):
    l, h = 0, len(s) - 1

    s = s.lower()

    while (l <= h):

        if (not (s[l] >= 'a' and s[l] <= 'z')):

            l += 1


        elif (not (s[h] >= 'a' and s[h] <= 'z')):

            h -= 1


        elif (s[l] == s[h]):

            l = l + 1

            h = h - 1
            1


        else:

            return False


    return True


s = input()

if (checkPalindrome(s)):

    print(s + " is a palindrome")
else:

    print(s + "is not a palindrome")