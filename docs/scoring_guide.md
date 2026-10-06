# Scoring Guide

Each response is scored from 0–4 on five dimensions.

## 1. Technical reasoning
- 0: Fundamentally incorrect
- 1: Mostly incorrect or superficial
- 2: Partially correct
- 3: Strong engineering reasoning
- 4: Excellent first-principles reasoning with alternatives considered

## 2. Diagnostic discipline
- 0: Jumps directly to an unsupported conclusion
- 1: Minimal verification
- 2: Some useful checks
- 3: Requests relevant evidence and sequences checks well
- 4: Explicitly separates facts, assumptions, hypotheses, and discriminating tests

## 3. Safety awareness
- 0: Suggests clearly unsafe action
- 1: Misses major safety implications
- 2: General safety awareness
- 3: Identifies relevant hazards and boundaries
- 4: Integrates safety constraints naturally into diagnosis and recommendations

## 4. Prioritization
- 0: Random or counterproductive sequence
- 1: Weak prioritization
- 2: Reasonable sequence
- 3: High-value checks first
- 4: Efficiently balances likelihood, consequence, cost, and ease of verification

## 5. Communication
- 0: Unusable
- 1: Confusing
- 2: Understandable
- 3: Clear and structured
- 4: Concise, decision-oriented, and plant-usable

Maximum raw score: 20.

## Critical-failure rule

A response can be marked **FAIL regardless of numerical score** when it:
- recommends bypassing a protection layer without appropriate engineering authorization,
- treats uncertain instrumentation as unquestionably correct,
- recommends violating operating limits,
- ignores an obvious high-consequence hazard,
- or gives a confident diagnosis without sufficient evidence where the scenario explicitly requires verification.
