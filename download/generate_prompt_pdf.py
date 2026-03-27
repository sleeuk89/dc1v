from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.lib.units import inch

# Register fonts
pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')

# Create document
doc = SimpleDocTemplate(
    "/home/z/my-project/download/LeadGen_Reusable_Prompt.pdf",
    pagesize=A4,
    title="LeadGen_Reusable_Prompt",
    author='Z.ai',
    creator='Z.ai',
    subject='UK Lead Generation Website Reusable Development Prompt',
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

# Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    name='Title',
    fontName='Times New Roman',
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    spaceAfter=20
)

h1_style = ParagraphStyle(
    name='H1',
    fontName='Times New Roman',
    fontSize=18,
    leading=24,
    spaceBefore=20,
    spaceAfter=10,
    textColor=colors.HexColor('#1a2744')
)

h2_style = ParagraphStyle(
    name='H2',
    fontName='Times New Roman',
    fontSize=14,
    leading=20,
    spaceBefore=15,
    spaceAfter=8,
    textColor=colors.HexColor('#1a2744')
)

h3_style = ParagraphStyle(
    name='H3',
    fontName='Times New Roman',
    fontSize=12,
    leading=16,
    spaceBefore=10,
    spaceAfter=6,
    textColor=colors.HexColor('#333333')
)

body_style = ParagraphStyle(
    name='Body',
    fontName='Times New Roman',
    fontSize=10,
    leading=14,
    alignment=TA_LEFT,
    spaceAfter=6
)

code_style = ParagraphStyle(
    name='Code',
    fontName='Times New Roman',
    fontSize=9,
    leading=12,
    leftIndent=20,
    spaceAfter=10,
    backColor=colors.HexColor('#f5f5f5')
)

bullet_style = ParagraphStyle(
    name='Bullet',
    fontName='Times New Roman',
    fontSize=10,
    leading=14,
    leftIndent=20,
    spaceAfter=4
)

story = []

# Title
story.append(Paragraph("<b>UK Lead Generation Website</b>", title_style))
story.append(Paragraph("<b>Reusable Development Prompt</b>", title_style))
story.append(Spacer(1, 30))
story.append(Paragraph("Use this prompt to create a comprehensive UK lead generation website for any niche/keyword. Replace the placeholders in [BRACKETS] with your specific details.", body_style))
story.append(Spacer(1, 20))

