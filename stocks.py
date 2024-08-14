

def calculate_total_cost(stock_price, number_of_stocks, trading_fee):
    return (stock_price * number_of_stocks) + trading_fee

def calculate_profit_or_loss(current_price, stock_price, number_of_stocks, trading_fee):
    total_cost = calculate_total_cost(stock_price, number_of_stocks, trading_fee)
    current_value = current_price * number_of_stocks
    profit_or_loss = current_value - total_cost
    return profit_or_loss

def calculate_roi(profit_or_loss, total_cost):
    roi = (profit_or_loss / total_cost) * 100
    return roi

def main():
    print("Stock Trading Calculator")

    initial_investment = float(input("Enter your initial investment (in ZAR): "))
    stock_price = float(input("Enter the purchase price per stock (in ZAR): "))
    number_of_stocks = int(input("Enter the number of stocks you want to buy: "))
    trading_fee = float(input("Enter the trading fee (in ZAR): "))
    current_price = float(input("Enter the current price per stock (in ZAR): "))

    total_cost = calculate_total_cost(stock_price, number_of_stocks, trading_fee)

    profit_or_loss = calculate_profit_or_loss(current_price, stock_price, number_of_stocks, trading_fee)

    roi = calculate_roi(profit_or_loss, total_cost)

    print(f"\nTotal cost of purchasing stocks: R{round(total_cost, 2)}")
    print(f"Profit or Loss: R{round(profit_or_loss, 2)}")
    print(f"Return on Investment (ROI): {round(roi, 2)}%")

if __name__ == "__main__":
    main()
