import tkinter as tk
from tkinter import messagebox
import random

advinha = random.randint(1, 100) # quantidade de número, faz com que o pc pense

tentativas = 3 #tentativas do usuário para acertar

# Função para verificar o palpite do usuário
def verificar():
    global tentativas
    try:
        numero = int(entrada.get())  # Pega o valor digitado
        if numero < advinha:
            messagebox.showinfo("Resultado", "ERROU! O número é maior.")
        elif numero > advinha:
            messagebox.showinfo("Resultado", "ERROU! O número é menor.")
        else:
            messagebox.showinfo("Resultado", "🎉 PARABÉNS! VOCÊ ACERTOU! 🎉")
            botao.config(state=tk.DISABLED)  # Desativa o botão

        tentativas -= 1  # Reduz uma tentativa

    except ValueError:
        messagebox.showinfo("Erro", "Digite um número válido!")

    if tentativas == 0:
        messagebox.showinfo("Fim de jogo", f" Suas tentativas acabaram! O número era {advinha}")
        botao.config(state=tk.DISABLED)

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
