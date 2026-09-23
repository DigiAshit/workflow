# Reusable Facebook / Meta Ads Strategy Workflow

**Version:** 1.0  
**Platform:** Facebook and Instagram (Meta Ads)  
**Purpose:** Convert arbitrary project details and an offer into a complete, evidence-aware campaign strategy, creative production pack, lead journey, and controlled testing plan.

---

# 1. Workflow Objective

Use this workflow when a user supplies project context, an offer, or both and wants a complete Meta Ads strategy.

The workflow must produce:

- People, Pain, Process, and Offer variable banks
- Campaign and ad-set architecture
- Hooks, proof angles, objections, and CTAs
- Graphic ad concepts and production-ready briefs
- Video ad concepts, shot lists, and scripts
- Primary text, headlines, and descriptions
- Lead-form structure and qualification logic
- Retargeting and exclusion strategy
- Speed-to-lead and follow-up sequences
- A one-variable-at-a-time testing matrix
- KPI definitions, measurement requirements, and iteration rules

The workflow creates a strategy and production brief. It does not publish ads, generate unsupported claims, or substitute assumptions for missing business information.

---

# 2. Non-Negotiable Operating Principles

## 2.1 The Core Message Model

Build every ad from four controllable components:

```text
PEOPLE -> PAIN -> PROCESS -> OFFER
```

- **People:** Who the message is for and the situation that identifies them.
- **Pain:** The functional, financial, emotional, or decision problem they recognize.
- **Process:** How the business solves the problem or delivers a better experience.
- **Offer:** What the prospect receives, why it is valuable, and what to do next.

The ad message is an audience signal. Specific language should help the intended prospect recognize themselves without inventing targeting attributes or making prohibited personal-attribute assertions.

## 2.2 One Variable at a Time

Every experiment must have:

- One declared independent variable
- One control
- One or more variants
- All non-tested variables held constant
- A primary success metric
- A minimum data rule or decision window
- A documented outcome and next action

Never label a comparison as a valid test if it simultaneously changes the hook, pain, format, offer, CTA, and audience.

## 2.3 Evidence Before Claims

Only use a fact, number, deadline, guarantee, testimonial, accreditation, price, discount, or performance claim when the input includes verifiable support.

If support is absent, use an explicit placeholder:

```text
[PROOF REQUIRED]
[CONFIRM PRICE]
[CONFIRM DEADLINE]
[CONFIRM WARRANTY TERMS]
[CUSTOMER QUOTE REQUIRED]
[INPUT REQUIRED: describe missing information]
```

Do not turn a missing fact into persuasive copy.

## 2.4 Offers Before Discounts

Consider assessment, convenience, value-add, and risk-reduction offers before recommending a discount. A discount is valid only when supplied or approved and commercially sustainable.

## 2.5 Human-Led Creative by Default

When appropriate to the brand and available assets, prioritize real owners, staff, customers, products, locations, and project footage over generic stock imagery. If those assets are unavailable, specify what must be captured; do not claim they exist.

## 2.6 Policy and Human Review

Flag, but do not attempt to provide legal advice for:

- Regulated industries
- Credit, housing, employment, health, politics, or social issues
- Personal attributes and sensitive targeting
- Before/after claims
- Financial or health outcomes
- Testimonials, guarantees, contests, and limited-time promotions

Require a human review of current Meta policies, local law, landing-page claims, consent language, and offer terms before launch.

---

# 3. Input Contract

Accept free-form project information, but normalize it into this schema before strategy generation.

## 3.1 Project and Business

```text
project_name:
business_name:
website:
business_type:
primary_service_or_product:
secondary_services_or_products:
location_or_service_area:
service_radius_or_delivery_area:
primary_campaign_goal:
conversion_action:
average_customer_or_order_value:
gross_margin_or_allowable_acquisition_cost:
sales_capacity:
campaign_dates:
budget_daily_or_monthly:
```

## 3.2 Audience

