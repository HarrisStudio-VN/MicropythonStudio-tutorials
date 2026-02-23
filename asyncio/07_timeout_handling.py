"""
[Tutorial 07] Xử lý Timeout (asyncio.wait_for)
Mô tả: Cách giới hạn thời gian chờ của một task. Rất quan trọng khi kết nối WIFI hoặc Sensor.
"""

import asyncio

async def long_running_task():
    """Giả lập một việc tốn 5 giây (ví dụ: chờ phản hồi server)"""
    print("Task: Đang bắt đầu làm việc cực nhọc...")
    await asyncio.sleep(5)
    return "Dữ liệu hoàn tất!"

async def main():
    print("Bắt đầu gọi task với giới hạn thời gian 2 giây...")
    
    try:
        # Chờ task hoàn thành nhưng không quá 2 giây
        result = await asyncio.wait_for(long_running_task(), timeout=2)
        print(f"Thành công: {result}")
    except asyncio.TimeoutError:
        print("Lỗi: Task chạy quá lâu (Timeout)! Hủy task và tiếp tục việc khác...")
    
    print("Chương trình vẫn chạy bình thường sau khi timeout.")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Dừng.")
