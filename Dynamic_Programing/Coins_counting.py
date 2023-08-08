"""
Suppose we have n coins weighing W1, W2, ..., Wn respectively, 
and the problem is to find the smallest number of coins so that their total mass is a value S. 
Of course, The number of coins is unlimited

If input is: n = 3, S = 11, w = [1, 3, 5]
So the table of solution for sub problem is
P = 0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11
------+--+--+--+--+--+--+--+--+--+--+--
k = 0 |1 |2 |1 |2 |1 |2 |3 |2 |3 |2 |3

11 = 5 + 5 + 1
"""

def calculate_number_coins(lst, val):
    arr_dynamic = [0] * (val + 1)
    for p in range(1, val+1):
        arr_dynamic[p] = min(arr_dynamic[p - x] for x in lst if x <= p) + 1

    return arr_dynamic[val]

if __name__ == "__main__":
    n = int(input("Enter the number of coins:"))
    arr = []
    for i in range(n):
        k = int(input("Enter the value of coint " + str(i) + " :"))
        arr.append(k)

    s = int(input("Enter the value to calculate the number of coins: "))

    number_coin = calculate_number_coins(arr, s)
    print(number_coin)

