import os
import telebot

# Environment Variable থেকে টোকেন নেওয়া হবে
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8773972316:AAFx2r4nmwHnNNi_qZsKJGpiukA_uKkuIsQ")
bot = telebot.TeleBot(BOT_TOKEN)

# 1. Referral Link Join Handler (/start ref_12345678)
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    args = message.text.split()
    if len(args) > 1 and args[1].startswith("ref_"):
        referrer_id = args[1].replace("ref_", "")
        
        # নিজের লিংকে নিজে ক্লিক করলে নোটিফিকেশন যাবে না
        if str(referrer_id) != str(user_id):
            try:
                ref_msg = (
                    f"🎉 *New Referral Joined!*\n\n"
                    f"User *{first_name}* joined using your link.\n"
                    f"You will earn *$0.20 USDT* after their first withdrawal!"
                )
                bot.send_message(referrer_id, ref_msg, parse_mode="Markdown")
            except Exception as e:
                print(f"Referrer notification error: {e}")

    welcome_msg = (
        f"💎 *Welcome to USDT POOL, {first_name}!*\n\n"
        f"Watch ads, invite friends, and earn USDT directly to your TRC20 wallet."
    )
    bot.reply_to(message, welcome_msg, parse_mode="Markdown")


# 2. Notification Functions for Withdrawals
def send_withdraw_pending(user_id, amount, wallet):
    try:
        msg = (
            f"⏳ *Withdrawal Request Submitted!*\n\n"
            f"💰 *Amount:* ${amount:.2f} USDT\n"
            f"🏦 *Wallet:* `{wallet}`\n"
            f"📌 *Status:* Pending Processing"
        )
        bot.send_message(user_id, msg, parse_mode="Markdown")
    except Exception as e:
        print(f"Error sending pending msg: {e}")

def send_withdraw_complete(user_id, amount, wallet):
    try:
        msg = (
            f"✅ *Withdrawal Completed!*\n\n"
            f"🎉 Your payment of *${amount:.2f} USDT* has been sent.\n"
            f"🏦 *Wallet:* `{wallet}`\n\n"
            f"Thank you for using *USDT POOL*!"
        )
        bot.send_message(user_id, msg, parse_mode="Markdown")
    except Exception as e:
        print(f"Error sending complete msg: {e}")


if __name__ == "__main__":
    print("USDT Pool Bot is running...")
    bot.infinity_polling()
