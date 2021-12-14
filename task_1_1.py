duration = int(input('Введите время в секундах: '))

day = duration//(24*60*60)
hour = (duration - day * (60*60*24))//(60*60)
minute = (duration - day * (60*60*24) - hour * (60*60))//60
second = duration - day * (60*60*24) - hour * (60*60) - minute * 60


print(day, 'день', hour, 'час', minute, 'мин', second,'сек')