```text
primary_customer:
secondary_customer:
customer_context_or_trigger:
awareness_stage:
known_pains:
desired_outcomes:
common_objections:
qualification_requirements:
disqualifiers:
languages:
geographic_constraints:
existing_customer_data:
```

## 3.3 Offer

```text
core_service_or_product:
entry_offer:
deliverables:
price_or_price_positioning:
value_add:
bonus:
risk_reversal:
guarantee_or_warranty:
urgency_reason:
deadline:
real_capacity_limit:
terms_and_conditions:
primary_cta:
destination_url_or_lead_form:
```

## 3.4 Differentiation and Proof

```text
key_differentiators:
delivery_process:
response_time:
pricing_process:
credentials:
years_in_business:
customer_count:
ratings_and_review_sources:
approved_testimonials:
case_studies:
measured_results:
warranties_or_guarantees:
competitor_or_alternative_context:
```

## 3.5 Funnel and Operations

```text
landing_page:
lead_form_type:
crm:
booking_method:
sales_process:
speed_to_lead_target:
follow_up_channels:
follow_up_owner:
operating_hours:
privacy_policy_url:
tracking_status:
pixel_and_capi_status:
primary_conversion_event:
historical_conversion_rates:
historical_campaign_results:
```

## 3.6 Brand, Creative, and Compliance

```text
brand_voice:
brand_guidelines:
mandatory_wording:
prohibited_wording:
legal_disclaimers:
industry_constraints:
available_people_on_camera:
available_customer_permissions:
available_photos:
available_video:
available_product_or_project_footage:
available_logos_and_fonts:
creative_formats_available:
```

---

# 4. Input Validation and Assumption Policy

## Step 4.1 - Build the Input Ledger

Classify every important field as:

| Status | Meaning | Required treatment |
|---|---|---|
| Confirmed | Explicitly supplied by the user or a cited source | May be used as written |
| Derived | Logically calculated from confirmed inputs | Show the calculation |
| Proposed | A strategic recommendation, not a business fact | Label as proposed |
| Missing | Not supplied | Preserve as a placeholder |
| Conflicting | Inputs disagree | Surface the conflict; do not select silently |

## Step 4.2 - Apply the No-Invention Rule

Continue when information is missing, but:

1. State the missing input.
2. Explain which output it affects.
3. Use a clearly named placeholder.
4. Avoid false specificity.
5. Add the item to the final `Open Inputs and Approvals` list.

## Step 4.3 - Minimum Viable Input Gate

The workflow may generate a useful draft when these are known:

- What is being promoted
- Who it is for, even provisionally
- What action the campaign should generate
- What the offer is, or permission to propose offer options

If any is absent, create a framework-only strategy with `[INPUT REQUIRED]` fields rather than a project-specific strategy.

---

# 5. Phase 1 - Strategic Foundation

## Step 5.1 - Write the Campaign Thesis

Complete:

```text
We will reach [PEOPLE] who are experiencing [PAIN OR TRIGGER],
show that [BUSINESS] uses [PROCESS DIFFERENTIATOR],
and invite them to claim [OFFER] by [CTA].
```

## Step 5.2 - Define the Conversion Economics

Use supplied values only.

```text
Target CPL = [INPUT OR DERIVED VALUE]
Lead-to-appointment rate = [INPUT REQUIRED if missing]
Appointment-to-sale rate = [INPUT REQUIRED if missing]
Lead-to-sale rate = lead-to-appointment rate x appointment-to-sale rate
Allowable CAC = [INPUT OR DERIVED VALUE]
Derived maximum CPL = allowable CAC x lead-to-sale rate
Target ROAS = revenue attributed to ads / ad spend
```

Label benchmarks as `provisional planning thresholds` unless they come from the project's historical data.

## Step 5.3 - Choose Funnel Type

Recommend one primary path and explain why:

```text
Ad -> Instant Form -> Confirmation -> Contact -> Appointment/Sale
Ad -> Landing Page -> Form/Checkout -> Confirmation -> Follow-up
Ad -> Messenger/WhatsApp -> Qualification -> Appointment/Sale
Ad -> Call -> Qualification -> Appointment/Sale
```

