#!/usr/bin/env python3
from pathlib import Path
import argparse,re,json

PATTERNS={
 'CREATOR_COMMENTARY_LEAKAGE':[
  r'\bthis section (?:helps|is intended|exists)\b', r'\bwe (?:added|included|designed|trained|learned)\b',
  r'\bnote for (?:the )?(?:creator|author|designer)\b', r'\bthe purpose of this (?:section|rule) is\b'],
 'PROVENANCE_LEAKAGE':[
  r'\bbased on (?:the )?(?:previous|training|above) examples?\b', r'\bas learned from\b',
  r'\bprevious generations?\b', r'\bhistorical (?:case|failure|example)\b',
  r'\b(?:was|were|been|is|are)?\s*trained (?:using|on|with) (?:the )?examples?\b', r'\bthese examples (?:show|demonstrate|teach)\b'],
 'EXAMPLE_MARKER':[r'\bfor example\b', r'\be\.g\.', r'\bsuch as\b'],
 'DOCUMENTATION_STYLE_INTRUSION':[r'\bwhy this works\b', r'\bdesign rationale\b', r'\barchitecture summary\b', r'\bbenchmark score\b'],
}

def lint(text):
    findings=[]
    for name, pats in PATTERNS.items():
        for pat in pats:
            for m in re.finditer(pat,text,re.I):
                line=text.count('\n',0,m.start())+1
                findings.append({'gate':name,'line':line,'match':m.group(0)})
    status='FAIL' if any(f['gate'] in {'CREATOR_COMMENTARY_LEAKAGE','PROVENANCE_LEAKAGE'} for f in findings) else ('WARN' if findings else 'PASS')
    return {'status':status,'findings':findings}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description='Heuristic runtime Master Prompt purity linter')
    ap.add_argument('file')
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    result=lint(Path(args.file).read_text(encoding='utf-8'))
    if args.json: print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print(result['status'])
        for f in result['findings']: print(f"{f['gate']} line {f['line']}: {f['match']}")
