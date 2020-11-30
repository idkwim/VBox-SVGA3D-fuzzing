#!/usr/bin/python3

import socket
import subprocess
import random

import config
import converter
import generator

if __name__ == "__main__":
  # start target program (VBox, VMware)
  # TODO: recovery method
  
  # start socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", config.FUZZ_PORT))

    if config.DEBUG:
      print('Waiting for connection...')

    s.listen()
    conn, addr = s.accept()
    with conn:
      if config.DEBUG:
        print('Connected by', addr)
      
      while True:
        if config.DEBUG:
          print("running file")

        # generate file (cur.pkts)
        # TODO: implement generation of data
        

        cur_data = b""
        # for i in config.PKT_SIZE:
        #   cur_data += 

        with open("cur.pkts", "wb") as f:
          cur_data = f.write(cur_data)

        try:
          conn.sendall(cur_data)

          if config.DEBUG:
            print("Sending file done")

          if conn.recv(1024):
            continue
        except KeyboardInterrupt:
          break
        except:
          with open("crash.pkts", "wb") as f:
            f.write(cur_data)
          break