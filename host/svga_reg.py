# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-std=c99', '-Wall', '-target', 'x86_64']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes





# values for enumeration 'c__Ea_SVGA_REG_ID'
c__Ea_SVGA_REG_ID__enumvalues = {
    0: 'SVGA_REG_ID',
    1: 'SVGA_REG_ENABLE',
    2: 'SVGA_REG_WIDTH',
    3: 'SVGA_REG_HEIGHT',
    4: 'SVGA_REG_MAX_WIDTH',
    5: 'SVGA_REG_MAX_HEIGHT',
    6: 'SVGA_REG_DEPTH',
    7: 'SVGA_REG_BITS_PER_PIXEL',
    8: 'SVGA_REG_PSEUDOCOLOR',
    9: 'SVGA_REG_RED_MASK',
    10: 'SVGA_REG_GREEN_MASK',
    11: 'SVGA_REG_BLUE_MASK',
    12: 'SVGA_REG_BYTES_PER_LINE',
    13: 'SVGA_REG_FB_START',
    14: 'SVGA_REG_FB_OFFSET',
    15: 'SVGA_REG_VRAM_SIZE',
    16: 'SVGA_REG_FB_SIZE',
    17: 'SVGA_REG_CAPABILITIES',
    18: 'SVGA_REG_MEM_START',
    19: 'SVGA_REG_MEM_SIZE',
    20: 'SVGA_REG_CONFIG_DONE',
    21: 'SVGA_REG_SYNC',
    22: 'SVGA_REG_BUSY',
    23: 'SVGA_REG_GUEST_ID',
    24: 'SVGA_REG_CURSOR_ID',
    25: 'SVGA_REG_CURSOR_X',
    26: 'SVGA_REG_CURSOR_Y',
    27: 'SVGA_REG_CURSOR_ON',
    28: 'SVGA_REG_HOST_BITS_PER_PIXEL',
    29: 'SVGA_REG_SCRATCH_SIZE',
    30: 'SVGA_REG_MEM_REGS',
    31: 'SVGA_REG_NUM_DISPLAYS',
    32: 'SVGA_REG_PITCHLOCK',
    33: 'SVGA_REG_IRQMASK',
    34: 'SVGA_REG_NUM_GUEST_DISPLAYS',
    35: 'SVGA_REG_DISPLAY_ID',
    36: 'SVGA_REG_DISPLAY_IS_PRIMARY',
    37: 'SVGA_REG_DISPLAY_POSITION_X',
    38: 'SVGA_REG_DISPLAY_POSITION_Y',
    39: 'SVGA_REG_DISPLAY_WIDTH',
    40: 'SVGA_REG_DISPLAY_HEIGHT',
    41: 'SVGA_REG_GMR_ID',
    42: 'SVGA_REG_GMR_DESCRIPTOR',
    43: 'SVGA_REG_GMR_MAX_IDS',
    44: 'SVGA_REG_GMR_MAX_DESCRIPTOR_LENGTH',
    45: 'SVGA_REG_TRACES',
    46: 'SVGA_REG_GMRS_MAX_PAGES',
    47: 'SVGA_REG_MEMORY_SIZE',
    48: 'SVGA_REG_TOP',
    1024: 'SVGA_PALETTE_BASE',
    1792: 'SVGA_SCRATCH_BASE',
}
SVGA_REG_ID = 0
SVGA_REG_ENABLE = 1
SVGA_REG_WIDTH = 2
SVGA_REG_HEIGHT = 3
SVGA_REG_MAX_WIDTH = 4
SVGA_REG_MAX_HEIGHT = 5
SVGA_REG_DEPTH = 6
SVGA_REG_BITS_PER_PIXEL = 7
SVGA_REG_PSEUDOCOLOR = 8
SVGA_REG_RED_MASK = 9
SVGA_REG_GREEN_MASK = 10
SVGA_REG_BLUE_MASK = 11
SVGA_REG_BYTES_PER_LINE = 12
SVGA_REG_FB_START = 13
SVGA_REG_FB_OFFSET = 14
SVGA_REG_VRAM_SIZE = 15
SVGA_REG_FB_SIZE = 16
SVGA_REG_CAPABILITIES = 17
SVGA_REG_MEM_START = 18
SVGA_REG_MEM_SIZE = 19
SVGA_REG_CONFIG_DONE = 20
SVGA_REG_SYNC = 21
SVGA_REG_BUSY = 22
SVGA_REG_GUEST_ID = 23
SVGA_REG_CURSOR_ID = 24
SVGA_REG_CURSOR_X = 25
SVGA_REG_CURSOR_Y = 26
SVGA_REG_CURSOR_ON = 27
SVGA_REG_HOST_BITS_PER_PIXEL = 28
SVGA_REG_SCRATCH_SIZE = 29
SVGA_REG_MEM_REGS = 30
SVGA_REG_NUM_DISPLAYS = 31
SVGA_REG_PITCHLOCK = 32
SVGA_REG_IRQMASK = 33
SVGA_REG_NUM_GUEST_DISPLAYS = 34
SVGA_REG_DISPLAY_ID = 35
SVGA_REG_DISPLAY_IS_PRIMARY = 36
SVGA_REG_DISPLAY_POSITION_X = 37
SVGA_REG_DISPLAY_POSITION_Y = 38
SVGA_REG_DISPLAY_WIDTH = 39
SVGA_REG_DISPLAY_HEIGHT = 40
SVGA_REG_GMR_ID = 41
SVGA_REG_GMR_DESCRIPTOR = 42
SVGA_REG_GMR_MAX_IDS = 43
SVGA_REG_GMR_MAX_DESCRIPTOR_LENGTH = 44
SVGA_REG_TRACES = 45
SVGA_REG_GMRS_MAX_PAGES = 46
SVGA_REG_MEMORY_SIZE = 47
SVGA_REG_TOP = 48
SVGA_PALETTE_BASE = 1024
SVGA_SCRATCH_BASE = 1792
c__Ea_SVGA_REG_ID = ctypes.c_int # enum
class struct_SVGAGuestMemDescriptor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ppn', ctypes.c_uint32),
    ('numPages', ctypes.c_uint32),
     ]

