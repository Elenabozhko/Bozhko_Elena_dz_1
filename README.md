# Bozhko_Elena_dz_1

duration = int(input('Введите время в секундах: '))

day = duration//(24*60*60)
hour = (duration - day * (60*60*24))//(60*60)
minute = (duration - day * (60*60*24) - hour * (60*60))//60
second = duration - day * (60*60*24) - hour * (60*60) - minute * 60


print(day, 'день', hour, 'час', minute, 'мин', second,'сек')
# Bozhko_Elena_dz_1

#Создать список, состощий из кубов нечетных чисел от 1 до 1000(куб Х - третья степень числа Х):
#а.Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#б.к каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
# на цело на7

my_list=[]
for num in range(1, 1001, 2):
   my_list.append(num ** 3)

final_sum = 0
for num in my_list:
    check_sum = 0
    for check_num in str(num):
       check_sum += int(check_num)
    if check_sum % 7 == 0:
       final_sum += num
print(final_sum)

final_sum = 0
for num in my_list:
   num += 17
   check_sum = 0
   for check_num in str(num):
      check_sum += int(check_num)
   if check_sum % 7 ==0:
      final_sum += num
print(final_sum)




#
#Реализовать склонение слова "процент" во фразе "N процентов". Вывести эту фразу на экран
# отдельной строкой для каждого из числе в интервале от 1 до 100


percent = int(input('Введите число процента: '))
p1 = 'процентов'
p2 = 'процент'
p3 = 'процента'
if percent >= 0:
    if percent == 0:
        print(str(percent) + p1)
    elif percent%100 >= 10 and percent%100 <= 20:
        print(str(percent) + p1)
    elif percent%10 == 1:
        print(str(percent) + p2)
    elif percent%10 >= 2 and percent%10 <= 4:
        print(str(percent) + p3)
else:
  print(str(percent) + p1)
