#!/bin/bash
# Assemble Board Meeting Packet
# This script copies/symlinks available documents into the Meeting_Packet folder

set -e  # Exit on error

PACKET_DIR="/home/mike/project/rkl/rkl-program/1_Governance/Organizational_Meeting/Meeting_Packet"
cd "$PACKET_DIR"

echo "=========================================="
echo "Assembling RKL Board Meeting Packet"
echo "=========================================="
echo ""

# Function to safely copy or symlink
copy_doc() {
    local src="$1"
    local dest="$2"
    local name="$3"

    if [ -f "$src" ]; then
        # Check if file has actual content (not just placeholder)
        if [ -s "$src" ]; then
            echo "✓ Found: $name"
            cp "$src" "$dest"
        else
            echo "⚠ Empty: $name (placeholder file)"
        fi
    else
        echo "✗ Missing: $name"
    fi
}

echo "Copying available documents..."
echo ""

# 01 - Agenda
copy_doc "../Agenda.md" \
         "./01_Agenda.md" \
         "Meeting Agenda"

# 02 - Mission Statement
copy_doc "../../Board/Mission_Statement_Summary.md" \
         "./02_Mission_Statement.md" \
         "Mission Statement (Board Version)"

# 03 - Articles of Incorporation
copy_doc "../../../2_Compliance_and_Filings/Incorporation/Articles_of_Incorporation_SCC819.pdf" \
         "./03_Articles_of_Incorporation.pdf" \
         "Articles of Incorporation"

# 04 - Certificate of Incorporation (if different)
copy_doc "../../../2_Compliance_and_Filings/Incorporation/Certificate_of_Incorporation.pdf" \
         "./04_Certificate_of_Incorporation.pdf" \
         "Certificate of Incorporation"

# 05 - Draft Bylaws (check multiple locations)
if [ -f "../../Bylaws/Drafts"/*.pdf 2>/dev/null ]; then
    echo "✓ Found: Draft Bylaws"
    cp ../../Bylaws/Drafts/*.pdf ./05_Draft_Bylaws.pdf 2>/dev/null || true
else
    echo "⚠ Not ready: Draft Bylaws (create in ../../Bylaws/Drafts/)"
fi

# 06 - Board Member List
copy_doc "../../Board/Board_Member_List.xlsx" \
         "./06_Board_Member_List.xlsx" \
         "Board Member List"

# 07 - Banking Resolution
if [ -f "../../../3_Operations/Financials/Banking_Resolution.pdf" ]; then
    copy_doc "../../../3_Operations/Financials/Banking_Resolution.pdf" \
             "./07_Banking_Resolution.pdf" \
             "Banking Resolution"
else
    echo "⚠ Not ready: Banking Resolution (need to create)"
fi

# 08 - Initial Budget
copy_doc "../../../3_Operations/Financials/Budget_[YYYY].xlsx" \
         "./08_Initial_Budget.xlsx" \
         "Initial Budget"

# 09 - Conflict of Interest Policy
copy_doc "../../Policies/Conflict_of_Interest_Policy.pdf" \
         "./09_Conflict_of_Interest_Policy.pdf" \
         "Conflict of Interest Policy"

echo ""
echo "=========================================="
echo "Packet Assembly Complete"
echo "=========================================="
echo ""
echo "Documents in packet:"
ls -lh *.{md,pdf,xlsx} 2>/dev/null || echo "  (No documents copied yet)"
echo ""
echo "Next steps:"
echo "  1. Create missing documents (see warnings above)"
echo "  2. Review all copied documents"
echo "  3. Combine into single PDF or share folder with board"
echo ""
