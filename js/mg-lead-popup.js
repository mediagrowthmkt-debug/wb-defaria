/* mg-lead-popup.js — DeFaria Construction
   Form PASSO A PASSO (1 pergunta por tela, LEI 21-10-26) usado em POPUP e INLINE (home + meio dos artigos).
   - CTAs de orcamento e o form inline -> form passo a passo (servico > prazo > mensagem > nome > telefone > e-mail+consentimento).
   - Anti-robo: honeypot + interacao humana real (isTrusted) + tempo minimo 3 s + Turnstile opcional (MG_TURNSTILE_SITEKEY).
   - GA4: conversao so depois do 2xx do webhook (evento mg:lead_submitted, ouvido pelo mg-analytics.js).
   - Botao de ligar (tel:) -> popup SIMPLES: so telefone + botao Call (cria lead e disca).
   - Origem por pagina via window.MG_LEAD_SOURCE ('website' | 'blog/artigo') -> GHL NOVOS LEADS. */
(function () {
  "use strict";
  var ENDPOINT = "https://mediagrowth-n8n.63kuy3.easypanel.host/webhook/defaria-site-lead";
  var SOURCE = window.MG_LEAD_SOURCE || "website";
  var CALL_SOURCE = (SOURCE === "blog/artigo") ? "ligacao blog/artigo" : "ligacao site";
  var CALL_TEL = (SOURCE === "blog/artigo") ? "+17815803815" : "+17815868838", CALL_DISPLAY = (SOURCE === "blog/artigo") ? "(781) 580-3815" : "(781) 586-8838";
  var LOGO = "/images/logo/logo-white.webp";
  var SERVICES = ["Bathroom Remodeling","Kitchen Remodeling","Home Additions","Remodeling","Decks & Patios","Commercial Projects","Painting","Finish Carpentry","Other / Not sure yet"];
  var uid = 0;

  var css = "" +
  ".mglp[hidden]{display:none}.mglp{position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;padding:18px;font-family:var(--font-primary,system-ui,sans-serif)}" +
  ".mglp__ov{position:absolute;inset:0;background:rgba(8,42,70,.6);backdrop-filter:blur(3px)}" +
  ".mglp__card{position:relative;background:#0d3f68;color:#fff;border-radius:16px;max-width:470px;width:100%;max-height:94vh;overflow:auto;box-shadow:0 24px 70px rgba(0,0,0,.55)}" +
  ".mglp__x{position:absolute;top:10px;right:14px;border:0;background:none;color:#cdd9e6;font-size:30px;line-height:1;cursor:pointer;z-index:2}.mglp__x:hover{color:#fff}" +
  ".mgf{color:#fff}.mgf__hd{display:flex;align-items:center;gap:14px;padding:22px 24px 6px}.mgf__hd img{height:42px;width:auto}.mgf__hd b{display:block;font-size:18px;color:#fff}.mgf__hd span{font-size:12.5px;color:#d6a85f;font-weight:600}" +
  ".mgf__steps{padding:14px 24px 0}.mgf__bar{height:5px;background:#0a3559;border-radius:99px;overflow:hidden}.mgf__bar i{display:block;height:100%;background:linear-gradient(90deg,#d6a85f,#e8c489);width:50%;transition:width .3s}" +
  ".mgf__lbls{display:flex;justify-content:space-between;margin-top:8px}.mgf__lbls span{font-size:11px;text-transform:uppercase;letter-spacing:.5px;color:#7fa6c7;font-weight:700}.mgf__lbls .on{color:#fff}.mgf__lbls .dn{color:#d6a85f}" +
  ".mgf__form{padding:16px 24px 24px}.mgf__form h3{margin:6px 0 14px;font-size:20px;color:#fff}" +
  ".mgf__form .fg{margin-bottom:12px}.mgf__form label{display:block;font-size:13px;font-weight:600;margin-bottom:6px;color:#dbe6f0}" +
  ".mgf__form input,.mgf__form select,.mgf__form textarea{width:100%;box-sizing:border-box;background:#082a46;border:1px solid #1c4d76;border-radius:8px;color:#fff;padding:12px 13px;font-size:16px;font-family:inherit}" +
  ".mgf__form input:focus,.mgf__form select:focus,.mgf__form textarea:focus{outline:none;border-color:#d6a85f}.mgf__form input::placeholder,.mgf__form textarea::placeholder{color:#8fb0cd}.mgf__form select option{color:#111}" +
  ".mgf__chips{display:flex;flex-wrap:wrap;gap:8px}.mgf__chip{border:1px solid #1c4d76;background:#082a46;color:#dbe6f0;border-radius:99px;padding:9px 15px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit}.mgf__chip:hover{border-color:#d6a85f}.mgf__chip.on{background:#d6a85f;color:#0d3f68;border-color:#d6a85f}" +
  ".mgf__hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}" +
  ".mgf__act{display:flex;gap:10px;margin-top:18px}.mgf__act .b{flex:1;border:0;border-radius:10px;padding:14px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit}.mgf__act .go{background:#d6a85f;color:#0d3f68}.mgf__act .go:hover{background:#e8c489}.mgf__act .bk{background:#0a3559;color:#dbe6f0}" +
  ".mgf__err{display:block;color:#ff9c9c;font-size:12px;margin-top:5px;min-height:1px}.mgf__ok{display:none;text-align:center;color:#d6a85f;font-weight:700;margin-top:14px;font-size:15px}" +
  ".mgf__done{text-align:center;padding:30px 12px 26px}.mgf__done-ic{width:74px;height:74px;margin:0 auto 18px;border-radius:50%;background:#d6a85f;color:#0d3f68;font-size:40px;line-height:74px;font-weight:700;box-shadow:0 0 0 9px rgba(214,168,95,.16);animation:mgfpop .35s ease}.mgf__done h3{margin:0 0 8px;font-size:23px;color:#fff}.mgf__done p{color:#c7d8e8;font-size:15px;line-height:1.55;margin:0 auto;max-width:330px}@keyframes mgfpop{0%{transform:scale(.6);opacity:0}100%{transform:scale(1);opacity:1}}" +
  ".mglp-inline{background:#0d3f68;color:#fff;border-radius:16px;overflow:hidden;margin:1.75rem 0;box-shadow:0 12px 40px rgba(8,42,70,.25)}" +
  ".mglp-fab{position:fixed;right:20px;bottom:20px;z-index:9998;width:60px;height:60px;border-radius:50%;background:#0d3f68;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 28px rgba(8,42,70,.4);cursor:pointer;border:0;transition:transform .15s,background .15s}.mglp-fab:hover{background:#d6a85f;color:#0d3f68;transform:scale(1.06)}.mglp-fab svg{width:28px;height:28px}" +
  ".mgf__consent{margin:6px 0 4px}.mgf .mgf__form label.mgf__ck{display:flex;gap:8px;align-items:flex-start;font-size:11.5px;line-height:1.45;color:#c7d8e8;margin:0 0 10px;font-weight:400;text-transform:none;letter-spacing:0}.mgf__ck input{margin-top:2px;flex:0 0 auto;width:auto}.mgf__ck b{color:#fff}.mgf .mgf__legal{font-size:11px;line-height:1.45;color:#9fbdd6;margin:6px 0 10px}.mgf__legal a{color:#d6a85f;text-decoration:underline}" +
  ".mgf__meta{display:flex;justify-content:space-between;margin-bottom:8px;font-size:11.5px;text-transform:uppercase;letter-spacing:.5px;color:#7fa6c7;font-weight:700}.mgf__meta span:first-child{color:#d6a85f}" +
  ".mgf__opts{display:grid;grid-template-columns:1fr 1fr;gap:10px}.mgf__opt{border:1px solid #1c4d76;background:#082a46;color:#fff;border-radius:10px;padding:13px 12px;min-height:52px;font-size:14.5px;font-weight:600;line-height:1.25;text-align:left;cursor:pointer;font-family:inherit;transition:border-color .15s,background .15s}.mgf__opt:hover,.mgf__opt:focus-visible{border-color:#d6a85f;outline:none}.mgf__opt.on{background:#d6a85f;color:#0d3f68;border-color:#d6a85f}.mgf__opt:last-child:nth-child(odd){grid-column:1/-1}" +
  ".mgf .mgf__sub{margin:-6px 0 14px;color:#9fbdd6;font-size:13.5px;line-height:1.45}.mgf__ts:empty{display:none}.mgf__ts{margin:6px 0}" +
  "@media(max-width:360px){.mgf__opts{grid-template-columns:1fr}}" +
  "@media(min-width:560px){.mglp__card,.mglp-inline{max-width:520px}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var TIMEFRAMES = ["ASAP","1-3 months","3-6 months","Just exploring"];
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var TS_KEY = window.MG_TURNSTILE_SITEKEY || "0x4AAAAAAFygINOi1L2bQzxT", tsLoad = null; // Cloudflare Turnstile (widget "DeFaria site - formulario de leads", conta MG)

  function emit(name, detail){ try{ document.dispatchEvent(new CustomEvent(name,{detail:detail||{}})); }catch(_){} }
  // Conversao SO depois do 2xx do webhook. mg-analytics.js (v1.4+) escuta mg:lead_submitted; sem ele, dispara direto no gtag.
  function conversion(detail){
    emit("mg:lead_submitted", detail);
    if(!window.MG_ANALYTICS && typeof window.gtag==="function"){
      try{ gtag("event","form_submit_free_estimate",{label:"free_estimate",page_url:location.href}); gtag("event","generate_lead",{lead_source:detail.source,service:detail.service||"",page_url:location.href}); }catch(_){}
    }
  }
  // Sinais humanos: so conta evento REAL (isTrusted) dentro do form + tempo minimo + sem webdriver.
  function humanGuard(host){
    var g = { n:0, t0:0 };
    ["pointerdown","touchstart","keydown","input"].forEach(function(ev){
      host.addEventListener(ev, function(e){ if(!e.isTrusted) return; g.n++; if(!g.t0) g.t0 = Date.now(); }, true);
    });
    g.ok = function(minEvents, minMs){ return !navigator.webdriver && g.n >= minEvents && g.t0 > 0 && (Date.now() - g.t0) >= minMs; };
    return g;
  }
  // Cloudflare Turnstile (Managed, so aparece se o Cloudflare desconfiar). Carrega so quando a pessoa comeca o form.
  // O token e validado no n8n (siteverify); token vale 1 uso, por isso reset depois de cada envio.
  function turnstile(box){
    var tok = "", wid = null, waiters = [];
    function load(){
      if(!tsLoad) tsLoad = new Promise(function(res, rej){ var s=document.createElement("script"); s.src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"; s.async=true; s.onload=res; s.onerror=function(){ tsLoad=null; rej(); }; document.head.appendChild(s); });
      return tsLoad;
    }
    function got(t){ tok = t || ""; if(tok) waiters.splice(0).forEach(function(f){ f(tok); }); }
    var api = {
      start:function(){
        if(!TS_KEY || !box || wid!==null) return;
        wid = -1;
        load().then(function(){ try{ wid = window.turnstile.render(box,{ sitekey:TS_KEY, appearance:"interaction-only", action:"lead", callback:got, "expired-callback":function(){ tok=""; }, "error-callback":function(){ tok=""; } }); }catch(_){ wid=null; } }, function(){ wid=null; });
      },
      token:function(ms){
        api.start();
        if(tok || !TS_KEY) return Promise.resolve(tok);
        return new Promise(function(res){ waiters.push(res); setTimeout(function(){ res(tok); }, ms||10000); });
      },
      reset:function(){ tok=""; if(wid!==null && wid!==-1 && window.turnstile){ try{ window.turnstile.reset(wid); }catch(_){} } }
    };
    return api;
  }
  function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/</g,"&lt;"); }
  function optButtons(name, list){ return '<div class="mgf__opts" data-pick="'+name+'">' + list.map(function(s){ return '<button type="button" class="mgf__opt" data-v="'+esc(s)+'">'+esc(s)+'</button>'; }).join("") + '</div>'; }

  // Form PASSO A PASSO (uma pergunta por tela) dentro de `host`. Retorna controller.
  function makeForm(host, opts){
    opts = opts || {};
    var STEPS = 6;
    host.classList.add("mgf");
    host.innerHTML =
      (opts.header ? '<div class="mgf__hd"><img src="'+LOGO+'" alt="DeFaria Construction"><div><b>'+(opts.title||"Get your free estimate")+'</b><span>DeFaria Construction · Reply within 24h</span></div></div>' : '') +
      '<div class="mgf__steps"><div class="mgf__meta"><span data-stepn>Step 1 of '+STEPS+'</span><span>Free estimate</span></div><div class="mgf__bar"><i></i></div></div>' +
      '<form class="mgf__form" novalidate data-form="free_estimate" data-mg-ajax="1">' +
        '<input type="text" name="company" class="mgf__hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<input type="hidden" name="service"><input type="hidden" name="timeframe">' +
        '<div class="stp" data-s="1"><h3>What can we help you with?</h3>' + optButtons("service", SERVICES) + '<span class="mgf__err" data-e="service"></span></div>' +
        '<div class="stp" data-s="2" hidden><h3>When do you want to start?</h3>' + optButtons("timeframe", TIMEFRAMES) + '<span class="mgf__err" data-e="timeframe"></span>' +
          '<div class="mgf__act"><button type="button" class="b bk" data-back>&larr; Back</button></div></div>' +
        '<div class="stp" data-s="3" hidden><h3>Tell us about your project</h3><p class="mgf__sub">Optional: scope, rooms, address area, anything that helps.</p>' +
          '<div class="fg"><textarea name="message" rows="3" placeholder="Ex.: full kitchen remodel, new cabinets and island"></textarea></div>' +
          '<div class="mgf__act"><button type="button" class="b bk" data-back>&larr; Back</button><button type="button" class="b go" data-next>Continue &rarr;</button></div></div>' +
        '<div class="stp" data-s="4" hidden><h3>What is your name?</h3>' +
          '<div class="fg"><input name="name" placeholder="John Smith" autocomplete="name" enterkeyhint="next"><span class="mgf__err" data-e="name"></span></div>' +
          '<div class="mgf__act"><button type="button" class="b bk" data-back>&larr; Back</button><button type="button" class="b go" data-next>Continue &rarr;</button></div></div>' +
        '<div class="stp" data-s="5" hidden><h3>Best phone number?</h3><p class="mgf__sub">Optional. Only used to talk about your estimate.</p>' +
          '<div class="fg"><input name="phone" type="tel" inputmode="tel" placeholder="(617) 000-0000" autocomplete="tel" enterkeyhint="next"><span class="mgf__err" data-e="phone"></span></div>' +
          '<div class="mgf__act"><button type="button" class="b bk" data-back>&larr; Back</button><button type="button" class="b go" data-next>Continue &rarr;</button></div></div>' +
        '<div class="stp" data-s="6" hidden><h3>Where should we send your estimate?</h3>' +
          '<div class="fg"><input name="email" type="email" inputmode="email" placeholder="john@example.com" autocomplete="email" enterkeyhint="send"><span class="mgf__err" data-e="email"></span></div>' +
          (opts.optin ? '<div class="mgf__consent">' +'<label class="mgf__ck"><input type="checkbox" name="consent_transactional" value="yes"><span>By checking this optional box, I consent to receive transactional messages related to my account, orders, or services I have requested from <b>DeFaria Carpentry Inc. (DBA DeFaria Construction)</b>. These messages may include reminders, order confirmations, and account notifications among others. I understand my phone number is optional and this consent is not required to request an estimate or purchase services. Message frequency may vary. Message &amp; data rates may apply. Reply HELP for help or STOP to opt out.</span></label>' +'<label class="mgf__ck"><input type="checkbox" name="consent_marketing" value="yes"><span>By checking this optional box, I consent to receive marketing and promotional messages, including special offers, discounts, and new product updates, among others, from <b>DeFaria Carpentry Inc. (DBA DeFaria Construction)</b>. I understand my phone number is optional and this consent is not required to request an estimate or purchase services. Message frequency may vary. Message &amp; data rates may apply. Reply HELP for help or STOP to opt out.</span></label>' +'<p class="mgf__legal">SMS consent is optional. Mobile opt-in data and SMS consent are not shared with third parties or affiliates for marketing or promotional purposes. By submitting, you agree to our <a href="/pages/privacy-policy/" target="_blank" rel="noopener">Privacy Policy</a> and <a href="/pages/terms/" target="_blank" rel="noopener">Terms &amp; Conditions</a>.</p></div>' : '<p class="mgf__legal">By submitting, you agree to our <a href="/pages/privacy-policy/" target="_blank" rel="noopener">Privacy Policy</a> and <a href="/pages/terms/" target="_blank" rel="noopener">Terms &amp; Conditions</a>.</p>') +
          '<div class="mgf__act"><button type="button" class="b bk" data-back>&larr; Back</button><button type="submit" class="b go">Get My Free Estimate</button></div></div>' +
        '<div class="mgf__ts"></div>' +
        '<div class="stp mgf__done" data-done hidden><div class="mgf__done-ic">&#10003;</div><h3>Request received!</h3><p>Thank you. Our team will get back to you within 24 hours.</p></div>' +
      '</form>';
    var form = host.querySelector("form"), step = 1, lock = false, sending = false, started = false;
    var human = humanGuard(host), ts = turnstile(host.querySelector(".mgf__ts"));
    function v(n){ var e=form.querySelector('[name="'+n+'"]'); return (e&&e.value||"").trim(); }
    function err(n,m){ var e=form.querySelector('[data-e="'+n+'"]'); if(e)e.textContent=m||""; }
    function clearErr(){ host.querySelectorAll(".mgf__err").forEach(function(e){ e.textContent=""; }); }
    function render(focus){
      host.querySelectorAll(".stp[data-s]").forEach(function(s){ s.hidden = +s.getAttribute("data-s")!==step; });
      host.querySelector(".mgf__bar i").style.width = Math.round(step/STEPS*100)+"%";
      host.querySelector("[data-stepn]").textContent = "Step "+step+" of "+STEPS;
      if(!focus) return;
      var cur = host.querySelector('.stp[data-s="'+step+'"]');
      var f = cur && (cur.querySelector('input:not([type="checkbox"]),textarea') || cur.querySelector(".mgf__opt.on") || cur.querySelector(".mgf__opt"));
      if(f){ try{ f.focus({preventScroll:true}); }catch(_){ f.focus(); } }
    }
    function check(s){
      if(s===1 && !v("service")){ err("service","Please choose a service."); return false; }
      if(s===2 && !v("timeframe")){ err("timeframe","Please choose one option."); return false; }
      if(s===4 && v("name").length<2){ err("name","Please enter your name."); return false; }
      if(s===5){ var d=v("phone").replace(/\D/g,""); if(d && (d.length<10 || d.length>11)){ err("phone","Please enter a valid phone number or leave it blank."); return false; } }
      if(s===6 && !EMAIL_RE.test(v("email"))){ err("email","Please enter a valid email."); return false; }
      return true;
    }
    function next(){ clearErr(); if(!check(step)) return; if(step<STEPS){ step++; render(true); } else submit(); }
    function back(){ clearErr(); if(step>1){ step--; render(true); } }
    function showDone(){ host.querySelector(".mgf__steps").style.display="none"; host.querySelectorAll(".stp").forEach(function(s){ s.hidden = !s.hasAttribute("data-done"); }); }
    function resetSteps(){ form.reset(); host.querySelectorAll(".mgf__opt.on").forEach(function(x){ x.classList.remove("on"); }); clearErr(); host.querySelector(".mgf__steps").style.display=""; step=1; render(false); }
    function markStart(){ ts.start(); if(started) return; started=true; emit("mg:lead_start",{form:"free_estimate",source:SOURCE}); }
    host.querySelectorAll("[data-pick]").forEach(function(box){
      box.addEventListener("click", function(e){
        var b = e.target.closest(".mgf__opt"); if(!b || lock) return;
        box.querySelectorAll(".mgf__opt").forEach(function(x){ x.classList.remove("on"); }); b.classList.add("on");
        form.querySelector('[name="'+box.getAttribute("data-pick")+'"]').value = b.getAttribute("data-v");
        markStart(); lock = true; setTimeout(function(){ lock=false; next(); }, 180);
      });
    });
    host.addEventListener("click", function(e){
      if(e.target.closest("[data-next]")){ e.preventDefault(); markStart(); next(); }
      else if(e.target.closest("[data-back]")){ e.preventDefault(); back(); }
    });
    form.addEventListener("keydown", function(e){
      if(e.key!=="Enter" || e.isComposing) return;
      var t = e.target; if(t.tagName==="TEXTAREA" || t.tagName==="BUTTON" || t.tagName==="A") return;
      e.preventDefault(); markStart(); next();
    });
    form.addEventListener("submit", function(e){ e.preventDefault(); if(step<STEPS) next(); else { clearErr(); if(check(STEPS)) submit(); } });
    async function submit(){
      if(sending) return;
      // Anti-robo: honeypot, sem interacao humana real ou rapido demais (<3 s) = descarta em silencio (nada enviado, nada contado).
      if(v("company") || !human.ok(3, 3000)){ showDone(); return; }
      sending = true;
      var btn=form.querySelector('button[type="submit"]'), o=btn.innerHTML; btn.disabled=true; btn.innerHTML="Sending…";
      var tok = TS_KEY ? await ts.token(12000) : "";
      if(TS_KEY && !tok){ btn.disabled=false; btn.innerHTML=o; sending=false; err("email","Security check did not finish. Please try again or call "+CALL_DISPLAY+"."); return; }
      var tf=v("timeframe"), ck=function(n){var e=form.querySelector('[name="'+n+'"]');return e?(e.checked?"yes":"no"):null;}, msg=(tf?("["+tf+"] "):"")+v("message")+"\n\nPage: "+location.href+(ck("consent_transactional")!==null?("\nSMS consent: transactional="+ck("consent_transactional")+", marketing="+ck("consent_marketing")):"");
      var payload = {name:v("name"),email:v("email"),phone:v("phone"),service:v("service"),source:SOURCE,message:msg};
      if(TS_KEY) payload.cf_turnstile_token = tok;
      try{ var r=await fetch(ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(payload)});
        ts.reset();
        if(!r.ok) throw 0;
        conversion({form:"free_estimate",source:SOURCE,service:payload.service});
        showDone(); btn.disabled=false; btn.innerHTML=o;
        if(opts.onDone) opts.onDone(payload.phone); if(opts.reset!==false) setTimeout(resetSteps,7000);
      }catch(_){ btn.disabled=false; btn.innerHTML=o; err("email","Something went wrong. Please call "+CALL_DISPLAY+"."); }
      sending = false;
    }
    render(false);
    return { focusFirst:function(){ var f=host.querySelector('.stp[data-s="1"] .mgf__opt'); if(f) try{ f.focus({preventScroll:true}); }catch(_){} }, reset:resetSteps };
  }

  // Painel SIMPLES de ligacao: so telefone + botao de ligar.
  function makeCall(host){
    host.classList.add("mgf");
    host.innerHTML =
      '<div class="mgf__hd"><img src="'+LOGO+'" alt="DeFaria Construction"><div><b>Request a call</b><span>DeFaria Construction · Reply within 24h</span></div></div>' +
      '<form class="mgf__form" novalidate data-form="call_request" data-mg-ajax="1">' +
        '<input type="text" name="company" class="mgf__hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<h3>We will call you right back</h3>' +
        '<p style="color:#c7d8e8;font-size:14px;margin:0 0 14px">Enter your phone and tap Call.</p>' +
        '<div class="fg"><label>Phone *</label><input name="phone" type="tel" placeholder="(617) 000-0000" autocomplete="tel"><span class="mgf__err" data-e="phone"></span></div>' +
        '<p class="mgf__legal">We will only call you about your request. We do not send text messages without your separate consent. See our <a href="/pages/privacy-policy/" target="_blank" rel="noopener">Privacy Policy</a> and <a href="/pages/terms/" target="_blank" rel="noopener">Terms &amp; Conditions</a>.</p>' +
        '<div class="mgf__ts"></div>' +
        '<div class="mgf__act"><button type="submit" class="b go">Call '+CALL_DISPLAY+'</button></div>' +
        '<p style="font-size:12px;color:#9fbdd6;text-align:center;margin-top:10px">Prefer to dial? <a href="tel:'+CALL_TEL+'" style="color:#d6a85f">'+CALL_DISPLAY+'</a></p>' +
        '<div class="stp mgf__done" data-done hidden><div class="mgf__done-ic">&#10003;</div><h3>Connecting your call…</h3><p>Thank you! If we miss you, our team will get back to you within 24 hours.</p></div>' +
      '</form>';
    var form=host.querySelector("form"), human=humanGuard(host), ts=turnstile(host.querySelector(".mgf__ts"));
    form.addEventListener("focusin", function(){ ts.start(); });
    function v(n){ var e=form.querySelector('[name="'+n+'"]'); return (e&&e.value||"").trim(); }
    form.addEventListener("submit", async function(e){
      e.preventDefault();
      var er=form.querySelector('[data-e="phone"]');
      if(!v("phone")){ if(er)er.textContent="Please enter your phone."; return; } if(er)er.textContent="";
      var btn=form.querySelector('button[type="submit"]'), o=btn.innerHTML; btn.disabled=true; btn.innerHTML="Connecting…";
      // Anti-robo: honeypot ou sem interacao humana real = nao cria lead (so disca).
      if(!v("company") && human.ok(2, 1500)) try{
        var cp={name:"Call request",email:"",phone:v("phone"),service:"",source:CALL_SOURCE,message:"Call request (clicked to call)\n\nPage: "+location.href};
        if(TS_KEY) cp.cf_turnstile_token = await ts.token(6000);
        await fetch(ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(cp)}); ts.reset();
      }catch(_){}
      form.querySelectorAll(":scope > *:not([data-done])").forEach(function(x){ x.style.display="none"; });
      form.querySelector("[data-done]").hidden=false; btn.disabled=false; btn.innerHTML=o;
      window.location.href="tel:"+CALL_TEL;
    });
    return { focusFirst:function(){ var f=host.querySelector('[name="phone"]'); if(f)f.focus(); },
      reset:function(){ form.reset(); form.querySelectorAll(":scope > *").forEach(function(x){ x.style.display = x.hasAttribute("data-done")?"none":""; }); form.querySelector("[data-done]").hidden=true; } };
  }

  // ---- POPUP ----
  var modal = document.createElement("div"); modal.className="mglp"; modal.hidden=true; modal.setAttribute("role","dialog"); modal.setAttribute("aria-modal","true");
  modal.innerHTML = '<div class="mglp__ov" data-x></div><div class="mglp__card"><button class="mglp__x" data-x aria-label="Close">&times;</button><div data-formhost></div><div data-callhost hidden></div></div>';
  document.body.appendChild(modal);
  var formCtl = makeForm(modal.querySelector("[data-formhost]"), { header:true });
  var callCtl = makeCall(modal.querySelector("[data-callhost]"));
  function openPopup(isCall){
    modal.querySelector("[data-formhost]").hidden = !!isCall;
    modal.querySelector("[data-callhost]").hidden = !isCall;
    (isCall?callCtl:formCtl).reset();
    modal.hidden=false; document.body.style.overflow="hidden";
    setTimeout(function(){ (isCall?callCtl:formCtl).focusFirst(); }, 60);
  }
  function closePopup(){ modal.hidden=true; document.body.style.overflow=""; }
  modal.querySelectorAll("[data-x]").forEach(function(x){ x.onclick=closePopup; });
  document.addEventListener("keydown", function(e){ if(e.key==="Escape"&&!modal.hidden) closePopup(); });

  // ---- INLINE (home + meio dos artigos) ----
  document.querySelectorAll("[data-mglp-inline]").forEach(function(box){
    var card=document.createElement("div"); card.className="mglp-inline"; box.appendChild(card);
    makeForm(card, { header:true, title:(box.getAttribute("data-title")||"Get your free estimate"), reset:true, optin:box.hasAttribute("data-mglp-optin") });
  });

  // ---- WIRING dos CTAs ----
  function isEstimateCta(a){ var t=(a.textContent||"").toLowerCase(), h=a.getAttribute("href")||"";
    if(a.hasAttribute("data-lead-open"))return true;
    return a.classList.contains("btn") && (h==="#contact"||h==="#estimate"||h==="#estimateForm"||/estimate|quote|free|get started|book|consult/.test(t)); }
  document.querySelectorAll('a[href^="tel:"]').forEach(function(a){ a.addEventListener("click", function(e){ e.preventDefault(); openPopup(true); }); });
  document.querySelectorAll("a").forEach(function(a){ if(isEstimateCta(a)) a.addEventListener("click", function(e){ e.preventDefault(); openPopup(false); }); });

  // ---- Troca o float de WhatsApp por um FAB de LIGACAO (abre o popup de ligacao) ----
  document.querySelectorAll('.floating-whatsapp, a[href*="wa.me"], a[href*="api.whatsapp"]').forEach(function(e){ e.remove(); });
  var fab = document.createElement("button");
  fab.className = "mglp-fab"; fab.type = "button"; fab.setAttribute("aria-label", "Call " + CALL_DISPLAY);
  fab.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.5 11.5 0 003.61.58 1 1 0 011 1V21a1 1 0 01-1 1A17 17 0 013 5a1 1 0 011-1h3.5a1 1 0 011 1c0 1.26.2 2.49.58 3.61a1 1 0 01-.25 1.01l-2.21 2.17z"/></svg>';
  fab.addEventListener("click", function(){ openPopup(true); });
  document.body.appendChild(fab);
})();
