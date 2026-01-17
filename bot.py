import datetime
import os
import requests

def post_to_linkedin(message: str):
    access_token = os.getenv("LINKEDIN_TOKEN")

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    # 🔹 Add your company ID here
    company_id = "111488296"  # replace with your actual LinkedIn company page ID

    payload = {
        "author = "urn:li:person:me",
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

    if response.status_code == 201:
        print("✅ LinkedIn post successful!")
    else:
        print("❌ LinkedIn post failed:", response.status_code, response.text)

def run_bot():
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"RentMyBook Bot Running for {today}")

    # 🔹 Call LinkedIn posting here
    post_to_linkedin(f"RentMyBook Bot update for {today}")

    print("Bot finished successfully")

if __name__ == "__main__":
    run_bot()
