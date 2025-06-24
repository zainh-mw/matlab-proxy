# Troubleshooting guide for MATLAB Proxy
To check your environment for required dependencies, use the `troubleshooting.py` script.

## Table of Contents  
1. [Requirements](#requirements)
2. [Running the Script](#running-the-script)
3. [Collecting Logs](#collecting-logs)

# Requirements
- Python


# Running the Script
To generate troubleshooting output, run the following command from the folder where you cloned this `matlab-proxy` repository.
```bash
$ python ./troubleshooting/troubleshooting.py
```
# Collecting Logs
If you collect matlab-proxy logs using the **MWI_LOG_FILE** environment variable, we recommend that you provide the same variable when executing the troubleshooting script. This allows the script to gather the relevant logs for analysis.

For example, the command to do this in Linux would be:
```bash 
$ MWI_LOG_FILE=/tmp/log.file python ./troubleshooting/troubleshooting.py
``` 
For details about using environment variables in MATLAB Proxy, see [Advanced Usage](/Advanced-Usage.md).

----

Copyright 2021-2023 The MathWorks, Inc.

----
