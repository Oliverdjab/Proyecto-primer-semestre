import tkinter as tk


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

        def ingreso_dato():
            windows_for_destination.destroy()
            iniciar_interfaz()
            iniciar_interfaz.deiconify()

        buscar_buttom = tk.Button(windows_for_destination, text = "Search", font = ("Times New Roman",14),command=ingreso_dato, bg = "light green")
        buscar_buttom.pack(side = "bottom", anchor = "s", pady = 50)




    windows.mainloop()






def incrementar_contador(i):
    contadores[i] += 1
    labels[i].config(text=f"{opciones[i]}: {contadores[i]}")

def crear_botones(inicio, fin):
    for i in range(inicio, fin):
        boton = tk.Button(frame, text=f"{opciones[i]}", command=lambda i=i: incrementar_contador(i))
        boton.grid(row=i % 18, column=0, pady=5)
        botones.append(boton)
        labels[i] = tk.Label(frame, text=f"{opciones[i]}: {contadores[i]}")
        labels[i].grid(row=i % 18, column=1, padx=10)

def cambiar_pagina(direccion):
    global pagina_actual
    if direccion == "adelante":
        pagina_actual += 1
    elif direccion == "atras":
        pagina_actual -= 1

    if pagina_actual < 0:
        pagina_actual = 0
    elif pagina_actual >= total_paginas:
        pagina_actual = total_paginas - 1

    actualizar_botones()

def actualizar_botones():
    for boton in botones:
        boton.grid_forget()
    inicio = pagina_actual * botones_por_pagina
    fin = min((pagina_actual + 1) * botones_por_pagina, len(opciones))
    crear_botones(inicio, fin)

def iniciar_interfaz():
    global frame, frame_botones_pagina, root
    root = tk.Tk()
    root.geometry("1200x900")
    root.resizable(0,0)
    root.configure(bg="#23BAC4")
    root.title("Contadores de Opciones")

    global labels, botones
    labels = {}
    botones = []

    frame = tk.Frame(root,bg="#338DFF")
    frame.grid(row=0, column=0)

    crear_botones(0, min(botones_por_pagina, len(opciones)))

    frame_botones_pagina = tk.Frame(root, bg = "#23BAC4")
    frame_botones_pagina.grid(row=1, column=0, pady=10)

    btn_atras = tk.Button(frame_botones_pagina, text="Página anterior", command=lambda: cambiar_pagina("atras"), bg="#68FF33")
    btn_atras.grid(row=0, column=0, padx=5)

    btn_adelante = tk.Button(frame_botones_pagina, text="Página siguiente", command=lambda: cambiar_pagina("adelante"), bg="#68FF33")
    btn_adelante.grid(row=0, column=1, padx=5)

    root.mainloop()

