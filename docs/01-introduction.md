# 1 Introduction

## 1.1 Contact

For bug reports, installation issues, change requests etc. please use the forum on the moshell homepage.

### TR for MoShell

Put bug reports on the web page (see Section 1.1) or write them in MHWEB:

To write an MoShell TR/CR in MHWEB:

1.  MHO should be ENM-AMOS.
2.  Product should be AMOS CNA4033129. Refer to old TR HY15328 for more product details.

In order to get the fastest resolution to your problem, please add the following information to your TR or bug report:

- uv and pv printout
- Any _complete_ printout relevant to the fault
- How to recreate the fault (you can for instance include the hi printout showing all the commands that led to the fault)

## 1.2 MO concept

```text
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

| O&M Client |

| (eg: AMOS/moshell/EMCLI/ENM,etc.) |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

|

|

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

| CS,PM,AS,NS,LS Service Layer |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

|

|

\*\*\*\*\*\*\*\*\*\*|\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

- +++++++ \*
- | | \*
- | MAO | Management Adaption Layer\*
- | | \*

MO--> \* | | ------------------------ \*

```
|     |     |
| --- | --- |
| \* \| FRO \| | \*  |
| \* \| \| Resource Layer | \*  |
| \* \| RO \| | \*  |
| \* \| \| | \*  |
```text
| \* +++++++ | \*  |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

```
The O&M client can access the MOs through a number of services:

- _Configuration Service_ (CS): to read and change configuration data. Configuration data is stored in the MO attributes.
    - _Performance Measurement_ (PM): to setup statistics scanners or event filters. The statistics counters are stored in MO pm-attributes and output to an XML file every 15 minutes. The events are output into binary files every 15 minutes.
    - _Alarm Service_ (AS): to retrieve the list of alarms currently active on each MO.
    - _Notification Service_ (NS): to subscribe and receive notifications from the node, informing about parameter/alarm changes in the MOs.
    - _Log Service_ (LS): to save a log of certain events such as changes in the configuration, alarms raising and ceasing, node/board restarts, jvm events, O&M security events, etc

The MO is a way of modelling resources in a node. It consists of:

1.  A _Management Adaption Layer_

The purpose of the MAO (Management Adaptation Object) is to interface towards the various O&M services described above.

1.  A _Resource Layer_ consisting of Facade Resource Object (FRO) and a Resource Object (RO) . The RO is the actual resource modelised by the MO. The purpose of the FRO is to act as an interface between the MAO and the RO, by handling the configuration transactions and storing configuration data for the RO.

Figure 1: CPP and COM nodes have various access methods for different services. For the MO service, CORBA or NETCONF is used. For the command shell, ssh is used. To collect PM XML ROP files SFTP is used.

## 1.3 O&M services and protocols

From MoShell it is possible to:

- perform MO operations (get/set/delete/create/action) over CORBA / NETCONF / COMCLI
- run commands in the node’s shell (CPP-COLI / COMCLI / RCS-COLI / Linux-Shell)
- transfer files to and from the node via file transfer protocol

## 1.4 MO Tree and MO Naming Conventions

**1.4.1 LDN - Local Distinguished Name**

The MOs are organised in a hierarchical structure.

Each MO instance is uniquely identified in the node by its _Local Distinguished Name_ (LDN).

The highest MO in a node, the so called _root MO_ is the _ManagedElement_. This MO represents the whole node.

There is only one instance of the ManagedElement MO in the node and it is referenced by the LDN: **ManagedElement=1**

The string at the left of the equal sign is called the MO class (or MO type) and the string at the right of the equal sign is called the MO identity. In the case of the root MO, the _MO class_ is **ManagedElement** and the _identity_ is **1**.

If an MO is located further down in the MO tree, the LDN must contain the MO classes and identities of all the parents of that MO, in a sequence going from the root MO down to the MO in question. See example below:

ManagedElement=1

ManagedElement=1,Equipment=1

ManagedElement=1,Equipment=1,Subrack=MS

ManagedElement=1,Equipment=1,Subrack=MS,Slot=19

ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1

ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1,Program=DbmFpgaLoader

From this example, we can see that the ManagedElement has a child called **Equipment=1** which has a child called **Subrack=MS** (representing the main subrack of the node), which has a child called **Slot=19** (representing the slot in position 19), which has a child called **PlugInUnit=1** (representing the board located in that slot), which has a child called **Program=DbmFpgaLoader** (representing one of the programs loaded in that board).

The LDN of the lowest MO (the one called **Program=DbmFpgaLoader**) contains the address of all successive parents of that MO all the way up to the ManagedElement.

