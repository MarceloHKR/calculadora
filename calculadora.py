from tkinter import *

root = Tk()

#muda o nome da janela
root.title('Calculadora melhorzinha - beta')

#adiciona o icone da janela
root.iconbitmap('calculadora.ico')

#define o visor, width: define a quantidade max de caracteres,
visor = Entry(root,  width=15,  borderwidth=3,  justify='right',  font=('System', 15),  state='readonly',  readonlybackground='#373A41',  fg='#ffffff')

#posicionamento do visor, columnspan: define a quantidade de colunas que será usada
visor.grid(row=0, column=0, columnspan=3)


#defini a função dos botões numéricos, str:transforma em string
def click_numero(numero):
  visor.configure(state='normal')
  num_visor = visor.get() + str(numero)
  visor.delete(0, END)
  visor.insert(0, num_visor)
  visor.configure(state='readonly')


#definir os botões numéricos, lambda define uma função para o botão
btn_1 = Button(root, text='1', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(1))
btn_2 = Button(root, text='2', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(2))
btn_3 = Button(root, text='3', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(3))
btn_4 = Button(root, text='4', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(4))
btn_5 = Button(root, text='5', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(5))
btn_6 = Button(root, text='6', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(6))
btn_7 = Button(root, text='7', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(7))
btn_8 = Button(root, text='8', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(8))
btn_9 = Button(root, text='9', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(9))
btn_0 = Button(root, text='0', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_numero(0))

#posicionamento dos botões

btn_1.grid(row=3, column=0, sticky=E + W)
btn_2.grid(row=3, column=1, sticky=E + W)
btn_3.grid(row=3, column=2, sticky=E + W)

btn_4.grid(row=2, column=0, sticky=E + W)
btn_5.grid(row=2, column=1, sticky=E + W)
btn_6.grid(row=2, column=2, sticky=E + W)

btn_7.grid(row=1, column=0, sticky=E + W)
btn_8.grid(row=1, column=1, sticky=E + W)
btn_9.grid(row=1, column=2, sticky=E + W)

btn_0.grid(row=4, column=0, sticky=E + W)


#definir função do botão limpar
def click_limpar():
  visor.configure(state='normal')
  visor.delete(0, END)
  visor.configure(state='readonly')


#definir função do botão igual
def click_equal():
  visor.configure(state='normal')
  secon_number = int(visor.get())
  visor.delete(0, END)
  ans = 0
  if math == 'adição':
    ans = first_number + secon_number
  elif math == 'subtração':
    ans = first_number - secon_number
  elif math == 'multiplicação':
    ans = first_number * secon_number
  elif math == 'divisão':
    ans = first_number / secon_number
  visor.insert(0, str(ans))
  visor.configure(state='readonly')


#definir botões de igual e limpar
btn_equal = Button(root, text='=', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=click_equal)
btn_clear = Button(root, text='C', pady=15, font=('Helvetica', 9), bg='#DA671D', fg='#ffffff', command=click_limpar)

#posiciona botões de igual e limpar
btn_equal.grid(row=4, column=1, sticky=E + W)
btn_clear.grid(row=4, column=2, sticky=E + W)


#definir função do botão adição
def click_add():
  visor.configure(state='normal')
  global first_number
  first_number = int(visor.get())
  global math
  math = 'adição'
  visor.delete(0, END)
  visor.configure(state='readonly')


#definir função do botão subtração
def click_sub():
  visor.configure(state='normal')
  global first_number
  first_number = int(visor.get())
  global math
  math = 'subtração'
  visor.delete(0, END)
  visor.configure(state='readonly')


#definir função do botão multiplicação
def click_mul():
  visor.configure(state='normal')
  global first_number
  first_number = int(visor.get())
  global math
  math = 'multiplicação'
  visor.delete(0, END)
  visor.configure(state='readonly')


#definir função do botão divisão
def click_div():
  visor.configure(state='normal')
  global first_number
  first_number = int(visor.get())
  global math
  math = 'divisão'
  visor.delete(0, END)
  visor.configure(state='readonly')


#definir botões de operações
btn_add = Button(root, text='+', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=click_add)
btn_sub = Button(root, text='-', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=click_sub)
btn_mul = Button(root, text='x', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=click_mul)
btn_div = Button(root, text='/', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=click_div)

#posiciona botões de operações
btn_add.grid(row=5, column=0, sticky=E + W)
btn_sub.grid(row=5, column=1, sticky=E + W)
btn_mul.grid(row=5, column=2, sticky=E + W)
btn_div.grid(row=6, column=0, sticky=E + W)

root.mainloop()
