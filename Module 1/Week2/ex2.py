def count_characters(string):
    string_list = list(string)
    character_map = {}
    for character in string_list:
        if character in character_map:
            character_map[character] = character_map.get(character)+1
        else:
            character_map[character] = 1
    return character_map
print(count_characters("Happiness"))