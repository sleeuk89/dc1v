# UK Lead Generation Website - Reusable Development Prompt

Use this prompt to create a comprehensive UK lead generation website for any niche/keyword. Replace the placeholders in [BRACKETS] with your specific details.

---

## PROMPT TO USE:

```
Build me a comprehensive UK lead generation website for the following niche:

## PROJECT DETAILS
- YOUR_KEYWORD: [YOUR_KEYWORD_HERE] (e.g., "child injury claims")
- YOUR_DOMAIN: [YOUR_DOMAIN_HERE] (e.g., "https://childinjuryclaims.co.uk/")
- YOUR_FORMSPREE_ENDPOINT: [YOUR_FORMSPREE_URL_HERE] (e.g., "https://formspree.io/f/xyknozda")

## SAMPLE REFERENCE (Child Injury Claims)
This sample shows how the prompt works with actual values:
- YOUR_KEYWORD: "child injury claims"
- YOUR_DOMAIN: "https://childinjuryclaims.co.uk/"
- YOUR_FORMSPREE_ENDPOINT: "https://formspree.io/f/xyknozda"

---

## TECHNICAL REQUIREMENTS

### 1. Tech Stack
- Next.js 16 with App Router
- TypeScript
- Tailwind CSS 4
- shadcn/ui components
- Hash-based SPA routing (no server-side routing)
- Single page application architecture

### 2. Hydration-Safe Patterns (CRITICAL)
Use `mounted` state pattern to avoid SSR/CSR mismatch errors:
```typescript
const [mounted, setMounted] = useState(false)

useEffect(() => {
  setMounted(true)
}, [])

// Use mounted state in initializers
const [currentPath, setCurrentPath] = useState(() => {
  if (typeof window !== 'undefined') {
    return window.location.hash.slice(1) || '/'
  }
  return '/'
})
```

### 3. Hash-Based Routing Structure
- Homepage: `#home` or `#/`
- County pages: `#near-me/[county-slug]/`
- Town pages: `#near-me/[county-slug]-[town-slug]/`
- Static pages: `#about`, `#contact`, `#privacy`, `#cookies`

---

## WEBSITE STRUCTURE

### 1. Homepage Sections (12 H2 SEO Content Sections)
Create 12 unique H2 sections with 150-200 words each:

1. **Introduction to [KEYWORD]** - What it is, why it matters
2. **Types of [KEYWORD] Cases** - Different claim categories
3. **How to Make a [KEYWORD]** - Step-by-step process
4. **Compensation Amounts** - What people can expect to receive
5. **Time Limits for [KEYWORD]** - Legal deadlines and exceptions
6. **No Win No Fee Explained** - How the payment structure works
7. **The Claims Process** - Detailed walkthrough
8. **What Evidence You Need** - Documentation required
9. **Common Challenges** - Obstacles and how to overcome them
10. **Why Choose Us** - Unique selling points
11. **[KEYWORD] Statistics** - Relevant data and figures
12. **Frequently Asked Questions** - Common queries answered

### 2. Location Pages Structure

#### County Pages (40+ Counties)
- H1: "[KEYWORD] in [County Name]"
- Meta description: "Expert [KEYWORD] specialists serving [County Name]. No win no fee, free assessment."
- Content: 6 unique H2 sections about [KEYWORD] in that county
- Internal links: Link to main keyword page and town pages
- Town links section showing all towns in that county

#### Town Pages (200+ Towns)
- H1: "[KEYWORD] in [Town Name], [County Name]"
- Meta description: "Expert [KEYWORD] specialists in [Town Name], [County Name]. No win no fee, free assessment."
- Content: 6 unique H2 sections about [KEYWORD] in that town
- Internal links: Link to county page and main keyword page
- Nearby towns section

### 3. Location Data Structure
```typescript
const locationData = [
  {
    county: "Greater London",
    slug: "greater-london",
    towns: [
      { name: "Woolwich", slug: "woolwich", postcode: "SE18" },
      { name: "Croydon", slug: "croydon", postcode: "CR0" },
      // ... more towns
    ]
  },
  // ... 40+ counties with 5-8 towns each
]
```

---

## UI COMPONENTS

### 1. Header
- Logo/Brand name
- Navigation links: Home, About, Contact, Near Me dropdown
- Sticky header on scroll

### 2. Hero Section
- H1 with main keyword
- Subtitle with value proposition
- CTA button: "Start Your Claim" or "Free Assessment"
- Background gradient or image

### 3. Stats Bar
- "98% Success Rate"
- "£50M+ Recovered"
- "5,000+ Happy Clients"
- "No Win No Fee"

### 4. Sticky Sidebar Contact Form
- Fixed position on right side for desktop
- Appears after scrolling past hero (300px+)
- Fields: Name, Phone, Email, Message
- Submit button: "Get Free Advice"
- Submit to Formspree endpoint

