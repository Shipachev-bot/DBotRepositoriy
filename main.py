import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from states import StateSelection
import time

import keybords
from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="8158336790:AAFk4Mo-_zMut4Wx08aLc97i2n-OfmFpt4s")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Здравствуйте, я бот Деляна!🌲\n\nМоя задача постараться помочь вам разобраться в функционале нашего сервиса, надеюсь, что вместе у нас все получится!\n\nВ каком модуле затруднения?\nПожалуйста выберите модуль из представленных ниже.\n\nЕсли вы не являетесь нашим пользователем или вам необходима консультация специалиста напишите в чат слово Справка ",
        reply_markup=keybords.main_keybord())
    await state.set_state(StateSelection.moduleSelection)
    counter.clear()


@dp.message(F.text.lower() == "мобильное приложения📱")
async def answer_no(message: Message):
    # await message.answer('Выберите интересующий раздел', reply_markup=keybords.mobile_app_first_keybord())
    await message.answer('Этот блок в процесе разработки, поторопите Илью и тут появятся подсказки')


@dp.message(F.text.lower() == "модуль 1c")
async def answer_no(message: Message):
    # await message.answer('Ой, тут давай сам')
    await message.answer('Этот блок в процеcсе разработки, поторопите Илью и тут появятся подсказки')


@dp.message(F.text.lower() == "назад 🔙")
async def answer_no(message: Message, state: FSMContext):
    data = await state.get_state()
    if data == StateSelection.sectionSelection:
        await message.answer('Окей, промахнулись с модулем, хе-хе!', reply_markup=keybords.main_keybord())
        await state.set_state(StateSelection.moduleSelection)
    elif data == StateSelection.create_infro or data == StateSelection.ls_state:
        await message.answer('Выберите интересующий раздел', reply_markup=keybords.web_first_keybord())
        await state.set_state(StateSelection.sectionSelection)
    elif data == StateSelection.DA_state or data == StateSelection.ls_state or data == StateSelection.employes or data == StateSelection.count or data == StateSelection.maps or data == StateSelection.calcSelection:
        await message.answer('Окей, промахнулись с модулем, хе-хе!', reply_markup=keybords.main_keybord())
        await state.set_state(StateSelection.moduleSelection)
    else:
        await message.answer("Что-то пошло не так")


@dp.message(F.text.lower() == "личный кабинет")
async def LS(message: Message, state: FSMContext):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIJoWcsXO_BYkDNbVuAHoseY00m6LegAAJL5DEbRXhgSUxTi-lS5v8LAQADAgADeQADNgQ',
        caption="<b>Личный кабинет</b>\n\nЛичный кабинет — это рабочее место пользователя в Системе.Личный кабинет позволяет: \n\nВидеть основную информацию об аккаунте и подключённому тарифу; \n\nПроизводить установку и смену пароля; \n\nОтображать созданные рабочие области с возможностью их редактирования и удаления; \n\nОтображать список сотрудников с возможностью редактирования и добавления; \n\nПроизводить смену и оплату тарифа; \n\nВключать и отключать доступ к спутнику Sentinel \n\nОтправлять заявку на модули расширения функционала.\n\n<b>Пожалуйста выберите раздел на клавиатуре</b>",
        parse_mode="html",
        reply_markup=keybords.LS_keybord())
    await state.set_state(StateSelection.ls_state)


@dp.message(F.text.lower() == "карты/спутники")
async def answer_no(message: Message):
    await message.answer('Тест пройден', reply_markup=keybords.main_keybord())


@dp.message(F.text.lower() == "запись трека")
async def answer_no(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAOTZxm5zlbv2DjbsimKj_HCxAOUTvIAAs7oMRsDGchIFHfbqZ2pqKsBAAMCAAN4AAM2BA',
        caption="Записать трек очень просто!\nНажмите «Начать запись», чтобы запустить сохранение точек передвижения.\nВо время движения будет отображаться линия перемещений\nЧтобы завершить маршрут нажмите «Завершить».",
        reply_markup=keybords.treckRecording_keybord())


@dp.message(F.text.lower() == "спасибо! проблема решена!")
async def trouble_Complete(message: Message):
    await message.answer('Отлично! Приятного пользования!', reply_markup=keybords.main_keybord())


@dp.message(F.text.lower() == "ничего не понятно!")
async def dont_anderstand(message: Message):
    await message.answer(
        'Для более широкой справки вы можете связаться с нами по телефону:\n+7913-039-55-90\nТакже рекомендую посетить наш сайт  https://www.delyana.ru/',
        reply_markup=keybords.main_keybord())


