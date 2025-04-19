"""
Mad scientist Mike entertains himself by arranging rows of dominoes. He doesn't need dominoes, though: he uses rectangular magnets instead. Each magnet has two poles, positive (a "plus") and negative (a "minus"). If two magnets are put together at a close distance, then the like poles will repel each other and the opposite poles will attract each other.

Mike starts by laying one magnet horizontally on the table. During each following step Mike adds one more magnet horizontally to the right end of the row. Depending on how Mike puts the magnet on the table, it is either attracted to the previous one (forming a group of multiple magnets linked together) or repelled by it (then Mike lays this magnet at some distance to the right from the previous one). We assume that a sole magnet not linked to others forms a group of its own.


Mike arranged multiple magnets in a row. Determine the number of groups that the magnets formed.

Input
The first line of the input contains an integer n (1 ≤ n ≤ 100000) — the number of magnets. Then n lines follow. The i-th line (1 ≤ i ≤ n) contains either characters "01", if Mike put the i-th magnet in the "plus-minus" position, or characters "10", if Mike put the magnet in the "minus-plus" position.

Output
On the single line of the output print the number of groups of magnets.

"""

# num_of_magnets = int(input())
# magnets_poles = []
# for _ in range(num_of_magnets):
#     magnets_poles.append(input())

# magnets_poles.append(" ")
# count = 0
# for i in range(len(magnets_poles)-1):
    
#     if magnets_poles[i] == '01' and magnets_poles[i+1] != '01' :
#         count += 1
    
#     if magnets_poles[i] == "10" and magnets_poles[i+1] != '10':
#         count += 1
    



# print(count)


# do the other code concept that you saw

number_of_mag = int(input())

c=1

prev = input()
for _ in range(1, number_of_mag):
    n = input()

    if prev != n:
        prev = n
        c+=1

print(c)
