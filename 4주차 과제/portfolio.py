# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines, 
                                        select=['name','shares','price'], 
                                        types=[str,int,float],
                                        **opts)

        for d in portdicts:
            holding = stock.Stock(name=d['name'], shares=d['shares'], price=d['price'])
            self.append(holding)

        return self

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError("Expected a Stock instance")
        self._holdings.append(holding)


    @property
    def total_cost(self):
    # your code here 
        return sum(s.shares * s.price for s in self._holdings) 

    def __iter__(self):
        return iter(self._holdings)
    
    def print_report(self, prices):
        headers = ("Name", "Shares", "Price", "Change")
        print("{:<10} {:>10} {:>10} {:>10}".format(*headers))
        print("-" * 42)

        for holding in self._holdings:
            current_price = prices[holding.name]
            change = current_price - holding.price
            print("{:<10} {:>10} {:>10.2f} {:>10.2f}".format(holding.name, holding.shares, holding.price, change))
'''
    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

 

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
'''