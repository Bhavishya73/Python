<div align="center">
  <h1>⚡ Binance Futures CLI Trading Bot</h1>
  <p><i>A robust, production-ready execution layer for high-precision trading.</i></p>

  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Binance-Testnet-F3BA2F?style=for-the-badge&logo=binance&logoColor=black" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</div>

---

## 🌟 Overview
This project is a professional-grade trading execution engine designed for the **Binance Futures Testnet**. It bridges the gap between terminal commands and financial markets, allowing for rapid order execution while maintaining a high-fidelity audit trail through automated logging.

---

## 🏗️ Architecture Flow


1.  **CLI Input:** Parses symbol, side, and quantity via terminal.
2.  **Logic Validation:** Ensures data integrity (e.g., price requirements for LIMIT orders).
3.  **API Client:** Establishes a secure connection via `python-binance`.
4.  **Audit Trail:** Records all JSON responses and errors in `binance_app.log`.

---

## 🛠️ Key Features
| Feature | Description |
| :--- | :--- |
| **📉 Multi-Order** | Full support for `MARKET` and `LIMIT` order types. |
| **📜 Advanced Logging** | Timestamps every request/response for deep debugging. |
| **🛡️ Error Resilience** | Gracefully handles `BinanceAPIException` and network drops. |
| **💻 Interactive CLI** | Powered by `argparse` for a streamlined user experience. |

---

## 🚀 Getting Started

### 📋 Prerequisites
* Python 3.8 or higher.
* Active Binance Testnet API credentials.

### ⚙️ Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/binance-trading-bot.git](https://github.com/yourusername/binance-trading-bot.git)
   cd binance-trading-bot
2. Install necessary libraries:
  pip install -r requirements.txt

3. 📋 Usage Examples
✅ Market Buy Order
Bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
✅ Limit Sell Order
Bash
python main.py --symbol ETHUSDT --side SELL --type LIMIT --qty 0.1 --price 2500.50
👨‍💻 Technical Skills Demonstrated
Financial Data Engineering: Handling precision, leverage-ready quantity logic, and order types.

Backend Reliability: Implementing structured logging to replace simple print debugging.

API Integration: Mastering RESTful communication with high-security financial endpoints.

<div align="center">
<p>Distributed under the MIT License.</p>
<b>Developed with ❤️ by Bhavishya </b>
</div>
