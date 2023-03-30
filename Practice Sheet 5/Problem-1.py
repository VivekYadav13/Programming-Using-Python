"""
People often forget closing parentheses when entering formulas. Write a program that asks the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses.
"""
a = str(input('Enter your equation: '))
opennum = 0
closenum = 0
errorcount = 0
for ch in a:
    if ch == '(':
        opennum += 1
    elif ch == ')':
        closenum += 1
if opennum > closenum:
    errorcount = opennum - closenum
if opennum < closenum:
    errorcount = closenum - opennum
if errorcount > 0 and opennum > closenum:
    print('The equation is wrong with', errorcount, 'unclosed parentheses.')
elif errorcount > 0 and opennum < closenum:
    print('The equation is wrong with', errorcount, 'unopen parentheses.')
else:
    print('The equation is correct.')
