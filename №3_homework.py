#Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
for x in range(100):
    new_str = str(x + 1)
    new_list = list(new_str)
    if int(new_list[-1]) == 1 and x + 1 != 11:
        print('{} процент'.format(x + 1))
    elif int(new_list[-1]) > 1 and int(new_list[-1]) <= 4:
        if x + 1 > 10 and x + 1 <= 14:
            print('{} процентов'.format(x + 1))
        else:
            print('{} процента'.format(x + 1))
    else:
        print('{} процентов'.format(x + 1))
