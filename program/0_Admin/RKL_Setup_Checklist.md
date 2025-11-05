# RKL Setup & Launch Checklist

**Status Legend:**
- 🟢 **DONE** - Completed
- 🟡 **IN PROGRESS** - Started but not finished
- 🔴 **ON HOLD** - Waiting on something or not started

**Last Updated**: 2025-10-14

---

## 1. Legal Foundation & Incorporation

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🟢 | Incorporate in Virginia | SCC819 filed | `2_Compliance_and_Filings/Incorporation/` |
| 🟢 | Articles of Incorporation | Certificate received | `Articles_of_Incorporation_SCC819.pdf` |
| 🔴 | Apply for EIN (IRS) | Need to complete online application | IRS website |
| 🔴 | Draft Bylaws | Need template and customization | `1_Governance/Bylaws/Drafts/` |
| 🔴 | Adopt Bylaws | Requires organizational meeting | Board action |
| 🔴 | File Form 1023 (501c3) | After EIN, bylaws, and first board meeting | `2_Compliance_and_Filings/IRS/Form_1023_Application/` |

---

## 2. Mission & Strategic Documents

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🟢 | Draft Mission Statement | Core mission defined | `4_Programs_and_Research/Program_Design/Mission_and_Vision.md` |
| 🟢 | Board Mission Document | 9-section comprehensive version | `1_Governance/Board/Mission_Statement_Summary.md` |
| 🟢 | IRS Mission Statement | 501(c)(3) compliant version | `2_Compliance_and_Filings/IRS/Form_1023_Application/Mission_Statement.txt` |
| 🟢 | Define Core Programs | 5 program areas documented | Mission documents |
| 🔴 | Create Logic Model | Program outcomes and impact | `4_Programs_and_Research/Program_Design/Logic_Model.xlsx` |
| 🔴 | Write Evaluation Plan | How to measure success | `4_Programs_and_Research/Program_Design/Evaluation_Plan.md` |

---

## 3. Board Formation & Governance

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🔴 | Recruit Board Members | Need 3+ members (VA requirement) | `1_Governance/Board/Board_Member_List.xlsx` |
| 🔴 | Collect Board Bios | Background and expertise | Meeting packet |
| 🟡 | Prepare Organizational Meeting | Agenda ready, packet in progress | `1_Governance/Organizational_Meeting/` |
| 🟢 | Draft Meeting Agenda | GPT-5's 12-item agenda complete | `Organizational_Meeting/Agenda.md` |
| 🟡 | Assemble Meeting Packet | 3 of 9 documents ready | `Organizational_Meeting/Meeting_Packet/` |
| 🔴 | Hold Organizational Meeting | Not yet scheduled | TBD |
| 🔴 | Elect Officers | Chair, Secretary, Treasurer | During organizational meeting |
| 🔴 | Adopt Conflict of Interest Policy | IRS requirement | `1_Governance/Policies/` |
| 🔴 | Set Board Meeting Schedule | Quarterly minimum | During organizational meeting |

---

## 4. Meeting Packet Documents

| Status | Document | Notes | Action |
|--------|----------|-------|--------|
| 🟢 | Meeting Agenda | ✅ Ready | Customize dates/names |
| 🟢 | Mission Statement | ✅ Ready (9 sections) | Review with board |
| 🟢 | Certificate of Incorporation | ✅ Ready (246KB) | Include in packet |
| 🔴 | Articles of Incorporation PDF | Placeholder is empty | Get actual SCC819 document |
| 🔴 | Draft Bylaws | Not created yet | Create from template |
| 🔴 | Board Member Bios | Template empty | Fill out details |
| 🔴 | Banking Resolution | Not created yet | Use template |
| 🔴 | Initial Budget | Template empty | Create Year 1 budget |
| 🔴 | Conflict of Interest Policy | Template empty | Adopt standard policy |

**Quick Check**: Run `./assemble_packet.sh` in `Organizational_Meeting/Meeting_Packet/` to see current status

---

## 5. Financial Setup

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🔴 | Create Initial Budget | Year 1 revenue/expense projections | `3_Operations/Financials/Budget_2025.xlsx` |
| 🔴 | Open Bank Account | Requires EIN and board resolution | After organizational meeting |
| 🔴 | Set up Accounting System | QuickBooks, Wave, or similar | TBD |
| 🔴 | Establish Fiscal Policies | Expense approval, reimbursement | `3_Operations/Financials/` |
| 🔴 | Set Fiscal Year | Calendar year or other | Board decision |

---

