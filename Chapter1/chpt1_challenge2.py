'''
Challenge 2

Our multiplication table generator is cool, but it prints only the first 10 multiples. Enhance the generator so that the user can specify both the number
and up to which multiple. For example, I should be able to input that I want
to see a table listing the first 15 multiples of 9
'''


def mult_table(a):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a * i))


if __name__ == '__main__':
    a = input('Enter a number: ')
    b = int(input('Enter a multiple: '))
    mult_table(int(a))
