import tkinter # thư viện tạo cửa sổ main window
from tkinter import messagebox as msgbox
from PIL import Image, ImageDraw, ImageTk
from functools import partial
import sys
# điều chỉnh cấu hình giao diện của trò chơi 
FONT = "Arial"
kichthuoccuafont = 14
PADX_VALUE = 30
# thêm hai biến để tiến hành mở rộng chương trình lên 8x8
# thứ 1: kích thước bàn cờ 8x8
kichthuocbanco = 8
# thứ 2: số lượng ô đánh liên tiếp để dành chiến thắng - 5
SO_LUONG_THANG = 5

class Game(tkinter.Tk):
    # phương thức chính
    # bắt đầu tạo cửa sổ chính , giao diện gồm khung(frame) game chính và khung điểm số
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Game XO 8x8 với AI")
        self.diem = {"Máy": 0, "Người chơi": 0, "Hoà": 0}

        self.khungGame = tkinter.Frame(self)
        self.khungGame.grid(row=0, column=0)

        self.khungDiem = tkinter.Frame(self)
        self.khungDiem.grid(row=1, column=0)
        #  label nhãn người chơi, máy, hoà
        self.labelDiemMay = tkinter.Label(self.khungDiem, text=f"Máy:{self.diem['Máy']}", font=(FONT, kichthuoccuafont))
        self.labelDiemMay.grid(row=0, column=0, padx=PADX_VALUE)

        self.labelDiemNguoi = tkinter.Label(self.khungDiem, text=f"Người chơi:{self.diem['Người chơi']}", font=(FONT, kichthuoccuafont))
        self.labelDiemNguoi.grid(row=0, column=1, padx=PADX_VALUE)

        self.labelDiemHoa = tkinter.Label(self.khungDiem, text=f"Hoà:{self.diem['Hoà']}", font=(FONT, kichthuoccuafont))
        self.labelDiemHoa.grid(row=0, column=2, padx=PADX_VALUE)

        # tạo bàn cờ 8x8 là 64 phần tử
        self.banCo = [" " for _ in range(kichthuocbanco * kichthuocbanco)]
        # tạo hình ảnh cho hai quân x( người chơi) và quân o của máy
        self.hinhAnh = {
            "X": self.quanX("white"),
            "O": self.quanO("white"),
            "X-winner": self.quanX("green"),
            "O-winner": self.quanO("green"),
            "plain": self.Trang()
        }
        # quản lý nút bấm
        self.oCo = dict()
        for i in range(kichthuocbanco * kichthuocbanco):
            r, c = divmod(i, kichthuocbanco)
            nut = {
                "id": i,
                "Button": tkinter.Button(
                    self.khungGame, image=self.hinhAnh["plain"],
                    disabledforeground="white", command=partial(self.xuLyClick, i)
                )
            }
            nut["Button"].grid(row=r, column=c, sticky="NWSE")
            self.oCo[i] = nut

    def quanX(self, mau):
        new = Image.new("RGB", (60, 60), mau)
        shape = ImageDraw.Draw(new)
        shape.line([(10, 10), (50, 50)], fill="black", width=4)
        shape.line([(10, 50), (50, 10)], fill="black", width=4)
        return ImageTk.PhotoImage(new)

    def quanO(self, mau):
        new = Image.new("RGB", (60, 60), mau)
        shape = ImageDraw.Draw(new)
        shape.ellipse([10, 10, 50, 50], outline="black", width=4)
        return ImageTk.PhotoImage(new)

    def Trang(self):
        return ImageTk.PhotoImage(Image.new("RGB", (60, 60), (255, 255, 255)))
    
    # hàm xử lý khi người chơi nhấn vào ô cờ
    def xuLyClick(self, viTri):
        if self.banCo[viTri] != " ": 
            return
        self.diChuyen(viTri, "X")
        if self.kiemTraKetThuc():
            return
        nuocMay = self.mayDiChuyen()
        if nuocMay is not None:
            self.diChuyen(nuocMay, "O")
            self.kiemTraKetThuc()

    def diChuyen(self, viTri, nguoi):
        self.banCo[viTri] = nguoi
        self.oCo[viTri]["Button"].config(image=self.hinhAnh[nguoi])
        
    # hàm máy ai chọn bước đi - sử dụng minimax và cắt tỉa alpha-Beta
    def mayDiChuyen(self):
        diemTotNhat = -float("inf")
        nuocTotNhat = None
        for i in range(len(self.banCo)):
            if self.banCo[i] == " ":
                self.banCo[i] = "O"
                diem = self.minimax(self.banCo, 1, False, -float("inf"), float("inf"))
                self.banCo[i] = " "
                if diem > diemTotNhat:
                    diemTotNhat = diem
                    nuocTotNhat = i
        return nuocTotNhat
        
    # hàm minimax và alpha-beta Pruning - tìm nước đi tối ưu
    def minimax(self, banCo, doSau, laMax, alpha, beta):
        nguoiThang, _ = self.kiemTraNguoiThang(banCo)
        if nguoiThang == "O":
            return 100000
        elif nguoiThang == "X":
            return -100000
        elif " " not in banCo or doSau == 0:
            return self.danhGiaBanCo(banCo)

        if laMax:
            max_diem = -float("inf")
            for i in range(len(banCo)):
                if banCo[i] == " ":
                    banCo[i] = "O"
                    diem = self.minimax(banCo, doSau - 1, False, alpha, beta)
                    banCo[i] = " "
                    max_diem = max(max_diem, diem)
                    alpha = max(alpha, diem)
                    if beta <= alpha:
                        break
            return max_diem
        else:
            min_diem = float("inf")
            for i in range(len(banCo)):
                if banCo[i] == " ":
                    banCo[i] = "X"
                    diem = self.minimax(banCo, doSau - 1, True, alpha, beta)
                    banCo[i] = " "
                    min_diem = min(min_diem, diem)
                    beta = min(beta, diem)
                    if beta <= alpha:
                        break
            return min_diem
            
    # hàm đánh giá bàn cờ- đánh giá điểm số của bàn cờ hiện tại
    def danhGiaBanCo(self, banCo):
        def diemDong(dong):
            so_o = dong.count("O")
            so_x = dong.count("X")
            if so_o > 0 and so_x == 0:
                return 10 ** so_o
            elif so_x > 0 and so_o == 0:
                return -10 ** so_x
            return 0

        tong_diem = 0
        for dong in self.generate_TatCaDong():
            gia_tri = [banCo[i] for i in dong]
            tong_diem += diemDong(gia_tri)
        return tong_diem
        
    def generate_TatCaDong(self):
        dong = []
        for r in range(kichthuocbanco):
            for c in range(kichthuocbanco - SO_LUONG_THANG + 1):
                dong.append([r * kichthuocbanco + c + i for i in range(SO_LUONG_THANG)])
        for c in range(kichthuocbanco):
            for r in range(kichthuocbanco - SO_LUONG_THANG + 1):
                dong.append([(r + i) * kichthuocbanco + c for i in range(SO_LUONG_THANG)])
        for r in range(kichthuocbanco - SO_LUONG_THANG + 1):
            for c in range(kichthuocbanco - SO_LUONG_THANG + 1):
                dong.append([(r + i) * kichthuocbanco + c + i for i in range(SO_LUONG_THANG)])
        for r in range(SO_LUONG_THANG - 1, kichthuocbanco):
            for c in range(kichthuocbanco - SO_LUONG_THANG + 1):
                dong.append([(r - i) * kichthuocbanco + c + i for i in range(SO_LUONG_THANG)])
        return dong
        
    # hàm này kiểm tra xem có người thắng cuộc không
    def kiemTraNguoiThang(self, banCo):
        for dong in self.generate_TatCaDong():
            gia_tri = [banCo[i] for i in dong]
            if gia_tri.count(gia_tri[0]) == SO_LUONG_THANG and gia_tri[0] != " ":
                return gia_tri[0], dong
        return None, None

    def kiemTraKetThuc(self):
        nguoiThang, dongThang = self.kiemTraNguoiThang(self.banCo)
        if nguoiThang:
            for i in dongThang:
                self.oCo[i]["Button"].config(image=self.hinhAnh[f"{nguoiThang}-winner"])
            self.capNhatDiem("Người chơi" if nguoiThang == "X" else "Máy")
            self.ketThucTroChoi(nguoiThang)
            return True
        elif " " not in self.banCo:
            self.capNhatDiem("Hoà")
            self.ketThucTroChoi("Hoà")
            return True
        return False

    def capNhatDiem(self, ketQua):
        self.diem[ketQua] += 1
        self.labelDiemNguoi["text"] = f"Người chơi:{self.diem['Người chơi']}"
        self.labelDiemMay["text"] = f"Máy:{self.diem['Máy']}"
        self.labelDiemHoa["text"] = f"Hoà:{self.diem['Hoà']}"

    def ketThucTroChoi(self, ketQua):
        thongBao = {
            "X": "Bạn đã thắng! Chơi lại?",
            "O": "Bạn đã thua! Chơi lại?",
            "Hoà": "Hòa! Chơi lại?"
        }[ketQua]
        if msgbox.askyesno("Kết thúc trò chơi", thongBao):
            self.lamMoiBanCo()
        else:
            sys.exit()

    def lamMoiBanCo(self):
        for i in range(kichthuocbanco * kichthuocbanco):
            self.banCo[i] = " "
            self.oCo[i]["Button"].config(image=self.hinhAnh["plain"])

if __name__ == "__main__":
    Game().mainloop()