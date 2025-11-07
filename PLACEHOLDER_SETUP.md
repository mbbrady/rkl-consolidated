# Placeholder Site Setup

**Status:** Deployed and waiting for domain connection

## Current Placeholder Content

The placeholder shows:
- **Headline:** Resonant Knowledge Lab
- **Tagline:** Building open, verifiable frameworks for secure reasoning with AI
- **Status:** Full website launching soon
- **Contact:** info@resonantknowledgelab.org

**Design:**
- Navy blue gradient background
- Frosted glass card effect
- Responsive mobile design
- Clean, professional appearance

## Deployment Status

✅ **Placeholder HTML created** - Located at `placeholder/index.html`
✅ **Cloudflare Pages project created** - Project name: `rkl-placeholder`
✅ **Domain added to Cloudflare** - `resonantknowledgelab.org`
⏳ **Waiting for nameserver propagation** - Status shows "Invalid nameservers" (15min - 48hrs)
⏳ **Connect domain to Pages project** - After nameservers are active

## Next Steps

### Once nameservers are active (status changes to green checkmark):

1. Go to **Workers & Pages** → **rkl-placeholder**
2. Click **Custom domains** tab
3. Click **"Set up a custom domain"**
4. Enter: `resonantknowledgelab.org`
5. Cloudflare will automatically create DNS records
6. Site will be live at https://resonantknowledgelab.org within minutes

### To update placeholder content later:

1. Edit `/home/mike/project/rkl-consolidated/placeholder/index.html`
2. Commit and push changes:
   ```bash
   cd /home/mike/project/rkl-consolidated
   git add placeholder/index.html
   git commit -m "Update placeholder content"
   git push
   ```
3. Cloudflare Pages will auto-deploy the changes

## Squarespace

✅ **Nameservers changed** to Cloudflare
✅ **Can cancel Squarespace trial** - No longer needed for hosting
- Keep the domain registration in Squarespace (or transfer to another registrar later)
- Just cancel the hosting/website builder trial

## Current URLs

- **Old review site:** https://rkl-org.pages.dev/ (for board review)
- **New development site:** https://15298256.rkl-org.pages.dev/ (password protected)
- **Placeholder site:** https://rkl-placeholder.pages.dev/ (live, ready to connect to domain)
- **Live domain (pending):** https://resonantknowledgelab.org (will show placeholder once nameservers active)
