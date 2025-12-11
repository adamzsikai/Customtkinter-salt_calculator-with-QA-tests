import customtkinter as ctk

def check_entries(event=None):
    if salta.get().strip() and batchsize.get().strip() and desired_entry.get().strip() and corrector.get().strip():
        calculate_button.configure(state="normal")
        calculateback_button.configure(state="disabled")

    elif salta.get().strip() and batchsize.get().strip() and corrector.get().strip() and qty_entry.get().strip():
        calculate_button.configure(state="disabled")
        calculateback_button.configure(state="normal")

    else:
        calculate_button.configure(state="disabled")
        calculateback_button.configure(state="disabled")

    

def calc_component2_amount():
    try:
        salt1_input = salta.get()
        numbers = [float(x.strip()) for x in salt1_input.split(' ') if x.strip()]
        avg_salt1 = sum(numbers) / len(numbers)
        average.set(f"{avg_salt1:.2f}")

        salt2 = float(corrector.get())
        salt_target = float(desired.get())
        amount1 = float(batchsize.get())

        # Quotient számítás
        quotient1 = (salt_target - salt2) / (avg_salt1 - salt2)
        quotient2 = 1 - quotient1

        amount2 = amount1 * (quotient2 / quotient1)
        componentqty.set(f"{amount2:.2f}")
        newqty.set(f"{amount2 + amount1:.2f}")

    except Exception as e:
        average.set(f"ERROR: {str(e)}")
        componentqty.set(f"ERROR: {str(e)}")
        newqty.set(f"ERROR: {str(e)}")

def reversed_calculation():
    try:
        salt1_input = salta.get()
        numbers = [float(x.strip()) for x in salt1_input.split(' ') if x.strip()]
        avg_salt1 = sum(numbers)/len(numbers)
        average.set(f"{avg_salt1:.2f}")

        salt2 = float(corrector.get())
        amount1 = float(batchsize.get())
        amount2 = float(qty_entry.get())

        salt_backw = ((amount1*avg_salt1)+(amount2*salt2))/ (amount1+amount2)

        desired.set(f"{salt_backw:.2f}")
        newqty.set(f"{amount1+amount2:.2f}")

    except Exception as e:
        average.set(f"ERROR: {str(e)}")
        desired.set(f"ERROR: {str(e)}")
        newqty.set(f"ERROR: {str(e)}")

        


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

win = ctk.CTk()
win.geometry("550x250")
win.title("SALT CORRECTOR")


salta = ctk.CTkEntry(master=win, placeholder_text="                     %", width=160, corner_radius=9)
salta.grid(row=1, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="MEASURED SALT:", text_color="red",font=("Helvetica", 14)).grid(row=1, column=1)

average = ctk.StringVar()

ctk.CTkLabel(win, textvariable=average, font=("Helvetica", 14), width=110,corner_radius=9, fg_color="yellow", text_color="black").place(x=410, y=10)
ctk.CTkLabel(win, text="AVERAGE:", text_color="red",font=("Helvetica", 14)).place(x=330, y=10)

batchsize = ctk.CTkEntry(master=win, placeholder_text="                    KG", width=160, corner_radius=9)
batchsize.grid(row=2, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="BATCH SIZE:", text_color="red",font=("Helvetica", 14)).grid(row=2, column=1)

desired = ctk.StringVar()
desired_entry = ctk.CTkEntry(master=win, textvariable=desired,placeholder_text="                     %", width=160, corner_radius=9)
desired_entry.grid(row=3, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="TARGET SALT:", text_color="red",font=("Helvetica", 14)).grid(row=3, column=1)

corrector = ctk.CTkEntry(master=win, placeholder_text="                     %", width=160, corner_radius=9)
corrector.grid(row=4, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="COMPONENT SALT:", text_color="#28fc03",font=("Helvetica", 14)).grid(row=4, column=1,padx=5)

componentqty = ctk.StringVar()
qty_entry = ctk.CTkEntry(win,textvariable=componentqty, font=("Helvetica", 14), text_color="#28fc03")
qty_entry.place(x=380, y=155)
ctk.CTkLabel(win, text="QTY:", text_color="#28fc03",font=("Helvetica", 14)).place(x=330, y=155)


newqty = ctk.StringVar()
ctk.CTkLabel(win, text="NEW SIZE:", font=("Helvetica", 14), text_color="red").place(x=330, y=60)
ctk.CTkLabel(win, textvariable=newqty, font=("Helvetica", 14), width=110, corner_radius=9, fg_color="yellow", text_color="black").place(x=410, y=60)

calculate_button = ctk.CTkButton(win, text="CALCULATE", command=calc_component2_amount, fg_color="red", hover_color="yellow" , text_color="black", width = 110, corner_radius=9)
calculate_button.place(x=410, y=106)
calculate_button.configure(state="disabled")

calculateback_button = ctk.CTkButton(win, text="C.BACKWARD", command=reversed_calculation, fg_color="#28fc03", hover_color="yellow" , text_color="black", width = 110, corner_radius=9)
calculateback_button.place(x=410, y=203)
calculateback_button.configure(state="disabled")

salta.bind("<KeyRelease>",check_entries)
batchsize.bind("<KeyRelease>",check_entries)
desired_entry.bind("<KeyRelease>",check_entries)
corrector.bind("<KeyRelease>",check_entries)
qty_entry.bind("<KeyRelease>",check_entries)


win.mainloop()