def la_anagram(word1, word2):
    # Chuyển cả hai từ về chữ thường để so sánh không phân biệt chữ hoa
    word1 = word1.lower()
    word2 = word2.lower()

    # Kiểm tra xem các ký tự đã sắp xếp của cả hai từ có giống nhau không
    return sorted(word1) == sorted(word2)

# Ví dụ sử dụng:
tu1 = "restful"
tu2 = "fluster"

ket_qua = la_anagram(tu1, tu2)

if ket_qua:
    print(f"{tu1} và {tu2} là anagram.")
else:
    print(f"{tu1} và {tu2} không phải là anagram.")
