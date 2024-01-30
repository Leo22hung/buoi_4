def la_palindrome(s):
    # Chuyển đổi chuỗi thành chữ thường để so sánh không phân biệt chữ hoa
    s = s.lower()

    # Khởi tạo con trỏ cho đầu và cuối của chuỗi
    start = 0
    end = len(s) - 1

    # Tiếp tục kiểm tra cho đến khi con trỏ gặp nhau ở giữa
    while start < end:
        # Bỏ qua các ký tự không phải chữ cái hoặc số từ đầu
        while start < end and not s[start].isalnum():
            start += 1

        # Bỏ qua các ký tự không phải chữ cái hoặc số từ cuối
        while start < end and not s[end].isalnum():
            end -= 1

        # So sánh các ký tự (không phân biệt chữ hoa)
        if s[start].lower() != s[end].lower():
            return False

        # Di chuyển con trỏ về phía trung tâm
        start += 1
        end -= 1

    # Nếu vòng lặp hoàn thành, chuỗi là palindrome
    return True

# Ví dụ sử dụng:
chuoi_nhap = "A man, a plan, a canal, Panama!"
ket_qua = la_palindrome(chuoi_nhap)
print(ket_qua)
