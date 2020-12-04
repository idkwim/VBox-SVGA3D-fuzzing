#!/usr/bin/python3

import ctypes

import svga_reg
import svga3d_reg

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

def gen_issue_3():
  cmd = b""
  cmd += generator.p32(1040) # SVGA_3D_CMD_SURFACE_DEFINE
  cmd += generator.p32(48) # header size

  surfaceFaces = (svga3d_reg.SVGA3dSurfaceFace*6)( \
    svga3d_reg.SVGA3dSurfaceFace(1), \
    svga3d_reg.SVGA3dSurfaceFace(0), \
    svga3d_reg.SVGA3dSurfaceFace(0), \
    svga3d_reg.SVGA3dSurfaceFace(0), \
    svga3d_reg.SVGA3dSurfaceFace(0), \
    svga3d_reg.SVGA3dSurfaceFace(0) \
  )
  cmd += bytes(svga3d_reg.SVGA3dCmdDefineSurface(0, 2, 37, surfaceFaces))
  cmd += bytes(svga3d_reg.SVGA3dSize(-1, -1, -1))

  cmd += generator.p32(1040) # SVGA_3D_CMD_SURFACE_DEFINE
  cmd += generator.p32(48) # header size
  cmd += bytes(svga3d_reg.SVGA3dCmdDefineSurface(1, 2, 37, surfaceFaces))
  cmd += bytes(svga3d_reg.SVGA3dSize(-1, -1, -1))

  cmd += generator.p32(1043) # SVGA_3D_CMD_SURFACE_STRETCHBLT
  cmd += generator.p32(ctypes.sizeof(svga3d_reg.SVGA3dCmdSurfaceStretchBlt)) # header size
  cmd += bytes(svga3d_reg.SVGA3dCmdSurfaceStretchBlt( \
    svga3d_reg.SVGA3dSurfaceImageId(0, 0, 0), \
    svga3d_reg.SVGA3dSurfaceImageId(1, 0, 0), \
    svga3d_reg.SVGA3dBox(0, 0, 0, 1, 1, 1), \
    svga3d_reg.SVGA3dBox(0, 0, 0, 1, 1, 1), \
    0 \
  ))

  cmd += generator.p32(1044) # SVGA_3D_CMD_SURFACE_DMA
  cmd += generator.p32(64) # header size
  cmd += bytes(svga3d_reg.SVGA3dCmdSurfaceDMA( \
    svga3d_reg.SVGA3dGuestImage(svga3d_reg.struct_SVGAGuestPtr(-2, 0), 0), \
    svga3d_reg.SVGA3dSurfaceImageId(0, 0, 0), \
    2 \
  ))
  cmd += bytes(svga3d_reg.SVGA3dCopyBox(0, 0, 0, 1, 1, 1, 0, 0, 0))
  
  return cmd

if __name__ == "__main__":
  # test codes

  # generator test codes
  # test_cmd_error()

  # printer test codes
  # test_print_cmd()

  # issue-3
  raw = gen_issue_3()
  with open("issue-3.pkts", "wb") as f:
    f.write(raw)
  while len(raw) > 0:
    raw = printer.print_cmd(raw)