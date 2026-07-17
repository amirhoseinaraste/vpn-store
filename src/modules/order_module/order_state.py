# from packages
from aiogram.fsm.state import State, StatesGroup


# from file

class PaymentState(StatesGroup):
    waiting_for_receipt = State()

    