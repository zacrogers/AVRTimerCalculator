import math

class AvrTimerCalc():
    def __init__(self):
        self.clk_freq         = 8000000
        self.prescaler        = 1024     #1, 8, 32, 64, 128, 256, 1024
        self.timer_resolution = 8        #8, 16, 32
        
        self.total_ticks      = 0.0
        self.overflows        = 0.0
        self.remainder        = 0.0
        self.real_time        = 2.5
        self.new_freq         = 0.0


    def calc_total_ticks(self, ticks):
        self.total_ticks = ticks
        
        freq = self.clk_freq / self.prescaler
        
        self.overflows = math.floor(self.total_ticks / (2**self.timer_resolution))
        self.remainder = self.total_ticks - (self.overflows* (2**self.timer_resolution))
        self.real_time = self.total_ticks / freq
        self.new_freq  = freq / self.total_ticks
        

    def calc_overflow_remainder(self):
        freq = self.clk_freq / self.prescaler
        
        self.total_ticks = self.overflows * (2**self.timer_resolution)

        
    def calc_real_time(self, time):
        self.real_time = time

        freq = self.clk_freq / self.prescaler
        
        self.new_freq    = 1 / self.real_time
        self.total_ticks = self.real_time * freq
        self.overflows   = math.floor(self.total_ticks / (2**self.timer_resolution))
        self.remainder   = self.total_ticks - (self.overflows * (2**self.timer_resolution))
        
        
    def calc_new_freq(self, freq):
        self.new_freq = freq
        freq = self.clk_freq / self.prescaler   
            
        self.real_time   = 1 / self.new_freq
        self.total_ticks = self.real_time * freq
        self.overflows   = math.floor(self.total_ticks / (2**self.timer_resolution))
        self.remainder   = self.total_ticks - (self.overflows * (2**self.timer_resolution))
        

    def print_state(self):
        print("System clock:{}\nTimer Res:{}\n".format(self.clk_freq, self.timer_resolution))
        print("Prsc:{}\nTot ticks:{}\n".format(self.prescaler, self.total_ticks))
        print("Overflow:{}\nRemainder:{}\n".format(self.overflows, self.remainder))
        print("Real time:{}\nNew freq:{}\n".format(self.real_time, self.new_freq))


if __name__ == "__main__":
    calc = AvrTimerCalc()
    # calc.calc_total_ticks(ticks = 20)
    calc.calc_new_freq(freq = 8000)
    
    calc.print_state()

