#include <err.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>

#include "svga.h"
#include "svga3d_reg.h"

#include "config.h"

SVGADevice gSVGA;

void run_data(uint32_t* data);

int main(int argc, char **argv)
{
  if (argc != 3) {
    err(EXIT_FAILURE, "[*] Usage : ./worker <server port> <port>");
  }
  
  // svga setup
	if (conf_svga_device() != 0)
		errx(EXIT_FAILURE, "[!] Error initializing SVGA device");

	SVGA_WriteReg(SVGA_REG_WIDTH, 0x320);
	SVGA_WriteReg(SVGA_REG_HEIGHT, 0x258);
	SVGA_WriteReg(SVGA_REG_BITS_PER_PIXEL, 32);

  // fuzz iteration setup
  int sockfd = -1;
  char buf[MAX_DATA_SIZE];
  struct hostent* host = NULL;
  struct sockaddr_in host_addr = {0};

  if((host=gethostbyname(argv[1])) == NULL)
    err(EXIT_FAILURE, "[!] Invalid host name : %s", argv[1]);

  if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    err(EXIT_FAILURE, "[!] Socket binding failed");

  host_addr.sin_family = AF_INET;
  host_addr.sin_port = htons(atoi(argv[2]));
  host_addr.sin_addr = *((struct in_addr*)host->h_addr);
  memset(&(host_addr.sin_zero), 0, 8);

  // fuzz iteration
  while(1) {
    for(; connect(sockfd, (struct sockaddr*)&host_addr, sizeof(struct sockaddr)) == -1; );

    warnx("[+] Connection established");

    memset(buf, 0, MAX_DATA_SIZE);
    
    int numbytes = 0;
    int bytes_read = -1;
    while(numbytes < MAX_DATA_SIZE-1 && 
      (bytes_read=recv(sockfd, buf+numbytes, MAX_DATA_SIZE-numbytes-1, 0)) != -1) {
      numbytes += bytes_read;
    }
    warnx("[+] Received %d bytes", numbytes);

    run_data((uint32_t*)buf);
  }
	return 0;
}

void run_data(uint32_t* data) {
  unsigned idx = 0;
  while(idx < MAX_DATA_SIZE / 4) {
    uint32_t cmdnr = data[idx++];
    uint32_t hdrsize = data[idx++];

	  SVGA_WriteReg(SVGA_REG_CONFIG_DONE, false);

    VMwareWriteWordToFIFO(cmdnr);
    VMwareWriteWordToFIFO(hdrsize);
    for(int i = 0; i < hdrsize / 4; i++) {
      VMwareWriteWordToFIFO(data[idx++]);
    }
    VMwareWaitForFB();
  }
}