@dp.message(F.text.lower() == "справка")
async def dont_anderstand(message: Message, state: FSMContext):
    await message.answer(
        'Для более широкой справки вы можете связаться с нами по телефону:\n+7913-039-55-90\nТакже рекомендую посетить наш сайт  https://www.delyana.ru/',
        reply_markup=keybords.main_keybord())
    await state.set_state(StateSelection.moduleSelection)


@dp.message(F.text.lower() == "web-приложение 🖥")
async def dont_anderstand(message: Message, state: FSMContext):
    await message.answer('Выберите интересующий раздел', reply_markup=keybords.web_first_keybord())
    await state.set_state(StateSelection.sectionSelection)


@dp.message(F.text.lower() == "загрузка xml деклараций")
async def create_delyana_gpx(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMOZx-OX9-9SvJ6yVYhGtYreKFvr8kAAmDhMRvAvthIBILBmLvIUzUBAAMCAAN5AAM2BA',
        caption='<b>Шаг №1</b>\n\nЧтобы загрузить деляны из декларации XML необходимо перейти в раздел «Деляны» в левой части интерфейса\nДалее необходимо нажать на кнопку «Загрузить декларацию (XML)»',
        parse_mode="html")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMyZx-PqKGgEv8q0Ix6kUDMqd3fc0sAAl_hMRvAvthIruTsaCW44iYBAAMCAAN4AAM2BA',
        caption='<b>Шаг №2</b>\n\nПосле нужно выбрать рабочую область из списка, дать наименование декларации, выбрать XML из файловой системы компьютера и нажать на кнопку «Загрузить»\nЛесосеки из декларации «встанут на свои места», и отобразятся в списке делян.',
        parse_mode="html")


@dp.message(F.text.lower() == "создать деляну по gpx")
async def create_delyana_gpx(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMrZx-Pb0g88Epkqwln8tby3VzmtssAAo3jMRuxo-lIRQiLAlT597YBAAMCAAN5AAM2BA',
        caption='<b>Шаг №1</b>\n\nЧтобы загрузить координаты деляны необходимо перейти в раздел «Проекты», и выбрать договор аренды, к которому будет привязан данный объект, далее необходимо нажать на значок загрузки.',
        parse_mode="html")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMaZx-O9A0mvclytWuGZB1KSc3plDYAAo7jMRuxo-lI5T2puPvS6XYBAAMCAAN4AAM2BA',
        caption='<b>Шаг №2</b>\n\nВ появившемся окне необходимо нажать на «Загрузить GPX», и выбрать тип объекта «Полигон» после нажать на кнопку «Отправить»',
        parse_mode="html")


@dp.message(Command('new'))
async def send_album(message: Message):
    file_ids = [
        'AgACAgIAAxkBAAIB02cbEzsHEvEX71fkEe3TMlxvFc6PAAJg4TEbwL7YSNccVJ7WDR9uAQADAgADeQADNgQ',
        'AgACAgIAAxkBAAIB0mcbEzvVFMKvx1qs-ZPtvXGwPoZqAAJf4TEbwL7YSB7l3TpvSZLbAQADAgADeAADNgQ']
    media = [types.InputMediaPhoto(media=file_id) for file_id in file_ids]
    await message.answer_media_group(media=media)


@dp.message(F.text.lower() == "cоздание инфраструктуры", StateSelection.sectionSelection)
async def cmd_random(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMRZx-OnS_uBxFsH0gdGfxwZxaOEg0AAnjmMRuxo-FIn71JGxWvdKgBAAMCAAN5AAM2BA',
        caption='<b>Справочник про делянам</b>', reply_markup=keybords.inline_infro_delyana(), parse_mode="html")
    # await message.answer_photo(
    #  photo='AgACAgIAAxkBAAMTZx-OwCBgr3mzVKylo3_X_3gOTMYAAoHmMRuxo-FIDZdMbTMwJ78BAAMCAAN5AAM2BA',
    #   caption='<b>Справочник по дорогам и складам</b>', reply_markup=keybords.inline_infro_roads_and_sklads(),
    # parse_mode='html')


