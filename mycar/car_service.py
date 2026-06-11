from datetime import datetime

carlist = {}
''' cars '''

flag = True
while flag:
    carNumberselected = int(input('1.creat    2.read    3.update    4.delete    99.service-out '))
    if carNumberselected == 1:
        myCar = input('차량번호를 입력하세요: ')
        print(f'차량번호: {myCar}')

        inputTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'입차시간: {inputTime}')

        carlist[myCar] = {
            '차량번호': myCar,
            '입치시간': inputTime,
            '출차시간': None,
            '주차요금 할인대상': None
        }
    
    elif carNumberselected == 2:
        myCar = input('차량번호를 입력하세요: ')
        print(f'{myCar}: {inputTime}')

    elif carNumberselected == 3:
        myCar = input('차량번호를 입력하세요: ')
        selectCar = int(input('1.hybrid  2.N_hybrid '))
        if selectCar == 1:
            nowhourPay = (inputTime * 360) / 2
            electCar = nowhourPay /2
            print('저공해 요금할인 차량입니다.')

        else:
            print('요금할인 적용 차량이 아닙니다.')

    
    elif carNumberselected == 99:
        flag = False