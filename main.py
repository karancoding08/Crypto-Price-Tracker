import requests

print("========== CRYPTO PRICE TRACKER ==========")

coin = input("Enter coin name: ").lower()

try:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

    if coin in data:
        print("\nCoin:", coin.capitalize())
        print("Current Price: $", data[coin]["usd"])
    else:
        print("Coin not found!")

except Exception as e:
    print("Error:", e)

print("==========================================")