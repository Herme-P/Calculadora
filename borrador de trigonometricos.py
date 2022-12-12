from tkinter import *
from tkinter import ttk
from CalculadoraBasica import *
import numpy as np

cal = CalculadoraBasica()
contador = 0 ; contadorOP = 0; contadorPunto=0; contador2nd=0; operacion=""; abrirParen=False;

class App:
    def __init__(self, master):
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure('miframe.TFrame', background="black")
        self.miframe = ttk.Frame(master, style="miframe.TFrame", padding=5)
        self.miframe.grid(column=0, row=0, sticky=(W, N, E, S))
        self.miframe.columnconfigure(0, weight=1)
        self.miframe.columnconfigure(1, weight=1)
        self.miframe.columnconfigure(2, weight=1)
        self.miframe.columnconfigure(3, weight=1)
        self.miframe.rowconfigure(0, weight=1)
        self.miframe.rowconfigure(1, weight=1)
        self.miframe.rowconfigure(2, weight=1)
        self.miframe.rowconfigure(3, weight=1)

        #estilos
        self.estilos_entrada1 = ttk.Style()
        self.estilos_entrada1.configure('entrada1.TLabel', font="arial 15", anchor="e", background="#0A0A0A", foreground='white')
        self.estilos_entrada2 = ttk.Style()
        self.estilos_entrada2.configure('entrada2.TLabel', font="arial 38", anchor="e", background="#0A0A0A", foreground='white')
        self.estilos_botones_numeros = ttk.Style()
        self.estilos_botones_numeros.configure('BotonesNum.TButton', font='arial 13', width=6, background='#373737', foreground='white', relief="flat")
        self.estilos_botones_numeros.map('BotonesNum.TButton', background=[('active', 'black')])
        self.estilos_botones_igual = ttk.Style()
        self.estilos_botones_igual.configure('Botonesigual.TButton', font='arial 13', width=6, background='#85929E', foreground='black', relief="flat")
        #-estilos

        self.entrada1_ = StringVar()
        self.entrada1 = ttk.Label(self.miframe,textvariable=self.entrada1_, style='entrada1.TLabel')
        self.entrada1.grid(column=0, row=1, columnspan=5, sticky=(W, N, E, S))

        self.entrada2_ = StringVar(value="0")
        self.entrada2 = ttk.Label(self.miframe,textvariable=self.entrada2_, style='entrada2.TLabel')
        self.entrada2.grid(column=0, row=2, columnspan=5, sticky=(W, N, E, S))

raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("imagenes/logo.ico")
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)
raiz.config(background='black')

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)
estandar = Menu(barraMenu, tearoff=0)
estandar.add_command(label='Estándar', command=lambda: Estandar())
estandar.add_command(label='ED', command=lambda: ED())
estandar.add_command(label='Científica', command=lambda: Cientifica())
estandar.config(background='black', foreground='white',font='arial 12',  relief="flat")
barraMenu.add_cascade(label='|||| Menú', menu=estandar)

