# Getting Started with RKL Secure Reasoning Brief Agent

**Quick start guide to get your first brief generated in 15 minutes**

---

## What You're Building

A zero-cost, fully automated system that:
- ✅ Monitors AI research feeds
- ✅ Summarizes with local AI (Betty cluster + Ollama)
- ✅ Publishes weekly briefs to your Hugo website
- ✅ Demonstrates Type III secure reasoning
- ✅ Generates audit trails and educational content

**All for $0/month using your home cluster!**

---

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Betty cluster running** - Wake it if needed:
  ```bash
  /home/mike/project/cluster/management/scripts/wake-cluster.sh
  ```

- [ ] **Ollama running on head node** - Test with:
  ```bash
  curl http://192.168.1.10:11434/api/tags
  ```

- [ ] **Python 3.8+** installed:
  ```bash
  python3 --version
  ```

- [ ] **Git configured**:
  ```bash
  git config --global user.name
  git config --global user.email
  ```

---

## Installation (5 minutes)

```bash
# 1. Navigate to project
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief

# 2. Create Python environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# (Edit .env if needed - defaults should work)

# 5. Create necessary directories
mkdir -p data/logs
mkdir -p content/briefs

# 6. Verify Ollama
curl http://192.168.1.10:11434/api/tags
```

**Expected result:** You should see a JSON response with available models.

---

## Generate Your First Brief (10 minutes)

### Option 1: Step by Step (Recommended for First Time)

```bash
# Activate environment
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
source venv/bin/activate

# Step 1: Fetch and summarize articles
echo "Step 1: Fetching RSS feeds and summarizing..."
python scripts/fetch_and_summarize.py

# Check what was created
ls -lh content/briefs/

# Step 2: Generate and publish brief
echo "Step 2: Generating Hugo brief..."
python scripts/publish_brief.py

# Check the output
ls -lh ../website/content/briefs/
```

### Option 2: Single Command

```bash
# Run complete pipeline
scripts/run_weekly.sh
```

---

## What Just Happened?

### Step 1: RSS Collection & Summarization
- ✅ Fetched articles from ArXiv, AI Alignment Forum, etc.
- ✅ Filtered by keywords (verifiable AI, governance, etc.)
- ✅ Summarized each article using **local Ollama** (Betty cluster)
- ✅ Created `content/briefs/YYYY-MM-DD_articles.json`

**Type III in action:** Raw feed content stays local!

### Step 2: Brief Generation & Publishing
- ✅ Analyzed themes across articles
- ✅ Generated recommendations
- ✅ Assembled Hugo-compatible markdown
- ✅ Saved to `../website/content/briefs/YYYY-MM-DD-secure-reasoning-brief.md`

**Type III in action:** Only derived insights published!

---

## View Your Brief

### Local Preview (if Hugo installed)
```bash
cd ../website
hugo server
# Visit http://localhost:1313/briefs/
```

### Published Version (after git push)
```bash
cd ../website
git status
git add content/briefs/
git commit -m "Add Secure Reasoning Brief for $(date +%Y-%m-%d)"
git push
# Netlify will auto-deploy
```

---

## Setup Automated Weekly Generation

### On Betty Head Node (Recommended)

```bash
# SSH to head node
ssh mike-serv@192.168.1.10

# Edit crontab
crontab -e

# Add this line (runs every Monday at 9 AM):
0 9 * * 1 /home/mike/project/rkl-consolidated/secure-reasoning-brief/scripts/run_weekly.sh >> /home/mike/project/rkl-consolidated/secure-reasoning-brief/data/logs/cron.log 2>&1

# Save and exit

# Verify it's scheduled
crontab -l | grep "Secure Reasoning"
```

**That's it!** Briefs will now generate automatically every week.

---

## Customization Quick Start

### Adjust Article Count
```bash
# Edit .env
nano .env

# Change this line:
BRIEF_MAX_ARTICLES=20  # Increase or decrease
```

### Change Feed Sources
```bash
# Edit feed configuration
nano config/feeds.json

# Add/remove feeds or keywords
```

### Fine-Tune Summarizer
```bash
# Edit agent config
nano config/agents/summarizer.yaml

# Adjust:
# - max_words
# - temperature
# - system_prompt
```

---

## Troubleshooting

