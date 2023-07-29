"""
#07-dars: List

Sana: 07/09/2023

Muallif: Abdulloh
"""

# =============================================================================
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())
# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])
# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)
# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)
# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)
# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)
# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)
# =============================================================================

"""
Vazifa

Sana: 07/09/2023

Muallif: Abdulloh

"""

# =============================================================================
# ismlar = ['Rahmatilla', 'Abror', 'Shavkatjon', 'Abduvahob']
# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(f"{ismlar[2]} va {ismlar[3]} kelinlar biznikiga")
# print(ismlar[-1] + " kel birga dars qilamiz")
# 
# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# print(sonlar)
# 
# sonlar[0] = sonlar[0]+sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 37
# del sonlar[5]
# print(sonlar)
# 
# t_shaxslar = ['Amir Temur','Imom Buxoriy',]
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
# 
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# suhbat qilishni istar edim\n")
# 
# friends = []
# friends.append('Rahmatilla')
# friends.append('Abror')
# friends.append('Shavkatjon')
# friends.append('Abduvahob')
# print(friends)
# 
# friends.remove('Abror')
# friends.remove('Abduvahob')
# print(friends)
# 
# friends.append('Abduvahob')
# friends.insert(0, 'Otabek')
# friends.insert(2, 'Akmaljon')
# print(friends)
# 
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)
# =============================================================================