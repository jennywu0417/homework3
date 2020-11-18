import random
num = random.randint(1,20)
#a = input('請輸入1~10:')
#a = int(a)
b = 0
while b < 5:
    a = int(input('請輸入1~20:'))
    b = b + 1
    if a <= 20 and a >= 1:
        if a == num:
            print("Bingo! 玩的次數:",b)
            break
        elif a > num:
            print('太小')
        elif a < num:
            print('太大')
        else:
            pass
    else:
        print('輸入錯誤')
    if b ==5:
        print('已超過5次')    


