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

        if config.DEBUG:
          print("Generating file...")
        
        cur_data = b""
        data_len = 0
        # don't allow files larger than max file size (including null byte)
        while data_len >= config.MAX_FILE_SIZE or data_len == 0:
          for i in range(config.PKT_SIZE):
            cur_data += generator.gen_cmd()
          data_len = len(cur_data)
        
        if config.DEBUG:
          print("Generation complete - file length : " + str(data_len))

        with open("cur.pkts", "wb") as f:
          f.write(cur_data)

        try:
          conn.sendall(generator.p32(len(cur_data))+cur_data)

          if config.DEBUG:
            print("Sending file done")
            print("Running file")

          if conn.recv(1024):
            if config.DEBUG:
              print("Running file complete")
            continue
        except KeyboardInterrupt:
          break
        except:
          if config.DEBUG:
            print("Crash or error occured... Recording file to crash.pkts")
          
          with open("crash.pkts", "wb") as f:
            f.write(cur_data)
          break