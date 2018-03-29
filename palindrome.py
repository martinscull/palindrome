def isPalindrome(n): #returns true if n is a palindrome
    n=str(n)
    for i in range(len(n)/2):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True
        
#cycles first through b then increments a
for a in range(100,1000):
    for b in range(100,1000):
        c=a*b
        if isPalindrome(c):
        #if str(c) == str(c)[::-1]: #super leet hacker pro way of checking for palindromes
            print 'a is',a,' b is', b, 'and c is ',c,'\n'

