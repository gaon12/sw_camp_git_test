# compare.py
"""
Requirements: 현재 보유한 주식을 확인하고 업데이트된 가격을 확인한 후 최종 수익이 얼마인지 확인하는 프로그램을작성하시오
보유한 주식은 portpolio.csv를 통해 기록이 되어 있고 
보유주식은 name shares price로 구성 되어 있음 현재 price는 구매시 unit price이고 
현재 주식의 가격 변동은 price.csv를 통해 확인 할 수 있음. 

Problem Define:
1. 보유 주식의 portpolio를  'portpolio.csv'를 통해 확인
2. 현재 가격이 얼마인지 price를 'price.csv'통해 확인
3. portpolio와 price 가격 비교를 통해 total cost와 total gain을 구할 것 

##########################

Name: name, shares, price
precondition: Calculate the value of a stock portfolio by processing two CSV files
Method: 'csv.reader', 'strip', 'sum'
Post: Compare portpolio and price to find total cost and total gain

##########################

"""
#
import csv

# portfolio.csv 파일 읽기
portfolio = []
with open('portfolio.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # header 스킵
    for row in reader:
        if len(row) >= 3:  # 데이터를 올바르게 읽었는지 확인
            portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

# prices.csv 파일 읽기
prices = {}
with open('prices.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:  # 데이터를 올바르게 읽었는지 확인
            name = row[0].strip('"')
            price = float(row[1])
            prices[name] = price

# portfolio의 price를 prices.csv에 따라 업데이트
updated_portfolio = []
for stock in portfolio:
    if stock['name'] in prices:
        updated_price = prices[stock['name']]
        price_diff = updated_price - stock['price']
        updated_portfolio.append({'name': stock['name'], 'shares': stock['shares'], 'price': updated_price, 'price_diff': price_diff})
    else:
        updated_portfolio.append(stock)

# 각 name별 price 차이 출력
print("Price differences:")
for stock in updated_portfolio:
    print(f"{stock['name']} : {stock['price_diff']}")

# shares와 price 값을 곱한 것들을 모두 합친 값 출력
total_cost = sum([stock['shares'] * stock['price'] for stock in updated_portfolio])
print("Total Cost:", total_cost)
