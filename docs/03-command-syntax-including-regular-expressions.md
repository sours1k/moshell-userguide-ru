# 3 Command syntax, including Regular Expressions

## 3.1 How MOs are Identified

MOs can be identified using the RDN, LDN or FDN.

**3.1.1 RDN - Relative Distinguished Name**

This is used to identify an MO in relation to its nearest parent in the MO tree.

The RDN contains MO Class (also called MO Type), the equal sign, and MO identity. Example:

AtmPort=MS-24-1

**AtmPort** is the _MO Class_, **MS-24-1** is the _identity_.

**3.1.2 LDN - Local Distinguished Name**

This is used to uniquely identify an MO within a node.

The LDN shows the hierarchy above the MO, within the Managed Element’s MO tree. Example:

ManagedElement=1,TransportNetwork=1,AtmPort=MS-24-1

**3.1.3 FDN - Full Distinguished Name**

This is used to uniquely identify an MO within a network (used by RANOS/CNOSS/OSS-RC). Example:

SubNetwork=AUS,SubNetwork=H2RG_0201,MeContext=St_Leonards_Station_2065010,ManagedElement=1,TransportNetwork=1,AtmPort=MS-24-1

## 3.2 How to address the MOs in MO-related commands

The first argument in the MO-related commands is usually used to specify the MOs that should be used by the command.

There are currently six different ways to specify the MO(s):

1.  all

All loaded MOs will be affected. Example:

a) get all userlabel to get attribute _UserLabel_ on all MOs

Note: instead of all, it is also possible a regex wildcard such as . or \*. This has the same effect.

1.  Proxy ID(s)

All MO(s) with the given proxy id(s) will be operated upon.

To specify several MO proxies, there are two ways:

• Specify each Proxy ID with a space in between. Example:

a) pr 0 2 5 to print the MO proxies 0, 2 and 5.

• Give a range of Proxy IDs. Examples:

1.  pr 4-10 prints MO proxies from 4 to 10.
    2.  pr 10-4 prints all MO proxies from 10 down to 4 (reverse order, useful for deleting MOs).
    3.  acc 10-20 restart calls the action **restart** on MOs with proxy 10 up to 20.

Note: proxy ranges and individual proxy Ids can be mixed on the same line.

Example: pr 0 2 3-5 8 10-12

1.  Link handler (for PluginUnit and Spm MOs only!). Examples:
    1.  acc 001400 restart - to restart the MO **Subrack=MS,Slot=14,PlugInUnit=1**.
    2.  bl 001900/sp0.lnh - to lock the first SPM on the SPB in slot 19 with LDN:

**Subrack=MS,Slot=19,PlugInUnit=1,Spu=1,Spm=1**. Note that MOs start counting from 1 and the link handlers start from 0! 4. MO Group

MO Groups are user defined groups of MOs. All MO(s) belonging to the given MO group will be operated upon.

To create a MO group, see command description for ma/lma in Section 4.1.10. MO groups can also be created with the commands hget/lhget, lk/llk, st/lst, pdiff/lpdiff.

Note: In RNC, running the bo command will automatically create a number of MO groups containing the cc/dc/pdr device MOs for each module. 5. Board Group

MOs (**PlugInUnit** or **Spm**) mapped onto the boards belonging to the given board group will be operated upon.

Example 1:

- baw sccp sccp All boards with the swallocation matching "sccp" will go into the board group "sccp"
- bl sccp All **PlugInUnit** or **Spm** MOs connected to boards of this board group will be locked

Example 2: in RNC, using the default board groups created after running the bo command:

- acc mod10 restart
- pr dc10
- acc dc10 restart the board group dc10 is mapped onto the **Spm** MOs
- bl dc10dev in this case we are using the MO group containing the **Device** MOs, see above

6\. MO-Filter (regular expression)

MO(s) whose LDN/RDN match the _regular expression pattern_ will be affected.

If the command starts with _l_ then the pattern will match agains the LDN.

If the command doesn’t start with _l_, then the pattern will match against the RDN.

If the command doesn’t start with _l_, and the filter contains no commas, then the pattern will match against the RDN.

If the command doesn’t start with _l_, and the filter contains commas, then the pattern will match against the LDN but will not include the children. (Note: this particular syntax is not supported in multimode).

**Examples:**

1.  pr ms-24-1

TransportNetwork=1,AtmPort=MS-24-1

1.  lpr ms-24-1

