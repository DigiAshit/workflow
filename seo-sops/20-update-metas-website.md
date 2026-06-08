# SOP: Implementing and Publishing Metas on Website

## 1. Document Control
- **ID**: dn-seo-sop-20
- **Version**: 2.0
- **Owner Role**: Junior SEO Specialist
- **Trigger**: Meta titles and descriptions draft is approved.
- **Inputs**: CMS credentials, approved Meta Creation sheet.
- **Outputs**: Approved metas live on client website.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to upload approved meta titles and descriptions to a client website. Publishing these metas ensures that search engines display the optimized titles and descriptions in search results.

---

## 3. Required Tools
- Website CMS (WordPress, Shopify, etc.)
- SEO Plugin (Yoast SEO or RankMath)
- Approved Meta Creation sheet

---

## 4. Step-by-Step Instructions
1. **Log into Website CMS**
   - Action: Log into the website admin panel using the credentials stored in LastPass.
   - Expected Result: The CMS dashboard loads.
2. **Navigate to Target Page**
   - Action: Go to the Pages list and open the editor for the target page.
   - Expected Result: The page editor dashboard loads.
3. **Locate SEO Meta Fields**
   - Action: Scroll down to the bottom of the editor to locate the Yoast SEO or RankMath metadata settings.
   - Expected Result: You see the input boxes for SEO Title and Meta Description.
4. **Copy and Paste Meta Title**
   - Action: Copy the approved meta title from the spreadsheet and paste it into the SEO Title input field.
   - Expected Result: The title is updated.
5. **Copy and Paste Meta Description**
   - Action: Copy the approved description and paste it into the Meta Description input field.
   - Expected Result: The description is updated.
6. **Save Changes**
   - Action: Click the Update or Save button on the page editor.
   - Expected Result: The settings are saved in the CMS.
7. **Verify Live Metas**
   - Action: Open the live website page, right click, select View Page Source, and search for the `<title>` and `<meta name="description">` tags.
   - Expected Result: The HTML code displays the new meta content.

---

## 5. Quality Control & Measurable Checks
- [ ] Correct meta title matches the spreadsheet exactly.
- [ ] Correct meta description matches the spreadsheet exactly.
- [ ] Changes saved and updated in CMS.
- [ ] Live page verified by checking the browser title and page source code.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| SEO plugin settings override manual inputs | Snippet variables (like %%title%%) are active | Delete the default snippet variables in the input fields before you paste the custom meta text. |
| Live source code shows old metas | Website caching is active | Clear the server cache and CDN cache (like Cloudflare), then reload the page source. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Updated with V2 Update Metas On Website Q/A checklist |
