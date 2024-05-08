"""
# ex.5
You are interested in buying crypto-currencies. You want to check the current amount of money you have and see how many coins you can buy in Bitcoin, Ethereum, and Litecoin.

Create a program that:
1) Reads the total amount of money you have
2) Reads the price of Bitcoin, Ethereum, and Litecoin
3) Prints the amount of Bitcoin, Ethereum, and Litecoin you can buy

* Example: money = 100, bitcoin_price = 50, ethereum_price = 25, litecoin_price = 10
* Output: "With 100$ you can buy: 2 Bitcoins, 4 Ethereum, and 10 Litecoins"

(Warning! Τhe prices are made up for exercise purposes) """

def stocks_you_can_buy(money, bitcoin, ethereum, litecoin):
    if money != 0:
        num_bitcoin = money // bitcoin
        num_ethereum = money // ethereum
        num_litecoin = money // litecoin
    else:
        None
    return num_bitcoin, num_ethereum, num_litecoin

available_money = 800
price_bitcoin = 80
price_ethereum = 30
price_litecoin = 20

b, e, l = stocks_you_can_buy(available_money, price_bitcoin, price_ethereum, price_litecoin)
print(f"With ${available_money}, you can buy {b} Bitcoins, {e} ethereums, and {l} litecoins.")