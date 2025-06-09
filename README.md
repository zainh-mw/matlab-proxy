# MATLAB Proxy
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mathworks/matlab-proxy/run-tests.yml?branch=main&logo=github)](https://github.com/mathworks/matlab-proxy/actions) &nbsp; [![PyPI badge](https://img.shields.io/pypi/v/matlab-proxy.svg?logo=pypi)](https://pypi.python.org/pypi/matlab-proxy) &nbsp;  [![codecov](https://codecov.io/gh/mathworks/matlab-proxy/branch/main/graph/badge.svg?token=ZW3SESKCSS)](https://codecov.io/gh/mathworks/matlab-proxy) &nbsp; [![Downloads](https://static.pepy.tech/personalized-badge/matlab-proxy?period=month&units=international_system&left_color=grey&right_color=blue&left_text=PyPI%20downloads/month)](https://pepy.tech/project/matlab-proxy)

----

Run MATLAB® in your web browser using the `matlab-proxy` Python® package.

Install the package to create an executable named `matlab-proxy-app`, which starts MATLAB and provides you a URL to access it. 
 
MathWorks® is actively developing this package. To request technical support or report issues, see [Feedback](#feedback).

----

**Table of Contents**
- [Requirements](#requirements)
- [Install](#install)
  - [PyPI](#pypi)
  - [Building From Sources](#building-from-sources)
- [Run MATLAB in Browser](#run-matlab-in-browser)
- [Examples](#examples)
- [Platform Support](#platform-support)
- [Limitations](#limitations)
- [Security](#security)
- [Feedback](#feedback)

## Requirements

* Supported Operating Systems:
    * [Linux®](#linux)
    * [Windows® Operating System](#windows) (starting [v0.4.0](https://github.com/mathworks/matlab-proxy/releases/tag/v0.4.0))
    * [Windows Subsystem for Linux (WSL 2)](#windows-subsystem-for-linux-wsl-2)
    * [MacOS](#macos) (starting [v0.5.0](https://github.com/mathworks/matlab-proxy/releases/tag/v0.4.0))     

* Python versions: 3.8 | 3.9  | 3.10 | 3.11

* MATLAB® R2020b or later, installed and added to the system PATH.
  ```bash
  # Confirm MATLAB is on the PATH
  which matlab
  ```  
* System dependencies required to run MATLAB:
  - The [MATLAB Dependencies](https://github.com/mathworks-ref-arch/container-images/tree/main/matlab-deps) repository contains `base-dependencies.txt` files that list the libraries required to run each release of MATLAB on a given operating system. To see how to use these files, refer to the Dockerfiles in the same folder.


* Most modern web browsers: for details, see [Browser Requirements (MathWorks)](https://www.mathworks.com/support/requirements/browser-requirements.html).
  
* X Virtual Frame Buffer (Xvfb) (for Linux® based systems):

  Installing Xvfb is optional (starting [v0.11.0](https://github.com/mathworks/matlab-proxy/releases/tag/v0.11.0)) but highly recommended. Xvfb enables graphical abilities like plots and figures in MATLAB. 
  To install Xvfb on your Linux machine, use:

  ```bash
  # On a Debian/Ubuntu based system:
  $ sudo apt install xvfb
  ```
  ```bash
  # On a RHEL based system:
  $ yum search Xvfb
  xorg-x11-server-Xvfb.x86_64 : A X Windows System virtual framebuffer X server.

  $ sudo yum install xorg-x11-server-Xvfb
  ```
  

* Fluxbox Window Manager (for Linux® based systems):

  Installing fluxbox is optional but required if you want to use Simulink Online. To install fluxbox, use:
  ```bash
  # On a Debian/Ubuntu based system:
  $ sudo apt install fluxbox 
  ```


## Install

### PyPI
You can install this repository directly from the Python Package Index.
```bash
python -m pip install matlab-proxy
```

### Building From Source
You can also build the package from source, which requires [Node.js®](https://nodejs.org/en/) version 18 or higher.

```bash
git clone https://github.com/mathworks/matlab-proxy.git

cd matlab-proxy

python -m pip install .
```

Install the package to create an executable called `matlab-proxy-app` on your system PATH, usually at `$HOME/.local/bin/`
```bash
# Confirm MATLAB Proxy is on the PATH
which matlab-proxy-app
```

## Run MATLAB in Browser

After you install the `matlab-proxy` package:

1. Open a terminal and start `matlab-proxy-app`. 
  ```bash
  # On Linux:
  env MWI_BASE_URL="/matlab" matlab-proxy-app
  ```
  `MWI_BASE_URL` is an environment variable which specifies the link for accessing MATLAB in your browser.
  For details about customizing MATLAB Proxy behaviour using environment variables, see [Advanced Usage](./Advanced-Usage.md).

  Run the command above to print text on your terminal, which shows the URL to access MATLAB. For example:
```
Access MATLAB at 
http://localhost:44549/matlab/index.html
```

2. Open the link in a web browser. If prompted, enter credentials for a MathWorks account associated with a MATLAB license. If you use a network license manager, change to the _Network License Manager_ tab and enter the license server address instead. If you already have an activated MATLAB, you can use the _Existing License_ option to start MATLAB without authenticating every time.
For details about choosing the license type, see [MATLAB Licensing Information](./MATLAB-Licensing-Info.md).
<p align="center">
  <img width="400" src="https://github.com/mathworks/matlab-proxy/raw/main/img/licensing_GUI.png">
</p>

* Wait for the MATLAB session to start. This can take a few minutes.
<p align="center">
  <img width="800" src="https://github.com/mathworks/matlab-proxy/raw/main/img/MATLAB_Desktop.png">
</p>

* To manage the MATLAB session, click the tools icon shown below.
<p align="center">
  <img width="100" src="https://github.com/mathworks/matlab-proxy/raw/main/img/tools_icon.png">
</p>

* Clicking the tools icon opens a status panel with buttons like these:
<p align="center">
  <img width="800" src="https://github.com/mathworks/matlab-proxy/raw/main/img/status_panel.png">
</p>

You see these options in the status panel:

| Option |  Description |
| ---- | ---- |
| Start MATLAB | Start your MATLAB session. Available if MATLAB is stopped.|
| Restart MATLAB | Restart your MATLAB session. Available if MATLAB is already running or starting.|
| Stop MATLAB | Stop your MATLAB session. Use this option if you want to free up RAM and CPU resources. Available if MATLAB is already running or starting.|
| Sign Out | Sign out of MATLAB session. Use this to stop MATLAB and sign in with an alternative account. Available when using online licensing.|
| Unset License Server Address | Unset network license manager server address. Use this to stop MATLAB and enter new licensing information. Available when using network license manager.|
| Shut Down | Stop your MATLAB session and the `matlab-proxy` server.|
| Feedback | Provide feedback. Opens a new tab to create an issue on GitHub.|
| Help | Show details of the options mentioned above.|

## Examples
* For installing/usage in a Docker container, see this [Dockerfile](./examples/Dockerfile) and its [README](./examples/README.md).
* For upgrading **matlab-proxy** in an existing Docker image, see this [Dockerfile.upgrade.matlab-proxy](./examples/Dockerfile.upgrade.matlab-proxy) and its [README](./examples/README.md#upgrading-matlab-proxy-package-in-a-docker-image).
* For usage in a Jupyter environment, see [jupyter-matlab-proxy](https://github.com/mathworks/jupyter-matlab-proxy).

## Platform Support

### Linux
The package fully supports Linux.

### Windows

Windows support begins `v0.4.0`. To use the package with Windows, upgrade the version:

```bash
# To upgrade an existing package installation:
$ pip install --upgrade matlab-proxy>=0.4.0
```

### MacOS

MacOS support begins `v0.5.0` and works best for MATLAB versions newer than R2022b. (On older versions, figures open in separate windows).
Note: Figures *also* open in a separate windows on versions of MATLAB older than R2022b.

To use the package with MacOS, upgrade the version:

```bash
# To upgrade an existing installation of matlab-proxy package:
$ pip install --upgrade matlab-proxy>=0.5.0
```

### Windows Subsystem for Linux (WSL 2)

To install `matlab-proxy` in WSL 2, follow the steps mentioned in the [Installation Guide for WSL 2](./install_guides/wsl2/README.md).


## Limitations
This package supports the same set of MATLAB features and commands as MATLAB® Online. For the full list, see 
[Specifications and Limitations for MATLAB Online](https://www.mathworks.com/products/matlab-online/limitations.html). 

Simulink Online is supported exclusively on Linux platforms starting from MATLAB R2024b.

## Security
We take your security concerns seriously, and will attempt to address all concerns.
`matlab-proxy` uses several other python packages, and depend on them to fix their own vulnerabilities.

All security patches will be released as a new version of the package.
Patches are never backported to older versions or releases of the package.
Using the latest version will provide the latest available security updates or patches.

## Feedback

MathWorks encourages you to try this package in your environment and provide feedback. 

To request technical support or submit an enhancement request, create an issue [here](https://github.com/mathworks/matlab-proxy/issues)

---

Copyright 2020-2025 The MathWorks, Inc.

---
