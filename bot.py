import datetime
import os
import requests
import sys

def post_to_linkedin(message: str):
    access_token = os.getenv("LINKEDIN_TOKEN")

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    author = "urn:li:person:me"  # posting as yourself

    payload = {
        "author": author,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": message},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    # 🔍 Debug logging with flush
    print("🔍 Status Code:", response.status_code, flush=True)
    print("🔍 Response Text:", response.text, flush=True)

    if response.status_code == 201:
        print("✅ LinkedIn post successful!", flush=True)
    else:
        print("❌ LinkedIn post failed", flush=True)

def run_bot():
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"RentMyBook Bot Running for {today}", flush=True)

    # 🔹 Call LinkedIn posting here
    post_to_linkedin(f"RentMyBook Bot update for {today}")

    print("Bot finished successfully", flush=True)

if __name__ == "__main__":
    run_bot()
