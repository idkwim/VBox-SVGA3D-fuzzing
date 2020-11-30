#!/usr/bin/python3

import random
import struct
import inspect
import ctypes

import svga_reg
import svga3d_reg

import config
import printer

def choose_random(rand1, rand2):
  return random.choices([rand1, rand2], weights=(config.BOUNDARY_PROB, 100-config.BOUNDARY_PROB))[0]

def random_float():
  rand1 = random.choice([float('inf'), float('-inf'), 0.0])
  rand2 = struct.unpack('!f', struct.pack('!I', random.getrandbits(32)))[0]
  return choose_random(rand1, rand2)

def random_double():
  rand1 = random.choice([float('inf'), float('-inf'), 0.0])
  rand2 = struct.unpack('!d', struct.pack('!I', random.getrandbits(64)))[0]
  return choose_random(rand1, rand2)

def random_bool():
  return random.choice([True, False])

def random_int(numbits):
  rand1 = random.choice([0, (1 << numbits) - 1])
  rand2 = random.getrandbits(numbits)
  return choose_random(rand1, rand2)

# Given a reference object, generate randomized object based on that
def rand_ctypes_obj_rec(prefix, obj):
  if issubclass(type(obj), ctypes.Array): # array type
    args = []
    for obj2 in obj:
      elem = rand_ctypes_obj_rec(prefix, obj2)
      if elem == None:
        break
      args.append(elem)
    if len(args) != 0:
      return (type(args[0])*len(args))(*args)
    else: # primitive types
      typename = type(next(iter(obj), None)).__name__
      if typename == "float": # TODO: double
        return type(obj)(*[random_float() for i in range(len(obj))])
      elif typename == "int": # TODO: adapt this routine with custom numbits
        return type(obj)(*[random_int(32) for i in range(len(obj))])
      else:
        print("Exception occured: Invalid primitive type array : " + typename)
        raise ValueError

  elif hasattr(obj, '_fields_'): # obj type
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
        # random
        if "float" in ftype.__name__:
          res = random_float()
        elif "double" in ftype.__name__:
          res = random_double()
        elif "bool" in ftype.__name__:
          res = random_bool()
        elif "c_int" == ftype.__name__: # enum types may exist
          try:
            enum_name = varlist[idx].split(", ")[1].replace("),", "")+"__enumvalues"
            enum_dict = eval(prefix+"."+enum_name)
            if False in [bin(x).count("1") == 1 for x in enum_dict.keys()]:
              rand1 = random.getrandbits(fbitlen)
              rand2 = random.choice(list(enum_dict.keys()))
              res = choose_random(rand1, rand2)
            else:
              maxbits = len(bin(max(enum_dict.keys()))) - 2 # -2 to remove "0b"
              rand1 = random.getrandbits(fbitlen)
              rand2 = random.getrandbits(maxbits)
              res = choose_random(rand1, rand2)
          except: # enum type doesn't exist
            res = random_int(fbitlen)
        else:
          res = random_int(fbitlen)
      args.append(res)
    return eval(prefix+"."+obj.__class__.__name__+"(*args)") # TODO: improve this

  else:
    return None # endpoint of recursion

# Generate randomized object based on given class name
# Use example : rand_ctypes_obj("SVGA3dCmdDefineSurface")
def rand_ctypes_obj(cname):
  if cname in svga3d_reg.__all__:
    return rand_ctypes_obj_rec("svga3d_reg", eval("svga3d_reg."+cname+"()"))
  elif cname in svga_reg.__all__:
    return rand_ctypes_obj_rec("svga_reg", eval("svga_reg."+cname+"()"))
  else:
    return None # fails

def p32(d):
  return bytes(ctypes.c_uint32(d))

def pack_obj_list(li):
  return b"".join([bytes(i) for i in li])

def pack_cmd(cmd, pay):
  return p32(cmd)+p32(len(pay))+pay

