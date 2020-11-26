#!/usr/bin/python3

import socket
import subprocess
import random

from generator import Generator

import config

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
        with open("cur.pkts", "rb") as f:
          cur_data = f.read()

        if config.DEBUG:
          print("file length :", len(cur_data))

        try:
          if len(cur_data) % 1024 != 0:
            conn.sendall(cur_data)
          else:
            conn.sendall(cur_data + b"over")

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