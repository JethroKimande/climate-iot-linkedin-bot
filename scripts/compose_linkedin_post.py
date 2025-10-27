import os
import pandas as pd
import requests
import json
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

data_file = os.path.join('data', 'no2_comparison_data.csv')

# LinkedIn API Configuration
LINKEDIN_API_BASE = "https://api.linkedin.com/v2"
LINKEDIN_ACCESS_TOKEN = os.getenv('LINKEDIN_ACCESS_TOKEN')


def load_data() -> pd.DataFrame:
    if not os.path.exists(data_file):
        return pd.DataFrame()
    return pd.read_csv(data_file)


def compose_caption(df: pd.DataFrame) -> str:
    if df.empty:
        return "No data available to compose a LinkedIn post."
    df = df.dropna(subset=['date'])
    if df.empty:
        return "No valid data found."
    latest = df.iloc[-1]
    date_str = latest['date']
    img_val = latest.get('image_no2', '')
    api_val = latest.get('api_no2', '')
    caption_lines = [
        "🛰️ Weekly NO₂ update over Nairobi",
        f"Date: {date_str}",
        f"Satellite estimate: {img_val} ppb",
    ]
    if pd.notna(api_val) and str(api_val) != "":
        caption_lines.append(f"Caeli API: {api_val} ppb")
    caption_lines.append("#ClimateTech #DataForGood #IoTAfrica")
    return "\n".join(caption_lines)


def get_linkedin_profile_id() -> Optional[str]:
    """Get the LinkedIn profile ID for the authenticated user."""
    if not LINKEDIN_ACCESS_TOKEN:
        print("❌ LinkedIn access token not found. Please set LINKEDIN_ACCESS_TOKEN in your .env file.")
        return None
    
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(f"{LINKEDIN_API_BASE}/me", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('id')
        else:
            print(f"❌ Failed to get LinkedIn profile: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error getting LinkedIn profile: {e}")
        return None


def post_to_linkedin(text: str) -> bool:
    """Post content to LinkedIn."""
    if not LINKEDIN_ACCESS_TOKEN:
        print("❌ LinkedIn access token not found. Please set LINKEDIN_ACCESS_TOKEN in your .env file.")
        return False
    
    profile_id = get_linkedin_profile_id()
    if not profile_id:
        return False
    
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    
    # LinkedIn API payload for text posts
    payload = {
        "author": f"urn:li:person:{profile_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    try:
        response = requests.post(
            f"{LINKEDIN_API_BASE}/ugcPosts",
            headers=headers,
            data=json.dumps(payload)
        )
        
        if response.status_code == 201:
            print("✅ Successfully posted to LinkedIn!")
            return True
        else:
            print(f"❌ Failed to post to LinkedIn: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error posting to LinkedIn: {e}")
        return False


def main() -> None:
    df = load_data()
    caption = compose_caption(df)
    
    print("📝 Generated LinkedIn post content:")
    print("-" * 50)
    print(caption)
    print("-" * 50)
    
    # Ask user if they want to post
    post_to_linkedin_flag = os.getenv('AUTO_POST_LINKEDIN', 'false').lower() == 'true'
    
    if post_to_linkedin_flag:
        print("🚀 Auto-posting to LinkedIn...")
        success = post_to_linkedin(caption)
        if not success:
            print("💡 To enable LinkedIn posting:")
            print("1. Set up LinkedIn API credentials in your .env file")
            print("2. Set AUTO_POST_LINKEDIN=true to enable auto-posting")
    else:
        print("💡 To post this content to LinkedIn:")
        print("1. Set up LinkedIn API credentials in your .env file")
        print("2. Set AUTO_POST_LINKEDIN=true to enable auto-posting")
        print("3. Or manually copy the content above to LinkedIn")


if __name__ == "__main__":
    main()