TransportNetwork=1,AtmPort=MS-24-1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc32

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc33

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc337

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc332

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc34

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc35

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc40

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc64

1.  pr ms,slot=5,plug

Equipment=1,Subrack=MS,PlugInUnit=1

1.  lpr ms,slot=5,plug

Equipment=1,Subrack=MS,PlugInUnit=1

Equipment=1,Subrack=MS,PlugInUnit=1,Program=basic

Equipment=1,Subrack=MS,PlugInUnit=1,Program=nss

Equipment=1,Subrack=MS,PlugInUnit=1,Programs=spas ....

When using the _MO-Filter_, it is a good idea to test the pattern with pr/lpr command before issuing a get/set/acc/cr/del command, in order to see which MOs will be matched by the pattern.

Sometimes, a second or third argument can be given, which is usually a string matching the _attribute_ or _attribute value_ that you want to display.

## 3.3 Regular Expressions

**Note: MOSHELL pattern matching is NOT case sensitive**

The search string that is used in the filters is a Unix Regular Expression (like the patterns used in the grep -E command). Therefore, special meta-characters such as . \* \[ \] ^ $ can be used.

Short description of some meta-characters:

- “.” - any single character
- “\*” - 0 or more occurences of the previous character
- \[ \] - matches a character or range of characters inside the brackets
- \[^\] - NOT matching a character or range of characters inside the brackets
```text
- | - OR
```
- ^ - beginning of string
- $ - end of string
- ! - negation
- % - reverse order

Examples of using meta-characters:

- a\* means a or aa or aaa, etc.
- .\* is like a wildcard as it matches 0 or more occurences of any character
- \[a-z\] matches all letters from a to z
- \[abe\] matches letters a,b, and e
- \[^3\] matches any character but not 3
- 3|5|6 matches 3 or 5 or 6
- ^a.\*4$ matches a string beginning with a and finishing with 4, with any character in the middle

Regular expressions can also be grouped together using brackets, e.g:

- cell(11|23|45) matches cell11 or cell23 or cell45

Examples of using regular expressions in the filters:

1.  lpr ms-24-1.\*vp2

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc34

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc35

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc40

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc64

1.  lpr %ms-24-1.\*vp2

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc64

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc40

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc35 TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc34

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2

1.  lpr !loadmodule|program

• All MOs except those matching **loadmodule** or **program** will be printed

1.  lpr 20.\*os

Equipment=1,Subrack=1,Slot=20,PlugInUnit=1,Etm4=1,Os155PhysPathTerm=1

Equipment=1,Subrack=1,Slot=20,PlugInUnit=1,Etm4=1,Os155PhysPathTerm=2

1.  pr cc\[1-4\]

TransportNetwork=1,AtmCrossConnection=AtmCC1

TransportNetwork=1,AtmCrossConnection=AtmCC2

TransportNetwork=1,AtmCrossConnection=AtmCC3

TransportNetwork=1,AtmCrossConnection=AtmCC4

1.  pr cc\[135\]

TransportNetwork=1,AtmCrossConnection=AtmCC1

TransportNetwork=1,AtmCrossConnection=AtmCC3

TransportNetwork=1,AtmCrossConnection=AtmCC5

1.  lpr =6.\*prog.\*=1

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=15

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=1

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=14

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=13

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=12

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=11

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=10

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=19

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=18

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=17

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=16

1.  lpr =6.\*prog.\*=1$

Equipment=1,Subrack=1,Slot=6,PlugInUnit=1,Program=1

1.  lpr ms-24-1

TransportNetwork=1,AtmPort=MS-24-1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc32

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc33 TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc337 TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp1,VpcTp=1,VclTp=vc332

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc34

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc35

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc40

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc64

10\. lpr ms-24-1.\*=vc\[^3\]

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc40

TransportNetwork=1,AtmPort=MS-24-1,VplTp=vp2,VpcTp=1,VclTp=vc64

## 3.4 How to specify attribute values in set/cr/acc commands

1.  For attributes of type **Struct**, use the following syntax: attr1=val1,\[,attr2=val2\[,attr3=val3\]\]\]...

Example:

set sid sib11 sib11repperiod=128 set mtp3bspitu sppriority prioslt=2 set mtp3bspitu sppriority prioslt=2,prioco=2

1.  For attributes of type MoRef, just type the MO LDN (without **ManagedElement=1**). E.g.:

lset AtmPort=1221,VplTp=vp1 atmTrafficDescriptor

