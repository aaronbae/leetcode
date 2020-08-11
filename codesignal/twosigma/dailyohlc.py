def dailyOHLC(timestamp, instrument, side, price, size):
  def format_price(given_price):
    return "{:3.2f}".format(given_price)

  import datetime
  result = {}
  for i, t in enumerate(timestamp):
    formatted_time = datetime.datetime.fromtimestamp(int(t)).strftime('%Y-%m-%d')
    ticker = instrument[i]
    p = price[i]
    p_formatted = format_price(p)
    key = (formatted_time, ticker)
    if key not in result:
      result[key] = [formatted_time, ticker, p_formatted,p_formatted,p_formatted,p_formatted]
    row = result[key]
    row[3] = format_price(max(float(row[3]), p))
    row[4] = format_price(min(float(row[4]), p))
    row[5] = p_formatted
  final_result = []
  for k in sorted(result.keys()):
    final_result.append(result[k])
  return final_result


a = [1450625399, 1450625400, 1450625500, 
             1450625550, 1451644200, 1451690100, 1451691000]
b = ["HPQ", "HPQ", "HPQ", "HPQ", "AAPL", "HPQ", "GOOG"]
c = ["sell", "buy", "buy", "sell", "buy", "buy", "buy"]
d = [10, 20.3, 35.5, 8.65, 20, 10, 100.35]
e = [10, 1, 2, 3, 5, 1, 10]
print(dailyOHLC(a, b, c, d, e))