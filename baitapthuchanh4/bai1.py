

class sinhvien:
    def __init__(self, hoten, namsinh):
        self.hoten = hoten
        self.namsinh = namsinh

    def tinhtuoi(self):
        return 2023 - self.namsinh


class SVDHCN(sinhvien):
    def __init__(self, hoten, namsinh, toan, van, nn):
        super().__init__(hoten, namsinh)
        self.toan = toan
        self.van = van
        self.nn = nn

    def tongdiem(self):
        return self.toan + self.van + self.nn


sv = []
print("Nhập vào phần tử của SVDHCN:", end=" ")
n = int(input())
while n <= 0:
    print("Nhập vào phần tử của SVDHCN:", end=" ")
    n = int(input())

for i in range(n):
    print("Nhập vào họ tên: ", end=" ")
    hoten = input()
    print("Nhập vào năm sinh: ", end=" ")
    namsinh = int(input())
    print("Nhập vào điểm toán: ", end=" ")
    toan = float(input())
    print("Nhập vào điểm văn: ", end=" ")
    van = float(input())
    print("Nhập vào điểm ngoại ngữ: ", end=" ")
    nn = float(input())

    ob = SVDHCN(hoten, namsinh, toan, van, nn)
    sv.append(ob)

print("Hiển thị danh sách sinh viên vừa nhập")    
print("{:<20}{:<20}{:<10}{:<10}{:<10}{:<20}".format("Họ tên", "Năm sinh", "Toán", "Văn", "Ngoại ngữ", "Tổng điểm"))

for i in range(n):
    print("{:<20}{:<20}{:<10}{:<10}{:<10}{:<20}".format(sv[i].hoten, sv[i].namsinh, sv[i].toan, sv[i].van, sv[i].nn, sv[i].tongdiem()))
