import tkinter as tk
from tkinter import messagebox

from random import randint # biblioteca para gerar um número aleatorio
advinha = randint(0, 5) # degino a quantidade de número, faz com que o pc pense

# Função para verificar o palpite do usuário
def verificar():
    try:
        numero = int(entrada.get())  # Pega o valor digitado
        if numero < advinha:
            messagebox.showinfo("Resultado", "ERROU! O número é maior.")
        elif numero > advinha:
            messagebox.showinfo("Resultado", "ERROU! O número é menor.")
        else:
            messagebox.showinfo("Resultado", "🎉 PARABÉNS! VOCÊ ACERTOU! 🎉")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")

janela = tk.Tk()
janela.title("Jogo da Adivinhação")
janela.geometry("300x200")

label = tk.Label(janela, text="Adivinhe um número de 1 a 100:")
label.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Tentar", command=verificar)
botao.pack(pady=10)

janela.mainloop()
