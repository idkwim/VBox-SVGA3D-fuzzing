#!/usr/bin/python3

import random
import struct
import inspect

import svga_reg
import svga3d_reg

import config

# Given a reference object, generate randomized object based on that
def rand_ctypes_obj_rec(prefix, obj):
  # Assess wether the object is an array, a structure or an elementary type
  if issubclass(type(obj), ctypes.Array):
    args = []
    for obj2 in obj:
      args.append(rand_ctypes_obj_rec(prefix, obj2))
    return (type(args[0])*len(args))(*args)

  elif hasattr(obj, '_fields_'):
    args = []
    for idx, fdesc in enumerate(obj._fields_):
      # Get the next field descriptor
      fname = fdesc[0]
      ftype = fdesc[1]
      varlist = inspect.getsource(obj.__class__).split("\n")[3:-2]
      if len(fdesc) == 3:
        fbitlen = fdesc[2]
      else:
        fbitlen = 8*ctypes.sizeof(ftype)
      obj2 = getattr(obj, fname)
      res = rand_ctypes_obj_rec(prefix, obj2)
      if res == None:
        # resolve enum name
        enum_name = varlist[idx].split(", ")[1].replace("),", "")+"__enumvalues"
        
        # random
        if "float" in ftype.__name__:
          rand1 = random.choice([float('inf'), float('-inf'), 0.0])
          rand2 = struct.unpack('!f', struct.pack('!I', random.getrandbits(fbitlen)))[0]
          res = random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]
        elif "double" in ftype.__name__:
          rand1 = random.choice([float('inf'), float('-inf'), 0.0])
          rand2 = struct.unpack('!d', struct.pack('!I', random.getrandbits(fbitlen)))[0]
          res = random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]
        elif "bool" in ftype.__name__:
          res = random.choice([True, False])
        elif "c_int" == ftype.__name__: # enum types may exist
          try:
            enum_dict = eval(prefix+"."+enum_name)
            if False in [bin(x).count("1") == 1 for x in enum_dict.keys()]:
              print(enum_name, enum_dict.keys())
              rand1 = random.getrandbits(fbitlen)
              rand2 = random.choice(list(enum_dict.keys()))
              print(rand2)
              res = random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]
            else:
              maxbits = len(bin(max(enum_dict.keys()))) - 2 # -2 to remove "0b"
              rand1 = random.getrandbits(fbitlen)
              rand2 = random.getrandbits(maxbits)
              res = random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]
          except: # enum type doesn't exist
            rand1 = random.choice([0, (1 << fbitlen) - 1])
            rand2 = random.getrandbits(fbitlen)
            res = random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]
        else:
          rand1 = random.choice([0, (1 << fbitlen) - 1])
          rand2 = random.getrandbits(fbitlen)
          res = random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]
      args.append(res)
    return eval(prefix+"."+obj.__class__.__name__+"(*args)") # TODO: improve this

  else:
    return None # endpoint of recursion

# Generate randomized object based on given class name
def rand_ctypes_obj(cname):
  if cname in svga3d_reg.__all__:
    return rand_ctypes_obj_rec("svga3d_reg", eval("svga3d_reg."+cname+"()"))
  elif cname in svga_reg.__all__:
    return rand_ctypes_obj_rec("svga_reg", eval("svga_reg."+cname+"()"))
  else:
    return None # fails


# mini tests
import printer
import ctypes

if __name__ == "__main__":
  printer.print_ctypes_obj(rand_ctypes_obj("SVGA3dCmdDefineSurface"))
