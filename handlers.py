from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keyboards
from create_bot import dp, bot
import requests
from bs4 import BeautifulSoup


async def set_start_command(bot: Bot, chat_id):
    return await bot.set_my_commands(
        commands=[
            types.BotCommand('start', 'restart bot'),
            types.BotCommand('help', 'info about bot'),
        ],
        scope=types.BotCommandScopeChat(chat_id),
        language_code='ru'
    )


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await set_start_command(bot, message.from_user.id)
    # Отправляем приветственное сообщение
    photo = types.InputFile('ювентус.jpg')
    await message.answer_photo(photo=photo,
                               caption="Добро пожаловать! В этом боте вы можете посмотреть реализацию игроков по"
                                       " системе XG и вместе с этим пройти обучающий курс по теории футбола.",
                               reply_markup=keyboards.get_choice())


# обработчик для кнопки статистики XG
@dp.callback_query_handler(text='statXG')
async def statXG(call: types.CallbackQuery):
    await call.answer()
    photo_XG = types.InputMediaPhoto(open('XG.png', 'rb'))# открываеи фото в двоичным виде
    await call.message.edit_media(media=photo_XG)# редактируем фотографию
    await call.message.edit_caption(caption='вы в разделе XG статистика XG - это соотношение ударов игроков и'
                                 ' их показателей по допустимых голах, например игрок пробил с метра к чужим воротам и'
                                 ' не забил и статистика XG показывает, что у него +1,0, то есть он не дозабил 1 гол',
                                    reply_markup= keyboards.get_stat()) # редактируем подпись и клавиатуру


# обработчик для кнопки Назад
@dp.callback_query_handler(text='back_stat')
async def back_stat(call: types.CallbackQuery):
    await call.answer()
    photo_XG = types.InputMediaPhoto(open('ювентус.jpg', 'rb'))# открываеи фото в двоичным виде
    await call.message.edit_media(media=photo_XG)# редактируем фотографию
    await call.message.edit_caption(caption="Добро пожаловать! В этом боте вы можете посмотреть реализацию игроков по"
                                       " системе XG и вместе с этим пройти обучающий курс по теории футбола.",
                                    reply_markup= keyboards.get_choice()) # редактируем подпись и клавиатуру


@dp.message_handler(commands=['get_data'])
async def get_data_handler(message: types.Message):
    # Получаем данные из таблицы на сайте
    url = 'https://understat.com/league/EPL/2023'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлекаем нужные данные из таблицы
    # Здесь вам нужно будет использовать методы BeautifulSoup для поиска и извлечения данных из таблицы

    # Отправляем данные в телеграм-бота
    await bot.send_message(message.chat.id, 'Ваши данные: {}'.format(data))


# регистрация обработчиков
def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
