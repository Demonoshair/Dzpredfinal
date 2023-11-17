import logging
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="a",
    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s"
)
numbers = [1, 2, 3, 4, 5]           # итерируемый объект
iterable_numbers = iter(numbers)    # итератор

while True:
    try:
        current_number = next(iterable_numbers)
        logging.info(f"Мы взяли из корзинки тыблочко под номером {current_number}!")
    except StopIteration:
        logging.error("Корзинка пуста!")
        break
    sleep(1)

print('Happy End!')