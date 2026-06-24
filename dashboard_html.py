DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Trading Bot - v3.1</title>
    <style>
        :root {
            --bg: #faf8f6;
            --card: #ffffff;
            --text-main: #111111;
            --text-sub: #666666;
            --maroon: #542227;
            --green: #22c55e;
            --red: #ef4444;
            --border: #f1eae4;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: var(--bg);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            padding: 20px;
            min-height: 100vh;
        }

        /* Profile Top Header Card */
        .profile-card {
            background: var(--card);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.03);
            margin-bottom: 20px;
            border: 1px solid var(--border);
        }
        .user-block { display: flex; align-items: center; gap: 16px; margin-bottom: 20px; }
        .avatar {
            width: 48px; height: 48px; background: #f5e6e6; color: var(--maroon);
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 18px;
        }
        .user-info .name { font-size: 18px; font-weight: 700; color: var(--text-main); }
        .user-info .sub { font-size: 12px; color: var(--text-sub); }

        /* Navigation Buttons - Maroon Pill Style */
        .nav-container { display: flex; flex-direction: column; gap: 8px; }
        .tab-btn {
            background: transparent; border: none; text-align: left;
            padding: 14px 20px; border-radius: 16px; font-size: 14px; font-weight: 600;
            color: var(--text-sub); cursor: pointer; transition: all 0.2s ease;
            display: flex; align-items: center; gap: 10px;
        }
        .tab-btn.active {
            background: var(--maroon);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(84, 34, 39, 0.2);
        }

        /* Main View Panels */
        .tab-panel { display: none; margin-top: 20px; }
        .tab-panel.active { display: block; }

        /* Elegant Content Cards */
        .card {
            background: var(--card);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.03);
            margin-bottom: 16px;
            border: 1px solid var(--border);
        }
        .card-title { font-size: 20px; font-weight: 700; color: var(--text-main); margin-bottom: 16px; }
        .card-label { font-size: 12px; font-weight: 600; color: var(--text-sub); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
        
        /* Account Equity Serif-Style Big Numbers */
        .equity-num { font-size: 38px; font-weight: 700; color: var(--text-main); font-family: "Times New Roman", Times, serif; margin: 8px 0; }
        .profit-text { color: var(--green); font-size: 14px; font-weight: 600; }
        .loss-text { color: var(--red); font-size: 14px; font-weight: 600; }

        /* Multi-column Grid */
        .sub-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }
        .sub-val { font-size: 18px; font-weight: 700; color: var(--text-main); margin-top: 2px; }

        /* Lists & Rows */
        .list-row { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid var(--border); }
        .list-row:last-child { border-bottom: none; }
        .list-left { font-weight: 600; color: var(--text-main); }
        .list-right { font-weight: 700; color: var(--text-main); }
        .list-subtext { font-size: 11px; color: var(--text-sub); margin-top: 2px; }

        /* Special Styled Highlight Box */
        .spec-box { background: #fafafa; border-left: 4px solid var(--maroon); padding: 14px; border-radius: 0 12px 12px 0; margin-bottom: 12px; }
    </style>
</head>
<body>

    <div class="profile-card">
        <div class="user-block">
            <div class="avatar">F</div>
            <div class="user-info">
                <div class="name">@FabRichhhhhh</div>
                <div class="sub">Apex Trading Bot - v3.1</div>
            </div>
        </div>
        <div class="nav-container">
            <button class="tab-btn active" onclick="openTab(event, 'overview')">● Overview</button>
            <button class="tab-btn" onclick="openTab(event, 'portfolio')">● Live Portfolio</button>
            <button class="tab-btn" onclick="openTab(event, 'positions')">● Positions</button>
            <button class="tab-btn" onclick="openTab(event, 'trades')">● Trades</button>
        </div>
    </div>

    <div id="overview" class="tab-panel active">
        <div class="card">
            <div class="card-title">Account Equity</div>
            <div class="equity-num">$248.50</div>
            <div class="profit-text">+$148.50 (148.50%)</div>
            
            <div class="sub-grid">
                <div>
                    <div class="card-label">INR Capital</div>
                    <div class="sub-val">₹50,000</div>
                </div>
                <div>
                    <div class="card-label">USD Capital</div>
                    <div class="sub-val">$1,000</div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="card-title">Live Prices</div>
            <div class="list-row">
                <div class="list-left">INFY</div>
                <div class="list-right">₹2,500</div>
            </div>
            <div class="list-row">
                <div class="list-left">RELIANCE</div>
                <div class="list-right">₹2,500</div>
            </div>
        </div>
    </div>

    <div id="portfolio" class="tab-panel">
        <div class="card">
            <div class="card-title">Total Portfolio Value</div>
            <div class="equity-num" style="color: var(--maroon);">₹1,32,450</div>
            <div class="profit-text">Net Yield: +₹8,455 (6.8%)</div>
            
            <div class="sub-grid">
                <div>
                    <div class="card-label">Invested Capital</div>
                    <div class="sub-val">₹1,23,995</div>
                </div>
                <div>
                    <div class="card-label">Available Cash</div>
                    <div class="sub-val">₹8,455</div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="card-title">Asset Allocation</div>
            <div class="list-row">
                <div class="list-left">Equities (Stocks)</div>
                <div class="list-right">70%</div>
            </div>
            <div class="list-row">
                <div class="list-left">Crypto Assets</div>
                <div class="list-right">20%</div>
            </div>
            <div class="list-row">
                <div class="list-left">Liquidity Margin</div>
                <div class="list-right">10%</div>
            </div>
        </div>
    </div>

    <div id="positions" class="tab-panel">
        <div class="card">
            <div class="card-title">Open Positions</div>
            <div class="spec-box">
                <div style="display:flex; justify-content: space-between; font-weight:700;">
                    <span>RELIANCE LONG</span>
                    <span class="profit-text">+$450 (1.8%)</span>
                </div>
                <div class="list-subtext">Size: ₹25,000 • 5x Leverage</div>
            </div>
        </div>
    </div>

    <div id="trades" class="tab-panel">
        <div class="card">
            <div class="card-title">Past Executed Logs</div>
            <div class="list-row">
                <div>
                    <div class="list-left">INFY LONG</div>
                    <div class="list-subtext">Filled • 04:12:10</div>
                </div>
                <div style="text-align: right;">
                    <div class="profit-text">+$85.40</div>
                    <div class="list-subtext">3x Lev</div>
                </div>
            </div>
            <div class="list-row">
                <div>
                    <div class="list-left">RELIANCE SHORT</div>
                    <div class="list-subtext">Filled • 02:45:18</div>
                </div>
                <div style="text-align: right;">
                    <div class="loss-text">-$32.10</div>
                    <div class="list-subtext">5x Lev</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function openTab(evt, tabName) {
            var i, tabPanel, tabBtn;
            tabPanel = document.getElementsByClassName("tab-panel");
            for (i = 0; i < tabPanel.length; i++) { tabPanel[i].classList.remove("active"); }
            tabBtn = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tabBtn.length; i++) { tabBtn[i].classList.remove("active"); }
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }
    </script>
</body>
</html>
"""
