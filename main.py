from typing import final, Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final =  '7008238818:AAFLNTW4e0gIqHeU0QkxSthK9YF3GIJpoiA'
BOT_USERNAME : Final = '@CoffeeAks_bot'

async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, Thanks for chatting with me. I am a Coffee expert!")

async def help_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, please type something so that i can respond")

async def custom_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello,This is a custom command!")

def handle_response(text : str) -> str:
    processed:str = str.lower()
    if 'Hello' in processed:
        return("Hi There!")
    if 'How are you' in processed:
        return("I am good, How are you")
    if 'I love python' in processed:
        return("I love python too")
    return("I dont understand ..")

async def handle_message(update:Update, context : ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text:str = update.message.text

    print(f'User({update.message.chat.id})in {message_type}:{text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response : str = handle_response(new_text)
        else:
            return
    else:
        response:str=handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

async def error(update:Update, context : ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} aused error {context.error}')

if __name__ == '__main__':
    print("Starting bot ... ")
    app = Application.builder().token(TOKEN).build()
#command
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
#message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
#error
    app.add_error_handler(error)
#polling
    print("Polling...")
    app.run_polling(poll_interval=3)
