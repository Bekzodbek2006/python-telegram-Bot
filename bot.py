from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters


my = ReplyKeyboardMarkup([['My']], resize_keyboard=True)
secret_btns = ReplyKeyboardMarkup([['2328'], ['1225']])

async def login(update, context):
    await update.message.reply_text(
        f'Siz {update.effective_user.first_name} shu nom bilan kirdingiz'
    )
    return 1

async def start(update, context):
    await update.message.reply_text(
        f'Salom {update.effective_user.first_name}'
    )
async def help(update, context):
    await update.message.reply_text(
        't.me/webdev06'
    )


async def myfun(update, context):
    await update.message.reply_text(
        f' Sizning nick namegiz{update.effective_user.first_name} \nSizning foydalanuvchi nomigiz @{update.effective_user.username} \nSizning id raqamingizni {update.effective_user.id}'
    )

async def secret2328(update, context):
        await update.message.reply_text(
            'Siz adminmisiz? .... 😊'
        )

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("login", login)],
    states={
        1:{
            MessageHandler(filters.Regex('^(My)$'),myfun),
            MessageHandler(filters.Regex('^(2328)$'),secret2328)
        }
       
    },
    fallbacks=[MessageHandler(filters.Text, login)]
)



app = ApplicationBuilder().token("5401595436:AAHp9TQu5PjBXSea-9y6_j1t29O24zFON3s").build()


app.add_handler(CommandHandler("start", start))
app.add_handler(conv_handler)

app.run_polling()

app.idle()
