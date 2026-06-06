---
name: seo-internal-linking-workflow
description: "Advanced semantic internal linking workflow that constructs a website knowledge graph, identifies 7 categories of linking opportunities, forces anchor diversity, creates editorial sentence additions, and scores suggestions across a multi-factor engine."
risk: safe
source: community
date_added: "2026-06-06"
---

# SEO Internal Linking Strategist Workflow (Agent Skill V2)

This skill directs a Claude/Antigravity agent to act as a Senior SEO Consultant performing a complete, large-scale internal linking audit and strategy design. The agent will move beyond basic exact-match keyword matching to construct a semantic topic model and evaluate user journeys, clusters, and page authority.

## Trigger & Invocation Rules
- **Activation:** Triggered when the user requests an "internal linking audit", "internal linking optimization", "silo structuring", "semantic link audit", or "link opportunity map" for a target URL.
- **Inputs:** 
  - Required: Website URL.
  - Optional: Sitemap URL, specific focus page URLs.

---

## Phase 1: Build Website Knowledge Graph

Before recommending links, the agent must build a comprehensive topical map of the website.

### 1. Crawl & Analyse
Extract the following elements from every crawled page (using browser, search, or document-reading capabilities):
- URL, Page Title, Meta Title.
- H1, H2, and H3 headers.
- Full body content (focusing on primary text and removing navigation/footer menus).
- Existing internal inbound/outbound links (including anchor text and position).

### 2. Build Topic Relationships
Do not rely on basic exact keyword matching. Map each page to:
- **Primary Topic:** The main subject matter (e.g., *Dental Implants*).
- **Secondary Topics:** Intersecting concepts (e.g., *Surgical Procedure*, *Local Dentist Services*).
- **Supporting Entities:** Sub-components (e.g., *Tooth extraction*, *bone grafting*, *implant care*, *implant failure*, *implant longevity*, *cavity treatment*).
- **Search Intent:** Informational, Navigational, Commercial, or Transactional.
- **Content Type:** Service landing page, blog post, about/doctor page, pricing, home.

---

## Phase 2: Identify Internal Link Opportunity Types

Group all discovered link opportunities into these 7 distinct categories:

### Category A: Money Page Opportunities
- **Purpose:** Support service and conversion landing pages.
- **Direction:** Informational blog posts → Transactional service pages.

### Category B: Topical Authority Opportunities
- **Purpose:** Strengthen topical coverage and establish topical depth.
- **Direction:** Supporting blog post → Parent topic blog post, or cross-silo informational matches.

### Category C: Content Cluster Opportunities
- **Purpose:** Reinforce semantic silos.
- **Direction:** Interlink articles within the same sub-topic cluster (e.g., linking *Dental Implant Benefits* ↔ *Dental Implant Care* ↔ *Signs You Need Implants*).

### Category D: Authority Flow Opportunities
- **Purpose:** Pass PageRank from high-authority pages to weaker or new content.
- **Action:** Identify pages with high existing incoming link counts or traffic signals, and recommend outbound links pointing to newly created or low-authority pages.

### Category E: Orphan Content Recovery
- **Purpose:** Identify pages with $\le 1$ incoming internal links.
- **Action:** Determine the most semantically relevant high-authority donor pages and recommend exact anchor text placement to rescue the orphan.

### Category F: User Journey Opportunities
- **Purpose:** Guide users down the conversion funnel.
- **Direction:** Map path flows: *Symptoms (Informational)* → *Causes (Informational)* → *Treatments (Commercial)* → *Service Page (Transactional)*.

### Category G: Location Opportunities (Local SEO)
- **Purpose:** Boost geographical relevance.
- **Direction:** Main service page → Location landing page, or Location page → Location-specific blog article.

---

## Phase 3: Improve Anchor Strategy

Strictly enforce **Anchor Diversity** to prevent Google keyword over-optimization penalties. Avoid using the same exact-match keyword repeatedly for the same target page.

### Anchor Diversity Rules:
- **Exact Match Limit:** Use the exact service term (e.g., "dental implants") no more than once or twice across the entire linking profile.
- **Partial-Match / Long-Tail:** Use contextual variations that describe the value.
- **Semantic Synonyms:** Link using related terms and descriptions.
- **Generic Ban:** Never use generic terms like "click here", "read more", or "learn more".

### Example Variations:
- *Target:* `/services/dental-implants`
  - **Do NOT repeat:** "dental implants", "dental implants"
  - **DO use:** `permanent tooth replacement`, `implant-supported restoration`, `replacing missing teeth`, `implant treatment options`, `long-term tooth replacement solution`.
- *Target:* `/services/periodontics`
  - **Do NOT repeat:** "gum disease", "gum disease"
  - **DO use:** `periodontal infection`, `early signs of gum disease`, `gum health concerns`, `advanced gum treatment`, `periodontal care options`.

---

## Phase 4: Improve Sentence Generation

Do not copy existing text or extract sentences verbatim from paragraphs. You must generate **new, editorial-quality insertion text** that reads naturally and integrates the anchor logically.

- **Editorial standard:** The sentence must read like a human content strategist wrote it to help the user.
- **Incorrect:** "If you're considering veneers, go to our service page."
- **Correct:** "Patients looking to enhance the appearance of their smile may also benefit from exploring the advantages of [professional veneer treatments]."

---

## Phase 5: Internal Link Scoring Engine

Score every suggestion on a scale of 0-100 across 4 distinct metrics:

1. **Relevance Score (0–100):** How closely related are the topics of the source and target page?
2. **SEO Impact Score (0–100):** Will this pass substantial link equity? (High if the source page has high inbound link counts).
3. **Conversion Value Score (0–100):** How close is this link to prompting a booking or transaction?
4. **Topical Authority Score (0–100):** Does this link complete or strengthen a topic cluster?

### Implementation Priority Assignment:
- **CRITICAL:** High relevance + Orphan page rescue (Priority 1-3).
- **HIGH:** High relevance + Money page support (Priority 4-6).
- **MEDIUM:** Topical cluster interlinking (Priority 7-9).
- **LOW:** General cross-silo linking or hub-to-hub links (Priority 10-12).

---

## Phase 6: Expand Recommendation Depth

Do not restrict suggestion counts. Surfacing more valid internal link recommendations is preferred:
- **100-page site:** 50 - 150 recommendations.
- **300-page site:** 150 - 500 recommendations.
- **1000-page site:** 500 - 2000 recommendations.
*Exclude only recommendations that are genuinely weak or irrelevant.*

---

## Phase 7: Output Structure

Return the audit findings structured as **7 separate reports**:

### Report 1: Money Page Opportunities
| Source URL | Target URL | Anchor Text | Suggested Sentence | Relevance | SEO Impact | Conversion | Topical | Priority |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |

### Report 2: Topical Authority Opportunities
*(Same column format as Report 1)*

### Report 3: Cluster Strengthening Opportunities
*(Same column format as Report 1)*

### Report 4: Authority Flow Opportunities
*(Same column format as Report 1)*

### Report 5: Orphan Page Opportunities
*(Same column format as Report 1)*

### Report 6: User Journey Opportunities
*(Same column format as Report 1)*

### Report 7: Quick Wins
Highlight the top 10 highest-scoring recommendations from the reports above, sorted by a composite priority score.
