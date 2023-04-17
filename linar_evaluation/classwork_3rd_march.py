given_i=int(input("what is i? "))
given_f=int(input("what is f?"))
given_n=int(input("what is n?"))
given_s=int(input("what is s?"))
given_w=int(input("what is w?"))
rbn=20/given_f#round bracket numerator
rbnwp=rbn**given_w #round  bracket numerator with power
sqbn=given_s*given_i #square bracket numerator
sqbnwd=sqbn/given_f #
pn=sqbnwd+rbnwp
fpn=given_f**given_n
spn=fpn*pn
spd=20**given_n
rs=spn/spd
solve=given_i-rs
print("The value for y is " + str(solve))

#given_i = ' 6'
