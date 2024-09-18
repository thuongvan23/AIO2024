def load_vocab (file_path):
    with open (file_path, 'r') as f :
        lines = f . readlines ()
        words = sorted (set ([ line . strip () . lower () for line in lines ]) )
    return words
# vocabs = load_vocab('D://FPT//AIO2024_GitHub//Module 1//Week4//source//data//vocab.txt')
# print(vocabs)

def levenshtein_distance ( string1 , string2 ) :
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

import streamlit as st

def main():
    vocabs = load_vocab('D://FPT//AIO2024_GitHub//Module 1//Week4//source//data//vocab.txt')

    st.title('Word Correction using Levenshein Distance')
    word = st.text_input('Word: ')

    if st.button('Compute: '):
        leven_distances = dict()

        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item:item[1]))
        correct_word = list(sorted_distances)[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary: ')
        col1.write(vocabs)

        col2.write('Distance: ')
        col2.write(sorted_distances)
if __name__ == "__main__":
    main()