### 5. Sticky Bottom CTA Button (Mobile)
- Fixed at bottom of screen
- Text: "Make an Enquiry"
- Opens lead capture modal
- Adjusts position if cookie banner is visible

### 6. Lead Capture Modal (Multi-Step)
- Step 1: Incident type selection
- Step 2: When it happened
- Step 3: Contact details (Name, Phone, Email)
- Step 4: Success message

### 7. Compensation Calculator
- Slider for severity
- Type selection
- Estimated compensation display
- Disclaimer text

### 8. FAQ Accordion
- 5-6 questions relevant to the niche
- Expandable/collapsible sections

### 9. Cookie Consent Banner
- Fixed at bottom of screen
- Accept/Decline buttons
- Link to Cookie Policy
- Stores preference in localStorage

### 10. Footer
- Logo and description
- Quick Links (Home, About, Contact, Privacy, Cookies)
- Location links grid
- All counties grid
- Copyright and regulatory info (see below)

---

## FOOTER CONTENT (MANDATORY)

```
© 2026 DM Claims. All rights reserved.

[YOUR_KEYWORD] is operated by DM Claims. We're authorised and regulated by the Financial Conduct Authority under reference number 1005543.
```

Example for "Child Injury Claims":
```
© 2026 DM Claims. All rights reserved.

Child Injury Claims is operated by DM Claims. We're authorised and regulated by the Financial Conduct Authority under reference number 1005543.
```

---

## STATIC PAGES CONTENT

### 1. Privacy Policy Page
Include these sections:
- Introduction with DM Claims and FCA regulation
- Information We Collect (Personal, Automatic, Cookies)
- How We Use Your Information
- Sharing Your Information
- Data Security
- Retention of Your Information
- Your Rights (GDPR)
- Third-Party Links
- Changes to This Privacy Policy
- Contact Us

**Footer Privacy Policy text:**
```
At https://[YOUR_DOMAIN]/ ("the Website"), operated by DM Claims ("we," "us," or "our"), your privacy is of utmost importance to us. This Privacy Policy outlines how we collect, use, and protect your personal information when you visit our Website or use our services. DM Claims is authorised and regulated by the Financial Conduct Authority (FCA), number 1005543.
```

Contact email: `info@[YOUR_DOMAIN]`

### 2. Cookie Policy Page
Include these sections:
- Introduction with DM Claims
- What Are Cookies?
- Types of Cookies We Use (Necessary, Performance/Analytics, Functionality, Targeting/Advertising)
- How We Use Google Analytics
- Managing Cookies (Browser Settings, Cookie Banner, Opt-Out)
- Third-Party Cookies
- Changes to This Cookie Policy
- Contact Us

**Footer Cookie Policy text:**
```
This Cookie Policy explains how https://[YOUR_DOMAIN]/ ("the Website") operated by DM Claims ("we," "us," or "our") uses cookies and similar technologies to enhance user experience, analyse Website performance, and provide our services.
```

### 3. About Page
- Company overview
- Mission statement
- Why choose us
- Team/expertise

### 4. Contact Page
- Contact form (submits to Formspree)
- No phone number (as per requirements)
- Email contact option
- Response time commitment

---

## CONTENT GUIDELINES (CRITICAL)

### Words to AVOID:
- ❌ "lawyers"
- ❌ "lawyer"
- ❌ "solicitors"
- ❌ "solicitor"
- ❌ "specialist" (use "expert" or "professional" instead)

### Words to USE:
- ✅ "claims experts"
- ✅ "claims professionals"
- ✅ "claims team"
- ✅ "advisors"
- ✅ "consultants"
- ✅ "representatives"

### Content Style:
- Professional but accessible tone
- Focus on helping claimants
- Emphasize "no win no fee"
- Highlight free assessments
- Include statistics where relevant
- Use bullet points for readability

---

## INTERNAL LINKING STRUCTURE

### Homepage Content:
- Link to main keyword in introduction
- Link to top counties (Greater London, Greater Manchester, etc.)

### County Pages:
- Link to main keyword page: `#home`
- Link to all town pages within the county
- Link to other counties at bottom

### Town Pages:
- Link to main keyword page: `#home`
- Link to parent county page: `#near-me/[county-slug]`
- Link to nearby towns in same county

### All Content Sections:
Add contextual internal links:
- "[KEYWORD]" → `#home`
- "[County Name]" → `#near-me/[county-slug]`
- "[Town Name]" → `#near-me/[county-slug]-[town-slug]`

---

## FORM SUBMISSION

### Contact Form Configuration:
```typescript
const formspreeResponse = await fetch('[YOUR_FORMSPREE_ENDPOINT]', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: formData.name,
    email: formData.email,
    phone: formData.phone,
    message: formData.message,
    incidentType: formData.incidentType,
    incidentDate: formData.incidentDate
  })
});
```

