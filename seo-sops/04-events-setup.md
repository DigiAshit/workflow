# SOP: Events Setup

## 1. Document Control
- **ID**: dn-seo-sop-04
- **Version**: 2.0
- **Owner Role**: Technical SEO Specialist
- **Trigger**: Website access and client onboarding setup are complete.
- **Inputs**: Website CMS credentials, Google Tag Manager container, Google Analytics 4 property, GSC profile.
- **Outputs**: Google Tag Manager code installed on site, conversion events tracking active.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to set up Google Tag Manager (GTM), Google Analytics 4 (GA4), and Google Search Console (GSC) on the client website. It also details how to set up tracking for phone calls, form submissions, and email link clicks. This allows us to track leads and show real return on investment to clients.

---

## 3. Required Tools
- Google Tag Manager
- Google Analytics 4
- Google Search Console
- Client Website CMS (WordPress, Shopify, etc.)

---

## 4. Step-by-Step Instructions
1. **Create GA4 and GTM Accounts**
   - Action: Create a new GTM container and a new GA4 property for the client.
   - Expected Result: GTM and GA4 accounts are created and configured.
2. **Install GTM Code on Website**
   - Action: Copy the GTM header and body scripts. Paste the header script into the head section of the website template. Paste the body script immediately after the opening body tag.
   - Expected Result: GTM script is visible in the website source code.
3. **Verify GTM Installation**
   - Action: Open GTM, click Preview, enter the website URL, and test the site connection.
   - Expected Result: Tag Assistant connects successfully and shows Tag Container Loaded.
4. **Link GA4 to GTM**
   - Action: Create a Google Tag inside GTM and insert the GA4 Measurement ID. Set the trigger to initialization on all pages.
   - Expected Result: GA4 page view events start tracking.
5. **Setup Click-to-Call Tracking**
   - Action: Create a GTM trigger for link clicks where the URL starts with `tel:`. Connect this trigger to a GA4 event tag named `phone_call_click`.
   - Expected Result: Phone number clicks fire the phone call event.
6. **Setup Click-to-Email Tracking**
   - Action: Create a GTM trigger for link clicks where the URL starts with `mailto:`. Connect this trigger to a GA4 event tag named `email_link_click`.
   - Expected Result: Email link clicks fire the email click event.
7. **Setup Form Submission Tracking**
   - Action: Identify the contact form selector on the website. Create a GTM trigger that fires on successful form submissions. Link this trigger to a GA4 event tag named `form_submission`.
   - Expected Result: Form submissions fire the form event.
8. **Setup CTA Click Tracking**
   - Action: Create a GTM click trigger targeting all main CTA buttons (like "Get Quote" or "Book Call"). Connect it to a GA4 event tag named `cta_click`.
   - Expected Result: Landing page CTA button clicks are logged.
9. **Test and Publish**
   - Action: Run a GTM preview session, submit a test form, click the phone number, and verify that the GA4 event tags fire. Publish the GTM container.
   - Expected Result: GTM changes are live.
10. **Mark Conversions in GA4**
   - Action: Open GA4 Admin, navigate to Events, and toggle the Mark as conversion switch for `phone_call_click`, `cta_click`, and `form_submission`.
   - Expected Result: GA4 tracks these events as conversions.

---

## 5. Quality Control & Measurable Checks
- [ ] Form submission tracked successfully in GTM and GA4.
- [ ] Phone click tracked successfully in GTM and GA4.
- [ ] Email click tracked successfully in GTM and GA4.
- [ ] CTA click tracked successfully in GTM and GA4.
- [ ] Conversion events created in GA4.
- [ ] Events tested and firing in GA4 debug view.
- [ ] Conversions tested and verified in GA4.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| GTM preview mode does not connect | Browser extension blocks the preview script | Turn off ad blockers or privacy extensions in your browser and try again. |
| Form submission event fires on failed submissions | Trigger is set to click instead of form submission | Change the trigger type to Form Submission and check the Check Validation box. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Updated with V2 Events Setup Q/A checklist |
