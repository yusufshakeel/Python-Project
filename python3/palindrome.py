#palimdrome

def main():
    s = input("Enter string: ").strip()

    if isPalindrome(s):
        print(s + " is a Palindrome")
    else:
        print(s + " is not a Palindrome")

def isPalindrome(s):
    beg = 0
    end = len(s)-1
    while beg < end:
        if s[beg] != s[end]:
            return False
        beg+=1
        end-=1
    return True

main()
