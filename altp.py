import tkinter
from tkinter import *
import random
from PIL import Image, ImageTk
import pygame
from pygame import mixer

#các hàm về âm thanh cho game
def sound_game():
    mixer.init()
    mixer.music.load('background.mp3')
    mixer.music.play()
def sound_dung():
    mixer.init()
    mixer.music.load('dung.mp3')
    mixer.music.play()
def sound_sai():
    mixer.init()
    mixer.music.load('sai.mp3')
    mixer.music.play()
def sound_bravo():
    mixer.init()
    mixer.music.load('bravo.mp3')
    mixer.music.play()
def sound_troll():
    mixer.init()
    mixer.music.load('troll.mp3')
    mixer.music.play()
def hoihop():
    mixer.init()
    mixer.music.load('hoihop.mp3')
    mixer.music.play()
def exit():
    window.destroy()
#hàm hiển thị đáp án
def show_answer():
    global cauhoi
    global click_button
    global True_num
    global i
    if click_button == 2:
        click_button = 0
        if cauhoi == question[0]:
            asw_d.config(bg='#5df709')
            True_num='d'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[1]:
            asw_c.config(bg='#5df709')
            True_num = 'c'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[2]:
            asw_a.config(bg='#5df709')
            True_num = 'a'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[3]:
            asw_c.config(bg='#5df709')
            True_num = 'c'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[4]:
            asw_c.config(bg='#5df709')
            True_num = 'c'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[5]:
            asw_a.config(bg='#5df709')
            True_num = 'a'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[6]:
            asw_c.config(bg='#5df709')
            True_num = 'c'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[7]:
            asw_d.config(bg='#5df709')
            True_num = 'd'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[8]:
            asw_b.config(bg='#5df709')
            True_num = 'b'
            sound_dung()
            window.after(3000, hoihop)
        elif cauhoi == question[9]:
            asw_c.config(bg='#5df709')
            True_num = 'c'
            sound_dung()
            window.after(3000, hoihop)
        if num_choice==True_num:
            i+=1
            checkTF.config(text='ĐÚNG', bg='#5df709')
            print(i)
            if i == 2: money1.config(bg='#5df709')
            elif i == 3: money2.config(bg='#5df709')
            elif i == 4: money3.config(bg='#5df709')
            elif i == 5: money4.config(bg='#5df709')
            elif i == 6: money5.config(bg='#5df709')
            elif i == 7: money6.config(bg='#5df709')
            elif i == 8: money7.config(bg='#5df709')
            elif i == 9: money8.config(bg='#5df709')
            elif i == 10: money9.config(bg='#5df709')
            else:
                money10.config(bg='#5df709')
                sound_bravo()
                ask.config(text='Xin Chúc Mừng, Bạn là Triệu phú!')
                checkTF.config(text='DONE!')
                window.after(5000, exit)
            window.after(2000, update_question)
        else:
            sound_sai()
            checkTF.config(text='SAI', bg='red')
            window.after(5000, sound_troll)
            ask.config(text='Bạn đã trời lời sai rồi!\n Thoát GAME sau 10s.', bg='red')
            window.after(10000, exit)
#các hàm kiểm tra đáp án người chơi chọn
def check_click_a():
    global num_choice
    global click_button
    click_button += 1
    asw_a.config(bg='blue')
    asw_b.config(bg='#0f0e13', fg='white')
    asw_c.config(bg='#0f0e13', fg='white')
    asw_d.config(bg='#0f0e13', fg='white')
    num_choice='a'
    show_answer()
def check_click_b():
    global num_choice
    global click_button
    click_button += 1
    asw_a.config(bg='#0f0e13', fg='white')
    asw_b.config(bg='blue')
    asw_c.config(bg='#0f0e13', fg='white')
    asw_d.config(bg='#0f0e13', fg='white')
    num_choice = 'b'
    show_answer()
def check_click_c():
    global num_choice
    global click_button
    click_button += 1
    asw_a.config(bg='#0f0e13', fg='white')
    asw_b.config(bg='#0f0e13', fg='white')
    asw_c.config(bg='blue')
    asw_d.config(bg='#0f0e13', fg='white')
    num_choice = 'c'
    show_answer()
def check_click_d():
    global num_choice
    global click_button
    click_button += 1
    asw_a.config(bg='#0f0e13', fg='white')
    asw_b.config(bg='#0f0e13', fg='white')
    asw_c.config(bg='#0f0e13', fg='white')
    asw_d.config(bg='blue')
    num_choice = 'd'
    show_answer()
#hàm tạo câu hỏi mới
def setup_question():
    global cauhoi
    cauhoi = random.choice(question)