SVGAGuestMemDescriptor = struct_SVGAGuestMemDescriptor
class struct_SVGAGuestPtr(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gmrId', ctypes.c_uint32),
    ('offset', ctypes.c_uint32),
     ]

SVGAGuestPtr = struct_SVGAGuestPtr
class struct_SVGAGMRImageFormat(ctypes.Structure):
    pass

class union_SVGAGMRImageFormat_0(ctypes.Union):
    pass

class struct_SVGAGMRImageFormat_0_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('bitsPerPixel', ctypes.c_uint32, 8),
    ('colorDepth', ctypes.c_uint32, 8),
    ('reserved', ctypes.c_uint32, 16),
     ]

union_SVGAGMRImageFormat_0._pack_ = True # source:False
union_SVGAGMRImageFormat_0._fields_ = [
    ('s', struct_SVGAGMRImageFormat_0_0),
    ('value', ctypes.c_uint32),
]

struct_SVGAGMRImageFormat._pack_ = True # source:False
struct_SVGAGMRImageFormat._fields_ = [
    ('_0', union_SVGAGMRImageFormat_0),
]

SVGAGMRImageFormat = struct_SVGAGMRImageFormat
class struct_SVGAGuestImage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ptr', SVGAGuestPtr),
    ('pitch', ctypes.c_uint32),
     ]

SVGAGuestImage = struct_SVGAGuestImage
class struct_SVGAColorBGRX(ctypes.Structure):
    pass

class union_SVGAColorBGRX_0(ctypes.Union):
    pass

class struct_SVGAColorBGRX_0_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('b', ctypes.c_uint32, 8),
    ('g', ctypes.c_uint32, 8),
    ('r', ctypes.c_uint32, 8),
    ('x', ctypes.c_uint32, 8),
     ]

union_SVGAColorBGRX_0._pack_ = True # source:False
union_SVGAColorBGRX_0._fields_ = [
    ('s', struct_SVGAColorBGRX_0_0),
    ('value', ctypes.c_uint32),
]

struct_SVGAColorBGRX._pack_ = True # source:False
struct_SVGAColorBGRX._fields_ = [
    ('_0', union_SVGAColorBGRX_0),
]

SVGAColorBGRX = struct_SVGAColorBGRX
class struct_SVGASignedRect(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('left', ctypes.c_int32),
    ('top', ctypes.c_int32),
    ('right', ctypes.c_int32),
    ('bottom', ctypes.c_int32),
     ]

SVGASignedRect = struct_SVGASignedRect
class struct_SVGASignedPoint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_int32),
    ('y', ctypes.c_int32),
     ]

