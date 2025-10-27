# LinkedIn API Setup Guide

This guide will help you set up LinkedIn API integration to automatically post your climate data updates.

## 🔑 Step 1: Create a LinkedIn App

1. Go to [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
2. Click "Create App"
3. Fill in the required information:
   - **App name**: Climate IoT Bot (or your preferred name)
   - **LinkedIn Page**: Select your LinkedIn page
   - **Privacy Policy URL**: Add a privacy policy URL (can be a simple GitHub page)
   - **App logo**: Upload a logo for your app
4. Click "Create app"

## 🔐 Step 2: Configure App Permissions

1. In your app dashboard, go to the "Auth" tab
2. Add the following OAuth 2.0 scopes:
   - `r_liteprofile` - Read basic profile information
   - `w_member_social` - Write posts on behalf of the user
3. Add your redirect URL: `http://localhost:8000/auth/callback`

## 🎫 Step 3: Get Your Credentials

1. In the "Auth" tab, copy:
   - **Client ID**
   - **Client Secret**
2. You'll need these for the next step

## 🔑 Step 4: Generate Access Token

### Option A: Using LinkedIn's OAuth Playground (Recommended)

1. Go to [LinkedIn OAuth Playground](https://www.linkedin.com/developers/tools/oauth/playground)
2. Select your app
3. Add the scopes: `r_liteprofile w_member_social`
4. Click "Request token"
5. Authorize the app
6. Copy the **Access Token**

### Option B: Manual OAuth Flow

1. Create a simple OAuth flow script (see `scripts/linkedin_auth.py` below)

## ⚙️ Step 5: Configure Environment Variables

Create a `.env` file in your project root:

```env
# LinkedIn API Configuration
LINKEDIN_CLIENT_ID=your_client_id_here
LINKEDIN_CLIENT_SECRET=your_client_secret_here
LINKEDIN_ACCESS_TOKEN=your_access_token_here
LINKEDIN_REDIRECT_URI=http://localhost:8000/auth/callback

# Auto-posting configuration
AUTO_POST_LINKEDIN=true

# Other existing variables...
CAELI_API_KEY=your_caeli_api_key_here
REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO
```

## 🧪 Step 6: Test the Integration

Run the LinkedIn posting script:

```bash
python scripts/compose_linkedin_post.py
```

You should see:
- Generated post content
- Success message if posting works
- Error messages with helpful instructions if something is wrong

## 🔄 Step 7: Set Up Automated Posting

The script can be run automatically via:

1. **API Endpoint**: `POST /run-job/compose_linkedin_post`
2. **Cron Job**: Set up a cron job to run the script periodically
3. **APScheduler**: Use the built-in scheduler in `apscheduler_api/main.py`

## ⚠️ Important Notes

- **Access tokens expire**: LinkedIn access tokens typically expire after 60 days
- **Rate limits**: LinkedIn has rate limits for posting (typically 150 posts per day)
- **Content guidelines**: Ensure your posts comply with LinkedIn's content policies
- **Testing**: Always test with `AUTO_POST_LINKEDIN=false` first

## 🛠️ Troubleshooting

### Common Issues:

1. **"Invalid access token"**: Token may have expired, regenerate it
2. **"Insufficient permissions"**: Check that your app has the correct scopes
3. **"Rate limit exceeded"**: Wait before posting again
4. **"Profile not found"**: Ensure the access token is valid and has correct permissions

### Debug Mode:

Set `LOG_LEVEL=DEBUG` in your `.env` file for more detailed error messages.

## 📚 Additional Resources

- [LinkedIn API Documentation](https://docs.microsoft.com/en-us/linkedin/)
- [LinkedIn UGC Posts API](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/ugc-post-api)
- [LinkedIn OAuth 2.0 Guide](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow)
