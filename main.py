import os
import telebot


bot = telebot.TeleBot("1976855314:AAFFfIQ6WJsSnx3b9SkBrZKrOkahyzZal1U")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "👋 හායි, මම තමයි නවතම තාක්ශනයට අනූව හැඩ ගැසී සෑදුනු විශාලතම PDF පුස්තකාලය බොට්.. මට පුලුවන් බටන් ක්‍රමයට සහ inline ක්‍රමයට PDF සහ වීඩියෝ ගැනීමට.. වෙනත් උදව් සඳහා /help කමාන්ඩ් එක එවන්න..🇱🇰")


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "උදව් ඉල්ලුවට උදව් නෑ😂.")



bot.polling()
