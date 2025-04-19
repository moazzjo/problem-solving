"""
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. 
The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. 
The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. 
It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". 
If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.


"""


first_string = input()
second_string = input()

if len(first_string) < len(second_string):
    print(-1)
elif len(first_string) > len(second_string):
    print(1)
else:
    for i in range(len(first_string)):

        if first_string[i].casefold()  == second_string[i].casefold() and i == len(first_string)-1 :
            print(0)

        if first_string[i].casefold() < second_string[i].casefold() :
            print(-1)
            break
        elif first_string[i].casefold()  > second_string[i].casefold() :
            print(1)
            break
        elif first_string[i].casefold()  == second_string[i].casefold():
            continue



        
         


        
            

        