SVGASignedPoint = struct_SVGASignedPoint

# values for enumeration 'c__Ea_SVGA_FIFO_MIN'
c__Ea_SVGA_FIFO_MIN__enumvalues = {
    0: 'SVGA_FIFO_MIN',
    1: 'SVGA_FIFO_MAX',
    2: 'SVGA_FIFO_NEXT_CMD',
    3: 'SVGA_FIFO_STOP',
    4: 'SVGA_FIFO_CAPABILITIES',
    5: 'SVGA_FIFO_FLAGS',
    6: 'SVGA_FIFO_FENCE',
    7: 'SVGA_FIFO_3D_HWVERSION',
    8: 'SVGA_FIFO_PITCHLOCK',
    9: 'SVGA_FIFO_CURSOR_ON',
    10: 'SVGA_FIFO_CURSOR_X',
    11: 'SVGA_FIFO_CURSOR_Y',
    12: 'SVGA_FIFO_CURSOR_COUNT',
    13: 'SVGA_FIFO_CURSOR_LAST_UPDATED',
    14: 'SVGA_FIFO_RESERVED',
    15: 'SVGA_FIFO_CURSOR_SCREEN_ID',
    16: 'SVGA_FIFO_DEAD',
    17: 'SVGA_FIFO_3D_HWVERSION_REVISED',
    32: 'SVGA_FIFO_3D_CAPS',
    287: 'SVGA_FIFO_3D_CAPS_LAST',
    288: 'SVGA_FIFO_GUEST_3D_HWVERSION',
    289: 'SVGA_FIFO_FENCE_GOAL',
    290: 'SVGA_FIFO_BUSY',
    291: 'SVGA_FIFO_NUM_REGS',
}
SVGA_FIFO_MIN = 0
SVGA_FIFO_MAX = 1
SVGA_FIFO_NEXT_CMD = 2
SVGA_FIFO_STOP = 3
SVGA_FIFO_CAPABILITIES = 4
SVGA_FIFO_FLAGS = 5
SVGA_FIFO_FENCE = 6
SVGA_FIFO_3D_HWVERSION = 7
SVGA_FIFO_PITCHLOCK = 8
SVGA_FIFO_CURSOR_ON = 9
SVGA_FIFO_CURSOR_X = 10
SVGA_FIFO_CURSOR_Y = 11
SVGA_FIFO_CURSOR_COUNT = 12
SVGA_FIFO_CURSOR_LAST_UPDATED = 13
SVGA_FIFO_RESERVED = 14
SVGA_FIFO_CURSOR_SCREEN_ID = 15
SVGA_FIFO_DEAD = 16
SVGA_FIFO_3D_HWVERSION_REVISED = 17
SVGA_FIFO_3D_CAPS = 32
SVGA_FIFO_3D_CAPS_LAST = 287
SVGA_FIFO_GUEST_3D_HWVERSION = 288
SVGA_FIFO_FENCE_GOAL = 289
SVGA_FIFO_BUSY = 290
SVGA_FIFO_NUM_REGS = 291
c__Ea_SVGA_FIFO_MIN = ctypes.c_int # enum

