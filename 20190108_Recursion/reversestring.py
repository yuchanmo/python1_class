def reverse(s):
    if s == "":
        return s
    print(s[1:])
    return reverse(s[1:])+s[0]

reverse('hello')