def update_question():
    global i
    global cauhoi
    global curren_question
    curren_question.append(cauhoi)
    setup_question()
    while cauhoi in curren_question:
        setup_question()
    if 'Khẳng định nào sau đây' in cauhoi:
        a = answer1[0]
        b = answer1[1]
        c = answer1[2]
        d = answer1[3]
    elif 'Lệnh nào dùng để lấy' in cauhoi:
        a = answer2[0]
        b = answer2[1]
        c = answer2[2]
        d = answer2[3]
    elif 'Câu lệnh sử dụng' in cauhoi:
        a = answer3[0]
        b = answer3[1]
        c = answer3[2]
        d = answer3[3]
    elif 'Đâu không phải là kiểu' in cauhoi:
        a = answer4[0]
        b = answer4[1]
        c = answer4[2]
        d = answer4[3]
    elif 'ngôn ngữ' in cauhoi:
        a = answer5[0]
        b = answer5[1]
        c = answer5[2]
        d = answer5[3]
    elif 'Ronaldo' in cauhoi:
        a = answer6[0]
        b = answer6[1]
        c = answer6[2]
        d = answer6[3]
    elif 'Cầu thủ nào đã' in cauhoi:
        a = answer7[0]
        b = answer7[1]
        c = answer7[2]
        d = answer7[3]
    elif 'Nước nào vô địch' in cauhoi:
        a = answer8[0]
        b = answer8[1]
        c = answer8[2]
        d = answer8[3]
    elif 'Người đầu tiên dẫn' in cauhoi:
        a = answer9[0]
        b = answer9[1]
        c = answer9[2]
        d = answer9[3]
    elif 'Nước Việt Nam' in cauhoi:
        a = answer10[0]
        b = answer10[1]
        c = answer10[2]
        d = answer10[3]

    ask.config(text='Câu '+str(i)+': '+cauhoi)
    asw_a.config(text='A: ' + a, bg='#0f0e13', fg='white')
    asw_b.config(text='B: ' + b, bg='#0f0e13', fg='white')
    asw_c.config(text='C: ' + c, bg='#0f0e13', fg='white')
    asw_d.config(text='D: ' + d, bg='#0f0e13', fg='white')
#hàm khởi động game
def start_game():
    sound_game()
    global i
    i=1
# tao nut
    global ask
    global asw_a
    global asw_b
    global asw_c
    global asw_d

    ask = Button(window, text='Câu ' + ': ', width=100, height=5, bg='#0f0e13', fg='white')
    asw_a = Button(window, text='A: ' , width=50, height=3, command=check_click_a, bg='#0f0e13', fg='white')
    asw_b = Button(window, text='B: ' , width=50, height=3, command=check_click_b, bg='#0f0e13', fg='white')
    asw_c = Button(window, text='C: ' , width=50, height=3, command=check_click_c, bg='#0f0e13', fg='white')
    asw_d = Button(window, text='D: ', width=50, height=3, command=check_click_d, bg='#0f0e13', fg='white')
    update_question()
    ask.grid(columnspan=2, rowspan=2, pady=(340, 20))
    asw_a.grid(column=0, row=2, padx=2, pady=2)
    asw_b.grid(column=1, row=2, padx=2, pady=2)
    asw_c.grid(column=0, row=3, padx=2, pady=2)
    asw_d.grid(column=1, row=3, padx=2, pady=2)

    window.mainloop()
# khoi tao doi tuong tk
window = Toplevel()
window.title('Game-Ailatrieuphu')
window.geometry('870x600')
window.resizable(False, False)
bg = PhotoImage(file='altp.png')
img = Label(window, image=bg, width=870, height=600)
img.place(x=0, y=0)
checkTF = Label(window, width=15, height=5, text="", bg='#0f0e13', fg='yellow')
checkTF.place(x=0, y=0)
#câp nhật số $ người chơi
money1 = Button(window, text='$100', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money1.place(x=790, y=300)
money2 = Button(window, text='$200', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money2.place(x=790, y=270)
money3 = Button(window, text='$300', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money3.place(x=790, y=240)
money4 = Button(window, text='$500', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money4.place(x=790, y=210)
money5 = Button(window, text='$1000', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money5.place(x=790, y=180)
money6 = Button(window, text='$2000', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money6.place(x=790, y=150)
money7 = Button(window, text='$4000', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money7.place(x=790, y=120)
money8 = Button(window, text='$8000', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money8.place(x=790, y=90)
money9 = Button(window, text='$16000', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money9.place(x=790, y=60)
money10 = Button(window, text='$25000', width=5, heigh=1, bg='#0f0e13', fg='yellow')
money10.place(x=790, y=30)
# khai bao bien
curren_question = []
click_button = 0
question = ('Khẳng định nào sau đây về Python là đúng?',
            'Lệnh nào dùng để lấy dữ liệu đầu vào từ người dùng?',
            'Câu lệnh sử dụng toán tử and trả về kết quả TRUE khi nào?',
            'Đâu không phải là kiểu dữ liệu tiêu chuẩn trong Python?',
            'Đâu không phải là ngôn ngữ lập trình?',
            'Cầu thủ C.Ronaldo có quốc tịch nào?',
            'Cầu thủ nào đã giành được 6 quả bóng vàng?',
            'Nước nào vô địch EURO 2020?',
            'Người đầu tiên dẫn chương trình "Ai là triệu phú" là ai?',
            'Nước Việt Nam có bao nhiều tỉnh thành?'
            )
answer1 = ['Python là một ngôn ngữ lập trình cấp cao.', 'Python là một ngôn ngữ thông dịch.', 'Python là ngôn ngữ lập trình hướng đối tượng.', 'Tất cả các đáp án đều đúng.']
answer2 = ['cin', 'scanf()', 'input()', 'login']
answer3 = ['Cả hai toán hạng đều là TRUE.', 'Cả hai toán hàng đều là FALSE.', 'Một trong hai toán hạng là TRUE.', 'Toán hạng đầu tiên là TRUE.']
answer4 = ['List', 'Dictionary', 'Class', 'Tuple']
answer5 = ['Java', 'Python', 'English', 'Ruby']
answer6 = ['Bồ Đào Nha', 'Tây Ban Nha', 'Ý', 'Pháp']
answer7 = ['C.Ronaldo', 'Neymar', 'Messi', 'Pele']
answer8 = ['Pháp', 'Anh', 'Việt Nam', 'Ý']
answer9 = ['GS.Xoay', 'Lại Văn Sâm', 'Phan Đăng', 'Lâm Đức Long']
answer10 = ['54', '61', '63', '64']
cauhoi = ''
#chạy game
start_game()
