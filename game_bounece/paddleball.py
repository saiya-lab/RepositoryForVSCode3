from tkinter import *
import random
import time
import pygame.mixer

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

        # ボールの初期位置
        self.reset_ball()

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        #gameover判定
        self.hit_bottom = False

    def reset_ball(self):
        self.canvas.coords(self.id, 245, 200, 260, 215)

        # ボールの初期移動方向と速度を設定
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global sound_bounce

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        reflected = False

        # 天井の反射コード
        if pos[1] <= 0:
            self.y = self.y * -1
            reflected = True

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit_paddle(pos) == True:
            self.y = self.y * -1
            reflected = True

        #左右の反射
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * -1
            reflected = True

        #sound
        if reflected and 'sound_bounce' in globals() and sound_bounce is not None:
            sound_bounce.play()


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.start_move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.start_move_right)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_move)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_move)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # 画面端に達したら動きを止める
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

    def start_move_left(self, evt):
        self.x = -4

    def start_move_right(self, evt):
        self.x = 4

    def stop_move(self, evt):
        if evt.keysym == "Left" or evt.keysym == "Right":
            self.x = 0


tk = Tk()
tk.title("Bounce Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()  # ここで一度更新して、Canvasのサイズを確定させる

#sound
sound_bounce = None
sound_game_over = None
try:
    pygame.mixer.init()
    sound_bounce = pygame.mixer.Sound("bounce.wav")
    sound_bounce.set_volume(0.3)

    sound_game_over = pygame.mixer.Sound("game_over.wav")
    sound_game_over.set_volume(0.4)
except pygame.error as e:
    print(f"警告:サウンドの初期化またはロード中にエラーが発生しました。ノーサウンドで実行します。エラー詳細: {e}")
    sound_bounce = None
except Exception as e:
    print(f"その他エラー: {e}")
    sound_bounce = None


paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

# --- ゲームの状態管理 ---
GAME_STATE = "waiting_to_start"
DELAY_DURATION = 3

intro_text_id = canvas.create_text(
    250, 150, text="Press SPACE to Start", font=("Helvetica", 20), fill="gray"
)
delay_text_id = None
game_over_text_id = None


def start_delay(evt):
    """SPACEキーが押されたら遅延を開始。"""
    global GAME_STATE, delay_text_id, intro_text_id
    if GAME_STATE == "waiting_to_start" or GAME_STATE == "game_over":
        GAME_STATE = "delaying"
        canvas.delete(intro_text_id)
        canvas.delete(game_over_text_id)  # ゲームオーバーテキストも消す
        ball.reset_ball()
        # 遅延テキスト
        delay_text_id = canvas.create_text(
            250,
            200,
            text=f"Game starts in {DELAY_DURATION}...",
            font=("Helvetica", 24, "bold"),
            fill="green",
        )

        # countdown
        countdown(DELAY_DURATION)


def countdown(second_left):
    """指定された秒数でカウントダウンを行い、終了後にゲームを開始。"""
    global GAME_STATE, delay_text_id

    if second_left > 0:
        canvas.itemconfig(delay_text_id, text=f"Game starts in {second_left}...")

        tk.after(1000, countdown, second_left - 1)
    else:
        GAME_STATE = "playing"
        canvas.delete(delay_text_id)

        update_game()


def update_game():
    """ゲームの動きを定期的に更新するメインループ。"""
    global GAME_STATE, game_over_text_id, sound_game_over

    if GAME_STATE == "playing":
        ball.draw()
        paddle.draw()

        if ball.hit_bottom:
            GAME_STATE = "game_over"

            if sound_game_over is not None:
                sound_game_over.play()

            game_over_text_id = canvas.create_text(
                250, 200, text="GAME OVER!!", font=("Helvetica", 32, "bold"), fill="red"
            )
            tk.after(
                1500,
                lambda: canvas.itemconfig(
                    game_over_text_id, text="GAME OVER!!\nPress SPACE to restart."
                ),
            )
        # restart text
        else:
            tk.after(10, update_game)


canvas.bind_all("<space>", start_delay)
tk.mainloop()

# while True:
# if ball.hit_bottom == False:
# ball.draw()
# paddle.draw()
# tk.update_idletasks()
# tk.update()
# time.sleep(0.01)
#
