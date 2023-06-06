def cool():
    num1 = 10_111_222_444
    num2 = 99_999_556

    total = num1 + num2

    print(f'{total:,}')
    return


def filefun():
    with open('plansrs.txt','r') as f:
        file_contents = f.read()
    words = file_contents.split(' ')
    word_count = len(words)
    print(word_count)
    print(words)
    return


def enumfun():
    list = ['claws', 'tbow', 'etc']
    for index, item in enumerate(list):
        print(index, item)
    return


def zipfun():
    names = ('peter parker', 'clark kent', 'wade wilson', 'bruce banner')
    heroes = ('spiderman','superman','deadpool','hulk')
    universes = ('marvel', 'dc', 'marvel' , 'dc')


    for name, hero, universe in zip(names, heroes, universes):
        print(f'{name} is actually {hero} from {universe}')
    return


def main():
    #filefun()
    #enumfun()
    zipfun()

class car():
    pass
my_car = car()

car_type_key = 'Model'
car_type = 'Monte Carlo'

setattr(my_car, car_type_key, car_type)

value = getattr(my_car, car_type_key)

print(value)

main()