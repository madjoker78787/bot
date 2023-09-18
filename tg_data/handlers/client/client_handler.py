from aiogram import types, Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from tg_data.data import define
from tg_data.handlers.client import client_kb as kb
from tg_data.keyboards.factory_callback_keyboard import factory_keyboard, \
    NumbersCallbackFactory, assembly_keyboard, build_keyboard

router = Router()


@router.message(Command("start"))
async def start(msg: Message, state: FSMContext):
    await state.clear()
    # try:
    #     await msg.delete()
    # except:
    #     pass
    await msg.answer(f"{define.welcome_text}",
                     reply_markup=assembly_keyboard(kb.menu))


@router.callback_query(F.data.startswith("menu"))
async def call_menu(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("♻ Подождите, запрос обрабатывается...")

    await call.message.edit_text(f"{define.text}",reply_markup=build_keyboard(kb.menu))


@router.callback_query(F.data.startswith("shopping"))
async def select_city(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("♻ Подождите, запрос обрабатывается...")

    await call.message.edit_text("➖" * 15 +
                                 "\n\nВыбери город из списка ⬇\n\n"
                                 + "➖" * 15, reply_markup=build_keyboard(buttons=kb.city))


@router.callback_query(F.data.startswith("city"))
async def select_region(call: types.CallbackQuery, state: FSMContext):
    print(call.data)





# @router.callback_query(NumbersCallbackFactory.filter())
# async def shoping(call: types.CallbackQuery,
#                       callback_data: NumbersCallbackFactory):
#     print(callback_data.action, callback_data.value)
#     await call.message.answer(f"{callback_data.value}")
