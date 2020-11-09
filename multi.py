# phep nhan 2 so
tinh = input('Nhap vao phep tinh nhan: ')
## Check input
#isdigit()

# Kiểm tra kết quả âm dương, loại bỏ dấu:
def kt_dau(m):
    k = m.count('-')
    if k == 0 or k == 2:
        kq = 1
    else:
        kq = -1
    
    string = m.replace('-','')
    return kq,string


# Vi tri thap phan, loai bo dau thap phan
def vttp(m,n):
    m = m[::-1]
    n = n[::-1]
    if m.find('.') != -1 and n.find('.') != -1:
        vt = m.find('.') + n.find('.')
    elif m.find('.') != -1 and n.find('.') == -1:
        vt = m.find('.')
    elif m.find('.') == -1 and n.find('.') != -1:
        vt = n.find('.')
    elif m.find('.') == -1 and n.find('.') == -1:
        vt = 0
       
    m = m.replace('.','')
    n = n.replace('.','')
    m = m[::-1]
    n = n[::-1]
    return m,n,vt

#print(vttp('123.13','0.1321'))

#Multiply 1 digit by more digits
def nhan(m,n):
    kq = ''
    du = 0
    for i in range (len(m)-1, -1, -1):
        tam = int(n) * int(m[i]) + du
        if tam > 9:
            kq = str(tam % 10) + kq
            du = tam // 10
        else:
            kq = str(tam) + kq
            du = 0
    if du != 0:
        kq = str(du) + kq
    return kq

#print('kq nhan',nhan('52','8'))

#Plus 2 numbers have same length
def cong(m,n):
    du = 0
    kq = ''
    for i in range(len(n)-1, -1, -1):
        tam = int(m[i]) + int(n[i]) + du
        if tam > 9:
            kq = str(tam % 10) + kq
            du = 1
        else:
            kq = str(tam) + kq
            du = 0
    if du != 0:
        kq = str(du) + kq
    return kq

#print('kq cong:',cong('3','4'))


def phepnhan(m,n):
    kq = '0'*len(m)
    k = 0
    for i in range(len(n)-1, -1, -1):
        tam = nhan(m,n[i])
        tam = tam + '0'*k
        kq = '0'*(len(tam) - len(kq)) + kq
        kq = cong(kq,tam)
        k = k + 1
    return kq

#print(phepnhan('012','4569'))

#Kiểm tra dấu và chuỗi đã loại bỏ dấu
dau, nhap = kt_dau(tinh)

## Get a, b
a = nhap[:nhap.find('*')]
b = nhap[nhap.find('*')+1:]

## Bỏ dấu thập phân
a1, b1, vt = vttp(a,b)

#Kết quả phép nhân không dấu thập phân
ket = phepnhan(a1,b1)[::-1]

#Đưa dấu thập phân vào kết quả
ket = ket[:vt] + '.'+ ket[vt:]
ket = ket[::-1]
if dau == 1:
    ket = ket
else:
    ket = '-' + ket

kq = ket

#Xóa số 0 bên phải
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

# print('xu ly so 0:',xuly0phai('231'))
# print('xu ly so 0:',xuly0trai('-10.0'))
kq = xuly0phai(kq)
kq = xuly0trai(kq)
print('Ket qua phep nhan',tinh,'la:', kq)