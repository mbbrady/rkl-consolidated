# How to Assemble the Meeting Packet

The Meeting_Packet folder is a **staging area** where you gather copies of documents from across the organization for your board members.

---

## Documents You Need and Where They Are

### ✅ Available Now

1. **Meeting Agenda**
   - Location: `../Agenda.md`
   - Action: Copy or symlink here

2. **Mission Statement (Full Board Version)**
   - Location: `../../Board/Mission_Statement_Summary.md`
   - Action: Copy here
   - This is the comprehensive 9-section document

3. **Articles of Incorporation**
   - Location: `../../../2_Compliance_and_Filings/Incorporation/Articles_of_Incorporation_SCC819.pdf`
   - Action: Copy here

4. **Certificate of Incorporation** (if different from Articles)
   - Location: `../../../2_Compliance_and_Filings/Incorporation/Certificate_of_Incorporation.pdf`
   - Action: Copy here

### ⏳ Need to Create

5. **Draft Bylaws**
   - Location: `../../Bylaws/Drafts/` (create here first)
   - Action: Copy to packet when ready

6. **Board Member List & Bios**
   - Location: `../../Board/Board_Member_List.xlsx` (exists but empty)
   - Action: Fill out, export to PDF, copy here

7. **Banking Resolution Template**
   - Need to create
   - Action: Create in `../../../3_Operations/Financials/`, copy here

8. **Initial Budget**
   - Location: `../../../3_Operations/Financials/Budget_[YYYY].xlsx` (exists but empty)
   - Action: Fill out, copy here

9. **Conflict of Interest Policy**
   - Location: `../../Policies/Conflict_of_Interest_Policy.pdf` (exists but empty)
   - Action: Create policy, copy here

---

## Quick Copy Commands

Run these from this directory to copy available documents:

```bash
# Copy agenda
cp ../Agenda.md ./01_Agenda.md

# Copy mission statement
cp ../../Board/Mission_Statement_Summary.md ./02_Mission_Statement.md

# Copy Articles of Incorporation
cp ../../../2_Compliance_and_Filings/Incorporation/Articles_of_Incorporation_SCC819.pdf ./03_Articles_of_Incorporation.pdf

# Copy Certificate if different
cp ../../../2_Compliance_and_Filings/Incorporation/Certificate_of_Incorporation.pdf ./04_Certificate_of_Incorporation.pdf
```

---

## Or Use Symlinks (Recommended for Draft Stage)

Symlinks let you reference the original files without duplicating. Useful while documents are still changing:

```bash
# Symlink to agenda
ln -s ../Agenda.md ./01_Agenda.md

# Symlink to mission
ln -s ../../Board/Mission_Statement_Summary.md ./02_Mission_Statement.md

# Symlink to Articles
ln -s ../../../2_Compliance_and_Filings/Incorporation/Articles_of_Incorporation_SCC819.pdf ./03_Articles_of_Incorporation.pdf
```

---

## Numbering System

Prefix files with numbers to maintain order in the packet:

- `01_Agenda.md`
- `02_Mission_Statement.md`
- `03_Articles_of_Incorporation.pdf`
- `04_Certificate_of_Incorporation.pdf`
- `05_Draft_Bylaws.pdf`
- `06_Board_Member_Bios.pdf`
- `07_Banking_Resolution_Template.pdf`
- `08_Initial_Budget.pdf`
- `09_Conflict_of_Interest_Policy.pdf`

---

## For Distribution

### Digital Distribution
1. Keep documents in this folder
2. Upload this entire folder to Google Drive / Dropbox
3. Share link with board members
4. Or zip and email: `zip -r Board_Packet.zip Meeting_Packet/`

### Physical Distribution
1. Print all documents from this folder
2. Organize in binders with tabs
3. Include table of contents
4. Mail or hand-deliver 1 week before meeting

---

## What's Actually Empty vs. What Exists

Let me check what files are actually populated vs. placeholders...
