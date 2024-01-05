import telebot, requests
from telebot import types
from bs4 import BeautifulSoup as br
import time
time = time.asctime()
#BoxPrey
token = input("Pon El Token: ")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    channel = types.InlineKeyboardButton(text='🚀Tᵉˡᵉᵍʳᵃᵐ🚀', url = "t.me/addlist/iZfJw-LVfYthNzYx")
    xx = types.InlineKeyboardMarkup()
    xx.add(channel)
    bot.reply_to(message, f'''🧑🏻‍💻 ʙᴏᴛ ᴇӼᴛʀᴀᴇ ᴇʟ ᴄᴏ́ᴅɪɢᴏ ғᴜᴇɴᴛᴇ ᴅᴇ ʟᴏՏ ՏɪᴛɪᴏՏ ᴡᴇʙ (ʜᴛᴍʟ)

🧑🏻‍💻 ᴇɴᴠɪ́ᴀ ᴇʟ ᴇɴʟᴀᴄᴇ ʏ ʟᴜᴇɢᴏ ᴇՏᴘᴇʀᴀ.

🧑🏻‍💻 ᴇᴊᴇᴍᴘʟᴏ ᴅᴇ ᴇɴʟᴀᴄᴇ : https://www.wikipedia.org''',reply_markup=xx)
#BoxPrey
@bot.message_handler(func=lambda message: True)
def send_html(message):
    chat_id = message.chat.id
    try:
    	source_code = requests.get(message.text).text
    	soup = br(source_code, 'html.parser')
    	with open("AnonNews_irc.html", "w+", encoding='utf-8') as file:
    		file.writelines(str(soup))
    		with open("AnonNews_irc.html", "r", encoding='utf-8') as file:
    		  bot.send_chat_action(chat_id,action="upload_document");bot.send_document(chat_id, file, caption=f'ʜᴇᴄʜᴏ 👍🏻\nʜᴏʀᴀ : {time}\n- {message.text}')
    except:
        bot.reply_to(message,'ᴇʀʀᴏʀ')
  #BoxPrey      
print('Activado')
bot.infinity_polling()
