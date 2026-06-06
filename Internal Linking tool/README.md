# V2 Strategic Internal Linking Workflow Playbook

This folder contains a reusable **Claude Skill & Antigravity Workflow** that transforms Claude into an elite senior SEO strategist. The workflow shifts focus entirely from simple keyword-matching to a robust **Intelligence Layer**—optimizing relevance, search intent alignment, user value, and logical topic clustering.

---

## Strategic Core Principles

1. **Quality Over Volume:** An elite link audit rejects the noise. This engine targets a **70% to 90% rejection rate** of raw keyword matches. Only the highest-value, contextual links survive.
2. **Rejection-First Architecture:** Before a recommendation is made, it must pass 8 distinct quality checks, including **Contradiction Testing** (actively formulating the strongest argument *against* creating the link).
3. **Auditable Evidence:** Every recommendation is backed by a structured **Evidence Block** listing the specific shared topics, shared entities, and intent indicators that justify the link.
4. **Value vs. Confidence Decoupling:** We track value (Relevance, SEO Impact, User Value, Conversion Impact) separately from Confidence (data certainty). A link can have massive potential impact but low confidence due to context ambiguity.

---

## The 8-Step Rejection Framework

Every candidate link must pass at least **7 out of 8 tests** (including mandatory Tests 1, 2, 3, 5, and 8) to be approved:

- **Test 1: Topical Relationship (Mandatory):** Do the pages share a clear semantic connection?
- **Test 2: Intent Relationship (Mandatory):** Are search intents compatible? (e.g., no premature pricing links in early-stage guides).
- **Test 3: User Value (Mandatory):** Would a human user actually benefit from clicking this link?
- **Test 4: Editorial Naturalness:** Does the insertion sentence read naturally without feeling forced?
- **Test 5: Existing Link Check (Mandatory):** Is this link redundant or already present?
- **Test 6: Anchor Quality:** Is the anchor text descriptive and natural (no repetitive exact-match or generic text)?
- **Test 7: Cluster Relevance:** Does the link reinforce the primary topic cluster?
- **Test 8: Contradiction Testing (Mandatory):** Does the supporting evidence outweigh the strongest counter-argument?

---

## How to Execute the V2 Workflow in Claude

### Copy-Paste Prompt Template

To run this workflow on your site's data (HTML pages, sitemaps, or crawl JSON), copy the prompt template below and paste it into your chat session:

```markdown
I want you to run an Internal Linking Audit. Please follow the instructions defined in the `seo-internal-linking-workflow` skill.

Here is the page data from my website (searchIndex or paragraph crawl):
[INSERT PAGES OR SEARCH INDEX DATA HERE]

Please execute the 9-Stage Recommendation Pipeline:
1. Strip boilerplate, header, and footer text.
2. Build the relationship engine mapping topic clusters and intent categories.
3. Apply the 8-Step Rejection Framework (enforcing the 70%-90% rejection rate target).
4. Run Contradiction Testing for each candidate.
5. Calculate independent value metrics and separate confidence scores.
6. Generate natural, editorial-quality insertion sentences with diverse anchors.
7. Return the final report, including the "Why This Link Exists" Evidence Blocks for approved links and the Rejection Ledger.
```

---

## Report Output Format

The workflow generates two key tables and detailed evidence blocks:

### 1. Approved Recommendations Ledger
Every approved recommendation includes the complete auditable evidence block:

```markdown
### 1. Approved Recommendation: /blog/developer-burnout → /features/resource-scheduling
- **Source URL:** `/blog/developer-burnout`
- **Target URL:** `/features/resource-scheduling`
- **Suggested Anchor:** `visual capacity planning tools`
- **Suggested Sentence:** "To prevent burnout before it starts, managers can use [visual capacity planning tools] to monitor workloads in real-time."

[EVIDENCE & DECISION BLOCK]
- **Relationship Type:** Supporting Topic / Product Feature Mapping
- **Intent Relationship:** Informational → Commercial Investigation
- **User Journey:** Problem Aware (Burnout) → Solution Aware (Workload Management)
- **Objective Evidence:**
  - *Shared Topic:* Workload Allocation & Capacity Planning
  - *Shared Entities:* team capacity, burnout prevention, developer allocation, WIP limits
  - *Intent Indicators:* Informational search queries about team stress matching feature solutions.
- **Contradiction Test Objection:** "The user is looking for mental health tips for burnout; pitching a product scheduling feature too early might feel overly transactional."
- **Contradiction Test Resolution:** "Burnout is structurally caused by overallocation. Introducing a concrete workload management feature provides direct, actionable utility, solving the root cause of the reader's query."
- **Calculated Scores:**
  - *Relevance Score:* 85 (Strong alignment between team capacity and developer burnout)
  - *SEO Impact Score:* 75 (Pushes high blog traffic equity to key product features)
  - *User Value Score:* 88 (Provides a direct operational fix to the described problem)
  - *Conversion Impact Score:* 70 (Soft commercial funnel progression)
  - *Confidence Score:* 90 (High certainty of semantic alignment)
```

### 2. Rejection Ledger
All rejected candidate links must be documented to show the audit trail:

| Discovered Opportunity (Source → Target) | Trigger Phrase | Rejection Reason | Tripped Test |
| :--- | :--- | :--- | :--- |
| `/blog/security-compliance` → `/pricing` | "pricing structure" | Keyword match only. User intent is security regulation study; linking to product pricing plans disrupts the educational reading flow. | Test 2 (Intent Relationship) - Fail |
| `/blog/teeth-grinding` → `/services/veneers` | "veneers can restore" | Intent mismatch. Bruxism is a structural disorder. Suggesting cosmetic veneers before stabilizing the grinding habit violates clinical sequencing. | Test 8 (Contradiction Testing) - Fail |
| `/blog/summer-fashion` → `/products/winter-coat` | "winter clothing storage" | Seasonal relevance mismatch. surufacing a wool winter coat product page to a summer swimwear reader violates current intent. | Test 7 (Cluster Relevance) - Fail |
