import wx


class Example(wx.Frame):
    numbers = ""

    def operations(self, lst):
        def addition(x,y):
            total = float(x) + float(y)
            total = str(total)
            self.display.WriteText(total)
            return (str(total))

        def subtraction(x,y):
            total = float(x) - float(y) # Store sum of x and y in "total"
            total = str(total)
            self.display.WriteText(total)
            return (str(total)) # Return the amount of total

        def multiplication(x,y):
            i = 0 # total
            ii = 0 # Counter
            while int(ii) < int(y): # Loops ii until it is equal to y ( the amount of groups x is being put into)
                i += int(x) # i = x(input) + i(0). It counts the amount of times the loop is run
                ii += 1 # ii = ii(0) + 1 ; ii = 1 (ii will be the total returned)
                #if ii == y: # if ( and when) the value of i is equal to y
            i = str(i)
            self.display.WriteText(i)
            return (str(float(i))) # return i (the total)

        def division(dividend,divisor):
            dividend = float(dividend)
            divisor = float(divisor)
            if divisor == 0:
                self.display.WriteText("Error. Not Real Number")
            if dividend < 0 and divisor < 0:
                sign = 1
            elif dividend < 0 and divisor > 0:
                sign = -1
            elif dividend > 0 and divisor < 0:
                sign = -1
            else:
                sign = 1
            dividend = abs(dividend)
            divisor = abs(divisor)
            quotient = 0
            while divisor <= dividend:
                dividend -= divisor
                quotient += 1

            quotient = sign * quotient
            quotient = str(quotient)
            self.display.WriteText(quotient)

        def power(number,exponent):

            if exponent == 0:
                total = '1'
                self.display.WriteText(total)
            if exponent == 1:
                number = str(number)
                self.display.WriteText(number)
            if number < 0:
                if abs(exponent) % 2 == 0:
                    number = abs(number)
                elif abs(exponent) % 2 != 0:
                    number = abs(number)
                    sign = -1
            else:
                sign = 1



            if exponent < 0:
                exponent = abs(exponent)
                increment = number
                total = number
                fraction = '/'

                for i in range(1,exponent):
                    for x in range(1,number):
                        total += increment
                    increment = total
                total = sign * total
                total = '1' + fraction + str(total)
                self.diplay.WriteText(total)


            elif exponent > 1:
                increment = number
                total = number
                for i in range(1,exponent):
                    for x in range(1,number):
                        total += increment
                    increment = total
                total = sign * total
                total = str(total)

                self.display.WriteText(total)


        def base2_to_base8 (base_2):

             if '.' not in base_2:
                 base_2 = base_2 + '.000'

             [num_bef_dec, num_after_dec] = base_2.split(".")

             for i in num_bef_dec:
                 i = int(i)
                 if i > 1:
                     self.display.WriteText("Error")

             for i in num_after_dec:
                 i = int(i)
                 if i >1:
                     self.display.WriteText("Error")

             [num_bef_dec, num_after_dec] = base_2.split(".")
             print (num_bef_dec)
             print (num_after_dec)
             output = ""
             output_1 = ""
             count = 0
             side_a = len(num_bef_dec)
             print (side_a)
             side_b = len(num_after_dec)
             print (side_b)

             if side_a % 3 == 1:
                 num_bef_dec = num_bef_dec[::-1] + "00"
                 num_bef_dec = num_bef_dec[::-1]
                 print (num_bef_dec)
             elif side_a % 3 == 2:
                 num_bef_dec = num_bef_dec[::-1] + "0"
                 num_bef_dec = num_bef_dec[::-1]
             if side_b % 3 == 1:
                num_after_dec = num_after_dec + "00"
             elif side_b % 3 == 2:
                num_after_dec = num_after_dec + "0"

             for index in range(0, side_a, 3):
                 cur_group = num_bef_dec[index:index+3]

                 if cur_group == "000":
                     output = output + "0"
                 elif cur_group == "001":
                     output = output + "1"
                 elif cur_group == "010":
                     output = output + "2"
                 elif cur_group == "011":
                     output = output + "3"
                 elif cur_group == "100":
                     output = output + "4"
                 elif cur_group == "101":
                     output = output + "5"
                 elif cur_group == "110":
                     output = output + "6"
                 elif cur_group == "111":
                     output = output + "7"

             for index in range(0,side_b, 3):
                  cur_group = num_after_dec[index: index + 3]

                  if cur_group == "000":
                     output_1 = output_1 + "0"
                  elif cur_group == "001":
                     output_1 == output_1 + "1"
                  elif cur_group == "010":
                     output_1 = output_1 + "2"
                  elif cur_group == "011":
                     output_1 = output_1 + "3"
                  elif cur_group == "100":
                     output_1 = output_1 + "4"
                  elif cur_group == "101":
                     output_1 = output_1 + "5"
                  elif cur_group == "110":
                     output_1 = output_1 + "6"
                  elif cur_group == "111":
                     output_1 = output_1 + "7"
             total = output + '.' + output_1
             self.display.WriteText(total)

        def base2_to_base6 (base_2):
            if '.' not in base_2:
                base_2 = base_2 + '.0000'

            [num_bef_dec, num_after_dec] = base_2.split(".")
            for i in num_bef_dec:
                i = int(i)
                if i > 1:
                    self.display.WriteText("Error")

            for i in num_after_dec:
                i = int(i)
                if i >1:
                    self.display.WriteText("Error")

            output = ""
            output_1 = ""
            count = 0
            side_a = len(num_bef_dec)
            print (side_a)
            side_b = len(num_after_dec)
            print (side_b)

            if side_a % 4 == 1:
                num_bef_dec = num_bef_dec[::-1] + "000"
                num_bef_dec = num_bef_dec[::-1]
                print (num_bef_dec)
            elif side_a % 4 == 2:
                num_bef_dec = num_bef_dec[::-1] + "00"
                num_bef_dec = num_bef_dec[::-1]
            elif side_a % 4 == 3:
                num_bef_dec = num_bef_dec[::-1] + "0"
                num_bef_dec = num_bef_dec[::-1]

            if side_b % 4 == 1:
                num_after_dec = num_after_dec + "000"

            elif side_b % 4 == 2:
                num_after_dec = num_after_dec + "00"

            elif side_b % 4 == 3:
                num_after_dec = num_after_dec + "0"


            for index in range(0, side_a, 4):
                cur_group = num_bef_dec[index:index+4]

                if cur_group == "0000":
                    output = output + "0"
                elif cur_group == "0001":
                    output = output + "1"
                elif cur_group == "0010":
                    output = output + "2"
                elif cur_group == "0011":
                    output = output + "3"
                elif cur_group == "0100":
                    output = output + "4"
                elif cur_group == "0101":
                    output = output + "5"
                elif cur_group == "0110":
                    output = output + "6"
                elif cur_group == "0111":
                    output = output + "7"
                elif cur_group == "1000":
                    output =output + "8"
                elif cur_group == "1001":
                    output = output + "9"
                elif cur_group == "1010":
                    output = output + "A"
                elif cur_group == "1011":
                    output = output + "B"
                elif cur_group == "1100":
                    output = output + "C"
                elif cur_group == "1101":
                    output = output + "D"
                elif cur_group == "1110":
                    output = output + "E"
                elif cur_group == "1111":
                    output = output + 'F'

            for index in range(0, side_b, 4):
                cur_group = num_after_dec[index:index+4]

                if cur_group == "0000":
                    output_1 = output_1 + "0"
                elif cur_group == "0001":
                    output_1 = output_1 + "1"
                elif cur_group == "0010":
                    output_1 = output_1 + "2"
                elif cur_group == "0011":
                    output_1 = output_1 + "3"
                elif cur_group == "0100":
                    output_1 = output_1 + "4"
                elif cur_group == "0101":
                    output_1 = output_1 + "5"
                elif cur_group == "0110":
                    output_1 = output_1 + "6"
                elif cur_group == "0111":
                    output_1 = output_1 + "7"
                elif cur_group == "1000":
                    output_1 =output_1 + "8"
                elif cur_group == "1001":
                    output_1 = output_1 + "9"
                elif cur_group == "1010":
                    output_1 = output_1 + "A"
                elif cur_group == "1011":
                    output_1 = output_1 + "B"
                elif cur_group == "1100":
                    output_1 = output_1 + "C"
                elif cur_group == "1101":
                    output_1 = output_1 + "D"
                elif cur_group == "1110":
                    output_1 = output_1 + "E"
                elif cur_group == "1111":
                    output_1 = output_1 + 'F'
            total = output + '.' + output_1
            self.display.WriteText(total)

        def base2_to_base10(base_2):
            print (base_2)
            if '.' not in base_2:
                base_2 = base_2 + '.0'

            [num_bef_dec,num_after_dec] = base_2.split('.')

            for i in num_bef_dec:
                i = int(i)
                if i > 1:
                    self.display.WriteText("Error")

            for i in num_after_dec:
                i = int(i)
                if i >1:
                    self.display.WriteText("Error")

            output = 0
            output_1 = 0
            count = 0
            count_2 = -1
            for i in num_bef_dec:
                if i == '1':
                    i = 2 ** count
                    print(i)
                    output += i
                count += 1
            for i in num_after_dec:
                if i == '1':
                    i = 2 ** count_2
                    print(i)
                    output_1 += i
                count_2 -= 1
            output_1 = str(output_1)
            output_1 = output_1.replace(output_1[0],'')
            total = str(output) + str(output_1)
            self.display.WriteText(total)

        if '+' in lst:
            lst = lst.split("+")
            addition(float(lst[0]),float(lst[-1]))

        elif '-' in lst:
            lst = lst.split("-")
            subtraction(float(lst[0]),float(lst[-1]))

        elif '*' in lst:
            lst = lst.split("*")
            multiplication(float(lst[0]),float(lst[-1]))

        elif '/' in lst:
            lst = lst.split("/")
            division(float(lst[0]),float(lst[-1]))

        elif '^' in lst:
            lst = lst.split("^")
            power(int(lst[0]),int(lst[-1]))

        elif "bin_to_oct" in lst:
            lst = lst.replace("bin_to_oct", '')
            base2_to_base8(lst)
        elif "bin_to_hex" in lst:
            lst = lst.replace("bin_to_hex",'')
            base2_to_base6(lst)
        elif "bin_to_dec" in lst:
            lst = lst.replace("bin_to_dec",'')
            base2_to_base10(lst)


    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()


    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        btn_bck = (wx.Button(self,label = 'Bck'))
        btn_clear = (wx.Button(self, label = 'Clear'))
        btn_exponent = (wx.Button(self,label = "^"))
        btn_7 =(wx.Button(self, label='7'))
        btn_8 =(wx.Button(self, label='8'))
        btn_9 = (wx.Button(self, label='9'))
        btn_add = (wx.Button(self, label='+'))
        btn_4=(wx.Button(self, label='4'))
        btn_5=(wx.Button(self, label='5'))
        btn_6=(wx.Button(self, label='6'))
        btn_divide=(wx.Button(self, label='/'))
        btn_1 = (wx.Button(self, label='1'))
        btn_2 = (wx.Button(self, label='2'))
        btn_3 = (wx.Button(self, label='3'))
        btn_multiply = (wx.Button(self, label='*'))
        btn_0 = (wx.Button(self, label='0'))
        btn_decimal = (wx.Button(self, label='.'))
        btn_subtract = (wx.Button(self, label='-'))
        btn_bin_to_hex = (wx.Button(self, label='bin to hex'))
        btn_bin_to_oct = (wx.Button(self, label='bin to oct'))
        btn_bin_to_dec = (wx.Button(self, label='bin to dec'))
        btn_equals = (wx.Button(self, label='='))

        self.Bind(wx.EVT_BUTTON,self.OnButtonClear, btn_clear)
        self.Bind(wx.EVT_BUTTON, self.OnButtonBck, btn_bck)
        self.Bind(wx.EVT_BUTTON, self.OnButton7, btn_7)
        self.Bind(wx.EVT_BUTTON, self.OnButton8, btn_8)
        self.Bind(wx.EVT_BUTTON, self.OnButton9, btn_9)
        self.Bind(wx.EVT_BUTTON, self.OnButtonadd, btn_add)
        self.Bind(wx.EVT_BUTTON, self.OnButton4, btn_4)
        self.Bind(wx.EVT_BUTTON, self.OnButton5, btn_5)
        self.Bind(wx.EVT_BUTTON, self.OnButton6, btn_6)
        self.Bind(wx.EVT_BUTTON, self.OnButtondivide, btn_divide)
        self.Bind(wx.EVT_BUTTON, self.OnButton1, btn_1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2, btn_2)
        self.Bind(wx.EVT_BUTTON, self.OnButton3, btn_3)
        self.Bind(wx.EVT_BUTTON, self.OnButtonmultiply, btn_multiply)
        self.Bind(wx.EVT_BUTTON, self.OnButton0, btn_0)
        self.Bind(wx.EVT_BUTTON, self.OnButtondecimal,btn_decimal)
        self.Bind(wx.EVT_BUTTON, self.OnButtonsubtract,btn_subtract)
        self.Bind(wx.EVT_BUTTON, self.OnButtonequals,btn_equals)
        self.Bind(wx.EVT_BUTTON, self.OnButtonbin_to_dec, btn_bin_to_dec)
        self.Bind(wx.EVT_BUTTON, self.OnButtonbin_to_oct, btn_bin_to_oct)
        self.Bind(wx.EVT_BUTTON, self.OnButtonbin_to_hex, btn_bin_to_hex)
        self.Bind(wx.EVT_BUTTON, self.OnButtonExponent, btn_exponent)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(6, 4, 5, 5)
        gs.AddMany( [(btn_clear,0,wx.EXPAND),
            (btn_bck, 1, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (btn_exponent, 1, wx.EXPAND),
            (btn_7, 1, wx.EXPAND),
            (btn_8, 1, wx.EXPAND),
            (btn_9, 1, wx.EXPAND),
            (btn_add, 1, wx.EXPAND),
            (btn_4, 1, wx.EXPAND),
            (btn_5, 1, wx.EXPAND),
            (btn_6, 1, wx.EXPAND),
            (btn_divide, 1, wx.EXPAND),
            (btn_1, 1, wx.EXPAND),
            (btn_2, 1, wx.EXPAND),
            (btn_3, 1, wx.EXPAND),
            (btn_multiply, 1, wx.EXPAND),
            (btn_0, 1, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (btn_decimal, 1, wx.EXPAND),
            (btn_subtract, 1, wx.EXPAND),
            (btn_bin_to_dec, 1, wx.EXPAND),
            (btn_bin_to_oct, 1, wx.EXPAND),
            (btn_bin_to_hex, 1, wx.EXPAND),
            (btn_equals, 1, wx.EXPAND)]),



        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


    def list_to_string (self, lst):
        count = 0
        string = ""
        while count < len(lst) - 1:
            print (string)
            string += lst[count]
            count += 1
        return string


    def OnButtonClear(self,event):
        self.numbers = ''
        self.display.Clear()


    def OnButtonBck(self,event):
        self.numbers = (self.list_to_string(self.numbers))
        self.display.Clear()
        self.display.WriteText(self.numbers)

    def OnButton7(self,event):
        self.display.WriteText("7")
        self.numbers += ("7")

    def OnButton8(self,event):
        self.display.WriteText("8")
        self.numbers += ("8")
        print (self.numbers)

    def OnButton9(self,event):
        self.display.WriteText("9")
        self.numbers += ("9")

    def OnButtonadd(self,event):
        self.display.WriteText("+")
        self.numbers += ("+")
        print (self.numbers)

    def OnButton4(self,event):
        self.display.WriteText("4")
        self.numbers += ("4")

    def OnButton5(self,event):
        self.display.WriteText("5")
        self.numbers += ("5")

    def OnButton6(self,event):
        self.display.WriteText("6")
        self.numbers += ("6")

    def OnButtondivide(self,event):
        self.display.WriteText("/")
        self.numbers += ('/')

    def OnButton1(self,event):
        self.display.WriteText("1")
        self.numbers += ('1')

    def OnButton2(self,event):
        self.display.WriteText("2")
        self.numbers += ('2')

    def OnButton3(self,event):
        self.display.WriteText("3")
        self.numbers += ('3')

    def OnButtonmultiply(self,event):
        self.display.WriteText("*")
        self.numbers += ('x')

    def OnButton0(self,event):
        self.display.WriteText("0")
        self.numbers += ('0')

    def OnButtondecimal(self,event):
        self.display.WriteText(".")
        self.numbers += ('.')

    def OnButtonsubtract(self,event):
        self.display.WriteText("-")
        self.numbers += ('-')

    def OnButtonExponent(self,event):
        self.display.WriteText("^")
        self.numbers += ('^')

    def OnButtonequals(self,event):
        self.display.WriteText("=")
        print (self.numbers)
        self.operations(self.numbers)

    def OnButtonbin_to_dec(self,event):
        self.numbers += ("bin_to_dec")
        self.display.WriteText("bin_to_dec")

    def OnButtonbin_to_oct(self,event):
        self.numbers += ("bin_to_oct")
        self.display.WriteText("bin_to_oct")

    def OnButtonbin_to_hex(self,event):
        self.numbers += ("bin_to_hex")
        self.display.WriteText("bin_to_hex")



def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
