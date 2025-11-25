# Rate Limiting Fix for Gemini Free Tier

**Date:** November 25, 2025, 8:15 AM
**Issue:** Pipeline failing with 429 quota errors on Gemini API (15 requests/minute limit)
**Solution:** Added automatic rate limiting to gemini_client.py

## Problem

The Nov 24, 9 PM pipeline run failed with:
```
google.api_core.exceptions.ResourceExhausted: 429 You exceeded your current quota
Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests
limit: 15, model: gemini-2.0-flash
quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
```

**Root cause:** API keys from Google AI Studio (AIzaSy...) are on the free tier with a hard limit of **15 requests per minute** per model. The pipeline was making requests faster than this limit.

## Solution Implemented

Modified `scripts/gemini_client.py` to add automatic rate limiting:

### Changes Made:

1. **Added rate limiting attributes to `__init__`:**
   ```python
   # Rate limiting for free tier (15 requests/minute)
   self.last_request_time = 0
   self.min_request_interval = 4.5  # 4.5 seconds = ~13 requests/minute (safe margin)
   ```

2. **Added sleep logic to `generate()` method:**
   ```python
   # Rate limiting: ensure minimum time between requests
   time_since_last_request = time.time() - self.last_request_time
   if time_since_last_request < self.min_request_interval:
       sleep_time = self.min_request_interval - time_since_last_request
       logger.info(f"Rate limiting: sleeping {sleep_time:.2f}s before API call")
       time.sleep(sleep_time)

   # ... make API call ...
   self.last_request_time = time.time()  # Update timestamp
   ```

### Impact:

- **Throughput:** Maximum ~13 requests/minute (safe margin below 15/min limit)
- **Per-request overhead:** 4.5 seconds between calls
- **Pipeline duration:** Will take longer, but won't fail with quota errors
- **Cost:** Still free tier (no additional charges)

### Expected Behavior:

The pipeline logs will now show:
```
Rate limiting: sleeping 4.50s before API call
Rate limiting: sleeping 3.21s before API call
Rate limiting: sleeping 4.50s before API call
```

This is **normal and expected** - it's preventing quota exhaustion.

## Testing

```bash
# Test that client loads correctly
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
python3 -c "from scripts.gemini_client import GeminiClient; print('✅ OK')"
```

Result: ✅ Passed

## Next Steps

### For 9 AM Run (Nov 25):
The pipeline should now complete successfully, just slower. Monitor:
```bash
tail -f /home/mike/project/rkl-consolidated/secure-reasoning-brief/logs/cron/pipeline_2025-11-25_090001.log
```

### Long-term Solution (After Capstone):

**Option 1: Upgrade to Google Cloud Vertex AI (Paid)**
- Proper paid tier with higher quotas
- Requires service account JSON credentials
- Setup time: 15-30 minutes
- Cost: Pay-per-token (~$0.000125/1K tokens for Gemini 2.0 Flash)

**Option 2: Request Quota Increase**
- Google AI Studio sometimes grants quota increases for free tier
- Go to: https://ai.google.dev/gemini-api/docs/quota-increase
- May take days for approval

**Option 3: Multi-key rotation**
- Use multiple free-tier API keys
- Rotate between them automatically
- More complex, not recommended

## Files Modified

- `scripts/gemini_client.py` - Added rate limiting to `GeminiClient` class

## Verification Checklist

- ✅ Code loads without errors
- ⏳ 9 AM pipeline run (waiting for 8:57 AM)
- ⏳ Verify daily brief generation succeeds
- ⏳ Check demo/daily_briefs.html is updated

---

*Rate limiting fix for RKL Secure Reasoning Brief*
*Ensures Gemini free tier compatibility for Kaggle AI Agents Capstone*
