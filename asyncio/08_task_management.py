"""
[Tutorial 08] Quản lý Task: Gather và Cancel
Mô tả: Cách chạy nhiều task và chờ tất cả hoàn thành (gather), hoặc hủy một task đang chạy (cancel).
"""

import asyncio

async def background_service():
    """Một dịch vụ chạy nền mãi mãi cho đến khi bị hủy"""
    try:
        while True:
            print("Service: Đang kiểm tra hệ thống...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Service: Đang dọn dẹp trước khi dừng...")
        await asyncio.sleep(0.5)
        print("Service: Đã dừng an toàn.")

async def computation_task(n):
    """Giả lập một tính toán tốn thời gian"""
    print(f"Task {n}: Bắt đầu...")
    await asyncio.sleep(n)
    print(f"Task {n}: Xong.")
    return n * 10

async def main():
    # 1. Sử dụng gather để chạy nhiều task và lấy kết quả trả về cùng lúc
    print("--- Thử nghiệm asyncio.gather ---")
    results = await asyncio.gather(
        computation_task(1),
        computation_task(2)
    )
    print(f"Kết quả thu được: {results}")

    # 2. Thử nghiệm việc hủy task (Cancel)
    print("\n--- Thử nghiệm cancel task ---")
    srv = asyncio.create_task(background_service())
    
    await asyncio.sleep(3)
    print("Main: Đã đủ thời gian, yêu cầu dừng Service...")
    srv.cancel()
    
    # Chờ task hoàn tất việc dọn dẹp sau khi bị cancel
    try:
        await srv
    except asyncio.CancelledError:
        print("Main: Xác nhận Service đã bị hủy thành công.")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
