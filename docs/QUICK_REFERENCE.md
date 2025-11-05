# RKL - Quick Reference

## Folder Structure

```
/home/mike/project/rkl/
│
├── rkl.org/                    📱 PUBLIC website
│   ├── .git/                   → github.com/mbbrady/rkl.org
│   ├── content/                (Hugo content)
│   ├── config.toml
│   └── .gitignore
│
└── rkl-program/                🔒 PRIVATE organization
    ├── .git/                   → github.com/mbbrady/rkl (to create)
    ├── 0_Admin/
    ├── 1_Governance/
    ├── 2_Compliance_and_Filings/
    ├── 3_Operations/
    ├── 4_Programs_and_Research/
    ├── 5_Communications_and_Outreach/
    └── .gitignore
```

## Common Commands

### Website (Public)
```bash
cd /home/mike/project/rkl/rkl.org
hugo server -D              # Preview
hugo                        # Build
git add . && git commit -m "Update" && git push
```

### Organization (Private)
```bash
cd /home/mike/project/rkl/rkl-program
vim 4_Programs_and_Research/Program_Design/Mission_and_Vision.md
git add . && git commit -m "Update" && git push
```

## Security Reminder

❌ NEVER commit:
- .xlsx files with real data
- .pdf files with signatures
- Financial records
- Donor lists
- Personal information

✓ SAFE to commit:
- .md documentation
- Templates
- Folder structure
- README files

## Action Items

1. ⚠️  **Rotate GitHub PAT**: https://github.com/settings/tokens
2. 📦 **Create private repo**: https://github.com/new → name: `rkl` → PRIVATE
3. 📚 **Follow setup**: [rkl-program/SETUP_GITHUB.md](rkl-program/SETUP_GITHUB.md)

## Help

- Full setup: [SETUP_COMPLETE.md](SETUP_COMPLETE.md)
- Security: [rkl-program/SECURITY.md](rkl-program/SECURITY.md)
- Details: [README.md](README.md)
