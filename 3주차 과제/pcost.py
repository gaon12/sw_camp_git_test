from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum([stock.cost() for stock in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
