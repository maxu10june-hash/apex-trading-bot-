# dashboard_html.py

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Trading Bot - Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #fcfbfa; color: #333; padding: 20px; display: flex; justify-content: center; }
        .container { width: 100%; max-width: 450px; background: white; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 24px; border: 1px solid #f0ede9; }
        
        /* Menu Tabs */
        .menu-list { list-style: none; margin-bottom: 24px; }
        .menu-item { display: flex; align-items: center; padding: 14px 18px; margin-bottom: 8px; border-radius: 14px; font-weight: 600; color: #666; cursor: pointer; transition: 0.2s; }
        .menu-item:hover { background-color: #f7f4f0; }
        .menu-item.active { background-color: #501c1c; color: white; }
        .dot { width: 8px; height: 8px; background-color: #999; border-radius: 50%; margin-right: 12px; }
        .menu-item.active .dot { background-color: white; }
        
        /* Sections */
        .section-title { font-size: 20px; font-weight: 800; color: #111; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; }
        .counter-badge { font-size: 14px; background: #501c1c; color: white; padding: 4px 10px; border-radius: 12px; font-weight: bold; }
        .display-section { display: none; }
        .display-section.active { display: block; }
        
        /* Trade Cards */
        .trade-card { padding: 16px; border-bottom: 1px solid #f0ede9; display: flex; justify-content: space-between; align-items: center; }
        .trade-card:last-child { border-bottom: none; }
        .trade-info h4 { font-size: 15px; font-weight: 700; color: #111; margin-bottom: 4px; }
        .trade-info p { font-size: 12px; color: #888; }
        .trade-meta { text-align: right; }
        .pnl { font-weight: 700; font-size: 15px; }
        .pnl.profit { color: #27ae60; }
        .pnl.loss { color: #c0392b; }
        .lev { font-size: 12px; color: #888; margin-top: 4px; }
        
        /* Empty State */
        .empty-state { text-align: center; color: #999; padding: 30px 10px; font-size: 14px; font-style: italic; }
    </style>
</head>
<body>

<div class="container">
    <!-- Menu Sidebar / Tabs -->
    <ul class="menu-list">
        <li class="menu-item" onclick="switchTab('overview')"><span class="dot"></span> Overview</li>
        <li class="menu-item active" onclick="switchTab('positions')"><span class="dot"></span> Positions</li>
        <li class="menu-item" onclick="switchTab('history')"><span class="dot"></span> Trades History</li>
    </ul>

    <hr style="border: 0; border-top: 1px solid #f0ede9; margin-bottom: 20px;">

    <!-- 1. OVERVIEW TAB -->
    <div id="overview" class="display-section">
        <div class="section-title">Account Overview</div>
        <div style="background: #fdfaf6; padding: 16px; border-radius: 14px; margin-bottom: 12px; border: 1px solid #f5f0ea;">
            <p style="font-size: 13px; color: #666;">Virtual Cash (USD)</p>
            <h2 id="cash-usd" style="color: #111; margin-top: 4px;">$1,000.00</h2>
        </div>
        <div style="background: #fdfaf6; padding: 16px; border-radius: 14px; border: 1px solid #f5f0ea;">
            <p style="font-size: 13px; color: #666;">Last Status Sync</p>
            <h4 id="last-sync" style="color: #501c1c; margin-top: 4px;">Connecting...</h4>
        </div>
    </div>

    <!-- 2. POSITIONS TAB (Live Trades) -->
    <div id="positions" class="display-section active">
        <div class="section-title">Live Active Positions</div>
        <div id="live-positions-list">
            <div class="empty-state">Market scan chal raha hai, trade dhundte hi yahan dikhega...</div>
        </div>
    </div>

    <!-- 3. TRADES HISTORY TAB -->
    <div id="history" class="display-section">
        <div class="section-title">
            Executed Trades Log 
            <span class="counter-badge" id="history-count">0</span>
        </div>
        <div id="history-log-list">
            <div class="empty-state">Abhi tak koi trade complete nahi hui hai.</div>
        </div>
    </div>
</div>

<script>
    // Tab switching functionality
    function switchTab(tabId) {
        document.querySelectorAll('.display-section').forEach(sec => sec.classList.remove('active'));
        document.querySelectorAll('.menu-item').forEach(item => item.classList.remove('active'));
        
        document.getElementById(tabId).classList.add('active');
        event.currentTarget.classList.add('active');
    }

    // Main Function to Fetch State from Python Bot
    async function updateDashboardData() {
        try {
            let response = await fetch('/api/state');
            let state = await response.json();

            // 1. Update Overview Stats
            document.getElementById('cash-usd').innerText = "$" + state.portfolio.cash_usd.toLocaleString();
            document.getElementById('last-sync').innerText = "Live @ " + (state.last_update || "Waiting...");
            document.getElementById('history-count').innerText = state.portfolio.total_trades_executed;

            // 2. Update Live Positions
            let posList = document.getElementById('live-positions-list');
            if (state.active_positions.length === 0) {
                posList.innerHTML = '<div class="empty-state">Abhi bot market analyze kar rha h, entry ka wait h...</div>';
            } else {
                posList.innerHTML = '';
                state.active_positions.forEach(pos => {
                    let pnlClass = pos.pnl >= 0 ? 'profit' : 'loss';
                    let pnlSign = pos.pnl >= 0 ? '+' : '';
                    posList.innerHTML += `
                        <div class="trade-card" style="background: #fffdfb; border: 1px solid #fbf7f2; border-radius: 12px; margin-bottom: 8px;">
                            <div class="trade-info">
                                <h4>${pos.symbol}</h4>
                                <p>Entry: $${pos.entry_price} | Live: $${pos.current_price}</p>
                            </div>
                            <div class="trade-meta">
                                <span class="pnl ${pnlClass}">${pnlSign}${pos.pnl}%</span>
                                <div class="lev">${pos.leverage}</div>
                            </div>
                        </div>
                    `;
                });
            }

            // 3. Update Trades History List
            let histList = document.getElementById('history-log-list');
            if (state.trades_history.length === 0) {
                histList.innerHTML = '<div class="empty-state">Jaise hi bot paper trade close karega, history yahan aayegi.</div>';
            } else {
                histList.innerHTML = '';
                state.trades_history.forEach(trade => {
                    let pnlClass = trade.pnl >= 0 ? 'profit' : 'loss';
                    let pnlSign = trade.pnl >= 0 ? '+' : '';
                    histList.innerHTML += `
                        <div class="trade-card">
                            <div class="trade-info">
                                <h4>${trade.symbol}</h4>
                                <p>Closed at ${trade.exit_time} | Entry: $${trade.entry_price}</p>
                            </div>
                            <div class="trade-meta">
                                <span class="pnl ${pnlClass}">${pnlSign}${trade.pnl}%</span>
                                <div class="lev">Filled</div>
                            </div>
                        </div>
                    `;
                });
            }

        } catch (error) {
            console.error("Dashboard Sync Error: ", error);
        }
    }

    // Automatically sync every 5 seconds
    setInterval(updateDashboardData, 5000);
    // Initial load
    updateDashboardData();
</script>

</body>
</html>
"""
