
from pathlib import Path

dest = Path(__file__).with_name('index.html')

parts = []

parts.append(r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Fit Journey 💪 | Oct 2026 – Oct 2027</title>
  <meta name="description" content="Personal daily fitness tracker — 1 year transformation from Oct 20, 2026">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root{--bg:#070A13;--bg2:#0C1020;--card:rgba(255,255,255,0.042);--border:rgba(255,255,255,0.08);--border2:rgba(255,255,255,0.14);--t1:#EEF0FF;--t2:#8892B0;--t3:#4A5270;--purple:#A855F7;--pink:#EC4899;--green:#10B981;--yellow:#F59E0B;--r:16px;--r-sm:10px}
    *{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
    body{font-family:'Space Grotesk',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;overflow-x:hidden}
    .orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0;filter:blur(80px)}
    .orb-1{width:600px;height:600px;top:-180px;right:-180px;background:radial-gradient(circle,rgba(168,85,247,.13) 0%,transparent 70%)}
    .orb-2{width:500px;height:500px;bottom:-160px;left:-160px;background:radial-gradient(circle,rgba(236,72,153,.11) 0%,transparent 70%)}
    .header{position:sticky;top:0;z-index:100;background:rgba(7,10,19,.9);backdrop-filter:blur(24px);border-bottom:1px solid var(--border)}
    .hi{max-width:980px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
    .logo{font-family:'Outfit',sans-serif;font-weight:900;font-size:1.15rem;background:linear-gradient(135deg,var(--purple),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;white-space:nowrap}
    .daybadge{background:linear-gradient(135deg,rgba(168,85,247,.22),rgba(236,72,153,.18));border:1px solid rgba(168,85,247,.32);border-radius:50px;padding:4px 14px;font-size:.76rem;font-weight:700;color:var(--purple);white-space:nowrap}
    .hdate{font-size:.82rem;color:var(--t2);flex:1;text-align:center}
    .pw{min-width:180px;max-width:280px;flex:1}
    .pl{display:flex;justify-content:space-between;font-size:.69rem;color:var(--t3);margin-bottom:5px}
    .pb{height:5px;background:rgba(255,255,255,.08);border-radius:50px;overflow:hidden}
    .pf{height:100%;background:linear-gradient(90deg,var(--purple),var(--pink));border-radius:50px;transition:width 1.2s cubic-bezier(.4,0,.2,1)}
    .main{max-width:980px;margin:0 auto;padding:24px 20px 80px;position:relative;z-index:1}
    .qcard{background:linear-gradient(135deg,rgba(168,85,247,.12),rgba(236,72,153,.07));border:1px solid rgba(168,85,247,.22);border-radius:var(--r);padding:28px 36px;margin-bottom:22px;position:relative;overflow:hidden;animation:fadeUp .6s ease both}
    .qcard::before{content:'"';position:absolute;top:-30px;left:14px;font-size:12rem;font-family:'Outfit',sans-serif;color:rgba(168,85,247,.09);line-height:1;user-select:none;pointer-events:none}
    .qlbl{font-size:.69rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--purple);margin-bottom:10px}
    .qtxt{font-family:'Outfit',sans-serif;font-size:1.28rem;font-weight:600;line-height:1.55;color:var(--t1);max-width:720px;position:relative;z-index:1}
    .qauth{margin-top:10px;font-size:.84rem;color:var(--t2)}
    .srow{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:22px}
    .scard{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:16px 18px;display:flex;align-items:center;gap:12px;animation:fadeUp .6s ease both}
    .sico{font-size:1.7rem}.slbl{font-size:.7rem;color:var(--t2);margin-bottom:2px}
    .sval{font-family:'Outfit',sans-serif;font-size:1.35rem;font-weight:800;color:var(--t1)}.sval.due{color:var(--pink)}
    .wcard{background:var(--card);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;margin-bottom:22px;animation:fadeUp .65s ease .1s both}
    .wban{padding:26px 30px;position:relative;overflow:hidden}
    .wban::after{content:'';position:absolute;inset:0;background:rgba(0,0,0,.28)}
    .wbc{position:relative;z-index:1}
    .wbday{font-size:.69rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;opacity:.85;margin-bottom:5px}
    .wbname{font-family:'Outfit',sans-serif;font-size:1.65rem;font-weight:900;line-height:1.2}
    .wbemi{position:absolute;right:28px;top:50%;transform:translateY(-50%);font-size:4rem;opacity:.35;z-index:1}
    .wbody{padding:10px 24px 22px}
    .slbl2{font-size:.68rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--t3);margin:18px 0 8px}
    .ibox{background:rgba(255,255,255,.04);border-radius:var(--r-sm);padding:12px 16px;font-size:.86rem;color:var(--t2);line-height:1.65}
    .exhead{display:flex;gap:10px;padding:8px 12px;font-size:.68rem;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:var(--t3);background:rgba(255,255,255,.03);border-radius:8px 8px 0 0}
    .exrows{background:rgba(255,255,255,.03);border-radius:0 0 8px 8px;overflow:hidden}
    .exrow{display:flex;align-items:center;gap:10px;padding:13px 12px;border-top:1px solid rgba(255,255,255,.04);cursor:pointer;transition:background .2s}
    .exrow:hover{background:rgba(255,255,255,.05)}.exrow:first-child{border-top:none}
    .exc{width:26px;height:26px;flex-shrink:0;border:2px solid var(--border2);border-radius:50%;display:flex;align-items:center;justify-content:center;transition:all .25s}
    .exrow.done .exc{background:linear-gradient(135deg,var(--purple),var(--pink));border-color:transparent;box-shadow:0 0 12px rgba(168,85,247,.4)}
    .exrow.done .exc::after{content:'✓';color:#fff;font-size:.72rem;font-weight:800}
    .exname{flex:1;font-size:.9rem;font-weight:500;transition:all .22s}
    .exrow.done .exname{text-decoration:line-through;color:var(--t3)}
    .exsets{min-width:90px;font-size:.8rem;color:var(--purple);font-weight:600}
    .exrest{min-width:65px;font-size:.78rem;color:var(--t2)}
    .exwt{min-width:110px;font-size:.78rem;color:var(--yellow)}
    .rbtn{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.06);border:1px solid var(--border2);border-radius:8px;padding:7px 14px;font-size:.8rem;color:var(--t2);cursor:pointer;transition:all .2s;margin-top:14px;user-select:none}
    .rbtn:hover{background:rgba(168,85,247,.15);color:var(--t1);border-color:rgba(168,85,247,.3)}
    .rnotes{list-style:none;padding:10px 0 0}
    .rnotes li{display:flex;gap:10px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.04);font-size:.9rem;color:var(--t2);line-height:1.55}
    .rnotes li:last-child{border-bottom:none}
    .tcol{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:22px}
    .ccard{background:var(--card);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;animation:fadeUp .65s ease .18s both}
    .ccard:last-child{animation-delay:.26s}
    .chead{padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
    .ctitle{font-family:'Outfit',sans-serif;font-weight:700;font-size:1rem}
    .cpct{font-size:.75rem;color:var(--t2);font-weight:500}
    .cbody{padding:8px 18px 12px}
    .ci{display:flex;align-items:flex-start;gap:11px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.04);cursor:pointer;transition:all .2s;border-radius:8px}
    .ci:last-child{border-bottom:none}
    .ci:hover{background:rgba(255,255,255,.03);padding:11px 8px;margin:0 -8px}
    .cbox{width:22px;height:22px;flex-shrink:0;border:2px solid var(--border2);border-radius:6px;display:flex;align-items:center;justify-content:center;transition:all .22s;margin-top:2px}
    .ci.done .cbox{background:var(--green);border-color:var(--green);box-shadow:0 0 10px rgba(16,185,129,.35)}
    .ci.done .cbox::after{content:'✓';color:#fff;font-size:.72rem;font-weight:800}
    .clbl{font-size:.88rem;font-weight:600;transition:all .22s;line-height:1.4}
    .ci.done .clbl{text-decoration:line-through;color:var(--t3)}
    .cdesc{font-size:.78rem;color:var(--t2);margin-top:3px;line-height:1.5}
    .ctip{font-size:.74rem;color:var(--purple);margin-top:3px}
    .wkcard{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:18px 22px;margin-bottom:22px;animation:fadeUp .65s ease .3s both}
    .wktitle{font-family:'Outfit',sans-serif;font-weight:700;font-size:.95rem;color:var(--t2);margin-bottom:14px}
    .wkdays{display:flex;gap:8px;flex-wrap:wrap}
    .wkd{flex:1;min-width:80px;background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:var(--r-sm);padding:10px 8px;text-align:center}
    .wkd.today{border-color:rgba(168,85,247,.4);background:rgba(168,85,247,.1)}
    .wkdn{font-weight:700;font-size:.7rem;color:var(--t2);margin-bottom:5px;letter-spacing:.5px}
    .wkd.today .wkdn{color:var(--purple)}
    .wkde{font-size:1.3rem;margin-bottom:3px}
    .wkdt{font-size:.66rem;color:var(--t3);line-height:1.3}
    .wkd.today .wkdt{color:var(--t2)}
    .hcard{background:var(--card);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;animation:fadeUp .65s ease .35s both}
    .htoggle{width:100%;background:none;border:none;color:var(--t1);padding:18px 22px;text-align:left;cursor:pointer;display:flex;align-items:center;justify-content:space-between;font-family:'Outfit',sans-serif;font-size:1rem;font-weight:700;transition:background .2s}
    .htoggle:hover{background:rgba(255,255,255,.03)}
    .harrow{transition:transform .3s ease;font-size:.82rem;color:var(--t2)}
    .hbody{display:none;padding:0 22px 22px;overflow-x:auto}.hbody.open{display:block}
    .htbl{width:100%;border-collapse:collapse;font-size:.84rem}
    .htbl th{text-align:left;padding:8px 12px;font-size:.69rem;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:var(--t3);border-bottom:1px solid var(--border)}
    .htbl td{padding:12px;border-bottom:1px solid rgba(255,255,255,.03);color:var(--t2)}
    .htbl tr:last-child td{border-bottom:none}.htbl td:first-child{color:var(--t1);font-weight:600}
    .cg{color:var(--green);font-size:.72rem}.cb2{color:#EF4444;font-size:.72rem}
    .moverlay{position:fixed;inset:0;background:rgba(0,0,0,.88);backdrop-filter:blur(12px);z-index:900;display:none;align-items:center;justify-content:center;padding:20px}
    .moverlay.active{display:flex;animation:fadeIn .3s ease}
    .modal{background:#0D1122;border:1px solid rgba(168,85,247,.32);border-radius:20px;padding:36px 32px;max-width:470px;width:100%;box-shadow:0 0 80px rgba(168,85,247,.22);animation:slideUp .4s cubic-bezier(.16,1,.3,1)}
    .mbadge{display:inline-block;background:linear-gradient(135deg,rgba(168,85,247,.2),rgba(236,72,153,.2));border:1px solid rgba(168,85,247,.3);border-radius:50px;padding:4px 14px;font-size:.72rem;font-weight:700;color:var(--purple);margin-bottom:12px;letter-spacing:1px;text-transform:uppercase}
    .mtitle{font-family:'Outfit',sans-serif;font-size:1.6rem;font-weight:900;margin-bottom:8px;background:linear-gradient(135deg,var(--purple),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
    .msub{font-size:.87rem;color:var(--t2);margin-bottom:26px;line-height:1.6}
    .fgrp{margin-bottom:16px}
    .flbl{display:block;font-size:.8rem;font-weight:600;color:var(--t2);margin-bottom:8px}
    .opt{color:var(--t3);font-weight:400;font-size:.74rem}
    .irow{display:flex;gap:8px}
    .finp{flex:1;background:rgba(255,255,255,.06);border:1px solid var(--border2);border-radius:var(--r-sm);padding:12px 14px;font-family:'Space Grotesk',sans-serif;font-size:1rem;color:var(--t1);outline:none;transition:border-color .2s,box-shadow .2s}
    .finp:focus{border-color:var(--purple);box-shadow:0 0 0 3px rgba(168,85,247,.16)}
    .finp::placeholder{color:var(--t3)}
    .utag{display:flex;align-items:center;padding:12px 14px;background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:var(--r-sm);color:var(--t2);font-size:.82rem;white-space:nowrap}
    .bsave{width:100%;background:linear-gradient(135deg,var(--purple),var(--pink));border:none;border-radius:12px;padding:14px;font-family:'Outfit',sans-serif;font-size:1rem;font-weight:700;color:#fff;cursor:pointer;transition:all .22s;margin-top:6px}
    .bsave:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(168,85,247,.4)}
    .bskip{width:100%;background:transparent;border:none;color:var(--t3);font-size:.84rem;cursor:pointer;padding:10px;margin-top:4px;transition:color .2s;font-family:'Space Grotesk',sans-serif}
    .bskip:hover{color:var(--t2)}
    .imgm{position:fixed;inset:0;background:rgba(0,0,0,.93);z-index:1000;display:none;align-items:center;justify-content:center;padding:20px;cursor:zoom-out}
    .imgm.active{display:flex;animation:fadeIn .25s ease}
    .imgm img{max-width:100%;max-height:90vh;border-radius:12px;object-fit:contain}
    .imgclose{position:fixed;top:20px;right:24px;background:rgba(255,255,255,.1);border:1px solid var(--border2);border-radius:50%;width:38px;height:38px;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:1rem;color:var(--t2);transition:all .2s;z-index:1001}
    .imgclose:hover{background:rgba(255,255,255,.2);color:var(--t1)}
    .toast{position:fixed;top:24px;right:24px;background:linear-gradient(135deg,var(--purple),var(--pink));color:#fff;padding:14px 20px;border-radius:12px;font-weight:600;font-size:.9rem;z-index:800;transform:translateX(calc(100% + 40px));transition:transform .4s cubic-bezier(.16,1,.3,1);box-shadow:0 8px 32px rgba(168,85,247,.4);max-width:300px;line-height:1.4}
    .toast.show{transform:translateX(0)}
    @keyframes fadeIn{from{opacity:0}to{opacity:1}}
    @keyframes fadeUp{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
    @keyframes slideUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
    @media(max-width:720px){.tcol{grid-template-columns:1fr}.exrest,.exwt{display:none}.wbname{font-size:1.35rem}.qtxt{font-size:1.1rem}.modal{padding:28px 20px}.wkd{min-width:60px;padding:8px 5px}}
    @media(max-width:480px){.srow{grid-template-columns:1fr 1fr}.scard:last-child{grid-column:span 2}.hdate{display:none}}
  </style>
</head>
<body>
<div class="orb orb-1"></div><div class="orb orb-2"></div>
<header class="header">
  <div class="hi">
    <div class="logo">💪 My Fit Journey</div>
    <div class="daybadge" id="dayBadge">Day 1 / 366</div>
    <div class="hdate" id="hDate">—</div>
    <div class="pw">
      <div class="pl"><span>Journey Progress</span><span id="pPct">0%</span></div>
      <div class="pb"><div class="pf" id="pFill" style="width:0%"></div></div>
    </div>
  </div>
</header>
<main class="main">
  <div class="qcard">
    <div class="qlbl">✨ Today's Motivation</div>
    <div class="qtxt" id="qTxt">Loading…</div>
    <div class="qauth" id="qAuth"></div>
  </div>
  <div class="srow">
    <div class="scard"><div class="sico">🔥</div><div><div class="slbl">Streak</div><div class="sval" id="sSt">0 days</div></div></div>
    <div class="scard"><div class="sico">📅</div><div><div class="slbl">Days Left</div><div class="sval" id="sDl">366</div></div></div>
    <div class="scard"><div class="sico">📏</div><div><div class="slbl">Next Measure</div><div class="sval" id="sNm">—</div></div></div>
  </div>
  <div id="wSection"></div>
  <div class="wkcard">
    <div class="wktitle">📆 Weekly Workout Plan</div>
    <div class="wkdays" id="wkDays"></div>
  </div>
  <div class="tcol">
    <div class="ccard"><div class="chead"><div class="ctitle">🏋️ Gym Checklist</div><div class="cpct" id="gPct">0 / —</div></div><div class="cbody" id="gBody"></div></div>
    <div class="ccard"><div class="chead"><div class="ctitle">🥗 Diet Checklist</div><div class="cpct" id="dPct">0 / 4</div></div><div class="cbody" id="dBody"></div></div>
  </div>
  <div class="hcard">
    <button class="htoggle" onclick="togH()">📊 Body Measurement History <span class="harrow" id="hArr">▼</span></button>
    <div class="hbody" id="hBody"><div id="hCont"></div></div>
  </div>
</main>
<div class="moverlay" id="mModal">
  <div class="modal">
    <div class="mbadge" id="mBadge">Month 1 Check-In</div>
    <div class="mtitle">📏 Progress Check-In!</div>
    <div class="msub" id="mSub">It has been 30 days! Record your measurements to track your amazing transformation!</div>
    <div class="fgrp"><label class="flbl">Waist Measurement</label><div class="irow"><input class="finp" id="iW" type="number" placeholder="e.g. 32" step="0.1" min="0"><div class="utag">inches / cm</div></div></div>
    <div class="fgrp"><label class="flbl">Hip Measurement</label><div class="irow"><input class="finp" id="iH" type="number" placeholder="e.g. 38" step="0.1" min="0"><div class="utag">inches / cm</div></div></div>
    <div class="fgrp"><label class="flbl">Breast Measurement</label><div class="irow"><input class="finp" id="iB" type="number" placeholder="e.g. 36" step="0.1" min="0"><div class="utag">inches / cm</div></div></div>
    <div class="fgrp"><label class="flbl">Weight <span class="opt">(optional)</span></label><div class="irow"><input class="finp" id="iWt" type="number" placeholder="e.g. 65" step="0.1" min="0"><div class="utag">kg</div></div></div>
    <button class="bsave" onclick="saveM()">💾 Save My Measurements</button>
    <button class="bskip" onclick="skipM()">Remind me tomorrow →</button>
  </div>
</div>
<div class="imgm" id="imgM" onclick="closeImg()"><div class="imgclose" onclick="closeImg()">✕</div><img id="imgS" src="" alt="Workout Reference" onclick="event.stopPropagation()"></div>
<div class="toast" id="toast">🎉 Keep going!</div>
""")

parts.append(r"""<script>
const START=new Date(2026,9,20),END=new Date(2027,9,20),TOTAL=calendarDaysBetween(START,END)+1,KEY='fitJourney_v4';
const Q=[
{t:"Your body can stand almost anything. It's your mind you have to convince.",a:"Anonymous"},
{t:"The only bad workout is the one that didn't happen.",a:"Anonymous"},
{t:"Push yourself because no one else is going to do it for you.",a:"Anonymous"},
{t:"Success isn't always about greatness. It's about consistency.",a:"Dwayne Johnson"},
{t:"The pain you feel today will be the strength you feel tomorrow.",a:"Anonymous"},
{t:"Don't stop when you're tired. Stop when you're done.",a:"Anonymous"},
{t:"Wake up with determination. Go to bed with satisfaction.",a:"Anonymous"},
{t:"You are one workout away from a good mood.",a:"Anonymous"},
{t:"Small steps every day add up to miles of progress.",a:"Anonymous"},
{t:"Your health is an investment, not an expense.",a:"Anonymous"},
{t:"Be stronger than your excuses.",a:"Anonymous"},
{t:"Train insane or remain the same.",a:"Anonymous"},
{t:"The body achieves what the mind believes.",a:"Anonymous"},
{t:"Every rep, every step, every drop of sweat is proof of your commitment.",a:"Anonymous"},
{t:"You don't have to be extreme. Just consistent.",a:"Anonymous"},
{t:"Fitness is about being better than you used to be.",a:"Anonymous"},
{t:"Your future self is watching you right now through your memories.",a:"Anonymous"},
{t:"A little progress each day adds up to big results.",a:"Anonymous"},
{t:"You are what you repeatedly do. Excellence is a habit.",a:"Aristotle"},
{t:"Fall in love with taking care of yourself.",a:"Anonymous"},
{t:"Nothing will work unless you do.",a:"Maya Angelou"},
{t:"Make yourself proud.",a:"Anonymous"},
{t:"The secret of getting ahead is getting started.",a:"Mark Twain"},
{t:"Don't wish for it. Work for it.",a:"Anonymous"},
{t:"You are tougher than you think.",a:"Anonymous"},
{t:"Champions keep playing until they get it right.",a:"Billie Jean King"},
{t:"Believe you can and you're halfway there.",a:"Theodore Roosevelt"},
{t:"It always seems impossible until it's done.",a:"Nelson Mandela"},
{t:"Energy and persistence conquer all things.",a:"Benjamin Franklin"},
{t:"You've got what it takes — but it will take everything you've got.",a:"Anonymous"},
{t:"Don't limit your challenges. Challenge your limits.",a:"Anonymous"},
{t:"Good things come to those who sweat.",a:"Anonymous"},
{t:"Progress, not perfection.",a:"Anonymous"},
{t:"Show up. Even on the hard days.",a:"Anonymous"},
{t:"Eat well, move often, sleep deeply, be happy.",a:"Anonymous"},
{t:"Strong is the new beautiful.",a:"Anonymous"},
{t:"Discipline is choosing between what you want now and what you want most.",a:"Abraham Lincoln"},
{t:"Today is another chance to get stronger.",a:"Anonymous"},
{t:"You didn't come this far to only come this far.",a:"Anonymous"},
{t:"Be patient with yourself. Nothing in nature blooms all year.",a:"Anonymous"},
{t:"Motivation gets you started. Habit keeps you going.",a:"Jim Ryun"},
{t:"One year from now you'll wish you had started today.",a:"Karen Lamb"},
{t:"Every day is a new beginning. Take a deep breath and start again.",a:"Anonymous"},
{t:"What seems hard now will one day be your warm-up.",a:"Anonymous"},
{t:"Sore today. Strong tomorrow.",a:"Anonymous"},
{t:"Look in the mirror — that's your competition.",a:"Anonymous"},
{t:"Your body hears everything your mind says. Stay positive.",a:"Anonymous"},
{t:"Winners never quit, and quitters never win.",a:"Vince Lombardi"},
{t:"Strive for progress, not perfection.",a:"Anonymous"},
{t:"Pain is temporary. Pride is forever.",a:"Anonymous"},
{t:"Don't count the days — make the days count.",a:"Muhammad Ali"},
{t:"When you feel like quitting, think about why you started.",a:"Anonymous"},
{t:"Every workout is a step toward the best version of you.",a:"Anonymous"},
{t:"Strength comes from an indomitable will.",a:"Gandhi"},
{t:"The only person to be better than is who you were yesterday.",a:"Anonymous"},
{t:"Take care of your body. It's the only place you have to live.",a:"Jim Rohn"},
{t:"She believed she could, so she did.",a:"R.S. Grey"},
{t:"Hustle for that muscle.",a:"Anonymous"},
{t:"Your only limit is the one you set yourself.",a:"Anonymous"},
{t:"Fit is not a destination. It is a way of life.",a:"Anonymous"},
{t:"Each morning we are born again. What we do today matters most.",a:"Buddha"},
{t:"Success is the sum of small efforts repeated day in and day out.",a:"Robert Collier"},
{t:"You've survived 100% of your hardest days. You're unstoppable.",a:"Anonymous"},
{t:"Great things never came from comfort zones.",a:"Anonymous"},
{t:"If it doesn't challenge you, it doesn't change you.",a:"Fred DeVito"},
{t:"Your body is the vehicle for your dreams. Keep it running.",a:"Anonymous"},
{t:"Tough times never last, but tough people do.",a:"Robert H. Schuller"},
{t:"Keep going. You are making progress even when you can't see it.",a:"Anonymous"},
{t:"Dedication sees dreams come true.",a:"Kobe Bryant"},
{t:"You don't find willpower. You create it.",a:"Anonymous"},
{t:"Transform your mind, transform your body.",a:"Anonymous"},
{t:"Don't stop until you're proud.",a:"Anonymous"},
{t:"Push harder than yesterday if you want a different tomorrow.",a:"Anonymous"},
{t:"The pain of discipline weighs ounces. The pain of regret weighs tons.",a:"Jim Rohn"},
{t:"I am stronger than my excuses.",a:"Anonymous"},
{t:"Get comfortable being uncomfortable.",a:"Anonymous"},
{t:"You didn't wake up today to be average.",a:"Anonymous"},
{t:"You are braver than you believe and stronger than you seem.",a:"A.A. Milne"},
{t:"Work hard in silence, let your results make the noise.",a:"Frank Ocean"},
{t:"Commit to be fit.",a:"Anonymous"},
{t:"If you are tired of starting over, stop giving up.",a:"Anonymous"},
{t:"Results happen over time, not overnight. Work hard, stay consistent.",a:"Anonymous"},
{t:"Fitness is a lifestyle, not a phase.",a:"Anonymous"},
{t:"Being defeated is temporary. Giving up is permanent.",a:"Marilyn vos Savant"},
{t:"Rise above the storm and you will find the sunshine.",a:"Mario Fernandez"},
{t:"Invest in your health today, reap rewards for a lifetime.",a:"Anonymous"},
{t:"Your dedication today builds the body you'll be proud of tomorrow.",a:"Anonymous"},
{t:"Excuses don't burn calories.",a:"Anonymous"},
{t:"Every step forward is a step in the right direction.",a:"Anonymous"},
{t:"Eat right, train hard, think positive.",a:"Anonymous"},
{t:"Don't pray for an easy life. Pray for the strength to endure a difficult one.",a:"Bruce Lee"},
{t:"Today's workout is tomorrow's transformation.",a:"Anonymous"},
{t:"You earn your body.",a:"Anonymous"},
{t:"Act the way you want to feel, and you'll feel the way you act.",a:"Anonymous"},
{t:"The secret of your future is hidden in your daily routine.",a:"Mike Murdock"},
{t:"Sweat is magic. Cover yourself in it daily to grant your wishes.",a:"Anonymous"},
{t:"There is no shortcut to any place worth going.",a:"Beverly Sills"},
{t:"You have what it takes. Go prove it.",a:"Anonymous"},
{t:"Believe in the process. Every drop of effort counts.",a:"Anonymous"}
];
const DD=[
{name:"Complete Rest and Recovery",emoji:"🛌",st:"Rest Day",isRest:true,imgFile:null,warmup:null,cardio:null,exercises:[],cooldown:null,grad:"linear-gradient(135deg,#10B981,#3B82F6)",
rn:[{i:"💤",n:"No workout today. Muscles grow and fat loss gets easier when you recover."},{i:"🚶",n:"Light movement: An easy 15-20 min walk is fine, optional."},{i:"💧",n:"Hydration: Aim for 2.5-3 litres of water. Urine should be light yellow."},{i:"😴",n:"Sleep: Aim for 7-8 hours — poor sleep raises hunger and slows fat loss."},{i:"🥚",n:"Protein: Eggs, dal, paneer, curd, soya chunks, sprouts, chana — hostel-friendly!"},{i:"🎽",n:"Prep for Monday: Wash gym clothes, plan meals, check shoes and water bottle."}]},
{name:"Full Body Cardio and Strength",emoji:"🏃",st:"Cardio + Strength",isRest:false,imgFile:"monday.png",grad:"linear-gradient(135deg,#4A90D9,#7C3AED)",
warmup:"Brisk walk on treadmill (3 min), arm circles (10 each way), hip circles (10 each way), bodyweight squats (10), high knees (30 sec).",
cardio:"Treadmill or cycling 20-25 min at moderate pace. Treadmill: 5.5-6.5 km/h with 1-2% incline. Do cardio first, then strength.",
exercises:[{n:"Bodyweight Squats",s:"3 x 15",r:"45 sec",w:"Body weight"},{n:"Knee or Standard Push-ups",s:"3 x 8-12",r:"45 sec",w:"Body weight"},{n:"Glute Bridges",s:"3 x 15",r:"45 sec",w:"Body weight"},{n:"Dumbbell Bent-over Row",s:"3 x 10",r:"60 sec",w:"4-8 kg/hand"},{n:"Plank",s:"3 x 20-30s",r:"30 sec",w:"Body weight"}],
cooldown:"Quad stretch (30s each leg), hamstring stretch (30s each leg), chest doorway stretch (30s), child's pose (30s), deep breathing."},
{name:"Core and Abs",emoji:"💪",st:"Core & Abs",isRest:false,imgFile:"tuesday.png",grad:"linear-gradient(135deg,#E8834A,#EC4899)",
warmup:"Easy walk (2 min), torso twists (20), cat-cow (10), standing knee raises (20), arm swings (20).",
cardio:"Cross-trainer at medium resistance or fast walk at 6-6.5 km/h — 15 min.",
exercises:[{n:"Plank",s:"3 x 30-45s",r:"30 sec",w:"Body weight"},{n:"Crunches",s:"3 x 15",r:"30 sec",w:"Body weight"},{n:"Lying Leg Raises",s:"3 x 10-12",r:"45 sec",w:"Body weight"},{n:"Bicycle Crunches",s:"3 x 20 total",r:"30 sec",w:"Body weight"},{n:"Russian Twists",s:"3 x 20 total",r:"30 sec",w:"None or 2-4 kg"},{n:"Mountain Climbers",s:"3 x 20 sec",r:"30 sec",w:"Body weight"}],
cooldown:"Cobra stretch (30s), child's pose (30s), seated spinal twist (30s each side), knee-to-chest hug (30s each)."},
{name:"Upper Body Chest and Back",emoji:"🏋️",st:"Upper Body",isRest:false,imgFile:"wednesday.png",grad:"linear-gradient(135deg,#4ABDA8,#06B6D4)",
warmup:"Light cycling or walking (3 min), arm circles (15 each way), shoulder rolls (15), band or wall slides (10), 10 push-ups on knees.",
cardio:"Light cycling or easy cross-trainer pace — 15 min.",
exercises:[{n:"Machine Chest Press",s:"3 x 10-12",r:"60-75 sec",w:"15-25 kg"},{n:"Lat Pulldown",s:"3 x 10-12",r:"60-75 sec",w:"25-35 kg"},{n:"Seated Cable Row",s:"3 x 10-12",r:"60-75 sec",w:"20-30 kg"},{n:"Incline or Knee Push-ups",s:"2 x 10",r:"45 sec",w:"Body weight"},{n:"Dumbbell Shoulder Press (seated)",s:"2 x 10",r:"60 sec",w:"3-6 kg/hand"}],
cooldown:"Cross-body shoulder stretch (30s each), chest wall stretch (30s each), lat stretch (30s), neck tilts (20s each side)."},
{name:"Lower Body and Legs",emoji:"🦵",st:"Legs and Glutes",isRest:false,imgFile:"thursday.png",grad:"linear-gradient(135deg,#E84A6F,#F59E0B)",
warmup:"Light cycling or walk (4 min), leg swings (10 each leg, front and side), bodyweight squats (10), walking lunges (6 each leg).",
cardio:null,
exercises:[{n:"Goblet Squat",s:"3 x 12",r:"60-75 sec",w:"6-12 kg dumbbell"},{n:"Dumbbell Lunges (alternating)",s:"3 x 10/leg",r:"60 sec",w:"4-8 kg/hand"},{n:"Step-ups (bench or box)",s:"3 x 10/leg",r:"60 sec",w:"4-8 kg/hand"},{n:"Romanian Deadlift (dumbbell)",s:"3 x 10",r:"60-75 sec",w:"6-10 kg/hand"},{n:"Standing Calf Raises",s:"3 x 15-20",r:"30 sec",w:"BW or 5-10 kg"}],
cooldown:"Quad stretch (30s each), hamstring stretch (30s each), figure-4 glute stretch (30s each), calf wall stretch (30s each), butterfly stretch (30s)."},
{name:"Full Body Fat Burner",emoji:"🔥",st:"Fat Burn + Arms",isRest:false,imgFile:"friday.png",grad:"linear-gradient(135deg,#9B4AE8,#EC4899)",
warmup:"Easy walk (3 min), jumping jacks or step-jacks (30s), arm circles (15), hip rotations (10 each way).",
cardio:"30 min: Alternate 2 min fast (6.5-7.5 km/h, 3-5% incline) and 2 min moderate (5.5 km/h). Or use cross-trainer, bike, or rower at 7-8/10 effort.",
exercises:[{n:"Dumbbell Biceps Curl",s:"3 x 12",r:"45 sec",w:"3-6 kg/hand"},{n:"Hammer Curl",s:"2 x 12",r:"45 sec",w:"3-6 kg/hand"},{n:"Overhead Triceps Extension",s:"3 x 12",r:"45 sec",w:"3-6 kg both hands"},{n:"Bench Dips or Triceps Kickbacks",s:"3 x 10",r:"45 sec",w:"BW or 2-4 kg"}],
cooldown:"Biceps wall stretch (30s each), triceps overhead stretch (30s each), forward fold (30s), slow walk with deep breaths (2 min)."},
{name:"Flexibility Yoga and Recovery",emoji:"🧘",st:"Yoga and Stretch",isRest:false,imgFile:"saturday.png",grad:"linear-gradient(135deg,#E8C84A,#10B981)",
warmup:"Easy walk or march in place (3 min), neck and shoulder rolls, gentle torso twists.",
cardio:"Optional: 15-min relaxed walk before or after yoga.",
exercises:[{n:"Cat-Cow",s:"10 slow reps",r:"—",w:"Body weight"},{n:"Downward-Facing Dog",s:"Hold 30-45 sec",r:"—",w:"Body weight"},{n:"Low Lunge (each side)",s:"Hold 30-45 sec",r:"—",w:"Body weight"},{n:"Pigeon Pose or Figure-4 Stretch",s:"Hold 30-45s/side",r:"—",w:"Body weight"},{n:"Seated Forward Fold",s:"Hold 30-45 sec",r:"—",w:"Body weight"},{n:"Cobra Pose",s:"Hold 30-45 sec",r:"—",w:"Body weight"},{n:"Child's Pose",s:"1 min",r:"—",w:"Body weight"},{n:"Supine Spinal Twist (each side)",s:"Hold 30-45s/side",r:"—",w:"Body weight"}],
cooldown:"Lie on back with legs up the wall for 2-3 min. Slow belly breathing (4 sec in, 6 sec out)."}
];
const DT=[
{l:"🌅 Breakfast",d:"1 glass milk + 1 small piece 70%+ dark chocolate + 1 handful roasted chana",t:"Zero cooking — super fast!"},
{l:"☀️ Lunch (11:00 AM)",d:"1 roti + 1 bowl dal + homemade lemon-turmeric pickle",t:"Add paneer 2x/week for protein boost"},
{l:"🍎 Evening Snack (4-5 PM)",d:"1 fruit (Apple, Orange, or Watermelon) + 1 handful roasted chana",t:"Watermelon or orange is great for hydration!"},
{l:"🌙 Dinner",d:"Yogabar dark chocolate oats OR oil-free popped makhana",t:"Eat at least 2 hours before sleep"}
];
function load(){try{return JSON.parse(localStorage.getItem(KEY))||{}}catch{return{}}}
function save(d){localStorage.setItem(KEY,JSON.stringify(d))}
function tk(){const d=new Date();return d.getFullYear()+'-'+p(d.getMonth()+1)+'-'+p(d.getDate())}
function p(n){return String(n).padStart(2,'0')}
function calendarDay(d){return Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/86400000}
function calendarDaysBetween(a,b){return calendarDay(b)-calendarDay(a)}
function parseDateKey(key){const parts=key.split('-').map(Number);return new Date(parts[0],parts[1]-1,parts[2])}
function dn(){
  const diff=calendarDaysBetween(START,new Date())+1;
  return diff<1?0:diff>TOTAL?TOTAL+1:diff;
}
function fmtD(d){
  const DY=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  const MO=['January','February','March','April','May','June','July','August','September','October','November','December'];
  return DY[d.getDay()]+', '+d.getDate()+' '+MO[d.getMonth()]+' '+d.getFullYear();
}
function calcStr(){
  const data=load();const dd=data.dailyData||{};let s=0;
  const c=new Date();c.setHours(0,0,0,0);
  for(let i=1;i<=TOTAL;i++){c.setDate(c.getDate()-1);const k=c.getFullYear()+'-'+p(c.getMonth()+1)+'-'+p(c.getDate());if(dd[k]&&dd[k].completed)s++;else break;}
  return s;
}
function needsM(){
  const d2=dn();if(d2<1||d2>TOTAL)return false;
  const data=load();if(data.skD===tk())return false;
  const ms=data.ms||[];
  const last=ms.length?parseDateKey(ms[ms.length-1].date):START;
  return calendarDaysBetween(last,new Date())>=30;
}
function nextMin(){
  const d2=dn();if(d2>TOTAL)return "Journey complete 🏆";
  const ms=(load().ms)||[];
  const last=ms.length?parseDateKey(ms[ms.length-1].date):START;
  const left=30-calendarDaysBetween(last,new Date());
  return left<=0?"Due now! 🔔":"In "+left+" days";
}
function rStats(){
  const d2=dn();const tod=new Date();const pct=d2<=0?0:Math.min(100,Math.round(d2/TOTAL*100));
  document.getElementById('dayBadge').textContent=d2<=0?'Starts Soon!':d2>TOTAL?'DONE! 🏆':'Day '+d2+' / '+TOTAL;
  document.getElementById('hDate').textContent=fmtD(tod);
  document.getElementById('pPct').textContent=pct+'%';
  document.getElementById('pFill').style.width=pct+'%';
  document.getElementById('sSt').textContent=calcStr()+' days';
  document.getElementById('sDl').textContent=d2<=0?TOTAL:Math.max(0,TOTAL-d2+1);
  const nm=nextMin();const el=document.getElementById('sNm');
  el.textContent=nm;el.className='sval'+(nm.includes('now')?' due':'');
}
function rQuote(){
  const d2=dn()<1?1:dn();const q=Q[(d2-1)%Q.length];
  document.getElementById('qTxt').textContent=q.t;
  document.getElementById('qAuth').textContent='— '+q.a;
}
function rWeek(){
  const tod=new Date().getDay();
  const L=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
  document.getElementById('wkDays').innerHTML=DD.map((w,i)=>`<div class="wkd ${i===tod?'today':''}"><div class="wkdn">${L[i]}</div><div class="wkde">${w.emoji}</div><div class="wkdt">${w.st}</div></div>`).join('');
}
function rWorkout(){
  const d2=dn();const sec=document.getElementById('wSection');
  if(d2<=0){sec.innerHTML='<div class="wcard"><div class="wban" style="background:linear-gradient(135deg,#4A5270,#2D3748)"><div class="wbemi">🚀</div><div class="wbc"><div class="wbday">GET READY</div><div class="wbname">Your journey begins October 20, 2026!</div></div></div></div>';return;}
  if(d2>TOTAL){sec.innerHTML='<div class="wcard"><div class="wban" style="background:linear-gradient(135deg,#F59E0B,#EF4444)"><div class="wbemi">🏆</div><div class="wbc"><div class="wbday">JOURNEY COMPLETE</div><div class="wbname">366 Days Done! You are an absolute LEGEND! 🎉</div></div></div></div>';return;}
  const dow=new Date().getDay();const w=DD[dow];
  const data=load();const key=tk();const gc=(data.dailyData&&data.dailyData[key]&&data.dailyData[key].gym)||[];
  if(w.isRest){
    sec.innerHTML='<div class="wcard"><div class="wban" style="background:'+w.grad+'"><div class="wbemi">'+w.emoji+'</div><div class="wbc"><div class="wbday">TODAY — REST DAY</div><div class="wbname">'+w.name+'</div></div></div><div class="wbody"><ul class="rnotes">'+w.rn.map(r=>'<li><span style="font-size:1.2rem;flex-shrink:0;margin-top:1px">'+r.i+'</span><span>'+r.n+'</span></li>').join('')+'</ul></div></div>';
    return;
  }
  const exRows=w.exercises.map((e,i)=>'<div class="exrow '+(gc[i]?'done':'')+'" onclick="tEx('+i+')"><div class="exc"></div><div class="exname">'+e.n+'</div><div class="exsets">'+e.s+'</div><div class="exrest">'+e.r+'</div><div class="exwt">'+e.w+'</div></div>').join('');
  const imgBtn=w.imgFile?'<div class="rbtn" onclick="openImg(\''+w.imgFile+'\')">📸 View Full Workout Reference Image</div>':'';
  sec.innerHTML='<div class="wcard"><div class="wban" style="background:'+w.grad+'"><div class="wbemi">'+w.emoji+'</div><div class="wbc"><div class="wbday">TODAY\'S WORKOUT</div><div class="wbname">'+w.name+'</div></div></div><div class="wbody">'+(w.warmup?'<div class="slbl2">🌱 WARM-UP</div><div class="ibox">'+w.warmup+'</div>':'')+(w.cardio?'<div class="slbl2">❤️ CARDIO</div><div class="ibox">'+w.cardio+'</div>':'')+'<div class="slbl2">💪 STRENGTH EXERCISES</div><div class="exhead"><div style="width:26px"></div><div style="flex:1">Exercise</div><div style="min-width:90px">Sets x Reps</div><div style="min-width:65px">Rest</div><div style="min-width:110px">Weight</div></div><div class="exrows">'+exRows+'</div>'+(w.cooldown?'<div class="slbl2">🧊 COOL-DOWN</div><div class="ibox">'+w.cooldown+'</div>':'')+imgBtn+'</div></div>';
}
function rGym(){
  const dow=new Date().getDay();const w=DD[dow];const d2=dn();
  const data=load();const key=tk();const gc=(data.dailyData&&data.dailyData[key]&&data.dailyData[key].gym)||[];
  const body=document.getElementById('gBody');const pct=document.getElementById('gPct');
  if(d2<=0||w.isRest||!w.exercises.length){body.innerHTML='<div style="text-align:center;padding:24px 0;color:var(--t2);font-size:.9rem">Rest day — no exercises today 🛌</div>';pct.textContent='Rest Day';return;}
  pct.textContent=gc.filter(Boolean).length+' / '+w.exercises.length;
  body.innerHTML=w.exercises.map((e,i)=>'<div class="ci '+(gc[i]?'done':'')+'" onclick="tGym('+i+')"><div class="cbox"></div><div><div class="clbl">'+e.n+'</div><div class="cdesc">'+e.s+' · Rest '+e.r+'</div></div></div>').join('');
}
function rDiet(){
  const data=load();const key=tk();const dc=(data.dailyData&&data.dailyData[key]&&data.dailyData[key].diet)||[];
  document.getElementById('dPct').textContent=dc.filter(Boolean).length+' / '+DT.length;
  document.getElementById('dBody').innerHTML=DT.map((item,i)=>'<div class="ci '+(dc[i]?'done':'')+'" onclick="tDiet('+i+')"><div class="cbox"></div><div><div class="clbl">'+item.l+'</div><div class="cdesc">'+item.d+'</div><div class="ctip">💡 '+item.t+'</div></div></div>').join('');
}
function rHist(){
  const ms=(load().ms)||[];const el=document.getElementById('hCont');
  if(!ms.length){el.innerHTML='<p style="color:var(--t2);font-size:.88rem;padding:10px 0">No measurements yet. First check-in after 30 days! 📅</p>';return;}
  const rows=ms.map((m,i)=>{let wc='',hc='';if(i>0){const dw=(m.waist-ms[i-1].waist).toFixed(1),dh=(m.hips-ms[i-1].hips).toFixed(1);wc='<span class="'+(dw<0?'cg':'cb2')+'">'+(dw>0?'+':'')+dw+'</span>';hc='<span class="'+(dh<0?'cg':'cb2')+'">'+(dh>0?'+':'')+dh+'</span>';}return'<tr><td>'+m.date+' <span style="font-size:.72rem;color:var(--t3)">(Month '+(i+1)+')</span></td><td>'+m.waist+' '+wc+'</td><td>'+m.hips+' '+hc+'</td><td>'+m.breast+'</td><td>'+(m.weight||'—')+'</td></tr>';}).join('');
  el.innerHTML='<table class="htbl"><thead><tr><th>Date</th><th>Waist</th><th>Hips</th><th>Breast</th><th>Weight (kg)</th></tr></thead><tbody>'+rows+'</tbody></table>';
}
function ed(data,key){if(!data.dailyData)data.dailyData={};if(!data.dailyData[key])data.dailyData[key]={};return data.dailyData[key];}
function tEx(i){
  const data=load();const key=tk();const day=ed(data,key);
  const w=DD[new Date().getDay()];
  if(!day.gym)day.gym=[];day.gym[i]=!day.gym[i];
  day.gymDone=w.exercises.every((_,j)=>day.gym[j]);
  if(day.gymDone)toast('🏋️ All exercises done! You CRUSHED IT!');
  chkC(day);
  save(data);rWorkout();rGym();
}
function tGym(i){tEx(i);}
function tDiet(i){
  const data=load();const key=tk();const day=ed(data,key);
  if(!day.diet)day.diet=[];day.diet[i]=!day.diet[i];
  day.dietDone=DT.every((_,j)=>day.diet[j]);
  if(day.dietDone)toast('🥗 Diet complete! Nourishing your body perfectly!');
  chkC(day);
  save(data);rDiet();
}
function chkC(day){
  const isRest=DD[new Date().getDay()].isRest;
  const completed=day.dietDone&&(isRest||day.gymDone);
  const justCompleted=completed&&!day.completed;
  day.completed=completed;
  if(justCompleted)setTimeout(()=>toast('🎉 Day COMPLETE! Streak grows! You are unstoppable!'),700);
}
function saveM(){
  const w=parseFloat(document.getElementById('iW').value);
  const h=parseFloat(document.getElementById('iH').value);
  const b=parseFloat(document.getElementById('iB').value);
  const weightValue=document.getElementById('iWt').value.trim();
  const wt=weightValue===''?null:Number(weightValue);
  if(![w,h,b].every(value=>Number.isFinite(value)&&value>0)||(wt!==null&&(!Number.isFinite(wt)||wt<=0))){toast('⚠️ Enter positive waist, hip and breast measurements. Weight must also be positive when provided.');return;}
  const data=load();if(!data.ms)data.ms=[];
  data.ms.push({date:tk(),day:dn(),waist:w,hips:h,breast:b,weight:wt});
  delete data.skD;save(data);
  document.getElementById('mModal').classList.remove('active');
  ['iW','iH','iB','iWt'].forEach(id=>document.getElementById(id).value='');
  rHist();rStats();toast('📏 Measurements saved! Keep going! 💪');
}
function skipM(){const data=load();data.skD=tk();save(data);document.getElementById('mModal').classList.remove('active');}
function togH(){const b=document.getElementById('hBody');const a=document.getElementById('hArr');b.classList.toggle('open');a.style.transform=b.classList.contains('open')?'rotate(180deg)':'';}
function openImg(f){document.getElementById('imgS').src=f;document.getElementById('imgM').classList.add('active');}
function closeImg(){document.getElementById('imgM').classList.remove('active');document.getElementById('imgS').src='';}
function toast(msg){const el=document.getElementById('toast');el.textContent=msg;el.classList.add('show');clearTimeout(toast._t);toast._t=setTimeout(()=>el.classList.remove('show'),3800);}
function chkMeasure(){
  if(!needsM())return;
  const ms=(load().ms)||[];const mn=ms.length+1;
  document.getElementById('mBadge').textContent='Month '+mn+' Check-In';
  document.getElementById('mSub').textContent=mn===1?'It has been 30 days since you started! Time for your first progress check-in. See how far you have come!':'Another 30 days of hard work! Record Month '+mn+' measurements to track your amazing transformation.';
  document.getElementById('mModal').classList.add('active');
}
let renderedDate=tk();
function init(){rStats();rQuote();rWeek();rWorkout();rGym();rDiet();rHist();setTimeout(chkMeasure,1800);}
function refreshDate(){
  rStats();
  const today=tk();if(today===renderedDate)return;
  renderedDate=today;
  rQuote();rWeek();rWorkout();rGym();rDiet();chkMeasure();
}
init();setInterval(refreshDate,60000);
</script></body></html>""")

content = ''.join(parts)
with open(dest, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done! Written", len(content), "chars to", dest)