# values for enumeration 'c__Ea_SVGA_VIDEO_ENABLED'
c__Ea_SVGA_VIDEO_ENABLED__enumvalues = {
    0: 'SVGA_VIDEO_ENABLED',
    1: 'SVGA_VIDEO_FLAGS',
    2: 'SVGA_VIDEO_DATA_OFFSET',
    3: 'SVGA_VIDEO_FORMAT',
    4: 'SVGA_VIDEO_COLORKEY',
    5: 'SVGA_VIDEO_SIZE',
    6: 'SVGA_VIDEO_WIDTH',
    7: 'SVGA_VIDEO_HEIGHT',
    8: 'SVGA_VIDEO_SRC_X',
    9: 'SVGA_VIDEO_SRC_Y',
    10: 'SVGA_VIDEO_SRC_WIDTH',
    11: 'SVGA_VIDEO_SRC_HEIGHT',
    12: 'SVGA_VIDEO_DST_X',
    13: 'SVGA_VIDEO_DST_Y',
    14: 'SVGA_VIDEO_DST_WIDTH',
    15: 'SVGA_VIDEO_DST_HEIGHT',
    16: 'SVGA_VIDEO_PITCH_1',
    17: 'SVGA_VIDEO_PITCH_2',
    18: 'SVGA_VIDEO_PITCH_3',
    19: 'SVGA_VIDEO_DATA_GMRID',
    20: 'SVGA_VIDEO_DST_SCREEN_ID',
    21: 'SVGA_VIDEO_NUM_REGS',
}
SVGA_VIDEO_ENABLED = 0
SVGA_VIDEO_FLAGS = 1
SVGA_VIDEO_DATA_OFFSET = 2
SVGA_VIDEO_FORMAT = 3
SVGA_VIDEO_COLORKEY = 4
SVGA_VIDEO_SIZE = 5
SVGA_VIDEO_WIDTH = 6
SVGA_VIDEO_HEIGHT = 7
SVGA_VIDEO_SRC_X = 8
SVGA_VIDEO_SRC_Y = 9
SVGA_VIDEO_SRC_WIDTH = 10
SVGA_VIDEO_SRC_HEIGHT = 11
SVGA_VIDEO_DST_X = 12
SVGA_VIDEO_DST_Y = 13
SVGA_VIDEO_DST_WIDTH = 14
SVGA_VIDEO_DST_HEIGHT = 15
SVGA_VIDEO_PITCH_1 = 16
SVGA_VIDEO_PITCH_2 = 17
SVGA_VIDEO_PITCH_3 = 18
SVGA_VIDEO_DATA_GMRID = 19
SVGA_VIDEO_DST_SCREEN_ID = 20
SVGA_VIDEO_NUM_REGS = 21
c__Ea_SVGA_VIDEO_ENABLED = ctypes.c_int # enum
class struct_SVGAOverlayUnit(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('enabled', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('dataOffset', ctypes.c_uint32),
    ('format', ctypes.c_uint32),
    ('colorKey', ctypes.c_uint32),
    ('size', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
    ('srcX', ctypes.c_uint32),
    ('srcY', ctypes.c_uint32),
    ('srcWidth', ctypes.c_uint32),
    ('srcHeight', ctypes.c_uint32),
    ('dstX', ctypes.c_int32),
    ('dstY', ctypes.c_int32),
    ('dstWidth', ctypes.c_uint32),
    ('dstHeight', ctypes.c_uint32),
    ('pitches', ctypes.c_uint32 * 3),
    ('dataGMRId', ctypes.c_uint32),
    ('dstScreenId', ctypes.c_uint32),
     ]

SVGAOverlayUnit = struct_SVGAOverlayUnit
class struct_SVGAScreenObject(ctypes.Structure):
    pass

class struct_SVGAScreenObject_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
     ]

class struct_SVGAScreenObject_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_int32),
    ('y', ctypes.c_int32),
     ]

struct_SVGAScreenObject._pack_ = True # source:False
struct_SVGAScreenObject._fields_ = [
    ('structSize', ctypes.c_uint32),
    ('id', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('size', struct_SVGAScreenObject_0),
    ('root', struct_SVGAScreenObject_1),
    ('backingStore', SVGAGuestImage),
    ('cloneCount', ctypes.c_uint32),
]

SVGAScreenObject = struct_SVGAScreenObject

# values for enumeration 'c__EA_SVGAFifoCmdId'
c__EA_SVGAFifoCmdId__enumvalues = {
    0: 'SVGA_CMD_INVALID_CMD',
    1: 'SVGA_CMD_UPDATE',
    3: 'SVGA_CMD_RECT_COPY',
    19: 'SVGA_CMD_DEFINE_CURSOR',
    22: 'SVGA_CMD_DEFINE_ALPHA_CURSOR',
    25: 'SVGA_CMD_UPDATE_VERBOSE',
    29: 'SVGA_CMD_FRONT_ROP_FILL',
    30: 'SVGA_CMD_FENCE',
    33: 'SVGA_CMD_ESCAPE',
    34: 'SVGA_CMD_DEFINE_SCREEN',
    35: 'SVGA_CMD_DESTROY_SCREEN',
    36: 'SVGA_CMD_DEFINE_GMRFB',
    37: 'SVGA_CMD_BLIT_GMRFB_TO_SCREEN',
    38: 'SVGA_CMD_BLIT_SCREEN_TO_GMRFB',
    39: 'SVGA_CMD_ANNOTATION_FILL',
    40: 'SVGA_CMD_ANNOTATION_COPY',
    41: 'SVGA_CMD_DEFINE_GMR2',
    42: 'SVGA_CMD_REMAP_GMR2',
    43: 'SVGA_CMD_MAX',
}
SVGA_CMD_INVALID_CMD = 0
SVGA_CMD_UPDATE = 1
SVGA_CMD_RECT_COPY = 3
SVGA_CMD_DEFINE_CURSOR = 19
SVGA_CMD_DEFINE_ALPHA_CURSOR = 22
SVGA_CMD_UPDATE_VERBOSE = 25
SVGA_CMD_FRONT_ROP_FILL = 29
SVGA_CMD_FENCE = 30
SVGA_CMD_ESCAPE = 33
SVGA_CMD_DEFINE_SCREEN = 34
SVGA_CMD_DESTROY_SCREEN = 35
SVGA_CMD_DEFINE_GMRFB = 36
SVGA_CMD_BLIT_GMRFB_TO_SCREEN = 37
SVGA_CMD_BLIT_SCREEN_TO_GMRFB = 38
SVGA_CMD_ANNOTATION_FILL = 39
SVGA_CMD_ANNOTATION_COPY = 40
SVGA_CMD_DEFINE_GMR2 = 41
SVGA_CMD_REMAP_GMR2 = 42
SVGA_CMD_MAX = 43
c__EA_SVGAFifoCmdId = ctypes.c_int # enum
SVGAFifoCmdId = c__EA_SVGAFifoCmdId
SVGAFifoCmdId__enumvalues = c__EA_SVGAFifoCmdId__enumvalues
class struct_c__SA_SVGAFifoCmdUpdate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_uint32),
    ('y', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
     ]

