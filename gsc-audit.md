# Search Console Intelligence System Blueprint

## Overview

This blueprint outlines a high-level SEO intelligence system powered by Google Search Console (GSC), semantic analysis, intent mapping, CTR modelling, and AI visibility optimisation.

The goal is to transform raw search data into strategic growth decisions.

---

# Core Philosophy

Most SEO reporting tools only show metrics.

This system should:
- diagnose search performance problems
- identify opportunity patterns
- prioritise highest-impact actions
- recommend execution strategies
- support AI citation visibility
- detect intent mismatches
- automate growth discovery

---

# System Architecture

## Core Engines

1. Query Opportunity Engine
2. Intent Mismatch Engine
3. CTR Intelligence Engine
4. Content Gap Engine
5. Query Clustering Engine
6. Freshness Decay Engine
7. URL Structure Intelligence
8. Internal Linking Engine
9. AI Citation Opportunity Engine
10. Priority Scoring Engine

---

# STEP 1 — USER INPUT COLLECTION

## Required Inputs

### Google Search Console Export
Required fields:
- Query
- URL
- Clicks
- Impressions
- CTR
- Position

### Website Sitemap
Required:
- XML sitemap
- URL structure

### Analytics Data (Optional but Recommended)
Examples:
- Bounce rate
- Session duration
- Conversion rate

### Competitor URLs (Optional)
Useful for:
- content gap analysis
- semantic comparison
- SERP pattern analysis

---

# STEP 2 — DATA CLEANING

## Tasks

- Remove duplicate rows
- Standardise URLs
- Normalise query formatting
- Detect URL parameter issues
- Merge similar query variations

## Example

Merge:
- polished concrete
- polished concrete floor
- polished concrete flooring

Into semantic relationships.

---

# STEP 3 — QUERY INTELLIGENCE CATEGORIES (THE NEXT LAYER)

## Objective

Instead of a single filter, create multiple "opportunity buckets" representing distinct SEO strategies.

---

## 1. QUICK WIN QUERIES (Highest ROI)

### Conditions
- **Position**: 5–20
- **Impressions**: High (Top 25% of dataset)
- **CTR**: Below benchmark for position
- **URL**: Already relevant to the query

### Meaning
Google already partially trusts the page. Small technical or content refinements can trigger large traffic gains.
**Strategy**: Title/Meta optimization, content refresh, and internal linking.

---

## 2. HIDDEN DEMAND QUERIES (Underrated Opportunity)

### Conditions
- **Impressions**: Growing or stable
- **Clicks**: Low
- **Position**: 15–40
- **Targeting**: Query not directly addressed in H1 or Title

### Meaning
Google is "experimenting" with your page for these terms. It suggests relevance even without explicit targeting.
**Strategy**: Optimize existing sections, add dedicated subsections, or create new child pages.

---

## 3. HIGH-IMPRESSIONS / NO-CLICK QUERIES (Diagnosis Engine)

### Conditions
- **Impressions**: Massive
- **Clicks**: Near-zero
- **Position**: Variable (often Top 10)

### Diagnosis Factors
- **Bad Title**: Boring or irrelevant snippet.
- **Weak Intent Match**: Page is a service page, but SERP prefers a blog/guide.
- **Answer Box Proximity**: Google answers the query instantly in the SERP.
- **Low Commercial Appeal**: High volume but purely informational "what is" queries.

**Strategy**: Add pricing sections, cost calculators, or pivot content to match SERP intent.

---

## 4. POSITION 11–15 “PAGE 2 EDGE”

### Conditions
- **Position**: 11–15
- **Rankings**: Consistent over time
- **Intent**: High-value commercial or informational

### Meaning
Tiny improvements can move you from "invisible" (Page 2) to "high traffic" (Page 1).
**Strategy**: Improve topical depth, add LSI entities, optimize headings, and add FAQs.

---

## 5. POSITION DROPPING QUERIES (Decay Detection)

### Conditions
- **Impressions**: Falling
- **Avg Position**: Worsening
- **Clicks**: Declining

### Diagnosis
- **A. Freshness Decay**: Content is outdated compared to new competitors.
- **B. Intent Shift**: SERP results changed from "guides" to "product pages".
- **C. Competitor Outranking**: Competitors added more depth or better structured data.

---

# STEP 4 — COMPETITOR & SERP INTELLIGENCE

## Workflow

