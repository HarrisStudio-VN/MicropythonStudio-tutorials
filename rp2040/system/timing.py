import time

print("Microsecond Timing measurement.")

# Lấy thời điểm bắt đầu (uS)
start = time.ticks_us()

# Một khối mã cần đo thời gian
time.sleep_ms(10) 
for i in range(1000):
    pass

# Lấy thời điểm kết thúc
end = time.ticks_us()

# Tính toán chênh lệch
diff = time.ticks_diff(end, start)

print(f"Execution took: {diff} uS")