SVGAFifoCmdUpdate = struct_c__SA_SVGAFifoCmdUpdate
class struct_c__SA_SVGAFifoCmdRectCopy(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('srcX', ctypes.c_uint32),
    ('srcY', ctypes.c_uint32),
    ('destX', ctypes.c_uint32),
    ('destY', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
     ]

SVGAFifoCmdRectCopy = struct_c__SA_SVGAFifoCmdRectCopy
class struct_c__SA_SVGAFifoCmdDefineCursor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_uint32),
    ('hotspotX', ctypes.c_uint32),
    ('hotspotY', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
    ('andMaskDepth', ctypes.c_uint32),
    ('xorMaskDepth', ctypes.c_uint32),
     ]

SVGAFifoCmdDefineCursor = struct_c__SA_SVGAFifoCmdDefineCursor
class struct_c__SA_SVGAFifoCmdDefineAlphaCursor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_uint32),
    ('hotspotX', ctypes.c_uint32),
    ('hotspotY', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
     ]

SVGAFifoCmdDefineAlphaCursor = struct_c__SA_SVGAFifoCmdDefineAlphaCursor
class struct_c__SA_SVGAFifoCmdUpdateVerbose(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_uint32),
    ('y', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
    ('reason', ctypes.c_uint32),
     ]

SVGAFifoCmdUpdateVerbose = struct_c__SA_SVGAFifoCmdUpdateVerbose
class struct_c__SA_SVGAFifoCmdFrontRopFill(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('color', ctypes.c_uint32),
    ('x', ctypes.c_uint32),
    ('y', ctypes.c_uint32),
    ('width', ctypes.c_uint32),
    ('height', ctypes.c_uint32),
    ('rop', ctypes.c_uint32),
     ]

SVGAFifoCmdFrontRopFill = struct_c__SA_SVGAFifoCmdFrontRopFill
class struct_c__SA_SVGAFifoCmdFence(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('fence', ctypes.c_uint32),
     ]

SVGAFifoCmdFence = struct_c__SA_SVGAFifoCmdFence
class struct_c__SA_SVGAFifoCmdEscape(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('nsid', ctypes.c_uint32),
    ('size', ctypes.c_uint32),
     ]

SVGAFifoCmdEscape = struct_c__SA_SVGAFifoCmdEscape
class struct_c__SA_SVGAFifoCmdDefineScreen(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('screen', SVGAScreenObject),
     ]

SVGAFifoCmdDefineScreen = struct_c__SA_SVGAFifoCmdDefineScreen
class struct_c__SA_SVGAFifoCmdDestroyScreen(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('screenId', ctypes.c_uint32),
     ]

