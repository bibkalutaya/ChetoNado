lengthmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

while (True):

    year = int(input('Введите год: '))
    k=0
    i=0
    summ = 0
    while (i !=12):
        for j in lengthmonth:
            for k in range(int(j)+1):
                summ += sum_of_digits(k)
            i+=1

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Год високосный.')
        print (summ+11)
    else:
        print('Год не високосный.')
        print (summ)