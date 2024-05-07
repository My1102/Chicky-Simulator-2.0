import random

while True:
    wish = int(input('1 or 5 wish: '))
    item = ('coin5','coin5',
            'coin10','coin10',
            'coin15','coin15','coin15',
            'coin20','coin20','coin20',
            'coin25','coin25','coin25','coin25',
            'coin30','coin30','coin30','coin30',
            'coin35','coin35','coin35','coin35','coin35',
            'coin40','coin40','coin40','coin40','coin40',
            'coin45','coin45','coin45','coin45','coin45','coin45',
            'coin50','coin50','coin50','coin50','coin50','coin50',
            'kitty','tanker','worrier','speedy','magnet')

    if wish == 1:
        item1get = random.choice(item)
        print(item1get)

    else:
        item1get = random.choice(item)
        item2get = random.choice(item)
        item3get = random.choice(item)
        item4get = random.choice(item)
        item5get = random.choice(item)
        print(item1get,item2get,item3get,item4get,item5get)