1. **Query Selection**: Identify top queries from the Opportunity Buckets.
2. **SERP Analysis**:
    - Perform Google Search for target queries.
    - Analyze top 3-5 competitors for **Intent Match**.
    - Compare Competitor Titles vs. Client Titles.
3. **On-Page Audit**:
    - Visit competitor pages.
    - Identify content sections missing on Client page.
    - Take screenshots of layouts rewarded by Google.
4. **Diagnosis**: Determine if Google is rewarding "Guides" (e.g., 2025 Price Guide) over "Service Pages".

---

# STEP 5 — REWARDED PAGE INTELLIGENCE

## Objective

Identify which specific pages Google is "promoting" based on click-through performance and suggest content expansion.

## Detection
- **GSC Metric**: Pages where Clicks > Homepage Clicks for specific clusters.
- **Example**: If a "2025 Price Guide" blog gets 3x more traffic than the Home page, the guide is the new "Authority Hub".

## Action
- Create more content around the rewarded theme.
- Convert the rewarded page into a "Pillar Page".
- Support other service pages via internal linking from this high-traffic asset.

---

# STEP 6 — INTERNAL LINKING OPPORTUNITIES

## Logic
- **High Click Pages** (The Donors) support **High Impression / Low Click Pages** (The Recipients).
- Link from pages with Avg Position < 20 (Low-hanging fruit) to target pages.
- Use exact-match or semantically rich anchor text from "The Next Layer" queries.

---

# SOURCES OF INTELLIGENCE

The methodologies in this system are derived from established SEO leadership and Google’s own ranking signals:

1. **Ahrefs / Backlinko**: The "Low Hanging Fruit" (Pos 5-20) prioritization framework.
2. **Growth Memo (Kevin Indig)**: Content decay models and "Hidden Demand" detection.
3. **Google Search Central**: Documentation on "Helpful Content" and intent-based ranking.
4. **Moz / Search Engine Land**: Internal link authority flow and "Pillar-Cluster" architecture.
5. **Search Engine Journal**: SERP intent shift analysis (Informational vs. Transactional).

---


## Detection Logic

Compare:
- Actual CTR
- Expected CTR for ranking position

---

## Example

| Position | Expected CTR |
|---|---|
| 1 | 28% |
| 3 | 11% |
| 5 | 6% |
| 8 | 3% |

If actual CTR is far below expected:
- title likely weak
- meta description weak
- SERP mismatch
- poor keyword alignment

---

# STEP 5 — TITLE TAG ANALYSIS

## Detect Issues

### Missing Primary Keywords

Example:
Query:
- concrete grinding christchurch

Title:
- Professional Surface Solutions

Issue:
Weak alignment.

---

## Missing Commercial Modifiers

Examples:
- affordable
- trusted
- certified
- local
- free quote
- best

---

## Missing Freshness Signals

Important for:
- AI
- SEO
- finance
- technology
- legal

Example:
- Best SEO Strategies for 2026

---

## SERP Pattern Comparison

Compare:
- competitor titles
- formatting patterns
- numbers
- years
- brackets
- emotional triggers

---

# STEP 6 — META DESCRIPTION ANALYSIS

## Detect

- duplicate metas
- missing CTAs
- truncation risk
- no keyword reinforcement
- weak emotional hooks
- generic AI-generated wording

---

# STEP 7 — INTENT MISMATCH ENGINE

## Objective

Detect when the page intent does not match Google's preferred SERP intent.

---

# Intent Categories

| Intent Type | Example |
|---|---|
| Informational | what is polished concrete |
| Commercial | best polished concrete company |
| Transactional | hire polished concrete service |
| Comparison | epoxy vs polished concrete |
| Local | concrete polishing near me |
| Visual | polished concrete ideas |

---

# Detection Examples

## Example

Query:
- best concrete polish

Current page:
- service page

SERP intent:
- comparison articles

Recommendation:
- create comparison article
- add educational comparison section
- split search intent

---

# STEP 8 — CONTENT GAP ENGINE

## Objective

Compare page depth against competitors.

---

# Detect Missing Topics

Examples:
- dust-free grinding
- epoxy preparation
- machinery types
- commercial applications
- pricing guidance

---

# Outputs

## Recommendations

- Add new sections
- Add FAQs
- Add tables
- Add visual examples
- Add process explanations
- Add comparison blocks

---

