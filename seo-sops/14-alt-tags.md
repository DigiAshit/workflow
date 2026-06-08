# SOP: Alt Image Tags Review & Optimization

## 1. Document Control
- **ID**: dn-seo-sop-14
- **Version**: 1.0
- **Owner Role**: Junior SEO Specialist
- **Trigger**: SEO audit identifies images missing alt text.
- **Inputs**: CMS credentials, Screaming Frog image crawl list, keyword sheet.
- **Outputs**: All target images updated with unique, keyword-optimized alt descriptions.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to write and update image alt text. Optimizing alt text helps search engines understand image content. It improves website image ranking and ensures accessibility for visually impaired users.

---

## 3. Required Tools
- Website CMS (WordPress media library, etc.)
- Screaming Frog crawl reports
- Target keyword sheet

---

## 4. Step-by-Step Instructions
1. **Identify Missing Alt Tags**
   - Action: Open the Screaming Frog image report and locate the list of image URLs missing alt text.
   - Expected Result: You have a target list of images.
2. **Log into Website Media Library**
   - Action: Log into the website CMS and open the Media Library dashboard.
   - Expected Result: The media library loads.
3. **Select Target Image**
   - Action: Find and click the target image from your checklist to open its details.
   - Expected Result: The attachment details panel appears.
4. **Draft Alt Text**
   - Action: Write a clear description of what the image shows. Include the target page keyword naturally. Do not stuff keywords.
   - Expected Result: A descriptive alt text is written.
5. **Save Alt Text**
   - Action: Paste the written alt text into the Alt Text input field. Click Save or let it auto-save.
   - Expected Result: The alt tag is saved.
6. **Repeat for Other Images**
   - Action: Repeat steps three to five for all images on the target page.
   - Expected Result: All images on the page have descriptive alt text.

---

## 5. Quality Control & Measurable Checks
- [ ] Descriptive alt text added to all main images.
- [ ] Primary page keyword included naturally in at least one main image.
- [ ] No keyword stuffing present in alt text.
- [ ] Decorative images (like icons or lines) left blank or given null alt attributes.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Cannot locate the image in the library | The image is hardcoded in theme files | Open the theme template editor, find the image HTML tag, and insert `alt="description"` manually. |
| Alt text does not show up on the page | Page caching is active | Clear the website cache and reload the page. Inspect the image HTML element to verify. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 1.0 | Antigravity AI | Initial draft from ClickUp tasks |
