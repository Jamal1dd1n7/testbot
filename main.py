import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
TOKEN = '9252141437:AAEEbW559EST4_9CsRhgbb4-h5tsfSWuORw'

bot = telebot.TeleBot(TOKEN)


# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
  # Get the user's first name from the message object
  first_name = message.chat.first_name

  # Fallback just in case the first name is not available
  if not first_name:
    first_name = 'there'

  # Send the greeting message
  bot.reply_to(message, f'Hello {first_name}!')

@bot.message_handler(messages=['text'])
def echo_message(message):
  # Echo the received message back to the user
  bot.reply_to(message, message.text)


# Start the bot
print('Bot is running...')
bot.infinity_polling()