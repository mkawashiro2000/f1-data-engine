import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. Cargar el token desde el archivo secreto .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configuración de logs para ver errores en la terminal de la Pi
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 2. Función que se ejecuta cuando escribes /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Creamos botones físicos en el chat (Sección 4 de tu doc)
    teclado = [['/status', '/strategy'], ['/weather', '/ers_2026']]
    botones = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
    
    await update.message.reply_text(
        "🏎️ **F1 Data Engine: The Strategist**\n\n"
        "Hola Mitsunori, el sistema está activo en la Raspberry Pi.\n"
        "¿Qué reporte necesitas hoy?",
        reply_markup=botones,
        parse_mode='Markdown'
    )

# 3. Función para simular el estado del ERS 2026
async def check_ers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚡ **Reglamento 2026:** Balance 50/50 detectado.\nICE: 350kW | MGU-K: 350kW (Activo)")

if __name__ == '__main__':
    # Lanzar el bot
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Comandos que el bot entiende
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ers_2026", check_ers))
    
    print("🚀 Bot iniciado. Presiona Ctrl+C para detenerlo.")
    app.run_polling()
