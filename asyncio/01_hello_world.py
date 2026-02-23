"""
[Tutorial 01] Cơ bản về Asyncio - Chạy task đầu tiên
Mô tả: Hướng dẫn cách định nghĩa một hàm bất đồng bộ (coroutine) và chạy nó.
"""

import asyncio

# Định nghĩa một coroutine bằng từ khóa 'async def'
# Coroutine là một hàm có thể tạm dừng thực thi để nhường chỗ cho các task khác
async def hello_task():
    print("Bắt đầu task...")
    
    # 'await' được dùng để tạm dừng coroutine này cho đến khi sleep hoàn tất
    # Trong lúc sleep, MicroPython có thể làm việc khác thay vì treo máy (blocking)
    await asyncio.sleep(1)
    
    print("Chào mừng bạn đến với MicroPython Asyncio!")

# Điểm vào (Entry point) của chương trình
async def main():
    print("Chương trình đang khởi động...")
    
    # Chạy coroutine hello_task
    await hello_task()
    
    print("Kết thúc chương trình.")

# Chạy vòng lặp sự kiện (Event Loop)
# Đây là cách chính thống để khởi chạy ứng dụng asyncio trong MicroPython
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Đã dừng bởi người dùng.")
