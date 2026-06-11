import config
import config_02
import function

peoples = 5
foodtotal_price = 0
drinktotal_price = 0

flag = True
while flag:

    selectedNum = function.userSelectedNum()
    if selectedNum ==config_02.MENU:
        
        while flag:
            menuNum = int(input('1.chicken   2.hot_foot    3.dry_food   4.nudle    5.soju   6.beer  7.coke  99.service-out '))
            
            if menuNum == config.CHICKEN:
                foodtotal_price = function.chicken(foodtotal_price)

            elif menuNum == config.HOT_FOOT:
                foodtotal_price = function.hot_foot(foodtotal_price)
                    
            elif menuNum == config.DRY_FOOD:
                foodtotal_price = function.dry_food(foodtotal_price)

            elif menuNum == config.NUDLE:
                foodtotal_price = function.nudle(foodtotal_price)

            elif menuNum == config.SOJU:
                drinktotal_price = function.soju(drinktotal_price)

            elif menuNum == config.BEER:
                drinktotal_price = function.beer(drinktotal_price)
                    
            elif menuNum == config.COKE:
                foodtotal_price = function.coke(foodtotal_price)

            elif menuNum == config.SERVICE_OUT:
                break
            
    if selectedNum == config_02.TOTAL:
        food_total = foodtotal_price
        print(f'음식 총 금액: {food_total:,}원')

        drink_total = drinktotal_price
        print(f'주류 총 금액: {drink_total:,}원')

        print('='* 80)
        total = food_total + drink_total
        print(f'총 금액: {total:,}원')

        print('='* 80)

        userAcol_peoples = int(input('주류 이용한 인원수 입력: '))
        nonAcol_peoples = peoples - userAcol_peoples

        nonAcol_total = food_total / peoples
        print('='* 80)
        print(f'주류 이용안한 사람 n/1금액: {nonAcol_total:,.0f}원')

        userAcol_total = (total - nonAcol_total * nonAcol_peoples) / userAcol_peoples
        print(f'주류 이용한 사람 n/1금액: {userAcol_total:,.0f}원')
        print('='* 80)


    if selectedNum == config_02.SERVICE_OUT:
        flag = False