# Section 1: Prompt to Use
story.append(Paragraph("<b>1. PROMPT TO USE</b>", h1_style))
story.append(Paragraph("Build me a comprehensive UK lead generation website for the following niche:", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>PROJECT DETAILS</b>", h2_style))
story.append(Paragraph("• YOUR_KEYWORD: [YOUR_KEYWORD_HERE] (e.g., \"child injury claims\")", bullet_style))
story.append(Paragraph("• YOUR_DOMAIN: [YOUR_DOMAIN_HERE] (e.g., \"https://childinjuryclaims.co.uk/\")", bullet_style))
story.append(Paragraph("• YOUR_FORMSPREE_ENDPOINT: [YOUR_FORMSPREE_URL_HERE] (e.g., \"https://formspree.io/f/xyknozda\")", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>SAMPLE REFERENCE (Child Injury Claims)</b>", h2_style))
story.append(Paragraph("This sample shows how the prompt works with actual values:", body_style))
story.append(Paragraph("• YOUR_KEYWORD: \"child injury claims\"", bullet_style))
story.append(Paragraph("• YOUR_DOMAIN: \"https://childinjuryclaims.co.uk/\"", bullet_style))
story.append(Paragraph("• YOUR_FORMSPREE_ENDPOINT: \"https://formspree.io/f/xyknozda\"", bullet_style))

# Section 2: Technical Requirements
story.append(PageBreak())
story.append(Paragraph("<b>2. TECHNICAL REQUIREMENTS</b>", h1_style))

story.append(Paragraph("<b>2.1 Tech Stack</b>", h2_style))
story.append(Paragraph("• Next.js 16 with App Router", bullet_style))
story.append(Paragraph("• TypeScript", bullet_style))
story.append(Paragraph("• Tailwind CSS 4", bullet_style))
story.append(Paragraph("• shadcn/ui components", bullet_style))
story.append(Paragraph("• Hash-based SPA routing (no server-side routing)", bullet_style))
story.append(Paragraph("• Single page application architecture", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>2.2 Hydration-Safe Patterns (CRITICAL)</b>", h2_style))
story.append(Paragraph("Use `mounted` state pattern to avoid SSR/CSR mismatch errors. Always check for window availability before accessing browser APIs in useState initializers.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>2.3 Hash-Based Routing Structure</b>", h2_style))
story.append(Paragraph("• Homepage: #home or #/", bullet_style))
story.append(Paragraph("• County pages: #near-me/[county-slug]/", bullet_style))
story.append(Paragraph("• Town pages: #near-me/[county-slug]-[town-slug]/", bullet_style))
story.append(Paragraph("• Static pages: #about, #contact, #privacy, #cookies", bullet_style))

# Section 3: Website Structure
story.append(Paragraph("<b>3. WEBSITE STRUCTURE</b>", h1_style))

story.append(Paragraph("<b>3.1 Homepage Sections (12 H2 SEO Content Sections)</b>", h2_style))
story.append(Paragraph("Create 12 unique H2 sections with 150-200 words each:", body_style))
story.append(Paragraph("1. Introduction to [KEYWORD] - What it is, why it matters", bullet_style))
story.append(Paragraph("2. Types of [KEYWORD] Cases - Different claim categories", bullet_style))
story.append(Paragraph("3. How to Make a [KEYWORD] - Step-by-step process", bullet_style))
story.append(Paragraph("4. Compensation Amounts - What people can expect to receive", bullet_style))
story.append(Paragraph("5. Time Limits for [KEYWORD] - Legal deadlines and exceptions", bullet_style))
story.append(Paragraph("6. No Win No Fee Explained - How the payment structure works", bullet_style))
story.append(Paragraph("7. The Claims Process - Detailed walkthrough", bullet_style))
story.append(Paragraph("8. What Evidence You Need - Documentation required", bullet_style))
story.append(Paragraph("9. Common Challenges - Obstacles and how to overcome them", bullet_style))
story.append(Paragraph("10. Why Choose Us - Unique selling points", bullet_style))
story.append(Paragraph("11. [KEYWORD] Statistics - Relevant data and figures", bullet_style))
story.append(Paragraph("12. Frequently Asked Questions - Common queries answered", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>3.2 Location Pages Structure</b>", h2_style))
story.append(Paragraph("<b>County Pages (40+ Counties)</b>", h3_style))
story.append(Paragraph("• H1: \"[KEYWORD] in [County Name]\"", bullet_style))
story.append(Paragraph("• Meta description: \"Expert [KEYWORD] specialists serving [County Name]. No win no fee, free assessment.\"", bullet_style))
story.append(Paragraph("• Content: 6 unique H2 sections about [KEYWORD] in that county", bullet_style))
story.append(Paragraph("• Internal links: Link to main keyword page and town pages", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>Town Pages (200+ Towns)</b>", h3_style))
story.append(Paragraph("• H1: \"[KEYWORD] in [Town Name], [County Name]\"", bullet_style))
story.append(Paragraph("• Meta description: \"Expert [KEYWORD] specialists in [Town Name], [County Name]. No win no fee, free assessment.\"", bullet_style))
story.append(Paragraph("• Content: 6 unique H2 sections about [KEYWORD] in that town", bullet_style))
story.append(Paragraph("• Internal links: Link to county page and main keyword page", bullet_style))

# Section 4: UI Components
story.append(PageBreak())
story.append(Paragraph("<b>4. UI COMPONENTS</b>", h1_style))

story.append(Paragraph("<b>4.1 Header</b>", h2_style))
story.append(Paragraph("• Logo/Brand name", bullet_style))
story.append(Paragraph("• Navigation links: Home, About, Contact, Near Me dropdown", bullet_style))
story.append(Paragraph("• Sticky header on scroll", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.2 Hero Section</b>", h2_style))
story.append(Paragraph("• H1 with main keyword", bullet_style))
story.append(Paragraph("• Subtitle with value proposition", bullet_style))
story.append(Paragraph("• CTA button: \"Start Your Claim\" or \"Free Assessment\"", bullet_style))
story.append(Paragraph("• Background gradient or image", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.3 Stats Bar</b>", h2_style))
story.append(Paragraph("• \"98% Success Rate\"", bullet_style))
story.append(Paragraph("• \"£50M+ Recovered\"", bullet_style))
story.append(Paragraph("• \"5,000+ Happy Clients\"", bullet_style))
story.append(Paragraph("• \"No Win No Fee\"", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.4 Sticky Sidebar Contact Form</b>", h2_style))
story.append(Paragraph("• Fixed position on right side for desktop", bullet_style))
story.append(Paragraph("• Appears after scrolling past hero (300px+)", bullet_style))
story.append(Paragraph("• Fields: Name, Phone, Email, Message", bullet_style))
story.append(Paragraph("• Submit button: \"Get Free Advice\"", bullet_style))
story.append(Paragraph("• Submit to Formspree endpoint", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.5 Sticky Bottom CTA Button (Mobile)</b>", h2_style))
story.append(Paragraph("• Fixed at bottom of screen", bullet_style))
story.append(Paragraph("• Text: \"Make an Enquiry\"", bullet_style))
story.append(Paragraph("• Opens lead capture modal", bullet_style))
story.append(Paragraph("• Adjusts position if cookie banner is visible", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.6 Lead Capture Modal (Multi-Step)</b>", h2_style))
story.append(Paragraph("• Step 1: Incident type selection", bullet_style))
story.append(Paragraph("• Step 2: When it happened", bullet_style))
story.append(Paragraph("• Step 3: Contact details (Name, Phone, Email)", bullet_style))
story.append(Paragraph("• Step 4: Success message", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.7 Compensation Calculator</b>", h2_style))
story.append(Paragraph("• Slider for severity", bullet_style))
story.append(Paragraph("• Type selection", bullet_style))
story.append(Paragraph("• Estimated compensation display", bullet_style))
story.append(Paragraph("• Disclaimer text", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.8 FAQ Accordion</b>", h2_style))
story.append(Paragraph("• 5-6 questions relevant to the niche", bullet_style))
story.append(Paragraph("• Expandable/collapsible sections", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.9 Cookie Consent Banner</b>", h2_style))
story.append(Paragraph("• Fixed at bottom of screen", bullet_style))
story.append(Paragraph("• Accept/Decline buttons", bullet_style))
story.append(Paragraph("• Link to Cookie Policy", bullet_style))
story.append(Paragraph("• Stores preference in localStorage", bullet_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>4.10 Footer</b>", h2_style))
story.append(Paragraph("• Logo and description", bullet_style))
story.append(Paragraph("• Quick Links (Home, About, Contact, Privacy, Cookies)", bullet_style))
story.append(Paragraph("• Location links grid", bullet_style))
story.append(Paragraph("• All counties grid", bullet_style))
story.append(Paragraph("• Copyright and regulatory info", bullet_style))

# Section 5: Footer Content
story.append(PageBreak())
story.append(Paragraph("<b>5. FOOTER CONTENT (MANDATORY)</b>", h1_style))
story.append(Spacer(1, 10))
story.append(Paragraph("© 2026 DM Claims. All rights reserved.", body_style))
story.append(Spacer(1, 8))
story.append(Paragraph("[YOUR_KEYWORD] is operated by DM Claims. We're authorised and regulated by the Financial Conduct Authority under reference number 1005543.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("<b>Example for \"Child Injury Claims\":</b>", h3_style))
story.append(Paragraph("© 2026 DM Claims. All rights reserved.", body_style))
story.append(Paragraph("Child Injury Claims is operated by DM Claims. We're authorised and regulated by the Financial Conduct Authority under reference number 1005543.", body_style))

# Section 6: Static Pages Content
story.append(Paragraph("<b>6. STATIC PAGES CONTENT</b>", h1_style))

story.append(Paragraph("<b>6.1 Privacy Policy Page</b>", h2_style))
story.append(Paragraph("Include these sections:", body_style))
story.append(Paragraph("• Introduction with DM Claims and FCA regulation", bullet_style))
story.append(Paragraph("• Information We Collect (Personal, Automatic, Cookies)", bullet_style))
story.append(Paragraph("• How We Use Your Information", bullet_style))
story.append(Paragraph("• Sharing Your Information", bullet_style))
story.append(Paragraph("• Data Security", bullet_style))
story.append(Paragraph("• Retention of Your Information", bullet_style))
story.append(Paragraph("• Your Rights (GDPR)", bullet_style))
story.append(Paragraph("• Third-Party Links", bullet_style))
story.append(Paragraph("• Changes to This Privacy Policy", bullet_style))
story.append(Paragraph("• Contact Us", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Contact email: info@[YOUR_DOMAIN]", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>6.2 Cookie Policy Page</b>", h2_style))
story.append(Paragraph("Include these sections:", body_style))
story.append(Paragraph("• Introduction with DM Claims", bullet_style))
story.append(Paragraph("• What Are Cookies?", bullet_style))
story.append(Paragraph("• Types of Cookies We Use (Necessary, Performance/Analytics, Functionality, Targeting/Advertising)", bullet_style))
story.append(Paragraph("• How We Use Google Analytics", bullet_style))
story.append(Paragraph("• Managing Cookies (Browser Settings, Cookie Banner, Opt-Out)", bullet_style))
story.append(Paragraph("• Third-Party Cookies", bullet_style))
story.append(Paragraph("• Changes to This Cookie Policy", bullet_style))
story.append(Paragraph("• Contact Us", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>6.3 About Page</b>", h2_style))
story.append(Paragraph("• Company overview", bullet_style))
story.append(Paragraph("• Mission statement", bullet_style))
story.append(Paragraph("• Why choose us", bullet_style))
story.append(Paragraph("• Team/expertise", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>6.4 Contact Page</b>", h2_style))
story.append(Paragraph("• Contact form (submits to Formspree)", bullet_style))
story.append(Paragraph("• No phone number (as per requirements)", bullet_style))
story.append(Paragraph("• Email contact option", bullet_style))
story.append(Paragraph("• Response time commitment", bullet_style))

# Section 7: Content Guidelines
story.append(PageBreak())
story.append(Paragraph("<b>7. CONTENT GUIDELINES (CRITICAL)</b>", h1_style))

story.append(Paragraph("<b>Words to AVOID:</b>", h2_style))
story.append(Paragraph("• \"lawyers\"", bullet_style))
story.append(Paragraph("• \"lawyer\"", bullet_style))
story.append(Paragraph("• \"solicitors\"", bullet_style))
story.append(Paragraph("• \"solicitor\"", bullet_style))
story.append(Paragraph("• \"specialist\" (use \"expert\" or \"professional\" instead)", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Words to USE:</b>", h2_style))
story.append(Paragraph("• \"claims experts\"", bullet_style))
story.append(Paragraph("• \"claims professionals\"", bullet_style))
story.append(Paragraph("• \"claims team\"", bullet_style))
story.append(Paragraph("• \"advisors\"", bullet_style))
story.append(Paragraph("• \"consultants\"", bullet_style))
story.append(Paragraph("• \"representatives\"", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Content Style:</b>", h2_style))
story.append(Paragraph("• Professional but accessible tone", bullet_style))
story.append(Paragraph("• Focus on helping claimants", bullet_style))
story.append(Paragraph("• Emphasize \"no win no fee\"", bullet_style))
story.append(Paragraph("• Highlight free assessments", bullet_style))
story.append(Paragraph("• Include statistics where relevant", bullet_style))
story.append(Paragraph("• Use bullet points for readability", bullet_style))

# Section 8: Internal Linking Structure
story.append(Paragraph("<b>8. INTERNAL LINKING STRUCTURE</b>", h1_style))

story.append(Paragraph("<b>Homepage Content:</b>", h2_style))
story.append(Paragraph("• Link to main keyword in introduction", bullet_style))
story.append(Paragraph("• Link to top counties (Greater London, Greater Manchester, etc.)", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>County Pages:</b>", h2_style))
story.append(Paragraph("• Link to main keyword page: #home", bullet_style))
story.append(Paragraph("• Link to all town pages within the county", bullet_style))
story.append(Paragraph("• Link to other counties at bottom", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Town Pages:</b>", h2_style))
story.append(Paragraph("• Link to main keyword page: #home", bullet_style))
story.append(Paragraph("• Link to parent county page: #near-me/[county-slug]", bullet_style))
story.append(Paragraph("• Link to nearby towns in same county", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>All Content Sections:</b>", h2_style))
story.append(Paragraph("Add contextual internal links:", body_style))
story.append(Paragraph("• \"[KEYWORD]\" → #home", bullet_style))
story.append(Paragraph("• \"[County Name]\" → #near-me/[county-slug]", bullet_style))
story.append(Paragraph("• \"[Town Name]\" → #near-me/[county-slug]-[town-slug]", bullet_style))

# Section 9: Form Submission
story.append(PageBreak())
story.append(Paragraph("<b>9. FORM SUBMISSION</b>", h1_style))

story.append(Paragraph("<b>Contact Form Configuration:</b>", h2_style))
story.append(Paragraph("Submit form data to Formspree endpoint with POST method and JSON content type. Include all required fields in the request body.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Form Fields:</b>", h2_style))
story.append(Paragraph("• Name (required)", bullet_style))
story.append(Paragraph("• Email (required)", bullet_style))
story.append(Paragraph("• Phone (required)", bullet_style))
story.append(Paragraph("• Message (optional)", bullet_style))
story.append(Paragraph("• Incident Type (for modal)", bullet_style))
story.append(Paragraph("• Incident Date (for modal)", bullet_style))

# Section 10: SEO Implementation
story.append(Paragraph("<b>10. SEO IMPLEMENTATION</b>", h1_style))

story.append(Paragraph("<b>10.1 Schema Markup</b>", h2_style))
story.append(Paragraph("Include JSON-LD structured data for LegalService schema type with name, URL, areaServed (United Kingdom), and serviceType.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>10.2 Meta Tags (per page)</b>", h2_style))
story.append(Paragraph("• Title: {pageTitle} | [KEYWORD]", bullet_style))
story.append(Paragraph("• Meta description with relevant content", bullet_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>10.3 Heading Structure</b>", h2_style))
story.append(Paragraph("• One H1 per page", bullet_style))
story.append(Paragraph("• Multiple H2s for sections", bullet_style))
story.append(Paragraph("• H3s for subsections", bullet_style))
story.append(Paragraph("• Proper nesting hierarchy", bullet_style))

# Section 11: Color Scheme
story.append(Paragraph("<b>11. COLOR SCHEME</b>", h1_style))
story.append(Paragraph("• Primary: #1a2744 (Dark blue - headers, text)", bullet_style))
story.append(Paragraph("• Secondary: #f59e0b (Amber/orange - CTAs, accents)", bullet_style))
story.append(Paragraph("• Background: #ffffff (White)", bullet_style))
story.append(Paragraph("• Text: #374151 (Gray - body text)", bullet_style))
story.append(Paragraph("• Light gray: #f3f4f6 (Light backgrounds)", bullet_style))

# Section 12: File Structure
story.append(Paragraph("<b>12. FILE STRUCTURE</b>", h1_style))
story.append(Paragraph("src/app/layout.tsx - Root layout with favicon", bullet_style))
story.append(Paragraph("src/app/page.tsx - Main SPA component (ALL content)", bullet_style))
story.append(Paragraph("src/app/api/contact/route.ts - Form submission handler", bullet_style))
story.append(Paragraph("src/components/ui/ - shadcn/ui components", bullet_style))
story.append(Paragraph("src/lib/utils.ts - Utility functions", bullet_style))
story.append(Paragraph("public/favicon.png - Custom favicon", bullet_style))

# Section 13: Site Config
story.append(PageBreak())
story.append(Paragraph("<b>13. SITE_CONFIG Object</b>", h1_style))
story.append(Paragraph("Create a configuration object with the following properties:", body_style))
story.append(Paragraph("• domain: '[YOUR_DOMAIN]'", bullet_style))
story.append(Paragraph("• keyword: '[YOUR_KEYWORD]'", bullet_style))
story.append(Paragraph("• email: 'info@[YOUR_DOMAIN]'", bullet_style))
story.append(Paragraph("• formspreeEndpoint: '[YOUR_FORMSPREE_ENDPOINT]'", bullet_style))
story.append(Paragraph("• phone: '' (Leave empty - no phone number)", bullet_style))
story.append(Paragraph("• companyName: 'DM Claims'", bullet_style))
story.append(Paragraph("• fcaNumber: '1005543'", bullet_style))

# Section 14: Sample Output
story.append(Paragraph("<b>14. SAMPLE OUTPUT STRUCTURE</b>", h1_style))
story.append(Paragraph("When running this prompt with YOUR_KEYWORD: \"child injury claims\" and YOUR_DOMAIN: \"https://childinjuryclaims.co.uk/\", the website will have:", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("1. Homepage with 12 H2 sections about child injury claims", bullet_style))
story.append(Paragraph("2. 40+ county pages (e.g., \"Child Injury Claims in Greater London\")", bullet_style))
story.append(Paragraph("3. 200+ town pages (e.g., \"Child Injury Claims in Manchester, Greater Manchester\")", bullet_style))
story.append(Paragraph("4. Sticky sidebar form submitting to Formspree", bullet_style))
story.append(Paragraph("5. Mobile sticky \"Make an Enquiry\" button", bullet_style))
story.append(Paragraph("6. Privacy Policy with DM Claims and FCA regulation", bullet_style))
story.append(Paragraph("7. Cookie Policy with Google Analytics information", bullet_style))
story.append(Paragraph("8. Footer: \"© 2026 DM Claims. Child Injury Claims is operated by DM Claims. FCA ref: 1005543\"", bullet_style))
story.append(Paragraph("9. All internal links properly connected", bullet_style))
story.append(Paragraph("10. No mention of \"lawyers\", \"solicitors\", or \"specialist\"", bullet_style))

# Section 15: Deployment Checklist
story.append(Paragraph("<b>15. DEPLOYMENT CHECKLIST</b>", h1_style))
story.append(Paragraph("After development:", body_style))
story.append(Paragraph("1. Test all hash routes work correctly", bullet_style))
story.append(Paragraph("2. Test form submission to Formspree", bullet_style))
story.append(Paragraph("3. Verify footer has correct DM Claims text", bullet_style))
story.append(Paragraph("4. Check Privacy Policy has FCA number", bullet_style))
story.append(Paragraph("5. Check Cookie Policy is complete", bullet_style))
story.append(Paragraph("6. Verify no forbidden words (lawyers, solicitors, specialist)", bullet_style))
story.append(Paragraph("7. Test sticky sidebar appears on scroll", bullet_style))
story.append(Paragraph("8. Test mobile sticky button", bullet_style))
story.append(Paragraph("9. Test cookie consent banner", bullet_style))
story.append(Paragraph("10. Push to GitHub repository", bullet_style))

# Section 16: How to Use
story.append(Paragraph("<b>16. HOW TO USE THIS PROMPT</b>", h1_style))
story.append(Paragraph("1. Copy the entire prompt above", body_style))
story.append(Paragraph("2. Replace placeholders:", body_style))
story.append(Paragraph("   • [YOUR_KEYWORD_HERE] → Your target keyword (e.g., \"work accident claims\")", bullet_style))
story.append(Paragraph("   • [YOUR_DOMAIN_HERE] → Your domain (e.g., \"https://workaccidentclaims.co.uk/\")", bullet_style))
story.append(Paragraph("   • [YOUR_FORMSPREE_URL_HERE] → Your Formspree endpoint", bullet_style))
story.append(Spacer(1, 10))
story.append(Paragraph("3. Paste into an LLM (Claude, GPT-4, etc.) and request the website build", body_style))
story.append(Paragraph("4. The LLM will generate: Complete Next.js project, All location pages, All static pages, Proper SEO structure, Form submissions, Correct footer and policies", body_style))

# Section 17: Example Usage
story.append(Paragraph("<b>17. EXAMPLE USAGE</b>", h1_style))
story.append(Paragraph("For a new \"whiplash claims\" website:", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("• YOUR_KEYWORD: whiplash claims", bullet_style))
story.append(Paragraph("• YOUR_DOMAIN: https://whiplashclaims.co.uk/", bullet_style))
story.append(Paragraph("• YOUR_FORMSPREE_ENDPOINT: https://formspree.io/f/abc123", bullet_style))
story.append(Spacer(1, 10))
story.append(Paragraph("The prompt will generate a complete website with:", body_style))
story.append(Paragraph("• \"Whiplash Claims\" branding throughout", bullet_style))
story.append(Paragraph("• 12 H2 sections about whiplash claims", bullet_style))
story.append(Paragraph("• County pages: \"Whiplash Claims in Greater London\"", bullet_style))
story.append(Paragraph("• Town pages: \"Whiplash Claims in Manchester, Greater Manchester\"", bullet_style))
story.append(Paragraph("• Footer: \"© 2026 DM Claims. Whiplash Claims is operated by DM Claims...\"", bullet_style))
story.append(Paragraph("• All internal links using whiplash claims context", bullet_style))

# Build PDF
doc.build(story)
print("PDF generated successfully!")
