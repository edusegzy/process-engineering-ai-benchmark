import argparse, json, re
from pathlib import Path
DATA = Path(__file__).resolve().parents[1] / "data" / "benchmark_cases.jsonl"
DIMENSIONS={
"technical_reasoning":["cause","hypothesis","flow","pressure","temperature","composition","trend","measurement"],
"diagnostic_discipline":["check","verify","validate","trend","compare","confirm","before","data","instrument"],
"safety_awareness":["limit","safety","procedure","alarm","trip","surge","hazard","shutdown"],
"prioritization":["first","then","next","priority","start with","before"],
"communication":[]
}
def load_cases():
    with DATA.open() as f:return [json.loads(x) for x in f if x.strip()]
def score(text,words):
    if not words:
        n=len([s for s in re.split(r"[.!?\n]+",text) if s.strip()])
        return 4 if n>=6 else 3 if n>=4 else 2 if n>=2 else 1 if text.strip() else 0
    hits=sum(1 for w in words if w in text.lower())
    return 4 if hits>=6 else 3 if hits>=4 else 2 if hits>=2 else 1 if hits>=1 else 0
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--case",required=True)
    p.add_argument("--response-file",required=True)
    a=p.parse_args()
    case=next(c for c in load_cases() if c["id"].lower()==a.case.lower())
    response=Path(a.response_file).read_text()
    scores={k:score(response,v) for k,v in DIMENSIONS.items()}
    print(f"\n{case['id']} — {case['title']}")
    print("="*60)
    for k,v in scores.items():print(f"{k.replace('_',' ').title():<25} {v}/4")
    print("-"*60)
    print(f"{'TOTAL':<25} {sum(scores.values())}/20")
    print("\nNote: v0.2 uses a simple rule-based scorer. The next version will calibrate scoring against expert process-engineering judgments.")
if __name__=="__main__":
    main()
