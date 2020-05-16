#===============================================================================
# Palindromic Cargo
# 
# The Gocargo carriers are celebrating their digitisation process, which has given them a lot of benefits and ease of work for their employees. In account of this initiative they are offering their customers to ship their cargos free of cost, if and only if the cargo names are palindromic.
#  
# Given a cargo name, check whether the cargo name is a palindrome or not. Consider only alphabets while checking, remove special characters and spaces.
#  
# Note : Define a function named checkPalindrome() with a string argument.
#  
# Input Format :
#
# 
# Output Format:

#  
# Sample Input 1:
# !!Race !Car!!
# Sample Output 1:
# Yes
#  
# Sample Input 2:
# Racer Car
# Sample Output 2:
# No
# 
# Explanation For Sample 1:
# Cargo name: !!Race !Car!!
# After removing special characters and spaces, the name is "RaceCar".
# Now, making the string case-insensitive, it becomes "racecar", which is a palindrome.  
#===============================================================================
#===============================================================================
# Palindromic Cargo

if __name__ == '__main__':
    pass
import re
def checkPalindrome(s):
    str_in = re.sub('[^A-Za-z0-9]+', '', s)
    reverse_str = str_in[::-1]
    if str_in.upper() == reverse_str.upper():
        return "Yes"
    else:
        return "No" 


str_input = str(input())
print(checkPalindrome(str_input))
    