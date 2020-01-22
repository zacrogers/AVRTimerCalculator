import math

clk_freq = 8000000

prescaler = 1 #1, 8, 32, 64, 128, 256, 1024
timer_resolution = 8 #8, 16, 32

total_ticks = 0
overflows = 0
remainder = 0
real_time = 0
new_freq = 0

def calc_total():
  freq = clk_freq / prescaler
  
  overflows = math.floor(total_ticks / 2**timer_resolution)
  remander = total_ticks - (overflows* (2**timer_resolution))
  
  real_time = total_ticks / freq
  new_freq = freq / total_ticks

  print_state()

def calc_overflow_remainder():
  freq = clk_freq / prescaler
  
  total_ticks = overflows * (2**timer_resolution)
  print_state()
    
    
def calc_real_time():
  new_freq = 1 / real_time
  
  freq = clk_freq / prescaler
  total_ticks = real_time * freq
  
  overflow = math.floor(total_ticks / (2**timer_resolution))
  remainder = total_ticks - (overflow * (2**timer_resolution))
  
  print_state()
  
def calc_new_freq():
  real_time = 1 / new_freq
  freq = clk_freq / prescaler
  
  total_ticks = real_time * freq
  
  overflow = math.floor(total_ticks / (2**timer_resolution))
  remainder = total_ticks - (overflow * (2**timer_resolution))
  
  print_state()

  
  
def print_state():
  print("System clock:{} \n Timer Res:{}\n Prsc:{}\n Tot ticks:{}\n".format(clk_freq, prescaler, timer_resolution, total_ticks))
  print("Overflow:{} \n Remainder:{}\n Real time:{}\n New icks:{}\n".format(overflows, remainder, real_time, new_freq))
