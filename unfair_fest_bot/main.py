import time
from config.config_loader import config
from fest.fest_player import FestPlayer
from fest.fest_bot import FestBot

def main():
    print("=" * 30)
    print("🚀 Starting Fest Bot...")
    print("=" * 30)

    # Load credentials from config.json
    fest_id = config.get("player", "fest_id")
    token = config.get("player", "token")

    if not fest_id or not token:
        print("❌ Missing Fest ID or Token in config.json.")
        return

    # Create player and bot instances
    fest_player = FestPlayer(fest_id, token)
    bot = FestBot(fest_player)

    # Main bot loop
    while True:
        try:
            print("\n🔄 Running bot cycle...")
            bot.play_all_tourneys()
            print("✅ Cycle complete. Sleeping for 60 seconds...")
            time.sleep(60)
        except Exception as e:
            print(f"⚠️ Error in bot loop: {e}")
            print("⏳ Retrying in 30 seconds...")
            time.sleep(30)

if __name__ == "__main__":
    main()
