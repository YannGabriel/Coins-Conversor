import customtkinter, requests

# Configurações da janela
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry("500x300")

# Conteúdo da janela
intro = customtkinter.CTkLabel(window, text="Coins Conversor")
coin = customtkinter.CTkEntry(window, placeholder_text="Insert your coin: ")

def coin_verification():
    user_coin = coin.get()
    result_text = ''
    if user_coin == 'a':
        result_text = 'Dollar'
    else:
        result_text = 'Unknown coin'
    
    result_label.configure(text=f"Result: {result_text}")

result_label = customtkinter.CTkLabel(window, text="Result: ")
verify_button = customtkinter.CTkButton(window, text="Verify", command=coin_verification)

# Organizando na janela
intro.pack(padx=10, pady=10)
coin.pack(padx=20, pady=20)
verify_button.pack(padx=10, pady=10)
result_label.pack(padx=30, pady=30)

window.mainloop()
