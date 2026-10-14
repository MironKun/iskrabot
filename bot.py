
import os
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Привет! Я Искра ⚡\n\n"
        "Я твой личный помощник.\n"
        "Сейчас мы запускаем мою первую версию.\n\n"
        "Напиши мне что-нибудь — я отвечу!"
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Я Искра ⚡\n\n"
        "Доступные команды:\n"
        "/start — запустить бота\n"
        "/help — помощь\n\n"
        "Пока я умею отвечать на сообщения."
    )


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    user_text = update.message.text

    await update.message.reply_text(
        f"Ты написал: {user_text}\n\n"
        "Искра на связи! ⚡"
    )


def main():
    if not TOKEN:
        raise RuntimeError(
            "Не задан токен. Добавь TELEGRAM_BOT_TOKEN "
            "в секреты сервиса, на котором запускается бот."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message,
        )
    )

    print("Искра запущена!")

    app.run_polling()


if __name__ == "__main__":
    main()
