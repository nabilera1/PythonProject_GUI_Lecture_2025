import tkinter as tk
import webbrowser

def open_naver():
    url = 'https://www.naver.com'
    webbrowser.open(url)

# 기본 창 생성
root = tk.Tk()
root.title("웹 열기 예제")
# root.geometry("300x100")
root.geometry("300x100") # 소문자 x
# 버튼 추가
btn = tk.Button(root, text="네이버 열기", command=open_naver)
btn.pack(pady=20)

# GUI 실행
root.mainloop()
