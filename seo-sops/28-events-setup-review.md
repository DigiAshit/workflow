# SOP: Events Setup Review

## 1. Document Control
- **ID**: dn-seo-sop-28
- **Version**: 1.0
- **Owner Role**: Technical SEO Specialist
- **Trigger**: Three days and one week after Events Setup task is completed.
- **Inputs**: Google Tag Manager container, Google Analytics 4 property, GSC profile.
- **Outputs**: Documented verification of active event tracking and GSC search query verification.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to review and verify event and conversion tracking settings after initial installation. It ensures that conversion data is flowing correctly into analytics and the domain remains verified in GSC.

---

## 3. Required Tools
- Google Tag Manager
- Google Analytics 4
- Google Search Console

---

## 4. Step-by-Step Instructions
1. **Review Data Configuration**
   - Action: Open Google Analytics 4 admin panel and check the events list settings. Verify that custom events are active.
   - Expected Result: The custom event tracking settings are correct.
2. **Check Analytics Active Data**
   - Action: Go to the Realtime report in GA4 and check if user events are tracking live. Check the historical events tab after three days.
   - Expected Result: You see user click data and conversion events in the reports.
3. **Verify Google Search Console Ownership**
   - Action: Open GSC, select the client property, and check the Settings panel to verify that the domain ownership verification remains active.
   - Expected Result: Ownership verification is active.
4. **Log Review Result**
   - Action: Add a comment in the ClickUp task with a screenshot of the GSC dashboard and GA4 events report.
   - Expected Result: Verification is documented.

---

## 5. Quality Control & Measurable Checks
- [ ] Custom tracking events and conversions are configured correctly.
- [ ] User click and conversion data is visible in the GA4 reports.
- [ ] GSC domain ownership verification is active.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| No conversion data shows in reports after three days | GTM container was not published or trigger was incorrect | Log into GTM, check for unpublished changes, run the preview debugger, verify tags fire on click, and publish the container. |
| GSC ownership verification failed | DNS records or verification tag was deleted | Ask the client developer to verify the GSC HTML tag remains in the website header or re-add the verification TXT record to the DNS settings. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 1.0 | Antigravity AI | Initial draft from V2 ClickUp task |
