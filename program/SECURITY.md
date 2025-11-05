# Security & Privacy Guidelines

## Repository Security Policy

This repository contains the **organizational structure and public-facing content** for Resonant Knowledge Lab. All sensitive data is excluded via `.gitignore`.

### ✅ What IS in this repository:
- Folder structure and organization
- README files and documentation
- Template files and examples
- Website content (Hugo static site)
- Public program descriptions
- Draft policies (redacted/template versions)
- Research proposals (public versions)

### ❌ What is NOT in this repository:
- Signed legal documents
- Board member personal information
- Financial records (bank statements, budgets, receipts)
- Donor lists and fundraising data
- Tax returns and IRS correspondence
- Credentials, passwords, API keys
- Contracts with personal information
- Insurance policies
- Signed partnership agreements

## Security Best Practices

### 1. Never Commit Sensitive Data
Before committing:
```bash
git status
git diff
```
Double-check that no sensitive files are being added.

### 2. Use SSH for Git Authentication
Replace HTTPS URLs containing tokens with SSH:
```bash
# Check current remote
git remote -v

# Update to SSH (recommended)
git remote set-url origin git@github.com:mbbrady/rkl.org.git

# Or use HTTPS with credential helper (removes token from URL)
git remote set-url origin https://github.com/mbbrady/rkl.org.git
git config credential.helper store
```

### 3. Rotate Exposed Credentials
**IMPORTANT**: If you accidentally commit sensitive data:
1. Immediately rotate/revoke the credential
2. Remove from Git history: `git filter-branch` or `git filter-repo`
3. Force push: `git push --force`
4. Notify affected parties

### 4. Review .gitignore Regularly
As the organization grows, update `.gitignore` to cover new sensitive data patterns.

### 5. Separate Repositories for Sensitive Work
Consider creating private repositories for:
- Financial planning (separate private repo)
- Board-only materials (private board repo)
- Confidential research data (private data repo)

## Data Classification

### PUBLIC (safe for GitHub)
- Mission, vision, values
- Program descriptions
- Website content
- Public research findings
- Blog posts, press releases
- General documentation

### INTERNAL (exclude from GitHub)
- Board meeting minutes
- Internal strategy documents
- Operational procedures
- Staff/volunteer lists
- Grant applications (until awarded)

### CONFIDENTIAL (exclude from GitHub)
- Financial records
- Donor information
- Legal documents with signatures
- Tax returns
- Personnel files
- Contracts with personal data

### RESTRICTED (exclude from GitHub)
- Bank account information
- Credentials and API keys
- Social Security Numbers / EINs
- Payment processing data
- Research participant data (HIPAA/IRB protected)

## Incident Response

If sensitive data is accidentally committed:

1. **Immediate**: Remove from working directory
   ```bash
   git rm --cached <sensitive-file>
   git commit -m "Remove sensitive data"
   ```

2. **Rotate credentials**: Change passwords, revoke API keys immediately

3. **Clean history**: Use `git filter-repo` or contact GitHub support
   ```bash
   git filter-repo --path <sensitive-file> --invert-paths
   git push --force --all
   ```

4. **Notify**: Inform affected individuals if personal data was exposed

5. **Document**: Log the incident in `0_Admin/Notes/Security_Incidents.md`

## Questions?

If you're unsure whether a file should be committed, ask:
- Would I be comfortable with this being public?
- Does this contain personal information?
- Does this contain financial data?
- Does this contain credentials or secrets?

**When in doubt, leave it out.** You can always add files later, but removing them from Git history is difficult.

---

**Last updated**: 2025-10-14
**Policy owner**: Board of Directors
