word=input("type in a word and I will tell you if it is a palindrome ")
ltrs=[*word]
# print(ltrs)
num=len(ltrs)

if num%2==1 and num>=3:
    mid=num/2
else:
    # mid=num/2
    # mid=mid-1
    print("the word " + word + " is not a palindrome")
    quit()
mid=int(mid)
x=0
palindrome=True
while(mid-x!=-1):
    if(ltrs[mid+x]==ltrs[mid-x]):
        x=x+1
    else:
        palindrome=False
        break
# print(palindrome)
if palindrome==True:
    print("the word \"" + word + "\" is a palindrome")
else:
    print("the word \"" + word + "\" is not a palindrome")
