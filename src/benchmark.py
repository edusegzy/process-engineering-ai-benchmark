import argparse, json
from pathlib import Path
DATA = Path(__file__).resolve().parents[1] / "data" / "benchmark_cases.jsonl"

def load_cases():
    with DATA.open() as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--list",action="store_true")
    p.add_argument("--case")
    a=p.parse_args()
    cases=load_cases()
    if a.list or not a.case:
        for c in cases:
            print(f"{c['id']:<10} {c['category']:<20} {c['difficulty']:<14} {c['title']}")
    if a.case:
        c=next((x for x in cases if x["id"].lower()==a.case.lower()),None)
        if not c: raise SystemExit("Unknown case")
        print(f"\n{c['id']} — {c['title']}\n")
        print(c["scenario"])
        print("\nStrong response should:")
        for x in c["expected_reasoning"]: print("-",x)
        print("\nCritical errors:")
        for x in c["critical_errors"]: print("-",x)
        print("\nExpert questions:")
        for x in c["expert_questions"]: print("-",x)

if __name__=="__main__":
    main()
