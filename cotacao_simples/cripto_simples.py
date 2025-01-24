import tkinter as tk
from tkinter import messagebox
import requests

def obter_cotacao_cripto(cripto, moeda):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies={moeda}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        if cripto in dados:
            preco_cripto = dados[cripto][moeda]
            return preco_cripto
        else:
            messagebox.showerror("Erro", f"A criptomoeda '{cripto}' não foi encontrada. Verifique o nome e tente novamente.")
            return None
    else:
        messagebox.showerror("Erro", "Erro ao buscar a cotação. Tente novamente mais tarde.")
        return None

def mostrar_cotacao():
    cripto = cripto_entry.get().lower()
    moeda = moeda_entry.get().lower()
    
    if cripto == "" or moeda == "":
        messagebox.showwarning("Entrada inválida", "Por favor, preencha os campos de criptomoeda e moeda.")
        return
    
    preco = obter_cotacao_cripto(cripto, moeda)
    
    if preco is not None:
        resultado_label.config(text=f"A cotação de {cripto.upper()} em {moeda.upper()} é: {preco:.2f}")
        resultado_label.config(bg="#e3f2fd", fg="#1a237e", font=("Arial", 12))  # Fonte menor no resultado
    else:
        resultado_label.config(text="")
        resultado_label.config(bg="#f4f4f9", fg="#333", font=("Arial", 12))  # Fonte menor e padrão

def limpar_campos():
    cripto_entry.delete(0, tk.END)
    moeda_entry.delete(0, tk.END)
    resultado_label.config(text="")
    resultado_label.config(bg="#f4f4f9", fg="#333", font=("Arial", 12))

def sair_aplicacao():
    # Função para fechar a aplicação com confirmação
    resposta = messagebox.askyesno("Confirmar saída", "Você tem certeza que deseja sair?")
    if resposta:
        root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Consulta de Cotação de Criptomoedas")
root.geometry("400x450")  # Ajuste no tamanho da janela para acomodar as mudanças
root.config(bg="#f4f4f9")  # Cor de fundo suave

# Configuração do layout
frame = tk.Frame(root, bg="#f4f4f9")
frame.pack(pady=20)

# Título
titulo_label = tk.Label(frame, text="Consulta de Criptomoeda", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Rótulos
cripto_label = tk.Label(frame, text="Criptomoeda (ex: bitcoin):", font=("Arial", 12), bg="#f4f4f9", fg="#333")
cripto_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

moeda_label = tk.Label(frame, text="Moeda (ex: brl, usd):", font=("Arial", 12), bg="#f4f4f9", fg="#333")
moeda_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Entradas de texto
cripto_entry = tk.Entry(frame, width=20, font=("Arial", 12))
cripto_entry.grid(row=1, column=1, padx=10, pady=5)

moeda_entry = tk.Entry(frame, width=20, font=("Arial", 12))
moeda_entry.grid(row=2, column=1, padx=10, pady=5)

# Botões menores
buscar_button = tk.Button(frame, text="Buscar Cotação", font=("Arial", 10), bg="#4CAF50", fg="white", command=mostrar_cotacao, width=15, height=1, relief="solid", bd=2)
buscar_button.grid(row=3, column=0, columnspan=2, pady=10)

limpar_button = tk.Button(frame, text="Limpar", font=("Arial", 10), bg="#f44336", fg="white", command=limpar_campos, width=15, height=1, relief="solid", bd=2)
limpar_button.grid(row=4, column=0, columnspan=2, pady=5)

# Botão Sair
sair_button = tk.Button(frame, text="Sair", font=("Arial", 10), bg="#9E9E9E", fg="white", command=sair_aplicacao, width=15, height=1, relief="solid", bd=2)
sair_button.grid(row=5, column=0, columnspan=2, pady=10)

# Caixa de resultado com mais destaque
resultado_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f9", fg="#333", width=30, height=3, relief="solid", bd=2)
resultado_label.pack(pady=15)

# Inicia o loop da interface gráfica
root.mainloop()
