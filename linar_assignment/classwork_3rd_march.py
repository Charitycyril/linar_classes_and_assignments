#print(3+4*5//6**2+1//5-3)
book=int(input("line1.b="))
case=int(input("line2.c="))
fries=int(input("line3.f="))
home=int(input("line4.h="))
ans_1=book+case
ans_2=fries-home
ans_3=book*home
ans_4=case%fries
ans_5=home//fries
print(ans_1)
print(ans_2)
print(ans_3)
print(ans_4)
print(ans_5)
print(ans_4**2)
vain=book!=case
print(vain)
magic=ans_1<=ans_2
print(magic)
price=ans_2<ans_5
print(price)
print(ans_1>=ans_2)
go=ans_4>ans_5
stay=ans_3==ans_2
print(go and stay)
print(go or stay)
print(not vain)
print(not go)
print(not stay)
print(not magic)
print(not price)