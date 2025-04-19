"""There are n stones on the table in a row, each of them can be red, green or blue. Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.

Input
The first line contains integer n (1 ≤ n ≤ 50) — the number of stones on the table.

The next line contains string s, which represents the colors of the stones. We'll consider the stones in the row numbered from 1 to n from left to right. Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.

Output
Print a single integer — the answer to the problem."""


number_of_stones = int(input())

the_stones_color = list(map(str,input()))

count_neighbor = 0 
for i in range(number_of_stones):
    try:
        if the_stones_color[i] == the_stones_color[i+1]:
            count_neighbor+=1
    except:
        pass


print(count_neighbor)