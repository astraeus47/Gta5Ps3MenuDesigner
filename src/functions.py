from src.settings import *

def GetSafezoneSizeHalved():
    safeZoneSizeX = app_width * 0.9 / 2
    safeZoneSizeY = app_height * 0.9 / 2
    return safeZoneSizeX, safeZoneSizeY

def SetMenuPosition():
    safeZoneSizeX, safeZoneSizeY = GetSafezoneSizeHalved()

    if leftSided == 1:
        MenuXCoord3 = int(app_width * 0.6136) - safeZoneSizeX
        return MenuXCoord3
    else:
        MenuXCoord3 = int(app_width * 0.3864) + safeZoneSizeX
        return MenuXCoord3

# void SetMenuPosition(bool LeftSided)
# {
# 	if (LeftSided)
# 	{
# 		MenuXCoord1 = 0.5061f - GetSafezoneSizeHalved();
# 		MenuXCoord2 = 0.7211f - GetSafezoneSizeHalved();
# 		MenuXCoord3 = 0.6136f - GetSafezoneSizeHalved();
# 	}
# 	else
# 	{
# 		MenuXCoord1 = 0.2789f + GetSafezoneSizeHalved();
# 		MenuXCoord2 = 0.4939f + GetSafezoneSizeHalved();
# 		MenuXCoord3 = 0.3864f + GetSafezoneSizeHalved();
# 	}
# }

def CenterText(text, font_size, setMenuXCoord3, titleYCoord):
    rect_width = int(app_width * 0.2250)
    rect_height = int(app_height * 0.09) / 2

    # Correções para centralizar o texto no eixo X.
    str_count = len(text)
    text_x = (str_count * 10) / 2
    newTitleXCoord = setMenuXCoord3 + (rect_width / 2) - text_x

    # Correções para centralizar o texto no eixo Y.
    text_y = font_size / 2
    rect_y = titleYCoord - 14
    newTitleYCoord = rect_y + rect_height - text_y

    return newTitleXCoord, newTitleYCoord

class DrawText(customtkinter.CTkLabel):
    def __init__(self, master, text, font, fg_color):
        super().__init__(
            master,
            font = font,
            text = text,
            fg_color = '#e50000',
            text_color = fg_color,
            justify = 'center'
        )

def DrawImage(img_path, width, height):
    set_draw_image = customtkinter.CTkImage(
        dark_image = Image.open(img_path),
        size = (width, height)
    )
    return set_draw_image

class DrawRect(customtkinter.CTkFrame):
    def __init__(self, master, width, height, fg_color, img_path, setMenuXCoord3, backgroundYCoord):
        super().__init__(
            master,
            width = width,
            height = height,
            fg_color = fg_color,
            corner_radius = 0
        )
        if img_path != '':
            get_draw_img = DrawImage(img_path, width, height)
            set_draw_img = customtkinter.CTkLabel(master, image = get_draw_img, text = '')
            set_draw_img.place(x = setMenuXCoord3, y = backgroundYCoord)