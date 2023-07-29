
"""
Mavzu: If- elif- else

24/07/2023

Muallif: Abdulloh
"""

yosh = int(input('Yoshingiz nechida?: '))
if yosh <=4:
    print("Sizga kirish bepul.")
elif yosh<=12:
    print("Sizga kirish 5000 so'm")
elif yosh<=20:
    print("Sizga kirish 8000 so'm")
else:
    print("Sizga kirish 1000 so'm")

#yosh = int(input('Yoshingiz nechida?: '))
#if yosh <=15:
#    narh = 0
#elif yosh<=16:
#    narh = 5000
#elif yosh<=20:
#    narh = 8000
#else:
#    narh = 10000
#    print(f"Sizga kirish {narh} so'm")

#kun = input("Bugun nima kun?>>> ")
#if kun.lower()== 'shanba' or kun.lower()== 'yakshanba':
#    print("Bugun dam olish kuni.")
#else:
#    print('Bugun ish kuni.')

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<30:
#    print("Uyda dam olamiz!")

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#    print("Uyda dam olamiz!")

#narh = 15000
#choy = True
#salat = False
#if choy and salat:
#    narh = narh + 10000
#elif choy or salat:
#    narh = narh + 5000
#print(f"Jami {narh} so'm")

#narh = 15000
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#
#if choy:
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#    
#if salat:
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#    
#if non:
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#    
#if kompot:
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#    
#if assorti:
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
#    
#print(f"Jami {narh} so'm")

#narh = 15000
#choy = 1
#salat = 0
#non = 1
#kompot = 1
#assorti = 1

#if choy:
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#
#if salat:
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#
#if non:
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#
#if kompot:
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#
#if assorti:
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
#
#print(f"Jami {narh} so'm")

#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#'manti' in menu # menu da manti bormi?

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'osh' in menu # menu da osh bormi?

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>> ')
#if ovqat.lower() in menu:
#    print('Buyurtma qabul qilindi.')
#else:
#    print('Afsuski bizda bunday ovqat yo\'q')

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>> ')
#if ovqat.lower() not in menu:
#    print('Afsuski bizda bunday ovqat yo\'q')
#else:
#    print('Buyurtma qabul qilindi.')

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik', 'sho\'rva']

#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor.")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q.")

#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor.")
#        else: # agar ro'yxat bo'sh bo'lsa
#           print(f"Kechirasiz, menuda {taom} yo'q")
#else:
#    print("Savatchangiz bo'sh!")
           
son = float(input("Juft sonni kirting: "))
if son%2:
    print("Bu son juft emas.")
else:
    print("Rahmat.")













