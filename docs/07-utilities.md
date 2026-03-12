# 7 Utilities

The below two utilities are separate from moshell and shall be run stand-alone:

- mobatch: to execute a number of moshell sessions to multiple nodes in parallel. Type "/path/to/moshell/mobatch" on its own for help.
- pstool: to list or manage moshell processes on the workstation. Type "/path/to/moshell/pstool" on its own for help. More info about pstool is mentionned in chapter 8.

Regarding mobatch:

The list of nodes on which to perform the operations shall be stored in a file called the "sitefile".

The ip-addresses/DNS-names and passwords of all nodes of the network must be stored in a reference file called the "ipdatabase".

The ipdatabase uses the following syntax:

<nodeName> <nodeIpAddress>|<nodeDNSAddess> <nodePassword>|<dummytext> \[<uservariables>\] An example of a sitefile and an ipdatabase can be found in moshell/examples/mobatch_files .