Do not assume a channel exists merely because it would be useful.

---

# 6. Phase 2 - People Variable Bank

Define who should self-identify with the ad.

## People Dimensions

```text
PPL-01 Geography:
PPL-02 Customer type or role:
PPL-03 Property, business, or use-case type:
PPL-04 Trigger event:
PPL-05 Current situation:
PPL-06 Intent signal:
PPL-07 Qualification signal:
PPL-08 Awareness stage:
```

Generate 3-8 distinct People angles using only supported attributes. For each:

| Field | Required output |
|---|---|
| ID | `PPL-01`, `PPL-02`, etc. |
| Segment | Plain-language description |
| Self-identification line | A policy-aware callout |
| Trigger | Why the message is timely |
| Desired outcome | What this person wants |
| Qualification | Who is and is not a fit |
| Evidence | Confirmed input or `Proposed` |

Avoid wording that asserts a sensitive personal attribute. Prefer contextual phrasing such as `Planning a home renovation?` rather than an unsupported or sensitive assertion about the viewer.

---

# 7. Phase 3 - Pain Variable Bank

Map pains into separate testable angles.

## Pain Categories

- **Functional:** failure, delay, low performance, complexity, recurring issue
- **Financial:** waste, repeated cost, lost revenue, uncertainty about price
- **Emotional:** frustration, stress, inconvenience, lack of confidence
- **Decision:** repair or replace, which option, whom to trust, when to act
- **Prior experience:** poor communication, hidden costs, missed appointments, weak workmanship
- **Consequence:** what plausibly happens if the supported issue is left unresolved

For each pain produce:

```text
Pain ID: PAI-[NN]
Category:
Customer-language statement:
Observable symptom:
Underlying concern:
Desired resolution:
Evidence source:
Safe claim boundary:
```

Generate 4-8 pains. Do not combine them into one variant during the first pain test.

---

# 8. Phase 4 - Process and Differentiation Bank

Market the service experience as well as the product or outcome.

Evaluate:

```text
How enquiries are handled
How qualification or assessment works
How options are explained
How pricing is communicated
Who the customer deals with
How long each stage takes
What happens during delivery
What happens after delivery
How problems are resolved
What warranties, guarantees, or safeguards apply
```

Group valid differentiators as:

- **More personal** - named contact, owner involvement, tailored recommendation
- **Faster or easier** - response speed, booking convenience, turnaround
- **More transparent** - written scope, pricing clarity, clear options
- **Less risky** - verified warranty, credential, guarantee, documentation
- **More complete** - end-to-end delivery, aftercare, support

For each process angle:

```text
Process ID: PRC-[NN]
Feature:
Customer benefit:
Contrast with the common frustration:
Proof required:
Claim status: Confirmed / Proposed / Missing
```

Never present a proposed process improvement as an existing business capability.

---

# 9. Phase 5 - Proof and Review Mining

## Step 9.1 - Build a Proof Ladder

Use the strongest available evidence in this order, while considering relevance:

1. Measured project or customer outcome
2. Verifiable case study
3. Approved customer testimonial
4. Rating and review volume with source
5. Credential, licence, award, or warranty
6. Demonstration of the process or product
7. Specific explanation of how the process works

## Step 9.2 - Mine Reviews When Provided

Cluster repeated themes such as:

```text
Communication
Speed
Professionalism
Cleanliness
Clarity
Reliability
Value
Quality
Problem solving
Aftercare
```

For every theme output the source, frequency if calculable, representative wording, and marketing implication. Do not fabricate review language or counts.

## Step 9.3 - Create Proof Variables

```text
Proof ID: PRO-[NN]
Proof type:
Exact approved fact or placeholder:
Source:
Best placement in ad:
Required disclaimer or permission:
```

---

# 10. Phase 6 - Offer Architecture

Normalize the supplied offer and, when requested, propose alternatives.

```text
Core service/product:
Entry mechanism:
What the prospect receives:
Price or commercial terms:
Value add:
Bonus:
Risk reversal:
Urgency reason:
Deadline:
Capacity limit:
Eligibility:
Exclusions:
CTA:
Destination:
```

