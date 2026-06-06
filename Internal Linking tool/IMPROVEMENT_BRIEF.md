# Master Improvement Brief: Internal Linking Workflow (V2)

This document contains the design requirements and objectives for shifting the **Internal Linking Workflow** from a simple exact-match keyword matching tool into a comprehensive, strategist-level SEO audit process.

---

## 1. Problem Statement
The V1 workflow generated suggestions based primarily on exact-match keywords, blog-to-service page link models, and automated regex matching. On a typical 300+ page website, this keyword-centric behavior leaves a large percentage of internal link opportunities unexploited.

To act like a senior SEO consultant, the workflow must look past basic exact keywords and build a semantic topic map to establish conversion paths, topical authority, silo structures, and authority flow.

---

## 2. Master Directives

### A. Semantic Knowledge Graph & Topic Mapping
- Extract page URL, title, meta tag, H1-H3 headers, and body content.
- Do not rely on plain keyword matches. Map pages to primary/secondary topics and supporting entities (e.g. mapping "Dental Implants" to "Missing Tooth", "Implant Failure", "Bone Grafting", "Tooth Extraction", and "Implant Care").

### B. Distinct Opportunity Categories
The strategy should map links across 7 distinct categories:
1. **Category A: Money Page Opportunities** (supporting conversion, Blog → Service, Informational → Transactional).
2. **Category B: Topical Authority Opportunities** (Blog → Blog, Supporting → Parent, Parent → Supporting).
3. **Category C: Content Cluster Opportunities** (interlinking pages within a specific semantic silo, e.g. Benefits ↔ Care ↔ Signs ↔ Replacement Options).
4. **Category D: Authority Flow Opportunities** (mapping high PageRank pages to support weaker, deeper content).
5. **Category E: Orphan Content Recovery** (finding pages with $\le 1$ incoming links and linking to them from strong context positions).
6. **Category F: User Journey Opportunities** (mapping informational flows, e.g. Symptoms → Causes → Treatment → Service Page).
7. **Category G: Location Opportunities** (for Local SEO: Service Page ↔ Location Page, Location Page ↔ Relevant Blog).

### C. Mandatory Anchor Diversity
Prevent keyword over-optimization penalties (e.g., repeating "dental implants" endlessly) by forcing semantic variations:
- *Standard:* "dental implants"
- *V2 Anchors:* "permanent tooth replacement", "implant-supported restoration", "replacing missing teeth", "implant treatment options", "long-term tooth replacement solution".
- *Standard:* "gum disease"
- *V2 Anchors:* "periodontal infection", "early signs of gum disease", "gum health concerns", "advanced gum treatment", "periodontal care options".

### D. Human-Quality Editorial Sentence Insertion
- Do not copy-paste adjacent sentences.
- Craft new, context-rich, copy-ready paragraphs that read naturally and add actual editorial value to the page content.
- *Good Example:* "Patients looking to enhance the appearance of their smile may also benefit from exploring the advantages of professional veneer treatments."

### E. Multi-Factor Scoring Engine
Every recommended link must be scored on a scale of `0-100` across 4 dimensions (0-100) and assigned an Implementation Priority:
- **Relevance Score:** How closely aligned are the two pages?
- **SEO Impact Score:** How much authority/ranking power will this link pass?
- **Conversion Value Score:** Does it guide users closer to a transaction?
- **Topical Authority Score:** Does it strengthen the content cluster?
- **Implementation Priority:** Critical, High, Medium, Low.

### F. Deep Recommendation Output
Do not artificially cap suggestions. Uncover all valid connections:
- **100-page site:** 50 - 150 recommendations
- **300-page site:** 150 - 500 recommendations
- **1000-page site:** 500 - 2000 recommendations

### G. 7 Separate Structured Reports
Group and return opportunities in separate, readable tables:
1. Money Page Opportunities
2. Topical Authority Opportunities
3. Cluster Strengthening Opportunities
4. Authority Flow Opportunities
5. Orphan Page Opportunities
6. User Journey Opportunities
7. Quick Wins (highest impact)
