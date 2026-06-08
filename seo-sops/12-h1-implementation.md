# SOP: H1 Tags Optimization and Implementation

## 1. Document Control
- **ID**: dn-seo-sop-12
- **Version**: 2.0
- **Owner Role**: Technical SEO Specialist
- **Trigger**: SEO Audit identifies header structure issues.
- **Inputs**: Website CMS credentials, lists of pages with duplicate or missing H1 tags.
- **Outputs**: Corrected page header structure, unique H1 tag on each page.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to optimize and implement H1 headings on a client website. Correct heading usage improves keyword targeting and search visibility. It also improves content structure for human readers.

---

## 3. Required Tools
- Client Website CMS (WordPress, Shopify, etc.)
- Screaming Frog crawl list
- Page inspector (Chrome DevTools)

---

## 4. Step-by-Step Instructions
1. **Locate Target Page**
   - Action: Log into the website CMS, go to the page editor, and load a page that requires H1 fixes.
   - Expected Result: The page content editor is open.
2. **Review Header Structure**
   - Action: Inspect the page headings. Ensure there is exactly one H1 heading at the top of the page.
   - Expected Result: You locate duplicate or missing H1 elements.
3. **Format H1 Title**
   - Action: Rewrite the H1 title. It must include the primary page keyword and the target location (for local service pages). Make the title sound natural.
   - Expected Result: The H1 content is updated.
4. **Remove Extra H1 Tags**
   - Action: Locate any secondary headings that are formatted as H1. Change them to H2 or H3 format.
   - Expected Result: The page contains only one H1 tag.
5. **Save and Publish Changes**
   - Action: Click the Update or Publish button in the CMS dashboard.
   - Expected Result: The changes are saved on the website.
6. **Verify H1 in Browser**
   - Action: Open the live website page, right click the title, select Inspect, and check that the title is enclosed in an `<h1>` tag.
   - Expected Result: HTML inspection shows exactly one `<h1>` element.

---

## 5. Quality Control & Measurable Checks
- [ ] Exactly one H1 tag exists on the page.
- [ ] Primary keyword included in the H1 tag.
- [ ] Heading uses natural wording.
- [ ] H1 matches the page search intent.
- [ ] H1 tag is clearly visible on the page.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Theme automatically generates H1 and creates duplicate tags | The theme template has a built-in H1 title | Edit the theme template settings in the CMS to disable default page titles, or edit the theme file to remove the hardcoded heading. |
| Page title does not look good as an H1 | The font size is too large | Do not change the H1 tag format to H2. Instead, use website CSS styles to adjust the font size of the H1 tag to look correct. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Updated with V2 H1 Implement Q/A checklist |