## Offer Categories to Consider

- Assessment: consultation, inspection, quote, audit
- Value add: upgrade, maintenance, additional deliverable, aftercare
- Convenience: priority booking, simpler setup, faster response
- Risk reduction: no-obligation review, written options, transparent proposal
- Bundle: complementary products or services
- Promotion: verified price reduction or limited-time terms

For each offer variant:

```text
Offer ID: OFF-[NN]
Offer statement:
Best-fit audience:
Value logic:
Qualification effect:
Operational cost or constraint:
Evidence/approval needed:
Lead-quality risk:
```

Urgency and scarcity must be real. If absent, omit them.

---

# 11. Phase 7 - Hooks, Objections, and CTAs

## Hook Bank

Create at least one supported hook for each relevant category:

```text
H-01 Geographic or community context
H-02 Situation or trigger
H-03 Pain
H-04 Decision question
H-05 Consequence
H-06 Cost or waste
H-07 Trust or transparency
H-08 Comparison or alternative
H-09 Education or misconception
H-10 Offer
```

For every hook include:

- Hook text
- Intended People and Pain IDs
- Awareness stage
- Claim or policy risk
- Recommended opening visual

## Objection Bank

Create responses only from confirmed information:

```text
OBJ-01 Price or value
OBJ-02 Trust
OBJ-03 Timing
OBJ-04 Effort or disruption
OBJ-05 Fit
OBJ-06 Risk
```

## CTA Bank

Generate 3-6 CTAs aligned to the actual next step:

```text
CTA-01 Low commitment
CTA-02 Direct response
CTA-03 Booking
CTA-04 Learn/compare
CTA-05 Message/call
```

Do not promise instant booking, same-day response, or availability unless confirmed.

---

# 12. Phase 8 - Campaign Architecture

Recommend a structure appropriate to budget, geography, funnel, data volume, and operational capacity.

## Required Output

```text
Campaign objective:
Conversion location:
Optimization event:
Attribution setting: [INPUT/PLATFORM REVIEW REQUIRED]
Budget approach:
Geography:
Placements:
Audience approach:
Exclusions:
Retargeting split:
Creative count:
```

## Naming Convention

```text
Campaign: META_[OBJECTIVE]_[PEOPLE]_[OFFER]_[YYYY-MM]
Ad set: AS_[AUDIENCE]_[GEO]_[OPTIMIZATION]
Ad: [H]-[PPL]-[PAI]-[PRC]-[OFF]-[PRO]-[CTA]-[CR]
```

Example syntax only:

```text
H-02_PPL-01_PAI-03_PRC-02_OFF-01_PRO-01_CTA-02_CR-VID01
```

Avoid unnecessary audience fragmentation. Label every platform-dependent setting for confirmation in the current Meta interface before launch.

---

# 13. Phase 9 - Graphic Creative Production Pack

Generate 4-8 concepts suited to the supplied assets and offer. If an asset does not exist, write `Capture required` or `Asset required`.

## Recommended Concept Types

- Real person plus direct promise
- Problem/symptom visual
- Before/after, only with permission and substantiation
- Process in three steps
- Review or proof card
- FAQ or decision graphic
- Offer card
- Product or project demonstration

## Brief Template for Every Graphic

```text
Creative ID: CR-IMG[NN]
Concept name:
Test variable:
Target People ID:
Pain ID:
Process ID:
Offer ID:
Proof ID:
CTA ID:
Placement/aspect ratio:
Primary visual:
Asset source or capture requirement:
On-image headline:
Supporting line:
CTA treatment:
Brand treatment:
Composition and hierarchy:
Accessibility/legibility notes:
Required disclaimer:
Designer handoff notes:
Do-not-use notes:
```

Provide feed and vertical adaptations without changing the tested message variable.

---

# 14. Phase 10 - Video Creative and Script Pack

Generate 3-6 concepts. Prefer a natural, direct delivery when a real spokesperson is available.

## Recommended Video Types

