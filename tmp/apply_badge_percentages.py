with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

pos_start = text.find("const FAKE_PLAYERS=")
pos_end = text.find("function readFriends()")
assert pos_start != -1 and pos_end != -1, "Positions not found"

new_content = """const FAKE_PLAYERS=[
  // 10% Verified Bot Accounts (2 accounts)
  ['ProGamer_200K','🎮','Rocket League','200K','verified','Verified Star Player'],
  ['StarPlayer_200K','⭐','HMAILZ Obby 3D','200K','verified','Verified Top Creator'],

  // 30% Game Maker Badge Accounts (6 accounts)
  ['ChefOmar','👨‍🍳','Work at a Pizza Place','1.7K','maker','Game Maker · Pizza Place Creator'],
  ['TurboTom','🚗','Car Simulator 3D','2.4K','maker','Game Maker · Vehicle Engineer'],
  ['Pixel_Princess','👑','Hide & Seek 3D','1.4K','maker','Game Maker · Map Designer'],
  ['DarkKnight_01','⚔️','Survival Warrior','2.0K','maker','Game Maker · Combat Lead'],
  ['BrainrotLord','🧠','Escape Tsunami for Brainrot','1.5K','maker','Game Maker · Obby Builder'],
  ['PizzaKing_2026','🍕','Work at a Pizza Place','1.2K','maker','Game Maker · Level Designer'],

  // 40% HMAILZ Worker Badge Accounts (8 accounts)
  ['MegaNinja','🥷','HMAILZ Obby 3D','2.2K','worker','HMAILZ Staff · Senior Builder'],
  ['SpeedyMia','⚡','Speed Run','2.1K','worker','HMAILZ Staff · Head Moderator'],
  ['ShadowWolf','🐺','99 Nights in the Forest','1.3K','worker','HMAILZ Staff · Safety & Anti-Cheat'],
  ['HMAILZ_Dev','💻','City Explorer','2.8K','worker','HMAILZ Staff · Core Engineer'],
  ['HMAILZ_Mod','🛡️','Survival Warrior','1.9K','worker','HMAILZ Staff · Lead Admin'],
  ['CoolKid_Jay','😎','Football Challenge 3D','1.9K','worker','HMAILZ Staff · Community Events'],
  ['ZombieHunter77','🧟','Zombie Survival','1.6K','worker','HMAILZ Staff · QA Tester'],
  ['LunaStar','🌙','Pet Simulator','1.2K','worker','HMAILZ Staff · Community Support'],

  // 20% Regular Community Accounts (4 accounts)
  ['ProGamer_Alex','🕹️','Rocket League','1.8K','none','Active Community Member'],
  ['SkyHighSam','🏀','Basketball Challenge','1.4K','none','Competitive Player'],
  ['TsunamiSurfer','🌊','Escape Tsunami for Brainrot','1.1K','none','Speedrunner'],
  ['EpicEmma','💎','Gem Hunt','1.3K','none','Explorer']
].map((p,i)=>({
  username:p[0],
  emoji:p[1],
  kind:'fake',
  online:i%4!==3,
  game:p[2],
  followers:p[3],
  badge:p[4],
  roleTitle:p[5],
  verified:p[4]==='verified',
  description:(i%4!==3?'🟢 Online · ':'⚫ Offline · ')+p[5]+' · '+p[3]+' Followers'
}));

FAKE_PLAYERS.unshift({
  username:'HMAILZ',
  emoji:'🎮',
  kind:'fake',
  online:true,
  game:'',
  followers:'300K',
  badge:'worker',
  roleTitle:'Official Account · Platform Founder',
  verified:true,
  description:'Official HMAILZ account · 300K Followers'
});

const CHATGPT_FRIEND={
  username:'ChatGPT',
  emoji:'🤖',
  description:'HMAILZ AI Assistant · 259K Followers',
  kind:'ai',
  followers:'259K',
  badge:'verified',
  roleTitle:'AI Game Assistant',
  verified:true
};

const VERIFIED_BADGE_SVG = '<span class="badgeTag verifiedTag" title="Verified Player" style="display:inline-flex;align-items:center;vertical-align:middle;margin-left:4px;flex-shrink:0"><svg viewBox="0 0 24 24" width="16" height="16" fill="#1d9bf0" aria-label="Verified"><path d="M22.5 12.5c0-1.58-.875-2.95-2.148-3.6.154-.435.238-.905.238-1.4 0-2.21-1.79-4-4-4-.495 0-.965.084-1.4.238C14.55 2.475 13.18 1.6 11.6 1.6c-1.58 0-2.95.875-3.6 2.148-.435-.154-.905-.238-1.4-.238-2.21 0-4 1.79-4 4 0 .495.084.965.238 1.4C1.575 9.55.7 10.92.7 12.5c0 1.58.875 2.95 2.148 3.6-.154.435-.238.905-.238 1.4 0 2.21 1.79 4 4 4 .495 0 .965-.084 1.4-.238.65 1.273 2.02 2.148 3.6 2.148 1.58 0 2.95-.875 3.6-2.148.435.154.905.238 1.4.238 2.21 0 4-1.79 4-4 0-.495-.084-.965-.238-1.4 1.273-.65 2.148-2.02 2.148-3.6zm-12.72 4.14-3.54-3.54 1.41-1.41 2.13 2.12 5.66-5.66 1.41 1.41-7.07 7.08z"/></svg></span>';

const MAKER_BADGE_SVG = '<span class="badgeTag makerTag" title="Game Maker" style="display:inline-flex;align-items:center;gap:3px;font-size:10px;font-weight:900;padding:2px 7px;border-radius:999px;background:#78350f;color:#fde68a;border:1px solid #d97706;margin-left:5px;vertical-align:middle;flex-shrink:0"><svg viewBox="0 0 24 24" width="11" height="11" fill="#fde68a"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg> MAKER</span>';

const WORKER_BADGE_SVG = '<span class="badgeTag workerTag" title="HMAILZ Worker / Staff" style="display:inline-flex;align-items:center;gap:3px;font-size:10px;font-weight:900;padding:2px 7px;border-radius:999px;background:#064e3b;color:#a7f3d0;border:1px solid #059669;margin-left:5px;vertical-align:middle;flex-shrink:0"><svg viewBox="0 0 24 24" width="11" height="11" fill="#34d399"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg> WORKER</span>';

function getPlayerBadgesHTML(p){
  if(!p) return '';
  const u = String(p.username || '').toLowerCase();
  if(u === 'hmailz') return VERIFIED_BADGE_SVG + ' ' + WORKER_BADGE_SVG;
  if(u === 'chatgpt') return VERIFIED_BADGE_SVG;
  if(p.badge === 'worker') return WORKER_BADGE_SVG;
  if(p.badge === 'maker') return MAKER_BADGE_SVG;
  if(p.badge === 'verified' || p.verified === true) return VERIFIED_BADGE_SVG;
  return '';
}

function isProfileVerified(p){
  if(!p) return false;
  return getPlayerBadgesHTML(p).length > 0;
}
"""

text = text[:pos_start] + new_content + text[pos_end:]

# Update ppName to use getPlayerBadgesHTML
old_pp_name = "pan.querySelector('.ppName').innerHTML=p.username+(isProfileVerified(p)?VERIFIED_BADGE_SVG:'');"
new_pp_name = "pan.querySelector('.ppName').innerHTML=p.username+' '+getPlayerBadgesHTML(p);"
if old_pp_name in text:
    text = text.replace(old_pp_name, new_pp_name)

# Update friendCard to use getPlayerBadgesHTML
old_fc = "if(isProfileVerified(profile)){const b=document.createElement('span');b.innerHTML=VERIFIED_BADGE_SVG;name.appendChild(b);}"
new_fc = "const badges=getPlayerBadgesHTML(profile);if(badges){const b=document.createElement('span');b.innerHTML=badges;name.appendChild(b);}"
if old_fc in text:
    text = text.replace(old_fc, new_fc)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated index.html: 10% verified, 30% game maker, 40% worker badges!")
