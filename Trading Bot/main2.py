import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
import argparse

# =========================
# CONFIG
# =========================
API_KEY = "LdNfumjzvLpTj5A7DvFtePbmyUjjBbszr0ydxvRnXD8fK9NknJeSQRMtZZxxRxAR"
API_SECRET = "oIJTMRn3ROYmN0mQF0IVmObTcW9gLoBjGicEA3Wa9thVYaLckctLnvWB1tW48brk"

BASE_URL = "https://testnet.binancefuture.com"

# =========================
# LOGGING
# =========================
logging.basicConfig(
    filename="binance_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# CLIENT LAYER
# =========================
def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL
    return client

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Order Request: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order Response: {order}")
        return order

    except BinanceAPIException as e:
        logging.error(f"Binance API Error: {e}")
        print("❌ Binance API Error:", e)
    except Exception as e:
        logging.error(f"General Error: {e}")
        print("❌ Error:", e)

# =========================
# VALIDATION
# =========================
def validate_side(side):
    return side in ["BUY", "SELL"]

def validate_type(order_type):
    return order_type in ["MARKET", "LIMIT"]

# =========================
# CLI LAYER
# =========================
def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading App")

    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # Validation
    if args.type == "LIMIT" and args.price is None:
        print("❌ Price is required for LIMIT order")
        return

    print("\n===== ORDER REQUEST =====")
    print("Symbol :", args.symbol)
    print("Side   :", args.side)
    print("Type   :", args.type)
    print("Qty    :", args.qty)
    print("Price  :", args.price)

    client = get_client()

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    if order:
        print("\n===== ORDER RESPONSE =====")
        print("Order ID      :", order.get("orderId"))
        print("Status        :", order.get("status"))
        print("Executed Qty  :", order.get("executedQty"))
        print("Avg Price     :", order.get("avgPrice", "N/A"))
        print("✅ Order placed successfully!")

# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()