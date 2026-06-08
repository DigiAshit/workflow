# SOP: Monthly SEO Reporting QA & Distribution

## 1. Document Control
- **ID**: dn-seo-sop-29
- **Version**: 2.0
- **Owner Role**: Senior SEO Specialist
- **Trigger**: The monthly reporting cycle begins.
- **Inputs**: Google Search Console data, GA4 data, active keywords list, Zapier account login.
- **Outputs**: Verified client reports sent to clients and founders.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to verify monthly SEO reports. It covers coordinating with team members, managing Zapier automation rules, reviewing data accuracy, and sending reports to clients. This ensures that clients receive accurate performance data.

---

## 3. Required Tools
- Google Search Console
- Google Analytics 4
- Looker Studio
- Zapier
- Google Sheets (client project folder)

---

## 4. Step-by-Step Instructions
1. **Request Ads Reports**
   - Action: Send a message to Neil to ask for the Google Ads report data.
   - Expected Result: Neil sends you the Google Ads reports.
2. **Load Test Data**
   - Action: Open the reporting template and load the test data for each active project.
   - Expected Result: The test data displays in the draft reports.
3. **Check Indexing**
   - Action: Open Google Search Console and check the indexing status of all main pages for each project.
   - Expected Result: You confirm that all pages are correctly indexed.
4. **Access Zapier Settings**
   - Action: Log into the agency Zapier account.
   - Expected Result: The Zapier dashboard opens.
5. **Update Zapier Distribution**
   - Action: Remove the email address of Sagar from the active distribution zap.
   - Expected Result: Sagar will not receive draft reports.
6. **Set Review Email**
   - Action: Add the email address of Ashit in the target Google Sheet for receiving draft reports.
   - Expected Result: Draft reports are routed to Ashit.
7. **Test Navigation Buttons**
   - Action: Open the draft report link and click all navigation buttons.
   - Expected Result: Every button works and opens the correct page.
8. **Verify Report Dates**
   - Action: Check the dates displayed at the top of each report.
   - Expected Result: The report displays the correct calendar month.
9. **Verify Widget Data**
   - Action: Scan all charts and tables in the report.
   - Expected Result: All data widgets display numbers and contain no loading errors.
10. **Verify Current Month Metrics**
    - Action: Compare the current month data in the report with raw analytics numbers.
    - Expected Result: The numbers in the report match the raw analytics database.
11. **Review Account Analytics**
    - Action: Open the Google Analytics GA4 dashboard for each client account and check for tracking errors.
    - Expected Result: Analytics tracking is verified as active.
12. **Add Client Email**
    - Action: Open the report delivery Google Sheet and enter the email address of the client.
    - Expected Result: The client email is registered for report delivery.
13. **Restore Sagar Email**
    - Action: Log into Zapier and add the email address of Sagar back to the distribution list.
    - Expected Result: Sagar is restored to the final distribution list.

---

## 5. Quality Control & Measurable Checks
- [ ] Google Ads reports received from Neil.
- [ ] Website page indexing status verified in Search Console.
- [ ] Sagar email temporarily removed from Zapier.
- [ ] Ashit email added to the Google Sheet for testing.
- [ ] Report buttons and links verified.
- [ ] Report dates verified.
- [ ] Current month data display verified.
- [ ] Client email added to the sheet for final sending.
- [ ] Sagar email restored in Zapier.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Zapier does not send the draft report | Google Sheet triggers are inactive | Check the Zapier history, verify that the trigger row is updated, and restart the Zap. |
| Report displays error messages in widgets | Google account permissions expired | Log in again, open Looker Studio data sources, and reconnect the broken data source. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Initial draft from ClickUp V2 tasks |
