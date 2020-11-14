import tkinter as tk
import math
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import *

#Llave de cambio de pantalla
#c = 1

#Definiendo funcion donde se crean todos los botones
def CreateWidgets():

	#Pantalla de la calculadora
	Calc_pantalla = Entry(ventana, justify = 'right', font= ("Courier 20"), textvariable=d_valor, bg = "#F9FFCB", fg= 'black')
	#Extension de la pantalla en la ventana
	Calc_pantalla.grid(row = 0, column = 0, columnspan = 6)
	
	#Botones-------------------------------------------------------------------------------------------------------------------------------------------
    #Copia posicion de funcion basica para ubicar boton
    ##boton = Button(ventana, text = '', width = 5, height = 2)
    
    #Los botones se organizan de la siguiente forma:

    ## Funcion del botone
    ## Posicion del boton

    # Botones Fila N.1 : ( 'pi', '(' , ')' , '/' , 'AC' )

	boton_pi = Button(ventana, text = 'π', width = 5, height = 2, bg = '#FFE4D9',fg = '#B64D3A', command = lambda: click_boton('math.pi'))
	boton_pi.grid(row = 1, column = 0, padx = 5, pady = 5)

	boton_parentesis1 = Button(ventana, text = '(', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('('))
	boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)

	boton_parentesis2 = Button(ventana, text = ')', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton(')'))
	boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)

	boton_division = Button(ventana, text = '÷', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('/'))
	boton_division.grid(row = 1, column = 3, padx = 5, pady = 5)

	boton_AllClear = Button(ventana, text = 'AC', width = 5, height = 2, bg = '#baffc9',fg = '#602F44', command = allclearEntry)
	boton_AllClear.grid(row = 1, column = 4, padx = 5, pady = 5)

    # Botones Fila N.2 : ( 'e' , '^' , '√' , '%' , 'C' )

	boton_euler = Button(ventana, text = 'e', width = 5, height = 2, bg = '#FFE4D9',fg = '#B64D3A', command = lambda: click_boton('math.e'))
	boton_euler.grid(row = 2, column = 0, padx = 5, pady = 5)

	boton_elevar = Button(ventana, text = '^', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('**'))
	boton_elevar.grid(row = 2, column = 1, padx = 5, pady = 5)

	boton_raiz = Button(ventana, text = '√', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('math.sqrt('))
	boton_raiz.grid(row = 2, column = 2, padx = 5, pady = 5)

	boton_residuo = Button(ventana, text = '%', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('%'))
	boton_residuo.grid(row = 2, column = 3, padx = 5, pady = 5)

	boton_Clear = Button(ventana, text = '⌫', width = 5, height = 2, bg = '#baffc9',fg = '#602F44', command = clearEntry)
	boton_Clear.grid(row = 2, column = 4, padx = 5, pady = 5)

    # Botones Fila N.3 : ( '7' , '8' , '9' , '*' )

	boton7 = Button(ventana, text = '7', width = 5, height = 2, command = lambda: click_boton(7))
	boton7.grid(row = 3, column = 0, padx = 5, pady = 5)

	boton8 = Button(ventana, text = '8', width = 5, height = 2, command = lambda: click_boton(8))
	boton8.grid(row = 3, column = 1, padx = 5, pady = 5)

	boton9 = Button(ventana, text = '9', width = 5, height = 2, command = lambda: click_boton(9))
	boton9.grid(row = 3, column = 2, padx = 5, pady = 5)

	boton_multiplicacion = Button(ventana, text = '×', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('*'))
	boton_multiplicacion.grid(row = 3, column = 3, padx = 5, pady = 5)

    # Botones Fila N.4 : ( '4' , '5' , '6' , '+' , 'CambioFG' )

	boton4 = Button(ventana, text = '4', width = 5, height = 2, command = lambda: click_boton(4))
	boton4.grid(row = 4, column = 0, padx = 5, pady = 5)

	boton5 = Button(ventana, text = '5', width = 5, height = 2, command = lambda: click_boton(5))
	boton5.grid(row = 4, column = 1, padx = 5, pady = 5)

	boton6 = Button(ventana, text = '6', width = 5, height = 2, command = lambda: click_boton(6))
	boton6.grid(row = 4, column = 2, padx = 5, pady = 5)

	boton_suma = Button(ventana, text = '+', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('+'))
	boton_suma.grid(row = 4, column = 3, padx = 5, pady = 5)

	boton_cambiofg = Button(ventana, text = '🔘', width = 5, height = 2, bg = '#6F5A62' ,fg = 'white', command = CambioFG)
	boton_cambiofg.grid(row = 4, column = 4, padx = 5, pady = 5)		

    # Botones Fila N.5 : ( '1' , '2' , '3' , '-' , 'ConsejoUso' )

	boton1 = Button(ventana, text = '1', width = 5, height = 2, command = lambda: click_boton(1))
	boton1.grid(row = 5, column = 0, padx = 5, pady = 5)

	boton2 = Button(ventana, text = '2', width = 5, height = 2, command = lambda: click_boton(2))
	boton2.grid(row = 5, column = 1, padx = 5, pady = 5)

	boton3 = Button(ventana, text = '3', width = 5, height = 2, command = lambda: click_boton(3))
	boton3.grid(row = 5, column = 2, padx = 5, pady = 5)

	boton_resta = Button(ventana, text = '-', width = 5, height = 2, bg = '#B8DB1B', fg = '#572D15', command = lambda: click_boton('-'))
	boton_resta.grid(row = 5, column = 3, padx = 5, pady = 5)

	boton_consejo = Button(ventana, text = '❓', width = 5, height = 2, bg = '#6F5A62' ,fg = 'white', command = ConsejoUso)
	boton_consejo.grid(row = 5, column = 4, padx = 5, pady = 5)	

    # Botones Fila N.6 : ( '0' , '.' , '=' , '⚙' )

	boton0 = Button(ventana, text = '0', width = 16, height = 2, command = lambda: click_boton(0))
	boton0.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)

	boton_punto = Button(ventana, text = '.', width = 5, height = 2, command = lambda: click_boton('.'))
	boton_punto.grid(row = 6, column = 2, padx = 5, pady = 5)
       
	boton_igual = Button(ventana, text = '=', width = 5, height = 2, bg = '#FFB447', fg= 'white', command = CalcularResultado)
	boton_igual.grid(row = 6, column = 3, padx = 5, pady = 5)

	boton_config = Button(ventana, text = '🎴', width = 5, height = 2, bg = '#6F5A62' ,fg = 'white', command = ColorChooser)
	boton_config.grid(row = 6, column = 4, padx = 5, pady = 5)

