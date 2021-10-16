import random

human_choice = 0
curren_choice = 0

while curren_choice <=21:
    human_choice = int(input('Số bạn chọn là: '))
    curren_choice+=human_choice
    if curren_choice >= 21:
        print('Tổng hiện tại là = ', curren_choice)
        print('Bạn chơi NGU qá, thua máy rồi @@')
        break
    else:
        pc_choice = random.randint(1, 3)
        print('Máy chọn số: ', pc_choice)
        curren_choice += pc_choice
        print('Tổng hiện tại là = ', curren_choice)
        if curren_choice>=21:
            print('Bạn chơi tốt lắm, máy thua rồi!')
            break


