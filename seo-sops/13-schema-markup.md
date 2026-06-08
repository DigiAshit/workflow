# SOP: Schema Markup Creation & Validation

## 1. Document Control
- **ID**: dn-seo-sop-13
- **Version**: 2.0
- **Owner Role**: Technical SEO Specialist
- **Trigger**: Technical SEO implementation phase begins.
- **Inputs**: Client business address, phone number, primary keywords, Schema generation tools.
- **Outputs**: Validated JSON-LD schema code installed on client website.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to generate, validate, and install schema markup (structured data) on client websites. Structured data helps search engines understand the website content. It qualifies our clients for rich search results.

---

## 3. Required Tools
- Schema generator tool (e.g. Merkle Structured Data Generator)
- Schema Validator tool (validator.schema.org)
- Google Rich Results Test tool
- Website CMS (WordPress with header/footer plugin, etc.)

---

## 4. Step-by-Step Instructions
1. **Identify Required Schema Types**
   - Action: Review the website pages. Plan LocalBusiness and Organisation schema for the homepage, FAQ schema for FAQ sections, and Product schema for e-commerce pages.
   - Expected Result: You know which schema types are needed.
2. **Generate LocalBusiness Schema**
   - Action: Open the schema generator tool. Select LocalBusiness, then enter the client business name, address, phone number, website URL, and geo-coordinates.
   - Expected Result: The tool generates a JSON-LD code block.
3. **Generate FAQ Schema**
   - Action: Select FAQ schema in the generator. Copy the questions and answers from the website page and paste them into the generator fields.
   - Expected Result: FAQ JSON-LD code is generated.
4. **Validate Schema Code**
   - Action: Copy the generated JSON-LD code, open the Schema Validator tool, select Code Snippet test, paste the code, and click Test.
   - Expected Result: The test returns zero errors and zero warnings.
5. **Install Schema Code on Website**
   - Action: Log into the website CMS. Paste the validated JSON-LD schema script inside the header block of the target page.
   - Expected Result: Schema script is added to the page HTML code.
6. **Verify Live Schema Implementation**
   - Action: Copy the live page URL, open the Google Rich Results Test, paste the URL, and click Test URL.
   - Expected Result: The test confirms the structured data is detected and valid for rich results.

---

## 5. Quality Control & Measurable Checks
- [ ] Schema added to the correct page header.
- [ ] Live website page checked manually.
- [ ] No errors or warnings detected in Schema Validator.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| Validator shows missing field warning | Non-required fields were left blank in the generator | Fill in the missing fields (e.g. business hours or price range) and validate the code again. |
| Rich Results Test does not detect schema | Cache is active or script was pasted in the wrong place | Clear the website cache. Check that the script is in the page header template and verify the source code. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Updated with V2 Create Schema Q/A checklist |
