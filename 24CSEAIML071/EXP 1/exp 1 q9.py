#write a program to input your markes for 2 subject with & without useing the 3rd variable?
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
print(f"Before swap: Sub1={sub1}, Sub2={sub2}")

temp = sub1
sub1 = sub2
sub2 = temp

print(f"After swap: Sub1={sub1}, Sub2={sub2}")
 
#without

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
print(f"Before swap: Sub1={sub1}, Sub2={sub2}")

sub1, sub2 = sub2, sub1

print(f"After swap: Sub1={sub1}, Sub2={sub2}")
