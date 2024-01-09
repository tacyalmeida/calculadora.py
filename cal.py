from tkinter import*

#estrutura da janela
calculadora = Tk()
calculadora.title("calculadora")
calculadora.geonetry("500x4700+500+100")
calculadora.resizable(width=False, height=False)
calculadora.config(bg = "#022a3b")


#entry
campoNUmeros = Entry(calculadora, width=50)
campoNUmeros.place(x = 100, y = 25)

#botões
Bt1 = Button( calculadora, text="1", relief= FLAT, width=10, height=3)
Bt1.place(x = 50, y= 150)

Bt2 = Button( calculadora, text="2", relief= FLAT, width=10, height=3)
Bt2.place(x = 150, y= 150)

Bt3 = Button( calculadora, text="3", relief= FLAT, width=10, height=3)
Bt3.place(x = 250, y= 150)

Bt4 = Button( calculadora, text="4", relief= FLAT, width=10, height=3)
Bt4.place(x = 50, y= 150)

Bt5 = Button( calculadora, text="5", relief= FLAT, width=10, height=3)
Bt5.place(x = 150, y= 150)

Bt6 = Button( calculadora, text="6", relief= FLAT, width=10, height=3)
Bt6.place(x = 250, y= 150)

Bt7 = Button( calculadora, text="7", relief= FLAT, width=10, height=3)
Bt7.place(x = 50, y= 150)

Bt8 = Button( calculadora, text="8", relief= FLAT, width=10, height=3)
Bt8.place(x = 150, y= 300)

Bt9 = Button( calculadora, text="9", relief= FLAT, width=10, height=3)
Bt9.place(x = 250, y= 300)

Bt0 = Button( calculadora, text="0", relief= FLAT, width=10, height=3)
Bt0.place(x = 250, y= 300)

BtVirgula = Button( calculadora, text=",", relief= FLAT, width=10, height=3)
BtVirgula.place(x = 50, y= 375)

BtIgual = Button( calculadora, text="=", relief= FLAT, width=10, height=3)
BtIgual.place(x = 250, y= 375)

BtDivisao = Button( calculadora, text="/", relief= FLAT, width=10, height=3)
BtDivisao.place(x = 250, y= 300)

BtMutiplicacao = Button( calculadora, text="*", relief= FLAT, width=10, height=3)
BtMutiplicacao.place(x = 350, y= 225)

BtSoma = Button( calculadora, text="+", relief= FLAT, width=10, height=3)
BtSoma.place(x = 350, y= 300)

BtSubtracao = Button( calculadora, text="-", relief= FLAT, width=10, height=3)
BtSubtracao.place(x = 350, y= 375)

BtC = Button( calculadora, text="c", relief= FLAT, width=10, height=3)
BtC.place(x = 50, y= 75)

BtPorcentagem = Button( calculadora, text="%", relief= FLAT, width=10, height=3)
Bt9.place(x = 150, y= 75)

BtPotencia = Button( calculadora, text="X²", relief= FLAT, width=10, height=3)
BtPotencia.place(x = 250, y= 75)

BtRaiz = Button( calculadora, text="v", relief= FLAT, width=10, height=3)
BtRaiz.place(x = 350, y= 75)



calculadora.mainloop()
