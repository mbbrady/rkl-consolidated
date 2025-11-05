# RKL Quick Start Guide

**Keep this handy!** Quick reference for key locations and commands.

---

## 🎯 Most Important Files

### Mission Statements
```
Master:     4_Programs_and_Research/Program_Design/Mission_and_Vision.md
Board:      1_Governance/Board/Mission_Statement_Summary.md
IRS:        2_Compliance_and_Filings/IRS/Form_1023_Application/Mission_Statement.txt
```

### First Board Meeting
```
Agenda:     1_Governance/Organizational_Meeting/Agenda.md
Packet:     1_Governance/Organizational_Meeting/Meeting_Packet/
Status:     Run ./assemble_packet.sh in Meeting_Packet folder
```

### Checklists
```
Main:       0_Admin/RKL_Setup_Checklist.md  ← Your complete todo list!
```

---

## 🚀 Quick Commands

### Check Meeting Packet Status
```bash
cd ~/project/rkl/rkl-program/1_Governance/Organizational_Meeting/Meeting_Packet
./assemble_packet.sh
```

### Preview Website
```bash
cd ~/project/rkl/rkl.org
hugo server -D
# Open: http://localhost:1313
```

### View Checklist
```bash
cat ~/project/rkl/rkl-program/0_Admin/RKL_Setup_Checklist.md | less
```

---

## 📋 Status at a Glance

**🟢 DONE:**
- Incorporated in Virginia (SCC819)
- Mission documented (3 versions)
- Website built (Hugo)
- Folder structure organized
- First meeting agenda ready

**🟡 IN PROGRESS:**
- Meeting packet (3 of 9 docs ready)
- Arctic AI collaboration
- Website deployment

**🔴 NEED TO DO:**
- Apply for EIN
- Create bylaws
- Recruit board members
- Hold organizational meeting
- File Form 1023

---

## 🆘 Help! Where is...?

**Q: Where do board meeting docs go?**
A: First meeting → `1_Governance/Organizational_Meeting/`
   Future meetings → `1_Governance/Board/Board_Meeting_Minutes/`

**Q: How do I assemble the meeting packet?**
A: `cd` to `Meeting_Packet/` and run `./assemble_packet.sh`

**Q: Where's the comprehensive checklist?**
A: `0_Admin/RKL_Setup_Checklist.md` (color-coded with 🟢🟡🔴)

**Q: What's the mission statement?**
A: "To make human knowledge — in all its cultural, institutional, and environmental forms — discoverable, accessible, and securely interoperable with AI."

**Q: Where's the full documentation?**
A: Read `CLAUDE.md` in any folder for context

---

## 📞 Key Info

**Organization**: Resonant Knowledge Lab
**Location**: Virginia, USA
**Status**: 501(c)(3) Nonprofit (in formation)
**Website**: resonantknowledgelab.org
**Tagline**: Ethical AI for Living Knowledge

---

## 🔗 Folder Structure (Simplified)

```
rkl-program/
├── 0_Admin/          ← YOU ARE HERE! (guides, checklists)
├── 1_Governance/     ← Board meetings, bylaws, policies
├── 2_Compliance/     ← Legal docs, IRS, Virginia
├── 3_Operations/     ← Financials, HR, technology
├── 4_Programs/       ← Mission, research projects
└── 5_Communications/ ← Website materials, fundraising
```

---

**Pro Tip**: Bookmark this file in your editor!

**Last Updated**: 2025-10-14
