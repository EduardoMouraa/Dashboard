from datetime import datetime

def getVal(Order):
    order_Data = {}

    today = datetime.today()
    year = today.strftime("%Y")
    month = int(today.strftime("%m"))
    target = 0
    choiced = ''
    for n in range(5):
        orders = Order.query.filter(Order.month.like('%{}-{}%'.format(year, month + n if month + n > 9 else '0' + str(month + n ))))
        teste = list(orders)
        if len(teste) > 0:
            if len(teste) > 1:
                for test in teste:                    
                    if int(test.month[8:]) > target:
                        choiced = test 
                        target = int(test.month[8:])
            else:
                choiced = teste[0]

            order_Data[choiced.month[5:7]] = choiced.units
    return order_Data