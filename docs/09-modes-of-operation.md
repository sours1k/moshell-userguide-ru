# 9 Modes of operation

The list of commands that are supported in a specific mode can then be printed with the "h" command.

E.g. if connected in offline mode, the "h" printout will show only the commands that are applicable in this particular mode. Type "h <command>" for information on a specific command.

## 9.1 Offline Mode

The offline mode allows to run an moshell session against a modump.zip (collected with command "dcgk") or dcgm.zip (collected with command "dcgm").

When running moshell commands in offline mode, all information is from the zipfile, no communication is taking place with the node.

## 9.2 SQL Mode for CPP Nodes

The SQL mode allows to run an offline moshell session against the configuration database of a CPP node (db.dat, zipped CV, or dbdump).

- The db.dat file can be fetched using the ftget command, eg: ftget /d/configuration/cv/<cvname>/db.dat
- The CV can be fetched using the "cvget" command, eg: cvget <cvname>
- The dbdump can be fetched with the "cvgetd" command, eg: cvgetd <cvname>

To start moshell in SQL mode, use option -d, eg: moshell -d <cv.zip>, moshell -d <db.dat>, or moshell -d <dbdump.zip>

Moshell then opens an SQL client session to the file and loads all the MO data into memory.

To prevent loading MO data (for faster startup time), use the option -v nomo=1. Only sql commands will then be available. Note that the MO data when read from a CV/db.dat/dbdump only contains the MO configuration attributes, not the MO state attributes.

During startup, moshell also performs a consistency check on the various SQL tables of the database, to detect if there are any inconsistencies or corruptions.

Currently not all moshell commands are supported in SQL mode, type h at the moshell prompt to see the list of supported moshell commands.

It is also possible to run sql commands directly, e.g. sql select \* from tables.

## 9.3 Multi Mode for CPP Nodes

The multi mode allows an moshell session to be connect to several nodes CPP at the same time.

The command syntax for starting moshell in multi mode is: moshell -m <sitelist>|<sitefile>

The sitelist consists of a comma separated list containing all the node names or ip/dns addresses.

The sitefile is a text file containing the list of nodes names or ipaddresses, on node per line.

Example:

- moshell -m rnc2,10.1.128.17,rbs34,rxi2.ericsson.se,mgw3
- moshell -m /path/to/sitefile

If node names are used, they must be defined in the ipdatabase. For more information about ipdatabase and sitefile, see the help of the mobatch utility by typing "mobatch" from the unix prompt.

To print the list of commands which are supported in multi-mode, type h at the moshell prompt.

More information about a specific command can be obtained by typing h <command>.

The multi mode is primarily geared towards commands that use the corba services CS/FM/PM.

Moshell commands that access the node via telnet/ssh/ftp/sftp are currently not supported in multi mode.

When moshell is running in multi mode, a prefix is appended in front of certain objects in order to distinguish between different nodes and MOM versions:

- the RDN/LDN in MO commands are prefixed with the string "Me=<nodename>".
- the scanner names in PM commands are prefixed with the node name.
- the MO class in mom/pmom command are prefixed with the MOM version.

MOM handling in multimode:

- at startup, the MOM version of each node is checked, so it is supported to connect to nodes running different MOM versions.
- it is also possible to skip the MOM check by parsing a MOM file with the parsemom command. Then all nodes will use the same MOM, which may have unexpected effects.

**Known limitations in multi mode**

- u+, emom, pset: currently only work when all nodes have the same MOM version.
- u!: conversion of .mos to .mo script does not work correctly yet. Avoid using the u! command in multimode.
- pol: options (c/h/s/u) not supported in multimode. Syntax is: pol <node>. E.g: pol rnc2
- pcr: not supported in multi-mode.
- getmom: not supported in multimode.
- re: the "i" option is not supported in multimode.
- diff: syntax2 (parameter audit and dump comparison) is not supported. Only diff between individual MOs is currently supported (syntax1).
- pgets: the "n" and "m" options are not supported.
- lko: not supported in multimode.

## 9.4 Yang Mode for Cloud-RAN

Yang mode is similar to multi-mode but connects to the node via NETCONF/YANG over SSH/TLS instead of CORBA.

The option used for connecting in YANG mode is "-z" (or "-v yangcli=1"). The argument is the list of nodes. Examples:

- moshell -z vcucp1,vcuup1,vdu1 => connect to nodes vcucp1, vcuup1 , and vdu1

Note: connecting simultaneously to two separate nodes using same IP address (but different ports) is currently not supported.

**Connection methods SSH vs TLS:**

