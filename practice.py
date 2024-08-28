number = float(input("enter a number w/ a decimal"))
mod = number%100
mods = mod%10
modss = mods%1
float_to_str = str(modss)
decimal_find = float_to_str.find(".")
length_of_decimal = len(float_to_str)
cut = float_to_str[decimal_find+1:3]
cuts = int(cut)
fin = "The first decimal digit is {}"
print(fin.format(cuts))