# SEO Internal Linking Workflow Playbook

This directory contains a reusable **Claude Skill & Antigravity Workflow** designed to analyze website pages and output high-quality, editor-ready internal linking recommendations.

## What is this Workflow?

Unlike traditional software which requires complex server deployments and database configurations, this is a **playbook and instruction set** that turns any Claude agent (like Claude Code or Antigravity) into a specialized **Internal Linking Strategist**. 

It uses the exact algorithmic formulas, link positioning weights, and 12-tier priorities designed in our core Node.js codebase to perform audits and suggest links directly inside your chat.

---

## How the Workflow Operates (Replicated V1 Logic)

When you run this workflow, the AI agent mimics our core Node.js codebase calculations:

### 1. Link Position Power Calculation
Not all links are created equal. The workflow tracks the position of existing links on a page using the formula:
$$\text{DOM Position Ratio} = \frac{\text{Link Index}}{\text{Total Links on Page}}$$
- **Header & Navbar Links (`Ratio` $\le 0.15$):** Earn **0.2** power.
- **Footer Links (`Ratio` $\ge 0.85$):** Earn **0.1** power.
- **Main Content Links (`Ratio` between $0.15$ and $0.85$):** Earn **1.0** power.

### 2. Page Classification
The raw inbound link scores are normalized:
$$\text{Normalized Score} = \frac{\text{Page Inbound Score} - \text{Min Score}}{\text{Max Score} - \text{Min Score}}$$
Pages are grouped into:
- **Orphan Pages:** 0 inbound links (except homepage). Priority action needed!
- **Strong Pages:** Normalized score $> 0.7$ (these act as authority donor pages).
- **Normal Pages:** Normalized score between $0.3$ and $0.7$.
- **Weak Pages:** Normalized score $\le 0.3$ (target pages requiring more link equity).

### 3. The 12-Tier Priority Matrix
Recommendations are sorted using a 12-tier matrix, matching strong/normal donor pages with weak/orphan target pages:
- **Priority 1-3:** Links pointing to **Orphan Pages**.
- **Priority 4-6:** Links pointing to **Weak Pages**.
- **Priority 7-9:** Links pointing to **Normal Pages**.
- **Priority 10-12:** Links pointing to **Strong Pages**.

---

## How to Execute the Workflow in Claude

To execute this workflow, you can feed page metadata directly to Claude.

### Step 1: Copy the Prompt Template
Use the following prompt to initialize the audit:

```markdown
I want you to run an Internal Linking Audit. Please follow the rules defined in the `seo-internal-linking-workflow` skill.

Here is the list of pages and their metadata from my website:

---
URL: /home
Title: Finance Tips & Tricks
Description: Your guide to automated personal budgeting and smart saving.
Links:
  - href: /about (Position: 1, Total Links: 4, rel: follow)
  - href: /automated-budgeting (Position: 2, Total Links: 4, rel: follow)
---
URL: /automated-budgeting
Title: Complete Guide to Automated Budgeting
Description: Learn how to set up an automated budget using spreadsheets and tools.
Links:
  - href: /home (Position: 1, Total Links: 2, rel: follow)
---
URL: /saving-strategies
Title: 10 Savings Strategies that Work
Description: Simple changes to increase your monthly savings rate.
Links:
  - href: /home (Position: 1, Total Links: 2, rel: follow)
---
URL: /pricing
Title: Product Pricing Plans
Description: Compare plans and pricing.
Links: []
---

Please calculate the link power scores, classify the pages, find matching semantic opportunities (skipping utility/stop pages like /pricing), score them using the 12-tier matrix, and write contextual insertion sentences.
```

### Step 2: Review the Output Table
The workflow will generate a clean implementation table:

| Source URL | Target URL | Anchor Text | Suggested Sentence | Priority | Reason |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `/saving-strategies` | `/automated-budgeting` | automated budget | "To maximize your savings rate, setting up an [automated budget] can help track expenses without manual intervention." | 5 | Normal-to-Weak semantic flow linking savings to automated budgeting |

### Step 3: Action the Key Sections
- **Quick Wins:** Immediately copy the High Priority (Priority 1-4) suggestions and paste them into your CMS editor.
- **Orphan Rescue:** Add links to the flagged Orphan pages first to ensure Google indexes them.
- **Anchor Variations:** Use the suggested partial-match anchor texts to keep your link profile natural and avoid Google over-optimization penalties.
