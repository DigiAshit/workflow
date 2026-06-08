# SOP: Adding Location in URLs & Redirect Strategy

## 1. Document Control
- **ID**: dn-seo-sop-15
- **Version**: 1.0
- **Owner Role**: Technical SEO Specialist
- **Trigger**: Strategy requires target location keywords in service page URLs.
- **Inputs**: Website CMS credentials, target keyword list, redirection plugin (e.g. Redirection for WordPress).
- **Outputs**: Updated URL structures, active 301 redirects from old URLs.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to add location keywords to page URLs. It also explains how to set up 301 redirects from old URLs to the new ones. This protects existing rankings and prevents 404 page errors.

---

## 3. Required Tools
- Website CMS (WordPress, Shopify, etc.)
- WordPress Redirection Plugin (or `.htaccess` access)
- Redirect checker tool

---

## 4. Step-by-Step Instructions
1. **Define New URL Structure**
   - Action: Select the target page. Plan the new URL slug to include the target location keyword (e.g. change `/car-repairs/` to `/car-repairs-christchurch/`).
   - Expected Result: The new URL slug is defined.
2. **Copy Old URL**
   - Action: Open the target page on the live website and copy the exact URL link.
   - Expected Result: You save the old URL.
3. **Change URL Slug in CMS**
   - Action: Log into the website CMS, open the page editor, find the permalink setting, update the slug, and click Update.
   - Expected Result: The page URL changes to the new version.
4. **Create 301 Redirect**
   - Action: Open the redirection plugin dashboard. Enter the old URL as the Source URL and the new URL as the Target URL. Click Add Redirect.
   - Expected Result: A 301 redirect rule is created.
5. **Verify Redirect Operation**
   - Action: Open a new incognito browser tab, enter the old page URL, and press Enter.
   - Expected Result: The browser automatically loads the new page URL.
6. **Check Redirect Code**
   - Action: Enter the old URL in a redirect checker tool and verify that the server returns a `301 Moved Permanently` status.
   - Expected Result: The redirect status code is verified as 301.

---

## 5. Quality Control & Measurable Checks
- [ ] New URL contains the primary keyword and location.
- [ ] Incognito test confirms redirect works.
- [ ] Redirect checker confirms redirect code is 301.
- [ ] No duplicate pages are created.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Redirect loop error | The old URL redirects to the new one, but the new one redirects back to the old one | Open the redirection plugin dashboard. Check the settings and delete duplicate or circular redirection rules. |
| Page returns a 404 error | Redirect rule has a typo or was not saved | Double check the source and target URLs in the redirection tool and resave the rule. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 1.0 | Antigravity AI | Initial draft from ClickUp tasks |
