def levenshtein_distance(string1, string2):
    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo hàng đầu tiên và cột đầu tiên của bảng
    for i in range(m + 1):
        dp[i][0] = i  # Chi phí khi chuyển từ chuỗi dài i thành chuỗi rỗng
    for j in range(n + 1):
        dp[0][j] = j  # Chi phí khi chuyển từ chuỗi rỗng thành chuỗi dài j

    # Tính toán khoảng cách cho các phần tử còn lại
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                cost = 0  # Không cần thay thế nếu ký tự giống nhau
            else:
                cost = 1  # Chi phí thay thế nếu ký tự khác nhau

            dp[i][j] = min(dp[i - 1][j] + 1,      # Chi phí xóa
                           dp[i][j - 1] + 1,      # Chi phí chèn
                           dp[i - 1][j - 1] + cost)  # Chi phí thay thế

    return dp[m][n]
    
print(levenshtein_distance("abc", "bavd"))