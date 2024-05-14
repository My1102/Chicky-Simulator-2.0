import random

username = str(input('username: '))
chicky = str(input('what chicky: '))

def update_chicky(username, chicky):
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_backpack = line.strip().split(", ")
        if user_backpack[0] == username:
            chicky_list = user_backpack[1].split('/')
            if chicky_list[1] == '0':
                del chicky_list[1]
                chicky_list.append(f'{chicky}')
            elif chicky in chicky_list:
                break
            else:
                chicky_list.append(f'{chicky}')
            chicky_str = '/'.join(chicky_list)
            user_backpack[1] = str(chicky_str)
            lines[i] = ', '.join(user_backpack) + '\n'
            break

    with open('user_backpack.txt', 'w') as file:
        file.writelines(lines)
    return

wish = int(input('1 or 5 wish: '))
pull = int(input('Pull: '))
item = ('coin5','coin5',
        'coin10','coin10','coin10',
        'coin15','coin15','coin15','coin15',
        'coin20','coin20','coin20','coin20','coin20',
        'coin25','coin25','coin25','coin25','coin25',
        'coin30','coin30','coin30','coin30','coin30','coin30',
        'coin35','coin35','coin35','coin35','coin35',
        'coin40','coin40','coin40','coin40','coin40',
        'coin45','coin45','coin45','coin45',
        'coin50','coin50','coin50',
        'coin75','coin75',
        'coin90','kitty','tanker','worrier','speedy','magnet')

chickyhoho = ('kitty','tanker','worrier','speedy','magnet')

if wish == 1:
    pull += 1
    if pull < 50:
        itemget = random.choice(item)
        if itemget in chickyhoho:
            pull = 0
        print(itemget, pull)

    else:
        pull = 0
        itemget = random.choice(chickyhoho)
        print(itemget, pull)

else:
    n = 5
    itemlist = [0]
    while n > 0:
        pull += 1
        n -= 1
        if pull < 50:
            itemget = random.choice(item)
            if itemget in chickyhoho:
                pull = 0

        else:
            pull = 0
            itemget = random.choice(chickyhoho)

        itemlist.append(itemget)

    del itemlist[0]
    itemsget = str(f'{itemlist[0]},{itemlist[1]},{itemlist[2]},{itemlist[3]},{itemlist[4]}')
    item1,item2,item3,item4,item5 = itemsget.split(',')
    print(item1, item2, item3, item4, item5)

update_chicky(username, chicky)
