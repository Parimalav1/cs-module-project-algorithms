#!/usr/bin/python

import sys

# Write a function `making_change` that receives as input an amount of money in cents as well as an array of coin denominations 
# and calculates the total number of ways in which change can be made for the input
# For example, `making_change(10)` should return 4, since there are 4 ways 
# to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

#  1. We can make change for 10 cents using 10 pennies
#  2. We can use 5 pennies and a nickel
#  3. We can use 2 nickels
#  4. We can use a single dime


def making_change(amount, denominations):
  # Your code here

    names = {50: "halfdollar(s)", 25: "quarter(s)", 10: "dime(s)", 5: "nickel(s)", 1: "pennies"}
    add = None
    comb = []
    if add:
        comb.append(add)
        i = 0
    if amount == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and amount > 0:
            if amount % denominations[i]:
                return 0
            comb.append((amount/denominations[i], denominations[i]))
            i += 1
        while i < len(denominations):
            comb.append((0, denominations[i]))
            i += 1
        print(" ".join("%d %s" % (n, names[c]) for (n, c) in comb))
        return 1
    cur = denominations[i]
    return sum(count_combs(amount-x*cur, i+1, comb[:], (x, cur)) for x in range(0, int(amount/cur)+1))

# cents = 50
# denominations = [50, 25, 10, 5, 1]

# print(making_change(cents, denominations))


def making_change2(amount, denominations):
    print('making_change2({},{}) called'.format(amount, denominations))
    if amount < 0 or len(denominations) == 0:
        return 0
    elif amount == 0:
        return 1
    num_ways = 0
    for denomination in denominations:
        leftover_denominations = list(filter(lambda x: x != denomination, denominations))
        for i in range(amount // denomination + 1):
            leftover_amount = amount - i * denomination
            num_ways += making_change2(leftover_amount, leftover_denominations)

    print('making_change2({},{}) returns {}'.format(amount, denominations, num_ways))

    return num_ways


if __name__ == "__main__":

  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts

    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        # print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change2(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")





