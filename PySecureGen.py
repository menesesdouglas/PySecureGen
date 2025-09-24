import string
import secrets as sec
import customtkinter as ctk

def gerador_senhas(length):
    try:
        special_chars = '!@#$&*?'
        alphabet = string.ascii_letters + string.digits + special_chars
        password = ''.join(sec.choice(alphabet) for i in range(length))
        return password
    except Exception as e:
        print(f"Ocorreu um erro. {e}")

def gerar():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            label_result.configure(text="Tamanho inválido. Digite um número maior que 0.")
        else:
            senha = gerador_senhas(length=password_length)
            label_result.configure(text=f"Senha gerada: {senha}")
    except ValueError:
        label_result.configure(text="Por favor, digite um número inteiro.")

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Gerador de Senhas')
app.geometry('400x200')

title_app = ctk.CTkLabel(app,text='Gerador de Senha')
title_app.pack(pady=5)
instruc = ctk.CTkLabel(app,text='Tamanho da senha:')
instruc.pack(pady=5)
entry_length = ctk.CTkEntry(app,placeholder_text='Tamanho da senha')
entry_length.pack(pady=10)
button = ctk.CTkButton(app,text='Gerar Senha',command=gerar)
button.pack(pady=10)
label_result = ctk.CTkLabel(app, text='')
label_result.pack(pady=5)

app.mainloop()
