#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#до минуты: <s> сек
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400


duration = int (input('Введите продолжительность в секундах'))

if duration < one_minute:
    print('{} сек'.format(duration))
elif one_minute <= duration and one_hour > duration:
    my_minute = duration//one_minute
    my_sec = duration%one_minute
    print('{} мин {} сек'.format(my_minute,my_sec))
elif one_hour <= duration and  one_day > duration:
    my_hour = duration//one_hour
    duration = duration%one_hour
    my_minute = duration//one_minute
    my_sec = duration%one_minute
    print('{} час, {} мин, {} сек'.format(my_hour,my_minute,my_sec))