def Estandar():
    aplicacion = App(raiz)
    #funciones
    def numeroPulsado(numero):
        global contador, contadorPunto
        
        if contador == 0:
            aplicacion.entrada2_.set("")
            aplicacion.entrada2_.set(aplicacion.entrada2_.get()+numero)
            contador = 1
        else:
            aplicacion.entrada2_.set(aplicacion.entrada2_.get()+numero) 
        if contadorPunto==1:
            aplicacion.entrada1_.set(aplicacion.entrada1_.get()+numero) 
            print(aplicacion.entrada1_.get())

    def Operaciones(oper):
        global contador, operacion, contadorOP, contadorPunto
        
        if contadorOP == 0:
            aplicacion.entrada1_.set(aplicacion.entrada2_.get()+" "+ oper)
            cal.valor1 = float(aplicacion.entrada2_.get() )
            aplicacion.entrada2_.set(cal.MostrarResultado())
            contador = 0
            operacion = oper
            contadorOP += 1
        else:
            if contadorPunto==1:
                cal.valor1 = eval(aplicacion.entrada1_.get())
            else:
                cal.valor1 = eval(aplicacion.entrada1_.get()+aplicacion.entrada2_.get() )
            aplicacion.entrada1_.set(str(cal.valor1)+' '+oper)
            aplicacion.entrada2_.set('0')
            contador = 0
            operacion = oper
            contadorOP += 1
        contadorPunto = 0  

    def Resultados():
        global contador, operacion, contadorOP, contadorPunto  
        cal.valor2 = float(aplicacion.entrada2_.get())
        if operacion == '+':
            cal.sumar()
        elif operacion == '-':
            cal.restar()
        elif operacion == '*':
            cal.multiplicar()
        elif operacion == '/':
            cal.dividir()

        if contadorPunto == 1:
            aplicacion.entrada1_.set(str(cal.valor1)+' + '+str(cal.valor2))    
        else:
            aplicacion.entrada1_.set(aplicacion.entrada1_.get()+" "+aplicacion.entrada2_.get())
        
        aplicacion.entrada2_.set(cal.MostrarResultado()) 
        contador = 0; contadorOP = 0; contadorPunto = 0

    def Punto():
        global contadorPunto, contadorOP, contador
        if contadorPunto == 0 :
            if contador == 0:
                aplicacion.entrada2_.set('0.')
                aplicacion.entrada1_.set('0.')
                
            else:
                if contadorOP >= 1:
                    aplicacion.entrada1_.set(aplicacion.entrada1_.get()+aplicacion.entrada2_.get()+'.') 
                    aplicacion.entrada2_.set(aplicacion.entrada2_.get()+'.')  
                else:
                    aplicacion.entrada1_.set(aplicacion.entrada2_.get()+'.') 
                    aplicacion.entrada2_.set(aplicacion.entrada1_.get()) 
        
        contadorPunto+=1
    def BorrarTodo():
        global contador
        contador = 0
        aplicacion.entrada1_.set('')
        cal.valor1=0
        cal.valor2=0
        cal.resultado=0
        aplicacion.entrada2_.set('0')
    
    def BorrarUltimos():
        global contador
        contador = 0
        cal.valor2=0
        aplicacion.entrada2_.set('0')
    def BorrarUltimo():
        global contador
        contador = 0
        aplicacion.entrada2_.set(aplicacion.entrada2_.get()[:-1])
    def CuadradoX():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'**2')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def DivididoX():
        aplicacion.entrada2_.set(str(eval('1/'+aplicacion.entrada2_.get())))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def Raiz2():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'**0.5')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def Porcentaje():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'*'+aplicacion.entrada1_.get()[:-2]+'/100')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def Negacion():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'*(-1)')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    #funciones

    boton0 = ttk.Button(aplicacion.miframe, text="0", style='BotonesNum.TButton', command=lambda: numeroPulsado('0')) 
    boton1 = ttk.Button(aplicacion.miframe, text="1", style='BotonesNum.TButton', command=lambda: numeroPulsado('1')) 
    boton2 = ttk.Button(aplicacion.miframe, text="2", style='BotonesNum.TButton', command=lambda: numeroPulsado('2')) 
    boton3 = ttk.Button(aplicacion.miframe, text="3", style='BotonesNum.TButton', command=lambda: numeroPulsado('3')) 
    boton4 = ttk.Button(aplicacion.miframe, text="4", style='BotonesNum.TButton', command=lambda: numeroPulsado('4')) 
    boton5 = ttk.Button(aplicacion.miframe, text="5", style='BotonesNum.TButton', command=lambda: numeroPulsado('5')) 
    boton6 = ttk.Button(aplicacion.miframe, text="6", style='BotonesNum.TButton', command=lambda: numeroPulsado('6')) 
    boton7 = ttk.Button(aplicacion.miframe, text="7", style='BotonesNum.TButton', command=lambda: numeroPulsado('7')) 
    boton8 = ttk.Button(aplicacion.miframe, text="8", style='BotonesNum.TButton', command=lambda: numeroPulsado('8')) 
    boton9 = ttk.Button(aplicacion.miframe, text="9", style='BotonesNum.TButton', command=lambda: numeroPulsado('9')) 

    boton_Porcentaje = ttk.Button(aplicacion.miframe, text="%", style='BotonesNum.TButton', command=lambda: Porcentaje()) 
    boton_borrar = ttk.Button(aplicacion.miframe, text=chr(9003), style='BotonesNum.TButton', command=lambda: BorrarUltimo()) 
    boton_borrarTodo = ttk.Button(aplicacion.miframe, text="C", style='BotonesNum.TButton', command=lambda:BorrarTodo()) 
    boton_borrarCE = ttk.Button(aplicacion.miframe, text="CE", style='BotonesNum.TButton', command=lambda:BorrarUltimos()) 
    boton_Punto = ttk.Button(aplicacion.miframe, text=".", style='BotonesNum.TButton', command=lambda: Punto()) 
    boton_Negacion = ttk.Button(aplicacion.miframe, text="+/-", style='BotonesNum.TButton', command= lambda: Negacion())
    boton_CuadradoX = ttk.Button(aplicacion.miframe, text="X^2", style='BotonesNum.TButton', command=lambda: CuadradoX()) 
    boton_divididoX = ttk.Button(aplicacion.miframe, text="1/X", style='BotonesNum.TButton', command=lambda: DivididoX()) 
    boton_Raiz2 = ttk.Button(aplicacion.miframe, text="√", style='BotonesNum.TButton', command=lambda: Raiz2()) 

    boton_Mas = ttk.Button(aplicacion.miframe, text="+", style='BotonesNum.TButton', command=lambda: Operaciones("+")) 
    boton_Menos = ttk.Button(aplicacion.miframe, text="-", style='BotonesNum.TButton', command=lambda: Operaciones("-")) 
    boton_Multiplicar = ttk.Button(aplicacion.miframe, text="*", style='BotonesNum.TButton', command=lambda: Operaciones("*")) 
    boton_Dividir = ttk.Button(aplicacion.miframe, text=chr(247), style='BotonesNum.TButton', command=lambda: Operaciones("/")) 
    boton_Igual = ttk.Button(aplicacion.miframe, text="=", style='Botonesigual.TButton', command=lambda: Resultados()) 

    #colocar botones bisibles
    
    boton_Porcentaje.grid(column=0, row=3, sticky=(W, N, E, S))
    boton_borrarTodo.grid(column=1, row=3, sticky=(W, N, E, S))
    boton_borrarCE.grid(column=2, row=3, sticky=(W, N, E, S))
    boton_borrar.grid(column=3, row=3, sticky=(W, N, E, S))
    boton_divididoX.grid(column=0, row=4, sticky=(W, N, E, S))
    boton_CuadradoX.grid(column=1, row=4, sticky=(W, N, E, S))
    boton_Raiz2.grid(column=2, row=4, sticky=(W, N, E, S))
    boton_Dividir.grid(column=3, row=4, sticky=(W, N, E, S))
    boton7.grid(column=0, row=5, sticky=(W, N, E, S))
    boton8.grid(column=1, row=5, sticky=(W, N, E, S))
    boton9.grid(column=2, row=5, sticky=(W, N, E, S))
    boton_Multiplicar.grid(column=3, row=5, sticky=(W, N, E, S))
    boton4.grid(column=0, row=6, sticky=(W, N, E, S))
    boton5.grid(column=1, row=6, sticky=(W, N, E, S))
    boton6.grid(column=2, row=6, sticky=(W, N, E, S))
    boton_Menos.grid(column=3, row=6, sticky=(W, N, E, S))
    boton1.grid(column=0, row=7, sticky=(W, N, E, S))
    boton2.grid(column=1, row=7, sticky=(W, N, E, S))
    boton3.grid(column=2, row=7, sticky=(W, N, E, S))
    boton_Mas.grid(column=3, row=7, sticky=(W, N, E, S))
    boton_Negacion.grid(column=0, row=8, sticky=(W, N, E, S))
    boton0.grid(column=1, row=8, sticky=(W, N, E, S))
    boton_Punto.grid(column=2, row=8, sticky=(W, N, E, S))
    boton_Igual.grid(column=3, row=8, sticky=(W, N, E, S))


    for child in aplicacion.miframe.winfo_children():
        child.grid_configure(ipady=6, padx=1, pady=1)

