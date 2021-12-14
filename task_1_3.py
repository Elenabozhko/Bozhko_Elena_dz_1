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

