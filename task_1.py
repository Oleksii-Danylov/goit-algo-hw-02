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
