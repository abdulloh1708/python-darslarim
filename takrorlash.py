"""
Takrorlash

Sana: 15/07/2023

Muallif: Abdulloh
"""

# =============================================================================
# # print("\"Nexia\", \"Tico\", \"Spark\" ko'rganlar qilar havas")
# 
# # print("5 ning 4 darajasi ", 5**4)
# 
# # print("22 ni 4ga bo'lganda qoldiq", 22%4, "ga teng")
# 
# # print("Tomonlari 125 ga teng kvadrat yuzi", 125*125, "ga, perimetri esa", 4*125, "ga teng")
# 
# # print("Diametri 12 ga teng bo'lgan doiraning yuzi", 3.14*(12/2)**2, "ga teng")
# 
# # print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi", (6**2+7**2)**(1/2))
# =============================================================================

# =============================================================================
# # matn = "Assalomu aleykum"
# # print(matn)
# 
# # xabar = "Men keldim."
# # print(xabar)
# 
# # O'zgaruvchini class deb nomlash mumkin emas, sababi class bu maxsus kalit so'z.
# 
# # radius = 5
# # pi = 3.14159
# # aylana_yuzi = pi * radius**2
# # print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)
# =============================================================================

#📱

# =============================================================================
# # kocha = "Bog'bon"
# # mahalla = "Sog'bon"
# # tuman = "Chortoq"
# # viloyat = "Namangan"
# # print(viloyat + " viloyati", tuman + " tumani", mahalla + " mahallasi", kocha + " ko'chasi 99-uy" )
# 
# # print("Iltimos quyidagi ma'lumotlarni kiriting:\n>>>") 
# # kocha = input("Ko'changiz: ")
# # mahalla = input("Mahallangiz: ")
# # tuman = input("Tumanningiz: ")
# # viloyat = input("Viloyatingiz: ")
# # print(viloyat + " viloyati", tuman + " tumani", mahalla + " mahallasi", kocha + " ko'chasi 128-uy")
# 
# # kocha = "Bog'bon"
# # mahalla = "Sog'bon"
# # tuman = "Chortoq"
# # viloyat = "Namangan"
# # print(viloyat + " viloyati,\n", tuman + " tumani,\n", mahalla + " mahallasi\n", kocha + " ko'chasi\n 99-uy\n" )
# 
# # manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, \n{tuman} tumani, {viloyat} viloyati"
# # print(manzil)
# 
# # print(manzil.upper())
# # print(manzil.title())
# # print(manzil.lower())
# # print(manzil.capitalize())
# =============================================================================


# =============================================================================
# # son = int(input("Istalgan sonni kiriting:\n>>>"))
# # print(son, "ning kvadrati", son**2, "ga teng")
# # print(son, "ning kubi", son**3, "ga teng")
# 
# # yosh = int(input("Yoshingiz nechida? \n>>>"))
# # t_yil = 2023-yosh
# # print("Siz", t_yil, "yilda tug'ilgansiz")
# 
# # a = float(input("1-sonni kiriting: \n>>> "))
# # b = float(input("2-sonni kiriting: \n>>>"))
# 
# # print(f"{a}+{b}=", a+b)
# # print(f"{a}-{b}=", a-b)
# # print(f"{a}*{b}=", a*b )
# # print(f"{a}/{b}=", a/b)
# =============================================================================

# =============================================================================
# ismlar = ["Munavvar", "Maftuna", "Shavkatjon", "Farruh", "Odina"]
# print("Salom ", ismlar[0], " opa ishlaringiz yaxshimi?")
# print(f"{ismlar[2]} va {ismlar[3]} kelinlar biznikiga.")
# print(f"{ismlar[1]} opa birga dars qilaylik.")
# 
# friends = []
# friends.append('Shavkatjon')
# friends.append('Munavvar')
# friends.append('Farruh')
# friends.append('Maftuna')
# friends.append('Odina')
# print(friends)
# 
# friends.remove('Odina')
# friends.remove('Farruh')
# friends.remove('Shavkatjon')
# print(friends)
# 
# friends.append('Shuhratjon')
# print(friends)
# 
# friends.insert(0, 'Abduvahob')
# print(friends)
# 
# mehmonlar = []
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(-2))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar )
# =============================================================================

# =============================================================================
# davlatlar = ["O'zbekiston","Qozog'iston", "Qirg'ig'iston", "Dubai"]
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# 
# sonlar = list(range(12, 121))
# print(sonlar)
# print(sum(sonlar))
# print(max(sonlar))
# print(min(sonlar))
# print(sonlar[:16])
# print(sonlar[-15:])
# print(sonlar[12:25])
# 
# taomlar = ('osh', 'somsa', 'manti', 'mastava', 'shashlik', "sho'rva")
# nonushta = taomlar[:]
# nonushta = list(nonushta)
# nonushta.remove('somsa')
# nonushta.remove('manti')
# nonushta.remove('mastava')
# nonushta.remove("sho'rva")
# nonushta.remove('osh')
# nonushta.append('non')
# nonushta.append('qaymoq')
# nonushta.append('choy')
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# nonushta[0] = 'non'
# =============================================================================

# =============================================================================
# dostlar = ['Munavvar', 'Shavkatjon', 'Maftuna', 'Abror']
# for dost in dostlar:
#     print("Salom", dost)
# print('Kod', len(dostlar), 'marta takrorlandi')
# 
# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)
# 
# kinolar = []
# print("3 ta sevimli kinoingiz qaysilar?")
# for k in range(3):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?\n>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)
# =============================================================================

# =============================================================================
# #cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# #for car in cars:
# #    if car == 'gm':
# #        print(car.upper())
# #    else:
# #        print(car.title())
# 
# #cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# #if cars != 'gm':
# #    print(car.upper())
# #else:
# #    print(car.title())
# 
# #login = input("Login kiriting: ")
# #if login.lower() == 'admin':
# #    print("Xush kelibsiz Admin, foydalanuvchilar ro'yhatini ko'rasizmi?  ")
# #else:
# #    print(f"Xush kelibsiz {login.title()}! ")
# 
# #x = float(input("1-sonni kiriting: "))
# #y = float(input("2-sonni kiriting: "))
# #if x == y:   print("sonnlar teng: {x}={y}")
# 
# #son = float(input("Istalgan sonni kiriting: "))
# #print("Son manfiy")  if son<0 else print("Musbat son ")
# 
# #son = float(input('Istalgan son kiriting: '))
# #print(son**(1/2)) if son>0 else print('Musbat son kiriting')
# =============================================================================


 












