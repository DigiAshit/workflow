---
name: seo-internal-linking-workflow
description: "Executes a systematic internal linking audit and opportunity mapping based on link position ratios, page classifications, semantic similarities, and a 12-tier priority matrix."
risk: safe
source: community
date_added: "2026-06-06"
---

# SEO Internal Linking Workflow (Agent Skill)

This skill directs a Claude/Antigravity agent to perform a complete, high-quality internal linking audit and opportunity analysis of a website. It replicates the exact algorithmic steps, scoring weightings, classification thresholds, and priority scales implemented in the core Node.js backend.

## Invocations & Activation Rules

- **Trigger:** When requested to "run an internal linking audit", "find link opportunities", "optimize site structure", or "generate internal linking suggestions for [URL]".
- **Inputs:** 
  - Required: Target website URL (or sitemap URL).
  - Optional: Specific focus page(s).

---

## Step-by-Step Execution Protocol

### Step 1: Crawling & Metadata Extraction
Analyze the sitemap or crawl the target website pages. For each page, extract:
1. **Basic Info:** URL, Title, Meta Description, canonical URL, and Robots meta tags.
2. **Body Text:** Extract H1s, word count, and main body content text.
3. **Links Inventory:** Gather all outgoing links (`<a>` tags) with:
   - Target URL (`href`)
   - Relationship attributes (`rel` like follow/nofollow)
   - Anchor Text
   - **DOM Position Ratio:** The 0-indexed position of the link divided by the total number of links on the page (`index / totalLinks`). This determines if the link lies in the header, body, or footer.

---

### Step 2: Link Audit & Inbound Power Calculation
Analyze the existing internal links pointing to each crawled page to compute its **Inbound Link Power Score**:
- For each incoming internal link, add a weight to the page's score based on its **DOM Position Ratio**:
  - **Header/Navbar Link (`ratio <= 0.15`):** Add **`0.2`** points.
  - **Footer Link (`ratio >= 0.85`):** Add **`0.1`** points.
  - **Main Content Link (`0.15 < ratio < 0.85`):** Add **`1.0`** point.
- **Orphan Detection:** Identify pages (excluding the homepage) that have `0` incoming links.

---

### Step 3: Page Classification
Once raw scores are computed for all pages:
1. **Identify the Range:** Find the minimum (`min`) and maximum (`max`) scores in the site's link graph.
2. **Normalize Scores:** Calculate the normalized score for each page:
   $$\text{normalizedScore} = \frac{\text{page.score} - \text{min}}{\text{max} - \text{min}}$$
   *(If all page scores are equal, set $\text{normalizedScore} = 0.5$)*.
3. **Categorize Pages:** Partition all pages into one of four classes:
   - **Orphan Pages:** Raw score is `0` (excluding homepage).
   - **Strong Pages:** `normalizedScore > 0.7`.
   - **Normal Pages:** `0.3 < normalizedScore <= 0.7`.
   - **Weak Pages:** `normalizedScore <= 0.3` (and raw score > `0`).

---

### Step 4: Semantic Opportunity Matching
Compare all pages to map matching opportunities:
1. **Skip Stop-Pages:** Exclude utility pages from source or target suggestions if their URL contains:
   - `contact`, `privacy`, `terms`, `policy`, `thankyou`, `refund`, `cookie`, `about`, `price`, `pricing`, `team`, `faq`, `faqs`, `testimonials`, `appointment`.
2. **Topic Similarity Filtering:** Estimate the semantic correlation between Page A (source) and Page B (destination) based on title, description, and core topical keywords. Match only if the estimated semantic overlap is high ($\ge 0.75$ similarity).
3. **Link Verification:** Ensure the source page does not already link to the target page.

---

### Step 5: Prioritization Mapping
Order the matched suggestions by their SEO significance using the following 12-tier priority matrix (where Priority 1 is the highest and Priority 12 is the lowest):

| Source Type | Target Type | Priority Value | SEO Strategy |
| :--- | :--- | :---: | :--- |
| **Strong** | **Orphan** | **1** | Top-tier donor page rescuing an unlinked page |
| **Normal** | **Orphan** | **2** | Mid-tier donor page rescuing an unlinked page |
| **Weak** | **Orphan** | **3** | Lower-tier donor page rescuing an unlinked page |
| **Strong** | **Weak** | **4** | Boosting low-performing pages with strong equity |
| **Normal** | **Weak** | **5** | Supporting low-performing pages with mid-tier equity |
| **Weak** | **Weak** | **6** | Semantic grouping of low-authority content |
| **Strong** | **Normal** | **7** | Pushing standard pages to high-performing status |
| **Normal** | **Normal** | **8** | Normal semantic cluster flow |
| **Weak** | **Normal** | **9** | Supporting standard pages with weak equity |
| **Strong** | **Strong** | **10** | Interlinking authority hubs |
| **Normal** | **Strong** | **11** | Funneling mid-tier pages to authority hubs |
| **Weak** | **Strong** | **12** | Funneling low-tier pages to authority hubs |

---

### Step 6: Editorial Anchor & Context Synthesis
For each recommended opportunity, generate a copy-paste ready insertion sentence that integrates the link seamlessly:
- **Anchor Text Guidelines:** Use partial-match, branded, or natural semantic variations. Never use repetitive exact-match anchors, and never use generic terms ("click here", "read more").
- **Contextual Sentence Guidelines:**
  - Must read naturally and sound human-written.
  - Must fit perfectly into the source page's topical flow.
  - Must introduce the destination page's core concept logically.
  - **Example:**
    - *Target:* `/seo-audit` (Topic: Technical SEO audit)
    - *Sentence:* "Before publishing new articles, running a detailed [technical SEO audit] ensures Google can find and index your content correctly."

---

## Output Format & Delivery

The final audit output must be returned as a markdown response containing:

1. **Link Recommendations Table:**
   | Source URL | Target URL | Anchor Text | Suggested Sentence | Priority (1-12) | Reason for Recommendation |
   | :--- | :--- | :--- | :--- | :---: | :--- |

2. **Quick Wins:** The top 3-5 recommendations from Priorities 1 to 4.
3. **Topic Cluster Gaps:** Missing semantic associations between closely related articles.
4. **Orphan Content:** List of pages with 0 internal links and their recommended donor pages.
5. **Anchor Diversity Suggestions:** Recommended anchor variations for target pages to prevent keyword over-optimization.
