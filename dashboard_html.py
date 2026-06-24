# dashboard_html.py

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AlgoBot Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: linear-gradient(135deg, #fceeed 0%, #fbf4e7 50%, #eef5fc 100%);
            background-attachment: fixed;
            color: #333333;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 480px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* Profile & Sidebar Card Mock */
        .profile-card {
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            padding: 24px;
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.03);
        }

        .profile-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .avatar {
            width: 44px;
            height: 44px;
            background: #f4dcd9;
            color: #bd6a5f;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 18px;
        }

        .profile-info h2 {
            font-size: 18px;
            font-weight: 700;
            color: #2c2c2c;
        }

        .profile-info p {
            font-size: 12px;
            color: #7a7a7a;
        }

        /* Navigation Links Lookalike */
        .nav-mock {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .nav-item {
            display: flex;
            align-items: center;
            padding: 12px 16px;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 500;
            color: #666666;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        .nav-item.active {
            background: #542d32;
            color: #ffffff;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(84, 45, 50, 0.2);
        }

        /* Stats & Content Cards */
        .card {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            border-radius: 28px;
            padding: 24px;
            border: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.02);
        }

        .card-title {
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 20px;
        }

        .equity-value {
            font-family: 'Playfair Display', serif;
            font-size: 38px;
            font-weight: 700;
            color: #222222;
            margin-bottom: 4px;
        }

        .equity-change {
            font-size: 14px;
            font-weight: 600;
            color: #2d8a4e;
            margin-bottom: 15px;
        }

        /* Grid for Capitals */
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 10px;
        }

        .mini-box {
            background: rgba(255, 255, 255, 0.5);
            padding: 16px;
            border-radius: 18px;
            border: 1px solid rgba(255, 255, 255, 0.4);
        }

        .mini-box p {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #888888;
            font-weight: 600;
            margin-bottom: 4px;
        }

        .mini-box h3 {
            font-size: 18px;
            font-weight: 700;
            color: #2c2c2c;
        }

        /* Prices / Lists Styling */
        .list-container {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .list-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(0, 0, 0, 0.04);
        }

        .list-row:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }

        .asset-name {
            font-weight: 600;
            font-size: 15px;
            color: #333333;
        }

        .asset-price {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 700;
            font-size: 15px;
            color: #111111;
        }

        .status-bar {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 12px;
            font-weight: 600;
            color: #666666;
            margin-top: 10px;
        }

        .dot {
            width: 8px;
            height: 8px;
            background-color: #2d8a4e;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 8px #2d8a4e;
        }
    </style>
</head>
<body>

    <div class="container">
        
        <!-- Header Mock Card -->
        <div class="profile-card">
            <div class="profile-header">
                <div class="avatar">F</div>
                <div class="profile-info">
                    <h2>@FabRichhhhhh</h2>
                    <p>Apex Trading Bot - v2</p>
                </div>
            </div>
            
            <div class="nav-mock">
                <div class="nav-item active">● Overview</div>
                <div class="nav-item"> Positions</div>
                <div class="nav-item"> Trades</div>
            </div>
        </div>

        <!-- Account Equity Card -->
        <div class="card">
            <div class="card-title">Account Equity</div>
            <div class="equity-value">$248.50</div>
            <div class="equity-change">+$148.50 (148.50%)</div>
            
            <div class="stats-grid">
                <div class="mini-box">
                    <p>INR Capital</p>
                    <h3>₹50,000</h3>
                </div>
                <div class="mini-box">
                    <p>USD Capital</p>
                    <h3>$1,000</h3>
                </div>
            </div>
        </div>

        <!-- Live Prices Card -->
        <div class="card">
            <div class="card-title">Live Prices</div>
            <div class="list-container">
                <div class="list-row">
                    <div class="asset-name">INFY</div>
                    <div class="asset-price">₹2,500</div>
                </div>
                <div class="list-row">
                    <div class="asset-name">RELIANCE</div>
                    <div class="asset-price">₹2,500</div>
                </div>
                <div class="list-row">
                    <div class="asset-name">TCS</div>
                    <div class="asset-price">₹2,500</div>
                </div>
            </div>
            
            <div class="status-bar">
                <span class="dot"></span> Live • Updated <span id="time">05:01:49</span>
            </div>
        </div>

    </div>

    <script>
        // Server time setup to keep it rolling beautifully
        setInterval(() => {
            const now = new Date();
            const timeString = now.toUTCString().split(' ')[4];
            document.getElementById('time').innerText = timeString;
        }, 1000);
    </script>
</body>
</html>
"""
