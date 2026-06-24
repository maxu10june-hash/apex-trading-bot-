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

STATE = {
    "last_update": None,
    "portfolio": {
        "cash_inr": 50000,
        "cash_usd": 1000,
        "total_trades_executed": 0,
        "portfolio_value_inr": 132450
    },
    "prices": {
        "NSE": {"RELIANCE": 2500, "TCS": 3900, "INFY": 1600},
        "NASDAQ": {"AAPL": 180, "TSLA": 175, "NVDA": 850}
    },
    "active_positions": [],
    "trades_history": []
}

def get_live_price(market, symbol):
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
    print("🚀 Advanced Paper Trading Engine Started...")
    
    while True:
        # Render server (UTC) ko Indian Time (IST) mein convert karna
        utc_now = datetime.datetime.utcnow()
        ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
        now_str = ist_now.strftime("%H:%M:%S")
        STATE["last_update"] = now_str
        
        # 1. Update Prices
        for sym in STATE["prices"]["NSE"].keys():
            p = get_live_price("NSE", sym)
            if p: STATE["prices"]["NSE"][sym] = p
            
        for sym in STATE["prices"]["NASDAQ"].keys():
            p = get_live_price("NASDAQ", sym)
            if p: STATE["prices"]["NASDAQ"][sym] = p

        # 2. Check US Market Hours using IST (7:00 PM to 1:30 AM IST)
        is_us_market_open = (ist_now.hour >= 19 or ist_now.hour < 2)
        
        # 3. Decision Engine
        if len(STATE["active_positions"]) == 0:
            market = "NASDAQ" if is_us_market_open else "NSE"
            symbol = random.choice(list(STATE["prices"][market].keys()))
            entry_p = STATE["prices"][market][symbol]
            
            new_trade = {
                "symbol": f"{symbol} LONG" if market == "NASDAQ" else f"{symbol} LONG",
                "market": market,
                "entry_price": entry_p,
                "current_price": entry_p,
                "leverage": "3x (Virtual)",
                "pnl": 0,
                "status": "RUNNING",
                "time": now_str,
                "hold_duration": 0
            }
            STATE["active_positions"].append(new_trade)
            print(f"📥 Opened Position based on IST: {symbol} at {entry_p} (Market: {market})")
            
        # 4. Update Ongoing Positions
        else:
            for pos in STATE["active_positions"]:
                pos["hold_duration"] += 1
                
                # Dynamic market fluctuation code taaki trades live move karein
                market_fluctuation = random.uniform(-0.008, 0.009) 
                curr_price = round(STATE["prices"][pos["market"]][pos["symbol"].split()[0]] * (1 + market_fluctuation), 2)
                pos["current_price"] = curr_price
                
                # 3x Leverage PnL
                change_pct = ((curr_price - pos["entry_price"]) / pos["entry_price"]) * 100
                pos["pnl"] = round(change_pct * 3, 2) 
                
                # Exit constraint: Hold for minimum 1-2 minutes (6 loops) before closing randomly
                if pos["hold_duration"] >= 6 and random.random() < 0.20: 
                    STATE["active_positions"].remove(pos)
                    pos["status"] = "FILLED"
                    pos["exit_time"] = now_str
                    STATE["trades_history"].insert(0, pos)
                    STATE["portfolio"]["total_trades_executed"] += 1
                    print(f"📤 Closed Position: {pos['symbol']} | Final PnL: {pos['pnl']}%")

        time.sleep(10)

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/state')
def get_state():
    return jsonify(STATE)

if __name__ == '__main__':
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
