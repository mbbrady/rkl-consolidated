# Competition Demo: Automated Blog Presentation

## Problem

You have:
- ✅ Automated pipeline generating briefs with Gemini analysis
- ✅ JSON output with rich metadata
- ❌ No live website yet
- 🎯 Need to demonstrate blog concept for competition submission

## Solution: Static Demo Site

Create a **static HTML demo** that shows what the automated blog would look like, without requiring actual website integration.

---

## Demo Components

### 1. Generate Static HTML Blog Pages

**Create:**
```
demo-blog/
├── index.html                    # Latest brief (Nov 20)
├── archive.html                  # List of all briefs
├── article-detail.html           # Deep dive on one article
├── about.html                    # Explains the system
└── assets/
    ├── style.css                 # RKL branding
    └── sample-telemetry.png      # Phase-0 data viz
```

**Content sources:**
- Latest JSON brief (`content/briefs/2025-11-20_articles.json`)
- Enhanced with Gemini analysis (once implemented)
- Phase-0 telemetry screenshots
- System architecture diagram

### 2. Python Script to Generate HTML

**Create:** `scripts/generate_demo_blog.py`

```python
"""
Generate static HTML blog from JSON briefs for competition demo.
Shows what the automated RKL blog would look like.
"""

def generate_blog_html(brief_json: dict) -> str:
    """Convert brief JSON to styled HTML blog post"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secure Reasoning Research Brief - {brief_json['generated_at']}</title>
        <link rel="stylesheet" href="assets/style.css">
    </head>
    <body>
        <header>
            <h1>🔒 Secure Reasoning Research Brief</h1>
            <p class="date">{brief_json['generated_at']}</p>
            <p class="tagline">Expert-curated AI safety research with automated analysis</p>
        </header>

        <main>
            <section class="summary">
                <h2>Daily Digest</h2>
                <p>{len(brief_json['articles'])} articles curated by hybrid AI system:</p>
                <ul>
                    <li>Ollama (llama3.2:3b): Technical summaries</li>
                    <li>Gemini (2.0-flash): Expert secure reasoning analysis</li>
                </ul>
            </section>

            <section class="articles">
                {render_articles(brief_json['articles'])}
            </section>
        </main>

        <footer>
            <p>Generated automatically 2x daily | Phase-0 Research Telemetry Enabled</p>
            <p><a href="archive.html">View Archive</a> |
               <a href="about.html">About This System</a></p>
        </footer>
    </body>
    </html>
    """
    return html

def render_articles(articles: list) -> str:
    """Render articles with Gemini analysis highlighted"""
    html = ""
    for article in articles:
        html += f"""
        <article class="research-brief">
            <header>
                <h3>{article['title']}</h3>
                <div class="meta">
                    <span class="source">{article['source']}</span>
                    <span class="date">{article['date']}</span>
                    <a href="{article['link']}" class="arxiv-link">📄 Full Paper</a>
                </div>
            </header>

            <section class="ollama-summary">
                <h4>Technical Summary <span class="ai-badge">Ollama</span></h4>
                <p>{article['technical_summary']}</p>
            </section>

            <section class="lay-explanation">
                <h4>Lay Explanation <span class="ai-badge">Ollama</span></h4>
                <p>{article['lay_explanation']}</p>
            </section>

            <section class="gemini-analysis highlight">
                <h4>🔍 Secure Reasoning Analysis <span class="ai-badge">Gemini</span></h4>

                <div class="analysis-score">
                    <strong>Relevance Score:</strong>
                    {article.get('gemini_analysis', {}).get('relevance_score', 'N/A')} / 1.0
                </div>

                <div class="why-matters">
                    <strong>Why This Matters:</strong>
                    <p>{article.get('gemini_analysis', {}).get('why_this_matters',
                       'Gemini analysis coming soon...')}</p>
                </div>

                <div class="connections">
                    <strong>Secure Reasoning Connection:</strong>
                    <p>{article.get('gemini_analysis', {}).get('secure_reasoning_connection',
                       'Analysis pending...')}</p>
                </div>

                <div class="practical-value">
                    <strong>Practical Implications:</strong>
                    <p>{article.get('gemini_analysis', {}).get('practical_value',
                       'Coming soon...')}</p>
                </div>

                <div class="recommendation">
                    <strong>Recommendation:</strong>
                    <span class="badge {article.get('gemini_analysis', {}).get('recommendation', 'pending')}">
                        {article.get('gemini_analysis', {}).get('recommendation', 'pending').upper()}
                    </span>
                </div>
            </section>

            <footer class="article-tags">
                {render_tags(article.get('tags', []))}
            </footer>
        </article>
        """
    return html
```

### 3. Visual Design (CSS)

**Key elements:**
```css
/* Highlight Gemini analysis section */
.gemini-analysis {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 8px;
    margin: 1rem 0;
}

/* AI badges */
.ai-badge {
    background: #4299e1;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.875rem;
    font-weight: 600;
}

/* Recommendation badges */
.badge.must-include { background: #48bb78; }
.badge.include { background: #4299e1; }
.badge.consider { background: #ed8936; }
.badge.exclude { background: #f56565; }
```

