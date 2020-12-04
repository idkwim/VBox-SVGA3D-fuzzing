#!/usr/bin/python3

import generator
import printer

def test_cmd_error():
  for i in list(range(1040, 1072))+[1080, 1081]:
    print("TESTING CMD " + str(i))
    cmd = generator.gen_cmd(i)
    assert len(cmd) != 0
  print("TESTING INVALID CMD 1082")
  cmd = generator.gen_cmd(1082)
  assert len(cmd) == 0

def test_print_cmd():
  for i in list(range(1040, 1072))+[1080, 1081, 1082]:
    print("TESTING CMD " + str(i))
    cmd = printer.print_cmd(generator.gen_cmd(i))

if __name__ == "__main__":
  # test codes

  # generator test codes
  # test_cmd_error()

  # printer test codes
  test_print_cmd()