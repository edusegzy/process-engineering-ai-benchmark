# Process Engineering AI Benchmark

A domain-specific benchmark for evaluating whether AI systems can reason like careful chemical/process engineers.

## Why this exists

General-purpose LLM benchmarks rarely test the combination of:
- process fundamentals
- troubleshooting discipline
- uncertainty handling
- plant safety awareness
- operational realism
- asking for missing data before recommending action

This project evaluates AI systems intended for chemical plants, refineries, petrochemical facilities, midstream operations, and engineering workflows.

## What the benchmark measures

Each AI response is scored on five dimensions:

1. **Technical reasoning** — Are the hypotheses physically plausible?
2. **Diagnostic discipline** — Does the model ask for the right data before jumping to conclusions?
3. **Safety awareness** — Does it recognize hazards and avoid unsafe recommendations?
4. **Prioritization** — Does it rank likely causes and next checks intelligently?
5. **Communication** — Is the response clear, structured, and useful to an engineer/operator?

## Initial engineering coverage

- Distillation
- Heat exchangers
- Compressors
- Pumps
- Adsorption/dehydration beds
- Process control
- Utilities
- HAZOP/PHA reasoning
- Material balances
- Startup / abnormal operations

## Run locally

```bash
python -m src.benchmark --list
python -m src.benchmark --case HX-001
python -m src.evaluate_response --case HX-001 --response-file sample_response.txt
```

## What this project is becoming

The goal is not merely to collect engineering questions. It is to build a **testing laboratory for industrial AI**:

```text
Process engineering scenario
        ↓
AI under evaluation
        ↓
AI response
        ↓
Engineering evaluator
        ↓
Technical + diagnostic + safety score
```

## Roadmap

- [x] Define benchmark schema
- [x] Add first 10 process-engineering cases
- [x] Add scoring guide
- [x] Add command-line case browser
- [x] Add first rule-based evaluator
- [ ] Calibrate scoring against expert judgments
- [ ] Add calculation-heavy cases
- [ ] Add model API evaluation
- [ ] Add model comparison leaderboard
- [ ] Expand to 50+ expert-authored cases

## Safety

This benchmark is for evaluation, training, and engineering education. AI recommendations affecting an operating facility should be independently reviewed by qualified personnel and governed by site procedures, operating limits, management of change, and process-safety requirements.