### Form Fields:
- Name (required)
- Email (required)
- Phone (required)
- Message (optional)
- Incident Type (for modal)
- Incident Date (for modal)

---

## SEO IMPLEMENTATION

### 1. Schema Markup
```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "[KEYWORD]",
  "url": "[YOUR_DOMAIN]",
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "serviceType": "[KEYWORD] Services"
}
```

### 2. Meta Tags (per page)
```typescript
<title>{pageTitle} | [KEYWORD]</title>
<meta name="description" content={pageDescription} />
```

### 3. Heading Structure
- One H1 per page
- Multiple H2s for sections
- H3s for subsections
- Proper nesting hierarchy

---

## COLOR SCHEME

```css
--primary: #1a2744;      /* Dark blue - headers, text */
--secondary: #f59e0b;    /* Amber/orange - CTAs, accents */
--background: #ffffff;   /* White */
--text: #374151;         /* Gray - body text */
--light-gray: #f3f4f6;   /* Light backgrounds */
```

---

## FILE STRUCTURE

```
src/
├── app/
│   ├── layout.tsx       # Root layout with favicon
│   ├── page.tsx         # Main SPA component (ALL content)
│   └── api/
│       └── contact/
│           └── route.ts # Form submission handler
├── components/
│   └── ui/              # shadcn/ui components
└── lib/
    └── utils.ts
public/
├── favicon.png          # Custom favicon
└── robots.txt
```

---

## SITE_CONFIG Object

```typescript
const SITE_CONFIG = {
  domain: '[YOUR_DOMAIN]',
  keyword: '[YOUR_KEYWORD]',
  email: 'info@[YOUR_DOMAIN]',
  formspreeEndpoint: '[YOUR_FORMSPREE_ENDPOINT]',
  phone: '', // Leave empty (no phone number)
  companyName: 'DM Claims',
  fcaNumber: '1005543'
}
```

---

## SAMPLE OUTPUT STRUCTURE

When I run this prompt with:
- YOUR_KEYWORD: "child injury claims"
- YOUR_DOMAIN: "https://childinjuryclaims.co.uk/"

The website will have:
1. Homepage with 12 H2 sections about child injury claims
2. 40+ county pages (e.g., "Child Injury Claims in Greater London")
3. 200+ town pages (e.g., "Child Injury Claims in Manchester, Greater Manchester")
4. Sticky sidebar form submitting to Formspree
5. Mobile sticky "Make an Enquiry" button
6. Privacy Policy with DM Claims and FCA regulation
7. Cookie Policy with Google Analytics information
8. Footer: "© 2026 DM Claims. Child Injury Claims is operated by DM Claims. FCA ref: 1005543"
9. All internal links properly connected
10. No mention of "lawyers", "solicitors", or "specialist"

---

## DEPLOYMENT CHECKLIST

After development:
1. [ ] Test all hash routes work correctly
2. [ ] Test form submission to Formspree
3. [ ] Verify footer has correct DM Claims text
4. [ ] Check Privacy Policy has FCA number
5. [ ] Check Cookie Policy is complete
6. [ ] Verify no forbidden words (lawyers, solicitors, specialist)
7. [ ] Test sticky sidebar appears on scroll
8. [ ] Test mobile sticky button
9. [ ] Test cookie consent banner
10. [ ] Push to GitHub repository

---

## GITHUB PUSH COMMANDS

```bash
git add -A
git commit -m "Initial commit - [KEYWORD] lead generation website"
git remote add origin https://github.com/[USERNAME]/[REPO].git
git push -u origin master
```
```

---

## HOW TO USE THIS PROMPT

1. **Copy the entire prompt above** (everything between the triple backticks)

2. **Replace placeholders:**
   - `[YOUR_KEYWORD_HERE]` → Your target keyword (e.g., "work accident claims")
   - `[YOUR_DOMAIN_HERE]` → Your domain (e.g., "https://workaccidentclaims.co.uk/")
   - `[YOUR_FORMSPREE_URL_HERE]` → Your Formspree endpoint

3. **Paste into an LLM** (Claude, GPT-4, etc.) and request the website build

4. **The LLM will generate:**
   - Complete Next.js project
   - All location pages
   - All static pages
   - Proper SEO structure
   - Form submissions
   - Correct footer and policies

---

## EXAMPLE USAGE

For a new "whiplash claims" website:

```
YOUR_KEYWORD: whiplash claims
YOUR_DOMAIN: https://whiplashclaims.co.uk/
YOUR_FORMSPREE_ENDPOINT: https://formspree.io/f/abc123
```

The prompt will generate a complete website with:
- "Whiplash Claims" branding throughout
- 12 H2 sections about whiplash claims
- County pages: "Whiplash Claims in Greater London"
- Town pages: "Whiplash Claims in Manchester, Greater Manchester"
- Footer: "© 2026 DM Claims. Whiplash Claims is operated by DM Claims..."
- All internal links using whiplash claims context
