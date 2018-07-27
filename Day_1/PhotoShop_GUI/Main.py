from PIL import Image
from PIL import ImageFilter
import wx

class Example(wx.Frame):
    def INIT_UI(self):

        btn_invert = (wx.Button(self,label = "Invert"))
        btn_gray_scale = (wx.Button(self,label = "Black And White"))
        btn_posterize = (wx.Button(self, label = "Posterize"))
        btn_solarize = (wx.Button(self, label = 'Solarize' ))
        btn_darken = (wx.Button(self, label = 'Darken'))
        btn_brighten = (wx.Button(self, label = 'Brigten'))
        btn_crop = (wx.Button(self, label = 'Crop'))
        btn_blur = (wx.Button(self, label = 'blur'))
        btn_sharpen -(wx.Button(self, label = 'Darken')

        self.Bind(wx.EVT_BUTTON(self.OnButtonInvert, btn_invert))
        self.Bind(wx.EVT_BUTTON(self.OnButtonGrayScale, btn_gray_scale))
        self.Bind(wx.EVT_BUTTON(self.OnButtonPosterize, btn_posterize))
        self.Bind(wx.EVT_BUTTON(self.OnButtonSolarize, btn_solarize))
        self.Bind(wx.EVT_BUTTON(self.OnButtonDarken, btn_darken))
        self.Bind(wx.EVT_BUTTON(self.OnButtonBrighten, btn_brighten))
        self.Bind(wx.EVT_BUTTON(self.OnButtonCrop, btn_crop))
        self.Bind(wx.EVT_BUTTON(self.OnButtonBlur, btn_blur))
        self.Bind(wx.EVT_BUTTON(self.OnButtonSharpen, btn_sharpen))

    def OnButtonInvert(self,event):
        self.load_and_go(input_filename,invert)
        invert(pixel)

    def OnButtonGrayScale(self,event):
        self.load_and_go(input_filename,gray_scale)
        gray_scale(pixel)

    def OnButtonPosterize(self,event):
        self.load_and_go(input_filename,posterize)
        posterize(pixel)

    def OnButtonSolarize(self,event):
        self.load_and_go(input_filename,solarize)
        solarize(pixel)

    def OnButtonDarken(self,event):
        self.load_and_go(input_filename,darken)
        darken(pixel)

    def OnButtonBrighten(self,event):
        self.load_and_go(input_filename,brighten)
        brighten(pixel)

    def OnButtonCrop(self,event):
        crop(image)

    def OnButtonBlur(self,event):
        self.load_and_go(input_filename,invert)
        blur(image)

    def OnButtonSharpen(self,event):
        sharpen(image)
