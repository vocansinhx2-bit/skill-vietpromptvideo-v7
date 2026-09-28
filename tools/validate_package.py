from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
required=['SKILL.md','manifest.yaml','modules/03_EXAMPLE_DISTILLATION_ENGINE.md','modules/32_AUDIENCE_FIREWALL_RUNTIME_PURITY.md','modules/37_MASTER_PROMPT_PURITY_LINTER.md','tests/master_prompt_purity_benchmark.md']
missing=[x for x in required if not (root/x).exists()]
if missing:
    print('FAIL missing:', missing); sys.exit(1)
text=(root/'SKILL.md').read_text(encoding='utf-8')
for phrase in ['EXAMPLE QUARANTINE LAW','AUDIENCE FIREWALL','MASTER PROMPT HARD GATES']:
    if phrase not in text:
        print('FAIL missing core phrase', phrase); sys.exit(1)
mods=list((root/'modules').glob('*.md'))
if len(mods)<45:
    print('FAIL module count', len(mods)); sys.exit(1)
print('PASS')
print('modules=',len(mods))
print('files=',sum(1 for p in root.rglob('*') if p.is_file()))
