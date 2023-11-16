
pip install  telebot
pip install openai

import telebot
from telebot import types
from openai import OpenAI

client = OpenAI(api_key="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")

token='6532340031:AAHy8J_tPbmfLQXukmqx-n5tss9uCVAdxCc'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['reply'])
def startMessage(message):
  answer = message.text.split(' ')[1]
  answer2 = message.text.split(' ')[2:]
  text = ' '.join(answer2)
  bot.send_message(f"{answer}",text=f"{text}")



@bot.message_handler(commands=['start'])
def startMessage(message):
  chat_id = message.chat.id
  bot.send_message(chat_id,"Твои сообщения будут обрабатываться от 2сек. до 1мин. в зависимости от вопрса и размера сообщения ответа на него:)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Обрабатываем все входящие сообщения
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.username
    text = message.text
    message = bot.reply_to(message, '⏳ Секунду...')
   #  bot.send_message("1062337361", text=f"**{message.chat.username}**\n{message.chat.id}\n{text}", parse_mode="MARKDOWN" )

    try:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-16k-0613",
          # response_format={ "type": "json_object" },
          messages=[
            {"role": "system", "content": "My name - Quemalls GPT designed to output text."},
            {"role": "user", "content": f"{text}\n"}
          ],
          max_tokens=500,
        )

        bot.delete_message(chat_id, message_id=message.message_id)


        bot.send_message(chat_id, f"{response.choices[0].message.content}", parse_mode="MARKDOWN")
    except:
        bot.reply_to(message, f"К ", parse_mode="MARKDOWN")

    # Отправляем ответное сообщение


if __name__ == "__main__":
    bot.infinity_polling()

