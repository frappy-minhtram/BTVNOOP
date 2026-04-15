class NhanVien:
    LUONG_MAX = 50000000 

    def __init__(self, ma_nv, ho_ten, luong_cb, he_so):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.he_so = he_so

    @property
    def ma_nv(self):
        return self.__ma_nv

    @ma_nv.setter
    def ma_nv(self, value):
        if not value or value.strip() == "":
            raise ValueError("Lỗi: Mã nhân viên không được để trống!")
        self.__ma_nv = value

    @property
    def luong_cb(self):
        return self.__luong_cb

    @luong_cb.setter
    def luong_cb(self, value):
        if value < 0:
            raise ValueError("Lỗi: Lương cơ bản không được âm!")
        self.__luong_cb = value

    @property
    def ho_ten(self): return self.__ho_ten

    @ho_ten.setter
    def ho_ten(self, value): self.__ho_ten = value

    @property
    def he_so(self): return self.__he_so

    @he_so.setter
    def he_so(self, value):
        if value <= 0: raise ValueError("Lỗi: Hệ số lương phải > 0")
        self.__he_so = value

    def tinh_luong(self):
        """Công thức chuẩn theo yêu cầu đề bài."""
        return self.luong_cb * self.he_so

    def tang_luong(self, delta):
        """Kiểm tra ngưỡng LUONG_MAX trước khi tăng."""
        luong_du_kien = (self.luong_cb + delta) * self.he_so
        if luong_du_kien > self.LUONG_MAX:
            print(f"!!! Không thể tăng: Lương dự kiến ({luong_du_kien:,.0f}) vượt ngưỡng cho phép.")
            return False
        else:
            self.luong_cb += delta
            print(f"--- Tăng lương thành công cho {self.ho_ten} ---")
            return True

    def in_ttin(self):
        """Hiển thị thông tin chuyên nghiệp."""
        print(f"[{self.ma_nv}] - {self.ho_ten}")
        print(f" + Lương CB: {self.luong_cb:,.0f} | Hệ số: {self.he_so}")
        print(f" + Tổng nhận: {self.tinh_luong():,.0f} VNĐ")

if __name__ == "__main__":
    print("--- QUẢN LÝ NHÂN VIÊN (A+ Version) ---")
    try:
        m = input("Nhập mã NV: ")
        t = input("Nhập họ tên: ")
        l = float(input("Nhập lương cơ bản: "))
        h = float(input("Nhập hệ số lương: "))
      
        nv = NhanVien(m, t, l, h)
        nv.in_ttin()
      
        bonus = float(input("\nNhập số tiền muốn tăng thêm vào lương CB: "))
        nv.tang_luong(bonus)
        nv.in_ttin()

    except ValueError as e:
        print(f"Dữ liệu nhập sai: {e}")
    except Exception as e:
        print(f"Có lỗi hệ thống: {e}")
