from cx_Freeze import setup, Executable 
  
setup(name = "AvrTimerCalculator" , 
      version = "0.1" , 
      description = "" , 
      executables = [Executable("AvrTimerCalculator.pyw", base = "Win32GUI")]) 