def ED():
    aplicacion = App(raiz)
    
    
    boton0 = ttk.Button(aplicacion.miframe, text="0", style='BotonesNum.TButton',) 
    boton0.grid(column=1, row=7, sticky=(W, N, E, S))
    boton1 = ttk.Button(aplicacion.miframe, text="1", style='BotonesNum.TButton',) 
    boton1.grid(column=1, row=8, sticky=(W, N, E, S))

def Cientifica():
    aplicacion = App(raiz)
    def numeroPulsado(numero):
        global contador, contadorPunto
        
        if contador == 0:
            aplicacion.entrada2_.set("")
            aplicacion.entrada2_.set(aplicacion.entrada2_.get()+numero)
            contador = 1
        else:
            aplicacion.entrada2_.set(aplicacion.entrada2_.get()+numero) 
        if contadorPunto==1:
            aplicacion.entrada1_.set(aplicacion.entrada1_.get()+numero) 
            print(aplicacion.entrada1_.get())

    def Operaciones(oper):
        global contador, operacion, contadorOP, contadorPunto, abrirParen
        
        if contadorOP == 0 and abrirParen == False:
            aplicacion.entrada1_.set(aplicacion.entrada2_.get()+" "+ oper)
            cal.valor1 = float(eval(aplicacion.entrada2_.get()) )
            aplicacion.entrada2_.set(cal.MostrarResultado())
            contador = 0
            operacion = oper
            contadorOP += 1
        else:
            if  abrirParen == False:
                if contadorPunto==1:
                    cal.valor1 = eval(aplicacion.entrada1_.get())
                else:
                    cal.valor1 = eval(aplicacion.entrada1_.get()+aplicacion.entrada2_.get() )
                aplicacion.entrada1_.set(str(cal.valor1)+' '+oper)
                aplicacion.entrada2_.set('0')
                contador = 0
                operacion = oper
                contadorOP += 1
            else:
                aplicacion.entrada1_.set(aplicacion.entrada2_.get()+' '+oper)
                aplicacion.entrada2_.set(aplicacion.entrada1_.get())
                
        contadorPunto = 0  

    def Resultados():
        global contador, operacion, contadorOP, contadorPunto, abrirParen  
        cal.valor2 = float(str(eval(aplicacion.entrada2_.get())))
        if operacion == '+':
            cal.sumar()
        elif operacion == '-':
            cal.restar()
        elif operacion == '*':
            cal.multiplicar()
        elif operacion == '/':
            cal.dividir()

        if contadorPunto == 1:
            aplicacion.entrada1_.set(str(cal.valor1)+' + '+str(cal.valor2))    
        else:
            if abrirParen:
                aplicacion.entrada1_.set(aplicacion.entrada2_.get())
            else:
                aplicacion.entrada1_.set(aplicacion.entrada1_.get()+" "+aplicacion.entrada2_.get())
        
        if operacion=='':
            aplicacion.entrada2_.set(cal.valor2) 
        else:    
            aplicacion.entrada2_.set(cal.MostrarResultado()) 
        contador = 0; contadorOP = 0; contadorPunto = 0; abrirParen=False

    def Punto():
        global contadorPunto, contadorOP, contador
        if contadorPunto == 0 :
            if contador == 0:
                aplicacion.entrada2_.set('0.')
                aplicacion.entrada1_.set('0.')
                
            else:
                if contadorOP >= 1:
                    aplicacion.entrada1_.set(aplicacion.entrada1_.get()+aplicacion.entrada2_.get()+'.') 
                    aplicacion.entrada2_.set(aplicacion.entrada2_.get()+'.')  
                else:
                    aplicacion.entrada1_.set(aplicacion.entrada2_.get()+'.') 
                    aplicacion.entrada2_.set(aplicacion.entrada1_.get()) 
        
        contadorPunto+=1
    def BorrarTodo():
        global contador
        contador = 0
        aplicacion.entrada1_.set('')
        cal.valor1=0
        cal.valor2=0
        cal.resultado=0
        aplicacion.entrada2_.set('0')
    
    def BorrarUltimo():
        global contador
        contador = 0
        aplicacion.entrada2_.set(aplicacion.entrada2_.get()[:-1])
    def Negacion():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'*(-1)')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def Boton2nd():
        global contador2nd
        if contador2nd==0:
            boton_CuboX = ttk.Button(aplicacion.miframe, text="X^3", style='BotonesNum.TButton', command=lambda: CuboX()) 
            boton_CuboX.grid(column=0, row=5, sticky=(W, N, E, S))
            boton_Raiz3 = ttk.Button(aplicacion.miframe, text="3√x", style='BotonesNum.TButton', command=lambda: Raiz3()) 
            boton_Raiz3.grid(column=0, row=6, sticky=(W, N, E, S))
            boton_Raizx = ttk.Button(aplicacion.miframe, text="y√x", style='BotonesNum.TButton', command=lambda: 2+2) 
            boton_Raizx.grid(column=0, row=7, sticky=(W, N, E, S))
            boton_2elevadoX= ttk.Button(aplicacion.miframe, text="2^x", style='BotonesNum.TButton', command=lambda: 2+2) 
            boton_2elevadoX.grid(column=0, row=8, sticky=(W, N, E, S))
            boton_logyX= ttk.Button(aplicacion.miframe, text="logyX", style='BotonesNum.TButton', command=lambda: 2+2) 
            boton_logyX.grid(column=0, row=9, sticky=(W, N, E, S))
            boton_e_elevadoX= ttk.Button(aplicacion.miframe, text="e^x", style='BotonesNum.TButton', command=lambda: 2+2) 
            boton_e_elevadoX.grid(column=0, row=10, sticky=(W, N, E, S))
            for child in aplicacion.miframe.winfo_children():
                child.grid_configure(ipady=6, padx=1, pady=1)
            contador2nd = 1
        else:
            boton_CuadradoX = ttk.Button(aplicacion.miframe, text="X^2", style='BotonesNum.TButton', command=lambda: CuadradoX()) 
            boton_CuadradoX.grid(column=0, row=5, sticky=(W, N, E, S))
            boton_Raiz2 = ttk.Button(aplicacion.miframe, text="√", style='BotonesNum.TButton', command=lambda: Raiz2()) 
            boton_Raiz2.grid(column=0, row=6, sticky=(W, N, E, S))
            boton_XelevadoY = ttk.Button(aplicacion.miframe, text="X^y", style='BotonesNum.TButton', )
            boton_XelevadoY.grid(column=0, row=7, sticky=(W, N, E, S))
            boton_10elevadoX = ttk.Button(aplicacion.miframe, text="10^x", style='BotonesNum.TButton',)
            boton_10elevadoX.grid(column=0, row=8, sticky=(W, N, E, S))
            boton_log = ttk.Button(aplicacion.miframe, text="log", style='BotonesNum.TButton',)
            boton_log.grid(column=0, row=9, sticky=(W, N, E, S))
            boton_ln= ttk.Button(aplicacion.miframe, text="ln", style='BotonesNum.TButton',)
            boton_ln.grid(column=0, row=10, sticky=(W, N, E, S))
            for child in aplicacion.miframe.winfo_children():
                child.grid_configure(ipady=6, padx=1, pady=1)
            contador2nd = 0
        
    
    def CuadradoX():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'**2')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def CuboX():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'**3')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def Raiz2():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'**0.5')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def Raiz3():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'**(1/3)')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def DivididoX():
        aplicacion.entrada2_.set(str(eval('1/'+aplicacion.entrada2_.get())))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    def ValorAbsoluto():
        aplicacion.entrada2_.set(abs(float(aplicacion.entrada2_.get())))
        cal.valor2 = aplicacion.entrada2_.get()
    def XelevadoY():
        aplicacion.entrada2_.set(str(aplicacion.entrada2_.get()+'**'))
    def _10elevadoX(): 
        aplicacion.entrada2_.set(str(eval('10**'+aplicacion.entrada2_.get())))
        cal.valor2 = float(aplicacion.entrada2_.get())  

    def factorial():
        aplicacion.entrada2_.get()
        n_fac=np.math.factorial(float(aplicacion.entrada2_.get()))
        aplicacion.entrada2_.set(str(n_fac))
        cal.valor2 = float(aplicacion.entrada2_.get())

    def exponencial():
        # global operacion
        aplicacion.entrada2_.set(str(aplicacion.entrada2_.get()+'*10**'))
        # operacion=''

    def logaritmo():
        val=aplicacion.entrada2_.get()
        if val == '0':
            cal.valor2 = str('Match error')
            aplicacion.entrada2_.set(cal.valor2)
        else:
            x_log=np.log10(float(aplicacion.entrada2_.get()))
            aplicacion.entrada2_.set(str(x_log))
            cal.valor2 = float(aplicacion.entrada2_.get())

    def logaritmo_natural():
        val=aplicacion.entrada2_.get()
        if val == '0':
            cal.valor2 = str('Match error')
            aplicacion.entrada2_.set(cal.valor2)
        else:
            x_log=np.log(float(aplicacion.entrada2_.get()))
            aplicacion.entrada2_.set(str(x_log))
            cal.valor2 = float(aplicacion.entrada2_.get())
        

    def fun_trig(event):
        fun_trig=variableTrigonometrica.get()
        if fun_trig == 'Sen':
            val=np.sin(float(aplicacion.entrada2_.get()))
            aplicacion.entrada2_.set(str(val))
            cal.valor2 = float(aplicacion.entrada2_.get())
        elif fun_trig == 'Cos':
            val=np.cos(float(aplicacion.entrada2_.get()))
            aplicacion.entrada2_.set(str(val))
            cal.valor2 = float(aplicacion.entrada2_.get())
        else:
            val=np.tan(float(aplicacion.entrada2_.get()))
            aplicacion.entrada2_.set(str(val))
            cal.valor2 = float(aplicacion.entrada2_.get())
    
    def Funcionescal(event):
        Valor = float(aplicacion.entrada2_.get())
        if variableFunciones.get()=="RAD":
            rad1 = np.deg2rad(Valor)  
            aplicacion.entrada2_.set(str(rad1)) 
            cal.valor2 = float(aplicacion.entrada2_.get())  
        elif variableFunciones.get()=="DEG":
            deg1 = np.rad2deg(Valor)  
            aplicacion.entrada2_.set(str(deg1)) 
            cal.valor2 = float(aplicacion.entrada2_.get())   
    
    def Aparentesis():
        global abrirParen
        aplicacion.entrada2_.set(str(aplicacion.entrada2_.get()+'*('))
        abrirParen=True
    
    def Cparentesis():
        aplicacion.entrada2_.set(str(aplicacion.entrada2_.get()+')'))
   
    def Porcentaje():
        aplicacion.entrada2_.set(str(eval(aplicacion.entrada2_.get()+'*'+aplicacion.entrada1_.get()[:-2]+'/100')))
        cal.valor2 = float(aplicacion.entrada2_.get()) 
    
    variableTrigonometrica = StringVar(aplicacion.miframe, value="Trigonometría")
    trigonometricas = OptionMenu(aplicacion.miframe, variableTrigonometrica, *["Sen","Cos","Tan"], command=fun_trig)
    trigonometricas.config(background='black', foreground='white',font='arial 12',  relief="flat")
    trigonometricas.grid(column=0, row=3, sticky=(W, N, E, S))

    variableFunciones = StringVar(aplicacion.miframe, value="Función")
    Funciones = OptionMenu(aplicacion.miframe, variableFunciones, *["RAD","DEG","..."], command=Funcionescal)
    Funciones.config(background='black', foreground='white',font='arial 12',  relief="flat")
    Funciones.grid(column=1, row=3, sticky=(W, N, E, S))


    boton0 = ttk.Button(aplicacion.miframe, text="0", style='BotonesNum.TButton', command=lambda: numeroPulsado('0')) 
    boton0.grid(column=2, row=10, sticky=(W, N, E, S))
    boton1 = ttk.Button(aplicacion.miframe, text="1", style='BotonesNum.TButton', command=lambda: numeroPulsado('1')) 
    boton1.grid(column=1, row=9, sticky=(W, N, E, S))
    boton2 = ttk.Button(aplicacion.miframe, text="2", style='BotonesNum.TButton', command=lambda: numeroPulsado('2'))
    boton2.grid(column=2, row=9, sticky=(W, N, E, S)) 
    boton3 = ttk.Button(aplicacion.miframe, text="3", style='BotonesNum.TButton', command=lambda: numeroPulsado('3')) 
    boton3.grid(column=3, row=9, sticky=(W, N, E, S))
    boton4 = ttk.Button(aplicacion.miframe, text="4", style='BotonesNum.TButton', command=lambda: numeroPulsado('4')) 
    boton4.grid(column=1, row=8, sticky=(W, N, E, S))
    boton5 = ttk.Button(aplicacion.miframe, text="5", style='BotonesNum.TButton', command=lambda: numeroPulsado('5'))
    boton5.grid(column=2, row=8, sticky=(W, N, E, S)) 
    boton6 = ttk.Button(aplicacion.miframe, text="6", style='BotonesNum.TButton', command=lambda: numeroPulsado('6'))
    boton6.grid(column=3, row=8, sticky=(W, N, E, S)) 
    boton7 = ttk.Button(aplicacion.miframe, text="7", style='BotonesNum.TButton', command=lambda: numeroPulsado('7')) 
    boton7.grid(column=1, row=7, sticky=(W, N, E, S))
    boton8 = ttk.Button(aplicacion.miframe, text="8", style='BotonesNum.TButton', command=lambda: numeroPulsado('8')) 
    boton8.grid(column=2, row=7, sticky=(W, N, E, S))
    boton9 = ttk.Button(aplicacion.miframe, text="9", style='BotonesNum.TButton', command=lambda: numeroPulsado('9')) 
    boton9.grid(column=3, row=7, sticky=(W, N, E, S))

    boton_borrar = ttk.Button(aplicacion.miframe, text=chr(9003), style='BotonesNum.TButton', command=lambda: BorrarUltimo()) 
    boton_borrar.grid(column=4, row=4, sticky=(W, N, E, S))
    boton_borrarTodo = ttk.Button(aplicacion.miframe, text="C", style='BotonesNum.TButton', command=lambda:BorrarTodo()) 
    boton_borrarTodo.grid(column=3, row=4, sticky=(W, N, E, S))
    boton_Igual = ttk.Button(aplicacion.miframe, text="=", style='Botonesigual.TButton', command=lambda: Resultados()) 
    boton_Igual.grid(column=4, row=10, sticky=(W, N, E, S))
    boton_Punto = ttk.Button(aplicacion.miframe, text=".", style='BotonesNum.TButton', command=lambda: Punto()) 
    boton_Punto.grid(column=3, row=10, sticky=(W, N, E, S))
    boton_Negacion = ttk.Button(aplicacion.miframe, text="+/-", style='BotonesNum.TButton', command= lambda: Negacion())
    boton_Negacion.grid(column=1, row=10, sticky=(W, N, E, S))

    boton_Mas = ttk.Button(aplicacion.miframe, text="+", style='BotonesNum.TButton', command=lambda: Operaciones("+")) 
    boton_Mas.grid(column=4, row=9, sticky=(W, N, E, S))
    boton_Menos = ttk.Button(aplicacion.miframe, text="-", style='BotonesNum.TButton', command=lambda: Operaciones("-")) 
    boton_Menos.grid(column=4, row=8, sticky=(W, N, E, S))
    boton_Multiplicar = ttk.Button(aplicacion.miframe, text="*", style='BotonesNum.TButton', command=lambda: Operaciones("*")) 
    boton_Multiplicar.grid(column=4, row=7, sticky=(W, N, E, S))
    boton_Dividir = ttk.Button(aplicacion.miframe, text=chr(247), style='BotonesNum.TButton', command=lambda: Operaciones("/")) 
    boton_Dividir.grid(column=4, row=6, sticky=(W, N, E, S))
    
    boton_2nd = ttk.Button(aplicacion.miframe, text="2nd", style='BotonesNum.TButton',command=lambda:Boton2nd())
    boton_2nd.grid(column=0, row=4, sticky=(W, N, E, S))
    boton_CuadradoX = ttk.Button(aplicacion.miframe, text="X^2", style='BotonesNum.TButton', command=lambda: CuadradoX()) 
    boton_CuadradoX.grid(column=0, row=5, sticky=(W, N, E, S))
    boton_Raiz2 = ttk.Button(aplicacion.miframe, text="√", style='BotonesNum.TButton', command=lambda: Raiz2()) 
    boton_Raiz2.grid(column=0, row=6, sticky=(W, N, E, S))
    boton_XelevadoY = ttk.Button(aplicacion.miframe, text="X^y", style='BotonesNum.TButton', command=lambda: XelevadoY())
    boton_XelevadoY.grid(column=0, row=7, sticky=(W, N, E, S))
    boton_10elevadoX = ttk.Button(aplicacion.miframe, text="10^x", style='BotonesNum.TButton', command= lambda: _10elevadoX())
    boton_10elevadoX.grid(column=0, row=8, sticky=(W, N, E, S))
    boton_log = ttk.Button(aplicacion.miframe, text="log", style='BotonesNum.TButton',command=lambda: logaritmo())
    boton_log.grid(column=0, row=9, sticky=(W, N, E, S))
    boton_ln= ttk.Button(aplicacion.miframe, text="ln", style='BotonesNum.TButton',command=lambda: logaritmo_natural())
    boton_ln.grid(column=0, row=10, sticky=(W, N, E, S))

    boton_PI = ttk.Button(aplicacion.miframe, text="π", style='BotonesNum.TButton',command=lambda: numeroPulsado('3.1415926535897932384626433832795'))
    boton_PI.grid(column=1, row=4, sticky=(W, N, E, S))
    boton_e = ttk.Button(aplicacion.miframe, text="e", style='BotonesNum.TButton',command=lambda: numeroPulsado('2.7182818284590452353602874713527'))
    boton_e.grid(column=2, row=4, sticky=(W, N, E, S))
    boton_divididoX = ttk.Button(aplicacion.miframe, text="1/X", style='BotonesNum.TButton', command=lambda: DivididoX())
    boton_divididoX.grid(column=1, row=5, sticky=(W, N, E, S))

    boton_abrirP = ttk.Button(aplicacion.miframe, text="(", style='BotonesNum.TButton',command=lambda: Aparentesis())
    boton_abrirP.grid(column=1, row=6, sticky=(W, N, E, S))
    boton_cerrarP = ttk.Button(aplicacion.miframe, text=")", style='BotonesNum.TButton',command=lambda: Cparentesis())
    boton_cerrarP.grid(column=2, row=6, sticky=(W, N, E, S))
    boton_factorial = ttk.Button(aplicacion.miframe, text="N!", style='BotonesNum.TButton',command=lambda: factorial())
    boton_factorial.grid(column=3, row=6, sticky=(W, N, E, S))
    boton_Vabsoluto = ttk.Button(aplicacion.miframe, text="|X|", style='BotonesNum.TButton',command=lambda: ValorAbsoluto())
    boton_Vabsoluto.grid(column=2, row=5, sticky=(W, N, E, S))
    boton_exp = ttk.Button(aplicacion.miframe, text="exp", style='BotonesNum.TButton',command=lambda: exponencial())
    boton_exp.grid(column=3, row=5, sticky=(W, N, E, S))
    boton_mod = ttk.Button(aplicacion.miframe, text="%", style='BotonesNum.TButton', command=lambda: Porcentaje())
    boton_mod.grid(column=4, row=5, sticky=(W, N, E, S))


    for child in aplicacion.miframe.winfo_children():
        child.grid_configure(ipady=6, padx=1, pady=1)


Estandar()

raiz.mainloop()
