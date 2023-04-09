
def cezar_code(text, move_by):
    cezar_table = []
    for i in range(65, 90):
        cezar_table.append(i)
    for i in range(97, 122):
        cezar_table.append(i)

    result = ""
    for letter in text:
        letter_code = ord(letter)
        in_table = False
        index_in_table = 0
        for number in cezar_table:
            if number == letter_code:
                in_table = True
                break
            index_in_table = index_in_table + 1

        if in_table:
            index_in_table = index_in_table + move_by
            if index_in_table >= len(cezar_table):
                index_in_table = len(cezar_table) - index_in_table

            result = result + chr(cezar_table[index_in_table])
        else:
            result = result + letter

    return result


print(cezar_code("hello World", 1))