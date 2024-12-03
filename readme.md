# Basic Docker compose template
`docker init`
Would give you a good starting point with all "docker files" necessary, its a CLI that would give you a template

FASTAPI TEMPLATE:
https://fastapi.tiangolo.com/deployment/docker/

OP1:
`docker build -t yourdockerusername/yourappname:1.0 .`
Notice the dot which means the path to the current directory.

Once built you would get a long hash code (either in the command or ti the description of the cokcer desktop) E.g: a00b5601d0898d3f2a413266c6a10458e00979595fe2457c15c6d454bcf01d18

After this step, an IMAGE is built, know lets mount the image in a CONTAINER
`docker run a00b5601d0898d3f2a413266c6a10458e00979595fe2457c15c6d454bcf01d18`
`docker run -d --name mycontainername -p 82:80 yourdockerusername/yourappname:1.0` # 8082 is the port on the host machine, change it to any port you want

OP2:
`docker compose up`<br>
It would directly built everything as specified in the docker-compose file