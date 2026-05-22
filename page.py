# -*- coding: utf-8 -*-
HTML = r'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>IP Scanner - @Net4All_None</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0a0e17;--s1:#111827;--s2:#1a2332;--bd:#2a3a4e;--pr:#3b82f6;--ok:#10b981;--wn:#f59e0b;--er:#ef4444;--tx:#e5e7eb;--dm:#9ca3af;--tg:#2AABEE}
body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:var(--tx)}
.hd{background:linear-gradient(135deg,#1a1a2e,#16213e,#0f3460);padding:14px 20px;border-bottom:2px solid var(--pr);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.hd h1{font-size:20px;color:#fff}
.hd-r{display:flex;align-items:center;gap:14px}
.hd .st{display:flex;align-items:center;gap:8px;font-size:13px}
.dt{width:10px;height:10px;border-radius:50%;background:var(--ok)}
.dt.on{background:var(--wn);animation:pu .5s infinite}
@keyframes pu{0%,100%{opacity:1}50%{opacity:.3}}
.tg-link{display:flex;align-items:center;gap:6px;color:var(--tg);font-size:12px;text-decoration:none;padding:4px 10px;background:rgba(42,171,238,.1);border-radius:20px;border:1px solid rgba(42,171,238,.3)}
.tg-link:hover{background:rgba(42,171,238,.2)}
.tg-ico{width:15px;height:15px;display:inline-block;vertical-align:middle;fill:currentColor}
.wr{max-width:1400px;margin:0 auto;padding:14px;display:grid;grid-template-columns:350px 1fr;gap:14px}
@media(max-width:850px){.wr{grid-template-columns:1fr}}
.cd{background:var(--s1);border:1px solid var(--bd);border-radius:10px;margin-bottom:12px}
.ct{background:var(--s2);padding:10px 14px;font-size:13px;font-weight:600;border-bottom:1px solid var(--bd);border-radius:10px 10px 0 0;display:flex;justify-content:space-between;align-items:center}
.cc{padding:14px}
label{display:block;font-size:11px;color:var(--dm);margin:8px 0 3px}
input[type=text],input[type=number],input[type=password],textarea,select{width:100%;padding:8px 10px;background:var(--bg);border:1px solid var(--bd);border-radius:6px;color:var(--tx);font-size:13px}
input:focus,textarea:focus,select:focus{outline:none;border-color:var(--pr)}
select option{background:var(--bg);color:var(--tx)}
textarea{resize:vertical;min-height:75px;font-family:Consolas,monospace}
.ts{display:flex;gap:3px;margin-bottom:10px}
.tb{flex:1;padding:8px;background:var(--bg);border:1px solid var(--bd);border-radius:6px;color:var(--dm);cursor:pointer;font-size:12px;text-align:center}
.tb:hover{border-color:var(--pr)}.tb.on{background:var(--pr);color:#fff;border-color:var(--pr)}
.rl{max-height:130px;overflow-y:auto;background:var(--bg);border-radius:6px;padding:4px}
.ri{display:flex;align-items:center;gap:6px;padding:3px 6px;font-size:11px;font-family:monospace;cursor:pointer;border-radius:4px}
.ri:hover{background:var(--s2)}
.ri input{width:14px;height:14px;accent-color:var(--pr)}
.rw{display:flex;gap:8px}.rw>*{flex:1}
.btn{padding:10px 16px;border:none;border-radius:6px;font-size:13px;font-weight:600;cursor:pointer;width:100%;display:flex;align-items:center;justify-content:center;gap:6px}
.bp{background:linear-gradient(135deg,var(--pr),#6366f1);color:#fff}
.bp:hover{box-shadow:0 4px 12px rgba(59,130,246,.4)}
.bst{background:var(--er);color:#fff;width:auto;padding:10px 14px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.bg{display:flex;gap:8px;margin-top:12px}
.pg{margin-top:12px;display:none}.pg.on{display:block}
.pgb{height:20px;background:var(--bg);border-radius:10px;overflow:hidden}
.pgf{height:100%;background:linear-gradient(90deg,var(--pr),var(--ok));border-radius:10px;transition:width .15s;font-size:10px;font-weight:700;color:#fff;display:flex;align-items:center;justify-content:center;min-width:30px}
.pgs{display:flex;justify-content:space-between;margin-top:5px;font-size:11px;color:var(--dm)}
.pgs b{color:var(--ok)}
.chk{display:flex;align-items:center;gap:6px;margin-top:8px;font-size:11px;color:var(--dm)}
.chk input{width:14px;height:14px;accent-color:var(--pr)}
.tg-box{margin-top:10px;padding:10px;background:var(--bg);border-radius:6px;border:1px solid #2AABEE33;display:none}
.tg-box.on{display:block}
.tg-box label{color:var(--tg)}
.tg-save-row{display:flex;gap:6px;margin-top:6px}
.tg-save-btn{padding:6px 12px;background:var(--s2);border:1px solid var(--bd);border-radius:5px;color:var(--dm);cursor:pointer;font-size:10px;text-align:center;transition:.2s}
.tg-save-btn:hover{border-color:var(--tg);color:var(--tg)}
.tg-send-btn{margin-top:10px;padding:10px;background:linear-gradient(135deg,#2AABEE,#1a8cd8);border:none;border-radius:6px;color:#fff;font-size:13px;font-weight:600;cursor:pointer;width:100%;display:none;align-items:center;justify-content:center;gap:6px}
.tg-send-btn.on{display:flex}
.tg-send-btn:hover{box-shadow:0 4px 12px rgba(42,171,238,.4)}
.tg-send-btn:disabled{opacity:.4;cursor:not-allowed}
.op-box{margin-top:6px;padding:10px;background:rgba(16,185,129,.05);border:1px solid rgba(16,185,129,.2);border-radius:6px}
.op-box label{color:var(--ok)}
.tw{overflow:auto;margin-top:8px;max-height:550px}
table{width:100%;border-collapse:collapse;font-size:12px}
thead{position:sticky;top:0;z-index:1}
th{background:var(--s2);padding:8px;text-align:left;color:var(--dm);border-bottom:2px solid var(--bd);cursor:pointer;white-space:nowrap}
th:hover{color:var(--pr)}
td{padding:7px 8px;border-bottom:1px solid var(--bd);white-space:nowrap}
tr:hover td{background:var(--s2)}
.lf{color:var(--ok);font-weight:600}
.lm{color:var(--wn);font-weight:600}
.ls{color:var(--er);font-weight:600}
.bx{padding:2px 8px;border-radius:8px;font-size:10px;font-weight:600}
.ba{background:rgba(255,107,53,.15);color:#ff6b35}
.bf{background:rgba(255,23,68,.15);color:#ff1744}
.bo{background:rgba(59,130,246,.15);color:var(--pr)}
.rk{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;font-size:10px;font-weight:700}
.k1{background:linear-gradient(135deg,#ffd700,#ffaa00);color:#000}
.k2{background:linear-gradient(135deg,#c0c0c0,#a0a0a0);color:#000}
.k3{background:linear-gradient(135deg,#cd7f32,#a0522d);color:#fff}
.sp{margin-top:12px;padding:12px;background:var(--bg);border-radius:8px;display:none}.sp.on{display:block}
.so{display:flex;gap:6px;margin-top:8px}
.svb{flex:1;padding:8px;background:var(--s2);border:1px solid var(--bd);border-radius:6px;color:var(--tx);cursor:pointer;text-align:center;font-size:12px;transition:.2s}
.svb:hover,.svb:active{border-color:var(--pr);background:var(--pr);color:#fff}
.lg{max-height:140px;overflow-y:auto;background:var(--bg);border-radius:6px;padding:6px;font-family:Consolas,monospace;font-size:10px}
.le{padding:1px 0}.le.ok{color:var(--ok)}.le.info{color:var(--pr)}.le.er{color:var(--er)}
.fl .fi{display:flex;justify-content:space-between;align-items:center;padding:5px 8px;background:var(--bg);border-radius:6px;margin-bottom:4px;font-size:11px}
.fi a{color:var(--ok);text-decoration:none;padding:3px 8px;background:rgba(16,185,129,.15);border-radius:5px;font-size:10px}
.fi a:hover{background:var(--ok);color:#fff}
.footer{text-align:center;padding:16px;border-top:1px solid var(--bd);margin-top:8px}
.footer a{color:var(--tg);text-decoration:none;font-size:13px;display:inline-flex;align-items:center;gap:6px}
.footer a:hover{text-decoration:underline}
.tt{position:fixed;bottom:16px;right:16px;padding:10px 16px;background:var(--s1);border:1px solid var(--bd);border-radius:8px;font-size:12px;z-index:99;box-shadow:0 8px 25px rgba(0,0,0,.5);animation:su .3s}
@keyframes su{from{transform:translateY(20px);opacity:0}to{transform:translateY(0);opacity:1}}
::-webkit-scrollbar{width:4px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--bd);border-radius:2px}
</style>
</head>
<body>
<div class="hd">
<h1>&#128269; IP Scanner</h1>
<div class="hd-r">
<a class="tg-link" href="https://t.me/Net4All_None" target="_blank">
<svg class="tg-ico" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>
@Net4All_None
</a>
<div class="st"><div class="dt" id="dot"></div><span id="stx">Ready</span></div>
</div>
</div>

<div class="wr">
<div>

<div class="cd">
<div class="ct">Settings</div>
<div class="cc">

<label>Mode</label>
<div class="ts" id="tabs">
<div class="tb on" onclick="SM('custom')">Custom</div>
<div class="tb" onclick="SM('akamai')">Akamai</div>
<div class="tb" onclick="SM('fastly')">Fastly</div>
<div class="tb" onclick="SM('both')">Both</div>
</div>

<div id="cp">
<label>IPs (one per line)</label>
<textarea id="ipIn" placeholder="151.101.0.0/24&#10;23.64.0.1-254&#10;1.2.3.4"></textarea>
</div>

<div id="rp" style="display:none">
<label>Ranges <span style="font-size:10px;color:var(--pr);cursor:pointer" onclick="TA()">all/none</span></label>
<div class="rl" id="rl"></div>
<label>Sample Size</label>
<input type="number" id="sn" value="500" min="10" max="50000">
</div>

<div class="op-box">
<label>&#128246; Operator</label>
<select id="opsel"><option value="none">No Operator (Direct)</option></select>
</div>

<div class="rw">
<div><label>Ports</label><input type="text" id="pt" value="443,80"></div>
<div><label>Threads</label><input type="number" id="th" value="200" min="1" max="600"></div>
</div>

<div class="rw">
<div><label>Timeout (s)</label><input type="number" id="to" value="1.5" min="0.3" max="10" step="0.1"></div>
<div></div>
</div>

<div class="chk">
<input type="checkbox" id="dohttp">
<label for="dohttp" style="margin:0">HTTP check (detect CDN)</label>
</div>

<div class="chk">
<input type="checkbox" id="sendtg" onchange="TGT()">
<label for="sendtg" style="margin:0">
<svg class="tg-ico" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>
Telegram
</label>
</div>

<div class="tg-box" id="tgbox">
<label>Bot Token</label>
<input type="password" id="tgtoken" placeholder="123456789:ABCdef...">
<label>Channel / Group ID</label>
<input type="text" id="tgchannel" placeholder="-100xxx:TopicID">
<div class="tg-save-row">
<div class="tg-save-btn" onclick="saveTG()">&#128190; Save Settings</div>
<div class="tg-save-btn" onclick="clearTG()">&#128465; Clear Saved</div>
</div>
</div>

<div class="bg">
<button class="btn bp" id="goBtn" onclick="GO()">&#9654; Start Scan</button>
<button class="btn bst" id="stBtn" onclick="STP()" disabled>&#9209; Stop</button>
</div>

<div class="pg" id="pg">
<div class="pgb"><div class="pgf" id="pb" style="width:0">0%</div></div>
<div class="pgs">
<span>Scanned: <b id="ps">0</b>/<b id="pt2">0</b></span>
<span>Found: <b id="pf">0</b></span>
</div>
</div>

</div>
</div>

<div class="cd">
<div class="ct">Log</div>
<div class="cc" style="padding:5px"><div class="lg" id="lg"></div></div>
</div>

<div class="cd">
<div class="ct">Saved Files <span style="font-size:10px;color:var(--pr);cursor:pointer" onclick="LF()">refresh</span></div>
<div class="cc"><div class="fl" id="fl">No files</div></div>
</div>

</div>

<div>
<div class="cd" style="min-height:400px">
<div class="ct">
<span>Results (sorted by speed)</span>
<div style="display:flex;gap:6px;align-items:center">
<input type="text" id="flt" placeholder="Filter..." style="width:120px;padding:4px 8px;font-size:11px;margin:0" oninput="RN()">
<span style="font-size:11px;color:var(--dm)" id="rc"></span>
</div>
</div>

<div class="cc">
<div class="tw">
<table>
<thead>
<tr>
<th onclick="SR(0)">#</th>
<th onclick="SR(1)">IP</th>
<th onclick="SR(2)">Port</th>
<th onclick="SR(3)">Latency</th>
<th onclick="SR(4)">Provider</th>
<th onclick="SR(5)">HTTP</th>
<th onclick="SR(6)">TLS</th>
<th onclick="SR(7)">Server</th>
</tr>
</thead>
<tbody id="tbd">
<tr><td colspan="8" style="text-align:center;padding:30px;color:var(--dm)">Start scan to see results</td></tr>
</tbody>
</table>
</div>

<div class="sp" id="sv">
<b>&#128190; Save Results</b>
<div class="so">
<div class="svb" onclick="SV('txt')">&#128196; TXT</div>
<div class="svb" onclick="SV('csv')">&#128202; CSV</div>
<div class="svb" onclick="SV('json')">&#128295; JSON</div>
</div>

<button class="tg-send-btn" id="tgSendBtn" onclick="sendTG()">
<svg class="tg-ico" style="width:16px;height:16px;fill:#fff" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>
Send to Telegram
</button>
</div>

</div>
</div>
</div>
</div>

<div class="footer">
<a href="https://t.me/Net4All_None" target="_blank">
<svg class="tg-ico" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>
Telegram: @Net4All_None
</a>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.4/socket.io.min.js"></script>
<script>
var sk,A=[],M='custom',R={},SD={},ok=false,saving=false,sending=false;

function saveTG(){
  var token=document.getElementById('tgtoken').value.trim();
  var channel=document.getElementById('tgchannel').value.trim();
  if(!token||!channel){TT('Enter token and channel first!');return}
  try{
    localStorage.setItem('tg_token',token);
    localStorage.setItem('tg_channel',channel);
    TT('Telegram settings saved!');
    L('Telegram settings saved','info');
  }catch(e){TT('Cannot save in this browser')}
}

function clearTG(){
  try{
    localStorage.removeItem('tg_token');
    localStorage.removeItem('tg_channel');
    document.getElementById('tgtoken').value='';
    document.getElementById('tgchannel').value='';
    TT('Saved settings cleared!');
    L('Telegram settings cleared','info');
  }catch(e){}
}

function loadTG(){
  try{
    var token=localStorage.getItem('tg_token');
    var channel=localStorage.getItem('tg_channel');
    if(token)document.getElementById('tgtoken').value=token;
    if(channel)document.getElementById('tgchannel').value=channel;
    if(token&&channel)L('Telegram settings loaded','info');
  }catch(e){}
}

function TGT(){
  var c=document.getElementById('sendtg').checked;
  document.getElementById('tgbox').className=c?'tg-box on':'tg-box';
}

function sendTG(){
  if(sending){TT('Sending...');return}
  if(A.length===0){TT('No results to send!');return}
  var token=document.getElementById('tgtoken').value.trim();
  var channel=document.getElementById('tgchannel').value.trim();
  if(!token||!channel){
    document.getElementById('sendtg').checked=true;
    TGT();
    TT('Enter Bot Token and Channel ID first!');
    return;
  }
  sending=true;
  document.getElementById('tgSendBtn').disabled=true;
  document.getElementById('tgSendBtn').innerHTML='<svg class="tg-ico" style="width:16px;height:16px;fill:#fff" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>Sending...';
  L('Sending to Telegram...','info');
  sk.emit('send_telegram',{
    tg_token:token,
    tg_channel:channel,
    operator:document.getElementById('opsel').value
  });
}

function loadOps(){
  fetch('/api/operators').then(function(r){return r.json()}).then(function(ops){
    var sel=document.getElementById('opsel');
    sel.innerHTML='';
    for(var k in ops){
      var o=document.createElement('option');
      o.value=k;
      o.textContent=ops[k];
      sel.appendChild(o);
    }
  }).catch(function(){});
}

function I(){
  sk=io({transports:['websocket','polling'],reconnection:true});

  sk.on('connect',function(){
    ok=true;
    L('Connected','info');
    SS('Ready',0);
    fetch('/api/ranges').then(function(r){return r.json()}).then(function(d){R=d}).catch(function(){});
    loadOps();
    LF();
    loadTG();
  });

  sk.on('disconnect',function(){
    ok=false;
    L('Disconnected','er');
    SS('Offline',0);
  });

  sk.on('scan_started',function(d){
    SS('Scanning...',1);
    document.getElementById('goBtn').disabled=true;
    document.getElementById('stBtn').disabled=false;
    document.getElementById('pg').classList.add('on');
    document.getElementById('pt2').textContent=d.total;
    document.getElementById('tgSendBtn').className='tg-send-btn';
    L('Started: '+d.total+' IPs','info');
  });

  sk.on('scan_progress',function(d){
    var p=Math.round(d.percent);
    document.getElementById('pb').style.width=p+'%';
    document.getElementById('pb').textContent=p+'%';
    document.getElementById('ps').textContent=d.scanned;
    document.getElementById('pf').textContent=d.found;
  });

  sk.on('ip_found',function(r){
    A.push(r);
    A.sort(function(a,b){return a.latency_ms-b.latency_ms});
    RN();
    L('+ '+r.ip+':'+r.port+' '+r.latency_ms+'ms '+r.provider,'ok');
  });

  sk.on('scan_complete',function(d){
    SS('Done',0);
    document.getElementById('goBtn').disabled=false;
    document.getElementById('stBtn').disabled=true;
    if(d.results&&d.results.length>0){
      A=d.results;
      A.sort(function(a,b){return a.latency_ms-b.latency_ms});
    }
    RN();
    document.getElementById('sv').classList.add('on');
    document.getElementById('tgSendBtn').className='tg-send-btn on';
    L('Done! '+d.total_found+'/'+d.total_scanned,'info');
    TT('Done: '+d.total_found+' IPs');
  });

  sk.on('scan_stopped',function(){
    SS('Stopped',0);
    document.getElementById('goBtn').disabled=false;
    document.getElementById('stBtn').disabled=true;
    document.getElementById('stBtn').innerHTML='&#9209; Stop';
    if(A.length>0){
      document.getElementById('sv').classList.add('on');
      document.getElementById('tgSendBtn').className='tg-send-btn on';
    }
    L('Stopped. Found: '+A.length,'er');
    TT('Stopped!');
  });

  sk.on('scan_error',function(d){
    SS('Error',0);
    document.getElementById('goBtn').disabled=false;
    document.getElementById('stBtn').disabled=true;
    L('Error: '+d.message,'er');
    TT(d.message);
  });

  sk.on('save_ok',function(d){
    saving=false;
    SB(true);
    L('Saved: '+d.filename+' ('+d.count+')','info');
    TT('Saved: '+d.filename);
    LF();
  });

  sk.on('save_error',function(d){
    saving=false;
    SB(true);
    L('Save error','er');
    TT('Error!');
  });

  sk.on('telegram_ok',function(d){
    sending=false;
    document.getElementById('tgSendBtn').disabled=false;
    document.getElementById('tgSendBtn').innerHTML='<svg class="tg-ico" style="width:16px;height:16px;fill:#fff" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>Send to Telegram';
    L('Telegram: sent! ('+d.count+' IPs)','info');
    TT('Sent to Telegram!');
  });

  sk.on('telegram_error',function(d){
    sending=false;
    document.getElementById('tgSendBtn').disabled=false;
    document.getElementById('tgSendBtn').innerHTML='<svg class="tg-ico" style="width:16px;height:16px;fill:#fff" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.55 8.16-1.97 9.28c-.15.66-.54.82-1.08.51l-3-2.21-1.45 1.39c-.16.16-.29.29-.6.29l.21-3.05 5.56-5.02c.24-.21-.05-.33-.37-.12l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.54-.2 1.01.13.83.94z"/></svg>Send to Telegram';
    L('Telegram error: '+d.message,'er');
    TT('Telegram error: '+d.message);
  });
}

function SM(m){
  M=m;
  var t=document.getElementById('tabs').children;
  var ms=['custom','akamai','fastly','both'];
  for(var i=0;i<t.length;i++)t[i].className=ms[i]===m?'tb on':'tb';
  document.getElementById('cp').style.display=m==='custom'?'block':'none';
  document.getElementById('rp').style.display=m!=='custom'?'block':'none';
  if(m!=='custom')UR(m);
}

function UR(m){
  var r=[];
  if(m==='akamai')r=R.akamai||[];
  else if(m==='fastly')r=R.fastly||[];
  else r=(R.akamai||[]).concat(R.fastly||[]);
  var h='';
  for(var i=0;i<r.length;i++){
    h+='<label class="ri"><input type="checkbox" checked class="rc" value="'+r[i]+'"> '+r[i]+'</label>';
  }
  document.getElementById('rl').innerHTML=h;
}

function TA(){
  var c=document.querySelectorAll('.rc');
  var a=true;
  for(var i=0;i<c.length;i++)if(!c[i].checked){a=false;break}
  for(var i=0;i<c.length;i++)c[i].checked=!a;
}

function GO(){
  if(!ok){TT('Not connected!');return}
  var sr=[];
  var ch=document.querySelectorAll('.rc:checked');
  for(var i=0;i<ch.length;i++)sr.push(ch[i].value);

  var data={
    mode:M,
    ips:document.getElementById('ipIn').value,
    ports:document.getElementById('pt').value,
    threads:document.getElementById('th').value,
    timeout:document.getElementById('to').value,
    sample:document.getElementById('sn').value,
    do_http:document.getElementById('dohttp').checked,
    operator:document.getElementById('opsel').value,
    selected_ranges:sr
  };

  if(M==='custom'&&!data.ips.trim()){TT('Enter IPs!');return}

  A=[];
  document.getElementById('tbd').innerHTML='';
  document.getElementById('sv').classList.remove('on');
  document.getElementById('tgSendBtn').className='tg-send-btn';
  document.getElementById('pb').style.width='0';
  document.getElementById('pb').textContent='0%';
  document.getElementById('ps').textContent='0';
  document.getElementById('pf').textContent='0';
  sk.emit('start_scan',data);
  L('Starting...','info');
}

function STP(){
  L('Stop requested...','er');
  document.getElementById('stBtn').disabled=true;
  document.getElementById('stBtn').textContent='Stopping...';
  sk.emit('stop_scan');
}

function SB(en){
  var b=document.querySelectorAll('.svb');
  for(var i=0;i<b.length;i++){
    b[i].style.opacity=en?'1':'0.4';
    b[i].style.pointerEvents=en?'auto':'none';
  }
}

function SV(fmt){
  if(saving){TT('Saving...');return}
  if(A.length===0){TT('No results!');return}
  saving=true;
  SB(false);
  L('Saving '+fmt+'...','info');
  sk.emit('save_results',{format:fmt});
}

function RN(){
  var f=document.getElementById('flt').value.toLowerCase();
  var res=A;
  if(f){
    res=[];
    for(var i=0;i<A.length;i++){
      var r=A[i];
      if(r.ip.indexOf(f)>=0||r.provider.toLowerCase().indexOf(f)>=0||(r.server_header||'').toLowerCase().indexOf(f)>=0)res.push(r);
    }
  }
  var h='';
  var max=Math.min(res.length,500);
  for(var i=0;i<max;i++){
    var r=res[i],rk=i+1;
    var lc=r.latency_ms<50?'lf':r.latency_ms<150?'lm':'ls';
    var rb=rk<=3?'<span class="rk k'+rk+'">'+rk+'</span>':''+rk;
    var p=r.provider.toLowerCase();
    var bc=p.indexOf('akamai')>=0?'ba':p.indexOf('fastly')>=0?'bf':'bo';
    h+='<tr><td>'+rb+'</td><td><b>'+r.ip+'</b></td><td>'+r.port+'</td>';
    h+='<td class="'+lc+'">'+r.latency_ms+' ms</td>';
    h+='<td><span class="bx '+bc+'">'+r.provider+'</span></td>';
    h+='<td>'+(r.http_status||'-')+'</td><td>'+(r.tls_valid?'Y':'-')+'</td>';
    h+='<td>'+(r.server_header||'-')+'</td></tr>';
  }
  if(!h)h='<tr><td colspan="8" style="text-align:center;padding:20px;color:var(--dm)">No results</td></tr>';
  document.getElementById('tbd').innerHTML=h;
  document.getElementById('rc').innerHTML='<b>'+res.length+'</b>';
}

function SR(c){
  var ks=['','ip','port','latency_ms','provider','http_status','tls_valid','server_header'];
  var k=ks[c];
  if(!k)return;
  SD[k]=!SD[k];
  A.sort(function(a,b){
    var x=a[k],y=b[k];
    if(typeof x==='string')return SD[k]?x.localeCompare(y):y.localeCompare(x);
    return SD[k]?x-y:y-x;
  });
  RN();
}

function LF(){
  fetch('/api/files').then(function(r){return r.json()}).then(function(fs){
    var el=document.getElementById('fl');
    if(!fs.length){el.innerHTML='No files';return}
    var h='';
    for(var i=0;i<fs.length;i++){
      var f=fs[i];
      var sz=f.size<1024?f.size+'B':f.size<1048576?(f.size/1024).toFixed(1)+'KB':(f.size/1048576).toFixed(1)+'MB';
      h+='<div class="fi"><span>'+f.name+' ('+sz+')</span><a href="/api/download/'+f.name+'" download>Download</a></div>';
    }
    el.innerHTML=h;
  }).catch(function(){});
}

function L(m,t){
  var b=document.getElementById('lg');
  var d=document.createElement('div');
  d.className='le '+(t||'info');
  d.textContent='['+new Date().toLocaleTimeString()+'] '+m;
  b.appendChild(d);
  b.scrollTop=b.scrollHeight;
  while(b.children.length>100)b.removeChild(b.firstChild);
}

function SS(t,a){
  document.getElementById('stx').textContent=t;
  document.getElementById('dot').className=a?'dt on':'dt';
}

function TT(m){
  var t=document.createElement('div');
  t.className='tt';
  t.textContent=m;
  document.body.appendChild(t);
  setTimeout(function(){if(t.parentNode)t.remove()},3000);
}

I();
</script>
</body>
</html>'''
