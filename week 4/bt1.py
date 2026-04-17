class NhanVien:
    def __init__(self, ten, ma_nv, luongCoBan, heSoLuong):
        self.__ten = ten
        self.__ma_nv = ma_nv
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong
    @property
    def ma_nv(self):
        return self.__ma_nv
    @ma_nv.setter
    def ma_nv(self, value):
        self.__ma_nv = value
    @property
    def ten(self):
        return self.__ten
    @ten.setter
    def ten(self, value):
        if value.strip():
            self.__ten = value
        else:
            print("Tên không được trống!")
    @property
    def luongCoBan(self):
        return self.__luongCoBan
    @luongCoBan.setter
    def luongCoBan(self, value):
        if value <= 0:
            print("Lương phải là số dương!!")
        else:
            self.__luongCoBan = value
    @property
    def heSoLuong(self):
        return self.__heSoLuong
    @heSoLuong.setter
    def heSoLuong(self, value):
        if value < 0:
            print("Hệ số lương phải là số dương")
        else:
            self.__heSoLuong = value
    
    #METHODS : 
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong
    def tangLuong(self, ti_le_tang):
        if ti_le_tang > 0:
            self.__heSoLuong += ti_le_tang
            print(f"đã tăng hệ số lương mới cho nhân viên {self.__ten}")
            print(f"hệ số lương mới là {self.__heSoLuong}")
        else:
            print("hệ số lương phải dương!")
    def in_thông_tin(self):
        print(f"Họ & tên nhân viên là: {self.__ten}")
        print(f"Mã nhân viên là : {self.__ma_nv}")
        print(f"Lương cơ bản của nhân viên là: {self.__luongCoBan}")
        print(f"Hệ số lương của nhân viên là : {self.__heSoLuong}")
        print(f"Tổng lương của nhân viên: {self.tinhLuong}")
    #KHỞI TẠO ĐỐI TƯỢNG
if __name__ == "__main__":
    nv1 =NhanVien("NGUYỄN MINH TRÂM", 25112199, 3000, 2.5)
    print("Thông tin của nhân viên")
    nv1.in_thông_tin()
    
                
            
