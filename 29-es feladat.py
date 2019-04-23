#Tekintsük a következő egész számokból álló ai sorozatot: a1 = 1 és minden i >= 2 esetén
#ai egyenlő az aj (j < i) elemek számjegyeinek összegével. Pl.: 1, 1, 2, 4, 8, 16, 23, 28,
#38, … . Írjon programot, amely meghatározza az n-dik indexű elemet. Az n index értékét a standard bementről olvassa be!
try:
    n=int(input("Adj meg egy számot:"))
    j=1
    s=1
    while s<n-1:
        def digit_sum(j):
            num_str = str(j)
            sum = 0
            for i in range(0, len(num_str)):
                sum += int(num_str[i])
            return sum
        j=j+digit_sum(j)
        s+=1
    print(j)
except ValueError:
    print("Hibás az input, kérlek adj meg egy egész számot")