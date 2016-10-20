def reverse(hell):
    l=len(hell)
    he=""
    for i in range(l):
        he=he+hell[l-i-1]
    return he
print reverse("abcd")