### 4. About Page

**Explains the system:**
```html
<h2>About This Automated Blog</h2>

<h3>What You're Seeing</h3>
<p>This is a demonstration of an <strong>autonomous AI research curation system</strong>
built for the Kaggle "5-Day AI Agents Intensive" Capstone Competition.</p>

<h3>How It Works</h3>
<ol>
    <li><strong>Automated Monitoring</strong>: Scrapes ArXiv, AI Alignment Forum,
        Google AI Blog 2x daily</li>
    <li><strong>Local Processing</strong>: Ollama (llama3.2:3b) generates technical
        summaries and lay explanations</li>
    <li><strong>Expert Analysis</strong>: Gemini (2.0-flash) evaluates secure reasoning
        relevance and provides original analysis</li>
    <li><strong>Phase-0 Telemetry</strong>: All reasoning steps logged for auditability</li>
    <li><strong>Auto-Publication</strong>: Generates daily briefs in JSON format</li>
</ol>

<h3>The Hybrid Model</h3>
<table>
    <tr>
        <th>Component</th>
        <th>Role</th>
        <th>Why This Model</th>
    </tr>
    <tr>
        <td>Ollama (Local)</td>
        <td>Summarization</td>
        <td>Privacy-preserving, cost-effective, fast</td>
    </tr>
    <tr>
        <td>Gemini (Cloud)</td>
        <td>Expert Analysis</td>
        <td>Domain expertise, nuanced evaluation, quality</td>
    </tr>
</table>

<h3>Unique Value</h3>
<ul>
    <li>✅ <strong>Expert curation</strong> of secure reasoning research</li>
    <li>✅ <strong>Original analysis</strong> not found in papers</li>
    <li>✅ <strong>Practitioner focus</strong> on implications and value</li>
    <li>✅ <strong>Fully automated</strong> requiring no human intervention</li>
    <li>✅ <strong>Auditable</strong> via Phase-0 research telemetry</li>
</ul>

<h3>Competition Deliverable → Production System</h3>
<p>After the competition, this demo becomes a <strong>live RKL website</strong>
serving the AI safety and governance community with daily expert-curated research.</p>
```

---

## Demo Presentation Strategy

### For Competition Submission

**Package includes:**

1. **Static HTML Demo** (demo-blog/ folder)
   - Open `demo-blog/index.html` in browser
   - Shows 20 articles with full Gemini analysis
   - Demonstrates blog concept visually

2. **README.md** in demo-blog/
   ```markdown
   # Automated Blog Demo

   This demonstrates what the production RKL blog will look like.

   ## To View:
   1. Open `index.html` in your browser
   2. Browse articles with Gemini analysis
   3. See archive and about pages

   ## What This Shows:
   - Hybrid model in action (Ollama + Gemini)
   - Expert secure reasoning analysis on every article
   - Automated curation workflow
   - Phase-0 telemetry integration

   ## Post-Competition:
   - Deploy to https://rkl.org/secure-reasoning-research
   - Add search/filter functionality
   - Enable RSS feed
   - Connect to live pipeline
   ```

3. **Video/Screenshots** showing:
   - Latest brief with Gemini analysis
   - Archive of multiple days
   - About page explaining system
   - Phase-0 telemetry dashboard

### For Documentation

**In competition write-up:**
```markdown
### Practical Application: Automated Research Blog

The system generates daily curated briefs published as an automated blog:

**Production Vision:**
- URL: https://rkl.org/secure-reasoning-research
- Updates: 2x daily (9 AM, 9 PM)
- Content: 15-20 articles with expert analysis
- Audience: AI safety/governance practitioners

**Demo:** See `demo-blog/` folder for static HTML demonstration

**Value Proposition:**
Instead of manually reading 100+ AI papers daily, practitioners get:
- Pre-filtered secure reasoning research
- Expert analysis of relevance and implications
- Practical guidance on what matters and why
- Fully automated, requiring zero human curation
```

---

## Implementation Steps

1. ✅ Implement Gemini enhancement (add analysis to JSON)
2. Create `scripts/generate_demo_blog.py`
3. Design CSS with RKL branding
4. Generate HTML from latest brief
5. Add 2-3 historical briefs to show archive
6. Screenshot Phase-0 telemetry dashboard
7. Write about page
8. Test in multiple browsers
9. Package as `demo-blog/` in submission
10. Reference in documentation and video

---

## Post-Competition: Website Integration

**After submission, separately tackle:**
- Deploy to actual RKL website
- Add backend (Flask/FastAPI)
- Implement search/filter
- Enable RSS feed
- Connect live pipeline
- Add user subscriptions
- Analytics dashboard

**Timeline:** 2-3 weeks post-competition

---

## Summary

**For competition:** Static HTML demo showing the concept
**After competition:** Full website integration

This lets you:
- Demonstrate the blog value without website complexity
- Focus on core AI system for competition
- Have clear post-competition deployment path
- Show "production-ready" vision to judges

The demo is **sufficient to convey the value** without requiring actual web infrastructure for the submission deadline.
