'''
Write a Python program which solves simultaneous equation in three variables x, y, z.
'''

def simultaneous_solver(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    D = a1*b2*c3 + b1*c2*a3 + c1*a2*b3 - c1*b2*a3 - a1*c2*b3 - b1*c2*a3
    D1 = d1*b2*c3 + b1*c2*d3 + c1*d2*b3 - c1*b2*d3 - d1*c2*b3 - b1*c2*d3
    D2 = a1*d2*c3 + d1*c2*a3 + c1*a2*d3 - c1*d2*a3 - a1*c2*d3 - d1*c2*a3
    D3 = a1*b2*d3 + b1*d2*a3 + d1*a2*b3 - d1*b2*a3 - a1*d2*b3 - b1*d2*a3
    if D != 0:
        x = D1/D
        y = D2/D
        z = D3/D
        return f"x = {x}, y = {y}, z = {z}"
    elif D == 0:
        if D1 != 0 or D2 != 0 or D3 != 0:
            return "The given system is not consistent and cannot be solved."
        elif D1 == 0 or D2 == 0 or D3 == 0:
            return f"x = {d1/a1} - ({b1/a1})*t - ({c1/a1})*t, y = {d2/a2} - ({b2/a2})*t - ({c2/a2})*t, z = t \nHere t is an arbitary constant."


print("For simultaneous equations a1x + b1y + c1z = d1, a2x + b2y + c2z = d2 and a3x + b3y + c3z = d3, ")
solution = simultaneous_solver(eval(input('a1 = ')), eval(input('b1 = ')), eval(input('c1 = ')), eval(input('d1 = ')), eval(input('a2 = ')), eval(
    input('b2 = ')), eval(input('c2 = ')), eval(input('d2 = ')), eval(input('a3 = ')), eval(input('b3 = ')), eval(input('c3 = ')), eval(input('d3 = ')))
print(solution)
