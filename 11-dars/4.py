mahsulotlar = ['anor', 'uzum', 'apelsin', 'tarvuz', 'qovun', 'olma', 'ananas', 'yong\'oq', 'shaftoli', 'o\'rik']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for i in range(5):
    savat.append(input(f'Savatga {i+1}-mahsulotni kiriting: '))
for i in savat:
    if i.lower() in mahsulotlar:
        bor_mahsulotlar.append(i)
    else:
        mavjud_emas.append(i)

if mavjud_emas:
    print('Do\'konimizda quyidagi mahsulotlar yo\'q: ')
    for i in mavjud_emas:
        print(i)
else:
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
