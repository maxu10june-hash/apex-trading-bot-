# dashboard_html.py

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Trading Bot - Premium Glass</title>
    <style>
        :root {
            /* Apple Liquid Glass Transparency Variables */
            --glass-bg: rgba(255, 255, 255, 0.45);
            --glass-maroon: rgba(84, 34, 39, 0.65);
            --glass-border: rgba(255, 255, 255, 0.4);
            --text-main: #1a0f10;
            --text-sub: #4a3e3f;
            --text-white: #ffffff;
            --green: #1ea74c;
            --red: #e13434;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            /* 1st Image: Moon Wallpaper Integration */
            background-image: url('https://i.postimg.cc/Y237fP5H/IMG-6198.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }

        /* Container Layout */
        .wrapper-layout {
            width: 100%;
            max-width: 450px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* Apple Liquid Glass Applied to Base Profile Card */
        .profile-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px) saturate(190%);
            -webkit-backdrop-filter: blur(20px) saturate(190%);
            border-radius: 28px;
            padding: 24px;
            border: 1px solid var(--glass-border);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
        }
        
        .user-block { display: flex; align-items: center; gap: 16px; margin-bottom: 20px; }
        
        /* 2nd Image Profile Avatar Integration with Auto-Face Center Crop */
        .avatar-img-box {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            border: 2px solid rgba(255, 255, 255, 0.8);
            background-image: url('https://i.postimg.cc/HskgS2mp/IMG-5449.jpg');
            background-size: 180%; /* Zoomed a bit for focused face view */
            background-position: center 20%; /* Vertical position to focus exactly on face */
            background-repeat: no-repeat;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        
        .user-info .name { font-size: 18px; font-weight: 700; color: var(--text-main); text-shadow: 0 1px 2px rgba(255,255,255,0.4); }
        .user-info .sub { font-size: 12px; color: var(--text-sub); font-weight: 500; }

        /* Navigation Buttons - Apple Liquid Glass Maroon Pill */
        .nav-container { display: flex; flex-direction: column; gap: 8px; }
        .tab-btn {
            background: transparent; border: none; text-align: left;
            padding: 14px 20px; border-radius: 16px; font-size: 14px; font-weight: 600;
            color: var(--text-main); cursor: pointer; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            display: flex; align-items: center; gap: 10px;
        }
        .tab-btn:hover {
            background: rgba(255, 255, 255, 0.25);
        }
        .tab-btn.active {
            background: var(--glass-maroon);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            color: var(--text-white);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 6px 20px rgba(84, 34, 39, 0.25);
        }

        /* Main View Panels */
        .tab-panel { display: none; }
        .tab-panel.active { display: block; }

        /* General Liquid Glass Dynamic Cards */
        .card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px) saturate(190%);
            -webkit-backdrop-filter: blur(20px) saturate(190%);
            border-radius: 28px;
            padding: 24px;
            border: 1px solid var(--glass-border);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.12);
            margin-bottom: 16px;
        }
        .card-title { font-size: 20px; font-weight: 700; color: var(--text-main); margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; }
        .card-label { font-size: 12px; font-weight: 600; color: var(--text-sub); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
        
        /* Serif Balance Typography */
        .equity-num { font-size: 38px; font-weight: 700; color: var(--text-main); font-family: "Times New Roman", Times, serif; margin: 8px 0; }
        .profit-text { color: var(--green); font-size: 14px; font-weight: 600; }
        .loss-text { color: var(--red); font-size: 14px; font-weight: 600; }
        .counter-badge { font-size: 13px; background: var(--glass-maroon); color: white; padding: 4px 10px; border-radius: 12px; font-weight: bold; }

        .sub-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }
        .sub-val { font-size: 18px; font-weight: 700; color: var(--text-main); margin-top: 2px; }

        .list-row { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
        .list-row:last-child { border-bottom: none; }
        .list-left { font-weight: 600; color: var(--text-main); }
        .list-right { font-weight: 700; color: var(--text-main); }
        .list-subtext { font-size: 11px; color: var(--text-sub); margin-top: 2px; font-weight: 500; }

        /* Liquid Soft Alerts */
        .spec-box { background: rgba(255, 255, 255, 0.25); border-left: 4px solid rgba(84, 34, 39, 0.8); padding: 14px; border-radius: 0 16px 16px 0; margin-bottom: 12px; }
        .spec-box.green-side { border-left-color: var(--green); background: rgba(30, 167, 76, 0.08); }
        .spec-box.red-side { border-left-color: var(--red); background: rgba(225, 52, 52, 0.08); }
        
        .strategy-cat { margin-bottom: 20px; border-bottom: 1px dashed rgba(0,0,0,0.08); padding-bottom: 15px; }
        .strategy-cat:last-child { border-bottom: none; }
        .strategy-cat-title { font-size: 15px; font-weight: 700; color: #421216; margin-bottom: 10px; }
        .strategy-list { display: grid; grid-template-columns: 1fr; gap: 6px; }
        .strategy-item { display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: rgba(255,255,255,0.2); border-radius: 10px; font-size: 13px; font-weight: 500; }
        .strat-badge { font-size: 10px; padding: 2px 6px; background: rgba(84, 34, 39, 0.15); color: #421216; border-radius: 4px; font-weight: 700; }
        .strat-badge.active-strat { background: rgba(30, 167, 76, 0.2); color: var(--green); }

        .progress-bar-bg { background: rgba(0,0,0,0.08); border-radius: 10px; height: 12px; width: 100%; margin: 12px 0; overflow: hidden; }
        .progress-bar-fill { background: rgba(84, 34, 39, 0.85); height: 100%; width: 75%; }
        .empty-state { text-align: center; color: var(--text-sub); padding: 30px 10px; font-size: 14px; font-style: italic; font-weight: 500; }
    </style>
</head>
<body>

<div class="wrapper-layout">
    <div class="profile-card">
        <div class="user-block">
            <div class="avatar-img-box"></div>
            <div class="user-info">
                <div class="name">@FabRichhhhhh</div>
                <div class="sub">Apex Trading Bot - v3.1</div>
            </div>
        </div>
        <div class="nav-container">
            <button class="tab-btn active" onclick="openTab(event, 'overview')">● Overview</button>
            <button class="tab-btn" onclick="openTab(event, 'portfolio')">● Live Portfolio</button>
            <button class="tab-btn" onclick="openTab(event, 'positions')">● Positions</button>
            <button class="tab-btn" onclick="openTab(event, 'evolution')">● Evolution</button>
            <button class="tab-btn" onclick="openTab(event, 'strategy')">● Strategy Book</button>
            <button class="tab-btn" onclick="openTab(event, 'world')">● World Feature</button>
            <button class="tab-btn" onclick="openTab(event, 'lessons')">● Lesson Bank</button>
            <button class="tab-btn" onclick="openTab(event, 'trades')">● Trades History</button>
        </div>
    </div>

    <div id="overview" class="tab-panel active">
        <div class="card">
            <div class="card-title">Account Equity</div>
            <div class="equity-num" id="live-equity">$1,000.00</div>
            <div class="profit-text" id="live-net-pnl">+$0.00 (0.00%)</div>
            
            <div class="sub-grid">
                <div>
                    <div class="card-label">INR Capital</div>
                    <div class="sub-val" id="live-cash-inr">₹50,000</div>
                </div>
                <div>
                    <div class="card-label">USD Capital</div>
                    <div class="sub-val" id="live-cash-usd">$1,000</div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="card-title">Live Sync Status</div>
            <div class="list-row">
                <div class="list-left">Last Updated Loop:</div>
                <div class="list-right" id="last-sync-time" style="color: #542227;">Connecting...</div>
            </div>
        </div>
    </div>

    <div id="portfolio" class="tab-panel">
        <div class="card">
            <div class="card-title">Total Portfolio Value</div>
            <div class="equity-num" id="live-portfolio-val" style="color: #542227;">₹1,32,450</div>
            <div class="profit-text" style="color:var(--text-sub);">Net Yield Status: Stable (Paper Mode)</div>
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
            <div class="card-title">Active Leverage Positions</div>
            <div id="live-positions-container">
                <div class="empty-state">Bot market scan kar raha hai, entry aate hi trade yahan live dikhegi...</div>
            </div>
        </div>
    </div>

    <div id="evolution" class="tab-panel">
        <div class="card" style="text-align: center;">
            <div class="card-title" style="margin-bottom: 5px;">Bot Self-Evolution Engine</div>
            <div class="user-info"><div class="sub" style="margin-bottom: 15px;">Autonomous Learning Log</div></div>
            
            <div class="equity-num" style="color: #542227; font-size: 42px;">LEVEL 4</div>
            
            <div class="progress-bar-bg">
                <div class="progress-bar-fill"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--text-sub); font-weight: 600;">
                <span>75% Evolved</span>
                <span>Next: Level 5</span>
            </div>

            <div class="spec-box" style="text-align: left; margin-top: 25px;">
                <strong>Recent Auto-Evolution Update:</strong>
                <p class="list-subtext" style="font-size: 12px; line-height: 1.4; margin-top: 4px;">Bot updated its neural weights after scanning continuous loops. Adjusted dynamic slippage tolerances automatically for high-impact market phases.</p>
            </div>
        </div>
    </div>

    <div id="strategy" class="tab-panel">
        <div class="card">
            <div class="card-title">AI Strategy Book</div>
            <p class="list-subtext" style="margin-bottom: 20px; font-size: 12px;">The bot upgrades and optimizes these strategies dynamically according to market loops.</p>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Trend Following Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>1. Moving Average Crossover</span><span class="strat-badge active-strat">Upgrading</span></div>
                    <div class="strategy-item"><span>2. EMA Crossover</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>3. Supertrend Strategy</span><span class="strat-badge active-strat">Active</span></div>
                    <div class="strategy-item"><span>4. Donchian Channel Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>5. Turtle Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>6. ADX Trend Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>7. Ichimoku Cloud Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>8. Trendline Breakout</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Breakout Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>9. Opening Range Breakout (ORB)</span><span class="strat-badge active-strat">Active</span></div>
                    <div class="strategy-item"><span>10. Volume Breakout</span><span class="strat-badge active-strat">Upgrading</span></div>
                    <div class="strategy-item"><span>11. Range Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>12. Support Resistance Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>13. Volatility Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>14. Bollinger Band Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>15. Triangle Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>16. Flag Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>17. Pennant Breakout</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Reversal Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>18. Double Top</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>19. Double Bottom</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>20. Head and Shoulders</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>21. Inverse Head and Shoulders</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>22. RSI Divergence</span><span class="strat-badge active-strat">Active</span></div>
                    <div class="strategy-item"><span>23. MACD Divergence</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>24. Stochastic Reversal</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>25. V-Shape Reversal</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Pullback Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>26. EMA Pullback</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>27. Fibonacci Retracement</span><span class="strat-badge active-strat">Upgrading</span></div>
                    <div class="strategy-item"><span>28. VWAP Pullback</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>29. Trendline Retest</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>30. Support Retest</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>31. Demand Zone Pullback</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>32. Supply Zone Pullback</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Price Action Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>33. Inside Bar</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>34. Outside Bar</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>35. Pin Bar</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>36. Engulfing Candle</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>37. Fakey Pattern</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>38. Break and Retest</span><span class="strat-badge active-strat">Active</span></div>
                    <div class="strategy-item"><span>39. Order Block Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>40. Liquidity Grab Strategy</span><span class="strat-badge active-strat">Upgrading</span></div>
                    <div class="strategy-item"><span>41. Smart Money Concept (SMC)</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>42. ICT Strategy</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Indicator-Based Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>43. RSI Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>44. MACD Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>45. Bollinger Bands Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>46. VWAP Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>47. ATR Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>48. Parabolic SAR Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>49. CCI Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>50. Stochastic Strategy</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Scalping Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>51. 1-Minute Scalping</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>52. 5-Minute Scalping</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>53. Tick Scalping</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>54. VWAP Scalping</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>55. EMA Scalping</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>56. Momentum Scalping</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Intraday Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>57. Gap Up Gap Down</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>58. CPR Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>59. VWAP Intraday</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>60. First Hour Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>61. Noon Breakout</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>62. Momentum Trading</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Advanced Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>63. Market Structure Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>64. Wyckoff Method</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>65. Elliott Wave</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>66. Harmonic Patterns</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>67. Gann Strategy</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>68. Pair Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>69. Arbitrage Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>70. Statistical Arbitrage</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>71. Quantitative Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>72. Algorithmic Trading</span><span class="strat-badge active-strat">Active</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Options Trading Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>73. Covered Call</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>74. Cash Secured Put</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>75. Bull Call Spread</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>76. Bear Put Spread</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>77. Iron Condor</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>78. Iron Butterfly</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>79. Straddle</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>80. Strangle</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>81. Calendar Spread</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>82. Butterfly Spread</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Futures & Institutional Concepts</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>83. Volume Profile</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>84. Market Profile</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>85. Footprint Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>86. Delta Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>87. Order Flow Trading</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>88. Liquidity Sweep</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>89. Fair Value Gap (FVG)</span><span class="strat-badge active-strat">Active</span></div>
                    <div class="strategy-item"><span>90. Breaker Block</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>91. Mitigation Block</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>92. Kill Zone Strategy</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>

            <div class="strategy-cat">
                <div class="strategy-cat-title">Candlestick-Based Strategies</div>
                <div class="strategy-list">
                    <div class="strategy-item"><span>93. Morning Star</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>94. Evening Star</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>95. Three White Soldiers</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>96. Three Black Crows</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>97. Hammer</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>98. Shooting Star</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>99. Harami</span><span class="strat-badge">Ready</span></div>
                    <div class="strategy-item"><span>100. Doji Strategy</span><span class="strat-badge">Ready</span></div>
                </div>
            </div>
        </div>
    </div>

    <div id="world" class="tab-panel">
        <div class="card">
            <div class="card-title">World Sentiment Metric</div>
            
            <div class="sub-grid" style="margin-bottom: 20px;">
                <div>
                    <div class="card-label">Fear & Greed Index</div>
                    <div class="sub-val" style="color: #542227;">64 / 100 (GREED)</div>
                </div>
                <div>
                    <div class="card-label">Macro Capital Flow</div>
                    <div class="sub-val" style="color: var(--green);">BULLISH FLOW</div>
                </div>
            </div>

            <div class="card-label" style="margin-top: 15px;">Processed Global News Headlines</div>
            <div class="spec-box">
                <strong>🌐 Fed Signals Stable Interest Rates</strong>
                <p class="list-subtext">Macro Filter Impact: Bot asset allocation weights increased by 5%.</p>
            </div>
            <div class="spec-box" style="margin-top: 10px;">
                <strong>🌐 Tech Indices Face Temporary Structural Resistance</strong>
                <p class="list-subtext">Macro Filter Impact: Automated tight trailing stop-loss execution on IT assets.</p>
            </div>
        </div>
    </div>

    <div id="lessons" class="tab-panel">
        <div class="card">
            <div class="card-title">Bot Self-Compiled Lessons</div>
            <p class="list-subtext" style="margin-bottom: 15px;">Automated internal constraints written post back-testing failures.</p>

            <div class="spec-box red-side">
                <strong>Lesson #104 (Risk Management Rules)</strong>
                <p class="list-subtext" style="font-style: italic; font-size:12px; margin-top:4px;">"Entering aggressive positions 10 minutes before highly volatile institutional global news releases leads to bad slippage execution. Halting processing pipelines 15 mins prior to events."</p>
            </div>

            <div class="spec-box green-side" style="margin-top: 15px;">
                <strong>Lesson #103 (Leverage Risk Safety)</strong>
                <p class="list-subtext" style="font-style: italic; font-size:12px; margin-top:4px;">"Running 5x leverage positions on high-beta setups over-exposes net margin account buffers. Capped strict system max limits to 3x on extreme counters."</p>
            </div>
        </div>
    </div>

    <div id="trades" class="tab-panel">
        <div class="card">
            <div class="card-title">
                Executed Trades Log
                <span class="counter-badge" id="history-counter-badge">0</span>
            </div>
            
            <div id="live-history-container">
                <div class="empty-state">Abhi tak koi trade complete nahi hui hai.</div>
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

    async function syncWithBotBackend() {
        try {
            let response = await fetch('/api/state');
            let state = await response.json();

            document.getElementById('live-cash-inr').innerText = "₹" + state.portfolio.cash_inr.toLocaleString();
            document.getElementById('live-cash-usd').innerText = "$" + state.portfolio.cash_usd.toLocaleString();
            document.getElementById('last-sync-time').innerText = state.last_update || "Waiting...";
            document.getElementById('history-counter-badge').innerText = state.portfolio.total_trades_executed;

            let dynamicEquity = 1000; 
            state.active_positions.forEach(p => dynamicEquity += (p.pnl || 0));
            document.getElementById('live-equity').innerText = "$" + dynamicEquity.toFixed(2);
            document.getElementById('live-portfolio-val').innerText = "₹" + state.portfolio.portfolio_value_inr.toLocaleString();

            let posContainer = document.getElementById('live-positions-container');
            if(state.active_positions.length === 0) {
                posContainer.innerHTML = '<div class="empty-state">Bot market scan kar raha hai, entry aate hi trade yahan live dikhegi...</div>';
            } else {
                posContainer.innerHTML = '';
                state.active_positions.forEach(pos => {
                    let sideColor = pos.pnl >= 0 ? 'green-side' : 'red-side';
                    let textColor = pos.pnl >= 0 ? 'profit-text' : 'loss-text';
                    let sign = pos.pnl >= 0 ? '+' : '';
                    posContainer.innerHTML += `
                        <div class="spec-box ${sideColor}">
                            <div style="display:flex; justify-content: space-between; font-weight:700;">
                                <span>${pos.symbol}</span>
                                <span class="${textColor}">${sign}${pos.pnl}%</span>
                            </div>
                            <div class="list-subtext">Size: Dynamic Base • <strong>Leverage: ${pos.leverage}</strong></div>
                            <div class="list-subtext" style="margin-top:4px;">Entry Price: $${pos.entry_price} | Current Price: $${pos.current_price}</div>
                        </div>
                    `;
                });
            }

            let histContainer = document.getElementById('live-history-container');
            if(state.trades_history.length === 0) {
                histContainer.innerHTML = '<div class="empty-state">Jaise hi bot paper trade close karega, history yahan aayegi.</div>';
            } else {
                histContainer.innerHTML = '';
                state.trades_history.forEach(trade => {
                    let textClass = trade.pnl >= 0 ? 'profit-text' : 'loss-text';
                    let sign = trade.pnl >= 0 ? '+' : '';
                    histContainer.innerHTML += `
                        <div class="list-row">
                            <div>
                                <div class="list-left">${trade.symbol}</div>
                                <div class="list-subtext">Closed @ ${trade.exit_time}</div>
                            </div>
                            <div style="text-align: right;">
                                <div class="${textClass}">${sign}${trade.pnl}%</div>
                                <div class="list-subtext">Filled</div>
                            </div>
                        </div>
                    `;
                });
            }

        } catch (err) {
            console.log("Sync delay: ", err);
        }
    }

    setInterval(syncWithBotBackend, 5000);
    syncWithBotBackend();
</script>
</body>
</html>
"""
