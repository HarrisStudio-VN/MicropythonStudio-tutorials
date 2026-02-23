"""
[Tutorial 05] Đồng bộ hóa với Event (Asyncio Event)
Mô tả: Cách dùng Event để đồng bộ giữa các task. Task A chờ Task B báo hiệu mới chạy tiếp.
"""

import asyncio

# Tạo một đối tượng Event toàn cục
trigger_event = asyncio.Event()

async def worker_task(id):
    print(f"Worker {id}: Đang chờ tín hiệu kích hoạt...")
    # Chờ cho đến khi event.set() được gọi ở đâu đó
    await trigger_event.wait()
    print(f"Worker {id}: Đã nhận tín hiệu! Bắt đầu xử lý...")
    await asyncio.sleep(1)
    print(f"Worker {id}: Hoàn thành công việc.")

async def control_task():
    print("Control: Chờ 3 giây trước khi kích hoạt các worker...")
    await asyncio.sleep(3)
    print("Control: KÍCH HOẠT!")
    # Phát tín hiệu cho tất cả các task đang chờ .wait()
    trigger_event.set()
    
    await asyncio.sleep(2)
    print("Control: Reset event để các worker sau phải chờ tiếp.")
    trigger_event.clear()

async def main():
    # Chạy 3 worker chờ tín hiệu
    asyncio.create_task(worker_task(1))
    asyncio.create_task(worker_task(2))
    asyncio.create_task(worker_task(3))
    
    # Task điều khiển
    await control_task()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Dừng chương trình.")
