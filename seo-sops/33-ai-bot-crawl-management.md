# SOP: AI Bot Crawler Settings & Agent Indexing Setup

## 1. Document Control
- **ID**: dn-seo-sop-33
- **Version**: 2.0
- **Owner Role**: Senior SEO Specialist
- **Trigger**: Client requires AI search optimization setup.
- **Inputs**: Website root directory access, list of verified AI search bots.
- **Outputs**: llms.txt and agents.md uploaded, robots.txt bot rules updated and verified.

---

## 2. Purpose & Objectives
This Standard Operating Procedure explains how to manage AI crawler access and configure agent indexing files. We upload contextual text files and edit server permissions to help AI search engines crawl website content. This ensures that client websites rank in AI search summaries.

---

## 3. Required Tools
- Website hosting control panel (or FTP client)
- Text editor
- Google Search Console (to submit sitemaps)

---

## 4. Step-by-Step Instructions
1. **Access Server Root Directory**
   - Action: Log into the client website hosting panel and open the root folder.
   - Expected Result: You see the main website files.
2. **Create llms.txt File**
   - Action: Create a new plain text file in the root folder and name it exactly: `llms.txt`.
   - Expected Result: The empty `llms.txt` file is visible in the root directory.
3. **Add Website Summaries to llms.txt**
   - Action: Write a clear summary of the client business, services, and main page links inside the file.
   - Expected Result: The business information is saved in the file.
4. **Create agents.md File**
   - Action: Create a new markdown file in the root folder and name it exactly: `agents.md`.
   - Expected Result: The empty `agents.md` file is visible in the root directory.
5. **Add AI Guidelines to agents.md**
   - Action: Add structured brand facts, FAQ answers, and service details inside the file.
   - Expected Result: The AI agent context is saved.
6. **Open robots.txt File**
   - Action: Open the existing `robots.txt` file in the root folder using a text editor.
   - Expected Result: The text contents of the robots file load.
7. **Identify AI Bot Blocks**
   - Action: Scan the rules to check if any statement blocks crawlers like GPTBot or ClaudeBot.
   - Expected Result: You locate any blocked AI search crawlers.
8. **Update Robots Rules**
   - Action: Edit the rules to allow access for all verified AI search crawlers.
   - Expected Result: The robots file is updated with friendly crawl permissions.
9. **Verify live Links**
   - Action: Open a browser, enter the website address followed by `/llms.txt`, and check if it loads. Repeat this check for `/agents.md`.
   - Expected Result: Both files display correctly in the web browser.

---

## 5. Quality Control & Measurable Checks
- [ ] Access to root directory established.
- [ ] llms.txt file created in the root folder.
- [ ] agents.md file created in the root folder.
- [ ] llms.txt contains business summaries and key links.
- [ ] agents.md contains structured FAQs and brand details.
- [ ] robots.txt checked for bot blocks.
- [ ] Verified AI search crawlers allowed in robots.txt.
- [ ] Live URLs verified in a web browser.

---

## 6. Common Problems & Troubleshooting
| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| The browser displays a 404 error when loading the files | The files were uploaded to the wrong sub-folder | Move the files out of sub-folders and place them directly in the public root folder (like public_html). |
| AI search engines still block the crawl | Hosting firewall blocks the crawlers | Contact host support to white-list verified AI bot user agents in the server firewall rules. |

---

## 7. Version History
| Date | Version | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2026-06-08 | 2.0 | Antigravity AI | Initial draft from ClickUp V2 tasks |
