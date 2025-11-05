# GitHub Setup Guide - RKL Private Repository

This guide walks you through setting up the private GitHub repository for Resonant Knowledge Lab's organizational structure.

---

## Step 1: Rotate Exposed GitHub Token ⚠️ SECURITY

**IMPORTANT**: Your GitHub Personal Access Token (PAT) was exposed in the git remote URL and needs to be rotated immediately.

1. Go to https://github.com/settings/tokens
2. Find the token starting with `github_pat_11AXFDDNA0HMLti...`
3. Click "Delete" or "Regenerate"
4. If regenerating, copy the new token and save it securely (password manager)

**Why this matters**: The exposed token was visible in your git configuration and could be used to access your GitHub account.

---

## Step 2: Create Private GitHub Repository

### On GitHub.com:

1. Go to https://github.com/new
2. **Repository name**: `rkl` (or `rkl-internal` if you prefer)
3. **Description**: "Resonant Knowledge Lab - Internal organizational structure (private)"
4. **Visibility**: Select **Private** ✓ ✓ ✓
5. **Initialize**:
   - ❌ Do NOT add README (we already have one)
   - ❌ Do NOT add .gitignore (we already have one)
   - ❌ Do NOT add license yet
6. Click "Create repository"

### Copy the Repository URL

After creating, you'll see a setup page. Copy the repository URL:
- **SSH** (recommended): `git@github.com:mbbrady/rkl.git`
- **HTTPS**: `https://github.com/mbbrady/rkl.git`

---

## Step 3: Review What Will Be Committed

Before initializing git, let's verify that sensitive files are properly gitignored:

```bash
cd /home/mike/project/rkl/rkl-program

# Check that .gitignore exists
ls -la .gitignore

# Review what would be committed (dry run)
git init
git add -n .

# Review the list carefully - should see:
# - .gitignore, README.md, SECURITY.md
# - 0_Admin/*.md files (but NOT .xlsx files)
# - Folder structure
# - Should NOT see:
#   - Any .pdf files with real data
#   - Any .xlsx files with data
#   - Files with "Donor", "Board_Member", "Financial" in path
```

**STOP and review**: If you see any sensitive files in the output, do NOT proceed. Update `.gitignore` first.

---

## Step 4: Initialize Git Repository

```bash
cd /home/mike/project/rkl/rkl-program

# Initialize git
git init

# Add safe files first
git add .gitignore
git add README.md
git add SECURITY.md
git add SETUP_GITHUB.md

# Add Admin documentation
git add 0_Admin/*.md
git add 0_Admin/Git_Repository_Strategy.md
git add 0_Admin/File_Organization_Notes.md

# Check status
git status

# Review staged files
git diff --cached --name-only

# If everything looks safe, add all files
git add .

# Final check - review what's staged
git status
```

---

## Step 5: Create Initial Commit

```bash
git commit -m "Initial commit: Resonant Knowledge Lab organizational structure

This repository contains the internal organizational structure for RKL,
a Virginia-based 501(c)(3) nonprofit exploring ethical AI and knowledge systems.

Includes:
- Governance documentation structure
- Compliance and filings framework
- Operations templates
- Programs and research project structure
- Communications and outreach materials

Sensitive data excluded via comprehensive .gitignore.
See SECURITY.md for data classification policy."
```

---

## Step 6: Connect to GitHub and Push

### Using SSH (Recommended):

```bash
# Set default branch name
git branch -M main

# Add GitHub remote
git remote add origin git@github.com:mbbrady/rkl.git

# Push to GitHub
git push -u origin main
```

### Using HTTPS (Alternative):

```bash
# Set default branch name
git branch -M main

# Add GitHub remote
git remote add origin https://github.com/mbbrady/rkl.git

# Push to GitHub (will prompt for credentials)
git push -u origin main
# Username: mbbrady
# Password: <use your new PAT>
```

---

## Step 7: Configure GitHub Repository Settings

### On GitHub.com:

1. Go to your repo: https://github.com/mbbrady/rkl
2. Click "Settings"

#### Collaborators
- Settings → Collaborators → Add people
- Invite board members or staff (use GitHub usernames or email)

#### Branch Protection (Optional)
- Settings → Branches → Add rule
- Branch name pattern: `main`
- Enable: "Require pull request reviews before merging"

#### Security
- Settings → Security
- Enable: "Private vulnerability reporting"
- Enable: "Dependabot alerts"

---

## Step 8: Set Up Git Credential Storage (Optional)

To avoid entering your PAT every time:

### Using Git Credential Helper:
```bash
git config --global credential.helper store
# Next time you push, enter PAT - it will be saved
```

### Using SSH (More Secure):
```bash
# Generate SSH key if you don't have one
ssh-keygen -t ed25519 -C "your_email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# https://github.com/settings/keys → New SSH key → Paste

# Test connection
ssh -T git@github.com
```

---

## Step 9: Create .github/workflows (Optional CI/CD)

For automated checks:

```bash
mkdir -p .github/workflows
```

Create `.github/workflows/sensitive-data-check.yml`:
```yaml
name: Sensitive Data Check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check for sensitive patterns
        run: |
          ! git diff-tree --no-commit-id --name-only -r HEAD | xargs grep -l "password\|api_key\|secret"
```

---

## Verification Checklist

After setup, verify:

- [ ] Repository is set to **Private** on GitHub
- [ ] You can view the repo at github.com/mbbrady/rkl
- [ ] No sensitive files are visible in the repository
- [ ] You've rotated the exposed GitHub PAT
- [ ] README.md and SECURITY.md are visible
- [ ] Folder structure is intact
- [ ] .gitignore is working (check by trying to `git add` a sensitive file)

---

## Daily Workflow

### Adding New Files
```bash
cd /home/mike/project/rkl/rkl-program

# Make changes
vim 4_Programs_and_Research/Program_Design/Mission_and_Vision.md

# Check status
git status

# Review diff
git diff

# Stage changes
git add 4_Programs_and_Research/Program_Design/Mission_and_Vision.md

# Commit
git commit -m "Update mission and vision statement"

# Push
git push
```

### Before Committing Sensitive Files
```bash
# Always check what you're committing
git status
git diff --cached

# If you accidentally stage a sensitive file
git reset HEAD path/to/sensitive/file
```

---

## Troubleshooting

### "fatal: Authentication failed"
- Your PAT expired or is wrong
- Regenerate at https://github.com/settings/tokens
- Use the new token as your password

### "Permission denied (publickey)"
- Your SSH key isn't set up
- Follow Step 8 to add SSH key to GitHub

### "Repository not found"
- Check repo name and visibility
- Verify you have access: https://github.com/mbbrady/rkl

### Accidentally committed sensitive data
1. **DON'T PANIC**
2. Remove from working directory immediately
3. Follow incident response in [SECURITY.md](SECURITY.md)
4. Rotate any exposed credentials
5. Use `git filter-repo` to clean history

---

## Questions?

- GitHub Help: https://docs.github.com
- Git Documentation: https://git-scm.com/doc
- RKL Security Policy: [SECURITY.md](SECURITY.md)

---

**Last updated**: 2025-10-14
