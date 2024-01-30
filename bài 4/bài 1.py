def dao_nguoc_mang_tai_cho(arr):
    # Lấy độ dài của mảng
    n = len(arr)

    # Duyệt chỉ qua nửa đầu của mảng
    for i in range(n // 2):
        # Đổi chỗ các phần tử từ đầu và cuối
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# Ví dụ sử dụng:
mang_vao = [1, 2, 3, 4, 5]
dao_nguoc_mang_tai_cho(mang_vao)
print(mang_vao)
