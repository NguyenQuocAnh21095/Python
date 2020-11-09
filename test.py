import os

def tach_so(m, sign):
    return m.split(sign)


def kiem_tra_thap_phan(m):
    if "." in m:
        return True
    else:
        return False

def standard_num(m):
    if not kiem_tra_thap_phan(m):
        return m + "."
    else:
        return m

def sua_so(m,n):

    so_m = standard_num(m)
    so_n = standard_num(n)

    so_m = tach_so(so_m,".")
    so_n = tach_so(so_n,".")

    dif_nguyen = len(so_m[0]) - len(so_n[0])
    dif_thap = len(so_m[1]) - len(so_n[1])

    if dif_nguyen > 0:
        so_n[0] = "0"*dif_nguyen + so_n[0]
    elif dif_nguyen < 0:
        so_m[0] = "0"*abs(dif_nguyen) + so_m[0]

    if dif_thap > 0:
        so_n[1] = so_n[1] + "0"*dif_thap
    elif dif_thap < 0:
        so_m[1] = so_m[1] + "0"*abs(dif_thap)

    return so_m[0]+"."+so_m[1], so_n[0]+"."+so_n[1]

if __name__ == "__main__":
    m = "12.33+456" #012.33+456.80
    numbers = tach_so(m, "+")
    # for num in numbers:
    #     print(kiem_tra_thap_phan(num))

    a, b = sua_so(numbers[0], numbers[1])
    print(a,b)