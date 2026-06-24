import os
import time
import threading
import datetime
import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
from pyngrok import ngrok
from dashboard_html import DASHBOARD_HTML

app = Flask(__name__)
CORS(app)

# ==========================================
# CONFIGURATION & TOKENS
# ==========================================
NGROOK_AUTH_TOKEN = "3FZ3OZaE5f5li46oOKs12L1tzK7_4V1C5g6uCgm2UbcfwcHKK"

# Shared Real-time State
STATE = {
    "last_update": None,
    "portfolio": {
        "cash_inr": 50000,
        "cash_usd": 1000,
        "total_trades_executed": 0, # Total trades counter
        "portfolio_value_inr": 132450
    },
    "prices": {
        "NSE": {"RELIANCE": 2500, "TCS": 3900, "INFY": 1600},
        "NASDAQ": {"AAPL": 180, "TSLA": 175, "NVDA": 850} # US Stocks Added
    },
    "active_positions": [], # Abhi kaun sa trade chal raha hai
    "trades_history": []    # Purane saare trades ka record
}

def get_live_price(market, symbol):
    """Fetches real-time stock prices from Google Finance safely"""
    try:
        query = f"NSE:{symbol}" if market == "NSE" else f"NASDAQ:{symbol}"
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            div = soup.find('div', class_='BNeawe iBp4i AP7C9')
            if div:
                p_text = div.text.split()[0].replace(',', '')
                return float(p_text)
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
    return None

def paper_trading_logic():
    """Bot dynamic analysis loop for Indian & US Markets"""
    print("🚀 Advanced Paper Trading Engine Started...")
    
    while True:
        now = datetime.datetime.now()
        now_str = now.strftime("%H:%M:%S")
        STATE["last_update"] = now_str
        
        # 1. Update Prices
        for sym in STATE["prices"]["NSE"].keys():
            p = get_live_price("NSE", sym)
            if p: STATE["prices"]["NSE"][sym] = p
            
        for sym in STATE["prices"]["NASDAQ"].keys():
            p = get_live_price("NASDAQ", sym)
            if p: STATE["prices"]["NASDAQ"][sym] = p

        # 2. Check US Market Hours (Roughly 7:00 PM to 1:30 AM IST)
        is_us_market_open = (now.hour >= 19 or now.hour < 2)
        
        # 3. Simulate Paper Trades (Decision Engine)
        # Agar koi position nahi chal rahi, toh naya trade logic run karo
        if len(STATE["active_positions"]) == 0:
            # Decide market based on time
            market = "NASDAQ" if is_us_market_open else "NSE"
            symbol = random.choice(list(STATE["prices"][market].keys()))
            entry_p = STATE["prices"][market][symbol]
            
            new_trade = {
                "symbol": f"{symbol} LONG",
                "market": market,
                "entry_price": entry_p,
                "current_price": entry_p,
                "leverage": "3x (Virtual)",
                "pnl": 0,
                "status": "RUNNING",
                "time": now_str
            }
            STATE["active_positions"].append(new_trade)
            print(f"📥 Bot Opened Paper Position: {symbol} at {entry_p}")
            
        # 4. Update Ongoing Positions
        else:
            for pos in STATE["active_positions"]:
                curr_price = STATE["prices"][pos["market"]][pos["symbol"].split()[0]]
                pos["current_price"] = curr_price
                
                # PnL Calculation
                change_pct = ((curr_price - pos["entry_price"]) / pos["entry_price"]) * 100
                pos["pnl"] = round(change_pct * 3, 2) # 3x leverage impact
                
                # Exit Logic: Random target/stop hit simulation for paper trading
                if random.random() < 0.15: # 15% chance to close trade every 10 seconds
                    STATE["active_positions"].remove(pos)
                    pos["status"] = "FILLED"
                    pos["exit_time"] = now_str
                    STATE["trades_history"].insert(0, pos) # History mein add karo
                    STATE["portfolio"]["total_trades_executed"] += 1 # Counter up
                    print(f"📤 Bot Closed Position: {pos['symbol']} | Final PnL: {pos['pnl']}%")

        time.sleep(10)

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/state')
def get_state():
    return jsonify(STATE)

if __name__ == '__main__':
    # Start bot tracking thread
    t = threading.Thread(target=paper_trading_logic, daemon=True)
    t.start()
    
    if NGROOK_AUTH_TOKEN:
        try:
            ngrok.set_auth_token(NGROOK_AUTH_TOKEN)
            public_url = ngrok.connect(5000)
            print("\n" + "="*50)
            print(f"🌍 LIVE DASHBOARD URL: {public_url.public_url}")
            print("="*50 + "\n")
        except Exception as e:
            print(f"⚠️ Ngrok tunnel failed to start: {e}")

    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
