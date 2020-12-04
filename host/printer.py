#!/usr/bin/python3

import sys
import ctypes
import config
import struct

import svga3d_reg
import svga_reg

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

def resolve_name(typename):
  if typename in svga3d_reg.__all__:
    return eval("svga3d_reg."+typename)
  elif typename in svga_reg.__all__:
    return eval("svga_reg."+typename)
  else:
    try:
      return eval("ctypes."+typename) # TODO: improve this, WARNING: unsafe way to handle this
    except:
      return None # fails

def consume_and_print(pay, typename):
  tp = resolve_name(typename)
  if tp is None:
    return None
  print_ctypes_obj(tp.from_buffer(bytearray(pay[:ctypes.sizeof(tp)])))
  return pay[ctypes.sizeof(tp):]

def u32(p):
  return struct.unpack("<I", p)[0]

# prints commands in a readable way
def print_cmd(raw):
  cmd = u32(raw[0:4])
  hdrsize = u32(raw[4:8])
  pay = raw[8:hdrsize+8]
  assert hdrsize % 4 == 0

  delta_indent = " "*config.INDENT_SPACE

  # switch
  if cmd == 1040: # SVGA_3D_CMD_SURFACE_DEFINE
    print("SVGA_3D_CMD_SURFACE_DEFINE")
    pay = consume_and_print(pay, "SVGA3dCmdDefineSurface")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dSize"))):
      pay = consume_and_print(pay, "SVGA3dSize")
  elif cmd == 1041: # SVGA_3D_CMD_SURFACE_DESTROY
    print("SVGA_3D_CMD_SURFACE_DESTROY")
    pay = consume_and_print(pay, "SVGA3dCmdDestroySurface")
  elif cmd == 1042: # SVGA_3D_CMD_SURFACE_COPY
    print("SVGA_3D_CMD_SURFACE_COPY")
    pay = consume_and_print(pay, "SVGA3dCmdSurfaceCopy")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dSize"))):
      pay = consume_and_print(pay, "SVGA3dSize")
  elif cmd == 1043: # SVGA_3D_CMD_SURFACE_STRETCHBLT
    print("SVGA_3D_CMD_SURFACE_STRETCHBLT")
    pay = consume_and_print(pay, "SVGA3dCmdSurfaceStretchBlt")
  elif cmd == 1044: # SVGA_3D_CMD_SURFACE_DMA
    print("SVGA_3D_CMD_SURFACE_DMA")
    pay = consume_and_print(pay, "SVGA3dCmdSurfaceDMA")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dCopyBox"))):
      pay = consume_and_print(pay, "SVGA3dCopyBox")
  elif cmd == 1045: # SVGA_3D_CMD_CONTEXT_DEFINE
    print("SVGA_3D_CMD_CONTEXT_DEFINE")
    pay = consume_and_print(pay, "SVGA3dCmdDefineContext")
  elif cmd == 1046: # SVGA_3D_CMD_CONTEXT_DESTROY
    print("SVGA_3D_CMD_CONTEXT_DESTROY")
    pay = consume_and_print(pay, "SVGA3dCmdDestroyContext")
  elif cmd == 1047: # SVGA_3D_CMD_SETTRANSFORM
    print("SVGA_3D_CMD_SETTRANSFORM")
    pay = consume_and_print(pay, "SVGA3dCmdSetTransform")
  elif cmd == 1048: # SVGA_3D_CMD_SETZRANGE
    print("SVGA_3D_CMD_SETZRANGE")
    pay = consume_and_print(pay, "SVGA3dCmdSetZRange")
  elif cmd == 1049: # SVGA_3D_CMD_SETRENDERSTATE
    print("SVGA_3D_CMD_SETRENDERSTATE")
    pay = consume_and_print(pay, "SVGA3dCmdSetRenderState")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dRenderState"))):
      pay = consume_and_print(pay, "SVGA3dRenderState")
  elif cmd == 1050: # SVGA_3D_CMD_SETRENDERTARGET
    print("SVGA_3D_CMD_SETRENDERTARGET")
    pay = consume_and_print(pay, "SVGA3dCmdSetRenderTarget")
  elif cmd == 1051: # SVGA_3D_CMD_SETTEXTURESTATE
    print("SVGA_3D_CMD_SETTEXTURESTATE")
    pay = consume_and_print(pay, "SVGA3dCmdSetTextureState")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dTextureState"))):
      pay = consume_and_print(pay, "SVGA3dTextureState")
  elif cmd == 1052: # SVGA_3D_CMD_SETMATERIAL
    print("SVGA_3D_CMD_SETMATERIAL")
    pay = consume_and_print(pay, "SVGA3dCmdSetMaterial")
  elif cmd == 1053: # SVGA_3D_CMD_SETLIGHTDATA
    print("SVGA_3D_CMD_SETLIGHTDATA")
    pay = consume_and_print(pay, "SVGA3dCmdSetLightData")
  elif cmd == 1054: # SVGA_3D_CMD_SETLIGHTENABLED
    print("SVGA_3D_CMD_SETLIGHTENABLED")
    pay = consume_and_print(pay, "SVGA3dCmdSetLightEnabled")
  elif cmd == 1055: # SVGA_3D_CMD_SETVIEWPORT
    print("SVGA_3D_CMD_SETVIEWPORT")
    pay = consume_and_print(pay, "SVGA3dCmdSetViewport")
  elif cmd == 1056: # SVGA_3D_CMD_SETCLIPPLANE
    print("SVGA_3D_CMD_SETCLIPPLANE")
    pay = consume_and_print(pay, "SVGA3dCmdSetClipPlane")
  elif cmd == 1057: # SVGA_3D_CMD_CLEAR
    print("SVGA_3D_CMD_CLEAR")
    pay = consume_and_print(pay, "SVGA3dCmdClear")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dRect"))):
      pay = consume_and_print(pay, "SVGA3dRect")
  elif cmd == 1058 or cmd == 1068: # SVGA_3D_CMD_PRESENT or SVGA_3D_CMD_PRESENT_READBACK
    if cmd == 1058:
      print("SVGA_3D_CMD_PRESENT")
    else:
      print("SVGA_3D_CMD_PRESENT_READBACK")
    pay = consume_and_print(pay, "SVGA3dCmdPresent")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dCopyRect"))):
      pay = consume_and_print(pay, "SVGA3dCopyRect")
  elif cmd == 1059: # SVGA_3D_CMD_SHADER_DEFINE
    print("SVGA_3D_CMD_SHADER_DEFINE")
    pay = consume_and_print(pay, "SVGA3dCmdDefineShader")
    for i in range(0, len(pay), ctypes.sizeof(ctypes.c_uint32)):
      pay = consume_and_print(pay, "c_uint32")
  elif cmd == 1060: # SVGA_3D_CMD_SHADER_DESTROY
    print("SVGA_3D_CMD_SHADER_DESTROY")
    pay = consume_and_print(pay, "SVGA3dCmdDestroyShader")
  elif cmd == 1061: # SVGA_3D_CMD_SET_SHADER
    print("SVGA_3D_CMD_SET_SHADER")
    pay = consume_and_print(pay, "SVGA3dCmdSetShader")
  elif cmd == 1062: # SVGA_3D_CMD_SET_SHADER_CONST
    print("SVGA_3D_CMD_SET_SHADER_CONST")
    pay = consume_and_print(pay, "SVGA3dCmdSetShaderConst")
    for i in range(0, len(pay), ctypes.sizeof(ctypes.c_uint32)):
      pay = consume_and_print(pay, "c_uint32")
  elif cmd == 1063: # SVGA_3D_CMD_DRAW_PRIMITIVES
    print("SVGA_3D_CMD_DRAW_PRIMITIVES")
    consume_and_print(pay, "SVGA3dCmdDrawPrimitives")
    # Easier to manually randomize here
    numVertexDecls = u32(pay[4:8])
    numRanges = u32(pay[8:0xc])
    pay = pay[0xc:]
    for i in range(numVertexDecls):
      pay = consume_and_print(pay, "SVGA3dVertexDecl")
    for i in range(numRanges):
      pay = consume_and_print(pay, "SVGA3dPrimitiveRange")
    print("FIELD cVertexDivisor", ctypes.c_uint32)
    print(delta_indent, "VALUE = "+str(u32(pay[:4])))
  elif cmd == 1064: # SVGA_3D_CMD_SETSCISSORRECT
    print("SVGA_3D_CMD_SETSCISSORRECT")
    pay = consume_and_print(pay, "SVGA3dCmdSetScissorRect")
  elif cmd == 1065: # SVGA_3D_CMD_BEGIN_QUERY
    print("SVGA_3D_CMD_BEGIN_QUERY")
    pay = consume_and_print(pay, "SVGA3dCmdBeginQuery")
  elif cmd == 1066: # SVGA_3D_CMD_END_QUERY
    print("SVGA_3D_CMD_END_QUERY")
    pay = consume_and_print(pay, "SVGA3dCmdEndQuery")
  elif cmd == 1067: # SVGA_3D_CMD_WAIT_FOR_QUERY
    print("SVGA_3D_CMD_WAIT_FOR_QUERY")
    pay = consume_and_print(pay, "SVGA3dCmdWaitForQuery")
  # SVGA_3D_CMD_PRESENT_READBACK is done already
  elif cmd == 1069: # SVGA_3D_CMD_BLIT_SURFACE_TO_SCREEN
    print("SVGA_3D_CMD_BLIT_SURFACE_TO_SCREEN")
    pay = consume_and_print(pay, "SVGA3dCmdBlitSurfaceToScreen")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGASignedRect"))):
      pay = consume_and_print(pay, "SVGASignedRect")
  elif cmd == 1070: # SVGA_3D_CMD_SURFACE_DEFINE_V2
    print("SVGA_3D_CMD_SURFACE_DEFINE_V2")
    pay = consume_and_print(pay, "SVGA3dCmdDefineSurface_v2")
    for i in range(0, len(pay), ctypes.sizeof(resolve_name("SVGA3dSize"))):
      pay = consume_and_print(pay, "SVGA3dSize")
  elif cmd == 1071: # SVGA_3D_CMD_GENERATE_MIPMAPS
    print("SVGA_3D_CMD_GENERATE_MIPMAPS")
    pay = consume_and_print(pay, "SVGA3dCmdGenerateMipmaps")
  elif cmd == 1080: # SVGA_3D_CMD_ACTIVATE_SURFACE
    print("SVGA_3D_CMD_ACTIVATE_SURFACE")
  elif cmd == 1081: # SVGA_3D_CMD_DEACTIVATE_SURFACE
    print("SVGA_3D_CMD_DEACTIVATE_SURFACE")
  else:
    print("INVALID COMMAND")
  return raw[hdrsize+8:]

if __name__ == "__main__":
  import sys

  if len(sys.argv) != 2:
    print("[*] Usage : python3 printer.py <filename>")

  with open(sys.argv[1], "rb") as f:
    raw = f.read()
  
  cnt = 0
  while len(raw) > 0:
    print("PRINTING CMD", cnt)
    raw = print_cmd(raw)
    cnt += 1
  print("PRINTED", cnt, "Commands")
    