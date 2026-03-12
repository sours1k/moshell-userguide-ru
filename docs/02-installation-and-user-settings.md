# 2 Installation and user settings

## 2.1 Installation for Unix (Solaris/Linux)

Copy the moshell installation package **moshellxxx.zip** to your home directory **/home/youruser** or to the temp directory **/tmp**. Very important: do not store the zip file inside the moshell folder otherwise the installation will be corrupted.

Then go to the folder containing the zipfile (cd <folder>) and run the following commands:

unzip -o moshellxxx.zip bash moshell_install

When prompted to enter the directory where you want to install moshell, it is recommended to specify your HOME directory ( ~). If you have executed moshell_install from your home directory then you can press the enter key and the current directory is selected.

If a previous moshell installation already exists, it is recommended to install in the same directory as the old one. This way, all your custom files (jar/xml files, site files, etc.) get copied across to the new revision and the old revision gets moved to a different location so you can still access it if needed.

When prompted to enter the path to java, make sure to use Oracle Java or OpenJDK (https://jdk.java.net/archive/)

Note: In the case of AMOS installation use option -a, ie: bash moshell_install -a (must be run as root on OSS masterserver).

Note: for linux 64-bit, the 32-bit libc library is required, the package name is libc6-i386 or glibc.i686 or ia32-libs.

(Other packages which may be needed for certain commands are python and expect.)

Running moshell for the first time:

If you have set the PATH variable correctly in your ~/.bashrc file, you should be able to run moshell from any directory. E.g: moshell <ipaddress>

If this is the first time moshell is installed in this location, then it will download a number of jar files from the node. No progress indicator will be shown so just be patient as it will take a few minutes. Progress can be seen by doing "ls -l" in the moshell/jarxml directory. For more information about user settings etc, check the user guide.

If the Moshell execution fails on linux with the following error:

moshell/commonjars/lib/lin64/filefuncs.so: cannot restore segment prot after reloc: Permission denied Then try to run the following commands, while logged in as root:

chcon -t texrel_shlib_t ./commonjars/lib/lin64/libz.so.1 chcon -t texrel_shlib_t ./commonjars/lib/lin64/filefuncs.so

If Moshell is unable to connect to the node on port 22, try executing the program moshell/commonjars/ssh manually. If it fails with the following error:

moshell/commonjars/ssh: error while loading shared libraries: cannot restore segment prot after reloc:

Then try running the following command, while logged in as root: chcon -t texrel_shlib_t commonjars/ssh

## 2.2 Installation for Windows (using Cygwin or WSL)

When running on Windows, Moshell uses a unix emulator known as Cygwin. From Windows 10 it is also possible to run Ubuntu or Debian directly on Windows, using the Windows Subsystem for Linux (WSL).

**2.2.1 Installation for Cygwin 64-bit**

Go directly to step 10, _MoShell Installation_, if you have already installed and configured Cygwin previously.

1.  Download the file http://www.cygwin.com/setup-x86_64.exe and store it under

C:\\users\\youruser\\cygwin_setup\\, then execute it from that folder with the context menu "Run as administrator". If that does not work then try to start a DOS command window as Administrator and execute the setup-x86_64.exe file from the DOS window.

1.  Choose "Install from internet", then click Next.
2.  Root Directory **C:\\cygwin64** (It is not recommended to choose a different directory, especially if it contains spaces).
3.  Choose a Download Site. For instance cygwin.mirror.constant.com is known to work well but probably others work fine too.
4.  In the "Select Packages" View menu, choose "Category", then add the following packages:
    - under _Archive_ select _zip_ and _unzip_
        - under _Database_, select _postgresql_
        - under _Graphics_, select _gnuplot-base_
        - under _Libs_, select _libglib2.0_0_, _libssp0_, _zlib_, _libxml2_
        - under _Net_ select _curl_, _inetutils_, _openssh_, _openssl_, _net-snmp-utils_ (5.7.3), _net-snmp-libs_ (5.7.3)
        - under _Perl_ select _perl_, _perl-XML-Simple_, and _perl-IO-Tty_
        - under _Python_ select _python39_, _p_ython39-pexpect, _p_ython39-requests
        - under _Text_ select _jq_
5.  Click _Next_, install will start. Wait for installation to complete.
6.  Copy the file moshell/examples/cygwin_install/cygwin_install.txt to C:/cygwin64 (also available from http://newtran01.au.ao.ericsson.se/moshell/cygwin_install.txt). .
7.  Click on Start –> Run.

In the "Run" window, type: cmd , then press <enter>.

A DOS window opens. At the DOS prompt, execute the following commands:

cd c:\\ cd cygwin64 bin\\perl.exe cygwin_install.txt

This will create the following files: c:/cygwin64/etc/profile, c:/cygwin64/cygwin64.bat, c:/cygwin64/home/youruserid/.bashrc, c:/cygwin64/home/youruserid/.minttyrc, c:/cygwin64/home/youruserid/.inputrc.

If those files already exist, they are automatically moved to the folder c:/cygwin64/tmp/installbackup.

1.  Open a new cygwin terminal window. The window should be black with white text and the prompt should like this: \[~\]$ If not, then go through all the steps again and make sure you haven’t missed out anything.

If you had a 32-bit cygwin installation earlier, note that your c:/cygwin/home/youruser folder can be copied over to c:/cygwin64/home/

More info about Cygwin installation issues can be found at: http://cygwin.com/faq/faq0.html

Uninstall instructions for cygwin can be found at http://cygwin.com/faq/faq.setup.html#faq.setup.uninstall-all

1.  Moshell installation. Follows these steps if you already have a working Cygwin environment.
    - Copy the moshell installation package **moshellxxx.zip** to your home directory **c:/cygwin64/home/youruserid**
        - Open the cygwin shell and run:

unzip -o moshellxxx.zip bash moshell_install

When prompted to enter the directory where you want to install moshell, it is recommended to specify your HOME directory ( ~).

If you have executed moshell_install from your home directory then you can press the enter key and the current directory is selected.

If a previous moshell installation already exists, it is recommended to install in the same directory as the old one. This way, all your custom files (jar/xml files, site files, etc.) get copied across to the new revision and the old revision gets moved to a different location so you can still access it if needed.

When prompted to enter the path to Java, just type java .

1.  Running moshell for the first time

If you have set the PATH variable correctly in your **~/.bashrc** file, you should be able to run moshell from any directory. E.g: moshell <ip-address>

Note: More info about cygwin installation issues can be found on http://cygwin.com/faq/faq0.html

Note: On Ericsson PCs in cygwin it can happen that file export from LMT port on MSRBS fails with reason "Unable to connect using the available authentication methods". In this case it can be tried to add this line in the file /.bashrc :

export USER=ERICSSON+$USER

**2.2.2 Installation for WSL**

For more information refer to the post on https://eteamspace.internal.ericsson.com/pages/viewpage.action?pageId=898808172

1.  Make sure you have Windows 10 64-bit build 16215 or higher.

To check the build, open _Run_ (_WindowsKey + R_) and type winver. If lower than 16215, upgrade your windows 10 version to latest.

1.  Open PowerShell as administrator and execute the following command:

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux Then restart your computer when prompted.

1.  Open the Microsoft Store and in the searchfield, enter _wsl_ or _linux_. Select a distribution (preferably Ubuntu, or Debian), then from the distribution’s page, select _Get_.
2.  Launch a new instance of the distribution that was installed. The first time, you will be prompted to define a username and password.

Use for instance the Ericsson username and enter a password of your choice.

1.  From the linux shell, execute the following commands:
    - sudo apt update && sudo apt upgrade . (If any questions apear, you can just press "Enter")

•

sudo apt-get install unzip zip postgresql vim gnuplot libglib2.0-0 inetutils\* expect binutils

•

sudo apt-get install openssh-server openssl libxml-simple-perl libio-pty-perl default-jre

- sudo apt-get install python3.8 python3-pip
    - pip3 install numpy pandas
    - sudo dpkg-reconfigure tzdata (then select your timezone, eg "Europe" and "Stockholm")

1.  Download moshellxx.zip from http://newtran01.au.ao.ericsson.se/moshell/ and store somewhere such as your downloads folder C:/users/xxxx/downloads

Then copy the moshellxx.zip installation package to your WSL file system by doing the following command in the linux shell: cp /mnt/c/users/xxxx/downloads/moshellxx.zip ~/

Then run the moshell installation from the linux shell, eg:

unzip -o moshellxx.zip bash moshell_install

0

~/

1.  Update the linux PATH environment variable to be able to run moshell from anywhere: echo export PATH="${PATH}:$HOME/moshell" >> ~/.bashrc

INFO: The WSL file system can be accessed from the Windows file explorer from the penguin icon labelled "Linux". It is also possible to access files of the Windows file system from the WSL shell by putting "/mnt" in front of the path. For instance , in order to copy a dcgm.zip from c:/users/myusername/downloads to the WSL home folder, do the following command from a WSL shell: mv /mnt/c/users/myusername/downloads/xxxx_dcgm.zip ~/

**Procedure to upgrade from WSL1 to WSL2 (for better performance)**

1.  Check if BIOS virtualization is enabled. Start "Task Manager" and go to "Performance" and CPU and on the left hand side check "Virtualization" that it is in state "Enabled".
2.  Enable Virtual Machine feature. Open PowerShell as administrator and execute the following command: dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
3.  Set WSL 2 as default version. Open PowerShell as administrator and execute the following command:

wsl --set-default-version 2

1.  Restart machine.
2.  Check WSL version assigned to Linux distributions right now: wsl -l -v
3.  Set WSL2 version to linux dist. Will take a few minutes. If it only takes 1-3s, please restart PC again to make sure WSL has taken effect. wsl --set-version Ubuntu-20.04 2wsl -l -v
4.  Other useful commands wsl --updatewsl --shutdown

**Procedure to add 32-bit support in WSL/WSL2** Needed for running certain binaries such as Polyhedra

1.  sudo dpkg --add-architecture i386
2.  sudo apt-get update
3.  sudo apt update
4.  sudo apt upgrade
5.  sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386

## 2.3 Starting an moshell session

This section gives a brief overview of how to get started once you have installed moshell.

**2.3.1 Starting up Moshell**

A Moshell session is started from the Unix shell prompt using command: moshell <node-name>|<node-address>

If connecting with node name, an entry must exist in the ipdatabase file reference the node name against an ip or dns address.

Other ways of starting moshell are described by typing moshell on its own as well as in chapter Section 9 (Offline mode/multi mode Chapter) .

Upon startup, and running the command "lt all", moshell will go through the following steps:

1.  If CPP, download the node’s IOR file and store it on the workstation. The node’s IOR file is fetched from http://nodeipaddress/cello/ior_files/nameroot.ior
2.  Check the node’s MOM version. If CPP, the node’s MOM is fetched from http://nodeipaddress/cello/oe/xml/<filename> where <filename> is one of the files listed in the user variable xmlmomlist. If MSRBS, the node’s MOM is fetched from https://<nodeipaddress>/models. If YANG, the node’s MOM is downloaded over NETCONF. The MOM version is derived from the "mim" tag inside the MOM file, eg:

<mim name="RNC_NODE_MODEL_E" version="5" release="3"> becomes RNC_NODE_MODEL_E_5_3. If this MOM version does not exist on the workstation (under moshell/jarxml directory), then it is downloaded from the node and stored in that directory. If CPP and the MOM version could not be figured out (ie. moshell could not find any MOM on the node), the MOM specified in the moshell uservariable default_mom is used.

1.  Parse the MOM and generate an internal table specifying all MO classes, attributes, and actions supported by the node.
2.  If CPP, initiate Corba communication with the node by using the information contained in the IOR file. If ECIM/COM or YANG, initiate COMCLI/NETCONF communication with the node over SSH or TLS.
3.  Read the FDN of the root MO
4.  Ready to receive commands from the user

At this stage, it is possible to access the _Alarm Service_ and _OSE shell_ but the _Configuration Service_ is limited since Moshell doesn’t have any knowledge of what MO instances are contained in the node’s MO tree (apart from the root MO).

The following commands are of use at this stage:

• h - to show the help and list of commands. Can be used with a command name after to show help about that command.

The menus are split into two (m and n) only for readability purposes.

**2.3.2 Loading the MO Tree**

Once Moshell first connects to the node it has no knowledge of the MO structure on the node (execept for the _ManagedElement_ MO class). In order to _get attributes_ or _call actions_ you first need to load the MO _stubs_ onto your Moshell client.

The whole MO tree can be read with command lt all. The LDN of each MO of the MO tree is then allocated a "proxy" number and stored in an internal table in Moshell memory. The internal proxy table can be printed via the command pr which will show for each MO, the LDN and the proxy number.

When performing an operation on an MO (get, set, action, etc.), either the proxy number or the LDN can be given as argument.

By using a _Regular Expression_ matching part of the LDN, an operation can be performed on several MOs at a time.

More information about this can be found in Section 3 or by typing h syntax at the prompt.

To save memory on the workstation, it is possible to load only parts of the MO tree instead of the whole MO tree.

For instance, by typing lt pluginunit, only the LDNs of MOs whose MO class is _PlugInUnit_ will be read.

Instead of typing the whole MO class, it is possible to type a regular expression that will match the MO class.

In this case, lt plu would be the same as lt pluginunit, since the string plu matches pluginunit More information about this in Section 4 or by typing h lt and h lc at the prompt.

**2.3.3 Performing Actions on Loaded MO Stubs**

To perform operations on one or several MOs which you loaded in the previous section, follow the command syntax shown on the menu.

1.  Example: To read the MO attributes of the MO with LDN

**ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1** you would type the following:

pr plu #then lookup the proxy identity of that MO get <proxy> #enter the MOs proxy identity as argument to the "get" command

OR lget ms,slot=19,pluginunit=1$

1.  Example: To read the MO attributes of all MOs whose MO class is _PlugInUnit_

get plu #the get command will operate on all MOs whose RDN matches "plu"

More info about this in Section 3 or by typing h syntax at the Moshell prompt.

Help for each command can be found in Section 4 or by typing h <command-name> at the Moshell prompt.

## 2.4 User-specific settings

There are a number of moshell configuration parameters (called _user variables_) which can be set either permanently or on a session basis. These settings have a default value which is defined in the file **moshell/moshell**. If one or more user variables need to be changed from the default value, it is recommended to store the new setting in one of the moshellrc files (**~/.moshellrc** or **moshell/jarxml/moshellrc** or **moshell/jarxml/moshellrc.$USER**) instead of the moshell file. This way, the new setting will be kept even after an moshell upgrade.

It is also possible to define user variables on a session basis by:

1.  using the command uv \[var=value\] from the moshell prompt (type h uv for more info)
2.  or use the -v option from the command line when starting moshell (type moshell on its own for more info)

It is possible to have a multi-user installation where all users run moshell from the same central location but have their logfiles, credential files, user variables and aliases stored in their own user’s directory.

The administrator can define a number of user variables and aliases and save them into the **moshell/jarxml/moshellrc** file. These user variables and aliases will apply to all users and will be kept after each moshell installation. It is also possible for the administrator to define individual moshellrc files which will be located in **moshell/jarxml/moshellrc.$USER** (moshell or AMOS in OSS) or in **/home/shared/common/moshell/moshellrc.$USER** (AMOS in ENM).

Each user can also define their own settings and aliases and save them into the **~/.moshellrc** file in their home directory. If this file is not present, it will be created automatically and can be modified any time.

All user variables that are defined in the file moshell/moshell can be given a new value in the **moshell/jarxml/moshellrc** and/or the **~/.moshellrc** file and/or the file **moshell/jarxml/moshellrc.$USER** or **/home/shared/common/moshell/moshellrc.$USER** (for AMOS in ENM).

The user variables defined in **moshell/jarxml/moshellrc.$USER** override those defined in **~/.moshellrc** which override those defined in **moshell/jarxml/moshellrc**, which in turn override those defined in the file moshell/moshell.

Here is a short list of user variables, look inside the file **moshell/moshell** for more info on each variable:

- _disk_check_ \- check if enough free disk space on the workstation: 0=no check, 1=warning only, 2=exit if not enough space
- _disk_limit_ \- the minimum free disk space required by the disk check, default 1G (1 Gigabyte).
- _java_ \- path to Java executable
- _ip_database_ \- path to the IP database file (see example of this file in **moshell/examples/mobatch_files**)
- _ip_connection_timeout_, _ip_inactivity_timeout_, _http_timeout_, _ftp_timeout_, etc... –> connection timeouts and idle timeouts for the various interfaces
- _corba_class_, _sa_credential_, _sa_password_, _sls_urls_, _sls_username_, _sls_password_, _cpp_usernames_, emphcpplinux_usernames, etc... -> settings related to O&M security for CPP nodes
- _comcli_, _com_usernames_, _com_passwords_, _ca_credential_, etc... -> settings related to O&M security for ECIM/COM nodes
- _prompt_highlight_ \- to enable or disable the bold font of the prompt
- _set_window_title_ \- to enable or disable the display of a window title
- _logdir_ \- path to the logfiles directory (this one can only be changed from moshellrc or .moshellrc, not uv or -v)
- etc, see the **moshell** file for further details

Look in the **moshell** file for a more complete list and detailed explanation of each variable.

**File properties**

All files and subdirectories under the moshell installation folder are read-only for all users except the one who did the installation.

## 2.5 Ports used by moshell

If there is a firewall between moshell and the nodes, then the following TCP ports need to be open in the firewall:

**CPP nodes:**

1.  CORBA:
    - port 56834: for unsecure corba (O&M SL1)
    - port 56836: for secure corba (O&M SL2 and SL3)
2.  HTTP/HTTPS: 80/443
3.  SSH/SFTP: 22
4.  Telnet: 23 (optional)
5.  Ftp: 21 (optional). If ftp is used, an additional port range needs to be open for the data connection (21 is for control only).
6.  Target monitor: TCP ports 33077 to 33087 and UDP 33078-33079 . Needed in order to monitor the trace and error log with the "mon" command.
7.  Optional: for subscription to Corba CS/FM notifications, using the utility runClient.sh (-c/-a options): callback port range 49152-65535 from the node to the client. This is not needed for moshell, only for the utility runClient.sh -c/-a options.

**RCS/COM nodes (MSRBS):**

- HTTPS: 443 (Baseband) or 3443 (vRAN)
- SSH: 830 (NETCONF), 2023 (COMCLI), 4192 (COLI)
- SFTP: 22 (from Node), 2024 (to Node)
- TLS: 6513 (NETCONF), 9830 (COMCLI), 9831 (COLI), 9921 (FTPES), 11880 (DIA to node), 11881-11907 (node to DIA)
- Trace streaming from Node: TCP 5342 to 5362 (CPM traces), and UDP 33079 (EMCA traces)
- Optional: the port range 10001 to 11000 may be opened from Node to Client in case exports will be done with export_method=0

All ports to be opened in the direction Client->Node except 5342 to 5362 (Bidirectionnal) and 22/33079/9921/11881-11907 (Node->Client)

More info in the CPI document "Node Hardening Guidelines"

**Other ECIM/COM nodes:**

- Pico nodes: 22 (SFTP), 9830 (COMCLI), 830 (NETCONF)
- Other nodes: 22 (APG43L), 2024 (BSP), 830 (PGM), ...

**Cloud RAN nodes:**

- SSH: 830 (NETCONF), 9022 (SFTP)
- TLS: 6513 (NETCONF), 9021 (FTPES), 9831 (COLI), 11880 (DIA to node), 11881-11907 (node to DIA) • SNMP: UDP 161 (bi-directionnal)

**Note1:**

A port scanning is done by moshell at startup in order to distinguish the type of node (CPP, RCS, EPIC, CBA, etc)

If some of the ports are unavailable at the time when moshell was started then this may lead moshell to not recognise the node type correctly.

In this case it would be necessary to close and reopen the moshell session once the relevant O&M ports have become available.

**Note2:**

If port 4192 is unavailable at the time when running a COLI command on a RCS node for the first time in the moshell session then it will be assumed that this node does not support COLI.

In this case it would be necessary to run the command "bor" or close and reopen the moshell session once the port 4192 becomes available.

## 2.6 LDAP roles

### MSRBS

When connecting to a RCS/COM node such as MSRBS with a LDAP user, the following roles are needed by the user in order for all AMOS/moshell commands to work properly:

- SystemAdministrator: in order to access the SystemFunctions MO tree and also the SFTP server of the node (needed by AMOS commands such as pmr/pmx/pme/inv/sdi)
- BasebandSupportExpert: in order to executed certain COLI commands (need by AMOS commands such as dcg/inv/sdi/mon...)
- XXXX_ApplicationAdministrator (where XXX is ENB, GNB, etc)

### Cloud RAN

When connecting to a YANG node such as VCU/VDU/RDM with a LDAP user, the following roles are needed by user in order for all AMOS/moshell commands to work properly:

- SystemAdministrator: in order to access most of the MO tree as well as the SFTP server of the node (needed by AMOS commands such as pmr/pmx)
- SystemDiagnostics: in order to run VCU COLI actions on the MO tree rc-diagnostics and pp-diagnostics
- ECRSupportExpert: in order to run Radio COLI commands from VDU/RDM

## 2.7 O&M Security

**Uservariables for CPP nodes security**

- corba_class: used for setting whether corba security is used or not, as well as the type of credentials to use if corba security is activated
    - corba_class=2: no security
    - corba_class=3: security with stand-alone mode credential "sam.pbe"
    - corba_class=4: security with automatic download of network mode credential "ssucredentials.xml". Need to set the SLS login with "sls_username" and "sls_password"
    - corba_class=5: security with already downloaded network mode credential "ssucredentials.xml", located by default in /Ericsson/OMSec but the path can be set in "nm_credential"
- smart_password, cpp_usernames/cpp_passwords, cpplinux_usernames/cpplinux_passwords
    - In CPP OSE nodes with SL1/SL2, the ssh/sftp login consists only of a password which can be set in "standard_passwords" when "smart_password=1"
    - In CPP OSE nodes with enhanced SL1/SL2, the ssh/sftp login consists of a username and password which can be set in "cpp_usernames/cpp_passwords"
    - In CPP Linux nodes with SL1/SL2, the ssh/sftp login is specified in "cpplinux_usernames/cpplinux_passwords"
    - In SL3, the ssh/sftp login is specified in "sls_username/sls_password"

**Uservariables for ECIM/COM nodes security**

- SSH access: the ssh/sftp login can be specified in the uservariables "com_usernames/com_passwords"
- TLS access: the uservariable "comcli" is used for specifying the type of credential to use
    - comcli=27: uses credential and password specified in ca_credential (default:

/Ericsson/OMSec/CAcert/ssucredentials.p12) and ca_password (default: $USER)

- comcli=25: uses credential and password specified in sa_credential (default: /Ericsson/OMSec/sam.p12) and sa_password (set when downloading the sam.p12 from SLS)
    - comcli=26: uses credential files specified in clientpem and capem
    - comcli=29: uses credential files specified in clientpem, capem, and keypem
- File export: the uservariables export_username/export_password can be used for specifying the sftp/ftpes server login. The uservariable "export_protocol" can be used to specify export over SFTP (0: default) or FTPES (1).

**Uservariables for YANG nodes security**

- SSH access: the ssh/sftp login can be specified in the uservariables "yang_username/yang_password"
- TLS access: the uservariable "use_tls" is used to specify the type of credential to use
    - use_tls=31: uses credential file specified in ca_credential (default: /Ericsson/OMSec/CAcert/ssucredentials.p12) and ca_password (default: $USER)
    - use_tls=21: uses credential files specified in clientpem, capem, and keypem
