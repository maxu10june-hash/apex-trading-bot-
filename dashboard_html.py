DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AlgoBot Dashboard</title>
    <style>
        :root {
            --bg: #0a0e1a;
            --card: #111827;
            --border: #1f2937;
            --green: #10b981;
            --red: #ef4444;
            --blue: #3b82f6;
            --yellow: #f59e0b;
            --text: #f1f5f9;
            --muted: #94a3b8;
            --accent: #6366f1;
            --nav-bg: #1e1b4b;
        }
        * { margin:0; padding:0; box-sizing:border-box; transition: background 0.15s ease, color 0.15s ease; }
        body {
            background: var(--bg); color: var(--text);
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
            font-size: 14px; min-height: 100vh; -webkit-overflow-scrolling: touch; padding: 16px;
        }
        .header {
            background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
            padding: 16px; border-radius: 16px; border: 1px solid var(--border);
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .brand { display: flex; align-items: center; gap: 12px; }
        .brand-icon { font-size: 24px; }
        .brand-name { font-size: 18px; font-weight: 700; letter-spacing: -0.5px; color: #fff; }
        .brand-sub { font-size: 11px; color: var(--muted); margin-top: 2px; }
        
        .status-tag { display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600; color: var(--green); }
        .status-dot { width: 8px; height: 8px; background: var(--green); border-radius: 50%; box-shadow: 0 0 12px var(--green); }
        .server-time { font-size: 11px; color: var(--muted); text-align: right; margin-top: 4px; font-family: monospace; }

        /* Navigation Scrollbar styling */
        .nav-container {
            overflow-x: auto; display: flex; gap: 8px; margin-bottom: 20px;
            padding-bottom: 8px; -webkit-overflow-scrolling: touch;
        }
        .nav-container::-webkit-scrollbar { height: 4px; }
        .nav-container::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }
        
        .tab-btn {
            background: var(--card); border: 1px solid var(--border); color: var(--muted);
            padding: 10px 18px; border-radius: 25px; cursor: pointer; font-weight: 600;
            font-size: 13px; white-space: nowrap; display: flex; align-items: center; gap: 6px;
        }
        .tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3); }

        /* Tab Content */
        .tab-panel { display: none; }
        .tab-panel.active { display: block; animation: fadeIn 0.25s ease-in-out; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

        /* Metrics Grid */
        .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 16px; }
        .card {
            background: var(--card); border: 1px solid var(--border);
            padding: 18px; border-radius: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .card-full { grid-column: span 2; }
        .card-label { font-size: 11px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.75px; margin-bottom: 6px; }
        .card-val { font-size: 24px; font-weight: 700; color: #fff; letter-spacing: -0.5px; }
        .card-sub { font-size: 12px; margin-top: 4px; font-weight: 600; }

        /* Color classes */
        .pos-profit { color: var(--green); }
        .pos-loss { color: var(--red); }
        
        /* List rows */
        .list-item {
            display: flex; justify-content: space-between; align-items: center;
            padding: 14px 0; border-bottom: 1px solid var(--border);
        }
        .list-item:last-child { border-bottom: none; }
        .list-main { font-weight: 600; color: #fff; }
        .list-sub { font-size: 12px; color: var(--muted); margin-top: 2px; }

        /* Spec Boxes */
        .spec-box {
            background: rgba(255, 255, 255, 0.02); border-left: 4px solid var(--accent);
            padding: 14px; border-radius: 0 12px 12px 0; margin-bottom: 12px;
        }
        .spec-box.green-bar { border-left-color: var(--green); }
        .spec-box.red-bar { border-left-color: var(--red); }
        .spec-box.blue-bar { border-left-color: var(--blue); }
    </style>
</head>
<body>

    <div class="header">
        <div class="brand">
            <div class="brand-icon">🤖</div>
            <div>
                <div class="brand-name">AlgoBot</div>
                <div class="brand-sub">@FabRichhhhhh • v3.0</div>
            </div>
        </div>
        <div>
            <div class="status-tag"><div class="status-dot"></div>Live</div>
            <div class="server-time">UTC: 05:31:42</div>
        </div>
    </div>

    <div class="nav-container">
        <button class="tab-btn active" onclick="openTab(event, 'overview')">📊 Overview</button>
        <button class="tab-btn" onclick="openTab(event, 'positions')">💼 Positions</button>
        <button class="tab-btn" onclick="openTab(event, 'evolution')">⚡ Evolution</button>
        <button class="tab-btn" onclick="openTab(event, 'strategy')">📖 Strategy Book</button>
        <button class="tab-btn" onclick="openTab(event, 'world')">🌍 World Sentiment</button>
        <button class="tab-btn" onclick="openTab(event, 'lessons')">💡 Lesson Bank</button>
        <button class="tab-btn" onclick="openTab(event, 'trades')">📜 Trades History</button>
    </div>

    <div id="overview" class="tab-panel active">
        <div class="grid">
            <div class="card card-full" style="background: linear-gradient(135deg, #1e1b4b 0%, #111827 100%);">
                <div class="card-label">Account Equity</div>
                <div class="card-val" style="font-size: 32px;">$248.50</div>
                <div class="card-sub pos-profit">+$148.50 (148.50%)</div>
            </div>
            <div class="card">
                <div class="card-label">INR Capital</div>
                <div class="card-val">₹50,000</div>
            </div>
            <div class="card">
                <div class="card-label">USD Capital</div>
                <div class="card-val">$1,000</div>
            </div>
            <div class="card card-full">
                <div class="card-label">Live Tracking Status</div>
                <div class="list-item">
                    <div><span class="list-main">AI Analysis Loops</span></div>
                    <div><span style="background: rgba(99,102,241,0.15); color:#a5b4fc; padding:4px 10px; border-radius:12px; font-size:11px; font-weight:700;">14 Active Runs</span></div>
                </div>
                <div class="list-item">
                    <div><span class="list-main">Win Rate Metrics</span></div>
                    <div><span class="pos-profit">65% Target Met</span></div>
                </div>
            </div>
        </div>
    </div>

    <div id="positions" class="tab-panel">
        <div class="card">
            <div class="card-label" style="margin-bottom:12px;">Live Leverage Positions</div>
            <div class="spec-box green-bar">
                <div style="display:flex; justify-content:between; align-items:center; width:100%; justify-content: space-between;">
                    <span class="list-main">RELIANCE LONG</span>
                    <span style="font-size:11px; background:rgba(16,185,129,0.15); color:var(--green); padding:2px 8px; border-radius:6px; font-weight:700;">5x Leverage</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:var(--muted);">
                    <span>Size: ₹25,000</span>
                    <span>P&L: <span class="pos-profit">+$450 (1.8%)</span></span>
                </div>
            </div>
            <div class="spec-box red-bar">
                <div style="display:flex; justify-content:between; align-items:center; width:100%; justify-content: space-between;">
                    <span class="list-main">TCS SHORT</span>
                    <span style="font-size:11px; background:rgba(239,68,68,0.15); color:var(--red); padding:2px 8px; border-radius:6px; font-weight:700;">3x Leverage</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:var(--muted);">
                    <span>Size: ₹15,000</span>
                    <span>P&L: <span class="pos-loss">-$120 (-0.8%)</span></span>
                </div>
            </div>
        </div>
    </div>

    <div id="evolution" class="tab-panel">
        <div class="card" style="text-align: center; padding: 28px 16px;">
            <div style="font-size: 44px; margin-bottom: 12px; filter: drop-shadow(0 0 10px rgba(99,102,241,0.5));">⚡</div>
            <div class="card-label">Bot Autonomous Growth Level</div>
            <div class="card-val" style="color: var(--accent); font-size: 36px; margin: 8px 0;">LEVEL 4</div>
            <div style="background: #1f2937; border-radius: 20px; height: 10px; width: 100%; margin: 18px 0; overflow:hidden; border: 1px solid #374151;">
                <div style="background: linear-gradient(90deg, #6366f1, #818cf8); width: 75%; height: 100%; border-radius:20px;"></div>
            </div>
            <p style="color: var(--muted); font-size: 12px; line-height: 1.5;">75% Evolved to Level 5. Upgrades trigger automatically after completing evaluation cycles and maintaining an optimal risk-to-reward ratio.</p>
        </div>
    </div>

    <div id="strategy" class="tab-panel">
        <div class="card">
            <div class="card-label" style="margin-bottom:12px;">Active AI Trading Strategies</div>
            <div class="spec-box blue-bar">
                <span class="list-main">1. Mean Reversion v2.1</span>
                <p style="font-size:12px; color:var(--muted); margin-top:6px; line-height:1.4;">Bot shifted RSI parameters dynamically to 28/72 to filter false liquidity breakouts based on past cycles.</p>
            </div>
            <div class="spec-box blue-bar">
                <span class="list-main">2. Breakout Momentum v1.5</span>
                <p style="font-size:12px; color:var(--muted); margin-top:6px; line-height:1.4;">Scans high-volume breakout patterns on 15m frames. Currently re-weighting via global macro sentiment pipelines.</p>
            </div>
        </div>
    </div>

    <div id="world" class="tab-panel">
        <div class="grid">
            <div class="card" style="text-align: center;">
                <div class="card-label">Global Sentiment</div>
                <div class="card-val" style="color: var(--yellow);">GREED</div>
                <div style="font-size: 11px; color: var(--muted); margin-top: 4px;">Index Meter: 64/100</div>
            </div>
            <div class="card" style="text-align: center;">
                <div class="card-label">Macro Flow Filter</div>
                <div class="card-val" style="color: var(--blue);">BULLISH</div>
                <div style="font-size: 11px; color: var(--muted); margin-top: 4px;">US-India Overlay</div>
            </div>
            <div class="card card-full">
                <div class="card-label" style="margin-bottom:8px;">AI Scanned Headlines</div>
                <div class="list-item" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                    <span style="font-weight: 600; color:#fff;">📰 Fed Signals Stable Benchmark Rates</span>
                    <span style="font-size:11px; color:var(--green);">Bot Action: Increased initial asset allocations by +5%</span>
                </div>
                <div class="list-item" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                    <span style="font-weight: 600; color:#fff;">📰 Tech Indicies Facing Heavy Resistance</span>
                    <span style="font-size:11px; color:var(--yellow);">Bot Action: Tightened trailing stop thresholds on INFY</span>
                </div>
            </div>
        </div>
    </div>

    <div id="lessons" class="tab-panel">
        <div class="card">
            <div class="card-label" style="margin-bottom:12px;">Self-Compiled Lesson Logs</div>
            <div class="spec-box red-bar">
                <span class="list-main" style="color:var(--red);">Lesson #104 (Execution Risk)</span>
                <p style="font-size:12px; color:var(--muted); margin-top:6px; font-style:italic; line-height:1.4;">"High volatility news windows trigger heavy slippage. Halting direct execution 15 minutes before scheduled high-impact events."</p>
            </div>
            <div class="spec-box green-bar">
                <span class="list-main" style="color:var(--green);">Lesson #103 (Leverage Scale)</span>
                <p style="font-size:12px; color:var(--muted); margin-top:6px; font-style:italic; line-height:1.4;">"5x leverage setups on erratic counters over-expose net capital. Setting system cap at 3x for volatile high-beta stocks."</p>
            </div>
        </div>
    </div>

    <div id="trades" class="tab-panel">
        <div class="card">
            <div class="card-label" style="margin-bottom:8px;">Past Executed Logs</div>
            <div class="list-item">
                <div>
                    <span class="list-main">INFY LONG</span><br>
                    <span class="list-sub">Filled • 04:12:10</span>
                </div>
                <div style="text-align: right;">
                    <span class="pos-profit">+$85.40</span><br>
                    <span class="list-sub">3x Lev</span>
                </div>
            </div>
            <div class="list-item">
                <div>
                    <span class="list-main">RELIANCE SHORT</span><br>
                    <span class="list-sub">Filled • 02:45:18</span>
                </div>
                <div style="text-align: right;">
                    <span class="pos-loss">-$32.10</span><br>
                    <span class="list-sub">5x Lev</span>
                </div>
            </div>
            <div class="list-item">
                <div>
                    <span class="list-main">TCS LONG</span><br>
                    <span class="list-sub">Filled • Yesterday</span>
                </div>
                <div style="text-align: right;">
                    <span class="pos-profit">+$95.20</span><br>
                    <span class="list-sub">3x Lev</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        function openTab(evt, tabName) {
            var i, tabPanel, tabBtn;
            tabPanel = document.getElementsByClassName("tab-panel");
            for (i = 0; i < tabPanel.length; i++) {
                tabPanel[i].classList.remove("active");
            }
            tabBtn = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tabBtn.length; i++) {
                tabBtn[i].classList.remove("active");
            }
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }
    </script>
</body>
</html>
"""
