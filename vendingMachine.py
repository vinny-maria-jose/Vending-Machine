""" This module simulates a simple vending machine that sells two types of water
"""

class CoinHandler():
	""" This class handles the collection and validation of coins.
	"""
	COINS = [1, 2, 5, 10]

	@staticmethod
	def collectCoins():
		""" Utility function which returns the value of coins.
		"""
		total = 0
		print("\nInsert coins (accepted: 1, 2, 5, 10 coins). Type 'done' to finish inserting coins.")
		
		while True:
			coin = input("Insert coin: ").lower()
			if coin == 'done':
				break
			elif coin.isdigit() and int(coin) in CoinHandler.COINS:
				total += int(coin)
			else:
				print("Invalid coin. Please insert 1, 2, 5, or 10 coins.")
		return total


class ProductStock():
	""" This class manages the water bottle stocks.
	"""
	def __init__(self, initialStock):
		""" Constructor for ProductStock
		"""
		self.stock = initialStock

	def availableStock(self, waterType):
		""" Get the available water type stock.
			Args:
				waterType(str) - 'plain' or 'fizzy'
		"""
		return self.stock.get(waterType, 0) > 0

	def updateStock(self, waterType):
		""" Update the stock status based on availablity.
			Args:
				waterType(str) - 'plain' or 'fizzy'

			Returns: 
				(bool) - true if is deduct from the actual stock.
		"""
		if self.availableStock(waterType):
			self.stock[waterType] -= 1
			return True
		return False


class WaterType():
	""" This class represents the types of water available in the vending machine.
	"""
	PLAIN = 'plain'
	FIZZY = 'fizzy'


class VendingMachine():
	""" This class handles the logic of vending machine operations.
	"""

	def __init__(self):
		""" Constructor for VendingMachine.
		"""
		self.waterPrices = {
			WaterType.PLAIN: 30,
			WaterType.FIZZY: 35
		}
		self.productStock = ProductStock({'plain': 5, 'fizzy': 5})
	
	def menuView(self):
		""" Displays the menu options.
		"""
		print("\nHi, Welcome!")
		print("\nItem Menu:")
		print("1. Plain Water(30 coins)")
		print("2. Fizzy Water(35 coins)")
		print("Please choose an option (1 or 2):")

	def processTransaction(self, waterChoice, coinsInserted):
		""" Processes the purchase by verifying coin amount and stock.
			Args:
				waterChoice (int): Selected option number
				coinsInserted (int): Total value of coins
		"""
		waterType = WaterType.PLAIN if waterChoice == 1 else WaterType.FIZZY #water_type , water_choice
		price = self.waterPrices[waterType]

		if not self.productStock.availableStock(waterType):
			print(f"Sorry, we're out of {waterType} water.")
			return

		if coinsInserted >= price:
			change = coinsInserted - price
			if self.productStock.updateStock(waterType):
				print(f"Enjoy your {waterType} water! Your change is {change} coins.")
			else:
				print(f"Sorry, we're out of {waterType} water.")
		else:
			print(f"Not enough coins. You need {price - coinsInserted} more coins.")

	def run(self):
		""" Main loop for the vending machine.
		"""
		while True:
			self.menuView()
			try:
				choice = int(input())
			except ValueError:
				print("Invalid input. Please choose a valid option (1 or 2).")
				continue
			
			if choice not in [1, 2]:
				print("Invalid option. Please choose 1 for plain or 2 for fizzy water.")
				continue
			
			coins = CoinHandler.collectCoins()
			self.processTransaction(choice, coins)

			# Check if user wants to make another purchase
			if input("\nDo you want to make another purchase? (y/n): ").lower() != 'y':
				print("\nThank you for using the Vending Machine!")
				break

# Running the vending machine
if __name__ == "__main__":
	vm = VendingMachine()
	vm.run()
