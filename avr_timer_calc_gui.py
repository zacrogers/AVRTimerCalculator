import tkinter as tk

class AvrTimerCalc(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.init_label_frame()
        self.init_input_frame()
        self.init_button_frame()

    def init_label_frame(self):
        tk.Label(self, text="Timer Resolution:").grid(row=0, column=0)
        tk.Label(self, text="Prescaler:").grid(row=1, column=0)
        tk.Label(self, text="System Clock Frequency (Hz):").grid(row=2, column=0)
        tk.Label(self, text="Total Timer Ticks:").grid(row=3, column=0)
        tk.Label(self, text="Overflow Count:").grid(row=4, column=0)
        tk.Label(self, text="Remainder Timer Ticks:").grid(row=5, column=0)
        tk.Label(self, text="Real Time (sec):").grid(row=6, column=0)
        tk.Label(self, text="New Freq (Hz):").grid(row=7, column=0)

        tk.Label(self, text="Calculate using", relief=tk.RIDGE).grid(row=0, column=2, rowspan=3, sticky="nsew")

    def init_input_frame(self):  
        self.resolution_names = [
            "8 bit", 
            "16 bit",
            "32 bit"
        ]
        
        self.res_selected = tk.StringVar()
        self.res_selected.set(self.resolution_names[0])

        self.resolution_list = tk.OptionMenu(self, self.res_selected, *self.resolution_names)
        self.resolution_list.grid(row=0, column=1, sticky="nsew")

        self.psc_names = [
            "Clk/1", 
            "Clk/8",
            "Clk/32",
            "Clk/64",
            "Clk/128",
            "Clk/256",
            "Clk/1024"
        ]

        self.psc_selected = tk.StringVar()
        self.psc_selected.set(self.psc_names[0])

        self.prescaler_list = tk.OptionMenu(self, self.psc_selected, *self.psc_names)
        self.prescaler_list.grid(row=1, column=1, sticky="nsew")
        self.clk_freq = tk.Entry(self)
        self.clk_freq.grid(row=2, column=1, pady=2)

        self.total_ticks = tk.Entry(self)
        self.total_ticks.grid(row=3, column=1, pady=2)

        self.overflows = tk.Entry(self)
        self.overflows.grid(row=4, column=1, pady=2)

        self.remainder = tk.Entry(self)
        self.remainder.grid(row=5, column=1, pady=2)

        self.real_time = tk.Entry(self)
        self.real_time.grid(row=6, column=1, pady=2)

        self.new_freq = tk.Entry(self)
        self.new_freq.grid(row=7, column=1, pady=2)


    def init_button_frame(self):
        self.calc_tt_btn = tk.Button(self, text="Timer ticks", command = lambda:print("Pre:{}".format(self.get_prescaler())))
        self.calc_tt_btn.grid(row=3, column=2, sticky="nsew", padx = 5, pady = 5)

        self.calc_ofr_btn = tk.Button(self, text="Overflows and Remainder")
        self.calc_ofr_btn.grid(row=4, column=2, rowspan=2, sticky="nsew", padx = 5, pady = 5)

        self.calc_rt_btn = tk.Button(self, text="Real Time")
        self.calc_rt_btn.grid(row=6, column=2, sticky="nsew", padx = 5, pady = 5)

        self.calc_nf_btn = tk.Button(self, text="New Freq")
        self.calc_nf_btn.grid(row=7, column=2, sticky="nsew", padx = 5, pady = 5)


    def get_resolution(self):
        return self.res_selected.get().split(" ")[0]


    def get_prescaler(self):
        return self.psc_selected.get().split("/")[1]


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Avr Timer Calculator")
    a = AvrTimerCalc(root).grid()

    root.mainloop()
