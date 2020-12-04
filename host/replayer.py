#!/usr/bin/python3

import socket
import subprocess
import random

import config
import converter
import generator
import printer

if __name__ == "__main__":
  # start target program (VBox, VMware)
  # TODO: recovery method
  
  # start socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", config.FUZZ_PORT))

    if config.DEBUG:
      print('Waiting for connection...')

    s.listen()
    conn, addr = s.accept()
    with conn:
      if config.DEBUG:
        print('Connected by', addr)
      
      while True:
        # generate file (cur.pkts)
        # TODO: implement generation of data

        filename = input("Enter file name to replay: ")

        with open(filename, "rb") as f:
          cur_data = f.read()
          data_len = len(cur_data)

        if config.DEBUG:
          print_data = cur_data
          idx = 0
          while len(print_data) > 0:
            print("PRINTING CMD ", idx)
            print_data = printer.print_cmd(print_data)
            idx += 1
          print("Data read - file length : " + str(data_len))

        with open("cur.pkts", "wb") as f:
          f.write(cur_data)

        try:
          conn.sendall(generator.p32(len(cur_data))+cur_data)

          if config.DEBUG:
            print("Sending file done")
            print("Running file")

          res = conn.recv(1024)
          print(res)
          if res == b"Running data complete":
            if config.DEBUG:
              print("Running file complete")
            continue
          else:
            raise
        except KeyboardInterrupt:
          break
        except:
          if config.DEBUG:
            print("Crash or error occured... Recording file to crash.pkts")
          
          with open("crash.pkts", "wb") as f:
            f.write(cur_data)
          break