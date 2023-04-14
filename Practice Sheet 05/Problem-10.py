'''
Write a function called verbose that, given an integer less than 10^, returns the name of the integer in English. As an example, verbose(123456) should return one hundred twenty-three thousand, four hundred fifty-six. (International Method)
'''

def verbose(n):
    n1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
          'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    n2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty',
          'sixty', 'seventy', 'eighty', 'ninety']
    n3 = ['hundred', 'thousand', 'million', 'billion']
    v = ''

    def two(n):
        if n < 20:
            return n1[n]
        elif n in [20, 30, 40, 50, 60, 70, 80, 90]:
            return n2[int(str(n)[0])]
        elif 20 < n < 100 and n not in [20, 30, 40, 50, 60, 70, 80, 90]:
            return n2[int(str(n)[0])] + ' ' + n1[int(str(n)[-1])]

    def three(n):
        v = ''
        if n in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            return n1[int(str(n)[0])] + ' ' + n3[0]
        elif 100 < n < 1000 and n not in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            return n1[int(str(n)[0])] + ' ' + n3[0] + \
                ' and ' + two(int(str(n)[-2:]))

    def four(n):
        if n in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]:
            return n1[int(str(n)[0])] + ' ' + n3[1]
        elif 1000 < n < 10000 and n not in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]:
            return n1[int(str(n)[0])] + ' ' + n3[1] + \
                ' ' + three(int(str(n)[-3:]))

    def five(n):
        return two(int(str(n)[:2])) + ' ' + n3[1] + ' ' + three(int(str(n)[-3:]))

    def six(n):
        return three(int(str(n)[:3])) + ' ' + n3[1] + ' ' + three(int(str(n)[-3:]))

    def seven(n):
        return n1[int(str(n)[0])] + ' ' + n3[2]

    def eight(n):
        return two(int(str(n)[:2])) + ' ' + n3[2] + ' ' + six(int(str(n)[-6:]))

    def nine(n):
        return three(int(str(n)[:3])) + ' ' + n3[2] + ' ' + six(int(str(n)[-6:]))

    def above(n):
        return f"please enter a number below 1 billion"

    if n < 100:
        v = two(n)
    elif n < 1_000:
        v = three(n)
    elif n < 10_000:
        v = four(n)
    elif n < 100_000:
        v = five(n)
    elif n < 1_000_000:
        v = six(n)
    elif n < 10_000_000:
        v = seven(n)
    elif n < 100_000_000:
        v = eight(n)
    elif n < 1_000_000_000:
        v = nine(n)
    elif n == 1_000_000_000:
        v = n3[3]
    elif n > 1_000_000_000:
        v = above(n)
    return chr(ord(v[0])-32) + v[1:]


n = int(input("Enter a positive integer: "))
print("Your number is: " + verbose(n))
