import datetime

def run_bot():
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"RentMyBook Bot Running for {today}")
    print("Bot finished successfully")

if __name__ == "__main__":
    run_bot()
