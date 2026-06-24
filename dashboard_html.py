DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>AlgoBot Dashboard</title>
<style>
  :root {
    --bg: #0a0e1a; --card: #111827; --border: #1f2937;
    --green: #10b981; --red: #ef4444; --blue: #3b82f6;
    --yellow: #f59e0b; --text: #f1f5f9; --muted: #94a3b8;
    --accent: #6366f1;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    background: var(--bg); color: var(--text);
    font-family: 'SF Pro Display',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
    font-size: 14px; min-height: 100vh;
    scroll-behavior: smooth; -webkit-overflow-scrolling: touch;
  }
  * { transition: background 0.15s ease, color 0.15s ease, transform 0.1s ease, opacity 0.2s ease; }
  .header {
    background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
    padding: 16px 20px; border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 100; backdrop-filter: blur(20px);
  }
  .header h1 { font-size: 18px; font-weight: 700; color: var(--accent); letter-spacing: -0.5px; }
  .live-dot { width:8px; height:8px; background:var(--green); border-radius:50%; display:inline-block; margin-right:6px; animation: pulse 1.5s infinite; }
  @keyframes pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(16,185,129,0.4); }
    50%      { box-shadow: 0 0 0 6px rgba(16,185,129,0); }
  }
  .tabs { display: flex; overflow-x: auto; background: var(--card); border-bottom: 1px solid var(--border); padding: 0 12px; scrollbar-width: none; }
  .tabs::-webkit-scrollbar { display: none; }
  .tab { padding: 12px 16px; cursor: pointer; white-space: nowrap; color: var(--muted); font-size: 13px; font-weight: 500; border-bottom: 2px solid transparent; }
  .tab.active { color: var(--accent); border-bottom-color: var(--accent); }
  .page { display: none; padding: 16px; max-width: 600px; margin: 0 auto; }
  .page.active { display: block; }
  .kpi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px; }
  .kpi { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 14px; text-align: center; }
  .kpi-label { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
  .kpi-value { font-size: 22px; font-weight: 700; letter-spacing: -0.5px; }
  .pos { color: var(--green); } .neg { color: var(--red); } .neu { color: var(--text); }
  .section-title { font-size: 12px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.8px; margin: 20px 0 10px 2px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; margin-bottom: 10px; }
  .card-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; border-bottom: 1px solid var(--border); }
  .symbol { font-weight: 600; font-size: 15px; }
  .price  { font-size: 15px; font-weight: 600; }
  .badge { font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 20px; }
  .badge-buy  { background: rgba(16,185,129,0.15); color: var(--green); }
  .badge-sell { background: rgba(239,68,68,0.15);  color: var(--red);   }
  .badge-hold { background: rgba(148,163,184,0.1); color: var(--muted); }
  .trade-row { padding: 10px 16px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
  .pnl-pos    { color: var(--green); font-weight: 700; }
  .pnl-neg    { color: var(--red);   font-weight: 700; }
  .status-bar { text-align: center; padding: 8px; font-size: 11px; color: var(--muted); border-top: 1px solid var(--border); position: sticky; bottom: 0; background: var(--bg); }
</style>
</head>
<body>
<div class="header">
  <h1>🤖 AlgoBot</h1>
  <span style="font-size:12px;color:var(--muted)"><span class="live-dot"></span><span id="last-update">Loading...</span></span>
</div>
<div class="tabs">
  <div class="tab active" onclick="showPage('overview')">📊 Overview</div>
  <div class="tab" onclick="showPage('positions')">💼 Positions</div>
  <div class="tab" onclick="showPage('trades')">📋 Trades</div>
  <div class="tab" onclick="showPage('world')">🌍 World</div>
</div>
<div id="page-overview" class="page active">
  <div class="kpi-grid">
    <div class="kpi"><div class="kpi-label">INR Capital</div><div class="kpi-value neu" id="cash-inr">—</div></div>
    <div class="kpi"><div class="kpi-label">USD Capital</div><div class="kpi-value neu" id="cash-usd">—</div></div>
    <div class="kpi"><div class="kpi-label">INR P&L</div><div class="kpi-value" id="pnl-inr">—</div></div>
    <div class="kpi"><div class="kpi-label">Win Rate</div><div class="kpi-value neu" id="win-rate">—</div></div>
  </div>
  <p class="section-title">📡 Live Prices</p>
  <div class="card" id="prices-card"></div>
</div>
<div id="page-positions" class="page">
  <p class="section-title">💼 Open Positions</p>
  <div class="card" id="positions-full"></div>
</div>
<div id="page-trades" class="page">
  <p class="section-title">📋 Recent Trades</p>
  <div class="card" id="trades-list"></div>
</div>
<div id="page-world" class="page">
  <div class="card" id="world-nse">
    <div class="card-row"><b>🇮🇳 NSE India</b></div><div id="world-nse-prices"></div>
  </div>
</div>
<div class="status-bar"><span id="status-text">Connecting...</span></div>
<script>
let state = {};
async function fetchState() {
  try {
    const r = await fetch('/api/state');
    state = await r.json();
    renderAll();
    document.getElementById('last-update').textContent = state.last_update || 'now';
    document.getElementById('status-text').textContent = '🟢 Live · Updated ' + (state.last_update || '—');
  } catch(e) { document.getElementById('status-text').textContent = '🔴 Connection error'; }
}
function fmt_inr(n) { return '₹' + Number(n||0).toLocaleString('en-IN', {maximumFractionDigits:0}); }
function fmt_usd(n) { return '$' + Number(n||0).toLocaleString('en-US', {maximumFractionDigits:0}); }
function renderAll() {
  const p = state.portfolio || {};
  document.getElementById('cash-inr').textContent = fmt_inr(p.cash_inr);
  document.getElementById('cash-usd').textContent = fmt_usd(p.cash_usd);
  document.getElementById('win-rate').textContent = (p.win_rate_pct||0) + '%';
  let html = '';
  const mkts = (state.prices||{}).markets || {};
  if(mkts.NSE){ Object.entries(mkts.NSE).forEach(([sym,d]) => { if(d.ok) html += `<div class="card-row"><span class="symbol">${sym.replace('.NS','')}</span><span class="price">₹${d.price}</span></div>`; }); }
  document.getElementById('prices-card').innerHTML = html || '<div class="card-row">No prices</div>';
}
function showPage(name) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById('page-' + name).classList.add('active');
}
fetchState(); setInterval(fetchState, 10000);
</script>
</body>
</html>
"""
