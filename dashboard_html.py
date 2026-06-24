DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AlgoBot Autonomous Dashboard</title>
    <style>
        :root {
            --bg: #0d1117;
            --card: #161b22;
            --border: #30363d;
            --green: #238636;
            --red: #da3633;
            --blue: #58a6ff;
            --yellow: #d29922;
            --text: #c9d1d9;
            --text-muted: #8b949e;
            --purple: #8957e5;
        }
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            background: var(--bg); color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 14px; min-height: 100vh; padding: 15px;
        }
        .header {
            display: flex; justify-content: space-between; align-items: center;
            padding: 15px; background: var(--card); border: 1px solid var(--border);
            border-radius: 12px; margin-bottom: 15px;
        }
        .bot-profile { display: flex; align-items: center; gap: 10px; }
        .bot-avatar {
            width: 40px; height: 40px; background: var(--purple);
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-size: 20px;
        }
        .bot-name h2 { font-size: 16px; color: #fff; }
        .bot-name p { font-size: 12px; color: var(--text-muted); }
        
        /* Navigation Tabs */
        .nav-scroll { overflow-x: auto; display: flex; gap: 10px; margin-bottom: 15px; padding-bottom: 5px; }
        .nav-btn {
            background: var(--card); border: 1px solid var(--border); color: var(--text);
            padding: 8px 16px; border-radius: 20px; cursor: pointer; white-space: nowrap;
            transition: all 0.2s; font-weight: 500;
        }
        .nav-btn.active { background: var(--purple); border-color: var(--purple); color: #fff; }
        
        /* Content Sections */
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        
        /* Cards Layout */
        .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 15px; }
        .card {
            background: var(--card); border: 1px solid var(--border);
            padding: 15px; border-radius: 12px; margin-bottom: 15px;
        }
        .card-title { font-size: 12px; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;}
        .card-value { font-size: 22px; font-weight: bold; color: #fff; }
        
        /* Utilities */
        .text-green { color: #58a6ff !important; color: var(--green) !important; font-weight: bold; }
        .text-red { color: var(--red) !important; font-weight: bold; }
        .badge { padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
        .badge-purple { background: rgba(137, 87, 229, 0.2); color: #d3b6ff; border: 1px solid var(--purple); }
        
        /* Lists and Tables */
        .data-row {
            display: flex; justify-content: space-between; padding: 10px 0;
            border-bottom: 1px solid var(--border);
        }
        .data-row:last-child { border: 0; }
        
        /* Lesson & Strategy Styling */
        .box-item {
            background: rgba(255,255,255,0.03); border-left: 4px solid var(--purple);
            padding: 12px; border-radius: 0 8px 8px 0; margin-bottom: 10px;
        }
        .box-item.success { border-left-color: var(--green); }
        .box-item.danger { border-left-color: var(--red); }
    </style>
</head>
<body>

    <!-- Header -->
    <div class="header">
        <div class="bot-profile">
            <div class="bot-avatar">🤖</div>
            <div class="bot-name">
                <h2>@FabRichhhhhh</h2>
                <p>Apex Autonomous Trader v3.0</p>
            </div>
        </div>
        <div style="text-align: right;">
            <span style="color: var(--green); font-size: 12px;">● Live</span>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 3px;">UTC: 05:14:52</div>
        </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="nav-scroll">
        <button class="nav-btn active" onclick="switchTab('overview')">Overview</button>
        <button class="nav-btn" onclick="switchTab('positions')">Positions</button>
        <button class="nav-btn" onclick="switchTab('evolution')">Evolution</button>
        <button class="nav-btn" onclick="switchTab('strategy')">Strategy Book</button>
        <button class="nav-btn" onclick="switchTab('world')">World Sentiment</button>
        <button class="nav-btn" onclick="switchTab('lessons')">Lesson Bank</button>
        <button class="nav-btn" onclick="switchTab('trades')">Trades History</button>
    </div>

    <!-- 1. OVERVIEW TAB -->
    <div id="overview" class="tab-content active">
        <div class="card" style="background: linear-gradient(135deg, #1f1535, #161b22);">
            <div class="card-title">Account Equity</div>
            <div class="card-value" style="font-size: 28px;">$248.50</div>
            <div class="text-green" style="font-size: 13px; margin-top: 5px;">+$148.50 (148.50%)</div>
        </div>
        <div class="grid-2">
            <div class="card">
                <div class="card-title">INR Capital</div>
                <div class="card-value">₹50,000</div>
            </div>
            <div class="card">
                <div class="card-title">USD Capital</div>
                <div class="card-value">$1,000</div>
            </div>
        </div>
        <div class="card">
            <div class="card-title">Autonomous Status</div>
            <div class="data-row"><span>AI Decisions Today</span><span class="badge badge-purple">14 Analysis Runs</span></div>
            <div class="data-row"><span>Win Rate Level</span><span class="text-green">65% Win Rate</span></div>
        </div>
    </div>

    <!-- 2. POSITIONS TAB -->
    <div id="positions" class="tab-content">
        <div class="card">
            <div class="card-title">Active Leverage Positions</div>
            <div class="box-item danger" style="margin-top: 10px;">
                <div style="display:flex; justify-content:space-between; margin-bottom: 5px;">
                    <strong>RELIANCE LONG</strong>
                    <span class="badge badge-purple">Leverage: 5x</span>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:12px; color:var(--text-muted);">
                    <span>Size: ₹25,000</span>
                    <span>Unrealized P&L: <span class="text-green">+$450 (1.8%)</span></span>
                </div>
            </div>
            <div class="box-item success">
                <div style="display:flex; justify-content:space-between; margin-bottom: 5px;">
                    <strong>TCS SHORT</strong>
                    <span class="badge badge-purple">Leverage: 3x</span>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:12px; color:var(--text-muted);">
                    <span>Size: ₹15,000</span>
                    <span>Unrealized P&L: <span class="text-red">-$120 (-0.8%)</span></span>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. EVOLUTION TAB -->
    <div id="evolution" class="tab-content">
        <div class="card" style="text-align: center; padding: 25px 15px;">
            <div style="font-size: 50px; margin-bottom: 10px;">⚡</div>
            <div class="card-title">Bot Self-Evolution Level</div>
            <div class="card-value" style="color: var(--purple); font-size: 32px; margin: 10px 0;">LEVEL 4</div>
            <div style="background: #21262d; border-radius: 10px; height: 8px; width: 100%; margin: 15px 0; overflow:hidden;">
                <div style="background: var(--purple); width: 75%; height: 100%;"></div>
            </div>
            <p style="color: var(--text-muted); font-size: 12px;">75% Evolved to Level 5. Upgrades trigger automatically after processing market cycles and maintaining a positive win rate.</p>
        </div>
    </div>

    <!-- 4. STRATEGY BOOK TAB -->
    <div id="strategy" class="tab-content">
        <div class="card">
            <div class="card-title">Active AI Strategy Book</div>
            <div class="box-item" style="border-left-color: var(--blue);">
                <strong>1. Mean Reversion v2.1 (Upgraded)</strong>
                <p style="font-size:12px; color:var(--text-muted); margin-top:5px;">Bot adjusted RSI thresholds from 30/70 to 28/72 to avoid false breakouts based on recent losses.</p>
            </div>
            <div class="box-item" style="border-left-color: var(--blue);">
                <strong>2. Breakout Momentum v1.5</strong>
                <p style="font-size:12px; color:var(--text-muted); margin-top:5px;">Tracks high volume breakouts on 15-minute charts. Currently upgrading weight metrics using macro data flows.</p>
            </div>
        </div>
    </div>

    <!-- 5. WORLD SENTIMENT TAB -->
    <div id="world" class="tab-content">
        <div class="grid-2">
            <div class="card" style="text-align: center;">
                <div class="card-title">Global Sentiment</div>
                <div class="card-value" style="color: var(--yellow);">GREED</div>
                <span style="font-size: 11px; color: var(--text-muted);">Index: 64/100</span>
            </div>
            <div class="card" style="text-align: center;">
                <div class="card-title">Macro Flow Weight</div>
                <div class="card-value" style="color: var(--blue);">BULLISH</div>
                <span style="font-size: 11px; color: var(--text-muted);">US/India Correl.</span>
            </div>
        </div>
        <div class="card">
            <div class="card-title">Processed News Headlines</div>
            <div class="data-row" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                <span style="font-weight: 500;">🌐 Fed Signals Stable Interest Rates</span>
                <small style="color: var(--text-muted);">Bot Action: Increased long entry sizes by 5%</small>
            </div>
            <div class="data-row" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                <span style="font-weight: 500;">🌐 Tech Stocks Facing Resistance at Highs</span>
                <small style="color: var(--text-muted);">Bot Action: Tightened trailing stop-loss on INFY</small>
            </div>
        </div>
    </div>

    <!-- 6. LESSON BANK TAB -->
    <div id="lessons" class="tab-content">
        <div class="card">
            <div class="card-title">Bot Self-Taught Lessons</div>
            <div class="box-item danger">
                <strong>Lesson #104 (Risk Management)</strong>
                <p style="font-size:12px; color:var(--text-muted); margin-top:5px;">"Entering trades 10 minutes before major high-impact news leads to high slippage. I will now pause execution 15 mins prior."</p>
            </div>
            <div class="box-item success">
                <strong>Lesson #103 (Leverage Control)</strong>
                <p style="font-size:12px; color:var(--text-muted); margin-top:5px;">"5x Leverage on high volatility stock INFY over-exposed capital. Capped max leverage to 3x for high-beta stocks."</p>
            </div>
        </div>
    </div>

    <!-- 7. TRADES HISTORY TAB -->
    <div id="trades" class="tab-content">
        <div class="card">
            <div class="card-title">Executed Trades Log</div>
            
            <!-- Profit Trade (Green) -->
            <div class="data-row">
                <div>
                    <strong>INFY LONG</strong><br>
                    <small style="color: var(--text-muted);">Completed • 04:12:10</small>
                </div>
                <div style="text-align: right;">
                    <span class="text-green">+$85.40</span><br>
                    <small style="color: var(--text-muted);">Leverage 3x</small>
                </div>
            </div>

            <!-- Loss Trade (Red) -->
            <div class="data-row">
                <div>
                    <strong>RELIANCE SHORT</strong><br>
                    <small style="color: var(--text-muted);">Completed • 02:45:18</small>
                </div>
                <div style="text-align: right;">
                    <span class="text-red">-$32.10</span><br>
                    <small style="color: var(--text-muted);">Leverage 5x</small>
                </div>
            </div>

            <!-- Profit Trade (Green) -->
            <div class="data-row">
                <div>
                    <strong>TCS LONG</strong><br>
                    <small style="color: var(--text-muted);">Completed • Yesterday</small>
                </div>
                <div style="text-align: right;">
                    <span class="text-green">+$95.20</span><br>
                    <small style="color: var(--text-muted);">Leverage 3x</small>
                </div>
            </div>

        </div>
    </div>

    <!-- JavaScript to Handle Tab Switching -->
    <script>
        function switchTab(tabId) {
            // Remove active class from all buttons and tabs
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and target tab
            event.currentTarget.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        }
    </script>
</body>
</html>
"""
