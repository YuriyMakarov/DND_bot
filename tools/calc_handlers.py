from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State

from tools.jumps import *
from tools.converter_coins import *
from keyboards import make_reply_keyboard, calc_keyboard


class JumpStates(StatesGroup):
    strength_jump = State()


router = Router()


@router.message(Command(commands=["tools"]))
@router.message(F.text == "Инструменты")
async def tool(message: Message):
    await message.answer(
        text="Инструменты:"
             "Расчет прыжков(/calc_jump)\n"
             "Расчет переносимого веса(/calc_weight) - В разработке\n"
             "Конвертер монет(/convert_coins) - В разработке",
        reply_markup=make_reply_keyboard(calc_keyboard, 1, 1, 1)
    )


@router.message(StateFilter(None), Command(commands=["calc_jump"]))
@router.message(StateFilter(None), F.text == "Расчет прыжков")
async def tool_jump(message: Message, state: FSMContext):
    await message.answer(text="Введите значение характеристики силы вашего персонажа")
    await state.set_state(JumpStates.strength_jump)


@router.message(JumpStates.strength_jump)
async def super_jump(message: Message, state: FSMContext):
    await message.answer(text="Делаем расчет")
    try:
        har_strength = int(message.text)
        await message.answer(
            text=f"Прыжок в высоту\n"
                 f"При разбеге в 10 футов: {get_jump_height(har_strength=har_strength, running_start=True)}\n"
                 f"Без разбега: {get_jump_height(har_strength=har_strength, running_start=False)}\n"
                 f"_____________________________________\n"
                 f"Прыжок в длину\n"
                 f"При разбеге в 10 футов: {get_jump_length(har_strength=har_strength, running_start= True)}\n"
                 f"Без разбега: {get_jump_length(har_strength=har_strength, running_start= False)}\n")
    except ValueError:
        await message.answer(text="Введите положительное число, а не строку.")
    except CharacteristicMinimumError:
        await message.answer(text="Значение характеристики должно быть 5 или выше")
    finally:
        await state.clear()


@router.message(Command(commands=["calc_weight"]))
@router.message(F.text == "Расчет веса")
async def tool_weight(message: Message):
    await message.answer(text="Сказали же, В РАЗРАБОТКЕ, БЛЯТЬ")


@router.message(Command(commands=["converter_coins"]))
@router.message(F.text == "Конвертер монет")
async def tool_convert_coins(message: Message):
    await message.answer(text="Ваш счет")