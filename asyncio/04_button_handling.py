"""
[Tutorial 04] Xử lý nút nhấn (Button) không chặn
Mô tả: Cách đọc trạng thái nút nhấn và chống rung (debounce) hiệu quả bằng asyncio.
"""

import asyncio
from machine import Pin

# Cấu hình nút nhấn (Dùng pull-up nội bộ)
button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

async def wait_button():
    """Task theo dõi nút nhấn"""
    print("Đang chờ nhấn nút (Pin 0)...")
    last_state = button.value()
    
    while True:
        current_state = button.value()
        
        # Kiểm tra nếu trạng thái thay đổi từ 1 sang 0 (nhấn xuống)
        if last_state == 1 and current_state == 0:
            print("Nút đã được nhấn!")
            led.value(not led.value()) # Đảo trạng thái LED
            
            # Chống rung (Debounce): Chờ một chút trước khi đọc tiếp
            await asyncio.sleep_ms(200) 
        
        last_state = current_state
        
        # Luôn cần sleep một chút (dù là rất nhỏ) để nhường CPU cho task khác
        await asyncio.sleep_ms(20)

async def other_bg_task():
    """Một công việc khác chạy nền để chứng minh không bị chặn"""
    count = 0
    while True:
        print(f"Hệ thống vẫn đang hoạt động... ({count})")
        count += 1
        await asyncio.sleep(2)

async def main():
    # Chạy song song cả việc đọc nút và việc nền
    asyncio.create_task(wait_button())
    asyncio.create_task(other_bg_task())
    
    while True:
        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Dừng chương trình.")
