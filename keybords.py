import types

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def main_keybord() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Мобильное приложения📱")
    kb.button(text="Web-приложение 🖥"),
    kb.button(text="Модуль 1c")
    kb.adjust(2, 2)
    return kb.as_markup(resize_keyboard=True)


def keybord_infro() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Деляны')
    kb.button(text='Создать деляну по GPX')
    kb.button(text='Создать дорогу по GPX')
    kb.button(text='Загрузка xml деклараций')
    kb.button(text='Создать склад')
    kb.button(text="Другое")
    kb.button(text="Назад 🔙")
    kb.adjust(3, 3)

    return kb.as_markup(resize_keyboard=True)


def keybord_infro_delyana() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Создать деляну по GPX')
    kb.button(text='Загрузка xml деклараций')
    kb.button(text='Информация о деляне')
    kb.button(text="Приложение к отчету")
    kb.button(text="Назад 🔙")
    kb.adjust(2,2,2)

    return kb.as_markup(resize_keyboard=True)


def mobile_app_first_keybord() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Запись трека")
    kb.button(text="Фотозамер штабелей"),
    kb.button(text="Карты/спутники")
    kb.button(text="Загрузка карт для использования оффлайн")
    kb.button(text="Назад 🔙")
    kb.button(text="Другое")

    kb.adjust(3, 1, 2)
    return kb.as_markup(resize_keyboard=True)


def treckRecording_keybord() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Спасибо! Проблема решена!")
    kb.button(text="Ничего не понятно!")
    kb.button(text="Назад 🔙")

    kb.adjust(1, 1, 1)
    return kb.as_markup(resize_keyboard=True)


def web_first_keybord() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Оцифровка планшетов")
    kb.button(text="Фотозамер штабеля")
    kb.button(text="Личный кабинет")
    kb.button(text="Cоздание инфраструктуры")
    kb.button(text="Режим шторки")
    kb.button(text="Другое")
    kb.button(text="Назад 🔙")

    kb.adjust(3, 1, 3)
    return kb.as_markup(resize_keyboard=True)


def inline_infro_delyana():
    builder = InlineKeyboardBuilder()
    builder.button(text='Смотреть', callback_data='create_infro')

    builder.adjust()
    return builder.as_markup()


def inline_infro_roads_and_sklads():
    builder = InlineKeyboardBuilder()
    builder.button(text='Смотреть', callback_data='roads_and_sklads')

    builder.adjust()
    return builder.as_markup()
