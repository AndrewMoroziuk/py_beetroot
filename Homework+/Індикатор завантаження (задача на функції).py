import time


def load(t_sleep: float = 0.5, iteration: int = -1):
    """
    Функція для отримання анімації індикатора завантаження / очікування
    :param t_sleep: інтервал між зміною фреймів анімації (сек.)
    :param iteration: кількість ітерацій (за замовчуванням -1 => безкінечний цикл)
    :return: None
    """
    symbol = ('--', '\\\\', '||', '//')
    while iteration != 0:
        for i in range(len(symbol)):
            print(symbol[i], end='')
            time.sleep(t_sleep)
            print('\r', end='')
        iteration -= 1


load(0.4, 4)  # запуск функції
