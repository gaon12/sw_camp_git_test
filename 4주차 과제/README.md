```
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
Name    Shares  Price   Change
----------------------------------------
AA      100     9.22    -22.98
IBM     50      106.28  15.18
CAT     150     35.46   -47.98
MSFT    200     20.89   -30.34
GE      95      13.48   -26.89
MSFT    50      20.89   -44.21
IBM     100     106.28  35.84
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'csv')
Name, Shares, Price, Change
AA, 100, 9.22, -22.98
IBM, 50, 106.28, 15.18
CAT, 150, 35.46, -47.98
MSFT, 200, 20.89, -30.34
GE, 95, 13.48, -26.89
MSFT, 50, 20.89, -44.21
IBM, 100, 106.28, 35.84
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'html')
<tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
<tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
<tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
<tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
<tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
<tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
<tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
<tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>