"""
[Tutorial 03] Điều khiển LED (Hardware) không chặn
Mô tả: Nháy 2 LED với tần số khác nhau bằng Asyncio.
Đây là ưu điểm lớn nhất của Asyncio so với dùng time.sleep() truyền thống.
"""

import asyncio
from machine import Pin

# Cấu hình chân (Thay đổi số chân tùy thuộc vào board của bạn)
# Ví dụ ESP32: Pin 2 là LED onboard, Pin 4 là LED ngoài
led_blue = Pin(2, Pin.OUT)
led_red = Pin(4, Pin.OUT)

async def blink_blue():
    """Nháy LED xanh mỗi 0.5 giây"""
    while True:
        led_blue.value(not led_blue.value())
        # Không dùng time.sleep(), dùng asyncio.sleep() để tránh treo task khác
        await asyncio.sleep(0.5)

async def blink_red():
    """Nháy LED đỏ mỗi 0.15 giây (nhanh hơn)"""
    while True:
        led_red.value(not led_red.value())
        await asyncio.sleep(0.15)

async def main():
    print("Bắt đầu nháy LED bất đồng bộ...")
    
    # Tạo 2 task chạy song song
    asyncio.create_task(blink_blue())
    asyncio.create_task(blink_red())
    
    # Vòng lặp main làm việc khác hoặc đơn giản là chờ
    while True:
        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    # Tắt LED khi dừng
    led_blue.off()
    led_red.off()
    print("Dừng nháy LED.")
