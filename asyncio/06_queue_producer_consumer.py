"""
[Tutorial 06] Hàng đợi Producer-Consumer (Asyncio Queue)
Mô tả: Cách truyền dữ liệu an toàn giữa các task bằng Queue.
Ví dụ: Task đọc cảm biến (Producer) gửi dữ liệu vào hàng đợi, Task xử lý (Consumer) lấy ra xử lý.
"""

import asyncio
import random

# Tạo hàng đợi có kích thước giới hạn là 5 phần tử
queue = asyncio.Queue(5)

async def producer():
    """Giả lập việc đọc cảm biến và đưa vào hàng đợi"""
    count = 0
    while True:
        data = f"SensorData-{count}"
        print(f"Producer: Đang gửi {data} vảo hàng đợi...")
        # put() sẽ chờ nếu hàng đợi bị đầy (backpressure)
        await queue.put(data)
        count += 1
        await asyncio.sleep(random.uniform(0.5, 1.5)) # Gửi dữ liệu ngẫu nhiên

async def consumer():
    """Lấy dữ liệu từ hàng đợi và xử lý"""
    while True:
        # get() sẽ chờ cho đến khi có dữ liệu trong hàng đợi
        data = await queue.get()
        print(f"Consumer: Đã nhận và đang xử lý {data}...")
        await asyncio.sleep(2) # Giả lập thời gian xử lý lâu
        print(f"Consumer: Xử lý xong {data}.")
        # Báo hiệu task đã xong
        queue.task_done()

async def main():
    print("Khởi chạy mô hình Producer-Consumer...")
    # Chạy producer và consumer độc lập
    asyncio.create_task(producer())
    asyncio.create_task(consumer())
    
    while True:
        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Dừng chương trình.")
