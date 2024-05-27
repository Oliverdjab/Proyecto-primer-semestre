import tkinter as tk
#from PIL import Image, ImageTk

# import customtkinter 


# root = customtkinter.CTk()
# root.title("Prueba")
# root.geometry("800x600")
# root.resizable(0,0)
# root.configure(bg="#23BAC4")

# root.mainloop()

def main_windows():
    windows = tk.Tk()
    windows.title("Airlines")
    windows.geometry("800x600")
    windows.resizable(0,0)
    windows.configure(bg="#23BAC4")

    # # nombre_imagen = "avion.jpg"
    # imagen = Image.open("avion.jpg")
    # imagen= tamaño.resize = ((200, 200))
    # # imagen_pil.thumbnail(tamaño)
    # imagen = ImageTk.PhotoImage(imagen)
    # label_imagen = tk.Label(windows, image=imagen, bg="#86A789")
    # label_imagen.imagen = PhotoImage
    # label_imagen.pack(pady=30)
    # # label_imagen.place(x=100, y=100)  # Modifiqué las coordenadas para que la imagen sea visible

        
        
    

    etiqueta_welcome = tk.Label(windows, text="Welcome to airlines", font=("Times New Roman", 18, "bold"), fg="white", bg="#0B666A")
    etiqueta_welcome.pack(padx=100)



    marco_izquierda = tk.Frame(windows,bg="#23BAC4")
    marco_izquierda.pack(side = "left", padx=50)

    marco_derecha = tk.Frame(windows,bg="#23BAC4")
    marco_derecha.pack(side = "right", padx=50)

    etiqueta_codigo = tk.Label(marco_izquierda, text="Codigo", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_codigo.pack(pady=10)

    #marco_central = tk.Canvas(windows, bg="#35A29F")
    #marco_central.pack(expand=True, fill="both")

    etiqueta_apellido = tk.Label(marco_derecha, text = "Apellido", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_apellido.pack(pady=10)

    texto_codigo = tk.Entry(marco_izquierda, show = "*" ,font=("Arial", 14))
    texto_codigo.pack(pady=10)

    texto_apellido = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_apellido.pack(pady=10)

    def windows_check_in ():
        windows.destroy()
        travel_windows()
        travel_windows.deiconify()

    check_in_buttom = tk.Button(windows, text="Realizar Check-in", font = ("Times New Roman", 14), command = windows_check_in, bg = "light green")
    check_in_buttom.pack(side = "bottom", anchor = "s", pady= 50)

    # def windows_check_in ():
    #     windows.destroy()
    #     travel_windows.deiconify()






    
    def travel_windows():
        windows_for_destination = tk.Tk()
        windows_for_destination.title("Choose your Destination")
        windows_for_destination.geometry("800x600")
        windows_for_destination.resizable(0,0)
        windows_for_destination.configure(bg="#23BAC4")

        etiqueta_destination = tk.Label(windows_for_destination, text = "Where do you go?",font = ("Times New Roman", 18 ,"bold"), fg = "white", bg="#0B666A")
        etiqueta_destination.pack(padx = 100)

        # marco_central_for_destination = tk.Frame(windows_for_destination, bg="#86A789", highlightthickness=0)
        # marco_central_for_destination.pack(expand=True, fill="both")

        marco_izquierdo_for_destination = tk.Frame(windows_for_destination, bg="#23BAC4")
        marco_izquierdo_for_destination.pack(side = "left", padx = 50)
        
        marco_derecho_for_destination = tk.Frame(windows_for_destination, bg="#23BAC4")
        marco_derecho_for_destination.pack(side = "right", padx = 50)

        etiqueta_origen = tk.Label(marco_izquierdo_for_destination, text = "Origen", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
        etiqueta_origen.pack(pady = 10)

        texto_origen_entry = tk.Entry(marco_izquierdo_for_destination, font = ("Times New Roman", 14))
        texto_origen_entry.pack(pady = 10)

        etiqueta_destino = tk.Label(marco_derecho_for_destination, text = "Destino", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
        etiqueta_destino.pack(pady = 10)

        texto_destino_entry = tk.Entry(marco_derecho_for_destination, font = ("Times New Roman", 14))
        texto_destino_entry.pack(pady = 10)

        etiqueta_fecha = tk.Label(marco_derecho_for_destination, text = "Fecha", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
        etiqueta_fecha.pack(pady = 10)

        texto_fecha_entry = tk.Entry(marco_derecho_for_destination, font = ("Times New Roman", 14))
        texto_fecha_entry.pack(pady = 10)

        buscar_buttom = tk.Button(windows_for_destination, text = "Search", font = ("Times New Roman",14), bg = "light green")
        buscar_buttom.pack(side = "bottom", anchor = "s", pady = 50)
        



    windows.mainloop()



if __name__ == '__main__':
    main_windows()
#     #travel_windows()






