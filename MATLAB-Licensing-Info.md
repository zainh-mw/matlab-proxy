# MATLAB Licensing Info


**Table of Contents:**
- [For End Users ](#for-end-users)
- [For Administrators](#for-administrators)


**For End Users**

When you start MATLAB using the app, you see a user interface with three options for selecting your MATLAB license.

<p align="center">
  <img width="400" src="img/licensing_GUI.png">
</p>

To choose the right option, determine what MATLAB licenses you have access to. To see the licenses linked to your account, go to [License Center (MathWorks)](https://www.mathworks.com/licensecenter/?s_tid=hp_ff_s_license). To link your MathWorks account with a license, see [Link a License to MathWorks Account](https://www.mathworks.com/licensecenter/licenses/add).

Based on the license that you want to use, you can follow the procedures outlined in the table below to setup the MATLAB licensing for the app. If you already have an activated MATLAB, you can use the _Existing License_ option to start MATLAB without authenticating every time.

| License Type | Procedure |
| ------ | ------ |
| Individual, Home or Student (that only you use and is in your name)  | Your license is already configured for use with MATLAB Proxy. Using the _Online License Manager_ tab, enter the credentials to your MathWorks account.   |
| Campus-Wide License | Your license is already configured for use with MATLAB Proxy. Using the _Online License Manager_ tab, enter the credentials to your MathWorks account.  |
| Concurrent and Network Named User  | Using the _Network License Manager_ tab, enter the address to your organization’s network license manager. To find the address, contact your license administrator. To identify your license administrator, sign in to your [MathWorks Account](https://www.mathworks.com/mwaccount/), click the license you are using, then click the tab marked “Contact Administrators”. |


**For Administrators**

| Intended Workflow | License Type | Procedure |
| ------ | ------ | ------ |
| You want your users to use online licensing  | Campus-Wide, Individual  | These licenses are already configured for use with MATLAB Proxy. When starting MATLAB, your end user will need to log in to their MathWorks account to use the license linked to it. |
| You want your users to use licenses administered using a network license manager   | Campus-Wide, Concurrent, or Network Named User  | You need to embed the address of your network license manager using the `MLM_LICENSE_FILE` environment variable. See [Advanced-Usage.md](./Advanced-Usage.md). Otherwise, an end user will need to manually enter the address to the network license manager when they start MATLAB. Each instance of MATLAB will consume a license seat. Using network named user licenses is possible but is not recommended. All named users will need to be explicitly specified in the license manager options file. Named users cannot use MathWorks products on more than two computers simultaneously. Specifying a single, generic named user for the app will not work.   |

----

Copyright 2020-2024 The MathWorks, Inc.

----