- Owner or expert to camera
- Person to camera plus project/product B-roll
- Problem -> explanation -> solution
- FAQ or decision guide
- Process walkthrough
- Customer story, only with approved customer assets
- Before/after story, only with support and permission

## Video Brief Template

```text
Creative ID: CR-VID[NN]
Concept name:
Duration:
Placement/aspect ratio:
Presenter:
Test variable:
Variable IDs used:
Opening visual (0-3 seconds):
Hook:
Pain:
Process:
Proof:
Offer:
CTA:
B-roll list:
On-screen text:
Captions:
Audio/music direction:
Location/props:
Required permissions/disclaimers:
End card:
```

## Time-Coded Script Template

```text
0:00-0:03 - HOOK / PEOPLE
Dialogue: [HOOK]
Visual: [OPENING VISUAL]
On-screen text: [SHORT HOOK]

0:03-0:08 - PAIN
Dialogue: [ONE PAIN VARIABLE]
Visual: [SUPPORTED PROBLEM VISUAL]
On-screen text: [PAIN SUMMARY]

0:08-0:18 - PROCESS
Dialogue: [HOW THE BUSINESS HANDLES IT DIFFERENTLY]
Visual: [PROCESS B-ROLL]
On-screen text: [PROCESS BENEFIT]

0:18-0:23 - PROOF
Dialogue: [APPROVED PROOF OR OMIT]
Visual: [PROOF SOURCE]
On-screen text: [VERIFIABLE PROOF]

0:23-0:30 - OFFER / CTA
Dialogue: [OFFER, ELIGIBILITY, CTA]
Visual: [PRESENTER OR RESULT + END CARD]
On-screen text: [CTA]
```

Also provide:

- A 15-second cutdown plan
- A 30-second master plan
- A silent-viewing check
- A shot/capture checklist
- A list of claims or assets awaiting approval

The first test may change the hook while keeping the remaining script and edit identical.

---

# 15. Phase 11 - Meta Ad Copy Pack

Write copy that maps to the variable system rather than producing unrelated variations.

## Required Copy

- 3-5 primary texts per chosen angle
- 5-10 headlines
- 3-5 descriptions
- CTA button recommendation
- Destination and message-match note

## Primary Text Structures

### Short

```text
[PEOPLE/HOOK]
[ONE PAIN]
[PROCESS BENEFIT]
[OFFER + CTA]
```

### Medium

```text
[PEOPLE/HOOK]
[PAIN + CONSEQUENCE]
[PROCESS DIFFERENTIATOR]
[PROOF]
[OFFER]
[CTA]
```

### Long

```text
[PEOPLE/HOOK]
[PAIN EXPANSION]
[DECISION PROBLEM]
[PROCESS EXPLANATION]
[PROOF]
[OBJECTION RESPONSE]
[OFFER + TERMS]
[CTA]
```

## Copy Validation

For every item output:

```text
Copy ID:
Variable IDs:
Text:
Character count:
First-125-character preview:
Claim/proof status:
Policy or disclaimer note:
```

Use 40 characters as the recommended headline target and 30 characters as the recommended description target unless current placement requirements dictate otherwise. Longer copy must be clearly flagged for live placement review.

---

# 16. Phase 12 - Lead Form and Conversion Experience

## Lead Form Structure

```text
Form type/intent level:
Form headline:
Intro:
Value reminder:
Expectation statement:
Qualification questions:
Contact fields:
Consent language: [LEGAL/PRIVACY REVIEW REQUIRED]
Privacy policy URL:
Review screen:
Thank-you headline:
Thank-you message:
Immediate next step:
Secondary action:
```

## Question Rules

- Ask only questions used for qualification, routing, or preparation.
- Explain the purpose of high-friction questions.
- Prefer structured answers where useful.
- Do not request sensitive information unless necessary, lawful, secure, and approved.
- Separate required fields from optional fields.
- State the expected response or booking process accurately.

## Message-Match Check

The ad, form, thank-you screen, and follow-up must agree on:

- What the person requested
- Eligibility
- Price or free status
- Deadline
- What happens next
- Response time
- Required commitment

