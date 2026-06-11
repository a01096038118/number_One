menu = {
        'chicken': 8000,
        'hot_foot': 12000,
        'dry_food': 7000,
        'nudle': 12000,
        'soju': 4000,
        'beer': 4000,
        'coke': 2000 
}

def userSelectedNum():
    selectedNum = int(input('1.menu     2.total     99.service-out '))
    return selectedNum

def chicken(foodtotal_price):
    chicken_price = menu['chicken']
    print(f'chicken: {chicken_price:,}원')

    return foodtotal_price + chicken_price


def hot_foot(foodtotal_price):
    hot_footprice = menu['hot_foot']
    print(f'hot_foot: {hot_footprice:,}원')
    
    return foodtotal_price + hot_footprice

def dry_food(foodtotal_price):
    dry_foodprice = menu['dry_food']
    print(f'dry_food: {dry_foodprice:,}원')

    return foodtotal_price + dry_foodprice

def nudle(foodtotal_price):
    hot_nudle = menu['nudle']
    print(f'nudle: {hot_nudle:,}원')

    return foodtotal_price + hot_nudle

def soju(drinktotal_price):
    soju_Drink = menu['soju']
    print(f'soju: {soju_Drink:,}원')

    return drinktotal_price + soju_Drink

def beer(drinktotal_price):
    beer_Drink = menu['beer']
    print(f'beer: {beer_Drink:,}원')
    
    return drinktotal_price + beer_Drink

def coke(foodtotal_price):
    coke_Drink = menu['coke']
    print(f'coke: {coke_Drink:,}원')

    return foodtotal_price + coke_Drink

