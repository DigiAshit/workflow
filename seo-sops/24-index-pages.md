# SOP: Submitting Pages for Indexing

## 1. Document Control
- **ID**: dn-seo-sop-24
- **Version**: 1.0
- **Owner Role**: Junior SEO Specialist
- **Trigger**: Technical site changes or new content pages are published.
- **Inputs**: Live page URLs, Google Search Console access.
- **Outputs**: Index request submitted to Google Search Console.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to submit new and updated website pages to Google Search Console for indexing. Requesting indexing ensures Google crawls and indexes our changes quickly so pages can rank.

---

## 3. Required Tools
- Google Search Console
- Live page URLs list

---

## 4. Step-by-Step Instructions
1. **Copy Live URL**
   - Action: Open the updated webpage in your browser and copy the exact URL from the address bar.
   - Expected Result: You save the URL to your clipboard.
2. **Log into Google Search Console**
   - Action: Open Google Search Console and select the client website property.
   - Expected Result: The GSC dashboard loads.
3. **Inspect the URL**
   - Action: Paste the copied URL into the search box at the top of the GSC page and press Enter.
   - Expected Result: GSC retrieves index data and shows URL is not on Google or URL is on Google.
4. **Test Live URL**
   - Action: Click the Test Live URL button in the top right corner and wait for the test to complete.
   - Expected Result: The test confirms if the live URL can be indexed.
5. **Request Indexing**
   - Action: Click the Request Indexing link on the results panel.
   - Expected Result: A pop-up confirms that indexing was requested successfully.
6. **Update Sitemap**
   - Action: Go to the Sitemaps tab in GSC, select the active sitemap, and click Submit to refresh the crawl request.
   - Expected Result: GSC registers the sitemap update.

---

## 5. Quality Control & Measurable Checks
- [ ] Exact live URL inspected.
- [ ] Live URL test confirms page is crawlable.
- [ ] Indexing request submitted successfully.
- [ ] Sitemap submission confirmed.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Live test shows URL blocked by robots.txt | The robots.txt file contains a disallow rule | Open the website robots.txt file, locate the disallow rule blocking the page directory, and delete it. |
| Page contains noindex tag | The SEO plugin settings or page visibility settings are incorrect | Go to the page editor in the CMS, check the index settings, set to index, clear cache, and test again. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 1.0 | Antigravity AI | Initial draft from ClickUp tasks |