# This part is written manually
# May change due to versions of targets
def gen_cmd(testcmd=0):
  # random command id
  rand1 = random_int(32)
  rand2 = random.randint(1040, 1040+41) # commands are defined in this range (3D)
  cmd = choose_random(rand1, rand2) if testcmd == 0 else testcmd

  # switch
  if cmd == 1040: # SVGA_3D_CMD_SURFACE_DEFINE
    pCmd = rand_ctypes_obj("SVGA3dCmdDefineSurface")
    dsizes = [rand_ctypes_obj("SVGA3dSize") for i in range(random.randint(0, config.MAX_N_DEFINE_3D))]
    pay = bytes(pCmd)+pack_obj_list(dsizes)
    return pack_cmd(cmd, pay)
  elif cmd == 1041: # SVGA_3D_CMD_SURFACE_DESTROY
    pCmd = rand_ctypes_obj("SVGA3dCmdDestroySurface")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1042: # SVGA_3D_CMD_SURFACE_COPY
    pCmd = rand_ctypes_obj("SVGA3dCmdSurfaceCopy")
    copyBoxes = [rand_ctypes_obj("SVGA3dCopyBox") for i in range(random.randint(0, config.MAX_N_COPY_3D))]
    pay = bytes(pCmd)+pack_obj_list(copyBoxes)
    return pack_cmd(cmd, pay)
  elif cmd == 1043: # SVGA_3D_CMD_SURFACE_STRETCHBLT
    pCmd = rand_ctypes_obj("SVGA3dCmdSurfaceStretchBlt")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1044: # SVGA_3D_CMD_SURFACE_DMA
    pCmd = rand_ctypes_obj("SVGA3dCmdSurfaceDMA")
    copyBoxes = [rand_ctypes_obj("SVGA3dCopyBox") for i in range(random.randint(0, config.MAX_N_DMA_3D))]
    pay = bytes(pCmd)+pack_obj_list(copyBoxes)
    return pack_cmd(cmd, pay)
  elif cmd == 1045: # SVGA_3D_CMD_CONTEXT_DEFINE
    pCmd = rand_ctypes_obj("SVGA3dCmdDefineContext")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1046: # SVGA_3D_CMD_CONTEXT_DESTROY
    pCmd = rand_ctypes_obj("SVGA3dCmdDestroyContext")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1047: # SVGA_3D_CMD_SETTRANSFORM
    pCmd = rand_ctypes_obj("SVGA3dCmdSetTransform")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1048: # SVGA_3D_CMD_SETZRANGE
    pCmd = rand_ctypes_obj("SVGA3dCmdSetZRange")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1049: # SVGA_3D_CMD_SETRENDERSTATE
    pCmd = rand_ctypes_obj("SVGA3dCmdSetRenderState")
    renderStates = [rand_ctypes_obj("SVGA3dRenderState") for i in range(random.randint(0, config.MAX_N_SETRENDERSTATE_3D))]
    pay = bytes(pCmd)+pack_obj_list(renderStates)
    return pack_cmd(cmd, pay)
  elif cmd == 1050: # SVGA_3D_CMD_SETRENDERTARGET
    pCmd = rand_ctypes_obj("SVGA3dCmdSetRenderTarget")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1051: # SVGA_3D_CMD_SETTEXTURESTATE
    pCmd = rand_ctypes_obj("SVGA3dCmdSetTextureState")
    textureStates = [rand_ctypes_obj("SVGA3dTextureState") for i in range(random.randint(0, config.MAX_N_SETTEXTURESTATE_3D))]
    pay = bytes(pCmd)+pack_obj_list(textureStates)
    return pack_cmd(cmd, pay)
  elif cmd == 1052: # SVGA_3D_CMD_SETMATERIAL
    pCmd = rand_ctypes_obj("SVGA3dCmdSetMaterial")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1053: # SVGA_3D_CMD_SETLIGHTDATA
    pCmd = rand_ctypes_obj("SVGA3dCmdSetLightData")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1054: # SVGA_3D_CMD_SETLIGHTENABLED
    pCmd = rand_ctypes_obj("SVGA3dCmdSetLightEnabled")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1055: # SVGA_3D_CMD_SETVIEWPORT
    pCmd = rand_ctypes_obj("SVGA3dCmdSetViewport")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1056: # SVGA_3D_CMD_SETCLIPPLANE
    pCmd = rand_ctypes_obj("SVGA3dCmdSetClipPlane")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1057: # SVGA_3D_CMD_CLEAR
    pCmd = rand_ctypes_obj("SVGA3dCmdClear")
    rects = [rand_ctypes_obj("SVGA3dRect") for i in range(random.randint(0, config.MAX_N_CLEAR_3D))]
    pay = bytes(pCmd)+pack_obj_list(rects)
    return pack_cmd(cmd, pay)
  elif cmd == 1058 or cmd == 1068: # SVGA_3D_CMD_PRESENT or SVGA_3D_CMD_PRESENT_READBACK
    pCmd = rand_ctypes_obj("SVGA3dCmdPresent")
    rects = [rand_ctypes_obj("SVGA3dCopyRect") for i in range(random.randint(0, config.MAX_N_PRESENT_3D))]
    pay = bytes(pCmd)+pack_obj_list(rects)
    return pack_cmd(cmd, pay)
  elif cmd == 1059: # SVGA_3D_CMD_SHADER_DEFINE
    pCmd = rand_ctypes_obj("SVGA3dCmdDefineShader")
    cbData = random_int(32)
    pay = bytes(pCmd)+p32(cbData)
    return pack_cmd(cmd, pay)
  elif cmd == 1060: # SVGA_3D_CMD_SHADER_DESTROY
    pCmd = rand_ctypes_obj("SVGA3dCmdDestroyShader")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1061: # SVGA_3D_CMD_SET_SHADER
    pCmd = rand_ctypes_obj("SVGA3dCmdSetShader")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1062: # SVGA_3D_CMD_SET_SHADER_CONST
    pCmd = rand_ctypes_obj("SVGA3dCmdSetShaderConst")
    registers = [ctypes.c_uint32(random_int(32)) for i in range(random.randint(0, config.MAX_N_SETSHADERCONST_3D)*4)]
    pay = bytes(pCmd)+pack_obj_list(registers)
    return pack_cmd(cmd, pay)
  elif cmd == 1063: # SVGA_3D_CMD_DRAW_PRIMITIVES
    # Easier to manually randomize here
    cid = random_int(32)
    numVertexDecls = random.randint(0, config.MAX_N_DRAWPRIMITIVE_VERTEXDECL_3D)
    numRanges = random.randint(0, config.MAX_N_DRAWPRIMITIVE_NUMRANGE_3D)

    vertexDecls = [rand_ctypes_obj("SVGA3dVertexDecl") for i in range(numVertexDecls)]
    ranges = [rand_ctypes_obj("SVGA3dPrimitiveRange") for i in range(numRanges)]
    vertexDivisor = random.randint(0, config.MAX_N_DRAWPRIMITIVE_DIVISOR_3D)
    
    pay = b""
    pay += p32(cid)+p32(numVertexDecls)+p32(numRanges)
    pay += pack_obj_list(vertexDecls)
    pay += pack_obj_list(ranges)
    pay += p32(vertexDivisor)
    return pack_cmd(cmd, pay)
  elif cmd == 1064: # SVGA_3D_CMD_SETSCISSORRECT
    pCmd = rand_ctypes_obj("SVGA3dCmdSetScissorRect")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1065: # SVGA_3D_CMD_BEGIN_QUERY
    pCmd = rand_ctypes_obj("SVGA3dCmdBeginQuery")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1066: # SVGA_3D_CMD_END_QUERY
    pCmd = rand_ctypes_obj("SVGA3dCmdEndQuery")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1067: # SVGA_3D_CMD_WAIT_FOR_QUERY
    pCmd = rand_ctypes_obj("SVGA3dCmdWaitForQuery")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  # SVGA_3D_CMD_PRESENT_READBACK is done already
  elif cmd == 1069: # SVGA_3D_CMD_BLIT_SURFACE_TO_SCREEN
    pCmd = rand_ctypes_obj("SVGA3dCmdBlitSurfaceToScreen")
    rects = [rand_ctypes_obj("SVGASignedRect") for i in range(random.randint(0, config.MAX_N_BLITSCREEN_3D))]
    pay = bytes(pCmd)+pack_obj_list(rects)
    return pack_cmd(cmd, pay)
  elif cmd == 1070: # SVGA_3D_CMD_SURFACE_DEFINE_V2
    pCmd = rand_ctypes_obj("SVGA3dCmdDefineSurface_v2")
    dsizes = [rand_ctypes_obj("SVGA3dSize") for i in range(random.randint(0, config.MAX_N_DEFINEV2_3D))]
    pay = bytes(pCmd)+pack_obj_list(dsizes)
    return pack_cmd(cmd, pay)
  elif cmd == 1071: # SVGA_3D_CMD_GENERATE_MIPMAPS
    pCmd = rand_ctypes_obj("SVGA3dCmdGenerateMipmaps")
    pay = bytes(pCmd)
    return pack_cmd(cmd, pay)
  elif cmd == 1072: # SVGA_3D_CMD_ACTIVATE_SURFACE
    return pack_cmd(cmd, b"")
  elif cmd == 1073: # SVGA_3D_CMD_DEACTIVATE_SURFACE
    return pack_cmd(cmd, b"")
  
  return None

