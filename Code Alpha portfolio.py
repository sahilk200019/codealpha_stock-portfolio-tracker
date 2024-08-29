import csv

class Stock:
    def __init__(self, symbol, name, quantity, purchase_price):
        self.symbol = symbol
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price

class PortfolioTracker:
    def __init__(self):
        self.portfolio = []

    def add_stock(self, stock):
        self.portfolio.append(stock)

    def remove_stock(self, symbol):
        for i in range(len(self.portfolio)):
            if self.portfolio[i].symbol == symbol:
                del self.portfolio[i]
                break

    def update_stock_price(self, symbol, current_price):
        for stock in self.portfolio:
            if stock.symbol == symbol:
                stock.current_price = current_price
                break

    def calculate_portfolio_value(self):
        total_value = 0
        for stock in self.portfolio:
            total_value += stock.quantity * stock.current_price
        return total_value

    def calculate_portfolio_returns(self):
        total_cost = 0
        total_value = 0
        for stock in self.portfolio:
            total_cost += stock.quantity * stock.purchase_price
            total_value += stock.quantity * stock.current_price
        if total_cost == 0:
            return 0
        return (total_value - total_cost) / total_cost

    def save_portfolio(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['symbol', 'name', 'quantity', 'purchase_price', 'current_price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for stock in self.portfolio:
                stock_data = {
                    'symbol': stock.symbol,
                    'name': stock.name,
                    'quantity': stock.quantity,
                    'purchase_price': stock.purchase_price,
                    'current_price': stock.current_price
                }
                writer.writerow(stock_data)

    def load_portfolio(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stock = Stock(
                    row['symbol'],
                    row['name'],
                    int(row['quantity']),
                    float(row['purchase_price'])
                )
                stock.current_price = float(row['current_price'])
                self.portfolio.append(stock)

if __name__ == "__main__":
    portfolio_tracker = PortfolioTracker()

    while True:
        print("\nPortfolio Tracker Menu:")
        print("1. Exit")
        print("2. Remove Stock")
        print("3. Update Stock Price")
        print("4. Calculate Portfolio Value")
        print("5. Calculate Portfolio Returns")
        print("6. Save Portfolio")
        print("7. Load Portfolio")
        print("8. Add Stock")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            symbol = input("Enter stock symbol: ")
            name = input("Enter stock name: ")
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            stock = Stock(symbol, name, quantity, purchase_price)
            portfolio_tracker.add_stock(stock)
            print("Stock added successfully.")

        elif choice == 2:
            symbol = input("Enter stock symbol to remove: ")
            portfolio_tracker.remove_stock(symbol)
            print("Stock removed successfully.")

        elif choice == 3:
            symbol = input("Enter stock symbol to update: ")
            current_price = float(input("Enter current price: "))
            portfolio_tracker.update_stock_price(symbol, current_price)
            print("Stock price updated successfully.")

        elif choice == 4:
            portfolio_value = portfolio_tracker.calculate_portfolio_value()
            print("Portfolio Value: ", portfolio_value)

        elif choice == 5:
            portfolio_returns = portfolio_tracker.calculate_portfolio_returns()
            print("Portfolio Returns: ", portfolio_returns)

        elif choice == 6:
            filename = input("Enter filename to save portfolio: ")
            portfolio_tracker.save_portfolio(filename)
            print("Portfolio saved successfully.")

        elif choice == 7:
            filename = input("Enter filename to load portfolio: ")
            portfolio_tracker.load_portfolio(filename)
            print("Portfolio loaded successfully.")

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")