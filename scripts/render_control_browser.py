"""Build an offline, searchable view of the authoritative library."""
import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def render() -> str:
    library = yaml.safe_load((ROOT / "data/controls.yaml").read_text())
    payload = json.dumps(library, ensure_ascii=True).replace("<", "\\u003c")
    return '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Independent AI Control Library</title>
<style>
body{font:16px/1.6 system-ui,sans-serif;max-width:1080px;margin:auto;padding:32px;color:#173246;background:#f5f8fa}
h1{line-height:1.15}header{border-bottom:3px solid #087f8c;padding-bottom:20px}label{display:inline-grid;gap:6px;margin:8px 12px 8px 0}
input,select{font:inherit;padding:10px;border:1px solid #8195a5;border-radius:5px;max-width:100%;box-sizing:border-box}
input{width:330px}article{background:white;border:1px solid #d9e2e8;border-radius:8px;margin:18px 0;padding:22px}
article h2{margin-top:0;font-size:1.2rem}a{color:#086674}summary{cursor:pointer;font-weight:600}.meta{font-size:.9rem;color:#476173}
:focus-visible{outline:3px solid #087f8c;outline-offset:3px}@media(max-width:600px){body{padding:18px}label{display:grid;margin-right:0}input{width:100%}}
</style>
<header><p>Governance design / Reusable control library</p><h1>Independent AI Control Library</h1>
<p>Explore requirements, applicability, and evidence expectations. This generated view supports tailoring and human review; it does not establish compliance or control effectiveness.</p>
<p id="version"></p></header>
<main><label>Search controls<input id="search" type="search" placeholder="ID, topic, requirement, or evidence"></label>
<label>Domain<select id="domain"><option value="">All domains</option></select></label>
<label>Context<select id="context"><option value="">All contexts</option></select></label>
<p id="count" role="status" aria-live="polite"></p><div id="results"></div></main>
<script id="library" type="application/json">''' + payload + '''</script>
<script>
const library=JSON.parse(document.getElementById('library').textContent);
const controls=library.controls, el=id=>document.getElementById(id), display=s=>s.replaceAll('_',' ');
const text=(tag,value,parent)=>{const node=document.createElement(tag);node.textContent=value;parent.append(node);return node};
for(const [key,values] of [['domain',controls.map(c=>c.domain)],['context',controls.flatMap(c=>c.applicability_metadata.contexts)]]){
 for(const value of [...new Set(values)].sort()){const option=text('option',display(value),el(key));option.value=value;}}
el('version').textContent=`Library ${library.library.version} / ${controls.length} controls / Generated from data/controls.yaml`;
function render(){
 const term=el('search').value.toLowerCase(),domain=el('domain').value,context=el('context').value;
 const matches=controls.filter(c=>(!domain||c.domain===domain)&&(!context||c.applicability_metadata.contexts.includes(context))&&JSON.stringify(c).toLowerCase().includes(term));
 el('count').textContent=`${matches.length} of ${controls.length} controls`;el('results').replaceChildren();
 for(const c of matches){const card=document.createElement('article');card.id=c.control_id;
  const h=text('h2','',card),a=text('a',`${c.control_id}: ${c.title}`,h);a.href='#'+c.control_id;
  text('p',`${display(c.domain)} / ${display(c.layer)} / ${display(c.applicability_metadata.mode)}`,card).className='meta';
  text('p',c.objective,card);text('p',c.requirement,card);const details=document.createElement('details');text('summary','Applicability and evidence',details);
  text('p',c.applicability,details);text('p',c.applicability_metadata.rationale,details);
  const list=document.createElement('ul');for(const item of c.evidence_examples)text('li',item,list);details.append(list);
  text('p',c.implementation_notes,details);text('p','References: '+c.references.map(r=>library.reference_catalog[r]).join('; '),details);card.append(details);el('results').append(card);}
 if(location.hash){const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(target)target.scrollIntoView();}}
for(const id of ['search','domain','context'])el(id).addEventListener('input',render);render();
</script></html>
'''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    target = ROOT / "docs/control-browser.html"
    content = render()
    if args.check:
        raise SystemExit(0 if target.exists() and target.read_text() == content else 1)
    target.write_text(content, encoding="utf-8")
