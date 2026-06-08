# SOP: Website Technical and CRO Fixes

## 1. Document Control
- **ID**: dn-seo-sop-16
- **Version**: 1.0
- **Owner Role**: Technical SEO Specialist / Web Developer
- **Trigger**: SEO Audit or Monthly Review identifies technical speed, mobile layout, or lead conversion issues.
- **Inputs**: CMS credentials, page speed recommendations, list of design changes.
- **Outputs**: Improved page loading speed, optimized mobile layout, prominent call conversion elements.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to implement technical fixes and conversion rate optimization (CRO) adjustments. These tasks improve mobile responsiveness, load times, and call-to-action visibility. This helps convert traffic into phone calls and enquiries.

---

## 3. Required Tools
- Website CMS (WordPress, custom theme, etc.)
- PageSpeed Insights tool
- Mobile responsiveness test tool

---

## 4. Step-by-Step Instructions
1. **Optimize Website Images**
   - Action: Install and run a compression tool (like Smush) to resize and compress large images.
   - Expected Result: Image sizes decrease with zero visual quality loss.
2. **Review Mobile Responsiveness**
   - Action: Open the client website on a mobile device. Check that all text is readable and no elements overlap.
   - Expected Result: The mobile design looks clean.
3. **Add Sticky Call Button**
   - Action: Add a floating click-to-call button to the mobile website navbar.
   - Expected Result: Mobile visitors see a phone icon that stays visible as they scroll.
4. **Insert Google Map Above Footer**
   - Action: Embed the client Google My Business map location directly above the website footer.
   - Expected Result: The GMB map is visible on all main pages.
5. **Optimize CTA Messaging**
   - Action: Update CTA button text from generic terms like "Enquire Now" to action-oriented copy (e.g. change to "Get Your Free Quote").
   - Expected Result: The buttons have clear, benefits-focused labels.
6. **Verify Contact Form Operation**
   - Action: Fill in and submit all contact forms on the website.
   - Expected Result: The form submits successfully and shows a success message.
7. **Test Loading Speed**
   - Action: Run PageSpeed Insights and verify that performance scores have improved.
   - Expected Result: Better loading times are logged.

---

## 5. Quality Control & Measurable Checks
- [ ] Large images compressed.
- [ ] Sticky call button visible and clickable on mobile devices.
- [ ] Embedded GMB map active.
- [ ] CTAs use benefits-focused copy.
- [ ] Test form submission completed successfully.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Mobile navbar elements overlap | CSS styles conflict with the new sticky call button | Adjust the padding and margins of the mobile navbar elements in the theme stylesheet. |
| Embedded map slows down the website | Map script loads before the main content | Configure the map embed script to lazy load, so it only loads when a user scrolls down. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 1.0 | Antigravity AI | Initial draft from ClickUp tasks |