The uservariable use_tls indicates whether SSH or TLS is used.

For SSH, the value is use_tls=0 (default value)

For TLS, the value is use_tls=21 (moshell) or use_tls=31 (AMOS)

- SSH: The username/password can be saved in the uservariables yang_username/yang_password on node basis in the ipdatabase file or for all nodes in the moshellrc file.
- TLS: if use_tls=21, the path of the credential files can be saved in the uservariables clientpem (.cert file), capem (CA file), keypem (.key file). Optionnally if the .key file has a passphrase then the passphrase can be specified in the uservariable keypass.

If use_tls=31 then the path to the ssucredentials.p12 is found automatically on ENM

Example of entries in the ipdatabase file:

- SSH method: vcu01 10.49.20.147 x yang_username=expert,yang_password=expert01
- TLS method:

vcu02 10.49.20.148 x use_tls=21,clientpem=$HOME/keys/tlsnetconf.cert,capem=$HOME/keys/tlsnetconfCA.

Note: In case of use_tls=0 , if the uservariables yang_username/yang_password are unspecified then the username/password will be prompted in the terminal.

**Supported functionality:**

- The list of supported commands can be found in the "h" menu.
- To load the MOs, the following commands can be used:
    - "lt all" or "ltc all" to load all the MOs. Usually these commands are equivalent but in the case of YANG nodes, they use a slightly different method. Try the one that loads the quickest for your particular node.
    - "lt <motype>" : to load all MO instances of a particular class. Eg: lt nrcelldu -> loads all MO instances of class

"NRCellDU"

- "ltc <motype>": to load all MO instances of a particular class and all the underlying children MOs. Eg: ltc gnbdufunction -> loads the GNBDUFunction MO and all underlying children MOs.
- MO LDNs are prefixed with the string "Me=<nodename>" in order to distinguish MO instances from different nodes in the same session. This prefix is always used, even in single-node sessions.
- All MO read/write commands are supported: mom, momt, pmom, pr, get, kget, hget, st, ma, mr, mp, cr, set, del, acc, u+/u-/u!, gm, etc.
- It is supported to run .mos command files with run or run1
- It is possible to run NETCONF scripts via the command "netconf". Type "h netconf" for info.
- Offline mode is supported toward a modump.zip or dcgm.zip, collected with dcgk/dcgm command. The dcgk command can be run while connected to multiple nodes, thus the modump will contain a combined dump from several nodes and the offline session will act as a multi-node session. The dcgm command is currently only supported while connected to a single node.
- PM: pcr/pset/pmx/pmxe/pmr/pget/hpget/pdiff/hpdiff/pmxet are supported while connected to a single node. pmom/emom/pst/pgets/pbl/pdeb/pdel are supported both in single-mode and multi-mode.
- COLI: VCU COLI commands can be executed via MO actions ("acc" command) on the MOs under rc-diagnostics (CU-CP) and pp-diagnostics (CU-UP). To see the help, do "momc -diagn . " or "lacl -diagn".
- COLI: VDU/RDM COLI commands toward Radio units can be executed via "lh" or "lhsh" commands. Type "bp all" or "lhlist" to see the list of boards. Type "cmds" or "lhsh xxx ?" to see the list of supported commands. Refer to CPI for COLI

configuration example : https://cloudrandoc.ericsson.net/cloud-ran/distributed-unit/latest/deployment/install/prepare-valuesfile/prepare-values-file-for-mid-band/

- ORA: to connect to O-Radios connected to Open RAN Aggregator, the uservariable yang_enable_oru needs to be set to 1
- Alarm: the list of active alarms can be printed with "al" command, both toward single-node as well as in multi-node session. The uservariables snmp_username, snmp_sha_password, and snmp_aes_password need to be configured correctly. • Miscellaneous: the gpg command is supported to decrypt the ESI/DDB files in the dcgm.zip

**Planned to be supported in a future release:**

- pmx/pmxe/pmr/dcgm/lgf in multi-node (currently only to single node)
- cvls, cvmk, cvrm, etc
- inv/sdi
- ...

## 9.5 Router6000

The Router6000 has three separate O&M interfaces:

- ECIM/COM interface, accessed by moshell with the option -v comcli=35 : this gives access to all the platform-related MOs (HW, SW, License, etc)
- YANG interface, accessed by moshell with the option -v yangcli=1,use_yang_modelfile=1 : this gives access to all the transport-related MOs (IP interfaces, Ethernet ports, etc)
- IPOS CLI interface, accessed by moshell with the option -v rcli=1 : this gives access to all the transport-related configuration commands
