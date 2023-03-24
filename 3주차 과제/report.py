import fileparse
from Stock import Stock

def read_portfolio(filename):
    with open(filename) as lines:
        portfolio_dict = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
        portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portfolio_dict]
    return portfolio

def read_prices(filename):
    with open(filename) as lines:
        price_dict = dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))
    return price_dict

def make_report_data(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        rows.append((stock.name, stock.shares, current_price, change))
    return rows

def print_report(reportdata):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in reportdata:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def portfolio_report(portfoliofile, pricefile):        
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report_data = make_report_data(portfolio, prices)
    print_report(report_data)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