## 6. Website & Communications

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🟢 | Build Website Structure | Hugo site configured | `/home/mike/project/rkl/rkl.org/` |
| 🟢 | Write Mission Content | All pages updated | `rkl.org/content/` |
| 🟢 | Create About Page | Complete with mission/vision | `content/about.md` |
| 🟢 | Create Programs Page | 5 program areas documented | `content/programs.md` |
| 🔴 | Create Contact Page | Need contact form or email | `content/contact.md` |
| 🔴 | Deploy Website | Choose hosting (Netlify/Vercel/GitHub Pages) | TBD |
| 🔴 | Configure Domain DNS | Point resonantknowledgelab.org to hosting | Domain registrar |
| 🔴 | Set up Email | info@resonantknowledgelab.org | Google Workspace or similar |
| 🔴 | Social Media Accounts | Twitter, LinkedIn, etc. | Optional |

---

## 7. Repository & Documentation

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🟢 | Organize File Structure | Dual-repo setup complete | `/home/mike/project/rkl/` |
| 🟢 | Create .gitignore | Comprehensive security rules | Both repos |
| 🟢 | Write CLAUDE.md | Context for AI assistants | 3 files created |
| 🟢 | Document Mission Locations | Guide to all mission docs | `0_Admin/Mission_Statement_Locations.md` |
| 🟢 | Create Security Policy | Data classification guidelines | `SECURITY.md` |
| 🟢 | Fix GitHub PAT Security | Removed from remote URL | ✅ Done |
| 🔴 | Push Private Repo to GitHub | Need to create private repo first | github.com/new |
| 🟡 | Push Website to GitHub | Repo exists, need to push updates | `rkl.org` already has remote |

---

## 8. Technology & Infrastructure

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🟢 | Betty Cluster Operational | Compute infrastructure ready | `/home/mike/project/cluster/` |
| 🔴 | MCP Framework Setup | Model Context Protocol development | `4_Programs_and_Research/` |
| 🔴 | Closed RAG Initiative | Pilot program design | `4_Programs_and_Research/Research_Projects/` |
| 🔴 | Security Protocols | Infrastructure security docs | `3_Operations/Technology/` |

---

## 9. Partnerships & Programs

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🟡 | Arctic AI Collaboration | Ongoing research partnership | `/home/mike/project/cluster/projects/arctic-ai/` |
| 🔴 | Identify 2-3 Partner Organizations | Universities, NGOs, communities | By 2026 |
| 🔴 | TEK Digitization Pilot | Traditional ecological knowledge project | Program design needed |
| 🔴 | Closed RAG Pilot Launch | Secure AI retrieval demo | 2025-2026 goal |

---

## 10. Fundraising & Grants

| Status | Task | Notes | Location |
|--------|------|-------|----------|
| 🔴 | Research Foundation Funders | Ethical tech, cultural knowledge foundations | `5_Communications_and_Outreach/Fundraising/` |
| 🔴 | Create Grant Calendar | Track deadlines for 2025-2026 | Fundraising folder |
| 🔴 | Draft Funding Proposals | Seed funding applications | `4_Programs_and_Research/Program_Design/Funding_Proposals/` |
| 🔴 | Create Donor Management System | Track relationships | `5_Communications_and_Outreach/Fundraising/` |

---

## Critical Path: Next 30 Days

**Priority 1 - Board Formation:**
1. 🔴 Recruit 3+ board members
2. 🔴 Create draft bylaws
3. 🔴 Schedule organizational meeting
4. 🔴 Complete meeting packet (missing docs)

**Priority 2 - Legal Compliance:**
1. 🔴 Apply for EIN
2. 🔴 Prepare Form 1023 materials
3. 🔴 Adopt required policies (COI, etc.)

**Priority 3 - Public Presence:**
1. 🔴 Deploy website
2. 🔴 Set up email
3. 🔴 Push repos to GitHub

---

## Quick Command Reference

### Check Meeting Packet Status
```bash
cd /home/mike/project/rkl/rkl-program/1_Governance/Organizational_Meeting/Meeting_Packet
./assemble_packet.sh
```

### Preview Website
```bash
cd /home/mike/project/rkl/rkl.org
hugo server -D
```

### Check Git Status (Both Repos)
```bash
# Website
cd /home/mike/project/rkl/rkl.org && git status

# Organization
cd /home/mike/project/rkl/rkl-program && git status || echo "Not initialized yet"
```

---

## Resources & Templates

**Nonprofit Resources:**
- VA State Corporation Commission: https://scc.virginia.gov
- IRS Charities & Nonprofits: https://www.irs.gov/charities-non-profits
- Form 1023 Instructions: https://www.irs.gov/forms-pubs/about-form-1023

**Template Sources:**
- Bylaws templates: National Council of Nonprofits
- Conflict of Interest: IRS sample policies
- Banking resolution: Standard nonprofit template

**RKL Documentation:**
- Full setup guide: `SETUP_COMPLETE.md`
- Security policy: `SECURITY.md`
- Board meeting guide: `1_Governance/Board_Meeting_Guide.md`

---

**Maintained by**: RKL Founding Team
**Review Frequency**: Weekly during setup phase
**Last Review**: 2025-10-14
