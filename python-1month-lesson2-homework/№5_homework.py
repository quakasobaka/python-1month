#Создать список, содержащий цены на товары (10–20 товаров), например:
input_list = [57.8, 45.6, 76.6, 32.1, 56.8, 11.2, 19.6, 98.7, 101.2, 66.6]
print(input_list)
#Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
for x, num in enumerate(input_list):
    price = (f"{float(num):.2f}").split(".")
    if x == len(input_list) - 1:
        None
    print('{}руб {}коп'.format(price[0],price[1]), end='  ')
#Вывести цены, отсортированные по возрастанию, новый список не создавать
input_list_s = sorted(input_list, reverse=False)
print(input_list_s)
#(доказать, что объект списка после сортировки остался тот же).
input_list.sort()
input_list_s.sort()
print('Списки одинаковы' if input_list == input_list_s else 'Списки не одинаковы')
#Создать новый список, содержащий те же цены, но отсортированные по убыванию.
list = [57.8, 45.6, 76.6, 32.1, 56.8, 11.2, 19.6, 98.7, 101.2, 66.6]
list_s = sorted(list, reverse=True)
print(list_s)
#Вывести цены пяти самых дорогих товаров.
list_expensive = sorted(list, reverse=True)
x = list_expensive[0], list_expensive[1], list_expensive[2], list_expensive[3], list_expensive[4]
print('Цены пяти самых дорогих товаров: {}'.format(x))