@dp.message(F.text.lower() == "оцифровка планшетов")
async def planshet(message: Message):
    await message.answer(
        'В web-приложении Delyana существует возможность оцифровывать планшеты для их отображения на карте. Для данного функционала существует раздел “Редактор планшетов”.\nДля того, чтобы перейти в данный раздел существует 2 способа.')
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAANWZx-QJmcdnsBVMfp9n79Rkp5AHd4AAiDhMRughvhIXm1xWIXFThUBAAMCAAN4AAM2BA',
        caption='<b>Способ №1</b>\n\nИз раздела слои, путем нажатия на иконку карандаша напротив слоя “Планшеты”',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAANYZx-QRkiaqq8hToPIMPtFJ0YbP2AAAjnhMRughvhIU_W7c80pMGMBAAMCAAN5AAM2BA',
        caption='<b>Способ №2</b>\n\nНажатием на иконку человека в правом верхнем углу и выбора строки “Редактор планшетов” ',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAANaZx-QTJE_RDSGpXop5jdoIEe9qXwAAkrhMRughvhILwrEpaAfoiUBAAMCAAN5AAM2BA',
        caption='<b>Загрузка планшетов</b>\n\n<b>Шаг №1</b>\nВ разделе “Редактор планшетов” для загрузки планшета необходимо кликнуть по кнопке “Загрузить планшет”',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAANaZx-QTJE_RDSGpXop5jdoIEe9qXwAAkrhMRughvhILwrEpaAfoiUBAAMCAAN5AAM2BA',
        caption='<b>Шаг №2</b>\n\nВ открывшемся окне заполнить поля и нажать на кнопку “Загрузить планшет” для выбора файла',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAANeZx-QXCyindCNFjEXEhv-HBjqg7gAAovhMRughvhIkndalx18KtEBAAMCAAN4AAM2BA',
        caption='<b>Шаг №3</b>\n\nПосле заполнения данных и загрузки файла, планшет появится в левой части страницы в рабочей области к которой он был привязан при создании. После этого, следует нажать на него левой кнопкой мыши и кликнуть по кнопке “Загрузить кварталы”',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAANgZx-QbMflzg1patKAsXLHvOmXGwgAAqzhMRughvhICi0rIPYIguQBAAMCAAN4AAM2BA',
        caption='<b>Шаг №4</b>\n\nВ открывшемся окне, необходимо указать кварталы планшета, которые нужно оцифровать ',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAAN8Zx-Snoi03HtVAUwbIzZBFfNmirgAAuzmMRtJ1wFJDYGaxOgneuoBAAMCAAN5AAM2BA',
        caption='<b>Шаг №5</b>\n\nПосле того, как кварталы нанеслись на копию планшета следует их немного подредактировать для визуального отображения и нажать на значок дискеты для сохранения ',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAAOHZx-UK4YvFwjvotIVY3VTPmcPmGsAAvjmMRtJ1wFJ9Vsc__-t8CYBAAMCAAN5AAM2BA',
        caption='<b>Шаг №6</b>\n\nПосле всех действий оцифрованный планшет появится на карте. Для этого следует вернуться на страницу с картой и включить слой “Планшеты” ',
        parse_mode="html")


@dp.message(F.text.lower() == "фотозамер штабеля")
async def planshet(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAO7Zx-WzU6D5zJ4Rq8Cz366ShruWTwAAhPnMRtJ1wFJJLLUNqyhZQcBAAMCAAN5AAM2BA',
        caption='<b>Фотозамер штабеля</b>\n\nФункционал фотозамера штабелей в web-приложении деляна, предназначен для автоматического подсчёта объема заготовленной древесины, хранения всех фото штабелей в одном месте и привязка их к конкретной деляне.Для того, чтобы зайти в данный раздел, необходимо кликнуть по иконке человека в правом верхнем углу и нажать на строчку “Замер штабелей”',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIHG2cqCz6axJQBR3yXlPFPwfG1BWQzAAKB5DEba_RQSX7TFXlLCftZAQADAgADeQADNgQ',
        caption='<b>Привяжите штабель к лесосеке</b>\n\nДля этого в левой части страницы в списке делян, следует выбрать нужную нам и нажать на значок плюса справа от неё, после чего дать название и сохранить',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIHGWcqCztMBPHGqdUtfxne7KVGM8HUAAKA5DEba_RQSciVcVKBr_SHAQADAgADeQADNgQ',
        caption='<b>Добавление фотографий в штабель</b>\n\nПосле того как объект штабель создан, нужно по нему кликнуть и внизу страницы нажать на окно “Загрузить фото” и выбрать нужные фотоснимки (от 1 до 15 одновременно)',
        parse_mode="html")
    time.sleep(0.5)
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIHF2cqCzj9gCUoMUmT7We3ODkg8JMQAAJ_5DEba_RQSTiLcy4aKIuRAQADAgADeQADNgQ',
        caption='<b></b>\n\nПосле успешной загрузки, фотографии автоматически будут обработаны нашим нейросетевым алгоритмом. После загрузки, на каждой фотографии необходимо добавить ширину замера и данные древесины.Чтобы добавить или скорректировать ширину замера, следует кликнуть по кнопке “Ширина замера” находящейся сверху, поставить две точки на фотоснимке и указать длину',
        parse_mode="html")


