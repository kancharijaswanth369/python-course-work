
print("Welcome to Upstox")
print("Stock Profile".center(30, "*"))
stock_id = int(input("Enter Stock ID:"))
stock_name = input("Enter Stock Name:")
current_price = float(input("Enter Current Price of the Stock:"))
sectors = input("Enter Sectors").split(',')
available_volume = int(input("Enter Available volume:"))
traded_volume = int(input("Enter"))
volume_details = (available_volume,traded_volume)
dividend_yield = float(input("Enter Dividend Yield(%):"))
highlights_input = input("Enter Key Highlights:")
key_highlights = set(highlights_input.split(','))
broker_name = input("Enter Broker Name:")
broker_contact = input("Enter Broker Contact Number:")
broker_location = input("Enter Broker Location")
broker_details = {"Name":broker_name,
                  "Contact":broker_contact,
                  "Location":broker_location}
final_dividend = (dividend_yield/100) * current_price
#Comma Separated
print("stock_id:",stock_id,"Stock_Name:",stock_name,"Price:",current_price, sep='|')
print("Sectors:", sectors, "Volume:", volume_details, sep=' | ')
print("Dividend Yield:", dividend_yield, "%", "Key Highlights:", key_highlights, sep=' | ')
print("Broker Details:", broker_details, sep=' | ')
print("Final Dividend (INR):", final_dividend, sep=' | ')

#% formatting
print("Stock ID: %d | Stock Name: %s | Price: %.2f" % (stock_id, stock_name, current_price))
print("Dividend Yield: %.2f%% | Final Dividend: %.2f INR" % (dividend_yield, final_dividend))
#f strings
print(f"Stock ID: {stock_id} | Stock Name: {stock_name} | Price: ₹{current_price:.2f}")
print(f"Dividend Yield: {dividend_yield:.2f}% | Final Dividend: ₹{final_dividend:.2f}")
print(f"Sectors: {sectors}")
print(f"Key Highlights: {key_highlights}")
print(f"Broker: {broker_details['Name']} | Contact: {broker_details['Contact']} | Location: {broker_details['Location']}")

#.format()method
print("Stock ID: {} | Stock Name: {} | Price: ₹{:.2f}".format(stock_id, stock_name, current_price))
print("Dividend Yield: {:.2f}% | Final Dividend: ₹{:.2f}".format(dividend_yield, final_dividend))