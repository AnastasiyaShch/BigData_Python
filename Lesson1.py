#task1
a1 = 2
print(a1)
a2 = input()
print(a2)

#task2
sec = int(input("Введите количество секунд: "))
h = sec // 3600
m = (sec - h * 3600) // 60
s = sec - h * 3600 - m * 60
time = str(h) + ":" + str(m) + ":" + str(s)
print(time)

#task3
n = input ("Введите n: ")
nn = int(n * 2)
nnn = int (n * 3)
n3 = int(n) + nn + nnn
print (n3)


#task4
a = int(input("Введите число:"))
maxnumber = 0
while a >= 1:
    b = a % 10
    if b > maxnumber:
        maxnumber = b
    a = a // 10
print(maxnumber)

#task5
revenue = int(input("Введите выручку:"))
expenses = int(input("Введите расходы:"))
finresult = revenue - expenses
if revenue >= expenses:
    print ("Прибыль:", finresult)
else: print ("Убыток:", finresult)

#task6
margin = finresult / expenses * 100 // 1
if finresult >=0:
    print("Рентабельность:", margin, "%")
    empl_numb = int(input("Введите численность сотрудников:"))
    print("Прибыль на одного сотрудника:", finresult / empl_numb)

#task7
day = 1
km_day = int(input("Сколько километров пробежал спортсмен в первый день?"))
km_lastday = int(input("Сколько километров должен пробежать спортсмен?"))
while km_day < km_lastday:
    km_day = km_day * 1.1
    day = day + 1
print("Спортсмен пробежит ", km_lastday, " километров в день №", day)