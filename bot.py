
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
# from telegram.ext import *
import datetime
import time

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


subxi = "04:10:00"
bomdod = "05:00:00"
quyosh = "05:35:00"
qiyom = "12:20:00"
peshin = "13:00:00"
asr = "17:05:00"
shom = "19:00:00"
xufton = "21:40:00"

async def obuna(update, context):
    sor = True
   
    while sor == True:
        x = datetime.datetime.now()
        hozir = x.strftime("%H:%M:%S")
        if hozir == subxi:
            await update.message.reply_text(
                f'Subxi boldi {hozir} \n Subxi {subxi}da!'
            )
        elif hozir == bomdod:
            await update.message.reply_text(
                f'Bomdod bo`ldi {hozir} \n Bomdod {bomdod}da!'
            )
        elif hozir == quyosh:
            await update.message.reply_text(
                f'Quyosh chiqmoqda ! {hozir} \n Quyosh Chqishi {quyosh}da!'
            )
        elif hozir == qiyom:
            await update.message.reply_text(
                f'Qiyom bo`ldi {hozir} \n Qiyom vaqti {qiyom}da!'
            )
        elif hozir == peshin:
            await update.message.reply_text(
                f'Peshin bo`ldi {hozir} \n Peshin {peshin}da!'
            )
        elif hozir == asr:
            await update.message.reply_text(
                f'Asr bo`ldi {hozir} \n Asr {asr}da!'
            )
        elif hozir == shom:
            await update.message.reply_text(
                f'Shom bo`ldi {hozir} \n Shom {shom}da!'
            )
        elif hozir == xufton:
            await update.message.reply_text(
                f'Xufton bo`ldi {hozir} \n Xufton {xufton}da!'
            )
        # else:
        #     await update.message.reply_text(
        #         f' {hozir} '
        #     )
        time.sleep(1)
        
async def myfun(update, context):
    await update.message.reply_text(
        f' Sizning nick namegiz{update.effective_user.first_name} \nSizning foydalanuvchi nomigiz @{update.effective_user.username} \nSizning id raqamingizni {update.effective_user.id}'
    )

async def secret2328(update, context):
        await update.message.reply_text(
            'Siz adminmisiz? .... 😊'
        )
async def unknown(update, context):
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


app = ApplicationBuilder().token("5610525171:AAEPVr1e7n-0AVk0yXPyvUC0_AjkxL7Ew0g").build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("obuna", obuna))
app.add_handler(conv_handler)

app.run_polling()

app.idle()
