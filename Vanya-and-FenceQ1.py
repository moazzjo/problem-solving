"""

Vanya and his friends are walking along the fence of height h and they do not
want the guard to notice them.In order to achieve this the
height of each of the friends should not exceed h.
If the height of some person is greater than h he can bend down and
then he surely won't be noticed by the guard.
The height of the i-th person is equal to ai.

Consider the width of the person walking as usual to be equal to 1,
while the width of the bent person is equal to 2. 
Friends want to talk to each other while walking, 
so they would like to walk in a single row.
What is the minimum width of the road, 
such that friends can walk in a row and remain unattended by the guard?

Input
The first line of the input contains two integers n and h 
the number of friends and the height of the fence, respectively.

The second line contains n integers ai 
 the i-th of them is equal to the height of the i-th person.

Output
Print a single integer — the minimum possible valid width of the road.



"""


number_of_person,Height_of_the_wall  = map(int , input().split())

  
Height_of_every_person = list(map(int,input().split()))
The_min_width_count = 0

for i in range(number_of_person):
    if Height_of_every_person[i] > Height_of_the_wall:
        The_min_width_count += 2
    else:
        The_min_width_count += 1

        
print(The_min_width_count)

