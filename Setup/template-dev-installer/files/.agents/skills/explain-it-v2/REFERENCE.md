# Learning Science Reference

## The Evidence Base

### Retrieval Practice (Strongest Evidence)

**What:** Actively recalling information from memory rather than passively rereading.

**Evidence:** Systematic review of 50 classroom experiments found retrieval practice reliably benefits learning across materials, ages, abilities, and test types (Agarwal et al., Annual Reviews; Yang et al., Educational Psychology Review).

**Why it works:** Retrieval strengthens memory traces and slows forgetting. The act of trying to remember is itself a learning event.

**Application in this skill:**
- Ask "What do you think this does?" before explaining
- "Explain this back to me in your own words" after explaining
- "How would you modify this to do X?" (application-level retrieval)

### Generation Effect (Strong Evidence)

**What:** Producing information (writing, typing, saying) leads to better retention than reading it.

**Evidence:** Meta-analysis found moderate benefit (Hedges' g = .41) for generating text over reading, not due to extra time spent (Springer Nature, 2023).

**Why it works:** Generation requires deeper processing and creates stronger memory traces.

**Application in this skill:**
- Always ask user to attempt an answer before showing the correct one
- Even wrong guesses improve retention of the correct answer
- "What would happen if we removed this line?" forces generation

### Socratic Questioning (Good Evidence)

**What:** Asking questions that guide thinking rather than providing direct answers. Oxford tutorial system uses this extensively.

**Evidence:** Studies show Socratic-style AI questioning improves learning and engagement. One study reported 45% knowledge gain and 13% confidence boost in code comprehension (ACM, 2020).

**Why it works:** Forces active thinking, reveals misconceptions, builds intellectual curiosity.

**Application in this skill:**
- "What do you think [concept] means?" before explaining
- "Why do you think they chose to do it this way?"
- "What would be a different approach and what are the tradeoffs?"

### Bloom's Taxonomy (Widely Used Framework)

**Levels (lowest to highest cognitive demand):**
1. **Remember** — Recall facts ("What is a foreign key?")
2. **Understand** — Explain ideas ("Why do we need foreign keys?")
3. **Apply** — Use information in new situations ("Add a foreign key to this new table")
4. **Analyze** — Draw connections ("How does this trigger relate to the scores table?")
5. **Evaluate** — Justify decisions ("Is this schema design good? What would you change?")
6. **Create** — Produce new work ("Design a schema for a similar system")

**Application in this skill:**
- Start with Remember/Understand for basic concepts
- Progress to Apply/Analyze for retrieval checks
- End with Evaluate/Create in application challenges

### Desirable Difficulties (Bjork)

**What:** Conditions that make learning harder in specific ways improve long-term retention.

**Key strategies:**
- **Spacing** — Distribute practice over time
- **Interleaving** — Mix different topics within a session
- **Generation** — Produce answers rather than read them

**Why it works:** Difficulty during learning creates stronger memory traces. Easy learning = weak retention.

**Application in this skill:**
- Interleaving: Circle back to earlier concepts later (spaced retrieval)
- Generation: Always ask before telling
- Productive struggle: Let user think before giving answers

### Productive Struggle

**What:** Engaging with challenging tasks promotes deeper learning, even if the user gets it wrong initially.

**Evidence:** "Productive Failure" research shows solving problems before receiving instruction prepares learners to notice and encode critical features (Review of Educational Research, 2021).

**Why it works:** Struggle activates relevant prior knowledge and creates "hooks" for new information.

**Application in this skill:**
- Present code before explaining it
- Ask "What do you think this does?" even if user might be wrong
- Celebrate attempts — wrong answers are valuable learning events

### Feynman Technique

**What:** Explain a concept in simple language (like to a child), identify gaps, review and simplify.

**Evidence:** Effectiveness derives from combining self-explanation and retrieval practice (both have strong independent research support).

**Application in this skill:**
- "Explain this back to me in your own words" is a Feynman-style retrieval
- "How would you explain this to someone who's never seen SQL?"
- If user struggles, that reveals a gap to address

### Metacognition and Calibration

**What:** "Thinking about thinking" — the ability to monitor and control your own learning. A key component is **metacognitive calibration**: how accurately you assess what you know.

**Challenge:** Students are often overconfident and overestimate their understanding.

**Application in this skill:**
- Calibration phase helps user (and agent) accurately assess current knowledge
- Retrieval checks reveal actual understanding vs perceived understanding
- "Explain this back to me" exposes gaps the user didn't know they had

## When to Use Each Technique

### Generation Effect (Ask Before Telling)
**Use when:** Introducing any new section or concept
**Don't use when:** User clearly knows it already (from calibration)

### Retrieval Practice (Explain Back)
**Use when:** After explaining a concept, to solidify understanding
**Don't use when:** User is struggling and needs more support first

### Socratic Questioning (Guiding Questions)
**Use when:** User gives a partial answer or you want to probe deeper
**Don't use when:** User is clearly confused and needs direct explanation

### Interleaving (Mix Concepts)
**Use when:** Spaced retrieval phase, to strengthen connections
**Don't use when:** User needs to master one concept before moving on

### Productive Struggle (Present Challenge First)
**Use when:** User has some baseline knowledge (from calibration)
**Don't use when:** User is a complete beginner on this topic (just explain)

## Adapting to User Level

### For ✅ "Knows It" Concepts
- Minimal generation prompts ("Quick sanity check — what does this do?")
- Jump to higher Bloom's levels (Analyze, Evaluate)
- Focus on project-specific usage, not general explanation
- Retrieval checks can be application-level ("How would you change this?")

### For 🟡 "Sort of Knows It" Concepts
- Brief generation prompt ("What do you remember about this?")
- Quick refresher explanation
- Standard retrieval checks
- Connect to what they already know

### For ❌ "No Idea" Concepts
- Skip generation prompt (would be frustrating, not productive)
- Go straight to explanation with analogies and tables
- Simple retrieval checks ("Explain this back in your own words")
- Celebrate any attempt, even partial

## Example Dialogue Flow

### User says: "Explain this SQL file"

**Agent (Phase 2: Calibrate):**
> "Before we dive in, quick calibration — have you worked with SQL before, or is this new?"

**User:** "I know the basics — SELECT, INSERT, that kind of thing."

**Agent:** "Got it. And what about triggers and materialized views — familiar, or new territory?"

**User:** "No idea what those are."

**Agent (Phase 3: Active Explanation):**

*Shows first section (table definitions)*

> "Alright, let's start here. You know SQL basics, so — what do you think these CREATE TABLE statements are setting up? What's the relationship between these tables?"

**User:** "Looks like clans, events, and scores. Events probably reference clans?"

**Agent (Socratic feedback):**
> "Spot on! Events do reference clans. Quick follow-up — what do you think happens to events if we delete a clan? Look for a clue in the SQL."

**User:** "Oh, ON DELETE CASCADE — so the events get deleted too?"

**Agent:**
> "Exactly! Now here's the full breakdown..."

*[Gives detailed explanation with tables and analogies]*

**Agent (Retrieval check):**
> "OK, so if I insert a new event for clan 'SIG' in season 1 worth 100 points, what happens to the clan_season_scores table?"

**User:** "The trigger fires and adds 100 to SIG's season 1 total?"

**Agent:**
> "Perfect! Now let's tackle triggers and materialized views — these are new for you, so I'll explain first..."

*[Goes straight to explanation without generation prompt, since user said they don't know these]*

## Common Pitfalls

### Over-Questioning
**Wrong:** Asking 5 Socratic questions per section
**Right:** 1 generation prompt + 1 retrieval check per section (max)

### Ignoring Calibration
**Wrong:** Asking "What's a SELECT statement?" when user said they know SQL
**Right:** Skip basics, focus on project-specific usage

### No Retrieval
**Wrong:** Explaining everything without checking understanding
**Right:** "Explain this back to me" after key concepts

### Too Much Struggle
**Wrong:** Letting user flounder on completely new concepts
**Right:** If calibration shows "no idea", explain first, then retrieve

### Passive Consumption
**Wrong:** Long explanations without interaction
**Right:** One section at a time, always pause for retrieval
