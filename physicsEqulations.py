print('Fizikai számításokat végzek el. Kérlek válassz egy számot!')
print(' 1 - sebesség; 2 - gyorsulás; 3 - erő; 4 - munka; 0 - kilépés')
userChoice = input('Témakör: ')
userChoice = int(userChoice)
Answers = 0

while userChoice != 0:
    if userChoice == 1:
        print('11 - út; 12 - sebesség; 13 - idő')
        usCho = int(input('Mit szeretnél kiszámolni? '))
        if usCho == 11:
            num1 = int(input('Sebesség (km/h) : '))
            num2 = int(input('Idő (h) : '))
            ans = num1*num2
            Answers += 1
            print(ans)
        elif usCho == 12:
            num1 = int(input('Út (km) : '))
            num2 = int(input('Idő (h) : '))
            ans = num1/num2
            Answers += 1
            print(ans)
        elif usCho == 13:
            num1 = int(input('Út (km) : '))
            num2 = int(input('Sebesség (km/h) : '))
            ans = num1/num2
            Answers += 1
            print(ans)

print(f'{Answers} számítást végeztem el.')

input('Press Enter to exit!')