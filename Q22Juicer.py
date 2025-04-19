"""
Kolya is going to make fresh orange juice. He has n oranges of sizes a1, a2, ..., an. Kolya will put them in the juicer in the fixed order, starting with orange of size a1, then orange of size a2 and so on. To be put in the juicer the orange must have size not exceeding b, so if Kolya sees an orange that is strictly greater he throws it away and continues with the next one.

The juicer has a special section to collect waste. It overflows if Kolya squeezes oranges of the total size strictly greater than d. When it happens Kolya empties the waste section (even if there are no more oranges) and continues to squeeze the juice. How many times will he have to empty the waste section?

Input
The first line of the input contains three integers n, b and d (1 ≤ n ≤ 100 000, 1 ≤ b ≤ d ≤ 1 000 000) — the number of oranges, the maximum size of the orange that fits in the juicer and the value d, which determines the condition when the waste section should be emptied.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 1 000 000) — sizes of the oranges listed in the order Kolya is going to try to put them in the juicer.

Output
Print one integer — the number of times Kolya will have to empty the waste section.
"""

n = [int(x) for x in input().split()]

#To make it more understandable
number_of_oranges = n[0]
size_of_orange = n[1]
lim_exeeding_to_empty = n[2]

orangies = [int(x) for x in input().split()]

total_size = 0
count_of_empty = 0

for orange in orangies:
    if orange <= size_of_orange:
        total_size += orange
        if total_size > lim_exeeding_to_empty:
            count_of_empty = count_of_empty + 1
            total_size = 0


print(count_of_empty)