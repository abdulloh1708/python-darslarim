"""
Mavzu: Xatolar ustida ishlash

26/07/2023

Muallif: Abdulloh
"""

# =============================================================================
# #SyntaxError
# #print"Hello World!"
# #print("Hello World!
# #print("Hello World!"
# =============================================================================

# =============================================================================
# # IndentationError
# # print("Hello World!")
# #print("O'ngacha sanaymiz")
# #for n in range(10):
# #    print(n)
# #    print(n+1)
# 
# #son = 50
# #if son>=0:
# #    print("Musbat son")
# #else:
# #    print("Manfiy son")
# =============================================================================

# =============================================================================
# # TypeError
# #son = input("Istalgan son kiriting: ")
# #son = int(son)
# #print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================

# =============================================================================
# # NameError
# #prit("Hello World!")
# #mevalar = ['olma','uzum','nok','anor','anjir']
# #for meva in mvealar:
# #    print(meva)
# =============================================================================

# =============================================================================
# # ValueError
# #son = int(float(input("Istalgan son kiriting: ")))
# #if son>=0:
# #    print("Musbat son")
# #else:
# #    print("Manfiy son")
# =============================================================================

# =============================================================================
# # IndexError
# #mevalar = ['olma', 'anor', 'uzum']
# #print(mevalar[3])
# =============================================================================

# =============================================================================
# ZeroDivisionError
#x, y = 50, 50
#z = 250/(50-50)
# =============================================================================

# Mantiqiy xatolar
# =============================================================================
# radius = 5
# pi = 3.14
# aylana_yuzi =pi*radius**2
# print(aylana_yuzi)
# 
# son = float(input("Istalgan son kiriting: "))
# ildiz = son**0.5
# print(f"{son} ning ildizi {ildiz} ga teng")
# 
# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi.")
# =============================================================================

"""
Vazifa

Sana: 26/07/2023

Muallif: Abdulloh
"""

#son = float(input("Juft son kiriting: "))
#if son%2:
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")

#yosh = (input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#    narh = 0
#elif yosh <=18:
#    narh = 10000
#else:
#    narh = 20000
#    print(f"Chipta {narh} so'm")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))

#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#for n in range(5):
#    mahsulotlar.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if mahsulotlar:
#    for mahsulot in mahsulotlar:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
        
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
#    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)
#if mavjud_emas:
#  print("Do'konimizda quyidagi mahsulotlar yo'q:")
#for mahsulot in mavjud_emas:
#  print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
#users = ['alisher1983','aziza','yasina' 'umar']
#login = input("Yangi login tanlang: ")
#if login in users:
#    print('Login band, yangi login tanalng!')
#else:
#    print("Xush kelibsiz!")