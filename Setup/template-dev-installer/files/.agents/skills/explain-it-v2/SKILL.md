---
name: explain-it-v2
description: Evidence-based interactive walkthrough using retrieval practice, Socratic questioning, and productive struggle. Calibrated to user's level. Use when user says "explain this", "walk me through", "teach me this", "break this down", or pastes an error and asks "what happened".
---

# Explain It V2

Interactive, evidence-based walkthrough that challenges the user to think actively rather than passively consuming explanations.

## Core Learning Principles

Every interaction incorporates these evidence-based strategies:

1. **Retrieval Practice** — Force recall from memory, not passive rereading
2. **Generation Effect** — Ask user to produce an answer before showing the correct one
3. **Socratic Questioning** — Guide through questions, don't just give answers
4. **Productive Struggle** — Present challenges before solutions
5. **Bloom's Taxonomy** — Progress: Remember → Understand → Apply → Analyze → Evaluate → Create

See [REFERENCE.md](REFERENCE.md) for detailed learning science.

## Phase 1: Gather

Determine what's being explained:
- **File in project** → read it in full
- **Code in chat** → work from conversation directly
- **Error message** → work from pasted text

If the file references other short, directly relevant files, read those too.

## Phase 2: Calibrate

### Quick check (always)

Ask 2-3 rapid-fire questions to gauge skill level. One at a time.

**Style:** casual, "help me calibrate" not "let me test you."

If a question can be answered from codebase/conversation history, figure it out yourself.

### Grill session (optional)

After quick check, offer to do a quick grill session based on the grill me skill.

If yes: activate the grill-me skill and utilize its architecture to calibrate the user's skill level.

### Build level map

Tag each concept:
- ✅ **Knows it** → correct terminology, skip basics
- 🟡 **Sort of knows it** → brief refresh
- ❌ **No idea** → plain English, analogies, build from scratch

If user says "just explain it" → default to beginner and go.

## Phase 3: Active Explanation

For each section, follow this cycle:

### 3a. Present (Generation Effect)

Show the code WITHOUT explanation. Ask:

> "Before I break this down, what do you think this section does? Even a wrong guess helps."

Wait for user's attempt.

### 3b. Socratic Feedback

Assess their answer:
- If correct: acknowledge, ask a follow-up to probe deeper
- If partially correct: acknowledge what's right, ask guiding question about what's missing
- If wrong or "no idea": that's fine, move to explanation

Don't spend more than 1-2 exchanges here. The goal is activation, not interrogation.

### 3c. Explain

Now give the full breakdown using:
- **Tables** for structured comparisons
- **Analogies** for abstract concepts
- **Plain English translations** of technical syntax
- **Why it matters** in one line

Match depth to the level map from Phase 2.

### 3d. Retrieval Check

After explanation, ask a retrieval question:
- "Explain this back to me in your own words"
- "How would you modify this to do X?"
- "What would happen if we removed this line?"

Wait for answer, give brief feedback, then move on.

### For Error Messages

1. **Present** — show the error, ask "What do you think went wrong?"
2. **Socratic probe** — based on their answer, ask a follow-up
3. **Explain** — TL;DR, fix, why it happened, prevention
4. **Retrieval** — "If you saw this error again, what would you check first?"

## Phase 4: Reinforcement

After all sections:

### 4a. Connection Diagram

ASCII art showing how pieces relate.

### 4b. Spaced Retrieval

Circle back to 2-3 earlier concepts:
- "Quick check — can you remind me what [earlier concept] does?"
- Mix concepts from different sections (interleaving)

### 4c. Application Challenge

Present a new scenario requiring application:
- "Given this schema, how would you add [new feature]?"
- "If you wanted to change [behavior], what would you modify?"

Target Apply/Analyze level of Bloom's, not just Remember.

## Rules

- **Never explain before asking** — always give user a chance to generate first
- **One section at a time** for large files (>50 lines)
- **Match the level map** — don't over-explain what they know
- **Use their context** — reference their actual project, not generic examples
- **Celebrate attempts** — wrong answers are valuable, acknowledge the thinking
- **No setup overhead** — conversational only, don't create files unless asked
- **Pause after retrieval** — wait for answer before moving on