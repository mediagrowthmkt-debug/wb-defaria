/* mg-lead-popup.js — DeFaria Construction
   Form de 2 passos (limpo) usado em POPUP e INLINE (home + meio dos artigos).
   - CTAs de orcamento e o form inline -> form 2 passos.
   - Botao de ligar (tel:) -> popup SIMPLES: so telefone + botao Call (cria lead e disca).
   - Origem por pagina via window.MG_LEAD_SOURCE ('website' | 'blog/artigo') -> GHL NOVOS LEADS. */
(function () {
  "use strict";
  var ENDPOINT = "https://mediagrowth-n8n.63kuy3.easypanel.host/webhook/defaria-site-lead";
  var SOURCE = window.MG_LEAD_SOURCE || "website";
  var CALL_SOURCE = (SOURCE === "blog/artigo") ? "ligacao blog/artigo" : "ligacao site";
  var CALL_TEL = "+16178932221", CALL_DISPLAY = "(617) 893-2221";
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
  ".mgf__form input,.mgf__form select,.mgf__form textarea{width:100%;box-sizing:border-box;background:#082a46;border:1px solid #1c4d76;border-radius:8px;color:#fff;padding:12px 13px;font-size:15px;font-family:inherit}" +
  ".mgf__form input:focus,.mgf__form select:focus,.mgf__form textarea:focus{outline:none;border-color:#d6a85f}.mgf__form input::placeholder,.mgf__form textarea::placeholder{color:#8fb0cd}.mgf__form select option{color:#111}" +
  ".mgf__chips{display:flex;flex-wrap:wrap;gap:8px}.mgf__chip{border:1px solid #1c4d76;background:#082a46;color:#dbe6f0;border-radius:99px;padding:9px 15px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit}.mgf__chip:hover{border-color:#d6a85f}.mgf__chip.on{background:#d6a85f;color:#0d3f68;border-color:#d6a85f}" +
  ".mgf__hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}" +
  ".mgf__act{display:flex;gap:10px;margin-top:18px}.mgf__act .b{flex:1;border:0;border-radius:10px;padding:14px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit}.mgf__act .go{background:#d6a85f;color:#0d3f68}.mgf__act .go:hover{background:#e8c489}.mgf__act .bk{background:#0a3559;color:#dbe6f0}" +
  ".mgf__err{display:block;color:#ff9c9c;font-size:12px;margin-top:5px;min-height:1px}.mgf__ok{display:none;text-align:center;color:#d6a85f;font-weight:700;margin-top:14px;font-size:15px}" +
  ".mgf__done{text-align:center;padding:30px 12px 26px}.mgf__done-ic{width:74px;height:74px;margin:0 auto 18px;border-radius:50%;background:#d6a85f;color:#0d3f68;font-size:40px;line-height:74px;font-weight:700;box-shadow:0 0 0 9px rgba(214,168,95,.16);animation:mgfpop .35s ease}.mgf__done h3{margin:0 0 8px;font-size:23px;color:#fff}.mgf__done p{color:#c7d8e8;font-size:15px;line-height:1.55;margin:0 auto;max-width:330px}@keyframes mgfpop{0%{transform:scale(.6);opacity:0}100%{transform:scale(1);opacity:1}}" +
  ".mglp-inline{background:#0d3f68;color:#fff;border-radius:16px;overflow:hidden;margin:1.75rem 0;box-shadow:0 12px 40px rgba(8,42,70,.25)}" +
  ".mglp-fab{position:fixed;right:20px;bottom:20px;z-index:9998;width:60px;height:60px;border-radius:50%;background:#0d3f68;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 28px rgba(8,42,70,.4);cursor:pointer;border:0;transition:transform .15s,background .15s}.mglp-fab:hover{background:#d6a85f;color:#0d3f68;transform:scale(1.06)}.mglp-fab svg{width:28px;height:28px}" +
  "@media(min-width:560px){.mglp__card,.mglp-inline{max-width:520px}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  function optsHTML(){ return '<option value="">Select a service</option>' + SERVICES.map(function(s){return '<option>'+s+'</option>';}).join(""); }

  // Form de 2 passos dentro de `host`. Retorna controller.
  function makeForm(host, opts){
    opts = opts || {};
    host.classList.add("mgf");
    host.innerHTML =
      (opts.header ? '<div class="mgf__hd"><img src="'+LOGO+'" alt="DeFaria Construction"><div><b>'+(opts.title||"Get your free estimate")+'</b><span>DeFaria Construction · Reply within 24h</span></div></div>' : '') +
      '<div class="mgf__steps"><div class="mgf__bar"><i></i></div><div class="mgf__lbls"><span class="on" data-l="1">Project</span><span data-l="2">Details</span></div></div>' +
      '<form class="mgf__form" novalidate>' +
        '<input type="text" name="company" class="mgf__hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<div class="stp" data-s="1"><h3>What can we help you with?</h3>' +
          '<div class="fg"><label>Service</label><select name="service">'+optsHTML()+'</select></div>' +
          '<div class="fg"><label>Tell us about your project</label><textarea name="message" rows="2" placeholder="Optional: scope, rooms, timing..."></textarea></div>' +
          '<label>When do you want to start?</label>' +
          '<div class="mgf__chips" data-chips><button type="button" class="mgf__chip" data-v="ASAP">ASAP</button><button type="button" class="mgf__chip" data-v="1-3 months">1-3 months</button><button type="button" class="mgf__chip" data-v="3-6 months">3-6 months</button><button type="button" class="mgf__chip" data-v="Just exploring">Just exploring</button></div>' +
          '<input type="hidden" name="timeframe">' +
          '<div class="mgf__act"><button type="button" class="b go" data-next>Continue &rarr;</button></div></div>' +
        '<div class="stp" data-s="2" hidden><h3>Where can we reach you?</h3>' +
          '<div class="fg"><label>Full Name *</label><input name="name" placeholder="John Smith" autocomplete="name"><span class="mgf__err" data-e="name"></span></div>' +
          '<div class="fg"><label>Phone *</label><input name="phone" type="tel" placeholder="(617) 000-0000" autocomplete="tel"><span class="mgf__err" data-e="phone"></span></div>' +
          '<div class="fg"><label>Email *</label><input name="email" type="email" placeholder="john@example.com" autocomplete="email"><span class="mgf__err" data-e="email"></span></div>' +
          '<div class="mgf__act"><button type="button" class="b bk" data-back>&larr; Back</button><button type="submit" class="b go">Get My Free Estimate</button></div></div>' +
          '<div class="stp mgf__done" data-done hidden><div class="mgf__done-ic">&#10003;</div><h3>Request received!</h3><p>Thank you. Our team will get back to you within 24 hours.</p></div>' +
      '</form>';
    var form = host.querySelector("form"), step = 1;
    function showDone(){ host.querySelector(".mgf__steps").style.display="none"; host.querySelectorAll(".stp").forEach(function(s){ s.hidden = !s.hasAttribute("data-done"); }); }
    function resetSteps(){ host.querySelector(".mgf__steps").style.display=""; step=1; render(); }
    function v(n){ var e=form.querySelector('[name="'+n+'"]'); return (e&&e.value||"").trim(); }
    function err(n,m){ var e=form.querySelector('[data-e="'+n+'"]'); if(e)e.textContent=m||""; }
    function render(){
      host.querySelectorAll(".stp").forEach(function(s){ s.hidden = +s.getAttribute("data-s")!==step; });
      host.querySelector(".mgf__bar i").style.width = (step*50)+"%";
      host.querySelectorAll(".mgf__lbls span").forEach(function(sp){ var i=+sp.getAttribute("data-l"); sp.className = i===step?"on":(i<step?"dn":""); });
    }
    host.querySelector("[data-next]").onclick=function(){ step=2; render(); };
    host.querySelector("[data-back]").onclick=function(){ step=1; render(); };
    var chips=host.querySelector("[data-chips]");
    chips.onclick=function(e){ var c=e.target.closest(".mgf__chip"); if(!c)return; chips.querySelectorAll(".mgf__chip").forEach(function(x){x.classList.remove("on");}); c.classList.add("on"); form.querySelector('[name="timeframe"]').value=c.getAttribute("data-v"); };
    form.addEventListener("submit", async function(e){
      e.preventDefault(); if(v("company"))return;
      err("name");err("phone");err("email"); var ok=true;
      if(!v("name")){err("name","Please enter your name.");ok=false;}
      if(!v("phone")){err("phone","Please enter your phone.");ok=false;}
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v("email"))){err("email","Please enter a valid email.");ok=false;}
      if(!ok) return;
      var btn=form.querySelector('button[type="submit"]'), o=btn.innerHTML; btn.disabled=true; btn.innerHTML="Sending…";
      var tf=v("timeframe"), msg=(tf?("["+tf+"] "):"")+v("message")+"\n\nPage: "+location.href;
      try{ var r=await fetch(ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:v("name"),email:v("email"),phone:v("phone"),service:v("service"),source:SOURCE,message:msg})});
        if(!r.ok)throw 0; showDone(); btn.disabled=false; btn.innerHTML=o;
        if(opts.onDone) opts.onDone(v("phone")); if(opts.reset!==false) setTimeout(function(){ form.reset(); resetSteps(); },7000);
      }catch(_){ btn.disabled=false; btn.innerHTML=o; err("email","Something went wrong. Please call "+CALL_DISPLAY+"."); }
    });
    render();
    return { focusFirst:function(){ var f=host.querySelector('[name="service"]'); if(f)f.focus(); }, reset:function(){ form.reset(); resetSteps(); } };
  }

  // Painel SIMPLES de ligacao: so telefone + botao de ligar.
  function makeCall(host){
    host.classList.add("mgf");
    host.innerHTML =
      '<div class="mgf__hd"><img src="'+LOGO+'" alt="DeFaria Construction"><div><b>Request a call</b><span>DeFaria Construction · Reply within 24h</span></div></div>' +
      '<form class="mgf__form" novalidate>' +
        '<input type="text" name="company" class="mgf__hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<h3>We will call you right back</h3>' +
        '<p style="color:#c7d8e8;font-size:14px;margin:0 0 14px">Enter your phone and tap Call.</p>' +
        '<div class="fg"><label>Phone *</label><input name="phone" type="tel" placeholder="(617) 000-0000" autocomplete="tel"><span class="mgf__err" data-e="phone"></span></div>' +
        '<div class="mgf__act"><button type="submit" class="b go">Call '+CALL_DISPLAY+'</button></div>' +
        '<p style="font-size:12px;color:#9fbdd6;text-align:center;margin-top:10px">Prefer to dial? <a href="tel:'+CALL_TEL+'" style="color:#d6a85f">'+CALL_DISPLAY+'</a></p>' +
        '<div class="stp mgf__done" data-done hidden><div class="mgf__done-ic">&#10003;</div><h3>Connecting your call…</h3><p>Thank you! If we miss you, our team will get back to you within 24 hours.</p></div>' +
      '</form>';
    var form=host.querySelector("form");
    function v(n){ var e=form.querySelector('[name="'+n+'"]'); return (e&&e.value||"").trim(); }
    form.addEventListener("submit", async function(e){
      e.preventDefault(); if(v("company"))return;
      var er=form.querySelector('[data-e="phone"]');
      if(!v("phone")){ if(er)er.textContent="Please enter your phone."; return; } if(er)er.textContent="";
      var btn=form.querySelector('button[type="submit"]'), o=btn.innerHTML; btn.disabled=true; btn.innerHTML="Connecting…";
      try{ await fetch(ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:"Call request",email:"",phone:v("phone"),service:"",source:CALL_SOURCE,message:"Call request (clicked to call)\n\nPage: "+location.href})}); }catch(_){}
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
    makeForm(card, { header:true, title:(box.getAttribute("data-title")||"Get your free estimate"), reset:true });
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
