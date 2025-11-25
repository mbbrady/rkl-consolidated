# Vertex AI Paid Tier Setup - Step by Step

**Goal:** Upgrade from Google AI Studio free tier to Vertex AI paid tier
**Time Required:** 15-30 minutes
**Deadline:** Before 9 AM run (Nov 25, 2025)

---

## Step 1: Google Cloud Console Setup (5-10 minutes)

### 1.1 Go to Google Cloud Console
Open in browser: https://console.cloud.google.com/

### 1.2 Select or Create a Project
- Click the project dropdown at the top
- Either select an existing project OR click "New Project"
- If creating new: Name it something like "rkl-vertex-ai"
- Click "Create"

### 1.3 Enable Billing
**This is required for paid tier:**
1. Go to: https://console.cloud.google.com/billing
2. Click "Link a Billing Account" (or create new billing account)
3. Add payment method (credit card)
4. Confirm billing is ACTIVE for your project

**Verify billing is enabled:**
- Top of console should show your project name
- Billing should say "Billing enabled" (not "No billing account")

### 1.4 Enable Vertex AI API
1. Go to: https://console.cloud.google.com/apis/library/aiplatform.googleapis.com
2. Click "Enable" button
3. Wait for API to enable (~1 minute)
4. You should see "API enabled" checkmark

---

## Step 2: Create Service Account (5 minutes)

### 2.1 Go to Service Accounts
https://console.cloud.google.com/iam-admin/serviceaccounts

### 2.2 Create Service Account
1. Click "**+ CREATE SERVICE ACCOUNT**" at top
2. **Service account name:** `rkl-vertex-ai-sa`
3. **Service account ID:** Will auto-fill (rkl-vertex-ai-sa)
4. **Description:** "Service account for RKL Secure Reasoning Brief Vertex AI access"
5. Click "**CREATE AND CONTINUE**"

### 2.3 Grant Permissions
**Select role:**
1. Type "Vertex AI" in the role search box
2. Select: **"Vertex AI User"**
3. Click "**CONTINUE**"

### 2.4 Done with Service Account
Click "**DONE**" (skip optional step 3)

---

## Step 3: Create and Download JSON Key (2 minutes)

### 3.1 Find Your Service Account
In the service accounts list, find: `rkl-vertex-ai-sa@your-project-id.iam.gserviceaccount.com`

### 3.2 Create Key
1. Click on the service account email (opens details)
2. Go to "**KEYS**" tab at top
3. Click "**ADD KEY**" dropdown
4. Select "**Create new key**"
5. **Key type:** Select "**JSON**" (default)
6. Click "**CREATE**"

### 3.3 Download JSON
- A JSON file will download automatically
- **Filename:** `your-project-id-xxxxxxxxxxxx.json`
- **IMPORTANT:** Note where it downloaded (usually ~/Downloads/)

---

## Step 4: Move JSON Key to Secure Location (1 minute)

### On your thin client, run:

```bash
# Create credentials directory
mkdir -p /home/mike/.gcp-credentials

# Move the downloaded JSON key (adjust filename as needed)
mv ~/Downloads/your-project-*.json /home/mike/.gcp-credentials/vertex-ai-key.json

# Secure the file (only you can read it)
chmod 600 /home/mike/.gcp-credentials/vertex-ai-key.json

# Verify it's there
ls -la /home/mike/.gcp-credentials/vertex-ai-key.json
```

**Output should show:**
```
-rw------- 1 mike mike 2345 Nov 25 08:30 /home/mike/.gcp-credentials/vertex-ai-key.json
```

---

## Step 5: Get Your Project ID (1 minute)

### Find your Google Cloud Project ID:

**Option A: From Console**
- Top of Google Cloud Console shows project name
- Click it - you'll see "Project ID" underneath
- Copy the project ID (NOT the project name)

**Option B: From JSON file**
```bash
cat /home/mike/.gcp-credentials/vertex-ai-key.json | grep project_id
```

Output will show: `"project_id": "your-project-id-123456"`

**Write down your Project ID:** _________________________

---

## Step 6: Update RKL Environment Variables (2 minutes)

### Edit .env file:

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
nano .env
```

### Add these lines at the bottom:

```bash
# Vertex AI Configuration (Paid Tier)
USE_VERTEX_AI=true
VERTEX_AI_PROJECT_ID=your-project-id-here
VERTEX_AI_LOCATION=us-central1
VERTEX_AI_CREDENTIALS=/home/mike/.gcp-credentials/vertex-ai-key.json
```

**Replace `your-project-id-here` with your actual project ID!**

### Save and exit:
- Press `Ctrl+O` (save)
- Press `Enter` (confirm)
- Press `Ctrl+X` (exit)

---

## Step 7: Install Vertex AI Python Library (2 minutes)

```bash
# Activate conda environment
conda activate rkl-briefs

# Install Vertex AI SDK
pip install google-cloud-aiplatform

# Verify installation
python3 -c "import vertexai; print('✅ Vertex AI SDK installed')"
```

---

## Step 8: Update Gemini Client Code (5 minutes)

**I will do this step for you** - need to modify `scripts/gemini_client.py` to:
1. Detect `USE_VERTEX_AI=true` in environment
2. Use Vertex AI SDK instead of AI Studio API
3. Authenticate with service account JSON
4. Use paid tier quotas (much higher)

**Wait for me to complete this step...**

---

## Step 9: Test Vertex AI Connection (2 minutes)

After I update the code, test:

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief

# Test Vertex AI connection
python3 -c "
from scripts.gemini_client import GeminiClient
client = GeminiClient()
response = client.generate('Say hello', agent_id='test')
print(f'✅ Vertex AI working: {response[:50]}...')
"
```

---

## Step 10: Verify Billing and Quotas

### Check your quota status:
https://console.cloud.google.com/iam-admin/quotas

Search for: "Vertex AI API"

**Paid tier should show:**
- ✅ Much higher request limits (1000+ per minute)
- ✅ No "free tier" designation

---

## Estimated Costs (Vertex AI Gemini 2.0 Flash)

**Pricing:**
- Input: ~$0.000075 per 1K tokens
- Output: ~$0.00030 per 1K tokens

**Daily brief run estimate:**
- ~20 Gemini calls per run
- ~500 tokens per call average
- Cost per run: ~$0.01-0.03
- Daily cost (2 runs): ~$0.02-0.06
- Monthly: ~$0.60-1.80

**Very affordable for a research project!**

---

## Troubleshooting

### "Permission denied" on JSON key
```bash
chmod 600 /home/mike/.gcp-credentials/vertex-ai-key.json
```

### "Project not found"
- Verify project ID is correct (check JSON file or console)
- Verify billing is enabled for that project

### "API not enabled"
- Go back to Step 1.4 and enable Vertex AI API

### "Service account lacks permission"
- Go back to Step 2.3 and ensure "Vertex AI User" role is granted

---

## Current Status

- [ ] Step 1: Google Cloud Console setup
- [ ] Step 2: Create service account
- [ ] Step 3: Download JSON key
- [ ] Step 4: Move JSON key to secure location
- [ ] Step 5: Get project ID
- [ ] Step 6: Update .env file
- [ ] Step 7: Install Vertex AI SDK
- [ ] Step 8: Update gemini_client.py (I'll do this)
- [ ] Step 9: Test connection
- [ ] Step 10: Verify billing

---

**Let me know when you complete Steps 1-7, then I'll immediately update the code (Step 8)**

Time remaining until 9 AM: ~30 minutes
