def dao_nguoc_so_nguyen(num):
    so_nguyen_dao_nguoc = 0

    while num != 0:
        # Trích xuất chữ số cuối cùng của số
        chu_so = num % 10

        # Thêm chữ số vào số nguyên đảo ngược
        so_nguyen_dao_nguoc = so_nguyen_dao_nguoc * 10 + chu_so

        # Loại bỏ chữ số cuối cùng từ số nguyên gốc
        num = num // 10

    return so_nguyen_dao_nguoc

# Ví dụ sử dụng:
so_nguyen_nhap = 1234
ket_qua = dao_nguoc_so_nguyen(so_nguyen_nhap)
print(ket_qua)