transportnetwork=1,atmtrafficdescriptor=C1P4500

It is also possible to skip the first parent (eg **TransportNetwork**, **SwManagement**, etc). E.g.:

cr rncfunction=1,utrancell=30451,utranrelation=30451to305212 Attribute 1 of 1, utrancellref (moRef:UtranCell): utrancell=30521

1.  For attributes of type **array of MoRefs**, separate each element of the array with spaces. Eg:

set jvm admclasspath loadmodule=oms loadmodule=vbjorb ...

acc aal2pathdistributionunit=1 addPath

Parameter 1 of 1, aal2PathVccTpId (sequence-moRef-Aal2PathVccTp):

aal2pathvcctp=csa aal2pathvcctp=csb

1.  For attributes of type **array of Struct**, separate each element of the array with semicolons. Eg:

set rncfunction aliasPlmnIdentities

mcc=300,mnc=23,mnclength=2;mcc=345,mnc=32,mnclength=2;mcc=208,mnc=123,mnclength=3

1.  For attributes of type array of integer/long/float/string/boolean, separate each element of the array with commas or spaces.

Eg:

set antfeedercable=6 ulattenuation 10,10,10,10,10,10,10,10,10 set antfeedercable=6 ulattenuation 10 10 10 10 10 10 10 10 10

set jvm options -Xms65000k,-Dhttp.root=/c/public_html,

\-Dse.ericsson.security.PropertyFileLocation=/c/java/SecurityManagement.prp set cell=3041 ActiveOverlaidCDMAChannelList true,true,false,true set cell=3041 ActiveOverlaidCDMAChannelList true true false true

acc managedelementdata addDhcpServerAddress

Parameter 1 of 1, ipAddressArray (sequence-string): 10.1.1.3,10.1.1.4

1.  For attributes of type array of integer, it is also possible to specify ranges of values. Eg, in the command below, the attribute will be set to 1,2,3,4,5,23,24,25,26 set IpInterface=1,DscpGroup=1 dscpValues 1-5,23-26
2.  To input an empty value:
    - in set command, just leave the value field blank. Eg:

set 0 userlabel

set reliableprogramuniter admpassiveslot

- in cr command, type null or d. This is only supported for non-mandatory (restricted) attributes, because mandatory attributes must be given a value.
    - in acc command, type null. This is only supported for parameters of type MoRef or String.

1.  Attributes of type EcimPassword:

These attributes are of type struct and are usually entered as: cleartext=true,password=mysecret

To avoid entering the password in clear text it is possible to encode it first with the encpw command and then enter this string in the password field, eg: cleartext=true,password=ENC@?xyza

Alternatively for the set command it is possible to use the p option (setp) which prompts the user to enter only the password part of the EcimPassword struct, and no echoing is done on the screen so the password can be entered without encoding.

## 3.5 Moshell command line

The command line uses the Readline library from bash. Here are some of the supported function keys:

- **right arrow or Ctrl-f** \- move forward one character
- **left arrow or Ctrl-b** \- move backward one character
- **up arrow** \- previous command in history buffer
- **down arrow** \- next command in history buffer
- **backspace** \- delete one character backward
- **Ctrl-d or <del>** \- delete one character forward
- **Ctrl-a or <home>** \- go to beginning of line
- **Ctrl-e or <end>** \- go to end of line
- **Ctrl-u** \- erase all characters backward
- **Ctrl-k** \- erase all characters forward
- **Alt-f** \- move forward one word

**Alt-b** \- move backward one word

**select or select + ctrl-<insert>** \- copy to clipboard

- **<insert> or shift-<insert>** \- paste from clipboard

Note about command history: if you type the beginning of a command and then use the up/down arrow key, you will see all previous commands starting with this string

## 3.6 Piping

Some commands support piping, e.g. All OSE shell commands, lh, tg, str, etc.

This is usually indicated in the menu and the help for that command. Some examples are:

te log read | grep ERROR lh mp te log read | grep ERROR str | grep cell=30456

For other commands that don’t support piping (like MO commands), the workaround is to save the output to a logfile then run the unix command on that logfile by using the l or ! command. Example:

|     |     |
| --- | --- |
| l+  | #open the logfile, an arbitrary name will be given |
| prod loadmodule | #run the command |
| l-  | #close the logfile |
| l sort $logfile | #run unix command sort on the logfile. |

l grep -i basic $logfile

Note: $logfile is automatically set by MoShell to contain the name of the latest log file created.
