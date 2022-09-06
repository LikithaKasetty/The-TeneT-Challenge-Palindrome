from unicodedata import numeric
def do_tenet(s, n, k):
    s = list(s)
    ls3 = []
    #Create list for getting greatest number
    for i in range(0, n):
        ls3.append(i)
    ls1 , ls2 = [], []
    #A flag variable to check for number of changes
    flag = 0
    #Check if the number is even or odd and update the end iteration value
    range_itend = int ( len(s) / 2 if  len(s) % 2 == 0 else (len(s) - 1) / 2 )
    #Logic to handle numbers starting with zero
    if s[0] == '0':
            s[0] = '9' 
    #Logic to convert number into palindrome  
    for i in range(0 , range_itend) :
        #Logic to handle if the number is already a palindrome and number of changes is one
        if s == s[::-1] and k == 1 :
            if range_itend == (len(s) - 1) / 2 :
                s[range_itend] = '9'
                flag += 1
        if (flag < k):
            if (s[i] == s[-(i + 1)]) :
                ls2.append(i)
                continue
            else:
                if  (s[i] > s[-(i + 1)]):
                    s[-(i + 1)] = s[i]
                    flag += 1
                    ls1.append(i)
                elif s[i] < s[-(i + 1)]:
                    s[i] = s[-(i + 1)]
                    flag += 1
                    ls1.append(i)
                else:
                    pass
    #Logic to covert palindrome number to greatest possible palindrome number
    for i in ls3:
        if (flag < k) :
            if i in ls1:
                 if s[i] != '9':
                    s[i] = s[-(i + 1)] = '9'
                    flag += 1
            elif i in ls2:
                 if s[i] != '9' and  flag < (k - 1):
                    s[i] = s[-(i + 1)] = '9'
                    flag += 2
            else :
                pass
    #Logic to check the number and return the result 
    if s == s[::-1]:
        return "".join(s)
    else:
        return -1
#Take the input n (Number of digits) and k (Number of changes).
n = int(input("Enter the number of digits: "))
k = int(input("Enter the number of changes: "))
#Check for the constraints and assert the error
assert n  > 0 and n <= 10 ** 5 , "The range of n should be 1 to 10^5"
assert k  > 0 and k <= 10 ** 5 , "The range of k should be 1 to 10^5"
#Take the number
s = input ("Enter the number:")
assert s.isnumeric() , "The number should have only digits from 0 to 9" 
#Call the function and print the return value
print(do_tenet(s, n, k))
