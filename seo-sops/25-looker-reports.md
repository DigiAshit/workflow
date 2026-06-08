# SOP: Creating SEO & GMB Reports on Looker Studio

## 1. Document Control
- **ID**: dn-seo-sop-25
- **Version**: 2.0
- **Owner Role**: SEO Specialist
- **Trigger**: The monthly reporting cycle begins.
- **Inputs**: Google Search Console access, GA4 access, Google My Business access, Digital Neighbour Looker Studio Template.
- **Outputs**: Completed Looker Studio report link shared in the reports sheet.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to create monthly reports on Looker Studio. It links client data sources to show ranking progress, website traffic, GMB calls, and leads. This gives the client a clear view of campaign performance.

---

## 3. Required Tools
- Looker Studio
- Google Analytics 4, GSC, and GMB access
- Google Sheets (client project folder)

---

## 4. Step-by-Step Instructions
1. **Copy Report Template**
   - Action: Open the Digital Neighbour Looker Studio Master Template, click the three dots, and select Make a copy.
   - Expected Result: A new copy of the template is created.
2. **Connect Google Search Console**
   - Action: Under data sources, connect the new GSC property for the client website. Select URL Impression data.
   - Expected Result: GSC data loads in the report widgets.
3. **Connect Google Analytics 4**
   - Action: Add a new data source, select GA4, and choose the client property.
   - Expected Result: Website visitor traffic data is linked.
4. **Connect Google My Business**
   - Action: Add a new data source, select the Google My Business connector, and choose the client listing.
   - Expected Result: Local map search and call click data is linked.
5. **Rename Report**
   - Action: Change the report title to exactly match the format: `[Client Brand Name], Monthly Growth Report`.
   - Expected Result: The report has the correct name.
6. **Set Report Branding**
   - Action: Update the report logo and theme colors to match the client branding.
   - Expected Result: The report looks professional.
7. **Verify Conversion Data**
   - Action: Check the GA4 scorecard widget to verify that tracked events (like form submissions) match the analytics account data.
   - Expected Result: Conversion numbers are correct.
8. **Verify Keyword Tracking**
   - Action: Verify that the keyword tracking integration displays correct ranking shifts.
   - Expected Result: Ranking data is correct.

---

## 5. Quality Control & Measurable Checks
- [ ] Google Search Console data source connected.
- [ ] Google Analytics 4 data source connected.
- [ ] Google My Business data source connected.
- [ ] Keyword tracking data source connected and verified.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Looker Studio widgets display error messages | The connected data sources lost authorization | Click Manage added data sources, select Edit on the broken source, re-verify your Google account, and click Reconnect. |
| Report shows zero traffic | The wrong GA4 property or view was selected | Open the data source settings, verify the GA4 property ID matches the client account, and update the selection. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Updated with V2 Create Reports Q/A checklist |
