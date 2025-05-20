# import wx
# import webbrowser
#
# # 메인 창 클래스 정의
# class MyApp(wx.Frame):
#     def __init__(self):
#         # 창 제목과 크기 설정
#         wx.Frame.__init__(self, None, title="웹 열기", size=(400, 150))
#
#         panel = wx.Panel(self)  # 패널 생성
#
#         # URL 입력창 (기본값은 네이버)
#         self.text = wx.TextCtrl(panel, value="https://www.naver.com")
#
#         # 버튼 생성
#         button = wx.Button(panel, label="열기")
#
#         # 버튼 클릭 이벤트 연결
#         button.Bind(wx.EVT_BUTTON, self.open_url)
#
#         # 간단한 수직 레이아웃 구성
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.text, 0, wx.ALL | wx.EXPAND, 10)
#         sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)
#
#         panel.SetSizer(sizer)
#
#         self.Show()  # 창 보여주기
#
#     def open_url(self, event):
#         url = self.text.GetValue()  # 입력된 URL 가져오기
#         webbrowser.open(url)        # 브라우저로 열기
#
# # 프로그램 실행
# app = wx.App()
# MyApp()
# app.MainLoop()

import wx
import webbrowser

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='웹 열기 예제', size=(300, 150))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.button = wx.Button(panel, label='네이버 열기')
        self.button.Bind(wx.EVT_BUTTON, self.open_naver)

        vbox.Add(self.button, 0, wx.ALL | wx.CENTER, 20)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def open_naver(self, event):
        webbrowser.open('https://www.naver.com')

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()

