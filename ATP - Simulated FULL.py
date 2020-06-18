# Building a fullly simulated ATP


# Error seems to come from CANDLE is NOT updating as prices does.

# It should be creating prices constantly.
# Then, when (prices % 10):
#				Create and ADD a new candle.
# Go until 100 candles.




"""
1. Create a simulated price chart in the 10,000's decimal.
2. OHLC Chart (Candle chart) every 10 prices.
3. MAX: 10 candles, 10 prices within each candle.
4. CONDITIONS FOR TRADES: OHLC/Candles
	After 3 consecutive NSH (New Structural High),
		SELL.
		After 3 candles: BUY
	After 3 consecutive NSL (New Structural Low),
		BUY.
		After 3: SELL

NOTE: 	After building the entire thing,
		have it run each second.

	Add new price
	Remove oldest price

	KEEP ALL CANDLES, UNTIL we have a new candle.
	Once we have new candle,
		add the new candle,
		remove the oldest candle

"""

import random
import time



# INITIALIZE PRICES
prices 	= [1]
ohlc 	= []
candles = []

# INITIALIZE RANGE
minimum = 0
maximum = 0

# INITIALIZE TIMER
timer  	= 0

# Range of candle size to make.
candle_size = 5

# Prices for getting in and out of market.
entry_price = 0

total_pips 	= 0

# Q: Are we in market? If so, get out. If not, get in.
in_market = False


# TRADING
def buy(candles):
	"""
	With Candles, NEWEST candle...
	After 3 NSHs (which indicate three bull candles)
			SELL
		After 3 candles,
				BUY to get OUT.
	"""
	pass



def sell(candles):
	"""
	With Candles, NEWEST candle...
	After 3 NSLs (which indicate three bear candles)
			BUY
		After 3 candles,
				SELL to get OUT.
	"""
	pass


# Update prices
while True:

	# Wait one second.
	time.sleep(1)
	timer += 1
	print("Timer:   ", timer)

	# Generate NEW price
	r = round((random.randint(-5, 5)/10000) + prices[-1], 4)
	# ADD new price
	prices.append(r)

	# # SHOW 'prices'
	# print(prices)

	# Create a new candle, every '5' seconds.
	if (timer % candle_size == 0):
		o = prices[-candle_size]
		h = max(prices)
		l = min(prices)
		c = prices[-1]

		ohlc = [o, h, l, c]
		candles.append(ohlc)

		# If we have '3' or more candles, remove old candles.
		if (len(candles) >= 4):
			del candles[0]


		# SHOW 'candles'
		print("Candles: ", candles)



	# STRATEGY: If New Structural High, Sell for 3 candles.
	# At least 3 candles to test.
	if (len(candles) >= 3): 		

		# Either check in or out of market.
		#	After IF/THEN statements,
		# 	then 'PASS' to loop back to top, for a new candle.

		# If we are in the market, if NSL, get out.
		if (in_market == True):



			# New Structural Low?
			if (candles[-1][3] < candles[-2][2]):
			
				total_pips += entry_price - candles[-1][3] 		# Get OUT of market and reset.
				in_market   = False 						 		# We are NOW in the market.

			break 		# or return?


		if (in_market == False):

			# New Structural High?
			if (candles[-1][3] > candles[-2][1]):

				entry_price = candles[-1][3] 			# Get IN the market @ Close.
				in_market   = True 						# We are NOW in the market.

			break 		# or return?

		# Switch cases that SHOULD by-pass the loop
		#	of turning on and off a "light switch" back-to-back.








	print("Pips Made: ", total_pips)