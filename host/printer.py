#!/usr/bin/python3

import sys
import ctypes
import config

# Used to print generated object
# https://stackoverflow.com/questions/26927685/introspecting-nested-ctypes-structures
def print_ctypes_obj(obj, level=0):
  delta_indent=" "*config.INDENT_SPACE
  indent=delta_indent*level

  # Assess wether the object is an array, a structure or an elementary type
  if issubclass(type(obj), ctypes.Array) :
    print('{}ARRAY {}'.format(indent, obj))
    for obj2 in obj:
      print_ctypes_obj(obj2, level+1)

  elif hasattr(obj, '_fields_'):
    print('{}STRUCTURE {}'.format(indent, obj))
    for fdesc in obj._fields_:
      # Get the next field descriptor
      fname = fdesc[0]
      ftype = fdesc[1]
      if len(fdesc)==3:
        fbitlen = fdesc[2]
      else:
        fbitlen = 8*ctypes.sizeof(ftype)
      obj2 = getattr(obj, fname)
      print('{}FIELD {} (type={}, bitlen={})'.format(indent+delta_indent, fname, ftype, fbitlen))
      print_ctypes_obj(obj2, level+2)

  else:
    print('{}VALUE = {} (type={})'.format(indent, obj, type(obj)))