---

# 17. Phase 13 - Retargeting Strategy

Build segments only when the required tracking or engagement data exists.

## Segment Template

```text
Retargeting ID: RT-[NN]
Audience/source:
Lookback window:
Funnel stage:
Exclusions:
Observed intent:
Primary objection:
Message angle:
Offer:
Creative type:
CTA:
Frequency/fatigue monitoring rule:
Data requirement:
```

## Suggested Funnel Logic

- **Engaged but not visited/converted:** clarify problem and demonstrate process.
- **High-intent visitor but not converted:** address objection, proof, or next-step friction.
- **Form opened but not submitted:** simplify expectations; do not imply knowledge of sensitive behavior.
- **Lead not booked:** reinforce next step and trust; coordinate with CRM follow-up.
- **Existing customer:** exclude unless a separately approved cross-sell or retention campaign exists.
- **Recent converter:** exclude for an appropriate sales-cycle window.

Do not recommend lookback windows as universal facts. Mark them as proposed and adjust to buying cycle, audience size, and current platform capabilities.

---

# 18. Phase 14 - Speed-to-Lead and Follow-up

Map the full journey:

```text
Meta ad
-> Lead form or destination
-> Immediate confirmation
-> CRM record and owner assignment
-> First contact attempt
-> Qualification
-> Appointment or sale
-> Pre-appointment nurture
-> Proposal/checkout
-> Follow-up
-> Closed outcome and campaign feedback
```

## Required Follow-up Assets

Produce adaptable drafts with placeholders for missing operational facts:

1. Instant confirmation message
2. First SMS or WhatsApp message
3. First email
4. Call opener and qualification outline
5. No-answer follow-up
6. Appointment confirmation
7. Pre-appointment proof/expectation message
8. Quote or proposal follow-up
9. Close-lost reason capture

For each asset include timing, owner, purpose, message, stop condition, and required consent. The recommended cadence must respect the user's stated hours, channels, and local rules.

---

# 19. Phase 15 - Controlled Testing Matrix

## Variable Codes

| Variable | Code |
|---|---|
| People | PPL |
| Pain | PAI |
| Process | PRC |
| Offer | OFF |
| Hook | H |
| Proof | PRO |
| CTA | CTA |
| Creative concept/format | CR |
| Presenter | PRE |
| Length | LEN |
| Audience | AUD |
| Form | FRM |
| Follow-up | FUP |

## Test Record Template

| Field | Required value |
|---|---|
| Test ID | `T-[NN]` |
| Hypothesis | If X changes, Y should improve because Z |
| Funnel stage | Attention / consideration / lead / sale |
| Independent variable | Exactly one code |
| Control | Complete variable ID combination |
| Variant(s) | Complete combination, differing only in the independent variable |
| Constants | All held variables |
| Primary metric | One decision metric |
| Guardrail metrics | Quality/cost checks |
| Decision window | Time and/or data requirement |
| Winner rule | Predeclared rule |
| Result | Completed after the test |
| Next action | Keep, iterate, validate downstream, or retire |

## Recommended Test Sequence

1. People or pain-market resonance
2. Hook/opening
3. Process/differentiator
4. Proof
5. Offer
6. CTA
7. Creative delivery/format
8. Form friction or qualification
9. Follow-up process

The exact sequence should follow the biggest diagnosed uncertainty, not a ritual order.

## Valid Example

```text
Control: H-01_PPL-01_PAI-01_PRC-01_OFF-01_PRO-01_CTA-01_CR-VID01
Variant: H-02_PPL-01_PAI-01_PRC-01_OFF-01_PRO-01_CTA-01_CR-VID01
Changed variable: Hook only
```

## Invalid Example

```text
Control: owner video + pain A + offer A
Variant: static review card + pain B + offer B
Reason invalid: multiple variables changed, so the result is not diagnostic.
```

When Meta's delivery makes a clean test impossible, label the result `directional`, document the confounder, and do not overstate causality.

---

# 20. Phase 16 - Measurement and KPI Framework

