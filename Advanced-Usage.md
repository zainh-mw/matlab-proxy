# Advanced Usage

This page shows how to customize the behaviour of the `matlab-proxy` app using advanced settings.


----

**Table of Contents**
- [Customize Environment Variables](#customize-environment-variables)
- [Shutdown on Idle](#shutdown-on-idle)
- [Add MATLAB to System Path](#add-matlab-to-system-path)
- [Customize MATLAB Root](#customize-matlab-root)
- [Platform Support](#platform-support)
- [Limitations](#limitations)
- [Security](#security)
- [Feedback](#feedback)

## Customize Environment Variables

To control the behavior of MATLAB Proxy, you can use the environment variables described in this section. You must specify these variables before starting the app. For example, to specify a network license server when you start the app, using the command below:

```bash
env MLM_LICENSE_FILE="1234@example.com" matlab-proxy-app
```

The following table describes all the environment variables that you can set to customize the behavior of the app.

| Name | Type | Example Value | Description |
| ---- | ---- | ------------- | ----------- |
| **MLM_LICENSE_FILE** | string | `"1234@111.22.333.444"` | To use either a license file or a network license manager to license MATLAB, specify this variable.</br> For example, specify the location of the network license manager to be `123@hostname`.|                                                                         
| **MWI_BASE_URL** | string | `"/matlab"` | Set to control the base URL of the app. MWI_BASE_URL should start with `/` or be `empty`. |
| **MWI_APP_PORT** | integer | `8080` | Specify the port for the HTTP server to listen on. |
| **MWI_APP_HOST** | string | `127.0.0.1` | Specify the host interface for the HTTP server to launch on. Defaults to `0.0.0.0` on POSIX and Windows systems.<br />With the default value, the server will be accessible remotely at the fully qualified domain name of the system. |
| **MWI_LOG_LEVEL** | string | `"CRITICAL"` | Specify the Python log level to be one of the following `NOTSET`, `DEBUG`, `INFO`, `WARN`, `ERROR`, or `CRITICAL`. For more information on Python log levels, see [Logging Levels](https://docs.python.org/3/library/logging.html#logging-levels) .<br />The default value is `INFO`. |
| **MWI_LOG_FILE** | string | `"/tmp/logs.txt"` | Specify the full path to the file where you want the app to write the debug logs. |
| **MWI_ENABLE_WEB_LOGGING** | string | `"True"` | To see additional web server logs, set this value to `"True"`. |
| **MWI_CUSTOM_HTTP_HEADERS** | string  |`'{"Content-Security-Policy": "frame-ancestors *.example.com:*"}'`<br /> OR <br />`"/path/to/your/custom/http-headers.json"` |Specify valid HTTP headers as JSON data in a string format, or specify the full path to the JSON file containing valid HTTP headers. These headers are injected into the HTTP response sent to the browser. </br> For  more information, see the section on [Custom HTTP Headers](#custom-http-headers).|
| **TMPDIR** or **TMP** | string | `"/path/for/MATLAB/to/use/as/tmp"` | Set either one of these variables to specify the temporary folder used by MATLAB. `TMPDIR` takes precedence over `TMP` and if neither variable is set, `/tmp` is the default value used by MATLAB. |
| **MWI_ENABLE_SSL** | string | `"False"` | When set to `True`, the values in `MWI_SSL_CERT_FILE & MWI_SSL_KEY_FILE` are used to configure matlab-proxy to use SSL. If you do not provide a CERT and KEY file using these variables, the software generates a self-signed certificate. Defaults to `False`.|
| **MWI_SSL_CERT_FILE** | string | `"/path/to/certificate.pem"` | The certfile string must be the path to a single file in PEM format containing the certificate as well as any number of CA certificates needed to establish the certificate’s authenticity. For details, see [SSL Support](./SECURITY.md#ssl-support).|
| **MWI_SSL_KEY_FILE** | string | `"/path/to/keyfile.key"` | The keyfile string, if present, must point to a file containing the private key. Otherwise, the private key is taken from certfile as well. |
| **MWI_ENABLE_TOKEN_AUTH** | string | `"True"` | When you set the variable to `True`, matlab-proxy requires users to provide the security token to access the proxy. Optionally, set the token using the environment variable `MWI_AUTH_TOKEN`. If you do not specify `MWI_AUTH_TOKEN`, the software generates a token for you. <br />For more information, see [Token-Based Authentication](./SECURITY.md#token-based-authentication).
| **MWI_AUTH_TOKEN** | string (optional) | `"AnyURLSafeToken"` | Specify a custom `token` for matlab-proxy to use with [Token-Based Authentication](./SECURITY.md#token-based-authentication). A token can contain any combination of alpha numeric text along with the following permitted characters: `- .  _  ~`.<br />When not specified, matlab-proxy will generate a random URL-safe token. |
| **MWI_USE_EXISTING_LICENSE** | string (optional) | `"True"` | When set to `True`, matlab-proxy will not ask you for additional licensing information and will try to start an already activated MATLAB on your system PATH.
| **MWI_CUSTOM_MATLAB_ROOT** | string (optional) | `"/path/to/matlab/root/"` | Optionally, provide a custom path to MATLAB root. For more information, see [Add MATLAB to System Path](#add-matlab-to-system-path) |
| **MWI_PROCESS_START_TIMEOUT** | integer (optional) | `1234` |  Defines the duration (in seconds) that `matlab-proxy` waits for the processes it starts, namely MATLAB & Xvfb, to respond. Default value is `600`. A timeout either indicates an issue with the spawned processes or be a symptom of a resource-constrained environment. Increase this value if your environment needs more time for the spawned processes to start.|
| **MWI_MATLAB_STARTUP_SCRIPT** | string (optional) | `"addpath('/path/to/a/folder'), c=12"` | Run custom code at startup, specified as a string. For detailed instructions, see [Run Custom MATLAB Startup Code](#run-custom-matlab-startup-code). |
| **MWI_SHUTDOWN_ON_IDLE_TIMEOUT** | integer (optional) | 60 | Defines the duration, in minutes, that `matlab-proxy` remains idle before shutting down. If you do not set the variable, `matlab-proxy` does not shut down when idle. For details, see [Shutdown on Idle](#shutdown-on-idle). |

## Shutdown on Idle

Set the environment variable `MWI_SHUTDOWN_ON_IDLE_TIMEOUT` to the number of minutes with no user activity after which matlab-proxy will shut down.

The timer resets when the app detects:
* MATLAB being used from the desktop
* MATLAB code being run
* MATLAB code run from Jupyter notebooks

Use this environment variable to clean up idle system resources.

<p align="center">
  <img width="800" src="./img/shutdown_warning.png">
</p>



## Add MATLAB to System Path

When `matlab-proxy` starts, it expects the `matlab` executable to be present on system PATH in the environment from which it was spawned. If unable to find `matlab` on the path, `matlab-proxy` will error.

Add MATLAB to the system PATH using the following commands:
```bash
# On Linux & MacOS
sudo ln -fs ${MATLAB_ROOT}/bin/matlab /usr/bin/matlab

# On Windows environments
setx PATH "${MATLAB_ROOT}\bin;%PATH%"
```
`MATLAB_ROOT` points to the folder in which MATLAB was installed.
Example values of `MATLAB_ROOT` on various platforms are:
```
On linux: /usr/local/MATLAB/R2023a
On MacOS: /Applications/MATLAB_R2023a.app
On Windows: C:\Program Files\MATLAB\R2023a
```

### Customize MATLAB Root

To specify the location of `MATLAB_ROOT`, use the environment variable `MWI_CUSTOM_MATLAB_ROOT`.

If you set this variable, `matlab-proxy` does not search the system PATH for MATLAB.

This might be useful in the following scenarios:

1. Changes to the system PATH are not possible or desirable.
2. There are multiple MATLAB installations on a system, and you want to use `matlab-proxy` with a particular installation of MATLAB.
3. The existing `matlab` executable on PATH is a user defined script, as explained in this [Github Issue](https://github.com/mathworks/matlab-proxy/issues/3).

Example usage:
```bash
env MWI_CUSTOM_MATLAB_ROOT=/opt/software/matlab/r2023a matlab-proxy-app
```


## Custom HTTP Headers 
If the web browser renders the MATLAB Proxy with some other content, then the browser could block the integration because of mismatch of `Content-Security-Policy` header in the response headers from the integration.
To avoid this, provide custom HTTP headers. This allows browsers to load the content.

For example, if this integration is rendered along with some other content on the domain `www.example.com`, to allow the browser to load the content, create a JSON file of the following form:

```json
{
  "Content-Security-Policy": "frame-ancestors *.example.com:* https://www.example.com:*;"
}
```
Specify the full path to this sample file in the environment variable `MWI_CUSTOM_HTTP_HEADERS`.
Alternatively, if you want to specify the custom HTTP headers as a string in the environment variable, in a bash shell type a command of the form below:

```bash
export MWI_CUSTOM_HTTP_HEADERS='{"Content-Security-Policy": "frame-ancestors *.example.com:* https://www.example.com:*;"}'
```

If you add the `frame-ancestors` directive, the browser does not block the content of this integration hosted on the domain `www.example.com`.


For more information about `Content-Security-Policy` header,  check the [Mozilla developer docs for Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy).

**NOTE**: Setting custom HTTP headers is an advanced operation, only use this functionality if you are familiar with HTTP headers.


### Proxy Support

`matlab-proxy` support for proxies is based on the support available for them in the `aiohttp` package. [AIOHTTP Proxy Support](https://docs.aiohttp.org/en/stable/client_advanced.html#proxy-support).

`matlab-proxy` has configured its usage of `aiohttp` to honor the environment variables that are used to configure proxy environments. viz: `http_proxy, https_proxy, no_proxy` 

`matlab-proxy` however needs to communicate via HTTP(S) with several processes including MATLAB on the machine on which it is running, and will automatically add the following values into the `no_proxy` environment variable:
1. localhost
1. 0.0.0.0
1. 127.0.0.1

#### Example Usage

Start a web proxy on your machine using the `ubuntu/squid` container:
```bash
docker run --rm --name squid-container -e TZ=UTC -p 3128:3128 ubuntu/squid:5.2-22.04_beta
```

From another system terminal, configure the environment variables to use this server:
```bash
# Configure your environment to use the SQUID Container as its web proxy
export http_proxy=http://your.machine.fqdn.com:3128 && \
export HTTP_PROXY=${http_proxy} \
       HTTPS_PROXY=${http_proxy} \
       https_proxy=${http_proxy} \
       MW_PROXY_HOST=your.machine.fqdn.com MW_PROXY_PORT=3128 \
       PROXY_SETTINGS=${http_proxy}

# Start matlab-proxy-app from this terminal
matlab-proxy-app
```
Replace `your.machine.fqdn.com` with the FQDN for the machine on which the `ubuntu/squid` container is running.

The logs from the SQUID container terminal should show activity when attempting to login to MATLAB through matlab-proxy.

### Run Custom MATLAB Startup Code

Use the environment variable `MWI_MATLAB_STARTUP_SCRIPT` to specify MATLAB code to run at startup. 

When you start MATLAB using `matlab-proxy`, MATLAB will first run a `startup.m` file, if one exists on your path. For details, see [User-defined startup script for MATLAB](https://www.mathworks.com/help/matlab/ref/startup.html). MATLAB will then run any code you have provided as a string to the `MWI_MATLAB_STARTUP_SCRIPT` environment variable.


You might want to run code at startup to:
1. Add a folder to the MATLAB search path before you run a script.
2. Set a constant in the workspace

For example, to set variables `c1` and `c2`, with values `124` and `'xyz'`, respectively, and to add the folder `C:\Windows\Temp` to the MATLAB search path, run the command:
```bash
env MWI_MATLAB_STARTUP_SCRIPT="c1=124, c2='xyz', addpath('C:\Windows\Temp')" matlab-proxy-app
```
To specify a script to run at startup, use the `run` command and provide the path to your script.
```bash
env MWI_MATLAB_STARTUP_SCRIPT="run('path/to/startup_script.m')" matlab-proxy-app
```

If the code you specify throws an error, then after MATLAB starts, you see a variable `MATLABCustomStartupCodeError` of type `MException` in the workspace. To see the error message, run `disp(MATLABCustomStartupCodeError.message)` in the command window.

Note: Restarting MATLAB from within `matlab-proxy` will run the specified code again.

#### Limitations

* Commands that require user input or open MATLAB editor windows are not supported. Using commands such as `keyboard`, `openExample` or `edit` will render `matlab-proxy` unresponsive.

----

Copyright 2020-2025 The MathWorks, Inc.

----
