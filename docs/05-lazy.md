# 5 Lazy

## 5.1 Software Upgrade CPP

Delete some old UpgradePackage if necessary to free up some disk space: del upgradepackage=<oldpackage> Create the UpgradePackage MO: cr swmanagement=1,upgradepackage=<name>

At the prompt, enter _FTP Server Address_ where the UP is stored and the path to the _UCF (Upgrade Control File)_. At the next prompts, enter FTP Server _UserID_ and _Password_, or just d for default value (will be **anonymous**) Perform the SW installation:

acc upgradepackage=<name>$ nonblockinginstall

Monitor installation progress:

polu

Perform the SW upgrade: acc upgradepackage=<name>$ rebootnodeupgrade

Monitor upgrade progress (confirmUpgrade will be done automatically): polu

Check that the new cv is using the new upgrade package

cvls

Note: if polu was not run after performing rebootnodeupgrade, the upgrade will have to be manually confirmed:

- get upgradepackage=<name>$ state —> wait until state "awaitingconfirmation"
- acc upgradepackage=<name>$ confirmupgrade

## 5.2 Software Upgrade ECIM/COM

Delete some old UpgradePackage if necessary to free up some disk space: del upgradepackage=<oldpackage> Create the UpgradePackage MO: acc swm=1 createupgradepackage

At the firt prompt, enter the URI from where to fetch the package, eg sftp://<username>@<ipaddress>/<path>

At the next prompt, enter the server password

Perform the SW installation:

acc upgradepackage=<name>$ prepare

Monitor installation progress:

polu

Perform the SW upgrade: acc upgradepackage=<name>$ activate

Monitor upgrade progress (confirmUpgrade will be done automatically): polu

Check that the new cv is using the new upgrade package

cvls

Note: if polu was not run after performing rebootnodeupgrade, the upgrade will have to be manually confirmed:

- get upgradepackage=<name>$ state —> wait until state "awaitingconfirmation"
- acc upgradepackage=<name>$ confirm

## 5.3 RNC Iub operations

- str - view state of all Iub/Cells/Channels/Nbap/Nodesynch in a table format (type h str for more info)
- bl/deb iublink=<iubname>$ - block/deblock an iublink
- bl/deb cell=<cellname> - block/deblock a cell
- str -i <iubname> - view states for sites related to a particular iub filter only

## 5.4 Common RNC Iub Integration Problems

When trying to integrate a new RBS, some data mismatch might cause the _Iub_, _Cell_, or _Channels_ not to come up. Things to check are the values of:

- Transmission
- AAL2 Addresses
- VCI values
- localCellId

Take a print of all MOs related to the Iub and check that the vci values match on both sides, check if any related MOs are down:

lk iublink=<iub> #in RNC lk iub=<iub> #in RBS

Find out the Aal2Ap used by that Iublink in RNC: lk iublink=<iub>

Check that the AAL2 addresses match on all sides:

get aal2routingcase=<rbsroutingcase> (in RNC and RXI) get aal2sp=1 (in RBS and RXI)

Check that the AAL2 path id’s match on both sides:

get aal2pathvcctp=<pathname> pathid (in RNC, RBS, and RXI if applicable)

Check that the aal2 continuitycheck match on both sides:

get aal2pathvcctp=<pathname> continu (in RNC, RBS, and RXI if applicable)

Check that localcellid match on both sides:

get cell=<cell> local (in RBS and RNC)

Perform a loopback test on all VCIs of that iub, to see if transmission is ok

lacc atmport=<port>,vpltp=<vp>,vpctp=1,vcl eteloopback Check RNC/RBS alarms

al

Check RNC devices are ok

std

Check Cell error code, cellbarred, actor info, etc.

ced

tgc/tgd (type "h tg" for info)

Check RNC/RBS general state, look for potential HW/SW faults

dcgm

Check all cross-connects are ok

stc (mainly in RXI/MGW)

Find out the module MP that is handling the site and check if there are some errors:

get iublink= module lh modXX te log read

(to restart the module MP, you can use the command "acc modXX restart")

## 5.5 Common RNC Iu/Iur Integration Problems

Take a print of all MOs related to the Iu and check that the VCI values match on both sides. Also check if any related MOs are down: lk mtp3bsrs=<name>

Perform a loopback test on all VCs of that interface, to see if transmission is OK: lacc atmport=<port>,vpltp=<vp>, eteloopback Check that the pointcodes matches on both sides

get mtp code

Activate/deactivate a C7 link

lacc mtp3bsls=<name>, deactivate/activate

Block/deblock an Aal2Path, check that the _pathId_s and _a2ea_ addresses match on both sides:

bl/deb aal2pathvcctp=<pathname> get aal2pathvcctp=<pathname> pathid get routingcase=<name>
