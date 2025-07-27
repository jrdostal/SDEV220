import multiprocessing
from notebook_functions import what_time_is_it as Timer

if __name__ == "__main__":
  for n in range(3):
    p = multiprocessing.Process(target=Timer, args=(" "))
    p.start()