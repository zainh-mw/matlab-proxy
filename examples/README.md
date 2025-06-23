# Use matlab-proxy in a Docker Container

The example [Dockerfile](./Dockerfile) in this folder shows how to add `matlab-proxy` to an existing docker image with MATLAB. Docker images of MATLAB starting from R2022a will have `matlab-proxy` by default. Use the Dockerfile as a reference for adding `matlab-proxy` to your custom images or Docker images for older releases of MATLAB.

## Build Custom Image
Specify the name of your custom image with the docker build arg `IMAGE_WITH_MATLAB`. The default value for this build argument is `mathworks/matlab:r2021b`.  

```bash
 docker build  --build-arg IMAGE_WITH_MATLAB=my_custom_image_with_matlab_installed \
               -f Dockerfile -t my_custom_image_with_matlab_proxy .
```
## Update MATLAB Proxy Package in a Docker Image

To update your Docker images with the latest release of **matlab-proxy** package, you can use either:
* a Dockerfile
* the `docker commit` command

MathWorks recommends updating the package using a Dockerfile as this method helps to keep track of the changes you make to Docker images.
### Approach 1: Use Dockerfile
The example Dockerfile [`Dockerfile.upgrade.matlab-proxy`](./Dockerfile.upgrade.matlab-proxy) in this folder shows how to upgrade an existing installation of **matlab-proxy** package in a Docker image.


```bash
 docker build  --build-arg IMAGE_WITH_MATLAB_PROXY=my_custom_image_with_matlab_proxy \
               -f Dockerfile.upgrade.matlab-proxy -t my_custom_image_with_matlab_proxy .
```

### Approach 2: Use `docker commit` command
Launch your container with the flag `--entrypoint /bin/bash`. 
```bash
$  docker run --rm -it --shm-size=512M --entrypoint /bin/bash my_custom_image_with_matlab_proxy:latest 
```

Once in the container, change to root user and upgrade the package.
```bash
root@6624c4893071:/home/matlab/Documents/MATLAB: sudo su
root@6624c4893071:/home/matlab/Documents/MATLAB: python3 -m pip install --upgrade matlab-proxy
```

In a new terminal, use the `docker ps` command.
```bash
$ docker ps

CONTAINER ID        IMAGE                                        COMMAND                CREATED             STATUS              PORTS                          NAMES
6624c4893071        my_custom_image_with_matlab_proxy:latest     "/bin/run.sh -shell"   2 minutes ago       Up 2 minutes        5901/tcp, 6080/tcp, 8888/tcp   laughing_buck

```
In this example, the container ID is  `6624c4893071`. Now commit:
```bash
$ docker commit 6624c4893071 my_custom_image_with_matlab_proxy:latest
```

Stop the running container by exiting the shell:
```bash
root@6624c4893071::/home/matlab/Documents/MATLAB: exit
matlab@6624c4893071::/home/matlab/Documents/MATLAB: exit
```

## Run Docker Container
Run the Docker container:
```bash
docker run -it -p 8888:8888 --shm-shared=512M my_custom_image_with_matlab_proxy:latest 
```

To modify the behaviour of `matlab-proxy`, you can specify environment variables at runtime.
```bash
docker run -it -p 8888:8888 -e MLM_LICENSE_FILE="port@hostname" \
            --shm-shared=512M my_custom_image_with_matlab_proxy:latest 
```
For a complete list of the environment variables you can use to customize the behaviour of the app, see [Advanced-Usage.md](../Advanced-Usage.md).



---

Copyright 2020-2025 The MathWorks, Inc.

---