opciones = [
    ['Z328', '2024-06-5', '08:13:00', '10:35:00', 244463, 538669, 1666594, 'Santa Marta', 'Bogota'],
    ['X633', '2024-06-6', '02:55:00', '05:58:00', 483669, 640186, 4023518, 'Santa Marta', 'Cartagena'],
    ['G611', '2024-06-12', '16:50:00', '17:07:00', 295876, 915371, 2684321, 'Medellin', 'Santa Marta'],
    ['J786', '2024-06-26', '15:44:00', '16:20:00', 464673, 723388, 4718254, 'Cali', 'Bogota'],
    [ 'I506', '2024-06-26', '12:13:00', '13:48:00', 156761, 955557, 4359006, 'Medellin', 'Cartagena'],
    ['W151', '2024-06-27', '01:46:00', '03:28:00', 158668, 887450, 1527895, 'Santa Marta', 'Bogota'],
    ['I657', '2024-06-5', '23:46:00', '2:48:00', 227358, 920227, 3299390, 'Bogota', 'Medellin'],
    ['A722', '2024-06-6', '12:32:00', '14:25:00', 335925, 718598, 3201428, 'Medellin', 'Santa Marta'],
    ['G542', '2024-06-27', '10:15:00', '12:58:00', 364902, 620659, 3822832, 'Cali', 'Bogota'],
    ['R419', '2024-06-13', '18:45:00', '21:11:00', 263221, 823412, 1802097, 'Cali', 'Bogota'],
    ['K387', '2024-06-12', '08:52:00', '12:58:00', 111358, 837315, 1740776, 'Medellin', 'Cartagena'],
    ['I684', '2024-06-6', '18:25:00', '22:33:00', 268461, 861073, 4378830, 'Santa Marta', 'Cartagena'],
    ['T366', '2024-06-6', '15:59:00', '16:30:00', 441718, 551893, 1443926, 'Bogota', 'Medellin'],
    ['G973', '2024-06-27', '07:51:00', '09:59:00', 107735, 812320, 4667378, 'Cartagena', 'Medellin'],
    ['P628', '2024-06-20', '20:47:00', '21:45:00', 259683, 878251, 1406197, 'Cali', 'Bogota'],
    ['V577', '2024-06-20', '19:47:00', '23:12:00', 321437, 838480, 2594022, 'Bogota', 'Medellin'],
    ['Y916', '2024-06-5', '19:05:00', '20:07:00', 146788, 717336, 2479818, 'Bogota', 'Medellin'],
    ['C616', '2024-06-6', '14:43:00', '19:14:00', 251102, 768356, 3231604, 'Bogota', 'Medellin'],
   ['Z502', '2024-06-27', '02:33:00', '04:46:00', 135039, 739155, 3841687, 'Santa Marta', 'Medellin'],
['O706', '2024-06-19', '03:33:00', '08:12:00', 108543, 552765, 4776384, 'Cartagena', 'Medellin'],
['A425', '2024-06-12', '05:16:00', '07:38:00', 428767, 803167, 3465554, 'Bogota', 'Cartagena'],
['A643', '2024-06-27', '02:41:00', '06:50:00', 133731, 965070, 1155231, 'Bogota', 'Santa Marta'],
['C594', '2024-06-6', '20:14:00', '22:16:00', 179770, 755917, 3525256, 'Cartagena', 'Cali'],
['X712', '2024-06-5', '04:28:00', '05:47:00', 367356, 997236, 2511543, 'Santa Marta', 'Cartagena'],
['X517', '2024-06-26', '13:23:00', '16:23:00', 409500, 657451, 2024557, 'Cali', 'Cartagena'],
['M302', '2024-06-20', '15:15:00', '17:10:00', 138614, 638674, 4057270, 'Cartagena', 'Cali'],
['X448', '2024-06-12', '14:57:00', '16:48:00', 256801, 649687, 2492053, 'Medellin', 'Bogota'],
['K415', '2024-06-6', '01:59:00', '02:58:00', 118208, 955980, 3967119, 'Cartagena', 'Cali'],
['N999', '2024-06-20', '00:02:00', '01:28:00', 113404, 742916, 3870717, 'Cali', 'Bogota'],
['Q579', '2024-06-19', '10:13:00', '13:46:00', 442756, 900225, 4970730, 'Bogota', 'Cali'],
['O632', '2024-06-5', '10:46:00', '11:04:00', 450503, 759587, 3350417, 'Cali', 'Medellin'],
['W768', '2024-06-5', '00:14:00', '02:37:00', 309428, 530313, 3146101, 'Cartagena', 'Santa Marta'],
['N700', '2024-06-20', '17:02:00', '21:47:00', 428761, 586568, 4387318, 'Cali', 'Medellin'],
['A198', '2024-06-13', '10:07:00', '11:34:00', 471496, 637023, 3708333, 'Santa Marta', 'Cali'],
['N508', '2024-06-20', '07:49:00', '11:17:00', 380455, 885626, 1079810, 'Cali', 'Bogota'],
['S830', '2024-06-26', '06:11:00', '08:05:00', 136210, 609050, 1031737, 'Medellin', 'Bogota'],
['B193', '2024-06-12', '11:55:00', '16:16:00', 322687, 776707, 3559620, 'Santa Marta', 'Medellin'] ,
['N925', '2024-06-20', '20:09:00', '23:27:00', 348655, 584679, 2803067, 'Bogota', 'Cali'],
['O805', '2024-06-19', '08:11:00', '12:14:00', 180125, 637210, 4660148, 'Cartagena', 'Cali'],
['B165', '2024-06-20', '00:21:00', '03:01:00', 285230, 798592, 4037787, 'Medellin', 'Cali'],
['Q419', '2024-06-6', '18:09:00', '20:04:00', 336342, 966902, 3843081, 'Santa Marta', 'Bogota'],
['H905', '2024-06-6', '11:56:00', '13:11:00', 345069, 702454, 1287428, 'Cali', 'Santa Marta'],
['R873', '2024-06-6', '00:14:00', '04:15:00', 209011, 932430, 2499023, 'Santa Marta', 'Cali'],
['T810', '2024-06-6', '22:03:00', '00:13:00', 353905, 622617, 1739971, 'Medellin', 'Santa Marta'],
['R507', '2024-06-20', '03:35:00', '05:14:00', 338290, 891960, 3268081, 'Cartagena', 'Bogota'],
['E279', '2024-06-27', '03:32:00', '07:31:00', 112594, 535012, 2407140, 'Cali', 'Bogota'],
['T179', '2024-06-5', '21:42:00', '23:56:00', 194995, 970417, 3446179, 'Medellin', 'Bogota'],
['E348', '2024-06-6', '14:21:00', '17:45:00', 200805, 661664, 1423079, 'Cartagena', 'Cali'],
['V809', '2024-06-5', '15:17:00', '18:30:00', 412564, 851500, 4680941, 'Santa Marta', 'Medellin'],
['D483', '2024-06-12', '04:31:00', '09:24:00', 232173, 607087, 4661950, 'Cali', 'Cartagena'],
['F592', '2024-06-20', '20:57:00', '23:35:00', 387337, 666898, 4024585, 'Medellin', 'Cartagena'],
['B209', '2024-06-6', '07:51:00', '10:33:00', 422422, 832491, 3948879, 'Santa Marta', 'Cartagena'] ,
['F812', '2024-06-26', '04:51:00', '08:56:00', 100947, 539536, 3632244, 'Cali', 'Cartagena'],
['X552', '2024-06-26', '04:54:00', '07:10:00', 271127, 656834, 4845023, 'Cartagena', 'Santa Marta'] ,
['I848', '2024-06-5', '07:45:00', '12:08:00', 180814, 648460, 4560674, 'Cartagena', 'Bogota'],
['J755', '2024-06-20', '02:52:00', '07:15:00', 352497, 973921, 4954962, 'Cali', 'Medellin'],
['Y216', '2024-06-19', '02:44:00', '05:12:00', 339920, 690835, 3549467, 'Cartagena', 'Santa Marta'] ,
['G442', '2024-06-12', '01:09:00', '03:41:00', 346049, 850291, 4890999, 'Medellin', 'Cali'],
['V932', '2024-06-12', '16:57:00', '18:53:00', 368937, 836969, 2128948, 'Santa Marta', 'Medellin']   ,
['Q252', '2024-06-20', '08:20:00', '13:01:00', 477214, 801662, 4676437, 'Cartagena', 'Cali'],
['D848', '2024-06-27', '11:08:00', '14:48:00', 239379, 992500, 3004583, 'Bogota', 'Santa Marta'],
['S569', '2024-06-5', '14:40:00', '16:24:00', 198988, 955922, 4074101, 'Bogota', 'Medellin'],
['I656', '2024-06-13', '20:31:00', '23:13:00', 283863, 587002, 3987051, 'Medellin', 'Cali'],
['S129', '2024-06-6', '18:08:00', '19:08:00', 377016, 650034, 1915104, 'Medellin', 'Cartagena'],
['N232', '2024-06-5', '16:35:00', '19:08:00', 186616, 590890, 2616295, 'Medellin', 'Santa Marta'],
['M191', '2024-06-20', '03:11:00', '07:02:00', 343481, 664520, 3274677, 'Cartagena', 'Medellin'],
['H180', '2024-06-20', '00:19:00', '02:53:00', 314037, 672798, 3793121, 'Santa Marta', 'Cali'],
['V900', '2024-06-19', '10:39:00', '13:52:00', 361362, 575041, 4335294, 'Santa Marta', 'Cali'],
['Q449', '2024-06-27', '18:37:00', '20:56:00', 407816, 703210, 4323741, 'Santa Marta', 'Cali'],
['R250', '2024-06-26', '16:28:00', '18:29:00', 478289, 965855, 2387745, 'Cali', 'Bogota'],
['T654', '2024-06-26', '12:11:00', '14:20:00', 358074, 736442, 4444497, 'Santa Marta', 'Bogota'],
['Y804', '2024-06-12', '14:28:00', '16:34:00', 261803, 548104, 1150859, 'Cali', 'Bogota'],
['E971', '2024-06-12', '22:07:00', '23:12:00', 362030, 972110, 1721417, 'Santa Marta', 'Cartagena'] ,
['U728', '2024-06-12', '15:55:00', '18:43:00', 352021, 909057, 3924712, 'Santa Marta', 'Medellin'],
['U522', '2024-06-13', '12:46:00', '14:54:00', 169490, 503891, 2723741, 'Bogota', 'Cartagena'],
['V560', '2024-06-26', '08:41:00', '11:20:00', 118816, 675485, 2104917, 'Santa Marta', 'Cali'],
]

contadores = [0 for _ in range(len(opciones))]

botones_por_pagina = 18
total_paginas = (len(opciones) + botones_por_pagina - 1) // botones_por_pagina
pagina_actual = 0


if __name__ == '__main__':
    main_windows()
    # iniciar_interfaz()

