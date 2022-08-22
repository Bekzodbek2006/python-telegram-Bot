from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import os
PORT = int(os.environ.get('PORT', 5000))


buttons = ReplyKeyboardMarkup([['help'],['admin']], resize_keyboard=True)
my = ReplyKeyboardMarkup([['My nick name'],['My Username'],['My Id']], resize_keyboard=True)

async def login(update, context):
    await update.message.reply_text(
        f'Siz {update.effective_user.first_name} shu nom bilan kirdingiz ',reply_markup=buttons
    )
    return 1

async def start(update, context):
    await update.message.reply_text(
        f'Salom {update.effective_user.first_name}'
    )
async def help(update, context):
    await update.message.reply_text(
        f't.me/webdev06',reply_markup=buttons
    )

async def admin(update, context):
    await update.message.reply_text(
        f'Adminlar @shoh_ake006 \n yana bittasi @webdev06',reply_markup=my
    )

async def usernick(update, context):
    await update.message.reply_text(
        f' Sizning nick namegiz{update.effective_user.first_name}',reply_markup=buttons
    )

async def username(update, context):
    await update.message.reply_text(
        f' Sizning foydalanuvchi nomigiz @{update.effective_user.username}',reply_markup=buttons
    )

async def id(update, context):
    await update.message.reply_text(
        f' Sizning id raqamingizni #{update.effective_user.id}',reply_markup=buttons
    )
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("login", login)],
    states={
        1:{
            MessageHandler(filters.Regex('^(help)$'),help),
            MessageHandler(filters.Regex('^(admin)$'),admin),
            MessageHandler(filters.Regex('^(My nick name)$'),usernick),
            MessageHandler(filters.Regex('^(My Username)$'),username),
            MessageHandler(filters.Regex('^(My Id)$'),id)
        }
       
    },
    fallbacks=[MessageHandler(filters.Text, login)]
)



app = ApplicationBuilder().token("5401595436:AAHF4QmYrrtJORYxg3kd3QSqcQt-renOngY").build()
app.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path='5401595436:AAHF4QmYrrtJORYxg3kd3QSqcQt-renOngY')
app.bot.setWebhook('https://bekzodbeksbot.herokuapp.com/' + '5401595436:AAHF4QmYrrtJORYxg3kd3QSqcQt-renOngY')

app.add_handler(CommandHandler("start", start))
app.add_handler(conv_handler)

app.run_polling()

app.idle()