## Measurement Readiness

Confirm or flag:

- Meta Pixel status
- Conversions API status
- Domain and event configuration where relevant
- Primary and secondary events
- CRM source and outcome capture
- UTM convention
- Duplicate event handling
- Test lead completion
- Offline conversion feedback where available
- Privacy/consent review

## KPI Ladder

| Funnel stage | KPIs | Diagnostic purpose |
|---|---|---|
| Delivery | Spend, reach, impressions, CPM, frequency | Can the campaign reach the market efficiently? |
| Attention | 3-second views, hook/hold rate, thumb-stop proxy | Does the opening earn attention? |
| Engagement | CTR, outbound CTR, CPC, video retention | Does the message create intent? |
| Conversion | Landing-page view rate, form-open rate, completion rate, CVR, CPL | Does the experience convert? |
| Quality | Qualified lead rate, invalid lead rate, contact rate | Are leads suitable and reachable? |
| Pipeline | Booking rate, show rate, proposal rate, close rate | Does the sales process progress leads? |
| Economics | CAC, revenue, ROAS, payback, contribution | Is growth commercially viable? |

## Formula Reference

```text
CTR = clicks / impressions
CPC = spend / clicks
CPM = spend / impressions x 1,000
Form completion rate = submitted forms / opened forms
CVR = conversions / landing-page views or clicks (state denominator)
CPL = spend / leads
Qualified CPL = spend / qualified leads
Booking rate = booked appointments / leads
Show rate = attended appointments / booked appointments
Close rate = sales / qualified opportunities (state denominator)
CAC = spend / new customers
ROAS = attributed revenue / spend
```

Always state the denominator and attribution source. Do not mix platform leads, CRM leads, or sales without reconciliation.

---

# 21. Phase 17 - Diagnostic and Iteration Rules

Change the narrowest variable that plausibly addresses the observed break.

| Observation | Likely area | Next controlled test | Do not conclude yet |
|---|---|---|---|
| Weak initial video retention | Hook/opening visual/People callout | Hook only | Offer is bad |
| Drop during problem section | Pain relevance or clarity | Pain only | Audience cannot convert |
| Strong engagement, weak click intent | Process, proof, or CTA clarity | One of these at a time | Lead form is the only issue |
| Clicks but low landing/form starts | Message match, speed, first-screen clarity | Destination first screen or form intro | Ad hook failed |
| Form opens but low completion | Question friction or trust | Remove/rewrite one question or proof element | All traffic is poor quality |
| Many leads, low qualification | People, offer, or qualification | People or offer first; one at a time | More leads will fix quality |
| Qualified leads, low contact rate | Data validity or response process | Contact method/timing | Creative is the primary cause |
| Contacts, low booking rate | Sales opener, expectation, offer fit | Follow-up or booking step | CPM is the issue |
| Bookings, low show rate | Confirmation and nurture | Reminder/nurture element | Audience targeting is wrong |
| Opportunities, low close rate | Sales/process/price/value | Sales-stage diagnosis | Ad CTR is the fix |
| Rising frequency and falling response | Fatigue | New creative execution holding message constant | Winning angle is permanently exhausted |

## Iteration Decision Types

- **Scale:** Winner also passes lead-quality and economics guardrails.
- **Validate downstream:** Attention winner lacks sufficient conversion-quality data.
- **Iterate:** Signal supports the angle but execution remains weak.
- **Retire:** Variant loses after the declared decision rule and has no downstream quality advantage.
- **Inconclusive:** Insufficient data, confounded delivery, tracking failure, or material external change.

Never scale solely because an ad has the highest CTR if qualified CPL, CAC, or sales quality deteriorates.

---

# 22. Required Final Deliverable Structure

Return the completed strategy in this exact order:

