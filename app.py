import os
import random
import gradio as gr

class FabRichEngine:
    def __init__(self):
        self.equity = 248.50
        self.run_goal = 500.00
        self.available_cash = 238.08
        self.active_short_btc = True
        self.btc_entry = 66261.87
        self.btc_mark = 64021.13
        self.pnl_unrealized = 10.42
        
        self.twitter_feed = [
            {"user": "@CryptoWhale", "text": "Massive BTC spot sell wall detected on major orderbooks. Bearish pressure building.", "sentiment": "Bearish"},
            {"user": "@Macromonitor", "text": "Macro liquidity drying up. Risk-Off regime fully active across core systems.", "sentiment": "Bearish"},
            {"user": "@ElonMusk", "text": "Tesla might look back into green digital energy infrastructure soon.", "sentiment": "Bullish"}
        ]
        
        self.logs = [
            "open SHORT BTC 6x [breakout] 15m breakout",
            "close LONG BTC 6x stop-loss",
            "open LONG BTC 6x [breakout] 15m breakout"
        ]

bot = FabRichEngine()

def process_bot_logic():
    selected_tweet = random.choice(bot.twitter_feed)
    if selected_tweet["sentiment"] == "Bearish":
        bot.pnl_unrealized += 1.50
        bot.equity += 1.50
        status_msg = f"Processed alert from {selected_tweet['user']}: Market Sentiment is Bearish. Short position yielding profit!"
    else:
        bot.pnl_unrealized -= 1.10
        bot.equity -= 1.10
        status_msg = f"Processed alert from {selected_tweet['user']}: Market Sentiment is Bullish. Short position facing resistance."
        
    overview_html = f"""
    <div style='background: #ffffff; padding: 25px; border-radius: 16px; border: 1px solid #e5e7eb;'>
        <p style='color: #6b7280; font-size: 13px; font-weight: 600; margin: 0;'>Account Equity - Episode 4</p>
        <h1 style='color: #000000; font-size: 44px; font-weight: 800; margin: 5px 0;'>${bot.equity:,.2f}</h1>
        <p style='color: #047857; font-weight: 700; margin: 0;'>+${bot.pnl_unrealized:,.2f} (+148.50%)</p>
    </div>
    """
    
    position_html = f"""
    <div style='background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e5e7eb;'>
        <span style='background: #fee2e2; color: #b91c1c; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 4px;'>SHORT</span> <b>BTC 22x</b>
        <p style='color: #047857; font-weight: 700; margin: 0; margin-top: 10px;'>+${bot.pnl_unrealized:,.2f} (+74.40% ROI)</p>
    </div>
    """
    
    world_html = f"""
    <div style='background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e5e7eb;'>
        <h4 style='margin:0 0 10px 0;'>🔴 LIVE TWITTER FEED</h4>
        <p><b>{selected_tweet['user']}</b>: "{selected_tweet['text']}"</p>
    </div>
    """
    
    recent_fills_html = "".join([f"<div style='margin-bottom: 6px; color: #111827; font-weight:600;'>⚡ {log}</div>" for log in bot.logs])
    return overview_html, position_html, world_html, recent_fills_html, status_msg

luxury_css = "body, .gradio-container { background-color: #f8fafc !important; color: #000000 !important; }"

with gr.Blocks(css=luxury_css) as demo:
    gr.Markdown("# 🏛️ APEX TRADING CORE SYSTEMS")
    status_banner = gr.Textbox(label="Twitter NLP Engine Signal Status", value="Awaiting ticks...")
    
    with gr.Tabs():
        with gr.TabItem("📊 Overview"): overview_panel = gr.HTML()
        with gr.TabItem("⚡ Positions"): position_panel = gr.HTML()
        with gr.TabItem("🌍 World"): world_panel = gr.HTML()
        with gr.TabItem("📝 Recent Trades"): trades_panel = gr.HTML()
            
    refresh_btn = gr.Button("⚡ TICK SENTIMENT PROTOCOL")
    refresh_btn.click(process_bot_logic, inputs=None, outputs=[overview_panel, position_panel, world_panel, trades_panel, status_banner])
    demo.load(process_bot_logic, inputs=None, outputs=[overview_panel, position_panel, world_panel, trades_panel, status_banner])

# Render cloud specification
demo.launch(server_name="0.0.0.0", server_port=10000)
