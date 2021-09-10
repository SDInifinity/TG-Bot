import os
import telebot


bot = telebot.TeleBot("1986932872:AAGgsXeeiLmP4hVeUJzuOe854591B542wBk")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "👋Hello There Welcome To SZ Bots Info Bot You Can See SZ All Info And More.. See A My Commands Send /help command...☠️")


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "☠️ Welcome To Help Room ☠️   My Commands = /info /chat /bots /myinfo /support ©️")
  
  
@bot.massage_handler(commands=["info"])
def.send_massage(massage):
  bot.send_massage(massage.chat.id, "💝 SZ Info Privetly💝")



bot.polling()
