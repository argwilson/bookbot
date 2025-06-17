def get_num_words(string):
    return len(string.split())

def get_num_characters(string):
    char_count_dict = {}
    for char in string:
        char = char.lower()
        if char not in char_count_dict:
            char_count_dict[char] = 0
        char_count_dict[char] += 1
    return char_count_dict
        
def sorted_dict_list(dictionary):
    char_dict = {}
    char_list = []
    for key in dictionary:
        char_dict['char'] = key
        char_dict['num'] = dictionary[key]
        char_list.append(char_dict)
        char_dict = {}
    char_list.sort(reverse=True, key=lambda element: element['num'])
    return char_list
