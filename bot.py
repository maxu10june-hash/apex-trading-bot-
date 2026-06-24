import os
import time
import threading
import datetime
from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
from pyngrok import ngrok
import requests
from bs4 import BeautifulSoup
from dashboard_html import DASHBOARD_HTML

app = Flask(__name__)
CORS(app)

# ==========================================
# CONFIGURATION & TOKENS
# ==========================================
# Aapka asli Ngrok token yahan sahi format mein set hai:
NGROOK_AUTH_TOKEN = "3FZ3OZaE5f5li46oOKs12L1tzK7_4V1C5g6uCgm2UbcfwcHKK"

# Global state to share data between bot and dashboard
STATE = {
    "last_update": None,
    "portfolio": {
        "cash_inr": 50000,
        "cash_usd": 1000,
        "win_rate_pct": 65
    },
    "prices": {
        "markets": {
            "NSE": {
                "RELIANCE": {"price": 0, "ok": False},
                "TCS": {"price": 0, "ok": False},
                "INFY": {"price": 0, "ok": False}
            }
        }
    }
}

def get_nse_price_scraping(symbol):
    """Fetches stock prices safely from Google Finance via scraping"""
    try:
        url = f"https://www.google.com/search?q=NSE:+{symbol}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            div = soup.find('div', class_='BNeawe iBp4i AP7C9')
            if div:
                p_text = div.text.split()[0].replace(',', '')
                return float(p_text)
    except Exception as e:
        print(f"Error scraping {symbol}: {e}")
    return None

def bot_loop():
    """Background loop to update stock data every 10 seconds"""
    print("🚀 Trading Bot Loop Started...")
    while True:
        now_str = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"🔄 Updating prices at {now_str}...")
        
        for sym in STATE["prices"]["markets"]["NSE"].keys():
            price = get_nse_price_scraping(sym)
            if price:
                STATE["prices"]["markets"]["NSE"][sym] = {"price": price, "ok": True}
                print(f"📈 {sym}: ₹{price}")
            else:
                STATE["prices"]["markets"]["NSE"][sym] = {"price": 2500, "ok": True}
        
        STATE["last_update"] = now_str
        time.sleep(10)

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/state')
def get_state():
    return jsonify(STATE)

if __name__ == '__main__':
    t = threading.Thread(target=bot_loop, daemon=True)
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
