stock_dict = { 'GE': 'General Electric',
               'CAT': 'Caterpillar',
               'GM': 'General Motors'
             }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
              ( 'CAT', 100, '1-apr-1999', 24 ),
              ( 'GM', 200, '1-jul-1998', 56 ),
              ( 'GM', 150, '3-jul-1998', 47 )
            ]

total_portfolio_value = 0

for transaction in purchases:
  # each transaction is a tuple.
  stock_ticker = transaction[0]
  number_of_shares = transaction[1]
  transaction_date = transaction[2]
  stock_price = transaction[3]

  company_name = stock_dict[stock_ticker]
  purchase_price = number_of_shares * stock_price
  total_portfolio_value += purchase_price

  output = ['I bought {0} shares '.format(number_of_shares)]
  output.append('of {0} stock '.format(company_name))
  output.append('at {0} dollars per share, '.format(stock_price))
  output.append('for a total price of ${0}.'.format(purchase_price))
  print(''.join(partial for partial in output))

  # output = ['The total value of my investment in {0} is '.format()]

output = ['The total value of my stock portfolio is {0}'.format(total_portfolio_value)]
print(output)




# could also be something like this:
# [print ('I own {0} shares of {1} stock at ${2} for a total of ${3}'.format(p[3], p[0], p[1], (p[1] * p[3])) for p in purchases]
