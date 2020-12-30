def string_transformer(s):
    new_string = []
    new = s.lower()
    for i in range(0,len(s)):
        if s[i] == " ":
            return " "
        if s[i] == new[i]:
            a = s[i].upper()
            new_string.append(a)

        if s[i] != new[i]:
            b = s[i].lower()
            new_string.append(b)



    return

print(string_transformer("Example string"))