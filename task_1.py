''' Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.
Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:
У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає їх до черги, та process_request(), яка обробляє заявки, видаляючи їх із черги. Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок та їх обробку.'''

import queue
import random
import time

request_queue = queue.Queue()

request_id = 1

def generate_request():
    global request_id
    # Створення заявки
    request = f"Заявка {request_id}"
    request_id += 1
    # Додавання до черги
    request_queue.put(request)
    print(f"Створено: {request}")

def process_request():
    if not request_queue.empty():
        # Видалення заявки з черги
        request = request_queue.get()
        # Обробка заявки
        print(f"Обробляється: {request}")
        time.sleep(4)  #затримка
        print(f"Оброблено: {request}")
    else:
        print("Черга пуста")

if __name__ == "__main__":
    try:
        while True:
            if random.random() > 0.5:
                generate_request()
            
            process_request()
            
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nExit")
