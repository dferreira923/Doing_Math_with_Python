'''
Multiplication table printer
'''

def mult_table(a):
    for i in range(1, 13):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    mult_table(int(a)) 