1. Executive Summary
2. Input Ledger and Missing Information
3. Campaign Thesis and Funnel
4. Conversion Economics and Measurement Readiness
5. People Variable Bank
6. Pain Variable Bank
7. Process/Differentiation Bank
8. Proof and Objection Bank
9. Offer Architecture
10. Hooks and CTAs
11. Campaign and Ad-Set Architecture
12. Graphic Creative Briefs
13. Video Concepts, Shot Lists, and Scripts
14. Primary Text, Headlines, and Descriptions
15. Lead Form and Thank-You Experience
16. Retargeting and Exclusions
17. Speed-to-Lead and Follow-up Assets
18. Testing Matrix
19. KPI Dashboard Specification
20. Diagnostic and Iteration Rules
21. Launch QA Checklist
22. Open Inputs and Approvals

Every creative and copy item must show its variable IDs so the testing matrix is auditable.

---

# 23. Launch QA Checklist

## Strategy

- [ ] Campaign thesis connects People, Pain, Process, and Offer.
- [ ] Campaign goal and conversion event match the business outcome.
- [ ] Budget and capacity assumptions are confirmed or marked missing.
- [ ] Every proposed fact is clearly distinguished from a confirmed fact.

## Offer and Claims

- [ ] Price, terms, eligibility, deadline, scarcity, and availability are accurate.
- [ ] Proof sources are recorded.
- [ ] Testimonials and customer assets have permission.
- [ ] Guarantees and warranties match approved terms.
- [ ] Required disclaimers are present and readable.

## Creative and Copy

- [ ] Opening visual and hook communicate within the first moments.
- [ ] Video works with sound off and has captions.
- [ ] Text is legible in each placement.
- [ ] Ad, form, landing page, and follow-up use the same offer.
- [ ] No prohibited personal-attribute assertion or unsupported outcome claim appears.
- [ ] Current placement previews have been reviewed in Meta Ads Manager.

## Funnel and Operations

- [ ] Form fields are necessary and route correctly.
- [ ] Privacy policy and consent language have been reviewed.
- [ ] Thank-you step accurately explains what happens next.
- [ ] CRM owner, contact hours, and follow-up stop conditions are defined.
- [ ] Sales capacity can handle projected lead volume.

## Tracking

- [ ] Primary event fires once and has been tested.
- [ ] Pixel/CAPI deduplication is checked where applicable.
- [ ] UTMs identify campaign, ad set, ad, and creative variable IDs.
- [ ] CRM records source, qualification, appointment, sale, and revenue outcomes.
- [ ] Reporting reconciles Meta, analytics, and CRM data.

## Testing

- [ ] Each test changes exactly one declared variable.
- [ ] Controls, variants, constants, and hypotheses are recorded.
- [ ] Primary metric, guardrails, and winner rule are declared before launch.
- [ ] Tests with confounders are labelled directional.

---

# 24. Reusable Invocation Template

Use this prompt with any future project:

```markdown
Run the `Reusable Facebook / Meta Ads Strategy Workflow` for the project below.

Create the complete 22-section deliverable. Normalize the information into the
input ledger first. Do not invent facts. Mark missing information with explicit
placeholders and include it in Open Inputs and Approvals. Build all creative and
copy from People -> Pain -> Process -> Offer. Assign variable IDs to every angle,
ad, graphic, video, script, and copy item. Build tests that change exactly one
variable at a time.

PROJECT DETAILS
[PASTE PROJECT DETAILS]

OFFER
[PASTE CONFIRMED OFFER OR STATE: PROPOSE OPTIONS]

OPTIONAL EVIDENCE AND ASSETS
[PASTE REVIEWS, RESULTS, TESTIMONIALS, BRAND RULES, CREATIVE INVENTORY,
HISTORICAL PERFORMANCE, AND TRACKING/FUNNEL DETAILS]
```

---

# 25. Completion Standard

The workflow is complete only when:

- All 22 final sections are present.
- Missing facts remain visible as placeholders.
- Each claim can be traced to an input or is labelled proposed.
- Graphic briefs and video scripts are production-ready.
- Copy is mapped to variable IDs and checked for placement length.
- Lead capture, retargeting, follow-up, and sales feedback are connected.
- KPIs cover attention through revenue, not just clicks and leads.
- Every experiment changes one variable at a time.
- Launch blockers and approvals are explicitly listed.

