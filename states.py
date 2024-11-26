from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup


class StateSelection(StatesGroup):
    moduleSelection = State()
    sectionSelection = State()
    mobile_app_state = State()
    create_infro = State()
    ls_state = State()
    DA_state = State()
    count = State()
    employes = State()
    maps = State()
