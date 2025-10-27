#!/usr/bin/env python3
"""
LinkedIn OAuth Authentication Helper

This script helps you get a LinkedIn access token for the Climate IoT Bot.
Run this script to authenticate with LinkedIn and get your access token.
"""

import os
import webbrowser
import urllib.parse
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LinkedIn OAuth configuration
LINKEDIN_CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID')
LINKEDIN_CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET')
LINKEDIN_REDIRECT_URI = os.getenv('LINKEDIN_REDIRECT_URI', 'http://localhost:8000/auth/callback')

# Required scopes for posting
SCOPES = ['r_liteprofile', 'w_member_social']


def generate_auth_url():
    """Generate LinkedIn OAuth authorization URL."""
    if not LINKEDIN_CLIENT_ID:
        print("❌ LINKEDIN_CLIENT_ID not found in .env file")
        return None
    
    params = {
        'response_type': 'code',
        'client_id': LINKEDIN_CLIENT_ID,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'state': 'climate_iot_bot',
        'scope': ' '.join(SCOPES)
    }
    
    auth_url = f"https://www.linkedin.com/oauth/v2/authorization?{urllib.parse.urlencode(params)}"
    return auth_url


def exchange_code_for_token(authorization_code):
    """Exchange authorization code for access token."""
    if not LINKEDIN_CLIENT_SECRET:
        print("❌ LINKEDIN_CLIENT_SECRET not found in .env file")
        return None
    
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET
    }
    
    try:
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            token_data = response.json()
            return token_data.get('access_token')
        else:
            print(f"❌ Failed to exchange code for token: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error exchanging code for token: {e}")
        return None


def main():
    """Main authentication flow."""
    print("🔐 LinkedIn OAuth Authentication Helper")
    print("=" * 50)
    
    # Check if credentials are configured
    if not LINKEDIN_CLIENT_ID or not LINKEDIN_CLIENT_SECRET:
        print("❌ LinkedIn credentials not configured!")
        print("Please add the following to your .env file:")
        print("LINKEDIN_CLIENT_ID=your_client_id_here")
        print("LINKEDIN_CLIENT_SECRET=your_client_secret_here")
        return
    
    # Generate authorization URL
    auth_url = generate_auth_url()
    if not auth_url:
        return
    
    print("🌐 Opening LinkedIn authorization page...")
    print("If the browser doesn't open automatically, copy this URL:")
    print(auth_url)
    print()
    
    # Open browser
    try:
        webbrowser.open(auth_url)
    except Exception as e:
        print(f"⚠️ Could not open browser automatically: {e}")
        print("Please manually open the URL above in your browser")
    
    print("📋 After authorizing the app, LinkedIn will redirect you to a URL like:")
    print(f"{LINKEDIN_REDIRECT_URI}?code=AUTHORIZATION_CODE&state=climate_iot_bot")
    print()
    
    # Get authorization code from user
    authorization_code = input("🔑 Please paste the authorization code from the URL: ").strip()
    
    if not authorization_code:
        print("❌ No authorization code provided")
        return
    
    # Exchange code for token
    print("🔄 Exchanging authorization code for access token...")
    access_token = exchange_code_for_token(authorization_code)
    
    if access_token:
        print("✅ Successfully obtained access token!")
        print()
        print("📝 Add this to your .env file:")
        print(f"LINKEDIN_ACCESS_TOKEN={access_token}")
        print()
        print("🚀 You can now use the LinkedIn posting functionality!")
    else:
        print("❌ Failed to obtain access token")
        print("Please check your credentials and try again")


if __name__ == "__main__":
    main()
