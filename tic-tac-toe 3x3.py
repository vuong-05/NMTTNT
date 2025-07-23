import tkinter
from tkinter import messagebox as msgbox
from PIL import Image, ImageDraw, ImageTk
from functools import partial
import sys

FONT = "Arial"
kich_thuoc_font = 18
PADX_VALUE = 30

class TroChoi(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Game XO (tic-tac-toe) 3x3")

        self.diem = {"Máy":0, "Người chơi":0, "Hoà":0}

        self.khungBanCo = tkinter.Frame(self)
        self.khungBanCo.grid(row=0, column=0)

        self.khungDiem = tkinter.Frame(self)
        self.khungDiem.grid(row=1, column=0)

        self.nhanDiemMay = tkinter.Label(self.khungDiem, text=f"Máy:{self.diem['Máy']}", font=(FONT, kich_thuoc_font))
        self.nhanDiemMay.grid(row=0, column=0, padx=PADX_VALUE)

        self.nhanDiemNguoi = tkinter.Label(self.khungDiem, text=f"Người chơi:{self.diem['Người chơi']}", font=(FONT, kich_thuoc_font))
        self.nhanDiemNguoi.grid(row=0, column=1, padx=PADX_VALUE)

        self.nhanDiemHoa = tkinter.Label(self.khungDiem, text=f"Hoà:{self.diem['Hoà']}", font=(FONT, kich_thuoc_font))
        self.nhanDiemHoa.grid(row=0, column=2, padx=PADX_VALUE)

        self.banCo = [" " for _ in range(9)]

        self.hinhAnh = {
            "X": self.veX("white"),
            "O": self.veO("white"),
            "X-winner": self.veX("lightgreen"),
            "O-winner": self.veO("lightgreen"),
            "plain": self.veTrang()
        }

        self.oCo = dict()
        for i in range(9):
            o = {
                "id": i,
                "Button": tkinter.Button(self.khungBanCo, image=self.hinhAnh["plain"], disabledforeground="white", command=partial(self.xuLyClick, i))
            }
            r, c = divmod(i, 3)
            o["Button"].grid(row=r, column=c, sticky="NWSE")
            self.oCo[i] = o

    def veX(self, mau):
        new = Image.new("RGB", (150, 150), mau)
        shape = ImageDraw.Draw(new)
        shape.line([(30,30), (120,120)], fill="black", width=6)
        shape.line([(30,120), (120,30)], fill="black", width=6)
        return ImageTk.PhotoImage(new)

    def veO(self, mau):
        new = Image.new("RGB", (150, 150), mau)
        shape = ImageDraw.Draw(new)
        shape.ellipse([30, 30, 120, 120], outline="black", width=6)
        return ImageTk.PhotoImage(new)

    def veTrang(self):
        new = Image.new("RGB", (150, 150), (255, 255, 255))
        return ImageTk.PhotoImage(new)

    def capNhatDiem(self, ketQua):
        if ketQua == "Người chơi":
            self.diem["Người chơi"] += 1
            self.nhanDiemNguoi["text"] = f"Người chơi:{self.diem['Người chơi']}"
        elif ketQua == "Máy":
            self.diem["Máy"] += 1
            self.nhanDiemMay["text"] = f"Máy:{self.diem['Máy']}"
        elif ketQua == "Hoà":
            self.diem["Hoà"] += 1
            self.nhanDiemHoa["text"] = f"Hoà:{self.diem['Hoà']}"
        else:
            raise ValueError("Giá trị không hợp lệ")

    def xuLyClick(self, viTri):
        if self.banCo[viTri] != " ":
            return
        self.diChuyen(viTri, "X")
        
        # Kiểm tra xem trò chơi đã kết thúc sau nước đi của người chơi chưa
        ketQua = self.kiemTraThang(self.banCo)
        if ketQua or " " not in self.banCo:
            self.kiemTraKetThuc()
            return
            
        nuocDiMay = self.mayDiChuyen()
        if nuocDiMay != -1:
            self.diChuyen(nuocDiMay, "O")

    def diChuyen(self, viTri, nguoiChoi):
        self.oCo[viTri]["Button"].config(image=self.hinhAnh[nguoiChoi])
        self.banCo[viTri] = nguoiChoi
        self.kiemTraKetThuc()

    def mayDiChuyen(self):
        # Kiểm tra nếu không còn nước đi
        if not self.conNuocDi(self.banCo):
            return -1
            
        diemTotNhat = float("-inf")
        nuocTotNhat = -1

        for i in self.danhSachNuocDi(self.banCo):
            self.banCo[i] = "O"
            diem = self.minimaxMay(self.banCo, False)
            self.banCo[i] = " "
            if diem > diemTotNhat:
                diemTotNhat = diem
                nuocTotNhat = i
        return nuocTotNhat

    def minimaxMay(self, banCo, laMax):
        diem = self.danhGiaBanCo(banCo)
        if diem in [1, -1]:
            return diem
        if not self.conNuocDi(banCo):
            return 0

        if laMax:
            totNhat = float("-inf")
            for i in self.danhSachNuocDi(banCo):
                banCo[i] = "O"
                totNhat = max(totNhat, self.minimaxMay(banCo, False))
                banCo[i] = " "
            return totNhat
        else:
            totNhat = float("inf")
            for i in self.danhSachNuocDi(banCo):
                banCo[i] = "X"
                totNhat = min(totNhat, self.minimaxMay(banCo, True))
                banCo[i] = " "
            return totNhat

    def danhGiaBanCo(self, banCo):
        ketQua = self.kiemTraThang(banCo)
        if ketQua == "X":
            return -1
        elif ketQua == "O":
            return 1
        return 0

    def kiemTraThang(self, banCo):
        # Kiểm tra hàng ngang
        for i in range(0, 9, 3):
            if self.isSame(banCo[i], banCo[i+1], banCo[i+2]):
                return banCo[i]
        # Kiểm tra hàng dọc
        for i in range(3):
            if self.isSame(banCo[i], banCo[i+3], banCo[i+6]):
                return banCo[i]
        # Kiểm tra đường chéo
        if self.isSame(banCo[0], banCo[4], banCo[8]):
            return banCo[0]
        if self.isSame(banCo[2], banCo[4], banCo[6]):
            return banCo[2]
        return False

    def conNuocDi(self, banCo):
        return any(viTri == " " for viTri in banCo)

    def danhSachNuocDi(self, banCo):
        return [i for i, o in enumerate(banCo) if o == " "]

    def kiemTraKetThuc(self):
        ketQua = self.kiemTraThang(self.banCo)

        if ketQua:
            # Tô màu các ô thắng
            self.toMauChoViTriThang(ketQua)
            
            if ketQua == "X":
                self.capNhatDiem("Người chơi")
            else:
                self.capNhatDiem("Máy")
            self.ketThuc(ketQua)
        elif " " not in self.banCo:
            self.capNhatDiem("Hoà")
            self.ketThuc("Hoà")

    def isSame(self, a, b, c):
        return a == b == c and a != " "

    def toMauChoViTriThang(self, nguoiThang):
        # Tô màu cho ô thắng
        # Kiểm tra hàng ngang
        for i in range(0, 9, 3):
            if self.isSame(self.banCo[i], self.banCo[i+1], self.banCo[i+2]) and self.banCo[i] == nguoiThang:
                self.toMauThang(i, i+1, i+2)
                return
        # Kiểm tra hàng dọc
        for i in range(3):
            if self.isSame(self.banCo[i], self.banCo[i+3], self.banCo[i+6]) and self.banCo[i] == nguoiThang:
                self.toMauThang(i, i+3, i+6)
                return
        # Kiểm tra đường chéo
        if self.isSame(self.banCo[0], self.banCo[4], self.banCo[8]) and self.banCo[0] == nguoiThang:
            self.toMauThang(0, 4, 8)
            return
        if self.isSame(self.banCo[2], self.banCo[4], self.banCo[6]) and self.banCo[2] == nguoiThang:
            self.toMauThang(2, 4, 6)
            return

    def toMauThang(self, a, b, c):
        self.oCo[a]["Button"].config(image=self.hinhAnh[f"{self.banCo[a]}-winner"])
        self.oCo[b]["Button"].config(image=self.hinhAnh[f"{self.banCo[b]}-winner"])
        self.oCo[c]["Button"].config(image=self.hinhAnh[f"{self.banCo[c]}-winner"])

    def ketThuc(self, ketQua):
        if self.hoiChoiLai(ketQua):
            self.lamMoi()
        else:
            sys.exit()

    def hoiChoiLai(self, ketQua):
        if ketQua == "X":
            msg = "Bạn đã thắng! Chơi lại?"
        elif ketQua == "O":
            msg = "Bạn đã thua! Chơi lại?"
        else:
            msg = "Hoà! Chơi lại?"
        return msgbox.askyesno("Kết thúc trò chơi", msg)

    def lamMoi(self):
        for i in range(9):
            self.oCo[i]["Button"].config(image=self.hinhAnh["plain"])
        self.banCo = [" " for _ in range(9)]

if __name__ == "__main__":
    choi = TroChoi()
    choi.mainloop()