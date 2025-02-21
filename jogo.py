import tkinter as tk
from tkinter import messagebox

# Número correto
advinha = 5  

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

# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo da Adivinhação")
janela.geometry("300x200")

# Rótulo (Texto)
label = tk.Label(janela, text="Adivinhe um número de 1 a 100:")
label.pack(pady=10)

# Entrada de texto
entrada = tk.Entry(janela)
entrada.pack()

# Botão para verificar o número
botao = tk.Button(janela, text="Tentar", command=verificar)
botao.pack(pady=10)

# Rodar a aplicação
janela.mainloop()
