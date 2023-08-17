BM1= float(input("notas do primeiro bimestre: "))
BM2= float(input("notas do segundo bimestre: "))
BM3= float(input("notas do terceiro bimestre: "))
BM4= float(input("notas do quarto bimestre: "))
MEDIA= float((BM1+BM2+BM3+BM4)/4)
print ("digite a media",MEDIA)
if MEDIA>=9:
   print ("Aprovado com louvor")
elif MEDIA>=7:
   print ("Aprovado")
elif MEDIA<7: 
   print ("Reprovado")