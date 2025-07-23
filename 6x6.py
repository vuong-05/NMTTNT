import tkinter
from tkinter import messagebox as msgbox
from PIL import Image, ImageDraw, ImageTk
from functools import partial
from random import choice, randint
import sys

FONT = "Arial"
FONT_SIZE = 16
PADX_VALUE = 25
BOARD_SIZE = 6
WIN_CONDITION = 4  
TILE_SIZE = 70

class TicTacToe6x6(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Game XO 6x6 - Can 4 o lien tiep de thang")
        
        self.score = {"May": 0, "Nguoi choi": 0, "Hoa": 0}
        self.game_active = True
        
        self.setupui()
        self.khoitao()

    def setupui(self):
        #giao dien
        info_frame = tkinter.Frame(self)
        info_frame.grid(row=0, column=0, pady=10)
        
        info_label = tkinter.Label(info_frame, 
                                  text="Game XO 6x6 - Can 4 o lien tiep de thang!", 
                                  font=(FONT, FONT_SIZE), fg="darkblue", bg="lightyellow")
        info_label.pack(pady=5)
        
        new_game_btn = tkinter.Button(info_frame, text="Game Moi", 
                                     command=self.gamemoi, font=(FONT, 12, "bold"),
                                     bg="orange", fg="white", relief="raised", bd=3,
                                     activebackground="darkorange", activeforeground="white")
        new_game_btn.pack(pady=5)

        self.game_frame = tkinter.Frame(self, bg="darkgray", relief="sunken", bd=3)
        self.game_frame.grid(row=1, column=0, padx=10, pady=10)
        
        score_frame = tkinter.Frame(self, bg="lightblue", relief="ridge", bd=2)
        score_frame.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        self.score_label_ai = tkinter.Label(score_frame, 
                                           text=f"May: {self.score['May']}", 
                                           font=(FONT, FONT_SIZE, "bold"), bg="lightblue", fg="red")
        self.score_label_ai.grid(row=0, column=0, padx=PADX_VALUE, pady=5)
        
        self.score_label_human = tkinter.Label(score_frame, 
                                              text=f"Nguoi choi: {self.score['Nguoi choi']}", 
                                              font=(FONT, FONT_SIZE, "bold"), bg="lightblue", fg="blue")
        self.score_label_human.grid(row=0, column=1, padx=PADX_VALUE, pady=5)
        
        self.score_label_tie = tkinter.Label(score_frame, 
                                            text=f"Hoa: {self.score['Hoa']}", 
                                            font=(FONT, FONT_SIZE, "bold"), bg="lightblue", fg="green")
        self.score_label_tie.grid(row=0, column=2, padx=PADX_VALUE, pady=5)

    def khoitao(self):
        # bat dau, reset tat ca, cho ban co ve trang thai bat dau
        self.board = [" "] * 36
        self.game_active = True
        
        # ve hinh, chon mau
        self.images = {
            "X": self.vex("white"),
            "O": self.veo("white"), 
            "X-winner": self.vex("yellow"),
            "O-winner": self.veo("yellow"),
            "plain": self.otrong()
        }

        self.tiles = {}
        for i in range(36):
            row, col = divmod(i, BOARD_SIZE)
            btn = tkinter.Button(self.game_frame, 
                               image=self.images["plain"], 
                               command=partial(self.nguoichoidanh, i),
                               relief="raised", bd=2, bg="white",
                               activebackground="lightgray")
            btn.grid(row=row, column=col, padx=1, pady=1)
            self.tiles[i] = {"id": i, "Button": btn}

    def vex(self, bg_color):
        # ve X, dung mau do
        img = Image.new("RGB", (TILE_SIZE, TILE_SIZE), bg_color)
        draw = ImageDraw.Draw(img)
        margin = 15
        width = 5
        draw.line([margin, margin, TILE_SIZE-margin, TILE_SIZE-margin], fill="darkred", width=width)
        draw.line([margin, TILE_SIZE-margin, TILE_SIZE-margin, margin], fill="darkred", width=width)
        draw.line([margin-1, margin-1, TILE_SIZE-margin+1, TILE_SIZE-margin+1], fill="red", width=2)
        draw.line([margin-1, TILE_SIZE-margin+1, TILE_SIZE-margin+1, margin-1], fill="red", width=2)
        return ImageTk.PhotoImage(img)

    def veo(self, bg_color):
        # ve O, mau xanh
        img = Image.new("RGB", (TILE_SIZE, TILE_SIZE), bg_color)
        draw = ImageDraw.Draw(img)
        margin = 15
        width = 5
        draw.ellipse([margin, margin, TILE_SIZE-margin, TILE_SIZE-margin], outline="darkblue", width=width)
        draw.ellipse([margin+3, margin+3, TILE_SIZE-margin-3, TILE_SIZE-margin-3], outline="blue", width=2)
        return ImageTk.PhotoImage(img)

    def otrong(self):
        # ve o trong
        img = Image.new("RGB", (TILE_SIZE, TILE_SIZE), "white")
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, TILE_SIZE-1, TILE_SIZE-1], outline="gray", width=2)
        draw.rectangle([2, 2, TILE_SIZE-3, TILE_SIZE-3], outline="lightgray", width=1)
        return ImageTk.PhotoImage(img)

    def capnhatdiem(self, winner):
        # điểm cập nhật, dựa vào người thắng
        if winner == "Nguoi choi":
            self.score["Nguoi choi"] += 1
            self.score_label_human.config(
                text=f"Nguoi choi: {self.score['Nguoi choi']}",
                fg="darkgreen"
            )
            self.score_label_ai.config(fg="red")
            self.score_label_tie.config(fg="green")
        elif winner == "May":
            self.score["May"] += 1 
            self.score_label_ai.config(
                text=f"May: {self.score['May']}",
                fg="darkgreen"
            )
            self.score_label_human.config(fg="blue")
            self.score_label_tie.config(fg="green")
        else:
            self.score["Hoa"] += 1
            self.score_label_tie.config(
                text=f"Hoa: {self.score['Hoa']}",
                fg="purple"
            )
            self.score_label_human.config(fg="blue")  
            self.score_label_ai.config(fg="red")

    def nguoichoidanh(self, position):
        # nguoi bam
        if not self.game_active or self.board[position] != " ":
            return
        self.danhco(position, "X")
        if self.kiemtraketthuc():
            return
        self.after(300, self.maydanh)

    def maydanh(self):
        # may tinh, dựa vào thuật toán
        if not self.game_active:
            return
        ai_pos = self.maychonnuoc()
        if ai_pos != -1:
            self.danhco(ai_pos, "O")
            self.kiemtraketthuc()

    def danhco(self, pos, player):
        self.board[pos] = player
        self.tiles[pos]["Button"].config(image=self.images[player])

    def maychonnuoc(self):
        # may tinh chon nuoc, tinh toan, suy nghi, roi quyet dinh
        empty_positions = [i for i in range(36) if self.board[i] == " "]
        if not empty_positions:
            return -1
        for pos in empty_positions:
            if self.cothethang(pos, "O"):
                return pos
        for pos in empty_positions:
            if self.cothethang(pos, "X"):
                return pos
        best_positions = []
        max_threats = 0
        for pos in empty_positions:
            threats = self.demcohoithang(pos, "O")
            if threats > max_threats:
                max_threats = threats
                best_positions = [pos]
            elif threats == max_threats:
                best_positions.append(pos)
        if best_positions:
            return choice(best_positions)
        priority_positions = [14, 15, 20, 21, 13, 16, 19, 22]
        good_moves = [pos for pos in priority_positions if pos in empty_positions]
        if good_moves:
            return choice(good_moves)
        return choice(empty_positions)

    def cothethang(self, pos, player):
        # kiem tra xem co thang khong, neu thang thi tiep tuc danh
        self.board[pos] = player
        can_win = self.coduongthang(player)
        self.board[pos] = " "
        return can_win

    def demcohoithang(self, pos, player):
        # dem co hoi thang
        self.board[pos] = player
        row, col = divmod(pos, BOARD_SIZE)
        opportunities = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            for start in range(-WIN_CONDITION + 1, 1):
                line_positions = []
                valid = True
                for i in range(WIN_CONDITION):
                    r = row + (start + i) * dr
                    c = col + (start + i) * dc
                    if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                        line_positions.append(r * BOARD_SIZE + c)
                    else:
                        valid = False
                        break
                if valid and self.duongtot(line_positions, player):
                    opportunities += 1
        self.board[pos] = " "
        return opportunities

    def duongtot(self, positions, player):
        # đường tốt nhất, có thể thắng
        opponent = "X" if player == "O" else "O"
        player_count = 0
        empty_count = 0
        for pos in positions:
            if self.board[pos] == player:
                player_count += 1
            elif self.board[pos] == " ":
                empty_count += 1
            else:
                return False
        return player_count > 0 or empty_count == WIN_CONDITION

    def kiemtraketthuc(self):
        # ket thuc game, kiem tra nguoi thang
        winner = self.timnguoithang()
        if winner:
            self.game_active = False
            if winner == "X":
                self.capnhatdiem("Nguoi choi")
                self.hienketthuc("Chuc mung! Ban thang roi!")
            else:
                self.capnhatdiem("May") 
                self.hienketthuc("May thang! Lan sau co gang hon nhe!")
            return True
        elif " " not in self.board:
            self.game_active = False
            self.capnhatdiem("Hoa")
            self.hienketthuc("Hoa roi! Tran dau hay!")
            return True
        return False

    def timnguoithang(self):
        # tim nguoi thang
        winning_lines = self.cacduongthang()
        for line_positions in winning_lines:
            line_values = [self.board[pos] for pos in line_positions]
            if len(set(line_values)) == 1 and line_values[0] != " ":
                self.tomau(line_positions)
                return line_values[0]
        return None

    def cacduongthang(self):
        # lay tat ca cac duong thang
        if not hasattr(self, '_winning_lines'):
            self._winning_lines = []
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE - WIN_CONDITION + 1):
                    line = [row * BOARD_SIZE + col + i for i in range(WIN_CONDITION)]
                    self._winning_lines.append(line)
            for col in range(BOARD_SIZE):
                for row in range(BOARD_SIZE - WIN_CONDITION + 1):
                    line = [(row + i) * BOARD_SIZE + col for i in range(WIN_CONDITION)]
                    self._winning_lines.append(line)
            for row in range(BOARD_SIZE - WIN_CONDITION + 1):
                for col in range(BOARD_SIZE - WIN_CONDITION + 1):
                    line = [(row + i) * BOARD_SIZE + col + i for i in range(WIN_CONDITION)]
                    self._winning_lines.append(line)
            for row in range(BOARD_SIZE - WIN_CONDITION + 1):
                for col in range(WIN_CONDITION - 1, BOARD_SIZE):
                    line = [(row + i) * BOARD_SIZE + col - i for i in range(WIN_CONDITION)]
                    self._winning_lines.append(line)
        return self._winning_lines

    def coduongthang(self, player):
        # kiem tra xem co duong thang nao khong
        for line_positions in self.cacduongthang():
            if all(self.board[pos] == player for pos in line_positions):
                return True
        return False

    def tomau(self, positions):
        # to mau cac o thang
        for pos in positions:
            player = self.board[pos]
            self.tiles[pos]["Button"].config(
                image=self.images[f"{player}-winner"],
                relief="sunken",
                bg="gold"
            )

    def hienketthuc(self, message):
        # hien thong bao ket thuc, hoi nguoi choi co muon choi tiep khong
        full_message = f"{message}\n\nBan co muon choi lai khong?"
        if msgbox.askyesno("Ket thuc game", full_message):
            self.gamemoi()
        else:
            self.quit()

    def gamemoi(self):
        # bat dau lai, reset tat ca, cho cuoc choi tiep tuc
        for i in range(36):
            self.tiles[i]["Button"].config(
                image=self.images["plain"],
                relief="raised",
                bg="white"
            )
        self.board = [" "] * 36
        self.game_active = True
        self.score_label_human.config(
            text=f"Nguoi choi: {self.score['Nguoi choi']}",
            fg="blue"
        )
        self.score_label_ai.config(
            text=f"May: {self.score['May']}",
            fg="red"
        )
        self.score_label_tie.config(
            text=f"Hoa: {self.score['Hoa']}",
            fg="green"
        )

if __name__ == "__main__":
    game = TicTacToe6x6()
    game.mainloop()