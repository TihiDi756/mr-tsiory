(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const b=$('.burger'),m=$('#menu');
if(b){b.onclick=()=>{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)};$$('#menu a').forEach(a=>a.onclick=()=>{m.classList.remove('open');b.setAttribute('aria-expanded',false)})}
$$('[data-copy]').forEach(x=>x.onclick=async()=>{const s=$('#copied');try{await navigator.clipboard.writeText(x.dataset.copy);s.textContent='Adresse copiée.'}catch{s.textContent='Copie impossible : sélectionnez l\u2019adresse manuellement.'}});
const OK="Merci pour votre demande. Votre message a bien été transmis à MR TSIORY. Nous reviendrons vers vous par les coordonnées communiquées.";
const KO="Votre message n\u2019a pas pu être transmis. Veuillez réessayer ou nous contacter directement par e-mail.";
$$('.js-form').forEach(f=>{
 const st=$('.status',f),steps=$$('.step',f);let i=0;
 const valid=(scope)=>{let ok=true;$$('input,select,textarea',scope).forEach(el=>{if(el.name==='bot-field')return;const bad=!el.checkValidity();el.setAttribute('aria-invalid',bad);if(bad&&ok){ok=false;el.focus();st.className='status err';st.textContent='Veuillez corriger : '+(el.closest('label')?.firstChild?.textContent||el.name)+'.'}});if(ok)st.textContent='';return ok};
 const show=()=>{steps.forEach((s,k)=>s.classList.toggle('on',k===i));$('.stepno',f).textContent='Étape '+(i+1)+' sur '+steps.length;$('[data-prev]',f).hidden=i===0;$('[data-next]',f).hidden=i===steps.length-1;
  if(i===steps.length-1){const d=new FormData(f),r=$('#recap');r.textContent='';[...d.entries()].filter(([k,v])=>v&&!['form-name','bot-field','consentement'].includes(k)).forEach(([k,v])=>{const p=document.createElement('div');p.textContent=k+' : '+v;r.appendChild(p)})}};
 if(steps.length){f.classList.add('js-on');show();$('[data-next]',f).onclick=()=>{if(valid(steps[i])){i++;show()}};$('[data-prev]',f).onclick=()=>{i--;show()}}
 f.addEventListener('submit',async ev=>{ev.preventDefault();if(steps.length){f.classList.remove('js-on')}if(!valid(f)){if(steps.length)f.classList.add('js-on');return}
  const btn=$('button[type=submit]',f);btn.disabled=true;st.className='status';st.textContent='Envoi en cours…';
  try{const body=new URLSearchParams(new FormData(f)).toString();const r=await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body});
   if(!r.ok)throw new Error(r.status);st.className='status ok';st.textContent=OK;f.reset();$$('.step',f).forEach(s=>s.style.display='none')}
  catch{st.className='status err';st.textContent=KO;btn.disabled=false;if(steps.length)f.classList.add('js-on')}});
});})();