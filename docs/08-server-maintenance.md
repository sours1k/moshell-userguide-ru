# 8 Server Maintenance

When running moshell on a server in a multi-user environment, there needs to be regular maintenance in order to clean up the disk and any hanging processes.

## 8.1 Hanging Processes

A known bug of moshell is that it doesn’t always shut down all of its spawned processes upon exiting which leads to CPU overload and run out of RAM memory. This problem should now be fixed thanks to the use of various timeouts but if this does not help, then it is recommended to regularly check the rogue processes using the unix command top.

Once the top command is running, you can type the following commands in the top screen:

- n followed by the number of processes to display (e.g n 40) -> to show more than the default number of 15 processes
    - o to change the order of the sorting. E.g:
        - o time (to see the processes that have been running for the longest time)
        - o size (to see the processes that are using up the most memory)
        - o cpu (to see the processes that are using up the most cpu. this is the default).

• k followed by the process to kill. E.g k 2742

**8.2 Disk full**

For disk usage diagnostics and cleanup, please refer to the help of the smd command.

## 8.3 Run out of memory

If you get the following error when trying to start moshell:

gawk: fatal: cannot create child process for ‘/tmp/readlineXXXX_hhmmss’ (fork: Not enough space)".

It means that you do not have enough memory (i.e. RAM + swap space) on the machine.

Try running the command top on the Solaris box (it might not exist on the box though).

If you can run it, you’ll see a line like this:

Memory: 512M real, 107M free, 333M swap in use, 2.0G swap free

A fundamental rule of Operating System management is that your swap space should also be > 2x the memory, so in this box we have 512Mb of RAM so we should have at least 1Gb of RAM (it started with just 256Mb of RAM - and we had this problem after opening a few sessions of MoShell). As a rule - if you are running MoShell on a Solaris box you should give it at least 512Mb of RAM and ideally 2Gb of swap space.

Luckily - there is an easy way to add new swap space - this is to make a new "swap file" on the disk (then you don’t need to repartition everything). You can do this in Solaris by following these steps:

1.  mkfile -v 2000m /usr/swapfile

This will make a 2Gb file **/usr/swapfile** to be used as our extra swap space. But it’s not enabled as swap space yet.. To add it as swap space.

1.  swap -a /usr/swapfile

This adds it in as swap space. But this is not permanent, next time you reboot the machine it’ll disappear. You can make it permanent by adding the following line to (the end of) **/etc/vfstab**

1.  /usr/swapfile - - swap - no -

See man vfstab for more details on **/etc/vfstab**