**1.4.2 RDN - Relative Distinguished Name**

The string located at the far right of an LDN, just after the last comma, is called a _Relative Distinguished Name_ (RDN).

It is a unique way of addressing a MO instance in relation to its closest parent.

This means that there is only one MO instance with the RDN **Program=DbmFpgaLoader** under the parent MO

**ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1**. However, there could be another MO instance with the same RDN under a different parent MO. For instance, there could be an MO instance with the RDN

**Program=DbmFpgaLoader** under the parent MO **ManagedElement=1,Equipment=1,Subrack=MS,Slot=23,PlugInUnit=1**.

Therefore the RDN is a relative way of addressing an MO instance.

**1.4.3 FDN - Full Distinguished Name**

When a node is connected to a Network Management System such as OSS-RC, there is a need to uniquely address each MO within the whole network. The _Full Distinguished Name_ (FDN) adds a network element prefix (MIB prefix) in front of the LDN of each MO instance in order to specify which node this MO belongs to. See the figure below, summing up the FDN/LDN/RDN concept:

FDN (Full Distinguished Name)

<------------------------------------------------------------............................................................> LDN (Local Distinguished Name)

<----MIB Prefix-----------------------><--------------................................................................> MoClass Identity

<-----> <---> RDN (Relative Distinguished Name)

<--------->

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1 RDN

<-------->

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1 RDN <----->

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS RDN <---------->

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS,Slot=19 RDN

<------------------->

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1 Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1,Program=DbmFpgaLoader

## 1.5 MOM - Managed Object Model

Each MO class contains a number of attributes which are used to store _configuration data_ or _performance measurement data_.

Each MO class can also support a number of defined _actions_. These represent certain operations which can be performed by the MO. A typical example is the action **restart** which will cause the MO to restart the resource it is responsible for (e.g. a board, a program, etc.).

The _Managed Object Model_ (MOM) is a reference document describing all the MO Classes that can exist in a node, together with their _attributes_ and _actions_.

The format of the MOM can be UML, XML, HTML, or MS-Word.

The XML version of the MOM is usually stored on the web server of the node, eg at

http://<ipaddress>/cello/oe/xml/<filename>.xml (CPP), https://<ipaddress>/models/ (MSRBS) The MOMs for each SW release are also stored in HTML format in the CPI.

## 1.6 Moshell Functionality

MoShell is a text-based O&M client providing access to the following services:

- _Configuration service (CS)_
- _Alarm service (AS)_
- _Performance management service (PM)_
- _Log service (LS)_
- _OSE shell (COLI)_
- _File transfer (ftp/http)_

Access to all services is supported both in secure mode (secure Corba, ssh, sftp) and unsecure mode (unsecure corba, telnet, ftp).

**1.6.1 Alarm Service**

The list of active alarms can be retrieved with the commands al (to show an overview) or ala (the same as al, with more details).

**1.6.2 OSE shell**

Any OSE shell command can be typed at the moshell prompt and the output can be piped through external utilities (which exist in your workstate/server) if required.

**Examples:**

te log read te log read | grep ERROR

- Only the $ prompt is supported. For instance, it is not possible to type lhsh 000100 and expect a prompt to that board. The workaround is to type the command on the same line as the link handler shell, eg lhsh 000100 te log read or put a semicolon after the lhsh xxxx, eg lhsh 001400 ; te log read ; vii ; llog . Type h ose at the moshell prompt for more info.
- Other commands which require a shell such as sqlc have their own implementation. See Section 4.3.8.
- Any _Loco_ commands should be written as loco ts\\nloco ... You can achieve this automatically using aliases, see Section 4.3.57.

**1.6.3 Configuration Service**

Moshell supports the following 6 operations from the configuration service:

1.  **GetChildren** to load all or parts of the MO-tree
2.  **GetAttribute** to read the attributes of an MO
3.  **CallAction** to perform an action on an MO
4.  **SetAttribute** to set (change) the value of an MO attribute
5.  **CreateMO** to create a new MO in the node

1.  **DeleteMO** to delete an MO from the node

**1.6.4 Performance Management Service**

Moshell supports the following operations from the performance management service:

- List Scanners and Event Filters
- Create Scanner
- Stop Scanner
- Resume Scanner
- Delete Scanner
- Set Event Filter

**1.6.5 Log service**

Moshell supports fetching and parsing of the following logs:

- availability log
- system log
- event log
- alarm log
- command log
- O&M security event log
- COLI log
- Hardware inventory log
- JVM events log (upgrade log)

**1.6.6 File transfer**

Moshell can download/upload files and directories to/from the node, using http, ftp or sftp.
