


#returns bool, is num2 within 10% of num1?
def within_10_percent(num1, num2):
    num1_low  = num1 - (num1 * 0.1)
    num1_high = num1 + (num1 * 0.1)
    
    if   num1_low <= num2 and num2 <= num1:
        return True
    elif     num1 <= num2 and num2 <= num1_high:
        return True
    else:
        return False




print(within_10_percent(100, 90))
print(within_10_percent(100, 110))
print(within_10_percent(100, 89))