### "No articles found"
**Solution:** Keywords might be too restrictive
```bash
# Check what was fetched
cat content/briefs/*_articles.json | jq '.articles | length'

# Broaden keywords in config/feeds.json
```

### "Cannot connect to Ollama"
**Solution:** Wake Betty and check Ollama
```bash
# Wake cluster
/home/mike/project/cluster/management/scripts/wake-cluster.sh

# Wait 30 seconds, then test
curl http://192.168.1.10:11434/api/tags

# If still fails, SSH and check service
ssh mike-serv@192.168.1.10 'systemctl status ollama'
```

### "Git push fails"
**Solution:** Configure git credentials
```bash
# Set up git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Or use SSH keys
ssh-keygen -t ed25519 -C "your.email@example.com"
cat ~/.ssh/id_ed25519.pub  # Add to GitHub
```

---

## Next Steps

### Immediate
1. ✅ Generate your first brief
2. ✅ Review the output
3. ✅ Set up weekly cron job
4. ✅ Push to GitHub/Netlify

### This Week
- Read [ARCHITECTURE.md](ARCHITECTURE.md) for full system design
- Explore agent configurations in `config/agents/`
- Review transparency in `public/transparency/`
- Customize for your needs

### This Month
- Generate 4 weekly briefs
- Review quality trends in `telemetry/quality/`
- Create first case study for education
- Fine-tune agent prompts based on results

### Next Quarter
- Plan Phase 1.5 (Full MCP implementation)
- Add more specialized agents
- Develop custom teaching materials
- Consider ADK migration (Phase 2.0)

---

## Learning Resources

### Documentation
- **[README.md](README.md)** - Complete overview
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design
- **[cron/README.md](cron/README.md)** - Scheduling guide

### Configuration Files
- **[config/agents/](config/agents/)** - Agent settings
- **[config/governance/](config/governance/)** - Type III rules
- **[config/orchestration/](config/orchestration/)** - Workflow

### Output Locations
- **`content/briefs/`** - Intermediate JSON
- **`../website/content/briefs/`** - Published briefs
- **`data/logs/`** - Execution logs
- **`telemetry/`** - Performance metrics
- **`audit/`** - Compliance records

---

## Success Indicators

After your first brief, you should see:

✅ **Intermediate JSON file** - `content/briefs/YYYY-MM-DD_articles.json`
✅ **Published brief** - `../website/content/briefs/YYYY-MM-DD-secure-reasoning-brief.md`
✅ **Log files** - `data/logs/weekly-YYYY-MM-DD_HH-MM-SS.log`
✅ **Hugo front matter** - Valid YAML at top of brief
✅ **Articles summarized** - Technical summaries within 80 words
✅ **Themes identified** - Weekly patterns section populated
✅ **Recommendations** - Actionable guidance included

---

## Getting Help

### Check Logs
```bash
# View latest log
ls -lt data/logs/ | head
tail -100 data/logs/weekly-*.log
```

### Verify Components
```bash
# Check Python environment
source venv/bin/activate
pip list | grep -E "feedparser|requests|dotenv"

# Check Ollama models
curl -s http://192.168.1.10:11434/api/tags | jq '.models[].name'

# Check disk space
df -h
```

### Common Issues
- **Slow generation:** Normal for first run (downloading feeds)
- **Empty brief:** Check keywords in `config/feeds.json`
- **Quality issues:** Review `config/agents/qa_reviewer.yaml`
- **Git errors:** Verify repository is clean (`git status`)

---

## Quick Commands Reference

```bash
# Generate brief manually
source venv/bin/activate
python scripts/fetch_and_summarize.py
python scripts/publish_brief.py

# Run full pipeline
scripts/run_weekly.sh

# Check Ollama
curl http://192.168.1.10:11434/api/tags

# View latest brief
ls -lt ../website/content/briefs/ | head
cat ../website/content/briefs/$(ls -t ../website/content/briefs/ | head -1)

# Check logs
tail -f data/logs/weekly-*.log

# Test git publishing
cd ../website
git status
git diff content/briefs/
```

---

**Ready to start?** Run these commands:

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
source venv/bin/activate
scripts/run_weekly.sh
```

**Questions?** Check [README.md](README.md) or [ARCHITECTURE.md](ARCHITECTURE.md)

---

*Last updated: 2025-11-11*
