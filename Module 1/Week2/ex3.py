def count_word(file_path):
    word_map = {}
    with open(file_path, 'r') as file:
        while True:
            words_list = file.readline().split(" ")
            if words_list != ['']:
                for word in words_list:
                    if word in word_map:
                        word_map[word] += 1
                    else:
                        word_map[word] = 1
            else:     
                return word_map

print(count_word("D://FPT//AIO2024_GitHub//Module 1//Week2//P1_data.txt"))

