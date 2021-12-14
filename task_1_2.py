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
