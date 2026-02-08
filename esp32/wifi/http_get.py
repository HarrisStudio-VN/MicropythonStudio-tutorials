import urequests
import network

# Đảm bảo đã kết nối WiFi trước khi chạy
# URL ví dụ lấy dữ liệu JSON
url = "http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh"

try:
    print("Fetching data from:", url)
    response = urequests.get(url)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    response.close()
except Exception as e:
    print("Error:", e)
