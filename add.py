#adding 2 large number
tinh = input('Nhap vao phep tinh tong: ')

## Check input
#isdigit()

## Get a, b
for i in range(len(tinh)-1, 0, -1):
    if tinh[i] == '+':
        a = tinh[0:i]
        b = tinh[i+1:len(tinh)]
        break

##check decimal number
def check_decimal(n):
    for i in range(len(n)):
        if n[i] == '.':
            check = True
            break
        else:
            check = False
    return check

#Xu ly vi tri thap phan va do dai chuoi
def edit_num(n,m):

    #Them so 0 truoc dau phay
    if n.find('.') > m.find('.'):
        b1 = '0'*(n.find('.') - m.find('.')) + m
        a1 = n
    else:
        a1 = '0'*(m.find('.') - n.find('.')) + n
        b1 = m 

    #Them so 0 sau dau phay
    if len(a1) > len(b1):
        b1 = b1 + '0'*(len(a1)-len(b1))
    else:
        a1 = a1 + '0'*(len(b1)-len(a1))
    return a1,b1

#TH a,b la so thap phan
if check_decimal(a) & check_decimal(b) == True:
    a1,b1 = edit_num(a,b)
#TH a la so nguyen
elif check_decimal(a) == False:
    if check_decimal(b) == True:
        a1 = a + '.'
        a1,b1 = edit_num(a1,b)
    else:
        b1 = b + '.'
        a1 = a +'.'
        a1,b1 = edit_num(a1,b1)
#TH b la so nguyen
else:
    b1 = b + '.'
    a1,b1 = edit_num(a,b1)

kq = ''
du = 0
#Tinh tong hai so
for i in range (len(a1)-1,-1,-1):
    if a1[i] == '.':
        kq = '.' + kq
        continue
    else:
        tam = int(a1[i]) + int(b1[i]) + du
        if tam > 9:
            tam = tam % 10
            du = 1
        else:
            du = 0
        kq = str(tam) + kq   
if du == 1:
    kq = '1' + kq

#xóa số 0 bên phải
def xuly0phai(m):
    if m.find('.') != -1:
        for i in range (len(m) - 1, m.find('.') - 1, -1):
            if m[i] != '0':
                kq = m[:i+1]
                break
            elif m[i] == '0':
                kq = m[:i]
    else:
        kq = m
    if kq[len(kq)-1] == '.':
        kq = kq[:len(kq)-1]
    return kq

#Xóa số 0 bên trái
def xuly0trai(m):
    m = m[::-1]
    if m[len(m)-1] == '-':
        dau = '-'
        m = m[:len(m)-1]
    else:
        dau = ''
        m = m

    if m.find('.') != -1:
        for i in range (len(m) - 1, m.find('.') - 1, -1):
            if m[i] != '0':
                kq = m[:i+1]
                break
            elif m[i] == '0':
                kq = m[:i]
        if kq[len(kq)-1] == '.':
            kq = kq + '0'
    else:
        for i in range (len(m) - 1, m.find('.') - 1, -1):
            if m[i] != '0':
                kq = m[:i+1]
                break
            elif m[i] == '0':
                kq = m[:i]
    kq = dau + kq[::-1]
    return kq

kq = xuly0phai(kq)
kq = xuly0trai(kq)
print('Ket qua cua pheo tinh ' + tinh + ' = ',kq)