SVGAFifoCmdDestroyScreen = struct_c__SA_SVGAFifoCmdDestroyScreen
class struct_c__SA_SVGAFifoCmdDefineGMRFB(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ptr', SVGAGuestPtr),
    ('bytesPerLine', ctypes.c_uint32),
    ('format', SVGAGMRImageFormat),
     ]

SVGAFifoCmdDefineGMRFB = struct_c__SA_SVGAFifoCmdDefineGMRFB
class struct_c__SA_SVGAFifoCmdBlitGMRFBToScreen(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('srcOrigin', SVGASignedPoint),
    ('destRect', SVGASignedRect),
    ('destScreenId', ctypes.c_uint32),
     ]

SVGAFifoCmdBlitGMRFBToScreen = struct_c__SA_SVGAFifoCmdBlitGMRFBToScreen
class struct_c__SA_SVGAFifoCmdBlitScreenToGMRFB(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('destOrigin', SVGASignedPoint),
    ('srcRect', SVGASignedRect),
    ('srcScreenId', ctypes.c_uint32),
     ]

SVGAFifoCmdBlitScreenToGMRFB = struct_c__SA_SVGAFifoCmdBlitScreenToGMRFB
class struct_c__SA_SVGAFifoCmdAnnotationFill(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('color', SVGAColorBGRX),
     ]

SVGAFifoCmdAnnotationFill = struct_c__SA_SVGAFifoCmdAnnotationFill
class struct_c__SA_SVGAFifoCmdAnnotationCopy(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('srcOrigin', SVGASignedPoint),
    ('srcScreenId', ctypes.c_uint32),
     ]

SVGAFifoCmdAnnotationCopy = struct_c__SA_SVGAFifoCmdAnnotationCopy
class struct_c__SA_SVGAFifoCmdDefineGMR2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gmrId', ctypes.c_uint32),
    ('numPages', ctypes.c_uint32),
     ]

SVGAFifoCmdDefineGMR2 = struct_c__SA_SVGAFifoCmdDefineGMR2

# values for enumeration 'c__EA_SVGARemapGMR2Flags'
c__EA_SVGARemapGMR2Flags__enumvalues = {
    0: 'SVGA_REMAP_GMR2_PPN32',
    1: 'SVGA_REMAP_GMR2_VIA_GMR',
    2: 'SVGA_REMAP_GMR2_PPN64',
    4: 'SVGA_REMAP_GMR2_SINGLE_PPN',
}
SVGA_REMAP_GMR2_PPN32 = 0
SVGA_REMAP_GMR2_VIA_GMR = 1
SVGA_REMAP_GMR2_PPN64 = 2
SVGA_REMAP_GMR2_SINGLE_PPN = 4
c__EA_SVGARemapGMR2Flags = ctypes.c_int # enum
SVGARemapGMR2Flags = c__EA_SVGARemapGMR2Flags
SVGARemapGMR2Flags__enumvalues = c__EA_SVGARemapGMR2Flags__enumvalues
class struct_c__SA_SVGAFifoCmdRemapGMR2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gmrId', ctypes.c_uint32),
    ('flags', SVGARemapGMR2Flags),
    ('offsetPages', ctypes.c_uint32),
    ('numPages', ctypes.c_uint32),
     ]

