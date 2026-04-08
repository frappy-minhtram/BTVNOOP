class BANK_ACC:
    def __init__(self, stk, ten, so_du):
        self.stk = stk
        self.ten = ten
        self.so_du = so_du
    def nap_tien(self, so_tien):
        if (so_tien <= 0):
            print("VUI LONG NHAP LAI SO TIEN MUON NAP")
        else :
            print("NAP TIEN THANH CONG")
        return so_tien + self.so_du  # đoạn này kbt code sao 
    def rut_tien(self,so_tien):
        if so_tien <= 0:
         print("So tien khong hop le")
        elif so_tien > self.so_du:
         print("Khong du tien")
        else:
         self.so_du -= so_tien
        print("Rut tien thanh cong")
    def chuyen_tien(self, so_tien, tai_khoan_nhan):
        if so_tien <= 0:
         print("So tien khong hop le")
        elif so_tien > self.so_du:
         print("Khong du tien")
        else:
         self.rut_tien(so_tien)
         tai_khoan_nhan.nap_tien(so_tien)
    def hien_thi(self):
        print("So TK:", self.stk)
        print("Ten:", self.ten)
        print("So du:", self.so_du)
tk01 = BANK_ACC(22334455, "NGUYỄN MINH TRÂM",5000 )
tk02 = BANK_ACC(11223344, "NGUYỄN MINH TRANG",1000)
tk01.nap_tien(3000)
tk01.rut_tien(1000)
tk01.chuyen_tien(200,tk02)
tk01.hien_thi()
tk02.hien_thi()
