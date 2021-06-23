'''
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  
You must provide the correct change to each customer, 
so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

'''

def lemonadeChange(self, bills) -> bool:
    five = ten = twenty = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five:
                five -=1
                ten += 1
            else:
                return False
        else:
            if five and ten:
                five -= 1
                ten -= 1
                twenty += 1
            elif five >= 3:
                five -= 3
                twenty += 1
            else:
                return False
    return True