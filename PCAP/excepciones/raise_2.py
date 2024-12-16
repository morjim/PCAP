

def mal_asunto(n):
    try:
        return n/0
    except:
        print ("Lo hice de nuevo")
        raise ValueError

try:
    mal_asunto(0)
except ArithmeticError:
    print ("ya veo!!")
    exit()

print ("en -fin")