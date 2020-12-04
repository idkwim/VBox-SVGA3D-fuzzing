#!/usr/bin/python3

# network info
GUEST_IP = "10.0.2.15"
HOST_IP = "10.0.2.2"
FUZZ_PORT = 31337
MAX_FILE_SIZE = 0x20000

# gen info
PKT_SIZE = 100 # packet size
BOUNDARY_PROB = 95 # boundary value probability (max=100)
ALLOW_OOB_IDS = False # allow out of bounds ids (sid, cid, shid)
ALLOW_OOB_ENUMS = False # allow out of bounds enums
ALLOW_OOB_CMDS = False # allow out of bounds commands

MAX_N_DEFINE_3D = 7 # max number of dsizes in 3d define surface command
MAX_N_COPY_3D = 10 # max number of copyboxes in 3d surface copy command
MAX_N_DMA_3D = 10 # max number of copyboxes in 3d surface DMA command
MAX_N_SETRENDERSTATE_3D = 10 # max number of renderstates in 3d setrenderstate command
MAX_N_SETTEXTURESTATE_3D = 10 # max number of texturestates in 3d settexturestate command
MAX_N_CLEAR_3D = 10 # max number of rects in 3d clear command
MAX_N_PRESENT_3D = 10 # max number of rects in 3d present command
MAX_N_SETSHADERCONST_3D = 10 # max number of registers in 3d setshader const command
MAX_N_DRAWPRIMITIVE_VERTEXDECL_3D = 10 # max number of vertex decls in 3d drawprimitive command
MAX_N_DRAWPRIMITIVE_NUMRANGE_3D = 10 # max number of vertex decls in 3d drawprimitive command
MAX_N_DRAWPRIMITIVE_DIVISOR_3D = 10 # max number of vertex decls in 3d drawprimitive command
MAX_N_BLITSCREEN_3D = 10 # max number of signed rects in 3d blittoscreen command
MAX_N_DEFINEV2_3D = 7 # max number of dsizes in 3d define surface v2 command

# debug info
INDENT_SPACE = 2 # num of spaces per indent
DEBUG=True