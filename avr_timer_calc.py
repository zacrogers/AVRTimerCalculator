import math


clk_freq = 0
prescaler = 0
timer_resolution = 0

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


def calc_overflow_remainder():
  pass
    
    
def calc_real_time():
  pass
  
  
def calc_new_freq():
  pass
