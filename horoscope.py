from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import requests
if __name__ == '__main__':
    root = Tk()
    root.title('Horoscope')
    root.geometry('777x555')

    def get_daily():
        root = Tk()
        root.geometry("777x555")
        root.title("Daily Horoscope")
        root.config(bg="bisque")
        def get_horoscope(zodiac_sign):
            url = (f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={zodiac_sign}")
            Soup = BeautifulSoup(requests.get(url).content, "lxml")
            horoscope = Soup.find("div", class_="main-horoscope").p.text
            new_horoscope = horoscope.replace(".", ".\n")
            text_box.delete("1.0", END)
            text_box.insert(END, new_horoscope)

        inner_frame = Frame(root, bg="bisque")
        inner_frame.pack()
        label_choice = Label(inner_frame, text="Select Your Zodiac Sign", fg="darkorange", bg="bisque", font=("Arial", 25, "bold"), padx=10, pady=10)
        label_choice.grid(row=0, column=0, padx=10, pady=10)
        Select_frame = Frame(inner_frame, bg="bisque")
        Select_frame.grid(row=1, column=0)
        sign_1 = Button(Select_frame, text="Aries", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(1))
        sign_1.grid(row=1, column=0, padx=10, pady=10)
        sign_2 = Button(Select_frame, text="Taurus", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(2))
        sign_2.grid(row=1, column=1, padx=10, pady=10)
        sign_3 = Button(Select_frame, text="Gemini", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(3))
        sign_3.grid(row=1, column=2, padx=10, pady=10)
        sign_4 = Button(Select_frame, text="Cancer", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(4))
        sign_4.grid(row=2, column=0, padx=10, pady=10)
        sign_5 = Button(Select_frame, text="Leo", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(5))
        sign_5.grid(row=2, column=1, padx=10, pady=10)
        sign_6 = Button(Select_frame, text="Virgo", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(6))
        sign_6.grid(row=2, column=2, padx=10, pady=10)
        sign_7 = Button(Select_frame, text="Libra", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(7))
        sign_7.grid(row=3, column=0, padx=10, pady=10)
        sign_8 = Button(Select_frame, text="Scorpio", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(8))
        sign_8.grid(row=3, column=1, padx=10, pady=10)
        sign_9 = Button(Select_frame, text="Sagittarius", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(9))
        sign_9.grid(row=3, column=2, padx=10, pady=10)
        sign_10 = Button(Select_frame, text="Capricorn", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(10))
        sign_10.grid(row=4, column=0, padx=10, pady=10)
        sign_11 = Button(Select_frame, text="Aquarius", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(11))
        sign_11.grid(row=4, column=1, padx=10, pady=10)
        sign_12 = Button(Select_frame, text="Pisces", bg="orange", fg="white", borderwidth=0, padx=10, pady=5, font=("Arial", 12, "bold"), command=lambda: get_horoscope(12))
        sign_12.grid(row=4, column=2, padx=10, pady=10)

        frame_data = Frame(inner_frame, bg="bisque")
        frame_data.grid(row=5, column=0, padx=10, pady=10)
        text_box = Text(frame_data, bg="orange", height=10, width=80, fg="white", font=("Helvetica", 15))
        text_box.grid(pady=15)

    def get_career():
        root = Tk()
        root.geometry("777x555")
        root.title("Daily Horoscope")
        root.config(bg="paleturquoise")

        def get_horoscope(zodiac_sign):
            url = (
                f"https://www.horoscope.com/us/horoscopes/career/horoscope-career-daily-today.aspx?sign={zodiac_sign}")
            Soup = BeautifulSoup(requests.get(url).content, "lxml")
            horoscope = Soup.find("div", class_="main-horoscope").p.text
            new_horoscope = horoscope.replace(".", ".\n")
            text_box.delete("1.0", END)
            text_box.insert(END, new_horoscope)

        inner_frame = Frame(root, bg="paleturquoise")
        inner_frame.pack()
        label_choice = Label(inner_frame, text="Select Your Zodiac Sign", fg="teal", bg="paleturquoise",
                             font=("Arial", 25, "bold"), padx=10, pady=10)
        label_choice.grid(row=0, column=0, padx=10, pady=10)
        Select_frame = Frame(inner_frame, bg="paleturquoise")
        Select_frame.grid(row=1, column=0)
        sign_1 = Button(Select_frame, text="Aries", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(1))
        sign_1.grid(row=1, column=0, padx=10, pady=10)
        sign_2 = Button(Select_frame, text="Taurus", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(2))
        sign_2.grid(row=1, column=1, padx=10, pady=10)
        sign_3 = Button(Select_frame, text="Gemini", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(3))
        sign_3.grid(row=1, column=2, padx=10, pady=10)
        sign_4 = Button(Select_frame, text="Cancer", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(4))
        sign_4.grid(row=2, column=0, padx=10, pady=10)
        sign_5 = Button(Select_frame, text="Leo", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(5))
        sign_5.grid(row=2, column=1, padx=10, pady=10)
        sign_6 = Button(Select_frame, text="Virgo", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(6))
        sign_6.grid(row=2, column=2, padx=10, pady=10)
        sign_7 = Button(Select_frame, text="Libra", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(7))
        sign_7.grid(row=3, column=0, padx=10, pady=10)
        sign_8 = Button(Select_frame, text="Scorpio", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(8))
        sign_8.grid(row=3, column=1, padx=10, pady=10)
        sign_9 = Button(Select_frame, text="Sagittarius", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(9))
        sign_9.grid(row=3, column=2, padx=10, pady=10)
        sign_10 = Button(Select_frame, text="Capricorn", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                         font=("Arial", 12, "bold"), command=lambda: get_horoscope(10))
        sign_10.grid(row=4, column=0, padx=10, pady=10)
        sign_11 = Button(Select_frame, text="Aquarius", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                         font=("Arial", 12, "bold"), command=lambda: get_horoscope(11))
        sign_11.grid(row=4, column=1, padx=10, pady=10)
        sign_12 = Button(Select_frame, text="Pisces", bg="teal", fg="white", borderwidth=0, padx=10, pady=5,
                         font=("Arial", 12, "bold"), command=lambda: get_horoscope(12))
        sign_12.grid(row=4, column=2, padx=10, pady=10)

        frame_data = Frame(inner_frame, bg="paleturquoise")
        frame_data.grid(row=5, column=0, padx=10, pady=10)
        text_box = Text(frame_data, bg="teal", height=10, width=80, fg="white", font=("Helvetica", 15))
        text_box.grid(pady=15)

    def get_love():
        root = Tk()
        root.geometry("777x555")
        root.title("Daily Horoscope")
        root.config(bg="hotpink")

        def get_horoscope(zodiac_sign):
            url = (
                f"https://www.horoscope.com/us/horoscopes/love/horoscope-love-daily-today.aspx?sign={zodiac_sign}")
            Soup = BeautifulSoup(requests.get(url).content, "lxml")
            horoscope = Soup.find("div", class_="main-horoscope").p.text
            new_horoscope = horoscope.replace(".", ".\n")
            text_box.delete("1.0", END)
            text_box.insert(END, new_horoscope)

        inner_frame = Frame(root, bg="hotpink")
        inner_frame.pack()
        label_choice = Label(inner_frame, text="Select Your Zodiac Sign", fg="purple", bg="hotpink",
                             font=("Arial", 25, "bold"), padx=10, pady=10)
        label_choice.grid(row=0, column=0, padx=10, pady=10)
        Select_frame = Frame(inner_frame, bg="hotpink")
        Select_frame.grid(row=1, column=0)
        sign_1 = Button(Select_frame, text="Aries", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(1))
        sign_1.grid(row=1, column=0, padx=10, pady=10)
        sign_2 = Button(Select_frame, text="Taurus", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(2))
        sign_2.grid(row=1, column=1, padx=10, pady=10)
        sign_3 = Button(Select_frame, text="Gemini", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(3))
        sign_3.grid(row=1, column=2, padx=10, pady=10)
        sign_4 = Button(Select_frame, text="Cancer", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(4))
        sign_4.grid(row=2, column=0, padx=10, pady=10)
        sign_5 = Button(Select_frame, text="Leo", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(5))
        sign_5.grid(row=2, column=1, padx=10, pady=10)
        sign_6 = Button(Select_frame, text="Virgo", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(6))
        sign_6.grid(row=2, column=2, padx=10, pady=10)
        sign_7 = Button(Select_frame, text="Libra", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(7))
        sign_7.grid(row=3, column=0, padx=10, pady=10)
        sign_8 = Button(Select_frame, text="Scorpio", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(8))
        sign_8.grid(row=3, column=1, padx=10, pady=10)
        sign_9 = Button(Select_frame, text="Sagittarius", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                        font=("Arial", 12, "bold"), command=lambda: get_horoscope(9))
        sign_9.grid(row=3, column=2, padx=10, pady=10)
        sign_10 = Button(Select_frame, text="Capricorn", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                         font=("Arial", 12, "bold"), command=lambda: get_horoscope(10))
        sign_10.grid(row=4, column=0, padx=10, pady=10)
        sign_11 = Button(Select_frame, text="Aquarius", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                         font=("Arial", 12, "bold"), command=lambda: get_horoscope(11))
        sign_11.grid(row=4, column=1, padx=10, pady=10)
        sign_12 = Button(Select_frame, text="Pisces", bg="purple", fg="white", borderwidth=0, padx=10, pady=5,
                         font=("Arial", 12, "bold"), command=lambda: get_horoscope(12))
        sign_12.grid(row=4, column=2, padx=10, pady=10)

        frame_data = Frame(inner_frame, bg="hotpink")
        frame_data.grid(row=5, column=0, padx=10, pady=10)
        text_box = Text(frame_data, bg="purple", height=10, width=80, fg="white", font=("Helvetica", 15))
        text_box.grid(pady=15)

    def get_money():
        root = Tk()
        root.geometry("777x555")
        root.title("Daily Horoscope")
        root.config(bg="sandybrown")

        def get_horoscope(zodiac_sign):
            url = (
                    f"https://www.horoscope.com/us/horoscopes/money/horoscope-money-weekly.aspx?sign={zodiac_sign}")
            Soup = BeautifulSoup(requests.get(url).content, "lxml")
            horoscope = Soup.find("div", class_="main-horoscope").p.text
            new_horoscope = horoscope.replace(".", ".\n")
            text_box.delete("1.0", END)
            text_box.insert(END, new_horoscope)

        inner_frame = Frame(root, bg="sandybrown")
        inner_frame.pack()
        label_choice = Label(inner_frame, text="Select Your Zodiac Sign", fg="brown", bg="sandybrown",
                                 font=("Arial", 25, "bold"), padx=10, pady=10)
        label_choice.grid(row=0, column=0, padx=10, pady=10)
        Select_frame = Frame(inner_frame, bg="sandybrown")
        Select_frame.grid(row=1, column=0)
        sign_1 = Button(Select_frame, text="Aries", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(1))
        sign_1.grid(row=1, column=0, padx=10, pady=10)
        sign_2 = Button(Select_frame, text="Taurus", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(2))
        sign_2.grid(row=1, column=1, padx=10, pady=10)
        sign_3 = Button(Select_frame, text="Gemini", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(3))
        sign_3.grid(row=1, column=2, padx=10, pady=10)
        sign_4 = Button(Select_frame, text="Cancer", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(4))
        sign_4.grid(row=2, column=0, padx=10, pady=10)
        sign_5 = Button(Select_frame, text="Leo", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(5))
        sign_5.grid(row=2, column=1, padx=10, pady=10)
        sign_6 = Button(Select_frame, text="Virgo", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(6))
        sign_6.grid(row=2, column=2, padx=10, pady=10)
        sign_7 = Button(Select_frame, text="Libra", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(7))
        sign_7.grid(row=3, column=0, padx=10, pady=10)
        sign_8 = Button(Select_frame, text="Scorpio", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(8))
        sign_8.grid(row=3, column=1, padx=10, pady=10)
        sign_9 = Button(Select_frame, text="Sagittarius", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                            font=("Arial", 12, "bold"), command=lambda: get_horoscope(9))
        sign_9.grid(row=3, column=2, padx=10, pady=10)
        sign_10 = Button(Select_frame, text="Capricorn", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                             font=("Arial", 12, "bold"), command=lambda: get_horoscope(10))
        sign_10.grid(row=4, column=0, padx=10, pady=10)
        sign_11 = Button(Select_frame, text="Aquarius", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                             font=("Arial", 12, "bold"), command=lambda: get_horoscope(11))
        sign_11.grid(row=4, column=1, padx=10, pady=10)
        sign_12 = Button(Select_frame, text="Pisces", bg="brown", fg="white", borderwidth=0, padx=10, pady=5,
                             font=("Arial", 12, "bold"), command=lambda: get_horoscope(12))
        sign_12.grid(row=4, column=2, padx=10, pady=10)

        frame_data = Frame(inner_frame, bg="sandybrown")
        frame_data.grid(row=5, column=0, padx=10, pady=10)
        text_box = Text(frame_data, bg="brown", height=10, width=80, fg="white", font=("Helvetica", 15))
        text_box.grid(pady=15)



    frame = Frame(root, bg="hotpink")
    frame.pack(padx=50, pady=40)
    label_top = Label(frame, text="HoroScope", fg="purple", bg="hotpink", font=("Helvetica", 25, "bold"))
    label_top.grid(padx=10, pady=10)
    img = Image.open("astro.jpg")
    photo = ImageTk.PhotoImage(img)
    img_label = Label(frame, image=photo)
    img_label.grid(padx=20, pady=25)

    frame2 = Frame(frame, bg="hotpink")
    frame2.grid()
    btn1 = Button(frame2, text="Daily Horoscope", fg="purple", activebackground="pink", activeforeground="hotpink", bg="pink", padx=10, pady=10, font=("Helvetica", 15),
                  borderwidth=0, highlightthickness=0, command=get_daily)
    btn1.grid(row=0, column=0, padx=15, pady=15)
    btn2 = Button(frame2, text="Career Horoscope", fg="purple", activebackground="pink", activeforeground="hotpink", bg="pink", padx=10, pady=10, font=("Helvetica", 15),
                  borderwidth=0, highlightthickness=0, command=get_career)
    btn2.grid(row=0, column=1, padx=15, pady=15)
    btn3 = Button(frame2, text="Love Horoscope", fg="purple", activebackground="pink", activeforeground="hotpink", bg="pink", padx=10, pady=10, font=("Helvetica", 15),
                  borderwidth=0, highlightthickness=0, command=get_love)
    btn3.grid(row=1, column=0, padx=15, pady=15)
    btn2 = Button(frame2, text="Money Horoscope", fg="purple", activebackground="pink", activeforeground="hotpink", bg="pink", padx=10, pady=10, font=("Helvetica", 15),
                  borderwidth=0, highlightthickness=0, command=get_money)
    btn2.grid(row=1, column=1, padx=15, pady=15)

    root.mainloop()
