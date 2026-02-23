"""
[Tutorial 02] Chạy nhiều Task cùng lúc (Concurrency)
Mô tả: Hướng dẫn cách tạo và chạy nhiều task đồng thời mà không chờ nhau.
"""

import asyncio

async def task_one():
    while True:
        print("--- Task 1 đang chạy (mỗi 1 giây)")
        await asyncio.sleep(1)

async def task_two():
    while True:
        print("+++ Task 2 đang chạy (mỗi 2 giây)")
        await asyncio.sleep(2)

async def main():
    print("Khởi tạo các tasks...")
    
    # asyncio.create_task() dùng để lập lịch cho một coroutine chạy trong nền
    # Sau khi gọi lệnh này, task sẽ tự chạy mà không cần 'await' ngay lập tức
    t1 = asyncio.create_task(task_one())
    t2 = asyncio.create_task(task_two())
    
    # Giữ cho main() chạy mãi mãi để các task nền không bị hủy
    # Nếu main() kết thúc, mọi task tạo bởi create_task sẽ biến mất
    while True:
        await asyncio.sleep(10)

# Chạy loop
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Đã dừng chương trình.")
