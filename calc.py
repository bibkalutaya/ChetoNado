def main():
    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        print ("сколько переменных?")
        kolvo = input()
        i=0
        if action in ('+', '-', '*', '/'):
            if action == '+':
                while (int(kolvo)>int(i)):
                    print("введите число")
                    vveli = int(input())
                    if i==0:
                        sum=vveli
                        i+=1
                    else:
                        sum += vveli
                        i+=1
                print(sum)
            elif action == '-':
                while (int(kolvo)>int(i)):
                    print("введите число")
                    vveli = int(input())
                    if i==0:
                        razn=vveli
                        i+=1
                    else:
                        razn -= vveli
                        i+=1
                print(razn)
            elif action == '*':
                while (int(kolvo)>int(i)):
                    print("введите число")
                    vveli = int(input())
                    if i==0:
                        umn=vveli
                        i+=1
                    else:
                        umn *= vveli
                        i+=1
                print(umn)
            elif action == '/':
                while (int(kolvo)>int(i)):
                    print("введите число")
                    vveli = int(input())
                    if vveli != 0:
                        if i==0:
                            umn=vveli
                            i+=1
                        else:
                            umn /= vveli
                            i+=1
                    else:
                        print("Деление на ноль!")
                        break
                print(umn)
                
                    
                

if __name__ == '__main__':
    main()