#FinBotones----------------------------------------------------------------------------------------------------------------------------


#Funcinoes-----------------------------------------------------------------------------------------------------------------------------

#Funcion que toma el valor que fue seleccionado con el click

def click_boton(c_entrada):
	global c_expresion
	c_expresion += str(c_entrada)
	d_valor.set(c_expresion)

#Funcion que evalua el str() con la funcion eval() la cual toma de manera "literal" los signos

def CalcularResultado():
	global c_expresion
	resultado = eval(c_expresion)
	d_valor.set(resultado)

#Funcion que limpia toda las entradas ingresadas en pantalla

def allclearEntry():
	global c_expresion
	c_expresion = ''
	d_valor.set(c_expresion)

#Funcion que elimina el ultimo dato ingresado

def clearEntry():
	global c_expresion, d_valor
	valor_despejado =  d_valor.get()[:-1]
	c_expresion = valor_despejado
	d_valor.set(c_expresion)

#Funcion que activa 'ColorChooser'. Permite elegir el color del fondo

def ColorChooser():
	background_color = colorchooser.askcolor()[1]
	ventana.configure(background = background_color)

#Funcion que activa la 'Messagebox'. Brinda consejo para evitar no recibir respuesta

def ConsejoUso():
	messagebox.showinfo("Consejos de uso", '¡Ten cuidado con los paréntesis! \nCalculadora esta chikita y se confunde. >:(')

#Funcion que utiliza a 'c' como llave de entrada para distinguir el estado de la pantalla de la calculadora y cambiar sus colores base

def CambioFG():
	global Calc_pantalla
	global c

	if c == 1:
		Calc_pantalla = Entry(ventana, justify = 'right', font= ("Courier 20"), textvariable=d_valor, bg = "black", fg= 'white')
		Calc_pantalla.grid(row = 0, column = 0, columnspan = 6)
		c -= 1
	else:
		Calc_pantalla = Entry(ventana, justify = 'right', font= ("Courier 20"), textvariable=d_valor, bg = "#F9FFCB", fg= 'black')
		Calc_pantalla.grid(row = 0, column = 0, columnspan = 6)
		c += 1


#Llave de cambio de pantalla
c = 1

#Primeros pasos para iniciar ventana-----------------------------------------------------------------------------------------------------------------
ventana = tk.Tk()
# Titulo de ventana 
ventana.title("soɹǝɯúNɐpǝnQoƃl∀")
# Bloqueo para evitar deformar la venta
ventana.resizable(False, False)
#Primera asignacion de color al fondo de la calculadora
ventana.configure(background =  '#DEFDE0')

#Se le asigna por primera vez el valor al texto de la pantalla
d_valor = StringVar()
c_expresion = ''

#Inicializacion de ventana
CreateWidgets()

ventana.mainloop()

#Referencias

#[1]
#CodeWithSK, “PYTHON SCRIPT TO CREATE A SIMPLE GUI CALCULATOR & PERFORM THE CALCULATION USING eval() METHOD,” YouTube. 12-Oct-2020 [Online]. Available: https://www.youtube.com/watch?v=LfbrhSi8itc&ab_channel=CodeWithSK. [Accessed: 12-Nov-2020]

#[2]
#“SchemeColor.com: Download, create & share beautiful color combinations,” Schemecolor.com, 2020. [Online]. Available: https://www.schemecolor.com/. [Accessed: 14-Nov-2020]

#[3]
#M. Coding, “Codemy.com,” YouTube. 2020 [Online]. Available: https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw. [Accessed: 14-Nov-2020]