@dp.callback_query(F.data == "create_infro", StateSelection.sectionSelection)
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Отлично! Воспользуйтесь кнопками на клавиатуре',
                                  reply_markup=keybords.keybord_infro_delyana())
    await state.set_state(StateSelection.create_infro)


@dp.callback_query(F.data == "roads_and_sklads")
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Этот раздел еще формируется')
    await state.set_state(StateSelection.create_infro)


@dp.message(F.text.lower() == "другое")
async def another(message: Message):
    await message.answer('НУ другое так другое')


@dp.message(F.text, StateSelection.sectionSelection)
async def no_section(message: Message):
    await message.answer('Кажется у нас нет такого раздела, выберите другой)')


@dp.message(F.text.lower() == 'хуй')
async def no_section(message: Message, state: FSMContext):
    data = await state.get_state()
    await message.answer(str(data))


@dp.message(F.photo)
async def photo(message: Message):
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')


@dp.message(F.text.lower() == 'калькулятор')
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Давайте узнаем стоимость подходящего для тебя тарифа и стоимость внедрения!",
                         reply_markup=keybords.start_brif())
    await state.set_state(StateSelection.calcSelection)


@dp.callback_query(F.data == "start_brif", StateSelection.calcSelection)
async def first(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Введите количество договоров аренды')
    await state.set_state(StateSelection.DA_state)


counter = []


@dp.message(StateSelection.DA_state)
async def second(message: Message, state: FSMContext):
    da = int(message.text)
    counter.append(da)
    await state.update_data(DA_state=da)
    await message.answer(text='Введите количество сотрудников')
    await state.set_state(StateSelection.employes)


@dp.message(StateSelection.employes)
async def third(message: Message, state: FSMContext):
    employes = int(message.text)
    await state.update_data(employes=int(employes))
    await state.set_state(StateSelection.DA_state)
    counter.append(employes)
    await message.answer(
        text='Мы можем подгрузить растровые и векторные карты в ваш аккаунт, введите их количество, если такой необходимости нет введите 0')
    await state.set_state(StateSelection.maps)


@dp.message(StateSelection.maps)
async def mapss(message: Message, state: FSMContext):
    maps = int(message.text)
    counter.append(maps)
    await state.update_data(maps=maps)
    await message.answer(text='Нажмите кнопку', reply_markup=keybords.start_count())
    await state.set_state(StateSelection.count)


def counting(dogovor, sotrudniki, karty):
    # Внедрение
    vnedrenie = dogovor * 15000 + sotrudniki * 5000 + karty * 30000
    return vnedrenie


@dp.callback_query(StateSelection.count and F.data == "start_count")
async def ending(callback: types.CallbackQuery):
    dogovor = counter[0]
    sotrudniki = counter[1]
    karty = counter[2]
    if dogovor <= 3 and sotrudniki <= 10:
        await callback.message.answer(
            '<b>Тариф:</b>Проф\n\n<b>Стоимость лицензии: </b>70000руб/год\n\n<b>Стоимость внедрения:</b>' + str(
                counting(dogovor, sotrudniki, karty)), ' руб', parse_mode='html')

    elif sotrudniki > 20:
        await callback.message.answer(
            '<b>Тариф:</b>Копоративный\n\n<b>Стоимость лицензии: </b> хз руб/год\n\n<b>Стоимость внедрения:</b>' + str(
                counting(dogovor, sotrudniki, karty)), ' руб', parse_mode='html')

    else:
        await callback.message.answer(
            '<b>Тариф:</b>Проф+\n\n<b>Стоимость лицензии: </b>100000руб/год\n\n<b>Стоимость внедрения:</b>' + str(
                counting(dogovor, sotrudniki, karty)), ' руб', parse_mode='html')
    counter.clear()


@dp.message(F.text)
async def no_section(message: Message):
    await message.answer('Выберите что-нибудь из кнопок')


@dp.message(StateSelection.moduleSelection)
async def no_module(message: Message):
    await message.answer('У нас нет такого модуля, пожалуйста нормально выбери да')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
