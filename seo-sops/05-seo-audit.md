# SOP: Technical & On-Page SEO Audit

## 1. Document Control
- **ID**: dn-seo-sop-05
- **Version**: 2.0
- **Owner Role**: Senior SEO Specialist
- **Trigger**: Client onboarding and tracking setup are complete.
- **Inputs**: Website URL, Screaming Frog software, Google Search Console data.
- **Outputs**: Raw audit data, list of technical issues, competitor analysis report.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to audit a website using Screaming Frog and other analysis tools. It helps identify broken links, crawl issues, duplicate content, and slow loading pages. This audit forms the foundation of our SEO campaign.

---

## 3. Required Tools
- Screaming Frog SEO Spider
- Google Search Console
- Ahrefs (or SEMrush)
- PageSpeed Insights

---

## 4. Step-by-Step Instructions
1. **Configure Screaming Frog**
   - Action: Open Screaming Frog. Connect the Google Search Console API and Google Analytics API in the configuration settings.
   - Expected Result: API connections are active and verified.
2. **Start Website Crawl**
   - Action: Enter the client website URL in the address bar and click Start.
   - Expected Result: Screaming Frog crawls the website and the progress bar reaches one hundred percent.
3. **Identify Redirect and Broken Links**
   - Action: Go to the Response Codes tab. Filter for 4xx errors to find broken links and 3xx codes to find redirects. Export the data.
   - Expected Result: You have a spreadsheet listing all broken URLs and redirect chains.
4. **Identify Meta Title and Description Errors**
   - Action: Go to the Page Titles tab. Filter for missing titles, duplicate titles, and titles over sixty characters. Repeat the process on the Meta Description tab for descriptions over one hundred and sixty characters.
   - Expected Result: You have a list of all pages needing meta updates.
5. **Check Heading Structure**
   - Action: Go to the H1 tab. Filter for pages with missing H1 tags, multiple H1 tags, or duplicate H1 tags.
   - Expected Result: You locate heading structure errors.
6. **Analyze Image Sizes and Alt Text**
   - Action: Go to the Images tab. Filter for images over one hundred kilobytes and images missing alt text.
   - Expected Result: You have a list of images that need optimization.
7. **Test Website Loading Speed**
   - Action: Open PageSpeed Insights, enter the website URL, and run the test. Record the mobile performance score.
   - Expected Result: Core Web Vitals performance data is captured.
8. **Conduct Competitor SEO Review**
   - Action: Enter the top three competitor URLs in Ahrefs. Document their domain ratings, top keywords, and backlink counts.
   - Expected Result: Competitor strength metrics are saved in the audit notes.
9. **Review Social Media Presence**
   - Action: Check the client Facebook, LinkedIn, Instagram, and other social media pages. Ensure their business name, address, phone number, and email match the website exactly.
   - Expected Result: Social profiles consistency review is complete.

---

## 5. Quality Control & Measurable Checks
- [ ] Crawl completed successfully in Screaming Frog.
- [ ] Broken links identified and logged.
- [ ] Redirect issues identified and logged.
- [ ] Canonical issues identified and logged.
- [ ] Indexation issues identified and logged.
- [ ] XML sitemap reviewed and checked.
- [ ] Robots.txt reviewed and checked.
- [ ] Top 3 competitors reviewed.
- [ ] Competitor strengths documented.
- [ ] Gap opportunities documented.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Crawl stops early or website blocks crawler | Website firewall blocks Screaming Frog | Change the User-Agent setting in Screaming Frog to Googlebot and set the limit to one request per second. |
| Search Console API does not connect | You are logged into the wrong Google account | Verify that the active Google account has full access permissions for the client GSC property. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Updated with V2 SEO Audit Q/A checklist and social media review |