SVGAFifoCmdRemapGMR2 = struct_c__SA_SVGAFifoCmdRemapGMR2
__all__ = \
    ['SVGAColorBGRX', 'SVGAFifoCmdAnnotationCopy',
    'SVGAFifoCmdAnnotationFill', 'SVGAFifoCmdBlitGMRFBToScreen',
    'SVGAFifoCmdBlitScreenToGMRFB', 'SVGAFifoCmdDefineAlphaCursor',
    'SVGAFifoCmdDefineCursor', 'SVGAFifoCmdDefineGMR2',
    'SVGAFifoCmdDefineGMRFB', 'SVGAFifoCmdDefineScreen',
    'SVGAFifoCmdDestroyScreen', 'SVGAFifoCmdEscape',
    'SVGAFifoCmdFence', 'SVGAFifoCmdFrontRopFill', 'SVGAFifoCmdId',
    'SVGAFifoCmdId__enumvalues', 'SVGAFifoCmdRectCopy',
    'SVGAFifoCmdRemapGMR2', 'SVGAFifoCmdUpdate',
    'SVGAFifoCmdUpdateVerbose', 'SVGAGMRImageFormat',
    'SVGAGuestImage', 'SVGAGuestMemDescriptor', 'SVGAGuestPtr',
    'SVGAOverlayUnit', 'SVGARemapGMR2Flags',
    'SVGARemapGMR2Flags__enumvalues', 'SVGAScreenObject',
    'SVGASignedPoint', 'SVGASignedRect', 'SVGA_CMD_ANNOTATION_COPY',
    'SVGA_CMD_ANNOTATION_FILL', 'SVGA_CMD_BLIT_GMRFB_TO_SCREEN',
    'SVGA_CMD_BLIT_SCREEN_TO_GMRFB', 'SVGA_CMD_DEFINE_ALPHA_CURSOR',
    'SVGA_CMD_DEFINE_CURSOR', 'SVGA_CMD_DEFINE_GMR2',
    'SVGA_CMD_DEFINE_GMRFB', 'SVGA_CMD_DEFINE_SCREEN',
    'SVGA_CMD_DESTROY_SCREEN', 'SVGA_CMD_ESCAPE', 'SVGA_CMD_FENCE',
    'SVGA_CMD_FRONT_ROP_FILL', 'SVGA_CMD_INVALID_CMD', 'SVGA_CMD_MAX',
    'SVGA_CMD_RECT_COPY', 'SVGA_CMD_REMAP_GMR2', 'SVGA_CMD_UPDATE',
    'SVGA_CMD_UPDATE_VERBOSE', 'SVGA_FIFO_3D_CAPS',
    'SVGA_FIFO_3D_CAPS_LAST', 'SVGA_FIFO_3D_HWVERSION',
    'SVGA_FIFO_3D_HWVERSION_REVISED', 'SVGA_FIFO_BUSY',
    'SVGA_FIFO_CAPABILITIES', 'SVGA_FIFO_CURSOR_COUNT',
    'SVGA_FIFO_CURSOR_LAST_UPDATED', 'SVGA_FIFO_CURSOR_ON',
    'SVGA_FIFO_CURSOR_SCREEN_ID', 'SVGA_FIFO_CURSOR_X',
    'SVGA_FIFO_CURSOR_Y', 'SVGA_FIFO_DEAD', 'SVGA_FIFO_FENCE',
    'SVGA_FIFO_FENCE_GOAL', 'SVGA_FIFO_FLAGS',
    'SVGA_FIFO_GUEST_3D_HWVERSION', 'SVGA_FIFO_MAX', 'SVGA_FIFO_MIN',
    'SVGA_FIFO_NEXT_CMD', 'SVGA_FIFO_NUM_REGS', 'SVGA_FIFO_PITCHLOCK',
    'SVGA_FIFO_RESERVED', 'SVGA_FIFO_STOP', 'SVGA_PALETTE_BASE',
    'SVGA_REG_BITS_PER_PIXEL', 'SVGA_REG_BLUE_MASK', 'SVGA_REG_BUSY',
    'SVGA_REG_BYTES_PER_LINE', 'SVGA_REG_CAPABILITIES',
    'SVGA_REG_CONFIG_DONE', 'SVGA_REG_CURSOR_ID',
    'SVGA_REG_CURSOR_ON', 'SVGA_REG_CURSOR_X', 'SVGA_REG_CURSOR_Y',
    'SVGA_REG_DEPTH', 'SVGA_REG_DISPLAY_HEIGHT',
    'SVGA_REG_DISPLAY_ID', 'SVGA_REG_DISPLAY_IS_PRIMARY',
    'SVGA_REG_DISPLAY_POSITION_X', 'SVGA_REG_DISPLAY_POSITION_Y',
    'SVGA_REG_DISPLAY_WIDTH', 'SVGA_REG_ENABLE', 'SVGA_REG_FB_OFFSET',
    'SVGA_REG_FB_SIZE', 'SVGA_REG_FB_START',
    'SVGA_REG_GMRS_MAX_PAGES', 'SVGA_REG_GMR_DESCRIPTOR',
    'SVGA_REG_GMR_ID', 'SVGA_REG_GMR_MAX_DESCRIPTOR_LENGTH',
    'SVGA_REG_GMR_MAX_IDS', 'SVGA_REG_GREEN_MASK',
    'SVGA_REG_GUEST_ID', 'SVGA_REG_HEIGHT',
    'SVGA_REG_HOST_BITS_PER_PIXEL', 'SVGA_REG_ID', 'SVGA_REG_IRQMASK',
    'SVGA_REG_MAX_HEIGHT', 'SVGA_REG_MAX_WIDTH',
    'SVGA_REG_MEMORY_SIZE', 'SVGA_REG_MEM_REGS', 'SVGA_REG_MEM_SIZE',
    'SVGA_REG_MEM_START', 'SVGA_REG_NUM_DISPLAYS',
    'SVGA_REG_NUM_GUEST_DISPLAYS', 'SVGA_REG_PITCHLOCK',
    'SVGA_REG_PSEUDOCOLOR', 'SVGA_REG_RED_MASK',
    'SVGA_REG_SCRATCH_SIZE', 'SVGA_REG_SYNC', 'SVGA_REG_TOP',
    'SVGA_REG_TRACES', 'SVGA_REG_VRAM_SIZE', 'SVGA_REG_WIDTH',
    'SVGA_REMAP_GMR2_PPN32', 'SVGA_REMAP_GMR2_PPN64',
    'SVGA_REMAP_GMR2_SINGLE_PPN', 'SVGA_REMAP_GMR2_VIA_GMR',
    'SVGA_SCRATCH_BASE', 'SVGA_VIDEO_COLORKEY',
    'SVGA_VIDEO_DATA_GMRID', 'SVGA_VIDEO_DATA_OFFSET',
    'SVGA_VIDEO_DST_HEIGHT', 'SVGA_VIDEO_DST_SCREEN_ID',
    'SVGA_VIDEO_DST_WIDTH', 'SVGA_VIDEO_DST_X', 'SVGA_VIDEO_DST_Y',
    'SVGA_VIDEO_ENABLED', 'SVGA_VIDEO_FLAGS', 'SVGA_VIDEO_FORMAT',
    'SVGA_VIDEO_HEIGHT', 'SVGA_VIDEO_NUM_REGS', 'SVGA_VIDEO_PITCH_1',
    'SVGA_VIDEO_PITCH_2', 'SVGA_VIDEO_PITCH_3', 'SVGA_VIDEO_SIZE',
    'SVGA_VIDEO_SRC_HEIGHT', 'SVGA_VIDEO_SRC_WIDTH',
    'SVGA_VIDEO_SRC_X', 'SVGA_VIDEO_SRC_Y', 'SVGA_VIDEO_WIDTH',
    'c__EA_SVGAFifoCmdId', 'c__EA_SVGARemapGMR2Flags',
    'c__Ea_SVGA_FIFO_MIN', 'c__Ea_SVGA_REG_ID',
    'c__Ea_SVGA_VIDEO_ENABLED', 'struct_SVGAColorBGRX',
    'struct_SVGAColorBGRX_0_0', 'struct_SVGAGMRImageFormat',
    'struct_SVGAGMRImageFormat_0_0', 'struct_SVGAGuestImage',
    'struct_SVGAGuestMemDescriptor', 'struct_SVGAGuestPtr',
    'struct_SVGAOverlayUnit', 'struct_SVGAScreenObject',
    'struct_SVGAScreenObject_0', 'struct_SVGAScreenObject_1',
    'struct_SVGASignedPoint', 'struct_SVGASignedRect',
    'struct_c__SA_SVGAFifoCmdAnnotationCopy',
    'struct_c__SA_SVGAFifoCmdAnnotationFill',
    'struct_c__SA_SVGAFifoCmdBlitGMRFBToScreen',
    'struct_c__SA_SVGAFifoCmdBlitScreenToGMRFB',
    'struct_c__SA_SVGAFifoCmdDefineAlphaCursor',
    'struct_c__SA_SVGAFifoCmdDefineCursor',
    'struct_c__SA_SVGAFifoCmdDefineGMR2',
    'struct_c__SA_SVGAFifoCmdDefineGMRFB',
    'struct_c__SA_SVGAFifoCmdDefineScreen',
    'struct_c__SA_SVGAFifoCmdDestroyScreen',
    'struct_c__SA_SVGAFifoCmdEscape', 'struct_c__SA_SVGAFifoCmdFence',
    'struct_c__SA_SVGAFifoCmdFrontRopFill',
    'struct_c__SA_SVGAFifoCmdRectCopy',
    'struct_c__SA_SVGAFifoCmdRemapGMR2',
    'struct_c__SA_SVGAFifoCmdUpdate',
    'struct_c__SA_SVGAFifoCmdUpdateVerbose', 'union_SVGAColorBGRX_0',
    'union_SVGAGMRImageFormat_0']
