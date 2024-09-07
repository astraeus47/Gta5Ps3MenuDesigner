from src.functions import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(" GTA V Ps3 Menu Designer ")
        self.geometry(app_window)
        self.resizable(False, False)

        # Draw background image app. 
        self.app_bg_image()

        self.safeZoneSizeX, self.safeZoneSizeY= GetSafezoneSizeHalved()
        self.MenuXCoord3 = SetMenuPosition()

        self.DrawBackground()
        self.DrawTitle()
        self.DrawLateralScrollbar()

    def app_bg_image(self):
        img_path = '.\\pygtavmenu\\img\\background.png'
        width = app_width
        height = app_height
        self.app_background = DrawImage(img_path, width, height)
        self.app_bg_image = customtkinter.CTkLabel(self, image = self.app_background, text = '')
        self.app_bg_image.grid(row = 0, column = 0)

    def DrawLateralScrollbar(self):
        width = int(app_width * 0.0090)
        height = int(app_height * 0.035)
        fg_color = '#007cff'
        img_path = ''

        if numberOfOptions > 13:
            optionCount = 13.0 # no menu base ()
        else:
            optionCount = numberOfOptions

        backgroundLenght = optionCount * height
        height = backgroundLenght
        backgroundYCoord = (optionCount * int(app_height * 0.035) / int(app_height * 2.0)) + (int(app_height * 0.6046) - self.safeZoneSizeY)

        # Quando o menu esta na esquerda eu apenas preciso dar o espaço '64' referente a 90% da tela.
        # 1280x720 em 90% fica 1152x648 que é a zona segura.
        # centralizando o '1152x648 zona segura' ficam margens de 64 p/ 36.
        # Se o menu estiver na direta, ele tira a diferença do seu tamanho 'width'.
        if leftSided == 1:
            setLateralXCoord3 = self.MenuXCoord3 - 64
        else:
            setLateralXCoord3 = self.MenuXCoord3 - width + 64

        self.draw_lateral_scrollbar = DrawRect(self, width, height, fg_color, img_path, setLateralXCoord3, backgroundYCoord)
        self.draw_lateral_scrollbar.place(x = setLateralXCoord3 + int(app_width * 0.02), y = backgroundYCoord)

    def AddTitle(self):
        text = "Modloader"
        font_style = 'Impact'
        font_size = 24
        font = f'{font_style}', font_size
        fg_color = '#ffffff'
        titleYCoord = int(app_height * 0.5346) - self.safeZoneSizeY
        # Diferença entre o tamanho do rect do DrawTitle.
        width = int(app_width * 0.2250)

        if leftSided == 1:
            setMenuXCoord3 = self.MenuXCoord3 - 64
        else:
            setMenuXCoord3 = self.MenuXCoord3 - width + 64

        newTitleXCoord, newTitleYCoord = CenterText(text, font_size, setMenuXCoord3, titleYCoord)
        
        self.add_title = DrawText(self, text, font, fg_color)
        self.add_title.place(x = newTitleXCoord, y = newTitleYCoord)

    def DrawTitle(self):
        width = int(app_width * 0.2250)
        height = int(app_height * 0.09)
        fg_color = '#e50000'
        img_path = ''
        titleYCoord = int(app_height * 0.5596) - self.safeZoneSizeY - 30

        if leftSided == 1:
            setMenuXCoord3 = self.MenuXCoord3 - 64
        else:
            setMenuXCoord3 = self.MenuXCoord3 - width + 64

        self.draw_title = DrawRect(self, width, height, fg_color, img_path, setMenuXCoord3, titleYCoord)
        self.draw_title.place(x = setMenuXCoord3, y = titleYCoord)
        self.AddTitle() # Adicionar o titulo do menu.

    def DrawBackground(self):
        width = int(app_width * 0.2250)
        height = int(app_height * 0.035)
        fg_color = '#323232'
        img_path = '.\\pygtavmenu\\img\\bg.png'

        if numberOfOptions > 13:
            optionCount = 13.0 # no menu base ()
        else:
            optionCount = numberOfOptions

        backgroundLenght = optionCount * height
        height = backgroundLenght
        backgroundYCoord = (optionCount * int(app_height * 0.035) / int(app_height * 2.0)) + (int(app_height * 0.6046) - self.safeZoneSizeY)

        # Quando o menu esta na esquerda eu apenas preciso dar o espaço '64' referente a 90% da tela.
        # 1280x720 em 90% fica 1152x648 que é a zona segura.
        # centralizando o '1152x648 zona segura' ficam margens de 64 p/ 36.
        # Se o menu estiver na direta, ele tira a diferença do seu tamanho 'width'.
        if leftSided == 1:
            setMenuXCoord3 = self.MenuXCoord3 - 64
        else:
            setMenuXCoord3 = self.MenuXCoord3 - width + 64

        self.draw_background = DrawRect(self, width, height, fg_color, img_path, setMenuXCoord3, backgroundYCoord)
        self.draw_background.place(x = setMenuXCoord3, y = backgroundYCoord)

if __name__ == '__main__':
    app = App()
    app.mainloop()