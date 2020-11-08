# phep nhan 2 so
tinh = input('Nhap vao phep tinh nhan:')
## Check input
#isdigit()

# Kết quả âm dương, bỏ dấu:
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

#Dấu và chuỗi không dấu
dau, nhap = kt_dau(tinh)

## Get a, b
a = nhap[:nhap.find('*')]
b = nhap[nhap.find('*')+1:]

## Bỏ dấu .
a1, b1, vt = vttp(a,b)

ket = phepnhan(a1,b1)[::-1]

#Xử lý kết quả
ket = ket[:vt] + '.'+ ket[vt:]
ket = ket[::-1]
if dau == 1:
    ket = ket
else:
    ket = '-' + ket

kq = ket
## Xoa so 0 phia truoc '.'
k = 0
for i in range(0, kq.find('.') + 1, 1):
    if kq[i] == '-':
        continue
    elif kq[i] == '0':
        if kq[i+1] == '0':
            k = i+1
        elif kq[i+1] == '.':
            k = i-1
        else:
            break
    else:
        break
if kq[0] == '-':
    kq = kq[0]+kq[k+1:]
else:
    kq = kq
#Xoa so 0 phia sau '.'
for i in range(len(kq)-1, kq.find('.') - 1, -1):
    if kq[i] == '.':
        kq = kq[0:i]
        break
    elif kq[i] == '0':
        kq = kq[0:i]
    else:
        kq = kq[:i+1]
        break

print('Ket qua phep nhan',tinh,'la:', kq)