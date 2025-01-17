from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def clear_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    current_message_id = update.message.message_id

    # Loop untuk menghapus 100 pesan terakhir
    for message_id in range(current_message_id - 100, current_message_id):
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            print(f"Deleted message with ID: {message_id}")
        except Exception as e:
            print(f"Error deleting message {message_id}: {e}")

if __name__ == "__main__":
    TOKEN = "7869705949:AAEaM7AjFhCOuJiQ3GKo_ICjvKnSey6L6QQ"
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah "/clear"
    application.add_handler(CommandHandler("clear", clear_chat))

    application.run_polling()
