# sevimli_t = {
#     'Ali': 'osh',
#     'Vali': 'manti',
#     'Sali': 'qozonkabob',
#     'Olim': 'shashlik',
#     'Akbar': "lag'mon"
# }

# print(f'Alining sevimli taomi {sevimli_t["Ali"]}')
# print(f'Valining sevimli taomi {sevimli_t["Vali"]}')
# print(f'Akbarning sevimli taomi {sevimli_t["Akbar"]}')

lugat = {
    'integer': 'Butun son',
    'float': 'Suzuvchi son',
    'Boolean': 'Mantiqiy tur',
    'for': 'Sikl',
    'if': 'Agar',
    'else': 'aks holda',
    'list': "ro'yhat",
    'tuple': "o'zgarmas ro'yhat",
    'pop':"Sug'urib olish metodi",
    'append': "ro'yhat oxiriga element qo'shish"
}

# s = input("Kalit so'z kiriting: ")
# print(lugat.get(s,"Bunday so'z mavjud emas"))


s = input("Kalit so'z kiriting: ")
if s in lugat:
    print(lugat[s])
else:
    print("Bunday so'z mavjud emas")