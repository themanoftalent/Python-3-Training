inp = ''
tempSum = 0
prices = []
while True:
    inp = input('Insert a value: ')
    if inp == 'stop':
         break
    else:
        prices.append(inp)

if len(prices) >= 4:
    prices.remove((max(prices)))
    prices.remove((min(prices)))

    for price in prices:
        tempSum += float(price)

    avg = tempSum/len(prices)
    print('The average price is: ' + str(avg))

