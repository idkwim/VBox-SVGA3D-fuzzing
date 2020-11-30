#!/usr/bin/python3

import generator
import printer

def test_cmd_error():
  for i in range(1040, 1074):
    print("TESTING CMD " + str(i))
    cmd = generator.gen_cmd(i)
    assert len(cmd) != 0
  print("TESTING INVALID CMD 1074")
  cmd = generator.gen_cmd(1074)
  assert len(cmd) == 0

if __name__ == "__main__":
  # test codes

  # generator test codes
  test_cmd_error()