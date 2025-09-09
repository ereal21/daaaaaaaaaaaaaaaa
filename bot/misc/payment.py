import asyncio
import random
from typing import Optional

from yoomoney import Quickpay, Client

from bot.misc import EnvKeys


def quick_pay(message):
    bill = Quickpay(
        receiver=EnvKeys.ACCOUNT_NUMBER,
        quickpay_form="shop",
        targets="Sponsor",
        paymentType="SB",
        sum=message.text,
        label=str(message.from_user.id) + '_' + str(random.randint(1000000000, 9999999999))
    )
    label = bill.label
    url = bill.base_url
    return label, url


async def check_payment_status(label: str) -> Optional[str]:
    token = EnvKeys.ACCESS_TOKEN
    if not token:
        return None

    def _history():
        client = Client(token=token)
        return client.operation_history(label=label)

    history = await asyncio.to_thread(_history)
    for operation in getattr(history, "operations", []):
        return operation.status
    return None