# STEP 9 — QUERY CLUSTER ENGINE

## Purpose

Group semantically related queries.

---

# Example Cluster

Queries:
- garage floor polishing
- polished concrete garage
- garage polished flooring

Cluster:
- Garage Polished Concrete

---

# Recommendations

Possible outputs:
- dedicated page
- dedicated section
- child page creation
- supporting blog content

---

# STEP 10 — CANNIBALISATION DETECTION

## Detect

Multiple URLs ranking for similar intent clusters.

---

# Example

| URL | Overlap |
|---|---|
| /concrete-polishing | 60% |
| /polished-concrete | 55% |

---

# Recommendations

- consolidate pages
- canonical setup
- restructure internal linking
- merge overlapping content

---

# STEP 11 — FRESHNESS DECAY ENGINE

## Purpose

Detect declining relevance.

---

# Signals

| Signal | Meaning |
|---|---|
| Falling impressions | relevance decay |
| Falling CTR | snippet weakness |
| Position decline | competitor improvement |
| Reduced query diversity | authority loss |

---

# Refresh Recommendation Types

## Minor Refresh
- title update
- FAQ addition
- schema updates

## Medium Refresh
- content expansion
- updated examples
- updated statistics

## Major Refresh
- rewrite
- intent restructuring
- page split

---

# STEP 12 — URL STRUCTURE ENGINE

## Detect Problems

### Weak Slugs

Bad:
- /services/page1

Better:
- /concrete-grinding-christchurch

---

## Keyword Mismatch

Page ranks for:
- epoxy garage floor

URL:
- /resin-solutions

---

## Folder Structure Issues

Bad:
- /blog/service/concrete-polishing

Better:
- /services/concrete-polishing

---

# STEP 13 — INTERNAL LINK ENGINE

## Detect

- orphan pages
- weak authority flow
- missing anchor text opportunities
- weak commercial link pathways

---

# Recommendations

- contextual internal links
- stronger anchor text
- topical hub structures
- service-to-blog linking

---

# STEP 14 — AI CITATION ENGINE

## Purpose

Increase visibility in AI-generated answers.

---

# AI-Friendly Signals

Pages containing:
- concise definitions
- step-by-step explanations
- tables
- FAQs
- comparisons
- expert summaries
- entity clarity

---

# Missing Structures

Detect absence of:
- FAQ schema
- definition blocks
- comparison tables
- summary sections
- author credibility
- structured answers

---

# STEP 15 — PRIORITY SCORING ENGINE

## Purpose

Prioritise actions by impact.

---

# Scoring Factors

| Factor | Purpose |
|---|---|
| Traffic potential | growth opportunity |
| Difficulty | implementation complexity |
| Confidence | probability of success |
| Revenue intent | commercial value |
| Resource cost | execution effort |

---

# Example Prioritisation

| Opportunity | Impact | Effort |
|---|---|---|
| Title refresh | High | Low |
| FAQ schema | Medium | Low |
| Intent split | Very High | Medium |
| Full rewrite | High | High |

---

# PRODUCTISED SERVICES

## GSC Opportunity Audit
Potential pricing:
- £300–£1,500

---

## AI Visibility Audit
Potential pricing:
- £500–£2,000

---

## CTR Optimisation Sprint
Monthly optimisation service.

---

## Search Intent Restructuring
High-ticket SEO consulting.

---

## Topical Authority Mapping
Enterprise SEO service.

---

# AUTOMATION IDEAS

## Suggested Automations

### Weekly
- query opportunity scans
- CTR drop alerts
- ranking movement detection

### Monthly
- freshness decay analysis
- AI citation analysis
- internal link opportunity updates

### Quarterly
- full content architecture review
- intent restructuring audit

---

# FUTURE EXPANSION IDEAS

## Advanced Features

- NLP semantic entity scoring
- competitor semantic modelling
- AI answer retrieval prediction
- local intent intelligence
- YouTube search opportunity mapping
- Reddit intent mining
- Google Discover opportunity analysis

---

# FINAL STRATEGIC POSITIONING

This system should position the agency as:

- Search Intelligence Partner
- AI Visibility Consultant
- SEO Diagnostics Specialist
- Organic Growth Strategist

The real value is not keyword discovery.

The real value is understanding:
- how Google interprets trust
- how intent shifts
- how freshness impacts visibility
- how AI systems retrieve content
- how to convert search signals into business growth

