def abc():
    print('hello')

data = 'Bahot Saara'

def multiplier(*a):
    k = 1
    for i in a:
        k *= i
    return k

# print(__name__)
if __name__ == '__main__':
    print(data)