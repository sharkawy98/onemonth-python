#######
#Create a function called uppercase_and_reverse that takes a little bit of text,
#uppercases it all, and then reverses it (flips all the letters around)
#######

def uppercase_and_reverse(text):
    text = text.upper()
    # result = ''
    # for c in range(len(text)-1, -1, -1): #reversed(text) or text[::-1] 
    #     result += text[c]
    return text[::-1]
   

print(uppercase_and_reverse("ahmed"))