import tkinter as tk
import math

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

        tk.Label(self, text="Calculate using", relief=tk.RIDGE).grid(row=0, column=2, rowspan=3, sticky="nsew", padx=15, pady=15)

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
        self.clk_freq.grid(row=2, column=1, pady=3)

        self.total_ticks = tk.Entry(self)
        self.total_ticks.grid(row=3, column=1, pady=3)

        self.overflows = tk.Entry(self)
        self.overflows.grid(row=4, column=1, pady=3)

        self.remainder = tk.Entry(self)        
        self.remainder.grid(row=5, column=1, pady=3)

        self.real_time = tk.Entry(self)
        self.real_time.grid(row=6, column=1, pady=3)

        self.new_freq = tk.Entry(self)
        self.new_freq.grid(row=7, column=1, pady=3)


    def init_button_frame(self):
        self.calc_tt_btn = tk.Button(self, text="Timer ticks")#, command = self.calc_total_ticks)
        self.calc_tt_btn.grid(row=3, column=2, sticky="nsew", padx = 5, pady = 5)

        self.calc_ofr_btn = tk.Button(self, text="Overflows and Remainder")
        self.calc_ofr_btn.grid(row=4, column=2, rowspan=2, sticky="nsew", padx = 5, pady = 5)

        self.calc_rt_btn = tk.Button(self, text="Real Time", command = self.calc_real_time)
        self.calc_rt_btn.grid(row=6, column=2, sticky="nsew", padx = 5, pady = 5)

        self.calc_nf_btn = tk.Button(self, text="New Freq")
        self.calc_nf_btn.grid(row=7, column=2, sticky="nsew", padx = 5, pady = 5)


    def get_resolution(self):
        return int(self.res_selected.get().split(" ")[0])

    def get_prescaler(self):
        return int(self.psc_selected.get().split("/")[1])

    def get_clk_freq(self):
        return int(self.clk_freq.get())

    def get_total_ticks(self):
        return int(self.total_ticks.get())

    def get_overflows(self):
        return float(self.overflows.get())

    def get_remainder(self):
        return float(self.remainder.get())        

    def get_real_time(self):
        return float(self.real_time.get())

    def get_new_freq(self):
        return float(self.new_freq.get()) 



    def calc_real_time(self):
        freq = self.get_clk_freq() / self.get_prescaler()

        self.new_freq.insert(0, str(1 / self.get_real_time()))
        self.total_ticks.insert(0, str(self.get_real_time() * freq))
        self.overflows.insert(0, str(math.floor(self.get_total_ticks() / (2**self.get_resolution()))))
        self.remainder.insert(0, str(self.get_total_ticks() - (self.get_overflows() * (2**self.get_resolution()))))
'''

    def calc_total_ticks(self):
        #self.total_ticks = ticks
        
        freq = self.clk_freq.get() / self.get_prescaler()
        
        self.overflows.insert(math.floor(self.total_ticks / (2**self.get_resolution())))
        self.remainder.insert(self.total_ticks.get() - (self.overflows* (2**self.get_resolution())))
        self.real_time.insert(self.total_ticks.get() / freq)
        self.new_freq.insert(freq / self.total_ticks.get())



    def calc_overflow_remainder(self):
        freq = self.clk_freq.get() / self.get_prescaler()
        
        self.total_ticks = self.overflows * (2**self.timer_resolution)

    def calc_new_freq(self):
       # self.new_freq = freq
        freq = self.clk_freq.get() / self.get_prescaler() 
            
        self.real_time   = 1 / self.new_freq
        self.total_ticks = self.real_time * freq
        self.overflows   = math.floor(self.total_ticks / (2**self.timer_resolution))
        self.remainder   = self.total_ticks - (self.overflows * (2**self.timer_resolution))
'''

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Avr Timer Calculator")
    a = AvrTimerCalc(root).grid()

    root.mainloop()
