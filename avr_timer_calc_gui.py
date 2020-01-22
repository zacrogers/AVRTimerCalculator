import tkinter as tk

class AvrTimerCalc(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.label_frame = tk.Frame(self)
        self.input_frame = tk.Frame(self)


        self.resolution_names = [
            "8 bit", 
            "16 bit",
            "32 bit"
        ]
        self.res_selected = tk.StringVar()
        self.res_selected.set(self.resolution_names[0])

        self.resolution_list = tk.OptionMenu(self.input_frame, self.res_selected, *self.resolution_names)
        self.resolution_list.pack(side = tk.TOP, fill = "both", expand = True)

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

        self.prescaler_list = tk.OptionMenu(self.input_frame, self.psc_selected, *self.psc_names)
        self.prescaler_list.pack(side = tk.TOP, fill = "both", expand = True)
        self.clk_freq = tk.Entry(self.input_frame)
        self.clk_freq.pack(side=tk.TOP)

        self.total_ticks = tk.Entry(self.input_frame)
        self.total_ticks.pack(side=tk.TOP)

        self.overflows = tk.Entry(self.input_frame)
        self.overflows.pack(side=tk.TOP)

        self.remainder = tk.Entry(self.input_frame)
        self.remainder.pack(side=tk.TOP)

        self.real_time = tk.Entry(self.input_frame)
        self.real_time.pack(side=tk.TOP)

        self.new_freq = tk.Entry(self.input_frame)
        self.new_freq.pack(side=tk.TOP)

        self.label_frame.pack(side = tk.LEFT)
        self.input_frame.pack(side = tk.LEFT)
    

if __name__ == "__main__":
    root = tk.Tk()
    AvrTimerCalc(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
