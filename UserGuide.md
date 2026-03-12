**MoShell 24.0a User Guide**

This document presents an overview of the functionality included in **MoShell**, command line syntax, revision history and other important information.

It is important that all engineers working with **MoShell** read this document before using the tool as it contains important operational information.

# Contents

1.  **Introduction 6**
    1.  Contact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
    2.  MO concept . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
    3.  O&M services and protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
    4.  MO Tree and MO Naming Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
        1.  LDN - Local Distinguished Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
        2.  RDN - Relative Distinguished Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
        3.  FDN - Full Distinguished Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
    5.  MOM - Managed Object Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
    6.  Moshell Functionality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
        1.  Alarm Service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
        2.  OSE shell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
        3.  Configuration Service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
        4.  Performance Management Service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
        5.  Log service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
        6.  File transfer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.  **Installation and user settings 11**
    1.  Installation for Unix (Solaris/Linux) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
    2.  Installation for Windows (using Cygwin or WSL) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
        1.  Installation for Cygwin 64-bit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
        2.  Installation for WSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
    3.  Starting an moshell session . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
        1.  Starting up Moshell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
        2.  Loading the MO Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
        3.  Performing Actions on Loaded MO Stubs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
    4.  User-specific settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
    5.  Ports used by moshell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
    6.  LDAP roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
    7.  O&M Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.  **Command syntax, including Regular Expressions 19**
    1.  How MOs are Identified . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
        1.  RDN - Relative Distinguished Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
        2.  LDN - Local Distinguished Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
        3.  FDN - Full Distinguished Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
    2.  How to address the MOs in MO-related commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
    3.  Regular Expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
    4.  How to specify attribute values in set/cr/acc commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
    5.  Moshell command line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
    6.  Piping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.  **Command descriptions 24**
    1.  Basic MO commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
        1.  mom\[abcdfloprtuxi\] \[&lt;moclass/struct/enum&gt;\] \[&lt;attribute/action&gt;\] \[&lt;attr-type&gt;\] \[&lt;attr-flags&gt;\] \[&lt;description&gt;\] . 24
        2.  lt &lt;motype-filter&gt;|root|all . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
        3.  lt/ltc &lt;motype-filter&gt;|root|all . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
        4.  lcc &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
        5.  lt/clt/ltc\[1-9\] &lt;motype-filter&gt;|root|all \[&lt;attribute==value&gt; AND/OR &lt;attribute==value&gt;\] . . . . . . . . . . . . . 26
        6.  lc/lcc\[1-9\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
        7.  ld\[c\] &lt;ldn&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
        8.  lu/llu &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
        9.  pr\[s\]\[m\]/lpr\[s\]\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;\] \[&lt;mimName&gt;\] . . . . . . . . . . . . . . . . . . . . . . 28
        10. ma\[i\]/lma\[i\] &lt;moGroup&gt; &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute-filter&gt;\] \[&lt;value-filter&gt;\] . . . . . . . 28
        11. mr\[i\]/lmr\[i\] &lt;moGroup&gt; &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute-filter&gt;\] \[&lt;value-filter&gt;\] . . . . . . . 29
        12. mp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
        13. get\[d\]\[m\]\[i\]/lget\[d\]\[m\]\[i\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\] . . . . . 29 4.1.14 hget\[c\]\[d\]\[m\]\[i\]/lhget\[c\]\[d\]\[m\]\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; \[&lt;attribute-filter&gt;\] \[&lt;value1-filter&gt;\]

\[&lt;value2-filter&gt;\] \[&lt;value3-filter&gt;\] etc... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

- - 1.  kget\[m\]/lkget\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;\] \[&lt;attribute-filter&gt;\] \[&lt;attribute-type&gt;\] \[&lt;attribute-flag&gt;\]

\[&lt;attribute-description&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

- - 1.  zget/lzget \[-n &lt;number&gt;\] \[-t &lt;timeout&gt;\] \[-i &lt;interval&gt;\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute-filter&gt;

&lt;value-filter&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

- - 1.  fro/lfro\[m\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\] . . . . . . . . . . . . . 32
        2.  sql/select &lt;command&gt; \[ | &lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
        3.  st/lst &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;state-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
        4.  prod &lt;moGroup&gt;|&lt;moFilter&gt; \[&lt;productdata-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
        5.  lk/llk &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
        6.  lko/llko &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
        7.  set\[m\]\[c\]\[1\]\[i\]\[p\]\[1x\]/lset\[m\]\[c\]\[1\]\[i\]\[p\]\[1x\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute&gt; \[&lt;value&gt;\] . . . . . . 34
        8.  eset\[c\]\[1\]/leset\[c\]\[1\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute-filter&gt; \[&lt;value&gt;\] . . . . . . . . . . . . . . 35
        9.  rset/lrset &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute&gt; \[&lt;value&gt;\] . . . . . . . . . . . . . . . . . . . . . . . 35
        10. bl\[s\]\[1\]/lbl\[s\]\[1\] \[-t &lt;timeout&gt;\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . 36
        11. deb\[1\]/ldeb\[1\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
        12. acl/lacl &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;action-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . 36
        13. acc\[e\]\[n\]\[y\]/lacc\[e\]\[n\]\[y\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all &lt;action&gt; . . . . . . . . . . . . . . . . . . . . 37 4.1.30 cr\[e\]\[n\]\[1x\] &lt;ldn&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
        14. del\[b\]\[1x\]/ldel\[b\]\[1x\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
        15. rdel/lrdel &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
        16. gm\[c\]\[d\]/lgm\[c\]\[d\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
        17. sc\[g\]\[w\]\[d\] \[&lt;parameterlist&gt;|all\] \[&lt;namespacelist&gt;|all\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
        18. safe+/safe-/safe? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
        19. s+/s++/s-/s? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
        20. u+\[s\]/u-/u?/u!/u!! \[&lt;file&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
        21. run\[x\]\[1\]\[1p\]\[1r\] \[-l &lt;lineNr&gt;\] &lt;command file&gt; \[&lt;var1&gt;\] \[&lt;var2&gt;\] ... . . . . . . . . . . . . . . . . . . . . . . . . 44
        22. trun\[is1cr\] &lt;moScript&gt;|&lt;http://ipaddress/script&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
        23. Ctrl-Z; touch /tmp/xxxx; fg (abort MO command) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
        24. pol\[b\]\[c\]\[d\]\[g\]\[h\]\[i\]\[k\]\[m\]\[p\]\[s\]\[r\]\[u\]\[w\]\[y\] \[-m &lt;mo&gt;\] \[&lt;interval&gt;\] \[&lt;waitTime&gt;\] \[&lt;checkTime&gt;\] . . . . . . . . . . 47
        25. re\[i\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
        26. getmom \[&lt;momversion&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
        27. parsemom \[&lt;momFile&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
        28. flt/fltc &lt;motype-filter&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 4.1.46 fget\[i\]/lfget\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . 49 4.1.47 eget/leget &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . 49

4.1.48 sget/lsget/skget/lskget/shget/lshget &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all . . . . . . . . . . . . . . . . . . . 50 4.1.49 fset\[i\]/lfset\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all &lt;attribute&gt; \[&lt;value&gt;\] \[&lt;attribute-type&gt;\] . . . . . . . . . . 50

- - 1.  facc/lfacc &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all &lt;action&gt; \[&lt;param1&gt;\] \[&lt;param2&gt;\] . . . . . . . . . . . . . . 50
        2.  fdel/lfdel &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
    
    1.  Other MO commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
        1.  cvls/cvmk/cvms/cvset/cvrm\[u\]\[s\]/cvrbrm/cvcu/cvget\[f\]\[u\]\[d\]/cvput/cvls1/cvre/cvfa/cvfd . . . . . . . . . . . . . 51
        2.  inv\[hlxbpctyrgfau\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
        3.  cab\[adefghlmrstxc\] \[ | &lt;unix-cmds&gt; \] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
        4.  sdi\[cjrx\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
        5.  stc\[p\]\[r\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
        6.  std\[ar\] \[&lt;filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
        7.  stv\[b\]\[r\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
        8.  stt\[r\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
        9.  sta\[rc\] \[&lt;Filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 4.2.10 ste\[gr\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
        10. sti\[bcfopr\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
        11. sts\[c\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
        12. str . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
        13. dcg\[meiabsrfkx\] \[-m &lt;rophours&gt;\] \[-e &lt;eventrophours&gt;\] \[-d &lt;logdays&gt;\] \[-b &lt;boards|boardgroup&gt;|all\] \[-r &lt;mogroup&gt;\] \[-k &lt;nrdumps&gt;|&lt;esiGranularity&gt;\] \[-f &lt;mofilter&gt;\] \[-t &lt;seconds&gt;\] \[-t1 &lt;seconds&gt;\] \[-c &lt;collectorprofile&gt;\] \[-de &lt;ddb-enddate&gt;\] \[-d1 &lt;manualddb-minusdays&gt;\] \[-d2 &lt;periodicddb-minusdays&gt;\] \[&lt;logdir&gt;\] . . . 77
        14. stz\[rc01\] \[&lt;Filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
        15. hc\[iuzd\]\[v\] \[-r|-x &lt;numbers&gt;\] \[&lt;hclogfile&gt;|&lt;hclogdir&gt;|&lt;hcreportdir&gt;\] \[&lt;hclogfile2&gt;|&lt;hclogdir2&gt;\] . . . . . . . . 80
        16. trg\[idfubgs\] \[-e &lt;section&gt;\] \[-f &lt;faultString&gt;\] \[-s &lt;searchString&gt;\] \[-t PMDA|BBI\] \[&lt;NodeIP|/path/to/dcgm.zip&gt;\] 82 4.2.18 diff\[a\]\[d\]\[m\]\[o\]\[x\]\[i\]/ldiff\[a\]\[d\]\[m\]\[o\]\[x\]\[i\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
        17. diffs &lt;scRefFile&gt;|&lt;modumpFile&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
        18. w2f &lt;UP&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
        19. lkr\[a\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
        20. resub &lt;IubLink&gt; \[&lt;VplTp&gt;|&lt;Subrack&gt;\] \[&lt;VplTp&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
        21. ir\[cdpsomt\] \[&lt;IubLink&gt;\] \[&lt;CM&gt;\] \[&lt;period&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
        22. rinp\[c\]\[m\] &lt;/path/to/rinpm.json&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 4.2.25 gr\[acdfprsx\] \[&lt;IubLink&gt;\] \[&lt;OtherRNC&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
        23. tg\[r\]\[c\]\[d\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
        24. ueregprint/uer\[d\]\[t\]\[i\]\[s\]\[p\]\[v\] \[-m &lt;mod&gt;|-i &lt;imsi&gt;|-u &lt;ueref&gt;|-n &lt;maxUes&gt;|-c &lt;utrancell&gt;|-r &lt;iublink&gt;\]

\[&lt;attribute-filter&gt;\[=&lt;value&gt;\]|all\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

- - 1.  ced\[h\]\[p\]\[s\]\[g\]\[r\] \[-m &lt;module(s)&gt;|-c &lt;utrancell&gt;|-r &lt;iublink&gt;|-s &lt;rsite&gt;\] \[ | &lt;unix-cmds&gt;\] . . . . . . . . . . . . 97
        2.  al\[atkcg\]\[u\]\[z\] \[-tz &lt;hrs&gt;\] \[-a|-u &lt;alarm-id&gt;\] \[ | &lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
        3.  lg\[abcdefghijklmnopqrstuvwxyz012345678\] \[-l &lt;input-directory|logfile|zipfile&gt;\] \[-m &lt;minustime&gt;\] \[-p &lt;plustime&gt;\] \[-s &lt;startdate&gt;\] \[-e &lt;enddate&gt;\] \[-g &lt;boardgroup&gt;\] \[-r &lt;mogroup&gt;\] \[-n &lt;nodefilter&gt;\] \[-x &lt;XBlogfilter|ESIlog-filter&gt; \] \[-b &lt;xb&gt; \] \[-d &lt;nrdumps&gt;|&lt;esiGranularity&gt;\] \[-z\] \[-tz &lt;hrs&gt;\] \[-c &lt;collector-profile&gt;\] \[-ps &lt;startdate&gt;\] \[-pe &lt;enddate&gt;\] \[-pm &lt;minustime&gt;\] \[-pp &lt;plustime&gt;\] \[&lt;destination-directory&gt;\] \[|&lt;unix-cmds&gt;\] . 101
        4.  mfa\[grcp\] \[-m &lt;hrs&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
        5.  mfc\[rc\] \[&lt;Filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
        6.  mfi\[trc\] \[-s &lt;startdate&gt;\] \[-e &lt;enddate&gt;\] \[-p &lt;hrs&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
        7.  mfs\[hrc\] \[&lt;rfports&gt;\] \[&lt;samplingstep&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
        8.  mft\[adshy\] \[-c &lt;cellId&gt;\] \[-u &lt;ues&gt;\] \[-t &lt;timeout&gt;\] \[-n\] \[-d &lt;duration&gt;\] \[-i &lt;interval&gt;\] \[-o &lt;outputfile&gt;\] <Trace-

Profile(s)>|&lt;MtdCounterProfile(s)&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112

- - 1.  occ \[get|logs\] \[-h|...\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114 4.2.37 orx\[acglpr\] \[-r &lt;radios&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

4.2.38 ori\[shxc\] \[-r &lt;radios&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115 4.2.39 ors\[vdiacp\] \[-r &lt;radios&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

- - 1.  orf\[elptb\] \[-r &lt;radios&gt;\] \[directory\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
        2.  ort\[se\] -r &lt;radio&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
        3.  orp\[cdeirstux\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
    
    1.  Other commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
        1.  uv \[&lt;string&gt;|&lt;var&gt;=value\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
        2.  pv \[&lt;string&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
        3.  !/l &lt;unix-command&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
        4.  l+\[m\]\[m\]\[s\]\[o\]/l-\[s\]/l? \[&lt;logfile&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
        5.  dbc\[s\]\[a\] \[&lt;cvname&gt;|&lt;dbdat-file&gt;|&lt;cvzip-file&gt;|&lt;mobatch-folder&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . 123
        6.  dbd\[p\] \[&lt;cvname&gt;|&lt;dbdat-file&gt;|&lt;cvzip-file&gt;\] \[&lt;cvname&gt;|&lt;dbdat-file&gt;|&lt;cvzip-file&gt;\] . . . . . . . . . . . . . . . 129
        7.  dbcv\[r\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
        8.  &lt;ose/coli command&gt; \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
        9.  coli . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 4.3.10 comcli . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 4.3.11 ecli . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 4.3.12 esci . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 4.3.13 netconf\[y\]\[g\]\[gx\] \[&lt;commandfile&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 4.3.14 c+/c1/c2/c-/c?/c0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133 4.3.15 &lt;linux/rcs-coli/comcli command&gt; \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133 4.3.16 mcl\[d\] \[&lt;moClass-filter&gt;\] \[&lt;command-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134 4.3.17 mcc/lmcc &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;comcli commands(s)&gt; \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . 134
        10. bo\[ar\]/ba\[swdpmu\]/br\[wdm\]/be\[0-50\]/bp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
        11. lh\[z\]\[x\] &lt;boardGroup&gt;|&lt;moGroup&gt; &lt;OSE-command&gt;|run &lt;commandfile&gt; \[ | &lt;unix-cmds&gt;\] . . . . . . . . . 137
        12. mon\[?\]\[d\]\[u\]\[c\]\[f\]\[s\]\[t\]\[k\]\[a\]\[x\]\[e\]\[-\] \[&lt;board(s)|<boardGroup(s)&gt;\] \[&lt;/path/to/logfile&gt;\] . . . . . . . . . . . . . . . 138
        13. sql+/sql-/sql? \[&lt;heap&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
        14. pgu\[c\]\[f\]\[r\] \[-p &lt;board1,board2,...&gt;\] /path/to/newLM \[&lt;cvcomment&gt;\] . . . . . . . . . . . . . . . . . . . . . . 140
        15. procload/proctemp \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
        16. proglist/progkill \[-e\] \[&lt;string&gt;\] \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
        17. fte &lt;te-command&gt; \[&lt;trace-groups&gt;|all\] \[&lt;string&gt;\] \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . 142 4.3.26 goxb\[acib\] \[-p &lt;advpw&gt;\] &lt;commands&gt; \[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
        18. ftree\[f\]\[d\]\[1\] \[&lt;lnh&gt;/\]\[&lt;directory&gt;\] \[| &lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
        19. ftget\[1\]\[c\]/ftput\[1\]\[c\]/ftdel\[1\]\[a\]/ftrun \[&lt;options&gt;\] &lt;source&gt;\[/\*\] \[&lt;destination&gt;\] . . . . . . . . . . . . . . . . . . 144
        20. htget &lt;remotefile&gt; \[&lt;localfile/localdir&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
        21. edit &lt;remotefile&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
        22. fclean\[f|ff|a|d|e\] \[&lt;lnh&gt;/\]\[&lt;directory&gt;\] \[-f &lt;filename-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
        23. hi \[&lt;commandFilter&gt;\], !&lt;commandNr&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147 4.3.33 time\[t\] &lt;command&gt;|&lt;logfile&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
        24. pipe &lt;command&gt; | &lt;unix-command&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
        25. lmid\[c\]\[h\]/upid\[om\] &lt;pattern&gt;|refresh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148 4.3.36 p/w/pw/b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148 4.3.37 prox\[+-\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
        26. col . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
        27. ul . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
        28. conf\[bld\]\[+-\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149 4.3.41 gs\[+-\]/gsg\[+-\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149 4.3.42 ip2d &lt;ip-address&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
        29. d2ip/h2ip &lt;number&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
        30. h2d/d2h &lt;number&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150 4.3.45 h2b/b2h &lt;number&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150 4.3.46 d2b/b2d &lt;number&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
        31. rb2ip \[&lt;iublink&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
        32. z2f \[&lt;zipfile&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
        33. encpw\[f\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
        34. mos2ro &lt;moshell.zip&gt; \[/path/to/destinationfolder/\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
        35. gpg &lt;file&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
        36. enm &lt;command&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
        37. wait &lt;delay&gt;|&lt;newtime&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
        38. wf\[o\]\[a\]\[t\] &lt;file&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
        39. return . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154 4.3.56 print . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
        40. alias\[f\]/unalias &lt;alias&gt; &lt;command&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
        41. lf\[c\] &lt;file&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
        42. bg\[g\]/bgs/bgw \[&lt;commands&gt;|&lt;id(s)&gt;|all\] \[&lt;maxtime&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155 4.3.60 - smd\[slcr\] \[-m &lt;days&gt;\] \[-s &lt;size&gt;\] \[-f &lt;filter&gt;\] \[-o a|s|n\] \[-u &lt;user&gt;|all\] \[-d &lt;directory&gt;\] \[-n &lt;max&gt;\] . . . . . . 156
        43. split \[&lt;size&gt;\] &lt;file&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
        44. \- dia\[g|gu||k|kf|ls|ds|os|pn|ln|dn|le|lv|ac|pc|lc|sa|pfs|lfs|pfm|lns\] \[&lt;ME addr|ME Name&gt; &lt;ME addr|ME name&gt;

&lt;ME addr|ME name&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

- - 1.  pe\[c\]\[l\]\[k\] \[&lt;polling interval&gt;|&lt;pid&gt;\] \[&lt;trigger&gt;\] \[&lt;action script&gt;\] \[&lt;number of iterations&gt;\] . . . . . . . . . . . 158
        2.  q/by/exit/quit \[&lt;exitcode&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
    
    1.  PM commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
        1.  pmom\[acdpo\] \[&lt;moclass&gt;\] \[&lt;counter&gt;\] \[&lt;data-type&gt;\] \[&lt;flags&gt;\] \[&lt;description&gt;\] . . . . . . . . . . . . . . . . 159
        2.  kmom\[d\] \[&lt;area&gt;\] \[&lt;kpiname&gt;\] \[&lt;MOclass&gt;\] \[&lt;formula&gt;\] \[&lt;kpidescription&gt;\] . . . . . . . . . . . . . . . . . . 160
        3.  pget\[m\]/lpget\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\] . . . . . . . . . 160
        4.  spget/lspget \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\] . . . . . . . . . . . 161
        5.  hpget\[c\]\[m\]/lhpget\[c\]\[m\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; \[&lt;attribute-filter&gt;\] \[&lt;value1-filter&gt;\] \[<value2-

filter>\] \[&lt;value3-filter&gt;\] etc... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

- - 1.  pdiff/lpdiff \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\] . . . . . . . . . . . . 161
        2.  hpdiff\[m\]/lhpdiff\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value1-filter&gt;\] \[<value2-

filter>\] \[&lt;value3-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

- - 1.  pmx\[hfdnsckwlb3zeity\] \[&lt;mofilter&gt;|&lt;mogroup&gt;\] \[&lt;counter-filter&gt;|&lt;kpi(s)&gt;\] \[-z &lt;mogroup&gt;\] \[-l &lt;zipfile&gt;|&lt;directory&gt;\] \[-w &lt;webdirectory&gt;\] \[-m &lt;minushours&gt;\] \[-p &lt;plushours&gt;\] \[-s &lt;startdate&gt;\[.&lt;starttime&gt;\]\] \[-e &lt;enddate&gt;\[.&lt;endtime&gt;\]\] \[-a|-d|-h|-u\] \[-o &lt;outputFormat&gt;\] \[-tz &lt;hrs&gt;\] \[-f &lt;formulafile&gt;\] \[-j &lt;precision&gt;\] \[-mo

&lt;regexp&gt;\] \[| &lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162

- - 1.  pmx2\[h\]\[f\] &lt;mo-filter&gt; &lt;counter-filter&gt; \[-u\] \[-i 0|1|2\] \[&lt;time options&gt;\] \[-o &lt;outputFormat&gt;\] \[ | &lt;unix-cmds&gt;\] . . 164
        2.  pmr\[agfkwop3z\] \[-g &lt;mofilter&gt;|&lt;mogroup&gt;\] \[-z &lt;mogroup&gt;\] \[-r &lt;report(s)&gt;\] \[-l &lt;zipfile&gt;|&lt;directory&gt;\] \[-w &lt;webdirectory&gt;\] \[-i &lt;iubCellModule-file&gt;\] \[-f &lt;formulafile&gt;\] \[-c &lt;configfile&gt;\] \[-m &lt;minushours&gt;\] \[-p &lt;plushours&gt;\] \[-s &lt;startdate&gt;\[.&lt;starttime&gt;\]\] \[-e &lt;enddate&gt;\[.&lt;endtime&gt;\]\] \[-o &lt;outputFormat&gt;\] \[-t &lt;thresholdfile&gt;\] \[-tz &lt;hrs&gt;\]

\[|&lt;unix-cmds&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165

- - 1.  pme\[fd\]\[cgurvxyz\] \[&lt;pm_logdir|uehexcep.zip&gt;\] \[-b &lt;boardgroup&gt;\] \[-f\] \[-m &lt;minushours&gt;\] \[-p &lt;plushours&gt;\] \[-s

&lt;startdate&gt;\[.&lt;starttime&gt;\]\] \[-e &lt;enddate&gt;\[.&lt;endtime&gt;\]\] \[-o &lt;uehoptions&gt;\] . . . . . . . . . . . . . . . . . . . . 168

- - 1.  pst \[&lt;scan-filter&gt;|&lt;scan-proxy&gt;\] \[&lt;scan-state&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
        2.  pgets\[m\]\[n\]\[r\] \[&lt;scan-filter&gt;|&lt;scan-proxy&gt;\] \[&lt;contents-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . 169
        3.  pcr\[pcfpdazg\]/lpcr\[pcfpdazg\] &lt;ScannerName|JobName&gt; &lt;moclass-filter&gt;|&lt;moinstance-filter&gt;|&lt;mogroup&gt;|&lt;counter-file&gt; \[&lt;counter-filter&gt;\] \[&lt;granularity&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
        4.  pcrk\[f\]\[v\]\[d\] \[&lt;kpidefinitionfile&gt;\] \[&lt;granularity&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172 4.4.16 pbl &lt;scan-filter&gt;|&lt;scan-proxy&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172 4.4.17 pdeb &lt;scan-filter&gt;|&lt;scan-proxy&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172 4.4.18 pdel &lt;scan-filter&gt;|&lt;scan-proxy&gt; . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
        5.  emom \[uetr|gpeh|ctr|all\] \[&lt;event-filter&gt;\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
        6.  pset\[d\] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173

1.  **Lazy 174**
    1.  Software Upgrade CPP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174 5.2 Software Upgrade ECIM/COM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
    2.  RNC Iub operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
    3.  Common RNC Iub Integration Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
    4.  Common RNC Iu/Iur Integration Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177

EAB Finn Magnusson 2023-12-31 FH moshellUserGuide.tex

1.  **Scripting 177**
    1.  Preset Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
    2.  Variable assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
    3.  Hashtables (arrays) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
    4.  If/Else constructs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
    5.  For constructs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
    6.  User-defined functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
    7.  Nesting for and if statements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
    8.  Example scripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
2.  **Utilities 189**
3.  **Server Maintenance 190**
    1.  Hanging Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
    2.  Disk full . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
    3.  Run out of memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
4.  **Modes of operation 191**
    1.  Offline Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
    2.  SQL Mode for CPP Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
    3.  Multi Mode for CPP Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
    4.  Yang Mode for Cloud-RAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
    5.  Router6000 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
5.  **Revision History 193**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Document responsible/Approved** | **Checked** | **Date** | **Rev.** | **File** |
| EAB Finn Magnusson |     | 2023-12-31 | FH  | moshellUserGuide.tex |

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

|     |     |
| --- | --- |
| \* \| FRO \| | \*  |
| \* \| \| Resource Layer | \*  |
| \* \| RO \| | \*  |
| \* \| \| | \*  |
| \* +++++++ | \*  |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The O&M client can access the MOs through a number of services:

- - _Configuration Service_ (CS): to read and change configuration data. Configuration data is stored in the MO attributes.
    - _Performance Measurement_ (PM): to setup statistics scanners or event filters. The statistics counters are stored in MO pm-attributes and output to an XML file every 15 minutes. The events are output into binary files every 15 minutes.
    - _Alarm Service_ (AS): to retrieve the list of alarms currently active on each MO.
    - _Notification Service_ (NS): to subscribe and receive notifications from the node, informing about parameter/alarm changes in the MOs.
    - _Log Service_ (LS): to save a log of certain events such as changes in the configuration, alarms raising and ceasing, node/board restarts, jvm events, O&M security events, etc

The MO is a way of modelling resources in a node. It consists of:

- 1.  A _Management Adaption Layer_

The purpose of the MAO (Management Adaptation Object) is to interface towards the various O&M services described above.

- 1.  A _Resource Layer_ consisting of Facade Resource Object (FRO) and a Resource Object (RO) . The RO is the actual resource modelised by the MO. The purpose of the FRO is to act as an interface between the MAO and the RO, by handling the configuration transactions and storing configuration data for the RO.

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

&lt;------------------------------------------------------------............................................................&gt; LDN (Local Distinguished Name)

&lt;----MIB Prefix-----------------------&gt;&lt;--------------................................................................&gt; MoClass Identity

&lt;-----&gt; &lt;---&gt; RDN (Relative Distinguished Name)

&lt;---------&gt;

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1 RDN

&lt;--------&gt;

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1 RDN &lt;-----&gt;

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS RDN &lt;----------&gt;

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS,Slot=19 RDN

&lt;-------------------&gt;

Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1 Network=H3GA,Utran=Rnc1,MeContext=Rbs03,ManagedElement=1,Equipment=1,Subrack=MS,Slot=19,PlugInUnit=1,Program=DbmFpgaLoader

## 1.5 MOM - Managed Object Model

Each MO class contains a number of attributes which are used to store _configuration data_ or _performance measurement data_.

Each MO class can also support a number of defined _actions_. These represent certain operations which can be performed by the MO. A typical example is the action **restart** which will cause the MO to restart the resource it is responsible for (e.g. a board, a program, etc.).

The _Managed Object Model_ (MOM) is a reference document describing all the MO Classes that can exist in a node, together with their _attributes_ and _actions_.

The format of the MOM can be UML, XML, HTML, or MS-Word.

The XML version of the MOM is usually stored on the web server of the node, eg at

http://&lt;ipaddress&gt;/cello/oe/xml/&lt;filename&gt;.xml (CPP), https://&lt;ipaddress&gt;/models/ (MSRBS) The MOMs for each SW release are also stored in HTML format in the CPI.

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

# 2 Installation and user settings

## 2.1 Installation for Unix (Solaris/Linux)

Copy the moshell installation package **moshellxxx.zip** to your home directory **/home/youruser** or to the temp directory **/tmp**. Very important: do not store the zip file inside the moshell folder otherwise the installation will be corrupted.

Then go to the folder containing the zipfile (cd &lt;folder&gt;) and run the following commands:

unzip -o moshellxxx.zip bash moshell_install

When prompted to enter the directory where you want to install moshell, it is recommended to specify your HOME directory ( ~). If you have executed moshell_install from your home directory then you can press the enter key and the current directory is selected.

If a previous moshell installation already exists, it is recommended to install in the same directory as the old one. This way, all your custom files (jar/xml files, site files, etc.) get copied across to the new revision and the old revision gets moved to a different location so you can still access it if needed.

When prompted to enter the path to java, make sure to use Oracle Java or OpenJDK (https://jdk.java.net/archive/)

Note: In the case of AMOS installation use option -a, ie: bash moshell_install -a (must be run as root on OSS masterserver).

Note: for linux 64-bit, the 32-bit libc library is required, the package name is libc6-i386 or glibc.i686 or ia32-libs.

(Other packages which may be needed for certain commands are python and expect.)

Running moshell for the first time:

If you have set the PATH variable correctly in your ~/.bashrc file, you should be able to run moshell from any directory. E.g: moshell &lt;ipaddress&gt;

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
    - - under _Archive_ select _zip_ and _unzip_
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

In the "Run" window, type: cmd , then press &lt;enter&gt;.

A DOS window opens. At the DOS prompt, execute the following commands:

cd c:\\ cd cygwin64 bin\\perl.exe cygwin_install.txt

This will create the following files: c:/cygwin64/etc/profile, c:/cygwin64/cygwin64.bat, c:/cygwin64/home/youruserid/.bashrc, c:/cygwin64/home/youruserid/.minttyrc, c:/cygwin64/home/youruserid/.inputrc.

If those files already exist, they are automatically moved to the folder c:/cygwin64/tmp/installbackup.

1.  Open a new cygwin terminal window. The window should be black with white text and the prompt should like this: \[~\]$ If not, then go through all the steps again and make sure you haven’t missed out anything.

If you had a 32-bit cygwin installation earlier, note that your c:/cygwin/home/youruser folder can be copied over to c:/cygwin64/home/

More info about Cygwin installation issues can be found at: http://cygwin.com/faq/faq0.html

Uninstall instructions for cygwin can be found at http://cygwin.com/faq/faq.setup.html#faq.setup.uninstall-all

1.  Moshell installation. Follows these steps if you already have a working Cygwin environment.
    - - Copy the moshell installation package **moshellxxx.zip** to your home directory **c:/cygwin64/home/youruserid**
        - Open the cygwin shell and run:

unzip -o moshellxxx.zip bash moshell_install

When prompted to enter the directory where you want to install moshell, it is recommended to specify your HOME directory ( ~).

If you have executed moshell_install from your home directory then you can press the enter key and the current directory is selected.

If a previous moshell installation already exists, it is recommended to install in the same directory as the old one. This way, all your custom files (jar/xml files, site files, etc.) get copied across to the new revision and the old revision gets moved to a different location so you can still access it if needed.

When prompted to enter the path to Java, just type java .

1.  Running moshell for the first time

If you have set the PATH variable correctly in your **~/.bashrc** file, you should be able to run moshell from any directory. E.g: moshell &lt;ip-address&gt;

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

- - sudo apt-get install python3.8 python3-pip
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

A Moshell session is started from the Unix shell prompt using command: moshell &lt;node-name&gt;|&lt;node-address&gt;

If connecting with node name, an entry must exist in the ipdatabase file reference the node name against an ip or dns address.

Other ways of starting moshell are described by typing moshell on its own as well as in chapter Section 9 (Offline mode/multi mode Chapter) .

Upon startup, and running the command "lt all", moshell will go through the following steps:

1.  If CPP, download the node’s IOR file and store it on the workstation. The node’s IOR file is fetched from http://nodeipaddress/cello/ior_files/nameroot.ior
2.  Check the node’s MOM version. If CPP, the node’s MOM is fetched from http://nodeipaddress/cello/oe/xml/&lt;filename&gt; where &lt;filename&gt; is one of the files listed in the user variable xmlmomlist. If MSRBS, the node’s MOM is fetched from https://&lt;nodeipaddress&gt;/models. If YANG, the node’s MOM is downloaded over NETCONF. The MOM version is derived from the "mim" tag inside the MOM file, eg:

&lt;mim name="RNC_NODE_MODEL_E" version="5" release="3"&gt; becomes RNC_NODE_MODEL_E_5_3. If this MOM version does not exist on the workstation (under moshell/jarxml directory), then it is downloaded from the node and stored in that directory. If CPP and the MOM version could not be figured out (ie. moshell could not find any MOM on the node), the MOM specified in the moshell uservariable default_mom is used.

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

pr plu #then lookup the proxy identity of that MO get &lt;proxy&gt; #enter the MOs proxy identity as argument to the "get" command

OR lget ms,slot=19,pluginunit=1$

1.  Example: To read the MO attributes of all MOs whose MO class is _PlugInUnit_

get plu #the get command will operate on all MOs whose RDN matches "plu"

More info about this in Section 3 or by typing h syntax at the Moshell prompt.

Help for each command can be found in Section 4 or by typing h &lt;command-name&gt; at the Moshell prompt.

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

- - comcli=25: uses credential and password specified in sa_credential (default: /Ericsson/OMSec/sam.p12) and sa_password (set when downloading the sam.p12 from SLS)
    - comcli=26: uses credential files specified in clientpem and capem
    - comcli=29: uses credential files specified in clientpem, capem, and keypem
- File export: the uservariables export_username/export_password can be used for specifying the sftp/ftpes server login. The uservariable "export_protocol" can be used to specify export over SFTP (0: default) or FTPES (1).

**Uservariables for YANG nodes security**

- SSH access: the ssh/sftp login can be specified in the uservariables "yang_username/yang_password"
- TLS access: the uservariable "use_tls" is used to specify the type of credential to use
    - use_tls=31: uses credential file specified in ca_credential (default: /Ericsson/OMSec/CAcert/ssucredentials.p12) and ca_password (default: $USER)
    - use_tls=21: uses credential files specified in clientpem, capem, and keypem

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

- 1.  pr 4-10 prints MO proxies from 4 to 10.
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
- | - OR
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

- - in cr command, type null or d. This is only supported for non-mandatory (restricted) attributes, because mandatory attributes must be given a value.
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
- **Ctrl-d or &lt;del&gt;** \- delete one character forward
- **Ctrl-a or &lt;home&gt;** \- go to beginning of line
- **Ctrl-e or &lt;end&gt;** \- go to end of line
- **Ctrl-u** \- erase all characters backward
- **Ctrl-k** \- erase all characters forward
- **Alt-f** \- move forward one word

**Alt-b** \- move backward one word

**select or select + ctrl-&lt;insert&gt;** \- copy to clipboard

- **&lt;insert&gt; or shift-&lt;insert&gt;** \- paste from clipboard

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

# 4 Command descriptions

Here all the commands and their syntax which are possible using Moshell are supported. Each of the OSE shell commands are not mentioned specifically, but it is possible to run all of them through Moshell.

## 4.1 Basic MO commands

**4.1.1 mom\[abcdfloprtuxi\] \[&lt;moclass/struct/enum&gt;\] \[&lt;attribute/action&gt;\] \[&lt;attr-type&gt;\] \[&lt;attr-flags&gt;\] \[&lt;description&gt;\]**

Print description of _MO Classes, CM/FM Attributes, Actions, Enumerations and Structures_.

Regular expressions can be used in the various filters. There are five levels of filtering, as shown in the command syntax.

**Options:**

- a : show only the definitions relating to application MOs
- b : shows the default attribute values.
- c : show all the MO classes specified in the filter as well as their children/grandchildren/etc classes.
- d : gives a shorter printout, without the description part.
- f : shows the attribute flags (only applies when combined with options "b", "r", "l")
- i : only show the EricssonOnly attributes
- l : shows the attribute value lengths.
- p : show only the definitions relating to platform MOs (CPP)
- r : shows the valid attribute value range.
- x : show unidirectional and bidirectional MO relationships
- t : show MO containment relationships and cardinality in tree format
- tl: show MO containment relationships and cardinality in LDN format

Some of the options can be combined, see examples below.

After execution of the MOM command, two scripting variables are automatically created:

$moclass_filer : contains a regular expression matching all MO classes that were printed by the command

$attrib_filter : contains a regular expression matching all attributes that were printed by the command

These variables can then be used in the "get" command to read attributes matching certain MOM conditions based on the attribute name, data type, flag, or description text. In kget command, it is possible to specify the MOM conditions directly from the kget command arguments.

**MO tree view:**

The command momt shows three tables: first table with all valid LDNs, second table with parent MO(s), and third with children MO(s).

The first argument can be used to show only MO classes matching the filter.

The options o, u, l (momto/momtu/momtl) can be used to show only certain specific tables: momtl for the LDN table, momto for the parent table (MOs over), and momtu for the children table (MOs under).

**Examples:**

1.  momt - View the whole MO tree
2.  momt atmp - View all possible parents and children of the **AtmPort** MO
3.  mom atmp - View a description of the **AtmPort** MO
4.  momcd atmp - List all MO classes under the **AtmPort** MO
5.  momc atmp - View a description of all MO classes under the **AtmPort** MO
6.  mom vcl - View a description of the MO class **VclTp**
7.  mom vcl . - View a description of all attributes of MO class **VclTp**
8.  momdi . . . !readonly - List all EricssonOnly attributes that are not readOnly
9.  momd . restart - List all attributes and actions matching the word _restart_
10. momd . . struct - List all attributes of type struct and/or all actions containing struct parameters
11. momd . . . restricted - List all attributes that have the restricted flag
12. momd utrancell . . !restricted|readonly - List all utrancell attributes that do not have the restricted or readonly

flag

1.  momd . . . . license - List all MOs, attributes and actions whose description contains the word _license_
2.  mom . . . . license - View the description of all MOs, attributes and actions whose description contains the word _license_
3.  momd restart . - List all struct or enumerates matching the word _restart_
4.  mom restart . - View the description of all struct or enumerates matching the word _restart_
5.  momd . . enumref:admst - List all attributes of type _enumRef:AdmState_
6.  mom adminproductda . - View a description of all struct members contained in struct _AdminProductData_
7.  momd . . sequence:moref restricted - List all attributes of type _sequence:moRef_ who have a flag _restricted_
8.  momb utrancell - List the default values for all attributes in the MO class UtranCell
9.  mombf utrancell . . !restricted - List the default values for all UtranCell attributes that do not have the flag _restricted_
10. mombr . power|pwr - List the default values and valid ranges for all attributes that match the word power or pwr
11. momx - Show the relationships between MO classes
12. momx iublink - Show the relationships to and from IubLink
13. momx iublink.\*utrancell|utrancell.\*iublink - Show the relationships between IubLink and UtranCell
14. momx reservedby - Show the relationships connected via reservedBy attribute
15. mom . . ^moref, then get . $attrib_filter - Print attribute values for all attributes of data type moRef

**4.1.2 lt &lt;motype-filter&gt;|root|all**

Load MO tree and build proxy table - COM Nodes.

Arguments:

- root: clear the proxy table and allocate a proxy for the root MO (ManagedElement)

all: clear the proxy table, then load the whole MO tree and build a proxy table with all MO instances.

&lt;motype-filter&gt;: load MO instances of MO-type matching the filter. For instance:

- - lt cell : load all MOs of type matching the string "cell", this will usually be the MOs such as "EUtranCellFDD", "NodeBLocalCell", etc
    - clt cell : conditionally load all MOs of type matching the string "cell". Loading is only performed if no MOs of this type are already loaded.
    - lt ^eutrancell|termpoint : load MO instances of type matching the string "eutrancell" or "termpoint"

The pattern in motype-filter is a regular expression, more information can be found with command "h syntax" and "h pr". The argument root/all clears the proxy table, whereas lt &lt;motype-filter&gt; doesn’t, so the MO LDNs get appended to the existing table.

If the same MO type is loaded several times, only the latest fetched instance is kept. Previously fetched instances of that MO type are deleted from the internal table.

**4.1.3 lt/ltc &lt;motype-filter&gt;|root|all**

Load MO tree and build proxy table - YANG Nodes.

Arguments:

- root: clear the proxy table and allocate a proxy for the root MO (ManagedElement)
- all: clear the proxy table, then load the whole MO tree and build a proxy table with all MO instances.
- &lt;motype-filter&gt;: load MO instances of MO-type matching the filter. For instance:
    - lt cell : load all MOs of type matching the string "cell", this will usually be the MOs such as "EUtranCellFDD", "NodeBLocalCell", etc
    - lt ^eutrancell|termpoint : load MO instances of type matching the string "eutrancell" or "termpoint"
    - ltc gnbdufunction : load all MOs of type matching the string "gnbdufunction" and their children/grandchildren/etc

The pattern in motype-filter is a regular expression, more information can be found with command "h syntax" and "h pr". The argument root/all clears the proxy table, whereas lt &lt;motype-filter&gt; doesn’t, so the MO LDNs get appended to the existing table.

If the same MO type is loaded several times, only the latest fetched instance is kept. Previously fetched instances of that MO type are deleted from the internal table.

**4.1.4 lcc &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Load MO tree and build proxy table - COM Nodes

The "lcc" command is for loading the LDNs of the children MOs lying under one or more MO instances.

The parameters of the command are:

- &lt;proxy(s)&gt;: list children of one or several MO’s given their proxy id. For instance: lcc 5 : load all levels of children for the MO with proxy id 5
- &lt;moFilter&gt;: list children of all MO’s whose RDN match the pattern. For instance: lcc equipment=1 : load all levels of children under the MOs whose RDN match "equipment=1"

The pattern in mo-filter is a regular expression, more information can be found with command "h syntax" and "h pr".

**4.1.5 lt/clt/ltc\[1-9\] &lt;motype-filter&gt;|root|all \[&lt;attribute==value&gt; AND/OR &lt;attribute==value&gt;\]**

Load MO tree (full or partial) and build proxy table - CPP Nodes.

lt stands for _Load MO Types_, clt stands for _Conditional Load mo Types_, ltc stands for _Load MO Types and their Children_. The numeric option in ltc is for specifying the number of levels of children to load. Without the option, all levels of children are loaded.

This command queries the node to find out which MOs it contains and creates a table with the MO LDNs and a proxy number.

The first argument of the lt/clt/ltc command can be:

- _root_ clear the proxy table and allocate a proxy for the root MO (ManagedElement)
- _all_ clear the proxy table, then load the whole MO tree and build a proxy table with all MO instances.

_all!&lt;motype-filter&gt;_ clear the proxy table, then build a proxy table with all MO’s except some MO classes.

_&lt;motype-filter&gt;_ get a proxy for all MO types matching the specified pattern.

**Examples:**

1.  lt atmpor - load all MOs of type matching the string "atmpor", this will usually be the **AtmPort** MOs
2.  clt atmpor - conditionally load all MOs of type matching the string "atmpor". Loading only performed if no MOs of this type are already loaded.
3.  ltc equipm - load the Equipment MO and all its children (all the way down)
4.  ltc1 equipm - load the Equipment MO and only one level of children
5.  ltc2 transp - load the Transport MO and two level of children
6.  lt ^utrancell|fach|rach|pch - load all utrancells, fach, rach, pch MOs 7. lt iub - load all iublinks

8\. lt all!relation - load all MOs except the utranrelation/gsmrelation MOs.

The pattern in _motype-filter_ is a regular expression, more information can be found with command h syntax and h pr

The argument _root/all_ clears the proxy table, whereas lt &lt;motype-filter&gt; doesn’t, so the MO LDNs get appended to the existing table.

If the same MO type is loaded several times, only the latest fetched instance is kept. Previously fetched instances of that MO type are deleted from the internal table.

The second argument (optional) is a filter constraint for the attribute value. Example:

1.  lt utrancell operationalState==0 - load proxys for all disabled cells
2.  lt utrancell primaryCpichPower==270 - load proxys for all cells that have pichpower=270
3.  lt all operationalState==0 OR administrativeState==0 - load proxys for all MOs in the node that have opstate 0 or admstate 0.
4.  ltc rncfunction operationalState==0 - load proxys for all MOs under RncFunction that have opstate 0.

Note: This type of search is very hard for the node if it has to search through a large number of MOs (ie several thousand).

For more information about Filter constraint, refer to: MO Client Interface User Guide 1553-CXA 104 210 (internal Ericsson document).

**4.1.6 lc/lcc\[1-9\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all**

Load MO tree (full or partial) and build proxy table - CPP Nodes.

The lc command is for loading the LDNs of the children MOs lying under an MO or group of MOs. lc on its own or combined with the numeric option "1" will only load the direct children. With the numeric options 2 to 9 it is possible to specify the number of levels of children to be loaded. The "c" option (lcc command) is for loading all possible levels of children under the MO.

The parameters of the command are:

- _all_ clear the proxy table, then load the whole MO tree and build a proxy table with all MO instances.
- _&lt;proxy(s)&gt;_ \- load children of one or several MO’s given their proxy id. For example:
    - lc 0 load the direct children of the ManagedElement MO (only one level of children)
    - lc2 0 load two levels of children under ManagedElement MO
    - lcc 0 load all levels of children of the ManagedElement MO (same as lc all or lt all).
    - lc 5 6 7 load children of proxys 5, 6, and 7.
- _&lt;moFilter&gt;_ \- loads children of all MOs whose RDN match the pattern. For example:
    - lc3 transportnetwork=1 load three levels of children under TransportNetwork MO
    - lc cell=3002 loads direct children for MOs whose RDN match **cell=3002**
    - lcc ms-24-1 loads children of all MOs whose RDN match **ms-24-1**

The pattern in _mo-filter_ is a regular expression, more information can be found with command h syntax and h pr.

**4.1.7 ld\[c\] &lt;ldn&gt;**

Load one MO instance and (optionally) the MO tree below it

ld stands for _Load LDN_. This command loads a proxy for an MO, given its LDN. The LDN doesn’t need to contain _ManagedElement=1_, this is assumed.

The MO types are not case sensitive but the MO-ID is.

With the c option, the subtree below the MO is also loaded.

**Examples:**

- ld transportnetwork=1,atmport=MS-6-1,vpltp=vp1,vpctp=1,vcltp=36 - load the MO instance that has this LDN
- ldc equipment=1 - load the MO with LDN "Equipment=1" as well as the MO tree below it.

**4.1.8 lu/llu &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Unload MOs from MO tree.

The purpose is to reduce the size of the proxy table by unloading unwanted MOs. This is useful on large nodes with > 50,000 MOs. Memory usage on the workstation will be reduced and MO commands will be faster. The typical case is to unload all relation MOs in the RNC (UtranRelation and GsmRelation) which are very numerous but not used in most commands.

Example:

- lt all
- lu relation

**4.1.9 pr\[s\]\[m\]/lpr\[s\]\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;\] \[&lt;mimName&gt;\]**

Print MO LDNs and proxy ids for all or part of the MO tree currently loaded in moshell.

**Options:**

- s (silent) : to print only the total number of MOs matched in each MO class.
- m (mim) : to print the mimName of each MO instance. Only applicable for COM/ECIM nodes.

**Examples:**

- pr - print all MOs
- pr 0-1000 - prints the MOs with proxy id 0 to 1000
- lpr subrack=ms - print all MOs whose LDN match subrack=ms. This will print the MO Subrack=MS as well as all its children.
- pr !utranrel - print all MOs except those with an RDN matching _utranrel_

For further information see Section 3 or h syntax.

Note: The pr command is useful to test patterns used in mo-filters. For instance, some patterns will match more MOs than expected, which will result in executing a command on some unwanted MO’s. Therefore, it is good to first try the pattern on the pr/lpr command, then do it "for real" on a command that actually communicates with the node. The pr/lpr command also shows the total number of MOs matching the pattern.

**4.1.10 ma\[i\]/lma\[i\] &lt;moGroup&gt; &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute-filter&gt;\] \[&lt;value-filter&gt;\]**

Add MO(s) to an MO group.

The first argument (mandatory) indicates the name of the MO-Group.

The second argument (mandatory) indicates the Proxy Id’s or MO-Filter of the MOs to match.

If no further arguments are given then the MOs whose RDN/LDN match the MO-filter (or who have the corresponding proxy) will be put in the MO-Group.

If further arguments are given then a get or pget command is performed using the second/third(/fourth) argument of the ma/lma command.

If option "i" was given (mai/lmai) then the command "geti" is used instead of "get".

The third argument will be a string to match the attribute and the fourth (if it’s used) will match the value.

If the attribute is of any other type than MoRef, then the MO(s) whose attribute match the fourth argument will be put in the group. If the attribute is of type MoRef, then the MO(s) contained in the attribute is put in the group (except if there is a fourth argument).

Refer to the following examples:

- ma test atmport.\*24-1 - all MOs whose RDN match **atmport.\*24-1** are put in the group _test_
- lma test atmport.\*24-1 - all MOs whose LDN match **atmport.\*24-1** are put in the group _test_
- ma test atmport operationalst 0 - all MOs whose RDN match **atmport** and who have _operationalState_ matching "0" will be put in the group _test_
- ma test atmport physpathterm - all MOs who are referenced through the attribute **physpathermId** of the MOs matching **atmport** will be put in the group _test_ (since physpathermId is an attribute of type MoRef)
- lma test subrack=ms,slot=10,program loadmodule - all loadmodule MOs connected to program MOs running on slot 10 in main subrack will be put in the group _test_ (since **loadmodule** is an attribute of type MoRef)
- ma test atmport physpatherm slot=23 - all atmports whose physpatherm reference matches **slot=23** will be put in the group _test_
- ma test reliableprogram admactiveslot slot=10 - all reliableprograms that are on slot 10 will be put in the group _test_
- ma test vcltp pmrec 0 - all vcltps with 0 pmreceivedcells are put in the group
- ma test 34,58,42 - include MO instances with proxy id 34, 42, and 58 in the group
- mai test sectorcarrier= noOfUsedTxAntennas ^1$ - include all sectorcarriers that have exactly one antenna

Two-step example: To put all unlocked-disabled MOs in a group in order to lock them:

ma test all operational 0 ma test1 test administ 1 bl test1

To put all cells belonging to module 3 in a group in order to lock them

ma iubmod3 iublink module =3$ ma cellmod3 iubmod3 reservedby bl cellmod3

To put all vcltps that have 0 receivedcells and more than 0 transmitted cells in a group in order to find out which upper layers are affected

ma faultyvcltp vcltp pmrec ^0 mr faultyvcltp vcltp pmtrans ^\[^0\] lk faultyvcltp

Note: it is also possible to create MO groups with the commands hget/lhget, st/lst, lk/llk, and pdiff/lpdiff.

**4.1.11 mr\[i\]/lmr\[i\] &lt;moGroup&gt; &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute-filter&gt;\] \[&lt;value-filter&gt;\]**

Remove an MO group or remove MOs from an MO group (MOs will NOT be deleted, only the group).

Exactly the same syntax as ma described in Section 4.1.10 except that the MOs matching will be removed from the MO-Group instead of added.

**4.1.12 mp**

Print all defined MO groups. See ma command in Section 4.1.10 for more info about MO groups.

Note: To print the contents of a group, use the pr &lt;mo-group&gt; command.

**4.1.13 get\[d\]\[m\]\[i\]/lget\[d\]\[m\]\[i\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\]**

Read CM/FM attribute(s) from MO(s).

**Options:**

- d: to show the whole LDN instead of the shortened LDN, when using a 2nd or 3rd argument
- m: for reading the attributes via MibManager instead of Corba. Only applicable on CPP nodes with C15.1 or higher.
- i: to print internalmom attributes. Only applicable to MSRBS (DUS Gen2). Please make sure to activate the feature "Hidden Parameter Access" (CXC4012188/FAJ1214785) on the node for faster printout.

Note: to read PM attributes, use pget/lpget (see Section 4.4.3).

**Examples:**

1.  Get all attributes from all MOs except those whose RDN matches _utranrel_ or _iub_
    - get !(utranrel|iub)
2.  Get all attributes from MOs whose proxies range from 10 to 30
    - get 10-30
3.  From all MOs, get productdata containing the string 0843 (can be useful to find out which MO’s are related to a certain loadmodule)
    - get all product 0843
4.  From all Utrancells, get sintersearch attribute different from 10
    - get utrancel sinter !10
5.  Get traffic descriptors for all VclTp(s)
    - get vc trafficdes
6.  Get VcpTp(s) used by all cross-connections
    - get cross vc
7.  Get piutype for all MO’s under "Equipment"
    - lget equip piutype
8.  get attenuation values for all cables (in RBS)
    - get cable atten
9.  get all attributes in nodesynch MO, belonging to site 1164 (in RNC)
    - lget 1164,nodesy
10. get all attributes in MO’s under "RadioNetwork" matching pwr or power or sir
    - lget radion p.\*w.\*r|sir
11. view which cells are connected to which iub’s (in RNC)
    - get cell iub
12. get all attributes from nodebfunction MO, except those matching "overload"
    - get nodebfunc !overload
13. get the attribute loadCtrlPrioOfMta via the internalmomread/testmomdump command
    - geti . loadCtrlPrioOfMta

Important information:

1.  when doing a get &lt;mo(s)&gt; or get &lt;mo(s)&gt; all, one CORBA request is sent for each MO, asking for all attributes of that MO.
2.  when doing a get &lt;mo(s)&gt; &lt;attribute(s)&gt;, a CORBA request is sent for up to 100 MOs at a time, asking for the specified attributes of those MOs.

The implications of this is that it is faster but:

1.  if one or more attributes cannot be read due to some exception (eg: fRO not accessible), then all attributes will return the same exception, even if they can be read.
2.  if one or more MOs contain one or more attributes that cannot be read, then all MOs within that CORBA request will return the same exception even if they can be read.

The workaround for the first problem is to find out which attribute is causing the problem. The command sget/lsget can be used for this. The sget command reads each attribute one by one. The attribute(s) that is/are causing the exception(s) will then be easy to spot.

It is then possible to use the standard "get" command with with the negative filter (!) to exclude the "faulty" attribute.

- get nodebfunction !overload - all attributes of the nodebfunction MO except those matching "overload" will be read.
- pget utrancell !pmnoofrrc - all pm attributes of the utrancell MO except those matching "pmnoofrrc" will be read.

The workaround for the second problem is to lower the speed of reading so that only one MO instead of 100 is read per CORBA request.

This is done using the speed command.

Example: st all - one MO is returning an exception which means that up to 100 MOs cannot be read. Instead do:

speed 1 st all speed 100

The command will be slower but the exception will only affect the MO(s) that have it and not the "healthy" ones.

The speed command affects get,pget,kget,prod, and st commands.

By default, speed is set to 100, which means that up to 100 MOs share the same CORBA request.

By running the command speed 1, the exception will not affect the other MOs. However the speed will be slower. It is possible to use a value from 1 to 200 to define the speed. It is recommended to not use a speed higher than 100 since this takes more memory from the node.

Type speed on its own to see the current speed.

**Scripting and variable assignment with get**

It is possible to store the output into a variable

Example:

1.  Store one value into a variable
    - get utrancell pich > $pich
2.  Store many values into an array
    - for $mo in utrancellgroup $mordn = rdn($mo) get $mo pich > $pichTable\[$mordn\] done

Refer to the Section 6 (Scripting Chapter) for more information.

**4.1.14 hget\[c\]\[d\]\[m\]\[i\]/lhget\[c\]\[d\]\[m\]\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; \[&lt;attribute-filter&gt;\] \[&lt;value1-filter&gt;\] \[&lt;value2-filter&gt;\] \[&lt;value3-filter&gt;\] etc...**

Read CM/FM attribute(s) from MO(s), print horizontally one line per MO (instead of one line per attribute).

**Options:**

- c: display the output in CSV format for easier export to excel (for instance).
- d: to show the whole LDN instead of the shortened LDN
- m: print all MOs in a single table instead of separate tables per MO class
- i: to print internalmom attributes, similar as "geti" but horizontally. Only applicable to MSRBS (DUS Gen2). Please make sure to activate the feature "Hidden Parameter Access" (CXC4012188/FAJ1214785) on the node for faster printout.

Example:

- hget reliableprogramuniter slot|operational print the RPU attributes admActiveSlot, admPassiveSlot and operationalMode
- hget reliableprogramuniter slot|operational slot=10 . ^2 print all RPUs that are defined on slot10 (active), any slot for passive, and 2 for the operationalmode
- hget reliableprogramuniter slot|operational !slot=10 . !^1 print all RPUs that are not defined on slot10 (active), any slot for passive, and operationalmode is not equal to 1
- hget loadmodule type|productdata print the attributes loaderType and productData on all LoadModule MOs. Note that productData is a struct containing 5 members so the productData attribute will take up 5 columns
- hget loadmodule type|productdata@name only print the attribute loaderType and the structmember productData:productName passive, and operationalmode is not equal to 1
- hgetm port state print all attributes matching the word "state" on all MOs matching the word "port" and display all lines in one single table instead of a separate table per MO class.

For "slow" hget, use "shget/lshget": reads only one attribute at a time.

**4.1.15 kget\[m\]/lkget\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;\] \[&lt;attribute-filter&gt;\] \[&lt;attribute-type&gt;\] \[&lt;attribute-flag&gt;\] \[&lt;attribute-description&gt;\]**

Display CM/FM attributes in exportable printout format.

Same as get/lget, but with a different output format to allow import of the dump into external tools like MCOM, CCT, ETRAN.

The m option is for reading the attributes via MibManager instead of Corba. Only applicable on CPP nodes with C15.1 or higher. To collect a MO dump via MibManager, set the uservariable mibmgr_threshold with uv command. Refer to info in the file moshell/moshell.

For "slow" kget, use "skget/lskget": reads one attribute at a time.

The 2nd to 5th arguments have the same meaning as the arguments used in the "mom" command.

**Examples:**

- kget : print all MO attributes
- kget !relation= : print all attributes except from MOs with RDN matching "relation="
- kget . . moref : print all attributes of data type matching "moref"
- kget . . . ericsson : print all attributes with flag matching "ericsson"
- kget . . . . dbm : print all attributes with description matching "dbm"

**4.1.16 zget/lzget \[-n &lt;number&gt;\] \[-t &lt;timeout&gt;\] \[-i &lt;interval&gt;\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute-filter&gt; &lt;value-filter&gt;**

Read attribute(s) until the value matches the value-filter.

The command keeps running a "get" operation on the specified MOs/attributes until 1 or all attribute values match the value filter.

Options:

- \-t: to specify a timeout (in seconds) after when to stop the loop if the attributes(s) have not reached the value filter
- \-i: the interval (in seconds) between each get operation. Default: 5 seconds.
- \-n: the minimum number of MOs that should have reached the wanted value for the loop to stop. Default: all MOs.

The result is stored in the variable $returncode:

- 0: success (the attributes have reached the expected value)
- 1: failed (e.g. no MOs found or Timeout reached)

Examples:

- zget -t 30 ,eutrancellfdd= operationalstate 1 - keep reading the operationalstate of all EUtranCellFDD MOs until all have reached value 1 (enabled), give up after 30 seconds.
- zget -n 1 ,eutrancellfdd= operationalstate 0 - keep reading the operationalstate of all EUtranCellFDD MOs, stop when at least one Cell has reached value 0 (disabled)

**4.1.17 fro/lfro\[m\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\]**

Read MO persistent data from node database via SQL.

The fro/lfro command reads only the froId connecting the MAO and FRO parts of the MO.

The from/lfrom command reads all MAO/FRO data of the MO.

The command syntax and printout format is identical to that of the get/lget command.

**Examples:**

- from upgradepackage=cxp9012014_r5a - print MAO/FRO persistent data for MO UpgradePackage=CXP9012014_R5A
- from 0 - print MAO/FRO persistent data for the ManagedElement MO
- fro plugin - print froId for all pluginunit MOs
- fro plugin . 5 - print the PlugInUnit MOs who have a froid matching the value 5
- fro plugin . ^5$ - print the PlugInUnit MOs who have a froid equal to 5
- lfro ms,slot=10,plugin sairesource > $sai - save the sairesourceid of a particular pluginunit into a variable $sai

Note: If the SQL client LM (CXC1325608) is not started, the fro\[m\] command starts it automatically using the "sql+" command. After the session, the SQL client should be turned off using the "sql-" command. Type "h sql+" for more info.

**4.1.18 sql/select &lt;command&gt; \[ | &lt;unix-cmds&gt;\]**

To run a SQL command while in db.dat mode. The db.dat, cv.zip, or dbdump.zip is loaded with moshell option "-d".

**Examples:**

- select \* from tables | grep pgm
- select \* from tables where name like ’%iur%’
- select \* from cspgmresource_01 where pno=’CXC 132 0784’

**4.1.19 st/lst &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;state-filter&gt;\]**

Print state of MOs (operationalState and administrativeState when applicable).

It is similar to writing get/lget &lt;mo&gt; state, the only difference is that it presents the two states side-by-side in a more visible way.

The state filter matches towards both the Operational state and the Administrative state.

**Examples:**

- st - view state of all MOs
- st all dis - view all disabled MOs
- lst equip dis - view all disabled MOs under "Equipment" • st all 1.\*0 view all MOs which are unlocked and disabled
- st all ^0 - view all MOs which are locked:
- lst sector - view state of all MOs under "Sector" (in RBS)
- lst cell - view state of all channels in all 3 cells in the RBS
- lst cell=120 - view state of all channels in cells starting with 120 (in RNC)

**4.1.20 prod &lt;moGroup&gt;|&lt;moFilter&gt; \[&lt;productdata-filter&gt;\]**

Print the attribute productData on applicable MO(s).

It is similar to typing "hget &lt;mo&gt; productdata". This command prints _product data_ of all MO(s). It is similar to typing get all productdata, except that the _productData_ appears in one row. It is possible to filter only MOs matching a certain product identity. **Examples:**

- prod loadmodule cxc1320784 - print all MOs matching "loadmodule" and where the value of productData attribute matches "cxc1320784"

MO classes that have a productdata attribute can be found via mom command: mom all all struct:.\*productdata

Typically, this includes _Slot, Subrack, PiuType_ and _LoadModule_.

**4.1.21 lk/llk &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

View all MO(s) linked to an MO, and their states (_adminstrativeState_ and _operationalState_).

**Examples:**

- lk mtp3bsrs= - View all core network interface stacks
- lk ranap=cs - View all MO’s linked to Ranap=cs
- lk iublink=iub-12 - View all MO’s linked to iub 12
- lk atmport=ms-24-1 - View all MO’s linked to atmport MS-24-1 (and its VclTp’s)
- lk eutrancellfdd=1a - View all MO’s linked to EUtranCellFDD=1A

**4.1.22 lko/llko &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

The old lk. Obsolete command, use lk/llk instead.

Output format of e.g. lko ranap=cs:

\===================================================================================

MOs linked to 1316 RncFunction=1,Ranap=cs (-,E)

\===================================================================================

|     |     |     |
| --- | --- | --- |
| localSccpApRef Ranap=cs |     | \---> (-,E) SccpSp=1,SccpScrc=1,SccpAp=1 |
| sccpGlobalTitleRef Ranap=cs |     | \---> (-,-) SccpSp=1,SccpScrc=1,SccpGlobalTitle=1 |
| remoteSccpApRef | Ranap=cs | \---> (-,E) SccpSp=1,SccpScrc=1,SccpAp=2 |
| reservedBy | SccpSp=1,SccpScrc=1,SccpAp=1 | \---> (-,-) SccpSp=1,SccpScrc=1,SccpEntitySet=1 |
| mtp3bApId | SccpSp=1,SccpScrc=1,SccpAp=2 | \---> (-,E) Mtp3bSp=1,Mtp3bAp=1 |
| reservedBy | SccpSp=1,SccpScrc=1,SccpAp=2 | \---> (-,-) SccpSp=1,SccpScrc=1,SccpEntitySet=2 |
| routeSetId | Mtp3bSp=1,Mtp3bAp=1 | \---> (-,E) Mtp3bSp=1,Mtp3bSrs=1 |
| reservedBy | SccpSp=1,SccpScrc=1,SccpEntitySet=2 | \---> (-,-) SccpSp=1,SccpScrc=1,SccpGlobalTitle=2 |
| slsReservedBy | Mtp3bSp=1,Mtp3bSrs=1 | \---> (-,E) Mtp3bSp=1,Mtp3bSls=1 |
| reservedBy | Mtp3bSp=1,Mtp3bSls=1 | \---> (-,E) Mtp3bSp=1,Mtp3bSrs=1,Mtp3bSr=1 |
| nniSaalTpId | Mtp3bSp=1,Mtp3bSls=1,Mtp3bSl=2 | \---> (-,E) NniSaalTp=csb |
| nniSaalProfileId | NniSaalTp=csb | \---> (-,-) NniSaalProfile=1 |
| aal5TpVccTpId | NniSaalTp=csb | \---> (-,E) Aal5TpVccTp=csb |
| processorId | Aal5TpVccTp=csb | \---> (U,E) Subrack=MS,Slot=9,PlugInUnit=1 |
| vclTpId | Aal5TpVccTp=csb | \---> (-,E) AtmPort=MS-7-1,VplTp=vp12,VpcTp=1,VclTp=vc34 |

atmTrafficDescriptrId AtmPort=MS-7-1,VplTp=vp12,VpcTp=1,VclTp=vc34---> (-,-) AtmTrafficDescriptor=U3P4500M3000

|     |     |     |
| --- | --- | --- |
| nniSaalTpId | Mtp3bSp=1,Mtp3bSls=1,Mtp3bSl=1 | \---> (-,E) NniSaalTp=csa |
| nniSaalProfileId | NniSaalTp=csa | \---> (-,-) NniSaalProfile=1 |
| aal5TpVccTpId | NniSaalTp=csa | \---> (-,E) Aal5TpVccTp=csa |
| processorId | Aal5TpVccTp=csa | \---> (U,E) Subrack=MS,Slot=8,PlugInUnit=1 |
| vclTpId | Aal5TpVccTp=csa | \---> (-,E) AtmPort=MS-6-1,VplTp=vp11,VpcTp=1,VclTp=vc34 |

atmTrafficDescriptrId AtmPort=MS-6-1,VplTp=vp11,VpcTp=1,VclTp=vc34---> (-,-) AtmTrafficDescriptor=U3P4500M3000

\===================================================================================

In the middle column is the originating MO. In the far right column is the referenced MO. In the left column is the attribute containing the referenced MO. The letters in brackets show the _administrativeState_ and _operationalState_ of the referenced MO:

- **U** \= Unlocked
- **L** \= Locked
- **E** \= Enabled
- **D** \= Disabled
- **\-** \= Not Applicable

**4.1.23 set\[m\]\[c\]\[1\]\[i\]\[p\]\[1x\]/lset\[m\]\[c\]\[1\]\[i\]\[p\]\[1x\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute&gt; \[&lt;value&gt;\]**

Set an attribute value on one or several MO’s.

Only attributes that do not have the flag readOnly or restricted can be set. Use the mom command to check the flags of an attribute. For restricted attributes, it is possible to use the rset command.

**Options:**

- m : for setting several attributes simultaneously in the same MO, using a single transaction for all attributes in each MO. Needed for changing certain attributes in the RNC UtranCell (locationAreaRef, uarfcnDl, uarfcnUl).
- 1 : for setting one attribute on many MOs simultaneously, using a single transaction for all the MOs. Needed for changing certain attributes in the eNB EUtranCell (tac, frameStartOffset, subframeAssignment, specialSubframePattern).
- 1x : for setting several attributes on several MOs in a single transaction. Several set1x commands will be executed in order to change the attributes, then the commit command shall be issued. This is useful for setting attributes that have a dependency to other attributes. Note: set1x is currently only supported for COM and YANG nodes.
- c : for setting an attribute to its current value. When using this option, the attribute value shall not be specified since the existing attribute value is used.
- i : to set an attribute via "internalmomwrite" command. Only applicable to RCS nodes (MSRBS).
- p : to set the attribute value from a prompt instead of typing it on the command line. If the attribute is a password then the input will not be echoed on screen.

Note: These options cannot be combined.

**Examples:**

- set cell primarycpichpower 250 - set primarycpichpower to 250 on all cells (in RNC)
- lset uerc= sirmin 60 - set sirmin to 60 on all MO’s under uerc (in RNC)
- lset ms,slot=1,pluginunit=1$ userlabel - set an empty value for the userLabel of this PluginUnit
- set mtp3bspitu sppriority prioslt=2 - set an attribute of type struct
- setc iublink= preferredsubrackref - set the preferredsubrackref attribute to its current value on all Iublinks, in order to evenly spread the sites across all modules.
- \- setting three attributes simultaneously on a MO (split on several lines for readability)

setm utrancell=3012 locationarearef locationarea=9 servicearearef locationarea=9,servicearea=1 routingarearef locationarea=9,routingarea=1

- set1 ^eutrancellfdd= tac 1280 - set the tac attribute simultaneously on all EUtranCellFDD in the eNB.
- seti . loadCtrlPrioOfMta false - set the attribute loadCtrlPrioOfMta via internalmomwrite command
- set the following attributes in one transaction:

\>> set1x NRCellDU=1 subcarrierSpacing 15

\>> set1x NRCellDU=1 ssbSubcarrierSpacing 15

\>> set1x NRSectorCarrier=1 arfcnDL 460000

\>> set1x NRSectorCarrier=1 arfcnUL 420000

\>> commit

Please see Section 3 and specifically Section 3.4 for more information on how to set values for each specific attribute type (e.g. **Struct**, **array of MoRef**, **array of Struct**, etc).

**4.1.24 eset\[c\]\[1\]/leset\[c\]\[1\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute-filter&gt; \[&lt;value&gt;\]**

Set one or several attributes on one or several MO’s, using regexp matching on the attribute name.

Same as set command except that the second argument uses regular expression matching on the attribute name so all attributes whose name match the filter will be affected by the operation. Refer to the help of the set command for more information about syntax and command options c and 1.

**Examples:**

- Activate all features in the RBS/ERBS. The attribute is called featureStatexxxx , where xxx is the name of the feature. All MOs that have an attribute matching the word "featurestate" will have that attribute set to 1

\>> eset . featurestate 1

- Change the ENodeBFunction::eNodeBPlmnId on ERBS. The EUtranCellFDD::bPlmnList must be changed at the same time in one transaction.

\>> eset1 ^enodebf|^eutrancellfdd plmn mcc=240,mnc=99,mnclength=2

**4.1.25 rset/lrset &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;attribute&gt; \[&lt;value&gt;\]**

Set attribute value on a restricted attribute or change the MOid of an MO.

A _restricted attribute_ is an attribute that can only be set when the MO is created.

The rset command works by doing rdel/lrdel on the MO and recreating all previously deleted MOs using the new attribute value.

Therefore the rset command only works on MO classes that are supported by the rdel command. Type h rdel to find out the list of supported MO classes.

To change the MOid of an MO, the attribute name should be made up of the MOclass followed by "id", eg: atmportid, pluginunitid, etc.

Example 1, change a restricted attribute:

rset unisaaltp=.\*1004 unisaalprofileid unisaalprofile=win30a Example 2, change the MOid:

rset utrancell=cell123 utrancellid cell456

**4.1.26 bl\[s\]\[1\]/lbl\[s\]\[1\] \[-t &lt;timeout&gt;\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Locks one or more MOs by setting its administrativeState to 0 (hard-lock) or 2 (soft-lock). To unlock MOs, use the command "deb/ldeb" which sets the administrativeState to 1.

**Options:**

- s : soft-lock. The administrativestate is set to 2 ("shutting down") which means that the resource will have a grace period to handover traffic to other resources, before it gets locked. The administrativestate will automatically go over to 0 after the grace period, which can be between a few seconds to a couple of minutes, depending on the MO type. Without the s option, the resource is locked immediately.
- 1 : for locking several MOs simultaneously, using a single transaction for all the MOs.

Switches:

- \-t &lt;timeout&gt; : (in seconds) only applicable to the bls command (soft-lock). If the MOs have still not reached locked state after the timeout then the bls command will automatically hard-lock the MOs.

**Examples:**

- bl aal2.\*ca\[246\] - lock aal2paths ca2, ca4, ca6
- lbl subrack=ms,slot=19 - lock all MO(s) under subrack=ms,slot=19
- bl 234 256 248 - lock proxys 234, 256, and 248
- bl 001500 - lock a board. Same as lbl subrack=ms,slot=15,pluginunit=1$.
- bls 001500 - soft-lock a board.
- bl1 cell - lock all the cells in one transaction
- bls -t 30 ,eutrancellfdd= - soft-lock all LTE cells with 30 second timeout until hard-lock

Note: there is also an OSE command called bl. If the OSE command needs to be run instead of the moshell command, just type a "\\" (backslash) in front. E.g.: \\bl

**4.1.27 deb\[1\]/ldeb\[1\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Unlocks one or more MOs by setting its administrativeState to 1.

To lock an MO, use the command bl/lbl.

**Options:**

- 1 : for unlocking several MOs simultaneously, using a single transaction for all the MOs.

**Examples:**

- ldeb subrack=ms,slot=19 - deblock all MO(s) under subrack=ms,slot=19
- deb 001900 - deblock a board. Same as ldeb subrack=ms,slot=19,pluginunit=1$)

**4.1.28 acl/lacl &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;action-filter&gt;\]**

Lists available MO actions.

**Examples:**

1.  acl all restart - View all restart actions
2.  acl all \[^(restart)(eteloopback)\] - View all actions except _restart_ and _eteloopback_
3.  acl sync - View all actions related to the synchronisation MO. Output:

\------------------------------------------------------------------------------

Proxy MO Action Nr of Params

\------------------------------------------------------------------------------

396 Synchronization=1 changeSyncRefPriority 2

|     |     |     |     |
| --- | --- | --- | --- |
| 396 | Synchronization=1 | removeSyncRefResource | 1   |
| 396 | Synchronization=1 | resetLossOfTracking | 1   |
| 396 | Synchronization=1 | addSyncRefResource | 2   |

1.  acl all listrou - Find the MO with action matching regular expression _listrou_:

\-------------------------------------------------------------------------------------------------

Proxy MO Action Nr of Params

\-------------------------------------------------------------------------------------------------

471 Ip=1,IpRoutingTable=1 listRoutes 0

**4.1.29 acc\[e\]\[n\]\[y\]/lacc\[e\]\[n\]\[y\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all &lt;action&gt;**

Execute an MO action.

If the action requires parameters, these will be prompted for.

If no value is entered at a prompt, the action is aborted, unless option "y" was used (accy).

In order to be avoid being prompted for the parameters, use option "n" (accn/laccn), then the parameters can be given on the same line as the command.

**Options:**

- n : action parameters will not be prompted for and shall be input on the command line. Eg: accn 0 manualrestart 0 0 0
- e : for action parameters of type struct, there will be a separate prompt for each individual struct member. • y : allows to type an empty value at a parameter prompt, then the parameter is not included in the action

**Examples:**

1.  Restart a board:
    - - - acc 001400 restart - Same as:

lacc subrack=ms,slot=14,pluginunit=1$ restart

- - - - acc 001900/sp0.lnh restart - Same as:

lacc subrack=ms,slot=19,.\*,spm=1$ restart

1.  Restart the node:

• acc 0 manualrestart

1.  List the IP routing table:

• acc ip listroutes

1.  Perform End-To-End loopback on VclTp MOs:

• lacc atmport=ms-24-1 eteloopback

1.  Perform PhaseMeasurement on NodeSynchTp MOs:

• acc nodes performPhaseMeasurement

1.  Add a new synchronization reference:
    - acc sync addSyncRefResource

Note 1: To specify an attribute of type _Struct_, use the following syntax:

- - attr1=val1,attr2=val2,attr3=val3...

This is the same syntax as used in set and cr commands, and is not case sensitive. Example (in the case of routingTableEntry in action **deleteStaticRoute**) (note: line split for readability):

destinationIpAddr=10.1.10.0,destinationNetworkMask=255.255.255.0, nextHopIpAddr=10.128.15.1,routeMetric=3

Alternatively, the option e can be used, in which case each struct member is prompted on a separate line (command: acce/lacce).

Note2: Action manualRestart on ManagedElement MO

- - This action can be restricted with the uservariable restart_confirmation. See description in the file moshell/moshell.
    - Node restarts usually result in decrementing of the attribute ConfigurationVersion::rollbackCounter which leads to node rollback upon reaching zero. However the action manualRestart on ManagedElement is a special case which does not lead to decrement of the rollbackCounter, when executed from moshell/AMOS.

**4.1.30 cr\[e\]\[n\]\[1x\] &lt;ldn&gt;**

Create an MO.

When run without option, the command will prompt the user to enter the values for all mandatory and restricted attributes. The order in which the attributes are prompted is the same order in which they are listed inside the XML MOM file. Restricted attributes are optional, type d to select default value. To abort, type &lt;enter&gt; at the prompt.

**Options:**

- e : to receive a separate prompt for each individual struct member, useful when inputting attribute values of type struct
- n : allow the user to enter any attribute name and value. Each attribute name and value shall be entered on a separate line with space between the attribute name and value. Any attribute can be specified, does not have to be a mandatory or restricted attribute. Type "end" once all attributes have been entered.
- 1x : for creating several MOs in a single transaction. Several cr1x/crn1x commands will be executed in order to create the MOs, then the commit command shall be issued. This is useful for creating MOs that have a dependency to other MOs, e.g. when a MO can only be created if it has at least one child MO. Note: the "1x" option is currently only supported for COM and YANG nodes.

**Examples:**

cr swmanagement=1,upgradepackage=FAB102572%2_R14D.xml cr rncfunction=1,iublink=2456 cre swmanagement=1,loadmodule=CXC123456_R9A crn rncfunction=1,iublink=90

cr1x GNBDUFunction=1,DU5qiTable=1 ; cr1x GNBDUFunction=1,DU5qiTable=1,DU5qi=1 ; commit

Notes:

To specify an empty attribute value, type null or d.

To specify an attribute of type _Struct_, use the following syntax: attr1=val1,attr2=val2,attr3=val3...

This is the same syntax as used in set command, and is not case sensitive. Example, in the case of productdata in loadmodule

(note: line split for readability!):

productnumber=CXC1322155/2,productrevision=R3C08,productname=test, productinfo=test,productiondate=20010229

Alternatively, the option e can be used, in that case, each struct member is prompted on a separate line (command: cre).

An moshell script for MO creation can be automatically generated by using the simulated undo mode: u+s , del &lt;mo&gt; , u- , then edit the undocommandfile with the required values. By default the undo script will contain crn commands. To use cr commands instead of crn, do uv use_crn=0.

By default, the mandatory/restricted attributes that are marked as deprecated are not prompted by the cr command. This behaviour can be changed by setting the uservariable exclude_deprecated to 0.

As in the ld command, the LDN doesn’t need to contain ManagedElement=1.

If the wrong case is used in the MO class (e.g. eutrancellfdd instead of EUtranCellFDD) then moshell will automatically correct this.

**4.1.31 del\[b\]\[1x\]/ldel\[b\]\[1x\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Delete MO(s).

An MO can only be deleted when its reservedBy list is empty and when it does not have any children. If the MO does have children and/or a non-empty reservedBy attribute, it is possible to use the rdel/lrdel command instead.

The command first prints the MO(s) to be deleted, then asks for confirmation. Once the MO(s) are deleted, they are also removed from the proxy list.

To delete all MOs that have just been created by a script, just check the range of proxies that were created and delete them in the reverse order. This can be done easily by using the reverse proxy order.

Example: proxies 22 to 46 were created by a _CREATE_ script (in run or trun). To undo it:

del 46-22

To delete an MO and all its children, just use the % sign in front of the ldn/rdn filter. Example: ldel %ms,slot=20,plug will delete the programs first then the piu

To delete an MO group in the reverse order of the proxies, put the % sign in front of the MO group name. Example:

del %mymogroup - will delete all MOs of the MO group "mymogroup" in the reverse order of their proxies

Note:

The following MOs can only be deleted while in state LOCKED: PlugInUnit, EUtranCell, TermPointToENB, GpsReceiver, IpAccessHostEt, IpAccessHostGpb, IpAccessHostSpb, IpSyncRef .

By default, the "del" command will automatically perform the locking prior to deleting, unless the "b" option has been used (delb).

Note: the 1x option can be used for deleting several MOs in a single transaction. Several del1x commands will be executed in order to delete the MOs, then the commit command shall be issued. The "1x" option is currently only supported for COM and YANG nodes and is also available for the "cr" and "set" commands.

**4.1.32 rdel/lrdel &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Delete MO(s) together with children and reserving MOs.

For MO classes shown in the list below, the command finds out all the related MOs, then presents the list of MOs to be deleted and asks the user for confirmation. For all other MO classes, the command acts in the same way as a regular "del" operation, ie, just tries to delete the MO itself.

List of MO classes for which rdel acts recursively:

- Aal0TpVcctp
- Aal1TpVcctp
- Aal2Ap
- Aal2PathDistributionUnit
- Aal2PathVcctp
- Aal2RoutingCase
- Aal5TpVccTp
- AntennaNearUnit
- AtmCrossConnection
- AtmPort
- Cdma2000Cell
- Ds0Bundle
- EUtranCellFDD
- EUtranCellTDD
- EutranFrequency
- ExternalCdma2000Cell
- ExternalCdma20001xRttCell
- ExternalENodeBFunction
- ExternalEUtranCellFDD
- ExternalEUtranCellTDD
- ExternalGeranCell
- ExternalGsmCell
- ExternalUtranCell
- ExternalUtranCellFDD
- ExternalUtranCellTDD
- ImaGroup
- IpEthPacketDataRouter
- IuLink

Iub

- IubLink
- IurLink
- M3uAssociation
- Mtp2TpItu/Ansi/Ttc/China
- Mtp3bSlItu/Ansi/Ttc/China
- Mtp3bSls
- Mtp3bSrs
- NbapCommon
- NbapDedicated
- NniSaalTp
- NodeBLocalCell
- NodeBSectorCarrier
- NRCellDU
- NRSectorCarrier
- NodeSynchTp
- PacketDataRouter
- Ranap
- Rnsap
- SectorCarrier
- SectorEquipmentFunction
- UniSaalTp
- UtranCell
- VclTp
- Vmgw
- VpcTp
- VplTp

**4.1.33 gm\[c\]\[d\]/lgm\[c\]\[d\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Generate MO Creation/Deletion script.

**Options:**

- c : Generate MO Creation script.
- d : Generate MO Deletion script.

The output of the command is a command file containing the creation/deletion commands.

By default the create statements will use the crn command but it is possible to use the cr command by setting uv use_crn=0 It is possible to convert the command file to trun format with the u! command.

**Examples:**

- lgmc equipment=1 : Generate a MO script to create all the MOs under Equipment=1 . Parent and referenced MOs will be created before children and reserving MOs.
- gmd subrack=1,slot=2,pluginunit=1 : Generate a MO script to delete the MO Subrack=1,Slot=2,PlugInUnit=1 .

Children and reserving MOs will be deleted before parent and reserved MOs.

**4.1.34 sc\[g\]\[w\]\[d\] \[&lt;parameterlist&gt;|all\] \[&lt;namespacelist&gt;|all\]**

Read/Write/Reset SystemConstants on RBS/ERBS/MSRBS.

**Options:**

- g ("get") : read system constants
- w ("write") : set system constants
- d ("default"): reset system constants

On RBS/ERBS the MO operations on SystemConstants are used while on MSRBS, the COLI commands sysconXXXX are used. Note: on MSRBS, the command used for setting the system constants can be controlled via the uservariable sysconwrite

Syntax:

- scg \[&lt;const&gt;\] \[&lt;namespace&gt;\] \[ > $var\] : read one or all constants
- scw const1:val1,const2:val2,... \[&lt;namespacelist&gt;|all\] : write one or more constants
- scd const1,const2,... \[&lt;namespacelist&gt;|all\] : reset one or more constants to default
- scd all \[&lt;namespacelist&gt;|all\] : reset all constants to default

Note: the namespace argument is only applicable for MSRBS >= 20.Q1 and only for the RP/RC SC’s listed in the printout of "bbrs sysconst".

Attempting to set a SC on namespace level which is not part of the bbrs list will be rejected (this check can be disabled via the uv use_sc_namespacecheck).

Syntax examples:

- scg : read all system constants
- scg 915 : read the value of system constant "915"
- scg 915 > $var : read the value of system constant "915" and store to a variable
- scg RP28 NR-FR1-C1 > $var : read the value of system constant RP28 in namespace NR-FR1-C1 and store to a variable
- scd 915 : reset system constant 915 in the default namespace
- scd 915,2102,2085 : reset system constant 915, 2102, 2085 in the default namespace
- scd RP28,PP32 default,NR-FR1-C1 : reset system constants RP28 and PP32 in the default and NR-FR1-C1 namespaces
- scd RP28,PP32 all : reset system constants RP28 and PP32 in all namespaces
- scd all : reset all system constants in the default namespace
- scd all all : reset all system constants in all namespaces
- scw 915:14 : set system constant 915 to value 14 in the default namespace
- scw 915:14,2102:1,2085:1 : set system constants 915 to 14, 2102 to 1, 2085 to 1 in the default namespace
- scw RP28:1,PP32:0 default,NR-FR1-C1 : set system constants RP28 to 1 and PP32 to 0 in the default and NR-FR1-C1 namespaces

**4.1.35 safe+/safe-/safe?**

Purpose: Apply strict MO matching rules on MO WRITE commands

- safe+ : apply safe MO syntax, no proxy id or no regular expression matching for MO WRITE commands, exact MO name(s) must be given (case insensitive is allowed)
- safe- : allow proxy id and regular expression matching (this is the default setting)
- safe? : check the current setting

List of MO WRITE commands: bl, bls, deb, del, rdel, fdel, set, eset, rset, fset, acc, facc

**Examples:**

- bl utrancell=11 - will lock cell=11 only (cell=111, or cell=11a , etc. would not be affected)
- bl utrancell=11|utrancell=12|utrancell=13 - will lock cell=11, cell=12, cell=13
- bl utrancell=11|12|13 - same as above
- bl utrancell=11|12|13|iublink=1 - will lock cell=11/12/13 and iublink=1
- bl pluginunit=1 - nothing will happen as there are several MO instances with this name

bl subrack=ms,slot=28,pluginunit=1 - will lock this MO as the name given is unique

The setting is off by default but can be saved to "on" by adding the line safe_syntax=1 in the file moshell/jarxml/moshellrc or the file /.moshellrc

**4.1.36 s+/s++/s-/s?**

Purpose: Sort MO list in alphabetical order instead of proxy order.

- s+ : activate alphabetical sorting of the MO list by order of LDN (sort_proxy=1)
- s++ : activate alphabetical sorting of the MO list by order of MO class (sort_proxy=2)
- s- : go back to default behaviour where the MO list is sorted by proxy number (sort_proxy=0)
- s? : check if alphabetical sorting is active or not

Once the s+/s++ command has been entered, the alphabetical sorting takes effect on all subsequent MO commands such as, pr, get, set, st, etc.

Type s- to revert to the default behaviour of sorting by proxy number.

To change the default behaviour, it is possible to use the uservariable sort_proxy, eg, adding the line sort_proxy=1 in the file ~/.moshellrc Example:

Default behaviour: MOs are displayed in the order of the proxy numbering. The order of the proxy numbering depends on the order with which the MOs were created on the node.

RNC32> pr uerc=

\===================================================================================

Proxy MO

\===================================================================================

2587 RncFunction=1,UeRc=0

2591 RncFunction=1,UeRc=16

2604 RncFunction=1,UeRc=91

2620 RncFunction=1,UeRc=1

2628 RncFunction=1,UeRc=17

1.  RncFunction=1,UeRc=70
2.  RncFunction=1,UeRc=59

2670 RncFunction=1,UeRc=2

Activate MO list sorting and run some MO commands. MOs now appear in alphabetical order.

RNC32> s+

Proxy sorting: activated.

RNC32> pr uerc=

\===================================================================================

Proxy MO

\===================================================================================

2587 RncFunction=1,UeRc=0

2620 RncFunction=1,UeRc=1

2670 RncFunction=1,UeRc=2

2754 RncFunction=1,UeRc=3 4071 RncFunction=1,UeRc=4 ....&lt;cut&gt;....

RNC32> hget uerc= userlabel

\=======================================================================================================

MO userLabel

\=======================================================================================================

UeRc=0 Idle

UeRc=1 SRB (13.6/13.6)

UeRc=2 Conv. CS speech 12.2

UeRc=3 Conv. CS unkn (64/64)

UeRc=4 Interact. PS (RACH/FACH)

UeRc=5 Interact. PS (64/64)

UeRc=6 Interact. PS (64/128)

**4.1.37 u+\[s\]/u-/u?/u!/u!! \[&lt;file&gt;\]**

Handling of undo mode (for cr/del/rdel/set/bl/deb/acc commands). Can be used for generation of MO scripts as well.

- u+ : To start the _undo mode_
- u+s : To start the _simulated undo mode_
- u- : To stop the _undo mode_
- u? : To check if _undo mode_ is active or not
- u! : To convert a moshell ".mos" command files to netconf ".xml" format or trun ".mo" format (and vice-versa), or undo ".log" logfiles to ".mos" command files, see description further down for more info.
- u!! : To convert a moshell ".mos" command file to trun ".mo" format while placing transaction tags between each 300 MO operations. This makes the file run quicker. The value of 300 can be configured in the uv transaction_size but it is not recommended to raise it as high value could potentially cause issues in the node’s MO database.

While running in "undo mode", the MO data is saved in a special logfile for all MOs on which the following commands are run:

- cr
- del/ldel/rdel/lrdel
- bl/lbl/deb/ldeb
- set/lset
- acc/lacc

Upon stopping of undo mode, an undo file is generated to revert the MO configuration changes. It can also be used for deleting and recreating MOs when one needs to change a restricted attribute.

The undo file will contain the following commands:

- del commands to remove created MOs.
- cr commands to put back deleted MOs.
- bl/deb commands to change MOs back to their original administrative state.
- set commands to change MOs back to their original attribute values.
- acc commands to revert certain MO actions. This only works on actions that have an opposite, see note below.

When running the simulated undo mode (u+s), all MO operations (cr/del/rdel/bl/deb/set) are simulated. Two command files are generated, one for deletions and one for creation.

The files generated by undo mode and simulated undo mode are stored in the following variables:

- _$undologfile_
- _$undodelcommandfile_ (simulated undo mode only)
- _$undocommandfile_

Conversion functionality (**u!**): The **u!** command takes as input one of the files generated by the undo mode. Different output will be generated depending on the input file.

- if the input file is an undologfile (.log), the output will be an undodelcommandfile and an undocommandfile
- if the input file is an undodelcommandfile or an undocommandfile (.mos), the output will be:
    - in case of CPP node: an undotrunfile ($undotrunfile) which is a command file in trun/emas format (.mo)
    - in case of COM node: an undoxmlfile ($undoxmlfile) which is a command file in netconf format (.xml)
- if the input file is an undotrunfile (trun/emas format ".mo"), the output will be an undocommandfile (run format ".mos")

Note: to undo **create** commands run from a "trun" script, just run a delete on the proxy range in reverse order. See Section 4.1.31 or h del for more info.

Note: the undo mode currently cannot reverse a set command done on an attribute of type sequence of struct.

Note: the following actions are currently supported in the undo mode:

- addPath/removePath
- addDhcpServerAddress/removeDhcpServerAddress
- setAutoActivate/setAutoDown

activateRemoteSp/inactivateRemoteSp

- addRemoteSp/removeRemoteSp
- activate/deactivate
- localInhibit/localUninhibit
- activateLinkSet/deactivateLinkSet
- blockSignalingRoute/deBlockSignalingRoute
- addRepertoire/deleteRepertoire
- addSlot/deleteSlot
- addCicRange/removeCicRange
- addNri/removeNri
- addTdmTermGrpMos/removeTdmTermGrpMos
- addSyncrefResource/deleteSyncrefResource
- addAal2ApToRc/removeAal2ApFromRc
- writeSystConst/resetSystConst, deleteConst/writeConst
- changeFrequency, pnpChangeFrequency, setFrequencyBand
- removeIpAccessHostMos/addIpAccessHostMos
- manualMspSwitch, manualSwitch, switch

**4.1.38 run\[x\]\[1\]\[1p\]\[1r\] \[-l &lt;lineNr&gt;\] &lt;command file&gt; \[&lt;var1&gt;\] \[&lt;var2&gt;\] ...**

Run a command file in moshell format.

The command file layout is the same as for _monode_ and _mobatch_. See examples in **moshell/examples/mobatch_files**.

It shall contain all lines to be sent to the moshell prompt, including password (for ose commands), but NOT confirmations (**y**). This applies to commands such as lt/ltc, lc/lcc, del/ldel, bl/lbl, set/lset where confirmation is automatically entered when running a command file.

Comments can be put in the command file using the # sign. By typing **&lt;TAB&gt;**, the unix file system is displayed, making it easier to find the location of the command file.

If some arguments are given after the command file, the scripting variables $1, $2, $3, etc. will be set to the corresponding values. The variable $0 will be set to the whole line contents. Type "h scripting" for info.

**Options:**

- 1: to execute the file in one transaction and commit. Only applicable for COM or YANG nodes. To run a MO script in one transaction on CPP nodes, use trun1.
- 1p: to execute the file in one transaction and prompt for commit/rollback. Only applicable for COM or YANG nodes.
- 1r: to execute the file in one transaction and rollback. Only applicable for COM or YANG nodes.
- x: to stop execution of the file upon failure of a MO WRITE command (create, delete, set, action).

Note: if a create command fails due to the MO instance already exists the error is ignored unless the uservariable runx_ignore_moexist is set to 0 (default is 1).

The following scripting variables are set automatically when the script stops:

- - $errorline points to the line number where the script stopped
    - $errorcmdline points to the line number of the last command that failed
    - $nextcmdline points to the line number of the next command to execute **Switches:**
- \-l &lt;lineNumber&gt;: to start file execution at a specific line number.

**4.1.39 trun\[is1cr\] &lt;moScript&gt;|&lt;http://ipaddress/script&gt;**

Run a command file in EMAS/MoTester format.

Execute a command file in EMAS/MoTester format.

By typing **&lt;TAB&gt;**, the unix file system is displayed, making it easier to find the location of the command file.

It is also possible to specify a file located on a web server (eg. when the script is located on the CPP node).

The following commands are supported: ECHO, CREATE, SET, SETM, SETU, DELETE, ACTION, CHECK, CHECKM, CALL, CALLREL, WAIT.

Lines can be commented out by adding **//** at the beginning of each line.

See examples below. For more info, refer to MoTester documentation in moshell/examples/motester/runMoTester.html .

By default, the command file halts when a command fails.

**Options:**

- i : ignore exceptions, the execution does not halt when a command fails.
- s : simulated run, the command file execution is simulated, no commands are actually executed on the node. Can be used to verify the syntax of a script prior to running it for real. The simulated mode is always used in "offline mode" or "simulated undo mode", regardless of the "trun" options.
- 1 : executes the whole script in one transaction, then prompts for confirm or rollback. This option should be used with great care and only when absolutely necessary (e.g. when changing IP address of the node, see example script in moshell/examples/misc/ip_change.mo). In regular usage, it is recommended to not use this option as it has been observed to cause database corruptions in certain cases, for instance when creating/deleting certain types of MOs within the same transaction. Database inconsistencies can be checked with the command dbc.
- c : used in combination with option 1 above, will avoid the prompt by automatically confirming the transaction
- r : used in combination with option 1 above, will avoid the prompt by automatically rolling back the transaction

Command description. See syntax examples further down.

- ECHO: the script will echo some text on the screen
- CREATE: create a new MO instance
- DELETE: delete a MO instance
- ACTION: perform a MO action
- SET: set one MO attribute
- SETM: set several MO attributes
- SETU: set a single struct member (whereas with SET/SETM, all struct members must be specified)
- CHECK: check that an attribute value is equal to a given value
- CHECKM: enhanced "check" - supports non-transactional get operation and multiple attributes
- WAIT: pause the script execution for a given number of milliseconds
- CALL: execute another MO script. If the path of the script is not an absolute path then the current working directory will be searched.
- CALLREL: execute another MO script. If the path of the script is not an absolute path the the directory of the main script will be searched.
- TRANSACTION: mark the beginning or end of a transaction. All operations executed between the statements "TRANSACTION BEGIN" and "TRANSACTION END" will be executed within one single transaction.
- CORBATIMEOUT: set a different idle timeout for the script, to override the value of the uservariable "corba_timeout".

Script example:

//Echo a comment

ECHO "Start Test"

//Create a MO

CREATE (

parent "ManagedElement=1,SwManagement=1" identity "ROJ1192104_3_R4" moType PiuType exception none nrOfAttributes 3 productData Struct nrOfElements 5

productNumber String "ROJ1192104/3" productRevision String "R4" productName String "TUB"

productInfo String "TU" productionDate String "20030116" boardWidth Integer 3 role Integer 2 )

//Delete a MO

DELETE ( mo "ManagedElement=1,SwManagement=1,PiuType=ROJ1192104_3_R4" exception none )

//Set an attribute

SET ( mo "ManagedElement=1,Equipment=1,Jvm=1" exception none admClasspath Array Reference 4

"ManagedElement=1,SwManagement=1,LoadModule=Oms"

"ManagedElement=1,SwManagement=1,LoadModule=Asms"

"ManagedElement=1,SwManagement=1,LoadModule=VbjOrb"

"ManagedElement=1,SwManagement=1,LoadModule=Cma"

)

//Set several attributes in one MO

SETM ( mo "ManagedElement=1,RncFunction=1,UtranCell=Iub-1-1" exception none uarfcnDl Integer 10738 uarfcnUl Integer 9788

)

SETM ( mo "ManagedElement=1,RncFunction=1,Sid=1" exception none sib1 Struct nrOfElements 2 sib1RepPeriod Integer 32 sib1StartPos Integer 4 sib2 Struct nrOfElements 2 sib2RepPeriod Integer 128 sib2StartPos Integer 118 )

//Set an incomplete struct attribute. Missing struct members will be set to their current value.

SETU (

mo "ManagedElement=1,RncFunction=1,Sid=1" exception none sib1 Struct nrOfElements 1 sib1RepPeriod Integer 32 )

//Execute an MO action

ACTION ( actionName addRepertoire mo "ManagedElement=1,SwManagement=1,SwAllocation=TB_LLP" exception none nrOfParameters 1

Ref "ManagedElement=1,SwManagement=1,Repertoire=Cello_Common_MP" returnValue ignore )

//Read an attribute with transactional get and compare to a reference value

CHECK ( mo "ManagedElement=1,RncFunction=1,UtranCell=Iub-1-1" exception none uarfcnDl 10738

)

//Read one or more attributes with transactional get and compare to reference values

CHECKM (

mo "ManagedElement=1,RncFunction=1,UtranCell=Iub-1-1" exception none uarfcnDl 10738 uarfcnUl 9788

)

//Read one or more attributes with null transaction and compare to reference values

CHECKM ( mo "ManagedElement=1,RncFunction=1,UtranCell=Iub-1-1" exception none transaction null uarfcnDl 10738 uarfcnUl 9788

)

//Read one or more attributes with null transaction and print the values without comparing

CHECKM ( mo "ManagedElement=1,RncFunction=1,UtranCell=Iub-1-1" exception none transaction null compare no uarfcnDl uarfcnUl )

//wait 2 seconds (time given in milliseconds)

WAIT 2000

//run another MO script

CALL("/home/eric/scripts/newfile.mo")

//run another MO script using a path relative to the path of the main script CALLREL("test.mo")

//run some operations in a single transaction

TRANSACTION BEGIN

&lt;put some commands here&gt;

TRANSACTION END

//set a different idle timeout for the script (in seconds), to override the uv "corba_timeout" CORBATIMEOUT 1800

**4.1.40 Ctrl-Z; touch /tmp/xxxx; fg (abort MO command)**

Abort an MO command or a "for" loop.

To abort an MO command (like get/st/set/acc...) or a for loop, two steps are needed:

First type **Ctrl-Z**, to suspend moshell. Then, at the unix prompt, create an empty file **/tmp/xxxx** (where **xxxx** is the _process number_ indicated in moshell menu and in the window’s title bar) and resume moshell. This is done with the following command:

touch /tmp/xxxx ; fg

If the moshell prompt doesn’t come back even after typing &lt;enter&gt; a number of times, try again suspending (**ctrl-z**) and resuming (fg).

**4.1.41 pol\[b\]\[c\]\[d\]\[g\]\[h\]\[i\]\[k\]\[m\]\[p\]\[s\]\[r\]\[u\]\[w\]\[y\] \[-m &lt;mo&gt;\] \[&lt;interval&gt;\] \[&lt;waitTime&gt;\] \[&lt;checkTime&gt;\]**

Poll the node until the MO service is up or until an operation has completed.

**Options applicable for CPP nodes:**

- s: poll the node until telnet/ssh server is up.
- h: poll the node until http server is up.
- r: poll the node until http server is down. Eg to find out when the node restart has begun.
- d: poll the node until the action startHealthCheck is completed.
- g: poll the node until the attribute GeoRedundancy::functionState is IDLE.
- m: poll the node until /c disk mirroring is completed.
- k: poll the node until the system clock is in locked mode.
- c: poll the node until the ConfigurationVersion has completed its ongoing operations, by monitoring the attribute currentMainActivity. Useful to use after action restore/forcedRestore.
- u: poll the node until the UpgradePackage has completed its ongoing operations, by monitoring the attribute progressHeader. If progressHeader is awaiting_confirm, the confirmUpgrade action will be sent automatically to the node.

**Options applicable for COM nodes:**

- h: poll the node until COM port is up.
- r: poll the node until COM port is down. Eg to find out when the node restart has begun.
- u: poll the node until the UpgradePackage MO has completed its ongoing operations, by monitoring the attribute reportProgress. If the UpgradePackageState is waiting_for_commit, the confirm action will be sent automatically to the node.
- b: poll the node until the Brm\* MO (BrmBackup,BrmBackupManager,BrmBackupScheduler,BrmFailsafeBackup) has completed its ongoing operations.
- i: poll the node until the KeyFileManagement has completed its ongoing operations.
- w: poll the node until the SwM MO has completed its ongoing operations.
- y: poll the node until the CertM/NodeCredential MO has completed its ongoing operations.
- p: poll any MO that has a progress attribute, using option -m &lt;mo&gt;.

Only one option can be given at a time, ie, it is not supported to combine several options. If no options are given, then it will poll the node until the MO service is up. Note that this polling is done automatically before each MO command. If the loaded CV has changed during the polling then moshell will automatically reload the MOM and MIB (getmom,parsemom,lt all).

Arguments (optional):

- &lt;interval&gt; : to specify the time in seconds between each polling. Default value is 10 seconds.
- &lt;waitTime&gt; : to specify the time in seconds to wait before starting to poll. Default is 20 seconds (60 seconds for polu). The reason for this waiting time is because it can take some time before the node starts to execute an operation.
- &lt;checkTime&gt;: to specify the time in seconds to wait before checking the result of an action, when using options ’c’ or ’u’. Default value is 60 seconds.

To abort the polling, do ctrl-z, then touch &lt;stopfile&gt; (the path to stopfile is printed in the window title), then fg. See h ctrl-z for more info.

**Examples:** Performing various operations on a UpgradePackage and polling the node in between each, to find out when it’s possible to carry on.

- acc upgradepackage=CXP9012014_R10CD nonblockinginstall
- polu
- acc upgradepackage=CXP9012014_R10CD verifyupgrade
- polu
- acc upgradepackage=CXP9012014_R10CD rebootnodeupgrade

Note: if polu is executed on a node which is being upgraded from ENM or the OSSRC SMO application, then the uservariable polu_confirmupgrade should be set to 0 to prevent polu from confirming the upgrade. Otherwise this would confuse SMO. Refer to the description of this uservariable inside the file moshell/moshell.

**4.1.42 re\[i\]**

Disconnect and reconnect to the CM service (mobrowser) and/or the PM service (pmtester).

This is useful if the security settings have changed on the node during the moshell session. The "i" option is to refetch the iorfile which is necessary if the IORfile has changed on the node (this happens for instance when going from vbjorb to JacORB or changing to corba security). Note that when moshell first starts up, it is neither connected to CM nor PM.

To connect to CM service, just use the re command, the lt command or any other MO commands (eg pr, get, etc). As soon as moshell has connected to the CM service the userlabel/site attribute of **ManagedElement** will be read and prompt will be set accordingly.

To connect to PM service, just type the pst command which will list all scanners defined on the node.

If there is a node restart with change of CORBA supplier, ie going from Vbjorb (cpp3/4/5) to JacORB (cpp5.1 and above) or vice-versa, then it is necessary to issue the rei command which will also refetch the IOR file.

It is NOT necessary to type re after a node restart/upgrade or jvm restart, as long as the corba definitions have stayed the same

(corba supplier and corba security setting). Moshell stays connected all the time, though it may not be possible to perform operations while the restart is happening.

**4.1.43 getmom \[&lt;momversion&gt;\]**

Check the MOM version currently stored on the node or download a MOM from newtran01 server.

When the command is run on its own, without argument, a check will be done to find the MOM version of the node. For CPP nodes, the check is done by reading the header of the MOM file stored under http://&lt;NodeIpAddress&gt;/cello/oe/xml. For COM nodes, the check is done by reading the identifier and version attributes in the Schema MOs. Usually this check is done automatically when moshell connects to the MO service.

When the command is run with an argument, then it will try to fetch the corresponding MOM file from the newtran01 server and store it in the jarxml folder.

Example:

\>> getmom RNC_NODE_MODEL_K_9_115_COMPLETE

**4.1.44 parsemom \[&lt;momFile&gt;\]**

Parse an xml MOM file

Without argument, the parsemom command just reparses the current MOM version. Can be used in conjunction with the getmom command to check and parse the current MOM.

With argument, the parsemom command will parse a different MOM to the one currently loaded in moshell. Can be useful if an incorrect MOM is stored on the node or if just wanting to browse a MOM offline. Example: parsemom moshell/jarxml/RNC_NODE_MODEL_D_3.xml

**4.1.45 flt/fltc &lt;motype-filter&gt;**

Load proxys for an MO type that is not defined in the MOM. ("Force" lt/ltc).

Can be useful in case the xml MOM isn’t up to date with the node SW, or in case there is no xml MOM.

Example: flt rncsystemparameters

**4.1.46 fget\[i\]/lfget\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute&gt;\]**

Read attributes that are not listed in the MOM (f="Force").

With fget/lfget, the exact attribute name must be specified in the command.

Any attribute can be displayed as long as it is supported by the node SW.

**Options:**

- i: to read an attribute via "internalmomread" command. Only applicable to RCS nodes (MSRBS).

**Examples:**

- fget ^pluginunit= resourceid
- fgeti ^eutrancellfdd= loadCtrlPrioOfMta
- fgeti ^eutrancellfdd=7 dlCyclicPrefix > $var

**4.1.47 eget/leget &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all \[&lt;attribute&gt;\]**

Read attributes that are not listed in the MOM (e="Extended").

With eget/leget, the attribute name is optional, or an attribute filter can be used.

Only attributes listed in the file moshell/commonjars/extendedMOM.txt can be shown. The attributes of this file can also be shown in the commands get/kget/sget if the uservariable use_extended_mom is set to 1 (default: 0).

Example: eget plug res

**4.1.48 sget/lsget/skget/lskget/shget/lshget &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all**

Read CM/FM attributes from MO(s), one by one ("Slow" get).

Slow but useful in case the standard "get" command is not working due to some attribute returning an exception.

**4.1.49 fset\[i\]/lfset\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all &lt;attribute&gt; \[&lt;value&gt;\] \[&lt;attribute-type&gt;\]**

Set an attribute that is not described in the MOM ("Force" set).

Can be useful in case the xml MOM isn’t up to date with the node SW, or in case there is no xml MOM (e.g. MGW application part).

The syntax is similar to the "set" command except that the attribute type has to explicitely specified using the reference list below.

**Options:**

- i: to set an attribute via "internalmomwrite" command. Only applicable to RCS nodes (MSRBS). With "i" option, the attribute type should not be specified.

**Examples:**

- lfset subrack=ms,slot=20,pluginunit=1$ administrativestate 0 i
- fseti ^eutrancellfdd= loadCtrlPrioOfMta false

Following attribute types are supported:

- i integer/long/enum
- l longlong
- s string
- b boolean
- r moref
- f float
- t struct
- ai array of integer/long/enum
- al array of longlong
- as array of string
- ab array of boolean
- ar array of moref
- af array of float
- at array of structref

**4.1.50 facc/lfacc &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all &lt;action&gt; \[&lt;param1&gt;\] \[&lt;param2&gt;\]**

Perform actions that are not defined in the MOM ("force" action).

Can be useful in case the xml MOM isn’t up to date with the node SW, or in case there is no xml MOM.

If the parameter is a an _integer_ or a _string_, the parameter type does not need to be specified as in the example below.

Example:

- lfacc Sector=1,Carrier=1,HsDschResources=1 startRDBTCellHidden 16
- facc CommContexts=1 readHsMusOnCCHidden 0

Otherwise it should be explicitely specified, using the reference list below. **Examples:**

- lfacc Equipment=1,Subrack=1,Slot=4,PlugInUnit=1,RaxDeviceGroup=1,UbchDeviceSet defineCqiPatternHidden 0 5 15,16,17,18,19:ai Following parameter types are supported:
- i integer/long/enum
- l longlong

s string

- b boolean
- r moref
- f float
- t struct
- ai array of integer/long/enum
- al array of longlong
- as array of string
- ab array of boolean
- ar array of moref
- af array of float
- at array of structref

**4.1.51 fdel/lfdel &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;**

Delete MO(s), including systemCreated MOs.

Works in the same way as the regular del/ldel command except that it also tries deleting the systemCreated MOs, whereas the del command skips them.

Though the systemCreated MOs cannot be deleted, this command can be useful when generating set commands in "simulated undo mode" for those systemCreated MOs.

## 4.2 Other MO commands

**4.2.1 cvls/cvmk/cvms/cvset/cvrm\[u\]\[s\]/cvrbrm/cvcu/cvget\[f\]\[u\]\[d\]/cvput/cvls1/cvre/cvfa/cvfd**

CV backup handling: list, make local, make remote, remove, setstartable.

A set of commands similar to the "cv" commands in OSE but operate through MO interface instead of telnet/ssh.

Command syntax and description (CPP):

- cvcu: display the current cv information only (equivalent of "cv cu").
- cvls \[&lt;cv-filter&gt;\]: display both the current cv information (equivalent of cv cu) and cv list (equivalent of cv ls). It is possible to filter the output of cvls to only show CVs where the CV name or CV attributes match a certain string. The proxy Id of the CVs can be used in the commands cvrm and cvget. The display of CV proxy Id can be disabled with command "safe+".
- cvls1: similar to the cvls command except that it executes via the OSE shell instead of the MO service.
- cvmk &lt;cvname&gt; \[&lt;operator&gt;\] \[&lt;comment&gt;\] : create a local cv backup. Operator name and comments (not longer than 40 characters) can be given as argument.
- cvset &lt;cvname&gt;|&lt;cv-Id&gt;: set a cv as startable.
- cvms &lt;cvname&gt; \[&lt;operator&gt;\] \[&lt;comment&gt;\] : create a cv and make it startable (combination of cvmk and cvset)
- cvget\[f\] &lt;cvname&gt;|&lt;cv-filter&gt;|&lt;cv-Id&gt; \[&lt;destdir&gt;\] : make a remote backup of a cv to the workstation. The operation is done with the MO action putToFtpServer unless option "f" has been specified, in which case the transfer will be done by FTP/SFTP. The second argument is optional. If not given, a default folder is chosen for the backup

~/moshell_logfiles/logs_moshell/cv/&lt;node&gt;/&lt;date&gt;\_&lt;time&gt;/

- cvgetu &lt;UP&gt; : make a remote backup of all CVs connected to a specific UP (same as cvget but with the UP as argument).
- cvgetd &lt;cvname&gt;|&lt;cv-filter&gt;|&lt;cv-Id&gt; \[&lt;destdir&gt;\] : download the DB dump (dbdump.zip) for one or more CVs. This is only applicable for CPP OSE nodes that support the MO action generateDbDump. The DB dump is a text dump of the db.dat and can be read in SQL mode ("moshell -d /path/to/dbdump.zip") to perform DB consistency check without need for the Polyview SW.
- cvput &lt;zipped-cvfile&gt; : transfer a remote CV backup (zip file) from the workstation to the node. The operation is done with the MO action getFromFtpServer.

cvrm &lt;cvname&gt;|&lt;cv-filter&gt;|&lt;cv-Id&gt; : remove one or more cv’s. If the argument does not match an existing CV

then all CVs matching that string will be removed. A confirmation message is printed before removal. The CV(s) will automatically be removed from rollback list when necessary.

- cvrmu &lt;UP&gt; : remove all CV’s connected to a specific UP (same as cvrm but with the UP as argument).
- cvrbrm : remove one or more cv’s from the rollback list. If the argument does not match an existing CV then all CVs matching that string will be removed. A confirmation message is printed before removal.
- cvfa : activate robust reconfiguration (same as MO action Configuration.activateRobustReconfiguration)
- cvfd : deactivate robust reconfiguration (same as MO action Configuration.deactivateRobustReconfiguration)

Command syntax and description (COM):

- cvcu : display the current backup information only.
- cvls \[&lt;cv-filter&gt;\] : same as above plus the list of SwVersions, UpgradePackages and BrmBackups. The Id field of the BrmBackup can be used in the commands cvrm and cvget. Note: the RestType column corresponds to the attribute UpgradePackage::upgradeRestartType
- cvmk &lt;cvname&gt; : create a local backup.
- cvre &lt;cvname&gt;|&lt;cv-Id&gt; : restore a backup (equivalent to doing a cvset followed by node restart on CPP)
- cvrm &lt;cvname&gt;|&lt;cv-filter&gt;|&lt;cv-Id&gt; : remove one or more backups from the node. If the argument does not match an existing backup then all backups matching that string will be removed. A confirmation message is printed before removal.
- cvrmu &lt;UP&gt; : remove all backups connected to a specific UP (same as cvrm but with the UP as argument).
- cvrms: remove all SYSCR backups and clear the RestoreEscalationList (no arguments).
- cvget &lt;cvname&gt;|&lt;cv-filter&gt;|&lt;cv-Id&gt; \[&lt;destdir&gt;\] : export a backup to the workstation. The second argument is optional. If not given, a default folder is chosen for the backup

~/moshell_logfiles/logs_moshell/cv/&lt;node&gt;/&lt;date&gt;\_&lt;time&gt;/

- cvgetu &lt;UP&gt; : export all backups connected to a specific UP (same as cvget but with the UP as argument).
- cvput &lt;zipped-cvfile&gt; : transfer a backup (zip file) from the workstation to the node.
- cvfa : activate failsafe backup (same as MO action BrmFailsafeBackup.activate)
- cvfd : deactivate failsafe backup (same as MO action BrmFailsafeBackup.deactivate)
- cvfda : same as cvfd but the Post_failsafe_backup will be added to the RestoreEscalationList
- cvfdc : same as cvfda but all SYSCR backups will be deleted and removed from RestoreEscalationList

**Examples:**

- cvls: List all CVs
- cvls CXP9011274_R9A: List all CVs using Upgradepackage CXP9011274_R9A
- cvms RNC11_Final: Create a cv and make it startable (no userid or comments given)
- cvms RNC11_Final eanzmagn cell power increased to 33dBm: Create a cv and make it startable (userid and comments given)
- cvrm Temp: Remove all cv’s whose name match the string "Temp"
- cvrm !Final: Remove all cv’s whose name don’t match the string "Final"
- cvrm !Final|RNC: Remove all cv’s whose name don’t match the string "final" or the string "RNC"
- cvget RNC11_Final: Make a remote backup of a CV to the workstation where moshell is runing
- cvget RNC11.\*Fi: Make a remote backup of all CVs whose name matches RNC11.\*Fi
- cvput /home/eric/RNC11_Final.zip: Transfer a remote cv backup from the workstation to the node
- cvrm 1-15: Remove the oldest 15 CVs.
- cvget 3,5,8: Fetch CV number 3, 5, and 8 from the cv list.
- cvset 23 : Set CV number 23 as startable
- cvrmu CXP9011274_R9A: Remove all CVs/Backups connected to the UP CXP9011274_R9A
- cvgetu CXP9011274_R9A: Export/fetch all CVs/Backups connected to the UP CXP9011274_R9A
- cvfa: Activate failsafe/robust configuration cvfd: Deactivate failsafe/robust configuration cvfdc: Deactivate failsafe and delete all SYSCR backups (Gen2 only)

**4.2.2 inv\[hlxbpctyrgfau\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\]**

Complete HW/SW inventory. Includes information about RPUs, licensing, JVM, devices, XPs, ISL, etc.

This command performs a complete HW/SW inventory via the MO and COLI interface. All SW including JVM, RPU, and Device SW (spm,dsp,fpga) is shown. Licensing (features and capacity) as well as overview of the ISL links is also shown.

**Options:**

The options are used to reduce the number of tables displayed. Without options, all tables are displayed.

- h : HW information only.
- x : HW, CPRI, and RF information (TX/RX/VSWR and RU to Cell mapping)
- xf : same as "x" but without CPRI.
- xu : same as "x" but without RF (only UEs)
- xt : same as "x" but without RF nor temperature.
- xty : same as "x" but without RF, temperature and SFP data. Combined with "g" (invxtyg) this is the quickest way to get the CPRI and RF connections.
- xa : same as "x" but with RU mapping to Antenna/TMA/RET instead of Cell
- xaf : same as "x" but with RU mapping to both Cell and Antenna/TMA/RET
- xtaf: same as "xaf" but without TX/RX/VSWR/temperature (quicker)
- l : licensing information only (feature and capacity licenses)
- p : show CPU load of the PlugInUnits: obsolete, replaced by command "lh all procload".
- r : re-read the inventory data from the node.
- c : print the tables in CSV format
- b : show receiver BER values in the CPRI tables
- g : display graphical view of CPRI and RF connection (RBS/ERBS/MSRBS)

The first time the command is run, it takes a bit longer because the data has to be fetched from the node before parsing. The following times the command is run, the existing data is parsed again, unless the r switch is used ("refresh"), in which case, the data is fetched again and parsed. When no options are specified, all the information will be displayed except BER and Antenna (which can be printed with options "b" and "a" respectively).

**Arguments:**

- The first argument (general filter) allows to only show the lines matching the filter string. Negative filter is supported by putting a exclamation mark in front of the filter. See examples further down.
- The second argument (state filter) allows to only show the lines where the MO status matches the state filter.

**Printout description:**

- the first table shows the MP/BP hardware info, position, and status. The GE column (when subrack contains CMXB) shows the connection status to the 10G IP backplane (attribute EthernetSwitchModule::backPlanePortState), the CE column

(when subrack contains SCXB) shows the connection status to the 1G IP backplane (attribute

ControlSwitch::backPlanePortState). The column "c/p" shows the disk usage on /c or /p (depending if it is a central MP or regular MP), and the column "/d" shows the disk usage of the /d volume.

- the second table shows the AuxiliaryUnits (XP) hardware/software info, status, temperature in Celsius, and uptime in days ("UPT" column).
- the third table shows the subracks and backplanes HW info. The switchState field consists of three digits: the state of the switch, the state of plane A, and the state of plane B.
- the next table shows the ISL links. The ISL links are only applicable in nodes containing several subracks, eg RNC/MGW. All ISL links connecting the main subrack to each extension subrack are shown. The status of each link is shown: 1st digit corresponds to "operationalStateSync" and the 2nd digit corresponds "operationalStateTraffic". The ports connected to each ISL are shown, including the type of board (SCB/SXB) and the port state (active/passive).
- the next table shows the RDS/DOT inventory. Only applicable for RBS/ENB with IRU (Indoor Radio Unit). The description of the fields can be found further down in this help.

the next table shows the CPRI links, as well as IDL and IPL links when present (Inter-DU links, Inter-PIMCU links). Only

applicable for RBS/ENB.

- the next table shows the RF ports of the radio units, one line per port. See description further down.
- the next two tables shows the list of features and capacity and their licensing status

The FAJ numbers are read primarily from the License.xml file on the node and if not found there, they are read from the excel sheets on

https://ericsson.sharepoint.com/sites/SW_License_Handling_Community/SWLicenseHandling/ELIS/Wiki/License The information about restricted features is read from the documents 2/22104-FGB101135 and 4/19812-FGB101135.

- the next table shows the java loadmodules that are running in the JVM.
- the next table shows the configuration and status of the ReliableProgramUniters (RPU).
- the last table shows the Programs running in each processor including devices.

**Description of the "state" column:**

State information is always abbreviated to one digit, in the same way as for other printouts such as stt, stv, str, etc.

- 1 = unlocked enabled
- 0 = unlocked disabled
- D = unlocked enabled and availabilityStatus=degraded
- L = locked (opstate could be enabled or disabled)

On Router6000 there are additional states:

- L1 (Shutdown), L2 (Deactivated), L3 (Out of service diagnostic), L4 (Not configured)
- A1 (IN_TEST), A2 (FAILED), A3(POWER_OFF), A4(OFF_LINE), A5(OFF_DUTY), A6(DEGRADED), A8(LOG_FULL), A10(DEPENDANCY)

**Description of the LED columns - correspond to attributes in FieldReplaceableUnit or PlugInUnit MO:**

- FAULT: RED ( faultIndicator )
- OPER: GREEN ( operationalIndicator )
- MAINT: YELLOW or BLUE ( maintenanceIndicator )
- STAT: YELLOW ( statusIndicator )

**Description of the PMTEMP column (applicable in MSRBS >= 19Q2 )**

The value corresponds to the counter FieldReplaceableUnit::pmUnitTemperatureLevel and is translated as below:

- NOK-: the temperature is too low, service unavailable
- OK-: the temperature is low but still in the acceptable range
- OK: the temperature is ok
- OK+: the temperature is high but still in the acceptable range
- NOK+: the temperature is too high, service unavailable

**Description of the fields in the RDS/DOT table (only applicable for RBS/ENB containing IRUs with DOTs):**

- MO/FRU: the MO name of the AuxPlugInUnit/FieldReplaceableUnit representing this DOT unit
- LNH/ID: the linkhandler address and port number (1 to 8) of the IRU to which the DOT is connected
- RDS: the product name of the DOT unit
- ST: the state of the AuxPlugInUnit/FieldReplaceableUnit MO representing this DOT unit
- P: the PowerOverEthernet status. Read from the command eqpm rdPoe status all (1=detected:true, 0=detected:false)
- C: the Connection status. Read from the command rdc dump all (1=RD_OPERATIONAL, 0=RD_FAILED/NOT_PRESENT)
- T: the LTU status. Read from the command rdsh all hal ltu lock (1=LOCKED, 0=NOT_LOCKED)
- TX/RX: the status of the DOT’s TX/RX branch A and B respectively. Read from the command rdc dump all (1=ENABLE, 0=DISABLE)
- TEMP: the temperature of the DOT, in Celsius. Read from the command rdsh all temp.
- VII: the status of the visual indicator of the DOT. Read from the command rdsh all vind.

FAULT: indicates the presence of alarms on the DOT. Read from the command eqpm rdFault dump **Description of the fields in the CPRI table (only applicable for RBS/ENB):**

- ID: an arbitrary reference number for the link, also used in the SFP tables.
- T: Type. E=Electrical, O=Optical, I=Internal (eg IDL or IPL). For Optical links, there are three additional tables showing the product information and diagnostics for the SFP’s located at the extremities of each CPRI link (SFP= Small Form-factor Pluggable transceiver). See description further down.
- RiL: the name of the RiLink MO representing this CPRI link.
- BPBP: B=Board state, P=Port state. The state of PlugInUnit/AuxPluginUnit/FieldReplaceableUnit MO and RiPort MO on each side of the CPRI link.
- R: Role. M=Master, S=Slave. Master is always on the left hand side Slave on the right.
- LENGTH: Cable length. The cable length is obtained from the CPRI link delay value in nanoseconds which is then divided by 4.9 to obtain the cable length (assuming a delay of 4.9ns per meter of cable, or two thirds of the speed of light)
- BER: the counter value of the received Bit Error Rate. NZ=Non-Zero (=> there are Bit Errors on this port). Note: only shown with option "b".

**Description of the fields in the SFP diagnostics table (only applicable for RBS/ENB containing optical CPRI links):**

- ID: the unique id of the CPRI link which can be used to match against the connection and product information in the above two tables of the printout.
- LINK: indicates if the CPRI link is Up or Down according to the information from the COLI command "ricr".
- WL: the wavelength of the laser, in nm.
- TEMP: temperature of the SFP in Celsius
- TXbs: the TX bias level in percent of the low/high warning thresholds. Calculated with the formula 100 \* (Bias - LowLimit) / (HighLimit - LowLimit). Should not be negative or higher than 100%. Acceptable values are typically in the range of 1% to 50%, depending on SFP vendor.
- TXdBm: the transmitted power in dBm
- RXdBm: the received power in dBm
- BER: the counter value of the received Bit Error Rate. NZ=Non-Zero (=> there are Bit Errors on this port). Note: only shown with option "b".
- DlLoss/UlLoss: the difference in dB between the TX power of the sending port and the RX power of the remote port. Acceptable values should be between -1 dB and +3dB when using short point-to-point connections (length < 200m). When using longer connections and/or with xWDM filters/splitters then the loss values should be compared according to expected link budget, taking into account the losses filters/splitters/connectors.
- TT: corresponds to the value of the attribute RiLink::transportType. The meaning of the number can be obtained with command "mom transporttype".
- Consistency checks: three checks are performed on the content of the SFP A0 area. Check #1 is the preamble (should be 0304), check #2 is the checksumBase (bytes 2-62->63), check #3 is the checksumExtended (bytes 64-94->95). There is also the DMI checksum #4 done toward SFP A2 area (modulo 256 of bytes 0-94->95). If any of these checks fail the VENDORNAME will show CKSFAIL#x where x represents the list of failed checksums.

If the CPRI link is down or the SFP voltage is not between 2 and 4V, then some of the diagnostics values will show "NA" ("Not

Applicable").

**Description of the fields in the TN ports table**

- BOARD/LNH: the product name and linkhandler address of the board where the TN ports are located
- PORT: the MO name of the TnPort MO
- T: the port type. E=Electrical, O=Optical. For Optical port, the SFP information will be found in the SFP table just above the TN ports table.
- S: the state of the EthernetPort MO connected to the TnPort. 1=Unlocked&Enabled, 0=Unlocked&Disabled, D=Unlocked&Disabled&Degraded, L=Locked
- OpMode: the value of the attribute EthernetPort::operOperatingMode
- MacAddress: the value of the attribute EthernetPort::macAddress
- VlanIds: the list of vlanIds for all the VlanPorts connected to the EthernetPort which is associated with this TN port.
- LOS: the number of times connection was lost due to ethernet link failures during the current ROP. Corresponds to the

counter EthernetPort::ifHCLossOfSignal.

- BER: the counter value for the received and transmitted packet errors for the current ROP. NZ=Non-Zero (=> there were packet errors on this port). Corresponds to the counters ifInErrors/ifOutErrors on EthernetPort MO. Note: only shown with option "b".

**Description of the fields in the RF ports table**

- AuxPiu/FRU: the MO name of the AuxPlugInUnit/FieldReplaceableUnit MO representing this radio unit.
- LNH: the linkhandler address of the radio unit, can be used to connect to the radio with command "lhsh".
- BOARD: the product name of the radio unit
- RF: the RF port on the radio unit
- BP: B=Board state, P=Port state. The state of the AuxPlugInUnit/FieldReplaceableUnit MO and RfPort MO.
- TX (W/dBm): the currently transmitted power in Watts and dBm.
- VSWR (RL): the VSWR and Return Loss in dB
- RX (dBm): the received power in dBm
- RLs/UEs/gUEs: the number of 3G RadioLinks / 4G UE connections / 5G UE connections respectively
- Sector: the Sector MO or SectorEquipmentFunction MO connected to the RF port is represented by "SR" or "SE", respectively. SR is applicable for WRBS, and SE is applicable for ENB and MSRBS. If there is an asterisk next to the SR/SE name, then it means that this sector uses mixedModeRadio.
- Cells: for WRBS, shows the RbsLocalCells connected to that RF port and their state and localCellId values. For ENB and

MSRBS LTE, it shows the EUtranCellxDD/NbIotCell MO names, and their corresponding state, cellId and PCI values. For

MSRBS WCDMA, it shows the NodeBLocalCell name in the following way: NB=&lt;localcellgroup&gt;/&lt;localcell&gt;/&lt;sectorcarrier&gt; , followed by their respective state and localCellId values. For MSRBS GSM, it shows the GsmSector/Trx in the following way: GT=&lt;gsmsector&gt;/&lt;trx&gt;. For MSRBS NR, it shows the NRCellDU in the following way: NRC=&lt;name&gt;.

Regarding the cell states, the meaning is: 1: Unlocked&Enabled, 0: Unlocked&Disabled, L: Locked, B:

EUtranCellxDD::cellBarred=BARRED, R: EUtranCellxDD::primaryPlmnReserved=true, S:

EUtranCellxDD,CellSleepFunction::sleepState=ACTIVATED, D: EUtranCellxDD::availabilityStatus=DEGRADED

- AG: the name of the AntennaUnitGroup MO connected to this RF port.
- AS: the name of the AntennaSubunit MO connected to this RF port (AS=x/y => AntennaUnitGroup=x,AntennaUnit=y,AntennaSubunit=1)
- RET/TMA: the name of the AntennaNearUnit MO (RET or TMA) connected to this RF port (RET=x/y or TMA=x/y => AntennaUnitGroup=x,AntennaNearUnit=y)

**Description of the fields in the graphical view**

- each box represents a FieldReplaceableUnit (MSRBS) or PlugInUnit/AuxPlugInUnit (RBS/ERBS). Inside each box are the MO id, the board type, and the link handler. On the side of each box are the CPRI port names. On the bottom of each RU box are the RF ports and corresponding sector/cells.
- each line represents a CPRI connection. On the CPRI connection are listed:
    - - the ID number from the CPRI tables described above. Next to it is the RiLink number when applicable (MSRBS/ERBS).
        - the link type (E/O) and bit rate (eg: O25 = Optical 2.5 GB/s).
        - the length expressed in meters (considering delay of 5 ns per meter), when applicable (MSRBS/ERBS).

+---------+ +----------+

| | A O25 D1 | 2 |

| |-----1/1-----| RRUS11B4 |

| | 181m | BXP_0 |

|     |     |     |     |
| --- | --- | --- | --- |
| \|  |     | \|  | +----------+ |
| \|  |     | \|  | \|A \|B |
| \|  | 1   | \|  | SE=1 FDD=1 |

| DUS3201 |

| 000100 | +-----------+

| | B O25 D1 | 3 |

| |-----2/2-----| RRUS11B13 |

| | 180m | BXP_1 |

|     |     |
| --- | --- |
| \| \| | +-----------+ |
| \| \| | \|A \|B |
| +---------+ | SE=2 FDD=2 |

**Examples:**

- inv CXC132055 –> only rows matching CXC132055 will appear. This is convenient to lookup the name of an LM and in see which boards it is running.
- inv : –> only RPU information will be printed.
- inv nss –> to see which loadmodules contain the string "nss" and in which boards they are running.
- inv . L|0 –> only rows where the state of the MO is locked or disabled will appear.
- inv roj L|0 –> only rows matching "ROJ" and where the state is locked or disabled will appear.
- inv !program –> only rows NOT matching the word "program" are displayed.

**4.2.3 cab\[adefghlmrstxc\] \[ | &lt;unix-cmds&gt; \]**

Display of miscellaneous COLI printouts relating to hw, sw, restarts, leds, cpu load, errors, disk/ram usage

This command is only applicable to CPP nodes. On RCS nodes "cab/cabx" aliases to "invx" and "cabr/caba" aliases to "lgg".

The cab command offers a number of options, it is possible to combine several options, eg: cabslxrdg, cablx, cabxs, etc.

The command cabslxrdgm will give the maximum amount of information.

Note: Most options are now obsolete and superceded by other commands such as "inv", "proctemp", "procload", and "fte".

**Options:**

- h : prints MP/BP HW info and led status, MP temperature, and coreMgr status. If no options are given then this is the default option. Superceded by "inv" and "proctemp" commands.
- t : same as "h" but without the temperature, nor the TX/VSWR values (in RBS/ENB)
- x : same as "h" plus led and hw info for the XP boards (eg: TMA, MCPA, Fans, RU, RRU, etc.). With option "c" ("cabxc") the output is in CSV format. Superceded by "inv" command.
- s : same as "h" plus list of programs running in all MP/BP. Superceded by "inv" command.
- r : prints all MP/BP restarts grouped by board. To see this info in chronological order, use the command "lgg". Abnormal restarts are highlighted in red.
- a : prints only abnormal MP/BP restarts.
- d : print disk usage. Disks that are getting over a certain limit will appear in color. The limit can be defined in cabview file.
- f : print disk and flash usage.
- g : print MP/BP HW errors (e.g. faulty disk, faulty RAM, etc).
- m : print MP/BP RAM memory usage.
- e : print MP/BP added T&E trace conditions. Superceded by fte s command.
- l : MP/BP/SP processor load. Superceded by procload command.

The following OSE commands are run and parsed by the various "cab" functions:

- h : _pboot sh par, vii, mirror s, ppctemp, boardtemp_
- t : _pboot sh par, vii, mirror s_
- x : _pboot sh par, vii, mirror s, ps port\*, par get SYS_HW\*, listObj subrack, getAttrObj subrack, warpA/warpB read, warp3 txpwr, fui get temp, fui get vswr_
- s : _pboot sh par, vii, mirror s, listloaded_
- l : _pboot sh par, capi prio, capi core all_
- r : _llog -l_
- a : _llog -l_ Only restarts with error code not matching 0xB0AD or 1010\[9-F\] or containing a PMD are printed
- d/f: _vols, ls /d/loadmodules_
- g : _pboot sh par, dumpelg_
- m : _pboot sh par, mmu, mm -p_
- e : _pboot sh par, te s, te s -restart_

Note 1: Regarding the CoreManager status: If a board has got a CoreManager status, it means that the board is running the Core Manager programs (EqmMgr, Database, LoaderServer). If the node is configured with Fault Tolerant Core, there are two boards running the Core Manager functionality. One board is _Active_ and the other one is _Standby_.

When the node is configured with Fault Tolerant Core, the **/c** drive is mirrored between the two Core Manager boards.

If the status of the Standby board is _StandbyReady_, then it means that the **/c** drive is correctly mirrored and the standby board can take over the active role at any time, in case the active board fails or restarts.

If the status of the Standby board is _StandbyWriting_, then it means that the **/c** drive is performing a small update and the standby board can take over in a short while, as soon as the disks are updated.

If the status of the Standby board is _StandbySync_, then it means that the **/c** drive is performing a complete update and the standby board will not be able to take over until this is completed. The progress is shown as a percentage value (eg:

**StandbySync-56%**).

Note 2: When many commands are to be sent, the cab function will put them into a command file, transfer that file (via (s)ftp) to the node and run that file from within the node, using the shell -f command.

This will save time instead of having to send each command one by one to the node.

There is a user variable called _fast_cab_threshold_ which determines the number of boards in the node above which a command file will be transferred to the node.

See Section 2.4 and the **moshell** file for more info about user variables.

Note 3: Regarding PMD Ids appearing in cabr/caba:

A Post-Mortem Dump (PMD) may be associated with an abnormal board restart. In this case, the PMD Id is shown in cabr/caba commands. It is possible to show and collect the PMD files with the command lgp. Alternatively the commands dump list -a, ftreef /c/pmd, or lg1 can also be used to show the PMD files.

Note4: Regarding TX power calculation in "cabx":

For RU PL4:

TXPwrA=(DL_PM_PA0_C0+DL_PM_PA0_C1+DL_PM_PA0_C2+DL_PM_PA0_C3)\*16384\*powerClassA/(1228800\*8491396) TXPwrB=(DL_PM_PA0_C0+DL_PM_PA0_C1+DL_PM_PA0_C2+DL_PM_PA0_C3)\*16384\*powerClassB/(1228800\*8491396) Where:

- DL_PM_PA0_Cx are read from RU COLI commands "warpA read" for TXA och "warpB read" for TXB • powerClass is read from RU COLI command "db list \*currentPowerClass", or "txm rh all wrk dump" For RU PL5:
- TXPwrA=pwrClassA \* 268435456/8491396 \* ( 10^(B0/10) + 10^(B1/10) + ... + 10^(B7/10) )
- TXPwrB=pwrClassB \* 268435456/8491396 \* ( 10^(A0/10) + 10^(A1/10) + ... + 10^(A7/10) ) Where:
- A0 to A7 and B0 to B7 are read from RU COLI command "warp3 txpwr" or "warp:0/warp:1 txpwr"
- powerClass is read from RU COLI command "db list \*currentPowerClass", or "txm rh all wrk dump"

Note5: Regarding RSSI measurement in "cabx" for WRBS:

The RSSI is value is read from the MP trace bus_receive on CDCI_TR. A asterisk in front of a TrDevice in the printout indicates that this TrDevice has reported a measurement. TrDevices without asterisk could be due to that this is a TX or that the cell is disabled.

Note6: Regarding VSWR measurements in "cabx":

For most RUs/RRUs, the main command used for printing the return loss is fui get vswr &lt;tx&gt;.

Note7: Refreshing of the cache.

The cab command reads most of its data from the node each time it is executed. However there is some static data such as board list and cell list which is read only once and then kept in a cache. If this information has changed during the session, it is possible to refresh the cache by running the "bor" command.

Note8: DU Temperature is read with:

- DUW10/20/30: trace4 on process SriBcThread, sensor3 (0x4B)
- DUW11/31/41: coli command readPower, sensor 1 (0x4D)
- DUL20/21: coli command boardtemp, sensor0
- DUS31/41/ODS: coli command boardtemp, sensor1

**4.2.4 sdi\[cjrx\]**

System Diagnostics CPRI.

Perform a system diagnostics test of the RBS/ENB CPRI links.

Options:

- c : print the tables in CSV format
- j : combine the first three tables into one machine-readable CSV table (useful for parsing mobatch-run)
- r : re-read the data from the node.
- x : show Radio TX/RX power and read Radio SFP data from the radios instead of baseband (takes longer time but may give more complete data in some cases)

**Printout format, first table**

Each line in this table represents a CPRI link.

- ID: arbitrary number to identify the CPRI link
- RiL: MO name of the associated RiLink (only applicable for ENB/MSRBS, not WRBS)
- Type: E=Electrical, O=Optical, 25=2.5Gb/s , 49=4.9Gb/s, 98=9.8Gb/s, 103=10.3Gb/s
- Res: the result of the test, OK, NOK (Not OK), OKW (OK with Warning), NT (Not Tested = when a port or board on the link is locked)
- MO1-MO2: a shortened LDN of the CPRI port MO on each side of the link
- BOARD1-BOARD2: the board type on each side of the link
- AlmIDs: the list of alarms associated with the RiLink, RiPorts or FRU/PIU/AuxPius connected to the link (only applicable on ENB/MSRBS)
- Cells: the list of Cells (EUtranCell, NodeBLocalCell, RbsLocalCell, GsmTrx, etc) associated with any radios connected to the link

|     |     |
| --- | --- |
| 1 ;1 ;O98 ;OK ;1/1(A) 1/1/RU-1-1(D1) ;DUS4102 RRUS82B41 ; | ;TDD=1 TDD=2 (1,L) ;Passed |
| 2 ;2 ;O98 ;NOK ;1/1(B) 1/1/RU-1-1(D2) ;DUS4102 RRUS82B41 ; | ;TDD=1 TDD=2 (1,L) ;Fiber Loss DL (DlLoss-UlLo |
| 3 ;3 ;O25 ;OK ;1/1(C) 1/2/RU-1-2(D1) ;DUS4102 RRUS62B41D ; | ;TDD=3 (S) ;Passed |
| 4 ;4 ;O98 ;NOK ;1/1(D) 1/3/RU-1-3(D1) ;DUS4102 RRUS62B41D ;1,2 ... | ;TDD=4 (B) ;Fiber BER DL (BER2=NZ) |
| 15 ;13 ;O25 ;OKW ;XMU03(11) RRU-101(D1) ;XMU03 RRUS12B2 ; | ;FDD=9A_1 (R) ;Conditionally Passed (Unab |

- States: the state of each cell. 1: Unlocked&Enabled, 0: Unlocked&Disabled, D: Unlocked&Enabled&Degraded, L: Locked, B: EUtranCellxDD::cellBarred=BARRED, R: EUtranCellxDD::primaryPlmnReserved=true, S: EUtranCellxDD,CellSleepFunction::sleepState=ACTIVATED
- Issue: a short description of the test result including information about which particular checks failed.

\====================================================================================================================

ID ;RiL ;Type ;Res ;MO1-MO2 ;BOARD1-BOARD2 ;AlmIDs ;Cells (States) ;Issue (Failed checks)

\====================================================================================================================

\--------------------------------------------------------------------------------------------------------------------

**Printout format, second table**

This table is only printed if the option "a" was given and if there are alarms affecting CPRI links.

Each line in this table represents an alarm, could be an active alarm, or a past alarm that has been toggling during the past 24 hours

- AlmID: an arbitrary number to identify the alarm, this number is found next to one or more CPRI links in the first table
- IDs: the list of CPRI link IDs that have this alarm
- RiLs: the list of RiLink MOs that correspond to the CPRI link IDs
- Status: A=Active, if the alarm is still active. T=Toggling, if the alarm is not active but has been toggling in the past 24 hours. In case of toggling alarm, it will show how many times the alarm has toggled and how many hours/minutes ago was the last time since the alarm toggled.

\====================================================================================================================

AlmID ;IDs ;RiLs ;Status ;Alarm

\====================================================================================================================

1.  ;4 ;4 ;T 8x 12h28m ;Link Degraded - RiLink=4 (High BER at far end of the link. Near end port:PlugInUnit=1
2.  ;4 ;4 ;T 8x 12h30m ;Link Degraded - RiLink=4 (High BER at near end of the link. Near end port:PlugInUnit=

\-------------------------------------------------------------------------------------------------------------------====================================================================================================================

AlmID ;IDs ;RiLs ;Status ;Alarm

\====================================================================================================================

\--------------------------------------------------------------------------------------------------------------------

**Printout format, third table**

This table is only printed if some CPRI links failed the test.

Each line in this table represents a particular type of issue.

- - IDs: the list of IDs for the CPRI links that had a issue of this type
    - RiLs: this list of RiLink MOs corresponding to each CPRI link listed in the IDs column (only applicable for ENB/MSRBS, not WRBS)
    - Issue and Recommended Action: a longer description of the problem, followed by some recommendations for corrective actions for each type of issue.

\======================================================================================================= IDs ;RiLs ;Issue and Recommended Actions.

\======================================================================================================= 2 ;2 ;Fiber Issue - Far End Reports Excessive Optical Power Loss.

\-------------------------------------------------------------------------------------------------------

1.  Troubleshoot to determine where optical power is being lost or Bit Errors are detected. Start at th
2.  Refer to and follow Ericsson CPI "Handling SFP Modules and Optical Cables" for proper handling, Cle

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 ;4 ;Fiber Issue - Far End Reporting Bit errors.

\-------------------------------------------------------------------------------------------------------

1.  Troubleshoot to determine where optical power is being lost or Bit Errors are detected. Start at th

|     |     |     |
| --- | --- | --- |
| 1   | ;5 ;5 ;A | ;Inconsistent Configuration - FieldReplaceableUnit=6 (No hardware detected f |
| 2   | ;6 ;6 ;A | ;Inconsistent Configuration - FieldReplaceableUnit=7 (No hardware detected f |
| 3   | ;5 ;5 ;A | ;Link Failure - RiLink=5 (No signal detected (link start time-out). ManagedE |
| 4   | ;6 ;6 ;A 3x | ;Link Failure - RiLink=6 (No signal detected (link start time-out). ManagedE |
| 5   | ;1,2,3,4,5,6 ;1,3,5,2,4,6 ;A | ;Hardware Failure Imminent - Subrack=1,Slot=1,PlugInUnit=1 (HDFault, Read se |

1.  Refer to and follow Ericsson CPI "Handling SFP Modules and Optical Cables" for proper handling, Cle

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**Description of the fields in the graphical view**

- - each box represents a FieldReplaceableUnit (MSRBS) or PlugInUnit/AuxPlugInUnit (RBS/ERBS). Inside each box are the MO id, the board type, and the link handler. On the side of each box are the CPRI port names. On the bottom of each RU box are the RF ports and corresponding sector/cells.
    - each line represents a CPRI connection. On the CPRI connection are listed:
        - the ID number from the CPRI tables described above. Next to it is the RiLink number when applicable (MSRBS/ERBS).
        - the link type (E/O) and bit rate (eg: O25 = Optical 2.5 GB/s).
        - the length expressed in meters (considering delay of 5 ns per meter), when applicable (MSRBS/ERBS).
        - the test result: OK (green), NOK (red), OKW (purple), NT (blue).

+---------+ +----------+

| | A O25 D1 | 2 |

| |-----1/1-----| RRUS11B4 |

| | OK-181m | BXP_0 |

| | +----------+

| | |A |B

| 1 | SE=1 FDD=1

| DUS3201 |

| 000100 | +-----------+

| | B O25 D1 | 3 |

| |-----2/2-----| RRUS11B13 |

| | OKW-180m | BXP_1 |

| | +-----------+

| | |A |B

+---------+ SE=2 FDD=2

**4.2.5 stc\[p\]\[r\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\]**

Display state and configuration of Atm/Tdm CrossConnections.

The filter allows to only show the rows matching the filter string. The stateFilter allows to only shows the MOs matching the state filter.

The first time the command is run, it takes a bit longer because the data has to be fetched from the node before parsing. The following times the command is run, the existing data is parsed again, unless the r switch is used (_refresh_), in which case, the data is fetched again and parsed.

The first field is the MO id of the Atm/Tdm CrossConnection.

The second field is the state information, consists of five digits:

- 1st digit: _operationalState_ of the Atm/Tdm CrossConnection MO (0=disabled, 1=enabled)
- 2nd and 3rd digits: _operationalState_ of the VclTp MOs (A and B side).
- 4th and 5th digits: only applicable if "p" option was used. Shows the status of the **pget** on VclTp MOs (A and B side). Set to 0 if the transmittedCells counter has incremented but the receivedCells counter has not incremented within a given time period (by default 25 seconds, can be changed in the uservariable pm_wait): this indicates that there is no response from the remote end.

The third and fourth field are the MoId for VclTpA and VclTpB, abbreviated in the following way: AtmPortId/VplTpId/VclTpId

The fifth and sixth fields are the actual Vpi/Vci value for VclTpA and VclTpB. Can be useful in case the MoId of the VclTp does not match the Vpi/Vci value.

The seventh and eigth fields are the MoId for the traffic descriptor of VclTpA and VclTpB.

The last field is the _userLabel_ of the AtmCrossConnection MO.

Note: in the case of TdmCrossConnections, the third and fourth fields show the Timeslot in the Ds0Bundles A and B. The fifth and sixth fields show the Moid of the Ds0Bundle A and B.

**Examples:**

1.  stc 2051 - show all crossconnections where the information matches "2051" (in the case below, where the atmport is 2051)
2.  stc .\* 0 - show all crossconnections that are not working properly.

Printout format, AtmCrossConnection:

\=========================================================================================================================

CCId CSSPP VclTpA VclTpB Vp/VcA Vp/VcB TD-A TD-B UserLabel

\=========================================================================================================================

|     |     |     |     |
| --- | --- | --- | --- |
| MGTS44500_MSC6_AAL2a | 11110 2041.\*1.\*501 2071.\*1.\*501 | 1/501 | 1/501 C2P12000 C2P12000 MGTS44500_MSC6_AAL2a |
| MGTS44500_MSC6_AAL2b | 11111 2041.\*1.\*502 2071.\*1.\*502 | 1/502 | 1/502 C2P12000 C2P12000 MGTS44500_MSC6_AAL2b |
| SOLVER44800_MSC6_AAL2a | 10101 2051.\*1.\*136 2071.\*3.\*512 | 1/136 | 3/512 C2P12000 C2P12000 SOLVER44800_MSC6_AAL2a |
| MGTS45600_MSC9_AAL2a | 11100 2052.\*1.\*300 2041.\*1.\*300 | 1/300 | 1/300 U2P3520M3520 U2P3520M3520 MGTS45600_MSC9_AAL2a |

Printout format, TdmCrossConnection:

\=========================================================================================================================

CCId CSS TSA TSB Ds0A Ds0B UserLabel

\=========================================================================================================================

1192_1191_ts16 101 1 1 1,Slot=27.\*E1.\*=1277,Ds0.\*=127702 1,Slot=27.\*E1.\*=1276,Ds0.\*=127602 TS 16 127702_port1191

**4.2.6 std\[ar\] \[&lt;filter&gt;\]**

Display state and configuration of devices (RNC and MGW only).

Argument (optional):

Only lines matching the filter will be displayed. If no argument, all lines are displayed. Example:

- std fax - show fax devices (mgw)
- std pdr - show pdr devices (rnc)
- std 0020 - show devices on board 0020

**Options:**

- r: to refresh the printout. In MGW the device data is locally cached and updated when the "r" option is given. This is the same behavious as in commands such as bo, stc, stt, stv, inv, etc. In RNC, the "r" option forces moshell to re-check the device to module relationship. All other data is refreshed each time, even without the "r" option.
- a: to fetch some additional device usage information.

### std on MGW

The first table (only printed with option a) shows the DSP SW and usage for each MSB board. The GMD field indicates the status of the GRA-GPB ("G"), the MSB ("M") and DSPs ("D"). The GRA-GPB and MSB status correspond to the state of the corresponding PlugInUnit: L=locked, 1=enabled, 0=disabled. The DSP status is found from the command pingdsp on MSB3 and mmpp pingdp on MSB4. The DSP SW is found from the command rev on MSB3 and mmpp dspc devt on MSB4. The DeviceType and all remaining fields are found from the command gradsl on GRA-GPB:

- Set = DevSetNr : device set id
- ResId = resourceId
- nRes = nrOfResources : total nr of allocated resources for this device set
- nIdle = nrOfIdle : nr resources not in use
- graCap = graRdCapacity : available capacity expressed in PUs available for normal calls
- dspCap = dspRdCapacity : rdScaledCapacity (reported by DSP and used by MFD only) is available devices expressed as remaining PUs
- totCap = rdCapacityTot : total capacity expressed in PUs (reported by RD in attachCfm)
- rej = nrTimeoutRej : number of rejected requests because of 30+30ms + 1 sec DSP supervision timer timeout. At this point DSP is marked as failed
- nRest = nrGraOrderedDspRestarts : number of GRA ordered DSP restarts because of 30+30ms + 1+10 sec DSP supervision timer timeout
- dupCep = nrOfDupCeps : current number of duplicated CEPs in this RD

More info found in gradsl printout description in M-MGw Traffic Control Troubleshooting Guideline 25/1553-AXM 101 01/7

\======================================================================================================================================

Sr Slot Lnh Board GRA DSP GMD DeviceType SW Set ResId nRes nIdle graCap dspCap totCap rej nRest dupCep

\======================================================================================================================================

3 7 730700 MSB3 7304 1 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 2 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 3 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 4 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 5 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 6 111 MPC CXC1327801/8_R3D01 326 11088 24 24 55542 55542 55542 0 0 0

3 7 730700 MSB3 7303 7 111 IM CXC1327799/8_R3E01 327 100 100

3 7 730700 MSB3 7304 8 111 CSD_GSM_MFH CXC1327794/8_R3D01 328 11112 36 36 55650 55650 55650 0 0 0

3 7 730700 MSB3 7304 9 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 10 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 11 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 12 111 UMTS_MFD CXC1327790/8_R3L01 325 9594 166 166 57300 57300 57300 0 0 0

3 7 730700 MSB3 7304 13 111 CSD_DIGITAL CXC1327791/8_R3D01 329 11148 16 16 55650 55650 55650 0 0 0

3 7 730700 MSB3 7304 14 111 CSD_DIGITAL CXC1327791/8_R3D01 329 11148 16 16 55650 55650 55650 0 0 0

3 7 730700 MSB3 7304 15 111 CSD_MODEM CXC1327792/8_R3D01 330 11180 16 16 55650 55650 55650 0 0 0

3 7 730700 MSB3 7304 16 111 CSD_FAX CXC1720519/8_R3D02 331 11196 5 5 55650 55650 55650 0 0 0

The second table shows the device status and availability for each MSB board.

The MD field indicates the status of the MSB ("M") and DSPs ("D").

The MSB status corresponds to the state of the corresponding PlugInUnit: L=locked, 1=enabled, 0=disabled.

The DSP status is found from the command pingdsp on MSB3 and mmpp pingdp on MSB4. If all DSPs are ALIVE, the state is

1, otherwise it is 0.

The remaining fields are read from the action getBoardDetails on MsDeviceGroup:

- nDev = nrOfRds : The number of Root Devices (RD) on the board, configured with the same devices (set of services) as pointed out by the deviceType attribute.
- %Lock = capacityDependencyLockedDev : The fraction (
- %Dis = capacityDisabledDev : The fraction (
- maxDev = maxNrOfDev : A theoretical maximum number of configured devices on the board.

More info in MOM "mom dev getboarddetails".

\===========================================================================================

Sr Slot Lnh Board MD SwAllocation DeviceType nDev %Lock %Dis maxDev

\===========================================================================================

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| 3 7 730700 MSB3 | 11 MGW_MSB3_Profile_16 CSDDigital | 2   | 0 0 | 32  |
| 3 7 730700 MSB3 | 11 MGW_MSB3_Profile_16 CSDGSMFH | 1   | 0 0 | 36  |

The third table shows the device status and availability for each device pool.

In MGW R2/R3, the usage is given as a number, in MGW R4, it is given as a percentage.

\======================================================================

DevPool Total %Idle %Busy %Failed %DepLock %DepFail

\======================================================================

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| CSDDigitalPool | 256 | 100 | 0   | 0   | 0   | 0   |
| CSDGSMFHPool | 288 | 100 | 0   | 0   | 0   | 0   |
| CSDModemPool | 128 | 100 | 0   | 0   | 0   | 0   |

### std on RNC

Shows the configuration, status and usage of RNC devices, CC, DC, PDR.

State information is abbreviated in the following way:

- 1 = unlocked enabled
- 0 = unlocked disabled
- L = locked (enabled or disabled)
- I = idle (the device is not handling calls)
- A = active (the device is handling calls)
- B = busy (the device is fully used and cannot handle more calls)

**Options:**

- r: re-read the device configuration information. Without r, only device state and usage is updated.
- a: show additional device information relating to the device usage. Note: the use of this option means the moshell will run the command drh_dcrh_topdata all which may cause module restart on certain RNC SW releases, see TR WRNae26272. If the RNC is running a SW release containing the correction of TR WRNae26272, then it is safe to run stda. Otherwise, just run std without the a option.

The correction for this TR is included in RNC SW P6.1.4 (CXP9012842_R3BD) and P7.0.1 (CXP9012995_R6CF).

**Printout description for device tables:**

Note: some of the fields are only shown when running option a (stda).

**Common fields:**

- The MOD and GPB column show the module MP controlling the device.
- The SPM and DEV columns show the MO id of the Spm and Device MOs.
- The G column shows the state of the module MP (GPB).
- The D column shows the state of the Device MO.
- The S column shows the state of the Spm MO.
- The U column shows the usageState of the Device MO.

**CC device specific fields:**

\--------------------------------------------------------------------------------------

TYP MOD GPB SPB SPM DEV GDS U LNH CPU UEs Cells(DRH/CCS/max)

\--------------------------------------------------------------------------------------

CC 4 ES1-15 SPB21 ES1-10-1 ES1-10-1 111 A 011000/sp0.lnh 18% 5 52 52 96

....

- CPU shows the CPU load of the Device and is read from the variable spCpuLoad in the drh_ccrh_topdata printout in module MP.
- UEs shows the number of UEs handled by the device and is read from the uelist printout in CC SP.
- Cells/DRH shows the number of Cells handled by the device and is read from the drh_ccrh_topdata printout in module MP.
- Cells/CCS also shows the number of Cells handled by the device but it is read from the celllist command in CC SP.
- Cells/max shows the maximum number of Cells supported by the device (shown on RNC >= P7) The two values

Cells/DRH and Cells/CCS should always be the same, otherwise it indicates a discrepancy between DRH and CCS.

**DC device specific fields:**

\-------------------------------------------------------------------------------------------------------

TYP MOD GPB SPB SPM DEV GDS U LNH CPU Res HsUEs UEsDcs UEsDch UEsDrh gbrResourcePoints

\-------------------------------------------------------------------------------------------------------

DC 1 MS-14 SPB21 MS-19-5 3 111 A 001900/sp4.lnh 26% 10% 14 22 15/150 16/150 530/5100 DC 1 MS-14 SPB21 MS-20-3 4 111 A 002000/sp2.lnh 34% 11% 23 22 21/150 23/150 540/5100

....

- CPU is read from the variable cpuLoad in the drh_dcrh_topdata printout in module MP.
- Res is the percentage of resourcePoints used out of maxResourcePoints (read from drh_dcrh_topdata all)
- UEsDcs is read from the uelist printout in DC SP.
- the following columns are read from the drh_dcrh_topdata all printout in module MP: HsUEs–>noOfHsCapableUes,

UEsDch–>noOfUesOnDch/maxNoOfUesOnDch, UEsDrh–>noOfUesOnDch/maxNoOfUesOnDch, gbrResourcePoints–>gbrResourcePoints/maxResourcePoints.

**PDR device specific fields:**

\-------------------------------------------------------------------------------------------------------

TYP MOD GPB SPB SPM DEV GDS U LNH CPU UEs RABs aal5 usedCapacity

\-------------------------------------------------------------------------------------------------------

PDR 1 MS-14 SPB21 MS-19-1 MS-19-1 111 A 001900/sp0.lnh 3.7% 55 406 95 3796/215000

...

- CPU is read from the command spp -p xxxx00/spx.lnh sp procload 1 on central MP or capi prio and capi core 0 on PDR devices (depending on RNC SW release)
- UEs is read from the uelist printout in PDR SP.
- RABs and aal5 correspond to the variables noOfRabs and noOfAal5Conns in the drh_pdrrh printout in module MP.
- usedCapacity is read from usedCapacity/maxCapacity in drh_pdrrh in module MP.

**Module summary table:**

These table show the device usage on module basis.

The fields are the same as in the tables above except for the DC summary table which contains some additional fields, read from the printout lh mod drh_trbr_data:

- ATM: noOfAtmTrBr
- IP: noOfAtmToIpTrBr
- BEE: noOfBeesTrBr

Also in the CC summary table, the field "max" is replaced by the field "GPB" which indicates the number of cells that are handled by the GPB of that RncModule. The field "GPB" is read via the attributes IubLink::rncModuleRef and IubLink::reservedBy

**SPB summary table:**

In this table we get an overview of all the SPB boards, their device states, usage, and module allocation.

The State column shows first the state of the SPB PlugInUnit, then the state and usage of its devices.

The Module column shows which module is handling each device.

\--------------------------------------------------------------------------------

Sr Slot Lnh Board SwAlloc Type State Usage Module

\--------------------------------------------------------------------------------

MS 19 001900 SPB21 SPB_TYPE_A PCDDD 1-11111 AAAAA 1 1 13 8 8

**4.2.7 stv\[b\]\[r\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\]**

Display state, user, and bandwidth usage for ATM ports and channels.

**Options:**

- b: to get the bandwidth usage for AtmPorts. Requires running some COLI commands.
- r: to refresh the data (ie. re-read from node).

**Arguments:**

- the first argument matches on the whole line
- the second argument matches only the state field ("VU")

**Examples:**

- stvb ms-6-1 print ATM data for AtmPort=MS-6-1 and all VPs/VCs underneath it
- stv p4500 print ATM data for all VPs/VCs using a traffic descriptor with peak cell rate 4500 • stv . 0|L print all Ports/VPs/VCs with state disabled or locked

Printout format:

- The field ResrvBw/TraffDesc shows:
    - - the AtmTrafficDescriptor for VclTp MOs. For VC’s used by Aal2Path, the Aal2 QoS is shown in brackets.
        - the reserved bandwidth (in cells/s) for AtmPort and VplTp MOs. E.g. 353000/353207 means 353000 cells/s reserved out of 353207 available. The available bandwidth for AtmPort is obtained from the COLI command aet_atmmp etatmportfro &lt;fro&gt; and is only shown when option b is specified. The reserved bandwidth for

VplTp is obtained from the traffic descriptor of VplTp (total bandwidth) and the sum of the traffic descriptors of VclTp (used bandwidth). The cellrate used by a traffic descriptor is the PeakCellRate in case of CBR and the MinimumCellRate for UBR/UBR+.

- The field User shows the MO using the VclTp. For Aal2PathVccTp MOs, the information in brackets shows the aal2PathId and reserving Aal2Ap. For PacketDataRouter MOs, the information in brackets shows the PdrDevice position, the Aal5TpVccTp MOid, the rncIpAddress, and the cnIuLinkIpAddress. For Mtp3bSl MOs, the information in brackets shows the SignallingLinkCode (SLC), the linkState, the proceduralState, and the usageState, same as in stt printout. Refer to stt help for more info about the Mtp3bSl information.
- The field M shows the RncModule handing the User.
- The field VU shows the state of the VP/VC followed by the state of the User. L=locked, 0=disabled, 1=enabled. E.g. VU=10 means that the VclTp is enabled but the User MO is disabled. For Aal2PathVccTp MOs, there is an extra digit which represents the remoteBlockingState (0=remotely_blocked, 1=remotely_unblocked, ?=undefined). Note that the remoteBlockingState is not shown when the Aal2PathVccTp is locked. For PacketDataRouter MOs, there is an extra digit which represents the state of the PdrDevice MO.

Example printout:

\======================================================================================================================

VclTp VPI/VCI ResrvBw/TraffDesc VU M User

\======================================================================================================================

|     |     |     |     |
| --- | --- | --- | --- |
| AtmPort=MS-6-1 | /   | 1   | \--------------------------------------- |
| AtmPort=MS-6-1,VplTp=1 | 2 224000/353000 | 1   | \--------------------------------------- |
| AtmPort=MS-6-1,VplTp=1,.\*VclTp=vc34 | 2/34 U3P4500M3000 | 11  | Mtp3bSpItu=Iu1,Mtp3bSls=Iuc-1-2300-3,Mtp3bSlItu=1 |
| AtmPort=MS-6-1,VplTp=1,.\*VclTp=vc50 | 2/50 U3P4500M3000 | 11  | Mtp3bSpItu=Iu1,Mtp3bSls=Iup-2-2810-3,Mtp3bSlItu=1 |
| AtmPort=MS-6-1,VplTp=1,.\*VclTp=vc90 | 2/90 C2P12000(AB) | 111 | 1 Aal2PathVccTp=Iu1-1-1 (1, Aal2Ap=Iu1) |
| AtmPort=MS-6-1,VplTp=1,.\*VclTp=vc91 ...&lt;cut&gt;... | 2/91 C2P12000(AB) | 111 | 1 Aal2PathVccTp=Iu1-1-2 (2, Aal2Ap=Iu1) |
| AtmPort=MS-6-1,VplTp=1,.\*VclTp=Pdr1Gtpu1 | 2/230 U3P66600M5000 | 11  | RncModule=1,PacketDataRouter=Pdr1Gtpu1 |
| AtmPort=MS-6-1,VplTp=1,.\*VclTp=Pdr1Gtpu2 | 2/231 U3P66600M5000 | 11  | RncModule=1,PacketDataRouter=Pdr1Gtpu2 |
| AtmPort=MS-26-1 | /   | 1   | \--------------------------------------- |
| AtmPort=MS-26-1,VplTp=1 | 1 13804/14650 | 1   | \--------------------------------------- |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc34 | 1/34 C1P5 | 11  | 1 IubLink=1,NodeSynchTp=1 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc35 | 1/35 C1P5 | 11  | 1 IubLink=1,NodeSynchTp=2 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc36 | 1/36 U3P1000M80 | 11  | 1 IubLink=1,NbapCommon=1 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc37 | 1/37 U3P1000M80 | 11  | 1 IubLink=1,NbapDedicated=1 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc38 | 1/38 U3P1000M80 | 11  | 1 Aal2Sp=1,Aal2Ap=Iub1 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc39 | 1/39 C2P6657(AB) | 111 | 1 Aal2PathVccTp=Iub1-1 (101, Aal2Ap=Iub1) |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc40 | 1/40 C2P6657(AB) | 110 | 1 Aal2PathVccTp=Iub1-2 (102, Aal2Ap=Iub1) |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc43 | 1/43 U3P1000M80 | 11  | 1 IubLink=1,NbapCommon=1 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc44 | 1/44 U3P1000M80 | 11  | 1 IubLink=1,NbapDedicated=1 |
| AtmPort=MS-26-1,VplTp=1,.\*VclTp=vc45 ...&lt;cut&gt;... | 1/45 U3P1000M80 | 11  | 1 Aal2Sp=1,Aal2Ap=Iub1 |

**4.2.8 stt\[r\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\]**

Purpose: Display state and user of Physical Ports and Ds0Bundles.

**Options:**

- r : to refresh the data (ie. re-read from node).

**Arguments:**

- the first argument matches on the whole line
- the second argument matches only the state field ("PUI")

**Examples:**

- stt ms-26-1 print all ports and their users matching ms-26-1
- stt . 0|L print all ports and their users who have state disabled or locked
- stt mtp3 busy print all mtp3 links that are in usage state busy
- stt mtp3 deact print all mtp3 links that are in linkstate deactivated

Printout format:

- PUI : the first digit represents the state of the PhysicalPort/Ds0Bundle. The second digit (if present) represents the state of the User. The third digit (if present) represents the state of the intermediate layer which can be IMA (when user is AtmPort) or MTP2 (when user is Mtp3bSl). L=locked, 1=enabled, 0=disabled.
- CG/KLM: circuit group and K.L.M (for channelised STM-1)
- SLC/PCM: SignallingLinkCode for Mtp3bSl or pcmSystemNr for TdmTermGrp
- User : the layer that is using the physical port. Usually an AtmPort in Utran nodes. Can also be a TdmTermGrp or an Mtp3bSl in MGW. In case of Mtp3bSl, the linkState, proceduralState, and usageState are also shown.

Example printout RXI:

\======================================================================================================================

Port CG/KLM PUI USER

\======================================================================================================================

|     |     |     |
| --- | --- | --- |
| Subrack=MS,Slot=7,..\*,Os155SpiTtp=pp1,Vc4Ttp=1 ... |     | 11 AtmPort=MS-7-1 |
| Subrack=MS,Slot=24,.\*,Os155SpiTtp=pp1,Sts1SpeTtp=1,Vt15Ttp=1,T1Ttp=1 | 1/1.1.1 | 11 AtmPort=MS-24-1-1-1 |
| Subrack=MS,Slot=24,.\*,Os155SpiTtp=pp1,Sts1SpeTtp=1,Vt15Ttp=2,T1Ttp=1 | 1/1.1.2 | 111 AtmPort=MS-24-ima1 |
| Subrack=MS,Slot=24,.\*,Os155SpiTtp=pp1,Sts1SpeTtp=1,Vt15Ttp=3,T1Ttp=1 | 1/1.1.3 | 111 AtmPort=MS-24-ima1 |

Example printout MGW:

\======================================================================================================================

Port CG/KLM SLC/PCM PUI USER

\======================================================================================================================

|     |     |
| --- | --- |
| 2,Slot=25,.\*,E1PhysPathTerm=2251,Ds0.\*=22511 | 1 LL TdmTermGrp=E1_MSC3_Slot25_Port1_TS1-29_31 |
| 2,Slot=25,.\*,E1PhysPathTerm=2252,Ds0.\*=22521 | 2 1L TdmTermGrp=E1_MSC3_Slot25_Port2_TS1-29_31 |
| 2,Slot=25,.\*,E1PhysPathTerm=2253,Ds0.\*=22531 | 3 11 TdmTermGrp=E1_MSC3_Slot25_Port3_TS1-29_31 |
| 2,Slot=25,.\*,E1PhysPathTerm=2253,Ds0.\*=22532 | 0 111 Mtp3bSpItu=2.\*Sls=msc3.\*SlItu=msc3_0 (available,initialized,active) |
| 2,Slot=25,.\*,E1PhysPathTerm=2254,Ds0.\*=22541 | 4 11 TdmTermGrp=E1_MSC3_Slot25_Port4_TS1-29_31 |

**4.2.9 sta\[rc\] \[&lt;Filter&gt;\]**

Print configuration and status of SctpAssociations in MSRBS.

**Limitations:**

- currently does not show TermPoints using IPSec

**Options:**

- r : refresh the data locally cached in the moshell session.
- c : display the printout in CSV format

**Argument:**

- The argument allows to only show the lines matching the filter string. Negative filter is supported by putting a exclamation mark in front of the filter. See examples further down.

**Printout example:**

- EP: the SctpEndPoint, parent of the SctpAssociation MO
- LocalIP, Port: the SctpAssociation attributes localPrimaryAddress and localPortNumber
- RemoteIP, Port: the SctpAssociation attributes remotePrimaryAddress and remotePortNumber
- S: the SctpAssociation attribute associationState
- T: the state of the TermPoint MO (L=locked, 1=unlocked&enabled, 0=disabled, D=degraded)
- Redundancy: the SctpAccociation attribute redundancyStatus
- Sec: the SctpAccociation attribute associationSecurityState
- UsedBy: the MO using this SctpAssociation, whose state is shown in the "T" field

\=============================================================================================================================================================================

EP LocalIP Port RemoteIP Port ST Redundancy Sec UsedBy

\=============================================================================================================================================================================

NBAP-C 10.236.102.150 5113 10.16.7.119 1 11 RED_NOT_POSS UNSEC Iub=1,NbapCommon=1

NBAP-D 10.236.102.150 5114 10.16.7.119 2 11 RED_NOT_POSS UNSEC Iub=1,NbapDedicated=1

1 10.255.197.157 36422 10.51.97.5 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,EUtraN.\*=1,Ext.\*ENodeBF.\*=302720-411727,TermPointToENB=302720-411727

1 10.255.197.157 36422 10.51.97.9 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,EUtraN.\*=1,Ext.\*ENodeBF.\*=302720-411728,TermPointToENB=302720-411728

1 10.255.197.157 36422 10.246.32.1 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=302720-00000000003830453,TermPointToGNB=302720-00000000003830453

1 10.255.197.157 36422 10.246.33.9 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=C56AAX,TermPointToGNB=1

1 10.255.197.157 36422 10.246.34.1 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=C57AAX,TermPointToGNB=1

1 10.255.197.157 36422 10.246.34.5 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=C69GX,TermPointToGNB=1

1 10.255.197.157 36422 10.246.34.9 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=302720-00000000003830795,TermPointToGNB=302720-00000000003830795

1 10.255.197.157 36422 10.246.41.9 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=C12AX,TermPointToGNB=302720-00000000003830460

1 10.255.197.157 36422 10.246.42.1 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,GUtraN.\*=1,Ext.\*GNodeBF.\*=302720-00000000003831574,TermPointToGNB=302720-00000000003831574

1 10.255.197.157 36422 10.51.96.17 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,EUtraN.\*=1,Ext.\*ENodeBF.\*=302720-411656,TermPointToENB=302720-411656

1 10.255.197.157 36422 10.51.96.21 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,EUtraN.\*=1,Ext.\*ENodeBF.\*=302720-410109,TermPointToENB=302720-410109

1 10.255.197.157 36422 10.51.96.29 36422 11 RED_NOT_POSS UNSEC ENodeBF.\*=1,EUtraN.\*=1,Ext.\*ENodeBF.\*=302720-411659,TermPointToENB=302720-411659

**4.2.10 ste\[gr\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\]**

Purpose: Display state and configuration of Ethernet Ports.

**Options:**

- r: to refresh the data (clear cache and re-read from node).
- g: to print the RSTP tree in graphical format.

**Arguments:**

- the first argument matches on the whole line.
- the second argument matches only the state field ("S12" or "STL")

Command examples:

- ste !nolink : show all lines except those containing the word "nolink"
- ste . 0|L : show all lines containing a resource whose state is disabled or locked
- ste forwarding : show all lines containing the word "forwarding"

**Printout format, first table:** This tables shows the properties for ethernet ports where IP distribution is performed, ie, where IpInterfaces are defined. Each line corresponds to a GigabitEthernet MO (ETIPG/ETMFG) or a InternalEthernetPort MO (ETMFX). Each column corresponds to an attribute of these MOs. Refer to the MOM for more detail on each attribute.

- Position: the subrack, slot, and port number - GigaBitEthernet::portNo or 0 for InternalEthernetPort
- Speed: GigaBitEthernet::actualSpeedDuplex
- Conf: GigaBitEthernet::configuredSpeedDuplex
- AutoNg: GigaBitEthernet::autoNegotiation
- Mastr: GigaBitEthernet::masterMode
- Prot: GigaBitEthernet::protectiveMode
- DfRSw: GigaBitEthernet::defRoutersLinkSwitch
- S: GigaBitEthernet::administrativeState&operationalState (0=unlocked&disabled, 1=unlocked&enabled, L=locked) • 1: GigaBitEthernet::link1State
- 2: GigaBitEthernet::link2State. Note: this attribute is not applicable on EPB and will be shown as -.
- ActiveLink: GigaBitEthernet::activeLink
- Link: GigaBitEthernet::linkType
- Frame: GigaBitEthernet::frameFormat or InternalEthernetPort::frameFormat
- Vlans: the list of vlan ids for all IpInterfaces defined on that port (read from attribute vid or vlanRef on the children IpInterface MOs). A vlan id value of -1 means that vlan is not used on that port ("vlan=false")
- DscpPbitMap: GigaBitEthernet::dscpPbitMap or InternalEthernetPort::dscpPbitMap (only the pbit values are listed) Example:

\====================================================================================================================================

Board Position Speed Conf AutNg Mastr Prot DfRSw S12 ActiveLink Link Frame Vlans DscpPbitMap

\====================================================================================================================================

MFG MS-06-1 1G_F 1G_F true true true false 111 1 (PRIMARY) FRONT 2DIX 20 0000000000101010003030300040404000505050000000600000000000000000

MFG MS-07-1 1G_F 1G_F true true true false 111 1 (PRIMARY) FRONT 2DIX 20 0000000000101010003030300040404000505050000000600000000000000000

MFX12 MS-24-0 2DIX 19 0000000000101010003030300040404000505050000000600000000000000000

MFX12 MS-25-0 2DIX 19 0000000000101010003030300040404000505050000000600000000000000000

\====================================================================================================================================

**Printout format, second table:** Each line corresponds to a EthernetSwitch or EthernetSwitchPort MO (ETMFX), or a EthernetSwitchModule or EthernetSwitchModulePort MO (CMXB), or a EthernetBridgePort (CMXB/CCIB in CAX subrack), as well as the corresponding children MOs SwitchStp/SwitchPortStp. Each column corresponds to an attribute of these MOs. Refer to the MOM for more detail on each attribute.

- Position: the subrack, slot, and port number:
    - 0: EthernetSwitch(Module)
    - 1-7: EthernetSwitchPort::portNo
    - 1-8: EthernetSwitchModulePort::portNo
- Lag: The position of the port specified in masterPort of the connected Lag MO, when applicable.
- lagSp: Lag::aggregatedPortSpeed, the speed of the Lag
- Remote: SwitchStp::rootBridgeId or SwitchPortStp::remoteBridgeId -> if the Bridge Id is pointing to a switch inside the node, the MAC address of the remoteBridge/rootBridge will be translated into the position of the switch. If the MAC address is not found within the node but pointing to an outside switch, then the MAC address given in the remoteBridgeId will be printed.
- Speed: EthernetSwitch(Module)Port/EthernetPort::actualSpeedDuplex
- Conf: EthernetSwitch(Module)Port/EthernetPort::operatingMode:configuredSpeedDuplex
- AutoNg: EthernetSwitch(Module)Port/EthernetPort::operatingMode:autoNegotiation

Sys/Ext: EthernetSwitchPort::systemPort or EthernetSwitchModulePort::externalPort or EthernetBridgePort::externalPort

- S: EthernetSwitch(Module)Port/EthernetPort::administrativeState&operationalState (0=unlocked&disabled, 1=unlocked&enabled, L=locked)
- T: EthernetSwitch(Module)Port/EthernetPort::trafficState
- L: Lag:administrativeState&operationalState. Only applicable when the Port(s) are part of a Lag MO.
- Prio: SwitchStp::bridgePriority or SwitchPortStp::priority
- Cost: SwitchPortStp::actualPathCost
- RtCost: SwitchPortStp::rootPathCost
- Role-State: SwitchPortStp::stpRole and SwitchPortStp::stpState
- Edge: SwitchPortStp::edgePortMode
- PbitQMap: EthernetSwitch(Module)(Port)::pbitQueueMap
- UnIng: EthernetSwitchPort::untaggedIngressVid&untaggedIngressPriority or

EthernetSwitchModulePort::untaggedIngressVlanRef&untaggedIngressPriority. Shows the vid and priority that will be assigned to untagged ingress frames.

- Vlans: EthernetSwitchPort::vlanMembership or EthernetSwitchModulePort::vlanRef&egressUntagVlanRef. Shows the list of vlan ids supported by the port. Vlans on which egress frames will be untagged will be marked with a "U", eg "23U" means that vlan id 23 will be untagged on egress.

Example, ETMFX:

\=============================================================================================================================================

Board Position Remote Speed Conf AutNg Sys STL Prio Cost RtCost Role-State Edge PbitQMap UnIng Vlans

\=============================================================================================================================================

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| MFX12 | MS-24-0 ES4-26 | 1   | 32768 | BRIDGE 10112233 101:0 0,101 |     |
| MFX12 | MS-24-1 MS-25 1G_F 1G_F true | false 1 | 128 | 20000 100000 ROOT-FORWARDING EDGE_OFF 10112233 1:0 | 0,101 |
| MFX12 | MS-24-2 NOLINK 1G_F true | false L | 128 | 200000000 0 UNKNOWN-DISCARDING EDGE_OFF 10112233 1:0 | 0   |
| MFX12 | MS-24-3 NOLINK 1G_F true | false L | 128 | 200000000 0 UNKNOWN-DISCARDING EDGE_OFF 10112233 1:0 | 0   |
| MFX12 | MS-24-4 NOLINK 1G_F true | false L | 128 | 200000000 0 UNKNOWN-DISCARDING EDGE_OFF 10112233 1:0 | 0   |
| MFX12 | MS-24-5 ES1-03 1G_F 1G_F true | false 1 | 128 | 20000 100000 ALTERNATE-DISCARDING EDGE_OFF 10112233 1:0 | 0,101 |
| MFX12 | MS-24-6 MS-24 1G_F 1G_F true | true 1 | 128 | 20000 100000 DESIGNATED-FORWARDING EDGE_OFF 10112233 1:0 | 0,101 |
| MFX12 .... | MS-24-7 NOLINK 1G_F true | false L | 128 | 200000000 0 UNKNOWN-DISCARDING EDGE_OFF 10112233 1:0 | 0   |

Example, CMXB:

\=============================================================================================================================================

Board Position Remote Speed Conf AutNg Ext STL Prio Cost RtCost Role-State Edge PbitQMap UnIng Vlans

\=============================================================================================================================================

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CMXB | MS-03-0 MS-03 |     | 1   | 0   |     | BRIDGE |     |
| CMXB | MS-03-1 MS-03 | 1G_F 1G_F false | false 1 | 128 | 20000 0 | DESIGNATED-FORWARDING BPDU_FILTER 10234567 1:0 | 3005 |
| CMXB | MS-03-2 MS-03 | 10G_F 10G_F false | false 1 | 128 | 2000 0 | DESIGNATED-FORWARDING EDGE_OFF 10234567 1:0 | 1480,1481,2001,3005 |
| CMXB | MS-03-3 MS-03 | 10G_F 10G_F false | false 1 | 128 | 2000 0 | DESIGNATED-FORWARDING EDGE_OFF 10234567 1:0 | 1480,2001,3005 |
| CMXB | MS-03-4 MS-03 | 10G_F 10G_F false | false 1 | 128 | 2000 0 | DESIGNATED-FORWARDING EDGE_OFF 10234567 1:0 | 1480,2001,3005 |
| CMXB | MS-03-5 MS-03 | 1G_F 1G_F false | true 1 | 128 | 20000 0 | DESIGNATED-FORWARDING BPDU_FILTER 10234567 1:0 | 1480,1481 |
| CMXB | MS-03-6 | NOLINK 10G_F false | false L | 128 | 2000 0 | UNKNOWN-DISCARDING EDGE_OFF 10234567 1:0 |     |
| CMXB | MS-03-7 | NOLINK 10G_F false | false L | 128 | 2000 0 | UNKNOWN-DISCARDING EDGE_OFF 10234567 1:0 |     |
| CMXB ..... | MS-03-8 | NOLINK 10G_F false | true L | 128 | 2000 0 | UNKNOWN-DISCARDING EDGE_OFF 10234567 1:0 |     |

**Printout format, option g:**

- Box with double-line border is the identified root bridge in the RSTP domain
- stpState is marked in the middle of a line with "S" (DIS=DISABLED, BLO=BLOCKING, LIS=LISTENING, DSC=DISCARDING, LEA=LEARNING, FWD=FORWARDING, UNK=UNKNOWN)
- stpRole is marked in the middle of a line with "R" (R=ROOT, D=DESIGNATED, A=ALTERNATE, B=BACKUP, U=UNKNOWN)
- The arrow head (&lt; or &gt;) in the end of a line is the side where it is actually possible to determine which port that has the relationship to the board where the line originates
- The x is drawn on the side of the port where it is discarding
- Only one link per LAG will be drawn (thicker), label will include port numbers of all links in the group
- Bridge priority (P) is shown inside of a bridge
- rootPathCost (PC) is shown for each link Example, RNC3820:

0~~~~~~~~~~~~0

S NETWORK S

+---------------->S S<----------------+

| 0~~~~~~~~~~~~0 |

| |

| |

| Port 1, PC=0 Port 1, PC=2000 |

| R=D, S=FWD R=D, S=FWD |

| |

#============# +------------+

+---->H MS-03 H Port 2, PC=2000, R=R, S=FWD | MS-26 |<----+

| +-->H P=8192 H<----------------------------------| P=16384 |<--+ |

| | #============# +------------+ | |

| | | |

| | | |

| | Port 1, PC=2000 Port 1, PC=4000 | |

| | R=R, S=FWD R=R, S=FWD | |

| | | |

| | +------------+ +------------+ | |

| +---| ES1-03 | Port 2, PC=4000, R=A, S=DSC | ES1-26 |---+ |

|     |     |     |
| --- | --- | --- |
| \|  | \| P=32768 \|<---------------------------------x\| P=32768 \| | \|  |
| \|  | +------------+ +------------+ | \|  |
| \|  |     | \|  |
| \|  |     | \|  |

| Port 1, PC=2000 Port 1, PC=4000 |

| R=R, S=FWD R=R, S=FWD |

| |

| +------------+ +------------+ |

+-----| ES2-03 | Port 2, PC=4000, R=A, S=DSC | ES2-26 |-----+

| P=32768 |<---------------------------------x| P=32768 |

+------------+ +------------+

**4.2.11 sti\[bcfopr\] \[&lt;Filter&gt;\] \[&lt;stateFilter&gt;\]**

Purpose: Display state and configuration of IP interfaces.

The printout consists of up to 7 tables:

- the IpInterfaces table, one line per IpInterface MO.
- the IpAccessHostEt table, one line per IpAccessHostEt MO.
- the IpAccessHostGpb/Spb table, one line per IpAccessHostGpb or IpAccessHostSpb MO.
- the IpAccessHostPool table, one line per IpAccessHostEt MO part of an IpAccessHostPool (applicable to RNC and MGW only).
- the IpEthPacketDataRouter table, one line per IpEthPacketDataRouter MO (applicable to RNC38xx only).
- the M3uA table, one line per M3uAssociation MO (applicable to RNC and MGW only).
- the Iub/S1/X2 table, one line per MO of type IubLink,Iub,TemPointToMMe,TermPointToENB (applicable to RNC/RBS/ERBS only).

**Options:**

- p: ping the remote destinations (printout will take more time to complete)
- r: to refresh the data (clear cache and re-read from node).
- f: only show the IpInterface/IpAccessHost overview table. Without this option, all tables are shown.
- o: show the IpAccessHost froIds in the above tables.
- b: only show the Iub/S1/X2 signalling interfaces (in RNC/RBS/ERBS). Without this option, all tables are shown.
- c: only show the Core signalling interfaces (in RNC/MGW: SIGTRAN). Without this option, all tables are shown.

**Arguments:**

- the first argument matches on the whole line
- the second argument matches only the state field ("GS12MUP" or "GS12ISP" or "IRP")

**Printout format, IpInterfaces table:**

Each line corresponds to a IpInterface MO. Each column corresponds to an attribute of these MOs. Refer to the MOM for more detail on each attribute.

- Board: The type of ET board on which the IpInterface is located (ETIPG, ETMFG, ETMFX)

Interface: the subrack and slot of the ET board, followed by a sequential number to distinguish between numerous IpInterfaces defined on the same board.

- Vid: the vlan ID, read from the attribute IpInterface::vid or IpInterface:vlanRef
- Subnet: the value of the attributes IpInterface::subnet and IpInterface::networkPrefixLength
- DefaultRouter: the number in brackets shows which is the active defaultRouter according to the attribute

IpInterface::defaultRouterTraffic. Also shown is the ip addess of the active default router, read from the attribute IpInterface::defaultRouterX (where X is 0, 1, or 2)

- rps: the value of IpInterface::rps
- I: the value of IpInterface::operationalState (0=disabled, 1=enabled)
- R: the value of IpInterface::defaultRouterXState (where X is 0, 1, or 2). Only applicable when rps=true, otherwise a "-" is shown.
- P: the ping status to the active defaultRouter (0=unreachable, 1=alive)
- H: the state of each IpAccessHost connected to this IpInterface.
- IpHosts: the list of IP hosts connected to this IpInterface. G=IpAccessHostGpb, Et=IpAccessHostEt, S=IpAccessHostSpb. For each IpAccessHost, the location of the host is shown, not the MO name. To see the mapping of the host location vs MO name, check the following two tables. In brackets next to IpAccessHostEt is shown the IpAccessHostPool using this host, when applicable.

\=======================================================================================================================

Board Interface Vid Subnet DefaultRouter Rps IRP HHH IpHosts

\=======================================================================================================================

|     |     |     |
| --- | --- | --- |
| IPG | MS-04-1 | 632 10.164.233.64/29 (0) 10.164.233.70 false 1-1 1 G=MS-5-1 |
| IPG | MS-04-2 | 652 10.164.233.0/26 (0) 10.164.233.61 true 111 111 S=MS-10-2 S=MS-23-1 S=MS-9-1 |
| IPG | MS-04-3 | 662 10.164.233.128/26 (0) 10.164.233.188 false 1-1 1 Et=MS-04-3 (IuB) |
| IPG | MS-04-4 | 682 10.164.233.96/27 (0) 10.164.233.125 true 111 1 Et=MS-04-4 (IuR) |
| IPG | MS-04-5 | 2001 192.168.101.0/24 (0) 192.168.101.1 false 1-1 1 Et=MS-04-5 (intraNode) |

**Printout format, IpAccessHostEt table:**

Each line corresponds to a IpAccessHostEt MO. Description of the columns:

- ET: The type of ET board on which the IpAccessHostEt is located (ETIPG, ETMFG, ETMFX)
- Host: the subrack and slot of the ET board, followed by a sequential number to distinguish between numerous IpAccessHostEt defined on the same board.
- MOName: the name of the IpAccessHostEt MO.
- Lnh: the linkhander address of the ET board. Needed in order to run the EtHostMo_startPing/EtHostMo_startTraceRoute command.
- Ntp: the value of attribute ntpDscp. Only shown when ntpServerMode is enabled on this host. If ntpServerMode is disabled then a dash is shown instead.
- Fro: the froId of the IpAccessHostEt. Needed in order to run the EtHostMo_startPing/EtHostMo_startTraceRoute command. Only shown with option o.
- HostIp: the IP address of the IpAccessHostEt.
- Vid: the vlan ID of the IpInterface connected to this IpAccessHostEt.
- H: the state of the IpAccessHostEt (L=locked, 1=enabled, 0=disabled).
- IRP: the state of the IpInterface MO connected to this IpAccessHostEt. See description in table above.
- IpAccessHostPool/IpAcccessSctp: the list of MOs using this host, first the Pools are listed, then the IpAccessSctp. For the IpAccessSctp, it shows the position of the GPB on which the SCTP is located, not the MO name.

\=======================================================================================================================

ET Host MOName Lnh Ntp Fro HostIp Vid HIRP IpAccessHostPool/IpAccessSctp

\=======================================================================================================================

|     |     |     |     |
| --- | --- | --- | --- |
| IPG | Et=MS-04-2 MS-4-1 | 000400 - | 1 192.168.101.4 2001 11-1 intraNode |
| IPG | Et=MS-04-3 MS-4-3 | 000400 49 | 2 10.212.48.5 700 11-1 Iub MS-06,MS-08,MS-12,MS-16 |
| IPG | Et=MS-04-4 MS-4-2 | 000400 - | 3 10.202.212.3 812 1111 Iu_Iur |
| IPG | Et=MS-25-2 MS-25-1 | 002500 - | 4 192.168.101.25 2001 11-1 intraNode |
| IPG | Et=MS-25-3 MS-25-3 | 002500 49 | 5 10.212.48.6 700 11-1 Iub MS-06,MS-08,MS-12,MS-16 |

**Printout format, IpAccessHostGpb/Spb table:**

Each line corresponds to a IpAccessHostGpb/Spb MO. Description of the columns:

- Host: the subrack and slot of the GPB/SPB where the IP host is located.
- Board: the type of board where the IP host is located.
- MOName: the name of the IpAccessHostGpb/Spb MO.

HostIp1/2: the IP addresses of the IP Host.

- Interface1/2: the position of the IpInterfaces connected to the IP Host.
- Vid1/Vid2: the vlan ID of the IpInterfaces connected to the IP Host.
- H: the state of the IP Host (L=locked, 1=enabled, 0=disabled).
- IRP1/2: the state of the IpInterfaces connected to the IP Host (see detailed description of the IRP state in first table).

\=======================================================================================================================

Host Board MOName HostIp1 HostIp2 Interface1 Interface2 Vid1 Vid2 H IRP1 IRP2

\=======================================================================================================================

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| G=MS-08 GPB53 MS-8 10.159.22.2 10.159.22.18 MS-26-2 | MS-27-2 | 929 | 929 | 1 1-1 1-1 |
| G=ES1-12 GPB53 ES-1-12 10.212.0.27 10.212.0.28 ES1-03-1 | ES1-26-1 | 100 | 100 | 1 1-1 1-1 |
| G=ES1-13 GPB53 ES-1-13 10.212.0.29 10.212.0.30 ES1-03-1 | ES1-26-1 | 100 | 100 | 1 1-1 1-1 |
| S=MS-19 SPB3 MS-19 10.159.18.7 10.159.18.8 MS-26-3 | MS-27-3 | 945 | 945 | 1 111 111 |
| S=MS-20 SPB3 MS-20 10.159.18.9 10.159.18.10 MS-26-3 | MS-27-3 | 945 | 945 | 1 111 111 |
| S=MS-21 SPB3 MS-21 10.159.18.11 10.159.18.12 MS-26-3 | MS-27-3 | 945 | 945 | 1 111 111 |

**Printout format, IpAccessHostPool table (RNC/MGW):**

Each line corresponds to a IpAccessHostEt MO used by an IpAccessHostPool. Each column corresponds to an attribute of these MOs.

- Pool: the name of the IpAccessHostPool
- HostEt: the position (Subrack-Slot) of the IpAccessHostEt MO, followed by a sequential number to distinguish between numerous IpAccessHostEt defined on the same board.
- HostIp: the attribute IpAccessHostEt::ipAddress
- ET: the board type (ETIPG, ETMFG, or ETMFX)
- Vid: the vlan ID of the IpInterface connected to this IpAccessHostEt.
- P: the state of the IpAccessHostPool MO (L=locked, 1=unlocked&enabled, 0=unlocked&disabled)
- H: the state of the IpAccessHostEt MO
- I: the state of the IpInterface MO connected to this IpAccessHostEt, same as shown in the first table
- R: the state of the active defaultRouter, same as shown in the first table
- P: the ping status to the active defaultRouter, same as shown in the first table
- Users: read from the attribute IpAccessHostPool::reservedBy. Shows "Rnc" if the pool is used by the RncFunction MO (applicable to intraNode/BEES pool), else shows the number of IubLinks/IurLinks/IuLinks using this pool.

RNC:

\=======================================================================================================================

Pool HostEt HostIp ET Vid PH IRP Users: Iuc Iur Iub

\=======================================================================================================================

|     |     |     |
| --- | --- | --- |
| IUB | MS-04-3 10.164.233.129 IPG 662 11 1-1 | 0 0 34 |
| IUB | MS-25-3 10.164.233.130 IPG 662 11 1-1 | 0 0 34 |
| IUR | MS-04-4 10.164.233.97 IPG 682 11 111 | 0 24 0 |
| IUR | MS-25-4 10.164.233.98 IPG 682 11 111 | 0 24 0 |
| intraNode | MS-04-5 192.168.101.4 IPG 2001 11 1-1 Rnc | 0 0 0 |
| intraNode | MS-25-5 192.168.101.25 IPG 2001 11 1-1 Rnc | 0 0 0 |

MGW:

\=======================================================================================================================

Pool Type HostEt HostIp ET Vid PH IRP

\=======================================================================================================================

|     |     |     |
| --- | --- | --- |
| A   | A   | MAIN-06-2 10.52.211.10 IPG 1180 11 1- |
| A   | A   | MAIN-14-1 10.52.211.11 IPG 1180 11 1- |
| A   | A   | MAIN-17-1 10.52.211.12 IPG 1180 11 1- |
| A   | A   | MSE1-14-2 10.52.211.13 IPG 1180 11 1- |
| Iu  | IU  | MAIN-06-2 10.52.211.10 IPG 1180 11 1- |
| Iu  | IU  | MAIN-14-1 10.52.211.11 IPG 1180 11 1- |
| Iu  | IU  | MAIN-17-1 10.52.211.12 IPG 1180 11 1- |
| Iu  | IU  | MSE1-14-2 10.52.211.13 IPG 1180 11 1- |

**Printout format, IpEthPacketDataRouter table (RNC):**

Each line corresponds to a IpEthPacketDataRouter MO. Each column corresponds to an attribute of these MOs.

- IpEthPdr: the position (Subrack-Slot) of the PdrDevice, followed by the attribute

IpEthPacketDataRouter::ipAddressSelection. Value 1 means IP_ADDRESS_1, value 2 means IP_ADDRESS_2. Value 11 means that both IpEthPacketDataRouter of that PdrDevice are using IP_ADDRESS_1 while 22 means that both are using IP_ADDRESS_2 (which would mean that all traffic of the PdrDevice is routed to the same IpInterface instead of being load-shared on both IpInterfaces)

- SPB: the board type of the SPB hosting the PdrDevice
- HostSpb: the position of the IpAccessHostSpb connected to this IpEthPacketDataRouter, followed by the number 1 or 2, depending on the value of IpEthPacketDataRouter::ipAddressSelection
- HostIp: the ip address of the IpAccessHostSpb, could be ipaddress 1 or 2, depending on the value of IpEthPacketDataRouter::ipAddressSelection

ET: the board type of the IpInterface connected to this IpAccessHostSpb (ETIPG, ETMFG, or ETMFX)

- Vid: the vlan ID of the IpInterface connected to this IpAccessHostSpb
- E: the state of the IpEthPacketDataRouter MO (L=locked, 0=unlocked&disabled, 1=unlocked&enabled)
- H: the state of the IpAccessHostSpb MO
- U: the value of the usageState of the PdrDevice hosting this IpEthPacketDataRouter (I=Idle, A=Active, B=busy)
- I: the state of the IpInterface MO connected to this IpAccessHostEt, same as shown in the first table
- R: the state of the active defaultRouter, same as shown in the first table
- P: the ping status to the active defaultRouter, same as shown in the first table
- Iup: the value of IpEthPacketDataRouter::reservedBy. Shows which IP-based IuPS links can use this

IpEthPacketDataRouter for userplane connections. When empty, means that it can be used by all IP-based IuPS links.

\=======================================================================================================================

IpEthPdr SPB HostSpb HostIp ET Interface Vid EH U IRP Iup

\=======================================================================================================================

|     |     |
| --- | --- |
| MS-19-1 SPB21 MS-19-1 114.126.135.176 MFG | MS-07-1 2000 11 A 1-1 any |
| MS-19-2 SPB21 MS-19-2 114.126.135.181 MFG | MS-26-1 2000 11 A 1-1 any |
| MS-20-1 SPB21 MS-20-1 114.126.135.177 MFG | MS-07-1 2000 11 A 1-1 any |
| MS-20-2 SPB21 MS-20-2 114.126.135.182 MFG | MS-26-1 2000 11 A 1-1 any |

**Printout format, M3uAssociation table (RNC/MGW):**

Each line corresponds to a M3uAssociation MO. Each column corresponds to an attribute of these MOs.

- the HostGpb column identifies the IpAccessHostGpb MO.
- the Sctp column identifies the Sctp MO
- the M3uA column identifies the M3uAssociation MO. At the beginning of the string is the identity of the parent Mtp3bSp MO, then comes the identity of the M3uAssociation MO. A wildcard (.\*) separates the two identities.
- the Assoc column identifies the sctp association, given by the the gpb position and the association number. The association number can be used in the printout sctphost_info -assoc &lt;assocnumber&gt;.
- the GS12MUP column shows the various states, where: G=IpAccessHostGpb, S=Sctp, 1=IpInterface1, 2=IpInterface2, M=M3uAssociation, U=User, P=ipac_ping (1=alive, 0=notalive). The ping is done only when "sti" is run with the option "p".
- the A column shows the associationState of the M3uAssociation, where: I=inactive, A=active, E=established, D=down.
- the LocalInterface column shows the local interface, can be a IpInterface MO or a FastEthernet MO. In the case of FastEthernet, the letter "f" is appended to the identity as shown in the third line of the printout below. In brackets is indicated whether the chosen interface is interface 1 or interface 2. The association tries to setup on interface 1 but if that fails then it uses interface 2.
- the RemoteInterface column shows which interface is used on the remote side, 1 or 2.
- the LocalIp:Port and RemIp:Port columns show the ipaddress and sctp port of the association, for each side.
- ther User column shows which application part is using this association. Could be GCP (Vmgw), Q.AAL2 (Aal2Ap), RANAP, RNSAP.

Example MGW:

\============================================================================================================================

HostGpb Sctp M3uA Assoc GS12 MUP A LocalInterface,Ip:Port RemInterface,Ip:Port User

\============================================================================================================================

IPACGPB_2_6 Sctp_2_6 2.\*msc2qa 0006:148 1111 111 A (1) 2-19 10.201.0.31:2905 (2) 10.202.10.20:2905 Vmgw=VMGW92

IPACGPB_2_6 Sctp_2_6 2.\*nwp141a 0006:60 1111 111 D (2) 2-20 10.201.10.31:2905 (1) 10.201.12.141:2905 Aal2Sp=1,Aal2Ap=nwp141 SIG12_13 SIG12_13 2.\*nwp206a 0012:5 1111 111 A (1) 1-12f 10.202.0.30:2905 (1) 10.202.2.206:2905 Aal2Sp=1,Aal2Ap=nwp206

Example RNC:

\==================================================================================================================================

HostGpb Sctp M3uA Assoc GS12 MUP A LocalInterface,Ip:Port RemInterface,Ip:Port User

\==================================================================================================================================

MS-8-1 MS-8 Iu.\*mgw7-2521-1720 0008:21 1111 111 A (1) MS-7 10.207.2.121:2905 (1) 10.207.2.245:2905 Aal2Ap=Aal2routing-mgw7-2521-1720

MS-8-1 MS-8 Iu.\*mgw71-2521-1730 0008:4 1111 111 A (1) MS-7 10.207.2.121:2905 (1) 10.207.2.246:2905 Aal2Ap=Aal2routing-mgw71-2521-1730

|     |     |
| --- | --- |
| MS-8-1 MS-8 Iu.\*Iuc-2521-1700 | 0008:18 1111 111 A (1) MS-7 10.207.2.121:2905 (2) 10.207.12.240:2905 Cn.\*=23591,Iu.\*=Iuc-1700,Ranap=Iuc-1700 |
| MS-8-1 MS-8 Iu.\*Iuc-2521-1710 | 0008:2 1111 111 A (1) MS-7 10.207.2.121:2905 (1) 10.207.2.242:2905 Cn.\*=23591,Iu.\*=Iuc-1710,Ranap=Iuc-1710 |
| MS-8-1 MS-8 Iu.\*Iup-2521-2207 | 0008:33 1111 111 A (1) MS-7 10.207.2.121:2905 (2) 10.207.4.1:2905 Cn.\*=23591,Iu.\*=Iup-2207,Ranap=Iup-2207 |
| MS-8-1 MS-8 Iu.\*Iup-2521-2271 | 0008:34 1111 111 A (1) MS-7 10.207.2.121:2905 (2) 10.207.4.17:2905 Cn.\*=23591,Iu.\*=Iup-2271,Ranap=Iup-2271 |
| MS-8-1 MS-8 Iu.\*Iur-2521-2522 | 0008:22 1111 111 A (1) MS-7 10.207.2.121:2905 (2) 10.207.12.122:2905 Iur.\*=Iur-2521-2522,Rnsap=Iur-2521-2522 |

**Printout format, IubLink table (RNC):** This table shows the configuration and status of control plane connections for IP-based IubLinks (for Iub user plane connections refer to the IpAccessHostPool table). Each line corresponds to a IubLink MO in RNC. Each column corresponds to an attribute of these MOs.

- Sctp: the value of IubLink::sctpRef. The position of the GPB hosting this Sctp is shown.
- Mod: the value of IubLink::rncModuleRef.

Host: the value of Sctp::ipAccessHostGpbId or Sctp::ipAccessSctpRef. Shows "Gpb" if IpAccessHostGpb is used or "Et" if IpAccessSctp is used.

- Interf1/Interf2: the position of the IpInterfaces used by the IpAccessHost(s).
- LocalIp1/LocalIp2: the ip addresses of the IpAccessHost(s) used by the Sctp.
- RemoteIp: the value of IubLink::remoteCpIpAddress1
- IubLink: the name of the IubLink MO.
- G: the state of the IpAccessHostGpb or IpAccessSctp used by the Sctp MO (0=locked, 1=unlocked&enabled, 0=unlocked&disabled)
- S: the state of the Sctp MO
- 1: the state of IpInterface 1
- 2: the state of IpInterface 2
- I: the state of the IubLink MO
- S: the state of the NodeSynch MO
- PP: the ping status from each IpInterface to the RemoteIp (0=unreachable, 1=alive). The first "P" corresponds to the ping status from IpInterface 1, the second "P" corresponds to the ping status from IpInterface 2.
- the NbapC_Assoc and NbapD_Assoc fields identify the sctp associations for NbapCommon and NbapDedicated. First number is the local port number, then the remote port number, then the SCTP association reference number according to the printout of sctphost_info -assoc -all. The number in brackets identifies the active IpInterface used for this association.

\=========================================================================================================================================

Sctp Mod Host Interf1 Interf2 LocalIp1 LocalIp2 RemoteIp IubLink GS12 ISPP NbapC_Assoc NbapD_Assoc

\=========================================================================================================================================

MS-14 1 Gpb MS-25-1 MS-26-1 10.100.0.140 10.100.1.140 10.100.2.150 Iub-1 1111 1111 1:5101:30 (1) 2:5102:23 (1)

MS-14 1 Gpb MS-25-1 MS-26-1 10.100.0.140 10.100.1.140 10.100.2.150 Iub-10 1111 1111 1:5119:33 (1) 2:5120:26 (1)

**Printout format, Iub table (RBS):**

- LocalIp: ipaddress of the IpAccessHostGpb or IpAccessHostEt used for Iub control plane
- RemoteIp1/RemoteIp2: ip addresses used on the remote side (RNC) according to the printout of sctphost_info -assoc -all
- G: state of IpAccessHostGpb or IpAccessSctp MO
- S: state of Sctp MO
- I: state of IpInterface MO
- C: state of NbapCommon MO
- D: state of NbapDedicated MO
- P: ping status, one ping for each remoteIp (0=unreachable, 1=alive)
- the NbapC_Assoc and NbapD_Assoc fields identify the sctp associations for NbapCommon and NbapDedicated. First number is the local port number, then the remote port number, then the SCTP association reference number according to the printout of sctphost_info -assoc -all. The number in brackets identifies the active IpInterface used for this association.

\=======================================================================================================================

LocalIp RemoteIp1 RemoteIp2 IubLink GSI CDPP NbapC_Assoc NbapD_Assoc

\=======================================================================================================================

10.2.35.143 10.2.35.16 10.2.35.17 Iub=1 111 1111 5113:1 (2) 5114:2 (1)

\=======================================================================================================================

**Printout format, S1/X2 interfaces in ERBS:**

- T: state of the TermPoint MO
- S: state of the Sctp MO
- H: state of the IpAccessHostEt MO
- P: ping status to the active remote IP address (0=unreachable, 1=alive)
- Assoc: the reference number of the SCTP association according to the printout of sctphost_info -assoc -all
- TermPoint: "ENB" refer to TermPointToENB MO (X2), "Mme" refer TermPointToMME MO (S1).

\=======================================================================================================================

LocalIp:Port RemoteIp:Port StandbyRemoteIp TSHP Assoc TermPoint

\=======================================================================================================================

10.62.11.34:36422 10.62.11.33:36422 10.62.11.34 1111 71 ENB=104023

10.62.11.34:36422 10.64.193.81:36412 10.62.11.82 1111 68 Mme=MME010064193081

10.62.11.34:36422 10.64.193.91:36412 10.62.11.92 1111 70 Mme=MME010064193091

\=======================================================================================================================

**4.2.12 sts\[c\]**

Purpose: Display state and configuration of Network Synchronization.

The printout is read from the Synchronization MO on CPP nodes and all children MOs of Synchronization/Ntp/Ptp on COM nodes.

The c option is to print the output in CSV format.

### Printout format CPP

The first line corresponds to the value of the attribute nodeSystemClock. If the node is part of a Node Group Synchronization cluster then the next line will indicate the node group role (provider or receiver). The remaining lines correspond to the values of the attributes syncReference, syncRefPriority, syncRefActivity, syncRefStatus.

**Examples:**

RNC01> sts

SystemClock: LOCKED_MODE

\-------------------------------------------------------------------------------------

Prio Activity RefState AdmState OpState SyncReference

\-------------------------------------------------------------------------------------

|     |     |     |     |
| --- | --- | --- | --- |
| 1   | ACTIVE OK | UNLOCKED ENABLED | Subrack=MS,Slot=4,PlugInUnit=1,TimingUnit=1,TuSyncRef=1 |
| 2   | INACTIVE OK | UNLOCKED ENABLED | Subrack=ES-2,Slot=2,PlugInUnit=1,ExchangeTerminal=1,Os155 |
| 3   | INACTIVE OK | UNLOCKED ENABLED | Subrack=ES-2,Slot=27,PlugInUnit=1,ExchangeTerminal=1,Os15 |
| 4   | INACTIVE OK | UNLOCKED ENABLED | Subrack=ES-3,Slot=2,PlugInUnit=1,ExchangeTerminal=1,Os155 |
| 5   | INACTIVE OK | UNLOCKED ENABLED | Subrack=ES-3,Slot=27,PlugInUnit=1,ExchangeTerminal=1,Os15 |

|     |     |     |     |
| --- | --- | --- | --- |
| \*1 | 1 SYNC_E NO_FAULT | PRC | Synchronization=1,SyncEthInput=TN_B (SFP_OPTICAL Ethern |
| 2   | 1 FREQUENCY_PORT NO_FAULT | PRC | Synchronization=1,FrequencySyncIO=1 (FREQUENCY_1PPS Fiel |

RBS14> sts

SystemClock: HOLD_OVER_MODE

\-------------------------------------------------------------------------------------

Prio Activity RefState AdmState OpState SyncReference

\-------------------------------------------------------------------------------------

1 INACTIVE FAILED UNLOCKED DISABLED IpAccessHostEt=1,IpSyncRef=1 2 INACTIVE FAILED UNLOCKED DISABLED IpAccessHostEt=1,IpSyncRef=2

### Printout format MSRBS

The first line indicates the clock state in RadioEquipmentClock MO If the node is part of a Node Group Synchronization cluster then the next line will indicate the node group role (provider or receiver). The table shows the attributes of each

RadioEquipmentClockReference MO. The priority is marked with an asterisk to indicated the active Reference. The MO referred by the "encapsulation" attribute is shown on the right together with some of its attributes, in brackets.

**Examples:**

MSRBS1> sts

radioClockState : FREQUENCY_LOCKED

\-------------------------------------------------------------------------------------

Prio ST syncRefType refStatus opQualLevel SyncReference

\-------------------------------------------------------------------------------------

MSRBS2> sts

radioClockState : FREQUENCY_LOCKED

\-------------------------------------------------------------------------------------

Prio ST syncRefType refStatus opQualLevel SyncReference

\-------------------------------------------------------------------------------------

2 0 NTP_FREQUENCY NTP_FAULT QL_UNKNOWN Ntp=1,NtpFrequencySync=1 (192.168.250.101:32751 Router=OA \*3 1 PTP_FREQUENCY NO_FAULT PRC Ptp=1,BoundaryOrdinaryClock=PTP_FREQUENCY (G_8265_1 Rout

1.  1 PTP_FREQUENCY NO_FAULT PRC Ptp=1,BoundaryOrdinaryClock=PTP_FREQUENCY_IPV6 (G_8265_1
2.  1 GNSS_RECEIVER NO_FAULT GNSS Synchronization=1,TimeSyncIO=GPS (FieldReplaceableUnit=1,

7 1 PTP_TIME PTP_FAULT QL_UNKNOWN Ptp=1,BoundaryOrdinaryClock=PTP_TIME (IEEE_1588_J3 Ethern

**4.2.13 str**

Print status of the IubLinks/AbisLinks and their associated Cells and Channels (RNC/BSC only).

The command has two syntaxes, depending on the type of node.

**CDMA BSC: str \[ | &lt;unix-cmds&gt;\]**

\------------------------------------------------------------------

SITE C1 C2 C3 ABIS BACKHAUL ATMPORTS

\------------------------------------------------------------------

96 11 11 11 11 RBS1_Backhaul BHRBS1_Backhaul_BHSBackhaulSpan_1

\------------------------------------------------------------------

The states of the channels are shown for each cell, as well as the states of the **AbisCommon** and **AbisDedicated**.

The MO-id of the **BackHaul** and the **AtmPort**s are also shown for each site.

State abbreviation: L means Locked, 0 means Disabled, and 1 means Enabled.

**UTRAN RNC: str\[123ft\] \[&lt;csvfile&gt;\] \[&lt;filter-options&gt;\] \[ | &lt;unix-cmds&gt;\]**

To see the state of all or part of the cells/iubs/channels in the node, one line per site.

The filter options (-m, -s, -i, -c, -g, -t, -r) allow to get states on only part of the sites/cells, in order to speed up the output. For example:

- str -m 7,8,9 - print states only for modules 7, 8, and 9
- str -s ms,es-1 - print states only for subracks ms and es-1
- str -i 9012 - print states only for the MO Iublink=9012 and its connected cells
- str -c 90121,90131 - print states only for the Iublink MOs connected to the MO UtranCell=90121 and UtranCell=90131
- str -g clusterNorth - print states only for the Iublinks defined in the MO group "clusterNorth"
- str -t a - print states only for ATM-based iublinks
- str -t i - print states only for IP-based iublinks
- str -t ai - print states for dual stack iublinks
- str -r 9345 - print states for IubLinks connected to RSite=9345

There are five possible output formats:

The str printout uses an abbreviated naming of the cells where it is assumed that the last digit is identifying the sector. For networks where the sector is not identified by the last digit, it can be handy to use str1 or str2 since the whole cell name will then be shown for each sector.

The strt command shows the AtmPorts used by each site.

The str3 command shows cell status in a compressed format in order to fit 12 cells per line, see further down for details.

- str

\-----------------------------------------------------------------------------------------------

MOD IUBLINK CELLNAME CFRPHEU1 CFRPHEU2 CFRPHEU3 ICDS TN R

\-----------------------------------------------------------------------------------------------

1 Iub_3011 3011-1/2/3 1111111 L000000 1000000 1111 I P

\-----------------------------------------------------------------------------------------------

• strt

\-----------------------------------------------------------------------------------------------

MOD IUBLINK CELLNAME CFRPHEU1 CFRPHEU2 CFRPHEU3 ICDS TN TNPORTS

\-----------------------------------------------------------------------------------------------

1 Iub_3011 3011-1/2/3 1111111 L000000 1000000 1111 AI MS-25-1 MS-26-1

8 Iub_3012 3012-1/2/3 1111111 1111111 1111111 1111 I MS-23 MS-24

\-----------------------------------------------------------------------------------------------

• str1

\-----------------------------------------------------------------------------------------------

MOD IUBLINK CELLNAMES CFRPHEU1 CFRPHEU2 CFRPHEU3 ICDS

\-----------------------------------------------------------------------------------------------

1 Iub_3011 30111 30112 30113 1111111 L000000 1000000 1111

\-----------------------------------------------------------------------------------------------

• str2

\----------------------------------------------------------------------------------------

MOD IUBLINK ICDS CELL1 CFRPHEU CELL2 CFRPHEU CELL3 CFRPHEU

\----------------------------------------------------------------------------------------

1 Iub_3011 1111 30111 1111111 30112 1111111 30113 1111111

\----------------------------------------------------------------------------------------

- str3

\-----------------------------------------------------------------------

IUBLINK MOD TN R ICDS C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12

\-----------------------------------------------------------------------

Iub-1523 1111 I P 1111 111 111 111 11 11 111

Iub-1526 1161 A N 1111 111 1 111 111 111 111

\-----------------------------------------------------------------------

- **MOD**: The RNC module that is handling the control plane for this Iub, corresponds to the attribute IubLink::rncModuleRef
- **IUBLINK**: The MO name of the IubLink
- **CELLNAME**: The name of the cells that are connected to that IubLink. The cell names correspond to the respective sectors. Eg: 6306-1/2/3 means that: cell 63061 is connected to sector 1, cell 63062 is connected to sector 2, cell 63063 is connected to sector 3.
- **CFRPHEU**: The first digit is the state of the UtranCell MO. The following three digits are the state of the common channels (Fach/Rach/Pch). The fifth digit (if present) represents the state of the hsdpa channel (Hsdsch). The sixth digit (if present) represents the state of the enhanced uplink channel (Eul). The seventh digit (if present) represents the state of the EulFach channel (EulFach).
- **ICDS**: The first digit is the state of the IubLink. The second digit is the state of NbapCommon MO or SctpAssociation MO handling Nbap Common. The third digit is the state of NbapDedicated MO or SctpAssociation MO handling Nbap Dedicated. The fourth digit is the state of NodeSynch MO.
- **TN**: The type of transport network used by the IubLink. A=ATM, I=IP, AI=DualStack
- **R**: The Iub/Geo redundancy configuration of the IubLink, read from the attribute IubLink::poolRedundancy.
    - - N=No Redundancy
        - Iub Redundancy feature: P=Primary, S=Secondary
        - Geo Redundancy feature: G=Primary, A=SecondaryActive, I=SecondaryInactive
- **TNPORTS**: The Subrack and Slot of the ETIP (in case of IP Iub) or ATMPORT (in case ATM or DualStack Iub)
- **CXX**: A compressed cell status consisting of up to 3 digits per cell (XX is a number from 01 to 12):
    - - 1st digit is the combined state of UtranCell+Fach+Rach+Pch: if all four are up then it shows 1. If one or more are locked it will show "L", "T", "S", or "U" depending on the type of lock (see below). If one or more are disabled then it shows 0.
        - 2nd digit is the state of HsDsch.
        - 3rd digit is the combined state of Eul+EulFach (same rule applied as for 1st digit).

States values:

- **L** \= Locked
- **S** \= ShuttingDown
- **T** \= TPS power Locked (corresponds to the attribute tpsPowerLockState)
- **U** \= TPS power ShuttingDown
- **0** \= Unlocked & Disabled
- **1** \= Unlocked & Enabled

The output can be piped in external unix commands such as grep.

If a filename is given as argument, the output will be saved into this file in csv format (as well as being printed on the screen).

The _f_ option (_fast_) is for printing without fetching the data. I.e. the data can be fetched once, then displayed in many different ways without having to fetch it again each time.

**Examples:**

strf | grep 3011

str1f | sort -k 2 (sort on the second field)

**4.2.14 dcg\[meiabsrfkx\] \[-m &lt;rophours&gt;\] \[-e &lt;eventrophours&gt;\] \[-d &lt;logdays&gt;\] \[-b &lt;boards|boardgroup&gt;|all\] \[-r &lt;mogroup&gt;\] \[-k &lt;nrdumps&gt;|&lt;esiGranularity&gt;\] \[-f &lt;mofilter&gt;\] \[-t &lt;seconds&gt;\] \[-t1 &lt;seconds&gt;\] \[-c &lt;collector-profile&gt;\] \[-de &lt;ddb-enddate&gt;\] \[-d1 &lt;manualddb-minusdays&gt;\] \[-d2 &lt;periodicddb-minusdays&gt;\] \[&lt;logdir&gt;\]**

Fetch data for TRs/CSRs, according to the Data Collection Guidelines.

The dcg command offers a number of options, it is possible to combine several options, eg: "dcgmsr"

**Options for CPP nodes:**

- m: mandatory data. Includes modump, logfiles, pm ropfiles, CV’s, coli printouts.
- e: emergency data. Subset of the mandatory data which can be taken in case of emergency, before doing board/node restart. This option will usually be run on its own.
- i: IP printouts
- a: ATM/AAL2 printouts. By default only the AAL2 printouts are collected. To collect ATM printouts, use option "-b", see below.
- s: SS7 printouts
- x: SPAS printouts
- r: RNC specific printouts.
- f: fetch logfiles, ropfiles, and CV. Three zipfiles are produced which can be used in offline mode in pmr, pmx, lg, and dbc. Refer to the chapter "Offline mode" for more info.
- k: take a MO dump (kget format). A zipfile is produced containing the MO dump and MOM of the node, it can be used in offline mode by running "moshell &lt;zipfile&gt;". Refer to the chapter "Offline mode" for more info.

**Options for COM nodes:**

- m: mandatory data. Includes modump, logfiles, pm ropfiles, coli printouts, and large ESI (RCS nodes).

By default dcgm collects a large ESI.

To get a small ESI, use dcge or the option -k 0, eg dcgm -k 0.

To get a static ESI, use the option -k -1 (static=small without callbacks, useful in case small ESI failed).

- e: emergency data. Same as m but with small ESI instead of large.
- f: fetch logfiles and ropfiles. Two zipfiles are produced which can be used in offline mode in pmr, pmx, and lg. Refer to the chapter "Offline mode" for more info.
- k: take a MO dump (kget format). A zipfile is produced containing the MO dump and MOM of the node, it can be used in offline mode by running "moshell &lt;zipfile&gt;". Refer to the chapter "Offline mode" for more info.
- b: collect all Backups and store in a zipfile.

**Options for YANG nodes:**

- k: take a MO dump (kget format) from one or multiple nodes within the same session.
- m: mandatory data. Includes modump, DDB, ESI, and pm ropfiles. Currently supported only in single-node session.

Use option -c &lt;collector-profile-name&gt; to specify the colletor-profile to use for the DDB export. If unspecified, the collector-profile HelmChartValues is used as default.

The export will be done via the sftp-server specified in the collector-profile. The list of sftp-servers and corresponding passwords must be specified in the uservariables yang_sftp_servers and yang_sftp_passwords respectively. See example in the file moshell/moshell .

By default, the dcgm will contain a manual DDB for the last 3 hours. This can be changed via options "-de &lt;ddb-enddate&gt;" and/or "-d1 &lt;manualddb-minusdays&gt;".

Example: to collect a 12 hour manual DDB up until today, use option "-d1 12h". To collect a 6 hour manual DDB up until 20230831.0800 UTC, use option "-de 20230831.0800 -d1 12h".

If periodic DDC is enabled (data-collector::administrative-state==unlocked), the periodic DDB files from the last 2 days will be included in the dcgm. This can be changed via options "-de &lt;ddb-enddate&gt;" and/or "-d2 &lt;manualddb-minusdays&gt;"

Example: to collect a 36 hr periodic DDB up until today, use option "-d2 36h". To collect a 2 day periodic DDB up until

20230831.0800 in timezone UTC-6 use option "-de 20230831.0800-0600 -d2 2"

Example: to collect a 6 hour manual DDB and a 1 day periodic DDB, both up until 20230831.0800 UTC+2, use options: "-de 20230831.0800+0200 -d1 6h -d2 2"

**Switches:**

- \-m &lt;rophours&gt;: the number of hours of ROP files to collect with pmrf, eg "-m 2". Default is 8 hours in dcge and 48 hours in dcgm/dcgf.
- \-e &lt;eventrophours&gt;: the number of hours of Event ROP files to collect with pmef, eg "-e 2". Default is 2 hours in dcge and 12 hours in dcgm/dcgf.
- \-d &lt;logdays&gt; : the number of days of logfiles to collect with lgf, eg "-d 30". Default is 60 days in dcgm/dcgf. Note: to specify hours or minutes, use "h" or "m", eg "-d 2h" to collect the last 2 hours.
- \-b &lt;boards|boardgroup&gt;|all : the ET boards on which dcgi/dcga will be run. When this option is not specified, dcga collects no ET board data, while dcgi collects all ET boards data. Example: dcgi -b 000600,000700
- \-k &lt;nrdumps&gt; : the number of ENB DSP dumps to collect on CPP nodes, or the ESI granularity on RCS nodes: 1=large, 0=small, -1=static, -2=refresh, -101=sp1. Corresponds to the option -d in lg command. Default: 1 in dcgm, 0 in dcge.

If option -k -1 is specified on CPP nodes then the DCG proxy collection will be skipped (action DataCollection.runDcg()).

If option -k -2 is specified on RNC nodes then the COLI printouts will not be collected via SSH, only via the DCG proxy.

- \-f &lt;mofilter&gt;: the MO filter for MO dump collection. Eg "-f !relation=" to skip MOs such as UtranRelation/GsmRelation in the MO dump.
- \-t &lt;seconds&gt; : the maximum time (in seconds) allowed for the dcgm to complete. Default is 1800 seconds for RBS/ENB, 3600 seconds for RNC, and 2700 seconds for MSRBS.
- \-t1 &lt;seconds&gt;: the duration time for execution of "mft 11". Default: 300 seconds.
- \-r &lt;mogroup&gt; : the mogroup (created by "ma" command) containing a list of Cells/SectorCarriers/FieldReplaceableUnit MOs whose logs shall be included in the ESI and the RU/XMU COLI printouts. Only applicable for MSRBS.
- \-c &lt;collector-profilename&gt; : only applicable for YANG nodes. To specify the collector-profile to use in the collect-ddb action. Default: HelmChartValues
- \-de &lt;ddb-enddate&gt;: only applicable for YANG nodes. To specify the end date for the manual and periodic DDB collection (e.g. the time around when the fault occurred). Default: today’s date. Must be written in the below format: YYYYmmdd.HHMM\[TZ\]. The timezone is optional. If not given, UTC will be used. Example: 20230831.0800+0200 => means 08:00 in UTC+2 , i.e. 06:00 in UTC.
- \-d1 &lt;manualddb-minusdays&gt;: only applicable for YANG nodes. To specify the number of days to collect prior to the end date. Eg: "-d1 2" => 2 days. "-d1 6h" => 6 hours. "-d1 30m" => 30 minutes.
- \-d2 &lt;periodicddb-minusdays&gt;: same as above but for the periodic DDB.

**Argument:**

- the directory where the collected data will be stored. If no directory is given, the directory ~/moshell_logfiles/logs_moshell/dcg/&lt;node&gt;/&lt;date&gt;\_&lt;time&gt; is used.

**Notes:**

- A zipfile is produced, containing all the data collected by the dcg command. For dcgm/dcge, the name of the zipfile indicates the UP of the node as well as the timestamp when the dcg was collected. By default the timestamp is written in the local time of the workstation unless the uservariable dcg_name_utc is set to 1, in which case the timestamp will be in UTC.
- Please refer to the command file in moshell/commonjars/scripts/dcg_datacollection.mos to view the various commands that are run for each option. More info about each command can be found by typing h &lt;command&gt;
- For CPP nodes, if the MO layer is unavailable, it is possible to run dcg anyway by typing uv nocorba=1 before executing dcg. Using nocorba=1 means that moshell will not attempt to connect to the MO service and will only run commands via telnet/ftp/ssh/sftp.

**4.2.15 stz\[rc01\] \[&lt;Filter&gt;\]**

Print configuration and status of cells in MSRBS/ERBS.

bf Limitations:

- the fields "D", F", "Ess", and "Fru" are not available for ERBS.
- only LTE and NR cells are currently supported. GSM/WCDMA planned for a future release.

**Options:**

r : refresh the data locally cached in the moshell session.

- c : display the printout in CSV format
- 0 : only display cells that are unlocked and enabled, without alarm and without any active "TABREMDF" flags • 1 : only display cells that are not matching the above conditions

**Argument:**

- The argument allows to only show the lines matching the filter string. Negative filter is supported by putting a exclamation mark in front of the filter. See examples further down.

**Printout example:**

- LTECell/NRCell: the cell name. FDD=EUtranCellFDD, TDD=EUtranCellTDD, NIOT=NbIotCell, NRC=NRCellDU
- S: the combined state of the cell, explained directly in the printout, see example below.
- Alm: the Id(s) of any alarm(s) issued by the cell, the SectorCarrier, the SectorEquipment, or the FieldReplaceableUnit.
- TABREMDF: map showing various cell/sector settings, explained directly in the printout, see example below.
- UEs: the number of active UEs connnected in the cell. Read from coli printouts "ue print -admitted" (LTE) and "ue list –cell" (NR)
- cId, nci, tac, pci, rsi: EUtranCellFDD:cellId or NRCellDU:cellLocalId, NRCellDU:nCI, EUtranCellXDD:tac or NRCellDU:nRTac, EUtranCellXDD:physicalLayerCellId or NRCellDU:nRPCI, rachRootSequence
- freqDL/UL: cell frequency in MHz
- dlBw, ulBW: expressed in MHz, corresponds to EUtranCellxDD:xlChannelBandwidth or NRSectorCarrier:bSChannelBwDL/UL
- Band: EUtranCellxDD:freqBand
- cnfP, maxP: expressed in Watts , corresponds to (NR)SectorCarrier:configuredMaxTxPower , (NR)SectorCarrier:maximumTransmissionPower
- C-T/R: the number of configured TX/RX antennas, read from attributes (NR)SectorCarrier:noOfTx/RxAntennas
- U-T/R: the number of used TX/RX antennas, read from attributes (NR)SectorCarrier:noOfTx/RxAntennas
- M-T: the number of muted TX antennas, read from attribute SectorCarrier:noOfMutedTxAntennas
- Ess: the Id of the paired LTE/NR cell. The Id can be looked up in the first column of the other Cell table
- Fru: the Id(s) of the FRU(s) hosting this cell. The Id can be looked up in the first table where all FRUs are listed.An asterisk (\*) at the end of the FRU productName indicates that the radio is shared with an external ManagedElement.
- NRCellCU: the NRCellCU that has same nci as the NRCellDU , its combined state, its localCellId, and number of connected UEs.

S=administrativeState&operationalState&availabilityStatus (1=unlocked&enabled, 0=unlocked&disabled, L=locked, D=degraded)

D=FieldReplaceableUnit.deepSleepStatus ("D" Deep sleeping, "-" not sleeping)

T=OnSiteActivities.technicianPresent ("T" Technician is present, "-" not present)

B=PowerSaving.bbPowerSavingStatus ("B" BB Power Saving, "-" not power saving)

R=PowerSaving.ranCompDeepSleepStatus ("R" RanCompute deep sleeping, "-" not sleeping)

\=============================================================================================================================================================================

Id FRU S DTBR FAULT OPER MAINT ProductName

\=============================================================================================================================================================================

|     |     |     |     |
| --- | --- | --- | --- |
| 0 BB-1 1 ---- | OFF | ON  | OFF Baseband6630 |
| 1 RRU-1 D - | OFF | ON  | OFF RRU4449B71B85A |
| 2 RRU-16 1 - | OFF | ON  | OFF RRU4478B5\* |
| 3 RRU-17 1 - | OFF | ON  | OFF RRU4478B5\* |
| 4 RRU-18 1 - | OFF | ON  | OFF RRU4478B5\* |
| 5 RRU-2 1 - | OFF | ON  | OFF RRU4449B71B85A |
| 6 RRU-3 1 - | OFF | ON  | OFF RRU4449B71B85A |

\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\=============================================================================================================================================================================

Id Alarm

\=============================================================================================================================================================================

1.  Service Degraded - EUtranCellFDD=C77AXX (AI: S:15->13)
2.  Service Degraded - NRCellDU=C77AN1 (AI: S:14->13)
3.  VSWR Over Threshold - FieldReplaceableUnit=RRU-1,RfPort=B (ReturnLoss 0.3 dB, VSWR 57.9, Sensitivity 49%, Fault on DL FrequencyRange 617000 - 652000 kHz AI: P:13->14,15)

\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

S=administrativeState&operationalState&availabilityStatus (1=unlocked&enabled, 0=unlocked&disabled, L=locked, D=degraded)

T=dlPowerState ("I" invalid, "C" changing, "-" stable or not-applicable, eg when CXC4012260.serviceState=INOPERABLE)

A=ailgActive ("A" active, "-" not active)

B=cellBarred ("B" barred, "-" not barred)

R=primaryPlmnReserved ("R" reserved, "-" not reserved or not-applicable, eg when CXC4010960.serviceState=OPERABLE or CXC4012479.serviceState=OPERABLE)

E=CellSleepFunction.sleepState ("S" sleeping, "-" not sleeping)

M=MimoSleepFunction.sleepState ("M" sleeping, "-" not sleeping)

D=FRU.deepSleepStatus ("-" not sleeping, "D" deep sleeping)

F=FRU.maintenanceIndicator ("F" ongoing maintenance, "-" no ongoing maintenance)

\=============================================================================================================================================================================

Id LTECell S TABREMDF Alm UEs cId tac pci rsi arfcnDL arfcnUL freqDL freqUL dlBW ulBW Band cnfP maxP C-T/R U-T/R M-T Ess Fru

\=============================================================================================================================================================================

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 FDD=C77AXA 1 -------- | 3   | 0 10 33333 435 695 |     | 5070 | 23070 735 705 |     |     | 10  | 10  | 12  | 40  | 40  | 2/4 | 2/4 | 0   | \-  | 1   |
| 2 FDD=C77AXB 1 -------- | \-  | 0 11 33333 443 705 |     | 5070 | 23070 735 705 |     |     | 10  | 10  | 12  | 40  | 40  | 2/4 | 2/4 | 0   | \-  | 5   |
| 3 FDD=C77AXC 1 -------- | \-  | 11 12 33333 451 715 |     | 5070 | 23070 735 705 |     |     | 10  | 10  | 12  | 40  | 40  | 2/4 | 2/4 | 0   | \-  | 6   |
| 4 FDD=C77AXG 1 -------- | \-  | 2 16 33333 435 105 |     | 2436 | 20436 872.6 827.6 |     |     | 5   | 5   | 5   | 26  | 26  | 2/4 | 2/4 | 0   | \-  | 2   |
| 5 FDD=C77AXH 1 -------- | \-  | 1 17 33333 443 95 |     | 2436 | 20436 872.6 827.6 |     |     | 5   | 5   | 5   | 25  | 25  | 2/4 | 2/4 | 0   | \-  | 3   |
| 6 FDD=C77AXJ 1 -------- | \-  | 1 18 33333 451 85 |     | 2436 | 20436 872.6 827.6 |     |     | 5   | 5   | 5   | 25  | 25  | 2/4 | 2/4 | 0   | \-  | 4   |
| 7 FDD=C77AXX D -------- 1,3 |     |     | 1 22 33333 433 720 | 68636 133172 |     |     | 622 | 668 10 10 |     |     | 71 160 158 |     |     | 4/4 | 4/4 | 0   | 1   | 1   |
| 8 FDD=C77AXY 1 -------- - |     |     | 10 23 33333 439 730 | 68636 133172 |     |     | 622 | 668 10 10 |     |     | 71 160 158 |     |     | 4/4 | 4/4 | 0   | 2   | 5   |
| 9 FDD=C77AXZ 1 -------- - |     |     | 12 24 33333 445 740 | 68636 133172 |     |     | 622 | 668 10 10 |     |     | 71 160 158 |     |     | 4/4 | 4/4 | 0   | 3   | 6   |
| 10 NIOT=C77AOA 1 -------- 3 |     |     | 0 127 48314 435 695 | 5070 23070 |     |     | 735 | 705 0.4 0.4 |     |     | 12 40 40 |     |     | 2/4 | 2/4 | 0   | \-  | 1   |
| 11 NIOT=C77AOB 1 -------- - |     |     | 0 128 48314 443 705 | 5070 23070 |     |     | 735 | 705 0.4 0.4 |     |     | 12 40 40 |     |     | 2/4 | 2/4 | 0   | \-  | 5   |
| 12 NIOT=C77AOC 1 -------- - |     |     | 0 129 48314 451 715 | 5070 23070 |     |     | 735 | 705 0.4 0.4 |     |     | 12 40 40 |     |     | 2/4 | 2/4 | 0   | \-  | 6   |

\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Total: 12 Cells (11 up)

S=administrativeState&operationalState&cellState&serviceState&availabilityStatus (1=unlocked&enabled&active&inservice, 0=unlocked&disabled|inactive|outofservice, L=locked, D=degraded)

T=txPowerState ("I" invalid, "C" changing, "-" stable)

A=ailgActive ("A" active, "-" not active)

B=cellBarred ("B" barred, "-" not barred)

R=cellReservedForOperator ("R" reserved, "-" not reserved or not-applicable, eg when CXC4010960.serviceState=OPERABLE or CXC4012479.serviceState=OPERABLE)

M=massiveMimoSleepState ("M" sleeping, "-" not sleeping)

D=FRU.deepSleepStatus ("-" not sleeping, "D" deep sleeping)

F=FRU.maintenanceIndicator ("F" ongoing maintenance, "-" no ongoing maintenance)

\=============================================================================================================================================================================

Id NRCell S TABRMDF Alm UEs cId tac pci rsi nci arfcnDL arfcnUL freqDL freqUL dlBW ulBW cnfP maxP C-T/R U-T/R Ess Fru NRCellCU (State:cId:UEs)

\=============================================================================================================================================================================

1.  NRC=C77AN1 D ------- 2,3 1 6101 33333 435 105 62751725525 124400 133600 622 668 10 10 160 160 0/0 4/4 7 1 C77AN1 (1:6101:1)
2.  NRC=C77AN2 1 ------- - 3 6102 33333 443 95 62751725526 124400 133600 622 668 10 10 160 160 0/0 4/4 8 5 C77AN2 (1:6102:3)
3.  NRC=C77AN3 1 ------- - 2 6103 33333 451 85 62751725527 124400 133600 622 668 10 10 160 160 0/0 4/4 9 6 C77AN3 (1:6103:1)

\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Total: 3 Cells (2 up)

**4.2.16 hc\[iuzd\]\[v\] \[-r|-x &lt;numbers&gt;\] \[&lt;hclogfile&gt;|&lt;hclogdir&gt;|&lt;hcreportdir&gt;\] \[&lt;hclogfile2&gt;|&lt;hclogdir2&gt;\]**

Run a healthcheck report or compare healtcheck logs.

**Options:**

- - i: only perform checks applicable to pre-install phase (1-6, as well as 9,13 on RNC)
    - u: only perform checks applicable to pre-upgrade phase (5-8,10-12,14-17)
    - z: only perform checks applicable to post-upgrade phase (5-8,10-12,14-17, as well as 9 on RNC)
    - d: perform a diff between two HC log files or two HC log directories
    - v: verbose printout

**Switches:**

- - \-r &lt;numbers&gt;: list of checks to perform. Eg: -r 1-3,5,7-10
    - \-x &lt;numbers&gt;: list of checks to skip. Eg: -x 5,12-14 **List of checks:**

<div class="joplin-table-wrapper"><table><tbody><tr><td><p>Check numbers</p></td><td><p>Applicability</p></td></tr><tr><td><p>- 1: Disk space</p></td><td><p>All</p></td></tr><tr><td><p>- 2: Number of UpgradePackages</p></td><td><p>All</p></td></tr><tr><td><p>- 3: Number of CVs</p></td><td><p>All</p></td></tr><tr><td><p>- 4: Security settings</p></td><td><p>RNC</p></td></tr><tr><td><p>- 5: Alarm list</p></td><td><p>All</p></td></tr><tr><td><p>- 6: License status</p></td><td><p>All</p></td></tr><tr><td><p>- 7: HW status</p></td><td><p>All</p></td></tr><tr><td><p>- 8: HW supported by release</p></td><td><p>RNC</p></td></tr><tr><td><p>- 9: DB consistency</p></td><td><p>RNC,RBS,ENB</p></td></tr><tr><td><p>- 10: Synchronization status</p></td><td><p>All</p></td></tr><tr><td><p>- 11: NTP status</p></td><td><p>RNC,RBS,ENB</p></td></tr><tr><td colspan="2"><ul><li>12: Fault Tolerant Core status RNC</li><li>13: File System consistency RNC,RBS,ENB</li><li>14: Crash history All</li><li>15: Connectivity status All</li><li>16: Cell status All</li><li>17: Device status RNC</li></ul></td></tr></tbody></table></div>

**Arguments for hc\[iuz\]\[v\]:**

- - no argument: only applicable when connected to the node. Will generate a hclogfile, then parse it to generate a hcreportfile.
    - &lt;hclogfile&gt;: parse an existing hclogfile to generated a hcreportfile.
    - &lt;hclogdir&gt; : parse existing hclogfiles stored in a common folder to generate a set of hcreportfiles that will be stored in a new folder.
    - &lt;hcreportdir&gt;: parse existing hcreportfiles stored in a common folder to generate a common report showing the check results (OK, NOT OK, OK with Warning) for all the nodes whose logs are stored in that folder.

**Output files produced by hc\[iuz\]\[v\]:**

HcLogFile: a file containing a set of moshell printouts taken from the node (eg: invl, dbc, etc). FileName format:

$logdir/hc/logs/.../HcLog_&lt;NodeType&gt;\_&lt;NodeName&gt;-&lt;NodeIp&gt;\_&lt;HcVersion&gt;.log.gz

- - ReportFile: a file generated by parsing a hclogfile according to a number of checks resulting in OK, OK with Warning, or NOT OK. FileName format:

$logdir/hc/reports/.../HcReport_&lt;NodeType&gt;\_&lt;NodeName&gt;-&lt;NodeIp&gt;\_&lt;HcVersion&gt;.txt **Arguments for hcd\[v\]:**

- - &lt;hclogfile&gt; : only applicable when connected to the node. Will generate a hclogfile, then compare it toward a hclogfile previously collected from the same node.
    - &lt;hclogfile&gt; &lt;hclogfile2&gt;: compare two hclogfiles previously connected from a node to show differences such as active alarms, scanner states, MO states, operable features, HW state, etc
    - &lt;hclogdir&gt; &lt;hclogdir2&gt; : compare a set of hclogfiles stored in two separate folders to show differences as listed above. Only pairs of hclogfiles coming from the same node will be compared.

**Output files produced by hcd\[v\]:**

- - DiffFile: a file generated by parsing two hclogfiles (eg pre and post upgrade log) according to a number of checks resulting in OK, OK with Warning, or NOT OK. FileName format:

$logdir/hc/reports/.../HcDiff_&lt;NodeType&gt;\_&lt;NodeName&gt;-&lt;NodeIp&gt;\_&lt;HcVersion&gt;.txt

**Filter file:**

This is a text file containing configuration settings to tailor the behaviour of the health checks. The default filter file is stored under moshell/commonjars/scripts/hc/filterfile.txt and should not be modified as it contains the default settings. To modify certain settings please create a separate filter file containing the settings to be modified and specify its path in the uservariable hc_filter_file which can be specified in the /.moshellrc or moshell/jarxml/moshellrc .

**Batch reports:**

- - 1) Collect a set of HcLogFiles and HcReportFiles from a batch of nodes by running: mobatch &lt;sitefile&gt; ’hc\[iuz\] \[-x &lt;nrs&gt;\] \[-r &lt;nrs&gt;\]’

Note that the options \[iuz\], -x/-r are optional and only needed in case the user does not need to perform all checks, then these options allow to save time by skipping collection of certain printouts from the node.

The mobatch job will save all HcLogFiles and HcReportFiles in a folder common for all nodes specified in the sitefile. The path of this folder will be located under moshell_logfiles/logs_moshell/hc/(logs|reports)/&lt;date&gt;/&lt;sitefile&gt;/&lt;time&gt; The exact path can be found by looking inside one of the mobatch logfiles.

- - 2) After the mobatch job is completed, open a moshell offline session not connected to any node (eg just type "moshell" on its own) and run hc\[iuz\]\[v\] or hcd\[v\] against the relevant hc/logs folder(s), according to arguments described further up in this help. hc\[iuz\] typically should run toward the hc/reports folder while hcd should run toward a pair of hc/logs folders.

Eg: hc $logdir/hc/reports/&lt;date&gt;/&lt;sitefile&gt;/&lt;time&gt; or: hcd $logdir/hc/logs/&lt;date&gt;/&lt;sitefile&gt;/&lt;time1&gt; $logdir/hc/logs/&lt;date&gt;/&lt;sitefile&gt;/&lt;time2&gt;

**Description of the checks (criteria for OK):**

- - 1) Disk space: the amount of free disk space is at least 10% above the limit specified in the filterfile.txt (disk_space\*). If less than 10% above limit, the result will be OK with warning.
    - 2) Number of UpgradePackages: the number of UpgradePackages is less than the limit specified in the filterfile.txt (nr_ups).
    - 3) Number of CVs: the number of CVs/Backups is less than the limit specified in the filterfile.txt (nr_cvs).
    - 4) Security settings: corba security and ftp client are configured as unsecure
    - 5) Alarm list: there are no active alarms with the severities listed in the filter file (alarm_severities)
    - 6) License status: the license is installed and not in emergency state, the number of days remaining is above the limit specified in filterfile.txt (license_days), there are no licenses with inconsistent states (eg ACTIVE&ENABLED&INOPERABLE), the RNC HWAC codes and limits are valid.
    - 7) HW status: no HW is in state unlocked&disabled, and the fault LEDs are OFF and the oper LEDs are ON.
    - 8) HW supported by release: the HW product number/revision is same or higher as specified in the file HW_RNC.csv
    - 9) DB consistency: the result of dbc command is OK
    - 10) Synchronization status: the system clock is in state LOCKED mode.
    - 11) NTP status: there are valid NTP servers
    - 12) Fault Tolerant Core status: the passive core MP is in state StandbyReady.

13) File System consistency: the action ManagedElement.startHealthCheck() returned OK

- - 14) Crash history: there have not been any Crash/PMDs in the past 14 days
    - 15) Connectivity status: there are no unlocked&disabled MO instances of MO class listed in filterfile.txt (connectivity_mocs)
    - 16) Cell status: there are no unlocked&disabled MO instances of MO class listed in filterfile.txt (cell_mocs)
    - 17) Device status: there are no unlocked&disabled MO instances of MO class listed in filterfile.txt (device_mocs)

**4.2.17 trg\[idfubgs\] \[-e &lt;section&gt;\] \[-f &lt;faultString&gt;\] \[-s &lt;searchString&gt;\] \[-t PMDA|BBI\] \[&lt;NodeIP|/path/to/dcgm.zip&gt;\]**

Generate RBS TR observation template

Argument:

- - without argument: generate from the node or dcgm to which the moshell session is currently connected.
    - node IP: generate from a node with the specified IPaddress
    - /path/to/dcgm.zip: generate from a dcgm.zip located at the specified path

Options:

- - i: interactive (user will be prompted with various questions)
    - d: save debug values to /tmp/TR/TRToolValues.json. Do NOT use, only for development
    - f: force a new connection to ERIS (only applicable when run from Ericsson network). Do NOT use, only for development
    - u: unpack latest PMDs and BB dumps. E-mail will be sent when BB dump unpack is completed.
    - s: same as option "u" above but without sending E-mail.
    - b: bbi dump unpack. Do NOT use, only for development
    - g: login to external equipment and fetch versions/logs.

Switches

- - \-e &lt;no|all|1|2|3|1,2,3&gt; : exclude comments for all or specific sections of the template. Default is -e 2. Use -e no to not exclude comments from any sections.
    - \-f &lt;faultString&gt; : search for specific fault, eg trg -f &lt;name_of_pmd&gt; extracts information about matching pmd.
    - \-s &lt;searchString&gt; : search for a known fault in MHWEB, eg trg -s ulmacce_drxupdate. By default up to 10 search results will be produced. The upper limit can however be changed in the uservariable trg_search_count.
    - \-t PMDA|BBI : to specify the crash dump unpack tool to be used during fault string analysis. BBI is default. PMDA uses a remote CSDP server, accessible only from Ericsson Corporate Network with an Ericsson Corporate login. The username/password for the CSDP server can be saved in the uservariables csdp_username / csdp_password .

**4.2.18 diff\[a\]\[d\]\[m\]\[o\]\[x\]\[i\]/ldiff\[a\]\[d\]\[m\]\[o\]\[x\]\[i\]**

Parameter auditing or MO dump comparisons.

**Syntax 1:**

Compare two or three MOs side by side. All attribute values that are different between the MOs will be printed.

Example:

dif 4 32 17

Where 4, 32, 17 are the proxy identities of the MOs that should be compared.

**Syntax 2:**

diff\[a\]\[d\]\[m\]\[o\]\[x\]\[i\]/ldiff\[a\]\[d\]\[m\]\[o\]\[x\]\[i\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy&gt;|&lt;modumpFile&gt;|&lt;modumpDir&gt; \[&lt;baselineFile&gt;|&lt;modumpFile2&gt;|default\] \[&lt;outputDir&gt;\]

Purpose: To compare an MO dump with a parameter baseline file or with another MO dump.

**Options:**

a: show the list of MOs and attributes that are in the reference but not in the node or dump.

- d: compare against the default values in MOM (read from command "momb")
- m: when comparing against parameter baseline, any parameter not found in the baseline will be compared against the MOM default values instead.
- o: when comparing two MO dumps, only the differences in configuration parameters will be shown (= attributes that are not readOnly)
- ox: same as diffo but with an additional table showing attribute name differences.
- i: to audit the EricssonOnly ("internalmom") parameters of a Gen2 node, using "geti" command. Only applicable to MSRBS (DUS Gen2).
- im: same as "i" but where the EricssonOnly parameters are compared to their default value.

Note: It is currently not supported to combine several options together (apart from "o" and "x")

When no option is specified, the attributes are compared against the recommended values in baseline (files moshell/commonjars/pm/PARAM\*) User variables:

- diffo_exclude_attributes : to exclude certain attributes from the MO dump comparison (diffo &lt;dump1&gt; &lt;dump2&gt;)
- diffm_exclude_moclasses : to exclude certain MO classes from the MOM default value comparison (diffd and diffm)
- diffm_exclude_attributes : to exclude certain attributes from the MOM default value comparison (diffd and diffm)
- diffm_exclude_structs : to exclude certain structs from the MOM default value comparison (diffd and diffm)

Note: Any MO classes/attributes included in these lists will be skipped only in regard to the default value comparison. If there is a recommended value in the PARAM file or reference file then this check will not be excluded.

First Argument:

- &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy&gt;: to specify the MOs in the current node which should be used for the comparison.
- &lt;modumpFile&gt;: to specify an modump, taken from this node or another node. The modump file should be a zipfile taken by the command dcgk. Alternatively it can be a text or gzipped file containing the printout from the get or kget command.
- &lt;modumpDir&gt;: to specify a directory containing modump logfiles. Only files with the extension ".log" will be used in the comparison.

Second Argument (optional):

- empty or "default": a baseline parameter file from moshell/commonjars/pm/PARAM\* will be chosen according to the MOM type and version of the current node or of the modump specified in the first argument. Note: typing "default" is only necessary if one wants to specify a third argument (the outputDir).

If the uservariable custom_param_file is set then the file(s) specified in custom_param_file are read after the PARAM\* file, meaning that their values will override those of the PARAM\* file. The default parameter baseline files in moshell/commonjars/pm/PARAM\* are extracted from the following documents: RNC: 3/19059-HSD10102. RBS: 4/19059-HSD10102. ENB/MSRBS: 19706-CXP102051/\*

- &lt;baselineFile&gt;: a specific baseline file is used as reference, instead of the default one. In this case the file(s) specified in the uservariable custom_param_file are not read.

The format of a baseline file must consist of three words on each line: &lt;mo&gt; &lt;attribute&gt; &lt;value&gt; The &lt;mo&gt; field can be either an MO class (e.g. PlugInUnit) or an MO LDN (e.g.

Subrack=MS,Slot=1,PlugInUnit=1)

It is also possible to write a tilde sign ( ) in front of the MO LDN, in which case it is treated as a regular expression.

For instance: ~UniSaalTp=.\*q\[ab\]$ maxSduSize 128 means that the reference value only applies to the MOs whose LDN matches that string.

The recommended value can be a single value or several values separated by commas. For instance -1,2,25,300 : means any of these values is accepted as recommended value. If the recommended value is a sequence of Structs or sequence of moRefs, then it shall be written on one single line. In case of sequence of Structs, the struct members must be alphabetically sorted (in order of struct member name) and the struct member names shall not be specified, only the struct member values. Example:

EthernetSwitch pbitQueueMap \[8\] = 0,1;1,0;2,1;3,1;4,2;5,2;6,3;7,3

EUtranFreqRelation eutranFreqToQciProfileRelation \[9\] = 0,0,0,0,0 (ALLOWED),0 (ALLOWED),0,0,0,1 (F

If the reference file contains several entries with the same MO / attribute, the following priority rules apply:

1.  Lines with a fixed value take precedence over lines containing Iu/Iur/Iub, regardless of the order. Eg:

Sctp pathMaxRtx Iu, Iur: 4 Iub: 12

Sctp pathMaxRtx 13

\-> The line with value 13 will be used, regardless if it is before or after the Iu/Iur/Iub line.

1.  Lines containing a tilde: the first entry takes precedence. Eg:

~Sctp pathMaxRtx 13

~Sctp pathMaxRtx 14

\-> The line with the value 13 will be used as reference.

1.  Lines containing no tilde: the last entry takes precedence. Eg:

Sctp pathMaxRtx 13

Sctp pathMaxRtx 14

\-> The line with the value 14 will be used as reference

More information about the reference file format can be found in the document moshell/examples/audit_files/EAB_FJW-08_0071.doc

- &lt;modumpFile&gt;: the two modump logfiles are compared and the following differences will be highlighted: differences in attribute values, MOs found in one dump but not the other, attribute names found in one dump but not the other.

Third Argument:

- &lt;outputDir&gt;: to specify the directory where to store the result files (csv comparison file and correction command file). If not specified, a default directory and file names are chosen.

Result:

The result is shown on screen with space-separated fields and also saved in the result directory with comma-separated fields (CSV). Also, in the result directory is a command file to align the current values to the baseline values. The path to the CSV result file is saved in the moshell variable $diffcsvfile and the path to the command file is saved in the moshell variable $diffcmdfile.

Please refer to the document moshell/examples/audit_files/EAB_FJW-08_0071.doc for more information.

Note about parameter baseline files:

Parameter baseline files are taken from the Winnow database and stored in CDM in excel format:

- RNC: 3/19059-HSD10102
- RBS: 4/19059-HSD10102
- RXI: 5/19059-HSD10102
- ENB: 19706-CXP102051/\*

To use these files as reference for comparison, they need to be converted to text. This can be done by copy pasting the excel sheet to a text file. Moshell keeps a text copy of the latest version of each of these files in the folder moshell/commonjars/pm. By not specifying the baseline parameter file in the "diff" command will make moshell choose the best suited file for the node type and mom version of the current node or modump file.

**Examples:**

- diff . - Compare all MOs with the relevant baseline parameter file stored in moshell/commonjars/pm.
- diffa . - Same as above but showing MO/attributes found in reference but not in node
- diff . default ~/audit\\\_070110 - Same as above but store the results in the directory /audit_070110
- diff ~/moshell_logfiles/logs_mobatch/2007-01-10/mysites/11-21 - Compare all modumps under that directory against the relevant baseline parameter file stored in moshell/commonjars/pm
- ldiff msplatform=1 mgw\\\_parameters\\\_r4.txt - Compare all MOs under msplatform=1 in the current node with the baseline file "mgw_parameters_r4.txt"
- diff . rnc10\\\_before\\\_upgrade.txt - Compare all MOs in the current node with the MO dump

"rnc10_before_upgrade.txt"

- diff rnc10\\\_before\\\_upgrade.txt rnc10\\\_after\\\_upgrade.txt - Compare the MO dumps

"rnc10_before_upgrade.txt" and "rnc10_after_upgrade.txt"

- diffo rnc10_before_upgrade.txt rnc10_after_upgrade.txt - Same as above but only the configuration parameters are compared
- diffd utrancell - compare all utrancell parameters against MOM default values.

**4.2.19 diffs &lt;scRefFile&gt;|&lt;modumpFile&gt;**

Auditing or comparison of System Constants. Applicable to MSRBS only.

**Argument:**

- &lt;scRefFile&gt; : the path to a reference file containing default and recommended SystemConstant values for a given UP. This file is generated by the command "w2f".
- &lt;modumpFile&gt;: the path to a modump.zip (dcgk) or a dcgm.zip (dcgm)

**Output:**

The command compares the current system constant settings (read via "scg" command) against the system constant values stored in:

- a SystemConstant reference file produced by "w2f" command for the current UP
- or the SystemConstants stored in a offline dump (dcgk or dcgm)

**4.2.20 w2f &lt;UP&gt;**

Generate MO parameter reference file and System Constant reference file for a given MSRBS UP. Applicable for Ericsson PDU personnel only.

**Argument:**

- &lt;UP&gt; : the product number and revision of the MSRBS UP , eg: CXP9024418/12_R81C57

**Output:**

The command produces two files:

- a reference file containing recommended MOM parameter values for LTE and NR, to be used in the "diff" command. This is the same kind of file as found in moshell/commonjars/pm/PARAM_MSRBS_&lt;release&gt;.txt but can be produced for any UP and not only the major releases. The path of this file is output to the variable $refmomfile
- a reference file containing recommended System Constant settings for LTE and NR, to be used in the "diffs" command.

The path of this file is output to the variable $refscfile

**4.2.21 lkr\[a\]**

Print RNC Iub resources allocation.

**Purpose:**

- display the repartition of IubLinks and UtranCells across rncModules and Subracks, to identify any uneven resource allocations, for instance: rncModules that are handling more Iub/Cells than others, or CC devices that are handling different Cells than their controlling module MP.
- uneven allocation of IubLinks across RncModules can be corrected by the command resub iublink
- uneven allocation of UtranCells across CC devices can be corrected by locking/unlocking the cells using command bl and deb on the UtranCell MOs.
- with the option a, an additional table shows the IubLinks whose AtmPort(s) are located in a different Subrack than the Iub module resources. IubLinks can be moved to a different AtmPort or Subrack with the command resub &lt;iublink&gt; &lt;subrack&gt; or resub &lt;iublink&gt; &lt;atmport/vp&gt;. Type h resub for info.

**Printout example and description:**

The first table, only printed with option a (lkra), shows the list of IubLinks whose AtmPort(s) are in a different Subrack than the Iub module resources. The Sr column shows the Subrack containing the module resources, the Mod column shows the module number, the IubLink column shows the Iub, and the AtmPort(s) column shows the port(s) used by the Iub. Example:

\--------------------------------------------------------------

Sr Mod IubLink AtmPort(s)

\--------------------------------------------------------------

|     |     |     |
| --- | --- | --- |
| MS  | 1 Iub-198 | ES-1-27-2-1 |     |
| MS  | 13 Iub-203 | ES-1-27-2-1 |     |
| MS  | 8 Iub-208 | ES-1-27-2-1 |     |
| MS  | 1 Iub-213 | ES-1-27-2-1 |     |
| MS  | 13 Iub-214 | ES-1-27-2-1 |     |
| MS  | 1 Iub-87 | ES-1-3-1-1 |     |
| MS  | 8 Iub-88 | ES-1-3-1-1 |
| MS  | 1 Iub-89 | ES-1-3-1-1 |
| MS  | 13 Iub-90 | ES-1-3-1-1 |
| MS  | 8 Iub-91 | ES-1-3-1-1 |
| MS  | 1 Iub-92 | ES-1-3-1-1 |
| MS  | 13 Iub-93 | ES-1-3-1-1 |
| MS  | 8 Iub-94 | ES-1-3-1-1 |
| MS  | 1 Iub-95 | ES-1-3-1-1 |
| MS  | 13 Iub-96 | ES-1-3-1-1 |

\--------------------------------------------------------------

The second table (which is the first table when option "a" is not used) shows the resources allocation, module by module.

- Sr : the subrack containing the module resources
- Mod : the module number
- S : the state of the module MP: L=locked, 1=enabled, 0=disabled
- GPB : the board type of the module MP
- nIub : the number of IubLinks handled by the module MP. Having an equal number of IubLinks/Cells on each module gives a better spreading of the load.
- CellGPB: the number of UtranCells handled by the module MP
- CellCC : the number of UtranCells handled by the CC devices controlled by that module MP.
- nCC : the number of CC devices allocated to this RncModule.

Note: if the cell to CC device allocation has changed since the moshell session was started, the command "bor" needs to be run in order to refresh the moshell cache, otherwise the values in "CellCC" field could be wrong.

Cell repartition by rncModule:

\-----------------------------------------------

Sr Mod S GPB nIub CellGPB CellCC nCC

\-----------------------------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| MS  | 60 1 GPB65 | 14  | 90  | 117 | 1   |
| MS  | 80 1 GPB65 | 13  | 81  | 114 | 1   |
| MS  | 110 1 GPB65 | 14  | 90  | 119 | 1   |
| MS  | 140 1 GPB65 | 14  | 93  | 117 | 1   |

\-----------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| ES1 21 1 GPB65 | 14  | 99  | 118 | 1   |
| ES1 81 1 GPB65 | 14  | 99  | 114 | 1   |
| ES1 151 1 GPB65 | 14  | 111 | 119 | 1   |
| ES1 181 1 GPB65 | 14  | 96  | 106 | 1   |
| ES1 211 1 GPB65 | 14  | 105 | 103 | 1   |
| ES1 2121 1 GPB75 | 13  | 102 | 114 | 1   |
| ES1 2122 1 GPB75 | 13  | 87  | 114 | 1   |

\-----------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| ES2 3021 1 GPB75 | 14  | 93  | 140 | 1   |
| ES2 3022 1 GPB75 | 14  | 99  | 0   | 0   |
| ES2 3081 1 GPB75 | 14  | 90  | 140 | 1   |
| ES2 3082 1 GPB75 | 14  | 93  | 0   | 0   |
| ES2 3121 1 GPB75 | 15  | 99  | 140 | 1   |
| ES2 3122 1 GPB75 | 14  | 96  | 0   | 0   |
| ES2 3151 1 GPB75 | 14  | 99  | 114 | 1   |
| ES2 3152 1 GPB75 | 14  | 96  | 113 | 1   |
| ES2 3181 1 GPB75 | 14  | 102 | 120 | 1   |
| ES2 3182 1 GPB75 | 14  | 102 | 99  | 1   |
| ES2 3211 1 GPB75 | 14  | 93  | 87  | 1   |
| ES2 3212 1 GPB75 | 14  | 93  | 0   | 0   |

\-----------------------------------------------

The third table (which is the second table when option "a" is not used) is identical to the previous one but aggregated on Module Board level. In the case of GPB5/GPB6 it will give the same figures as the previous table but in the case of multicore boards (GPB75/EPB) it gives aggregated values for all RncModules of that board.

Cell repartition by Board:

\-----------------------------------------------

Sr Slot S GPB nIub CellGPB CellCC nCC

\-----------------------------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| MS  | 06 1 GPB65 | 14  | 90  | 117 | 1   |
| MS  | 08 1 GPB65 | 13  | 81  | 114 | 1   |
| MS  | 11 1 GPB65 | 14  | 90  | 119 | 1   |
| MS  | 14 1 GPB65 | 14  | 93  | 117 | 1   |

\-----------------------------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| ES1 | 02 1 GPB65 | 14  | 99  | 118 | 1   |
| ES1 | 08 1 GPB65 | 14  | 99  | 114 | 1   |
| ES1 | 12 1 GPB75 | 26  | 189 | 228 | 2   |
| ES1 | 15 1 GPB65 | 14  | 111 | 119 | 1   |
| ES1 | 18 1 GPB65 | 14  | 96  | 106 | 1   |
| ES1 | 21 1 GPB65 | 14  | 105 | 103 | 1   |

\-----------------------------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| ES2 | 02 1 GPB75 | 28  | 192 | 140 | 1   |
| ES2 | 08 1 GPB75 | 28  | 183 | 140 | 1   |
| ES2 | 12 1 GPB75 | 29  | 195 | 140 | 1   |
| ES2 | 15 1 GPB75 | 28  | 195 | 227 | 2   |
| ES2 | 18 1 GPB75 | 28  | 204 | 219 | 2   |
| ES2 | 21 1 GPB75 | 28  | 186 | 87  | 1   |

\-----------------------------------------------

The fourth table (which is the third table when option "a" is not used) shows an aggregated view of the previous table, on Subrack level. This is interesting to see if any Subracks are more loaded than others.

- Sr : the Subrack identity
- nMod : the number of rncModules contained in the Subrack
- nCC : the number of CC devices contained in the Subrack
- nIub : the number of IubLinks handled by all module MPs of the Subrack
- CellGPB : the number of UtranCells handled by all module MPs of the Subrack
- CellCC : the number of UtranCells handled by all CC devices of the Subrack
- avIub : the average number of IubLinks per module MP in that subrack
- avCell : the average number of UtranCells per module MP in that subrack
- avCellCC: the average number of UtranCells per CC device in that subrack

Cell repartition by Subrack:

\--------------------------------------------------------------

Sr nMod nCC nIub CellGPB CellCC avIub avCell avCellCC

\--------------------------------------------------------------

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MS  | 4   | 4   | 55  | 354 | 467 | 14  | 88  | 117 |
| ES1 | 7   | 7   | 96  | 699 | 788 | 14  | 100 | 113 |
| ES2 | 12  | 8   | 169 | 1155 | 953 | 14  | 96  | 119 |

\--------------------------------------------------------------

Tot: 23 19 320 2208 2208

**4.2.22 resub &lt;IubLink&gt; \[&lt;VplTp&gt;|&lt;Subrack&gt;\] \[&lt;VplTp&gt;\]**

Moving Iub resources within or across Subracks (RNC >= P5).

There are three ways to run the command:

1.  **Respreading of Iub resources within a subrack: resub &lt;iublink(s)&gt;**

The lkr command shows the repartition of Cells/IubLinks across rncModules, Cc devices and Subracks. The performance is affected when the resources allocation is uneven. The Cells/IubLinks resources can be evenly reallocated by using the command resub &lt;iublink(s)&gt;. Example:

- - resub iublink= - Reallocate all iublink resources evenly in the node
    - ma iub_es1 iublink subrackref subrack=es-1 ; resub iub_es1 - Reallocate all iublink resources evenly in subrack ES-1

1.  **Moving Iub resources to a different subrack: resub &lt;iublink(s)&gt; &lt;subrack&gt;**

The lkra command shows the list of IubLinks whose AtmPort(s) are located in a different Subrack than the IubLink. This causes higher ISL load. The IubLink can then be moved to a different Subrack with the command resub &lt;iublink(s)&gt; &lt;subrack&gt;.

Example:

- - resub iublink=iub-10 subrack=es-1 - Move IubLink iub-10 to subrack ES-1

1.  **Moving Iub resources to different AtmPort/Vp: resub &lt;iublink&gt; &lt;vp&gt; \[&lt;vp&gt;\]**

When there is is need for more Atm bandwidth it may be necessary to move an Iub to a different Atm port. This can be done with the command resub &lt;iublink&gt; &lt;vp&gt; \[&lt;vp&gt;\]. The second vp is optional and only needed for IubLinks that use two AtmPorts for redundancy.

- - resub iublink=3040 atmport=ms-27-2,vpltp=vp2 - Move the IubLink 3040 to AtmPort=MS-27-2,VplTp=vp2
    - resub iublink=3040 atmport=ms-27-2,vpltp=vp2 atmport=ms-26-2,vpltp=vp8 - Move the IubLink 3040 to AtmPort=MS-27-2,Vpltp=vp2 and AtmPort=MS-26-2,VplTp=vp8

**Result:**

- - **a) and b)** In these cases, the command sets the attribute preferredSubrackRef (P5/P6) or atmUserPlaneTermSubrackRef (P7) to the required subrack. In the case of a), this is the current subrack, equivalent to running

setc &lt;iublink(s)&gt; preferredsubrackref. In the case of b), this is the given subrack, equivalent to running set &lt;iublink(s)&gt; preferredsubrackref &lt;subrack&gt;

- - **c)** In the case where one or two VplTp(s) have been specified, a command file is generated containing all the commands necessary for moving the IubLink to the new VplTp(s). The command can be executed with the run command or can be converted to EMAS/MoTester format using the u! command. In that case, it can be executed with the trun command.

**4.2.23 ir\[cdpsomt\] \[&lt;IubLink&gt;\] \[&lt;CM&gt;\] \[&lt;period&gt;\]**

Iub Redundancy operations for RNC in pool. Only applicable for RNC <= 21.Q1.

Arguments (all optional):

- - the first argument is for specifying the IubLink(s) on which the command will apply. It can be a MO filter, a proxy ID, or a MO group. If no IubLink is specified then the command will apply to all. IubLinks using ATM transport will be silently ignored. Note: the c option will always ignore this argument.
    - the second argument is for specifying the address of the other Cluster Member, which can be an ip address or the path to an MO dump. The other Cluster member can also be specified in the uservariable cluster_members in which case it is not necessary to specify this argument. The uservariable cluster_members shall contain the list of ip addresses or MO dump paths for all nodes of the cluster. It can be specified from the command line with uv command or saved in the ipdatabase file.
    - the third argument is only applicable to option "t" and is for specifying the report period, using same syntax as in pmx/pmr command (eg: -m &lt;hrs&gt;, -s &lt;startdate&gt;, etc)

**Options:**

- - o: Overview of the Iub Redundancy configuration and status. Will generate a printout listing all IubLinks and Cell states, both redundant and non-redundant, in a format similar to the str3 command. In this option, the first argument is ignored. See printout description further down.
    - c: Consistency check of the Iub Redundancy configuration. Will generate a printout listing all the checks and their result. In this option, the first argument is ignored. See printout description further down.
    - p: Protect one or more IubLinks. Only IubLinks with poolRedundancy PRIMARY or NON-REDUNDANT will be considered by the command. The poolRedundancy attribute will be set to PRIMARY and a command file will be generated to define the secondary IubLink(s) and associated cell data in the other Cluster Member. The command file shall be executed in the other Cluster Member and the file path can be accessed from the variable $irpcommandfile.
    - s: Synchronise the configuration data of one or more secondary IubLinks. Only IubLinks with poolRedundancy SECONDARY and operationalState DISABLED will be considered by the command. A command file will be generated to align the secondary Iub/Cell data to its counterpart in primary side. The command file shall be executed in the same

Cluster Member where the irs command was run, and the file path can be accessed from the variable $irscommandfile. Any secondary IubLinks without a primary counterpart will be saved in the variable $irs_orphan_iubs and can be removed with the command ird $irs_orphan_iubs.

- - d: Delete one or more secondary IubLinks. Only IubLinks with poolRedundancy SECONDARY and operationalState DISABLED will be considered by the command. A command file will be generated to remove the secondary IubLink(s) and associated cell data. The command file shall be executed in the same Cluster Member where the ird command was run, and the file path can be accessed from the variable $irdcommandfile. The corresponding primary IubLinks can be set to non-redundant with the command set $ird_iubs poolRedundancy 0, to be run in the other Cluster Member.
    - m: Move one or more non-redundant IubLink(s) from a Cluster Member to another. Two command files are generated: one for creating the IubLink(s) on the other CM, and one for deleting them on the current CM.
    - t: Traffic Reports. Currently shows the Paging Success Rates at Pool level. Example: to print the report for the last 2 hrs, do: irt . . -m 2

Notes:

- - when a secondary UtranCell is created by irp or irs, the previously existing RemoteUtranCell with that cId will be removed, and any cell relations terminating to the RemoteUtranCell will be redirected towards the newly secondary UtranCell.
    - when a secondary UtranCell is deleted by ird or irs, a RemoteUtranCell will be created in its place in order to terminate any cell relations that were pointing to the newly deleted UtranCell.
    - secondary UtranCells created by irp or irs will use a dedicated Ura common for all cells of that secondary IubLink. The Ura MO used by the primary UtranCells will not be used as it is currently not supported by RNC to use the same UraIdentity in several members of the same cluster.
    - any attributes that shall not be copied over from primary to secondary Iub/Cells can be specified in the uservariable ir_nosync.
    - the secondary IubLink created by irp will be created in administrativeState=LOCKED if redundancySwitchoverWaitTime=-1 on the s-CM.

Example printout from irc command:

\==============================================================================

Iub Redundancy Consistency Check for nodes: RNC01 (CM1) and RNC02 (CM2)

\==============================================================================

1.  Same SW level in all CMs: NOT OK

CurrentUpgradePackage: CXP9021776_R4FC40 (CM1) CXP9021776_R4FC39 (CM2)

\------------------------------------------------------------------------------

1.  Same features operational in all CMs: NOT OK

RncFeature=RabCombination009 serviceState: 0 (CM1) 1 (CM2)

\------------------------------------------------------------------------------

1.  All primary/non-redundant IubLinks/UtranCells have unique rbsId/cId within the cluster: NOT OK cId=2205 UtranCell=cell1106-Iub-1523-6 (CM1) UtranCell=cell2205-Iub-1525-5 (CM2)

\------------------------------------------------------------------------------

1.  All secondary IubLinks/UtranCells have unique rbsId/cId within the cluster: NOT OK cId=2202 UtranCell=cell2202-Iub-1525-2 (CM1) UtranCell=cell2201-Iub-1525-1 (CM1)

\-----------------------------------------------------------------------------5) No Utran/Coverage Relations between two cells with same cId: NOT OK cId=1201 UtranCell=cell2204-Iub-1525-4,UtranRelation=Rem-Inter-Iub-1526-1 (CM1) cId=1201 UtranCell=cell1201-Iub-1526-1,UtranRelation=Rem-Intra-Iub-1525-4 (CM1) cId=2202 UtranCell=cell2201-Iub-1525-1,UtranRelation=Intra-Softer-cell2202-Iub-1525-2 (CM1) cId=2202 UtranCell=cell2202-Iub-1525-2,UtranRelation=Intra-Softer-cell2201-Iub-1525-1 (CM1)

\------------------------------------------------------------------------------

1.  No RemoteUtranCells with same cId as a local UtranCell or another RemoteUtranCell within each CM: NO cId=2202 UtranCell=cell2202-Iub-1525-2 UtranCell=cell2201-Iub-1525-1 (CM1) cId=2205 UtranCell=cell1106-Iub-1523-6 UtranCell=cell2205-Iub-1525-5 (CM1) cId=1201 UtranCell=cell1201-Iub-1526-1 UtranCell=cell2204-Iub-1525-4 (CM1) ------------------------------------------------------------------------------
2.  No unlocked disabled secondary IubLinks when redundancySwitchoverWaitTime=-1: NOT OK

IubLink=Iub-1523 (CM1)

IubLink=Iub-1525 (CM2)

\------------------------------------------------------------------------------

Example printout from iro command:

The iro printout consists of 3 tables.

- - The first two tables show the status of IubLinks and associated UtranCells, one line per IubLink unless it has more than 12 cells in which case the IubLink will take two lines. Redundant-Primary and Non-Redundant IubLinks are shown on the left, Redundant-Secondary are shown on the right. For description about how to interpret the different columns, refer to the help of the str3 command.

\--------------------------------------------------------------------------------------------------------------------

IUBLINK RNC MOD TN R ICDS C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 RNC MOD TN R ICDS C01 C02 C03 C04 C05

\--------------------------------------------------------------------------------------------------------------------

Iub-1 CM1 1062 I P 1111 1 1 1 CM2 1162 I S 0000 0 0 0

Iub-10 CM1 1061 I P 1111 111 111 111 111 111 111 CM2 1163 I S 0000 000 000 000 000 000

Iub-44 CM1 2221 I N 1111 111 111 111 111 111 111 111 111 111

Iub-569 CM2 3081 I P 0000 000 000 000 000 000 000 000 000 000 000 000 000 CM1 3071 I S 1111 111 111 111 111 111

- - The third table summarizes the total availability for all IubLinks and UtranCells in the RNC pool. In each column, the first number is the number of MOs up , and the second value is the total number of MOs, then the The line "IubLinks" is the availability of IubLink MOs, "UtranCells" is for UtranCell MOs, "HS channels" is for Hsdsch MOs, and "EUL channels" is Eul MOs. The column "Total" indicates the total availability, with and without iub redundancy, and should always be equal to the sum of the next two columns "Non-Redundant" and "Redundant". The column "Redundant-Normal" indicates the total availability of redundant sites which are not switched, while "Redundant-Switched" gives the availability of sites that are switched. The sum of the values in the last two columns should always be equal to the values in the column "Redundant".

\------------------------------------------------------------------------------------------------------------------

Availability Total Non-Redundant Redundant Redundant-Normal Redundant-Switched

\------------------------------------------------------------------------------------------------------------------

IubLinks 818/818 (100%) 273/273 (100%) 545/545 (100%) 108/108 (100%) 437/437 (100%)

Cells 6357/6357 (100%) 2121/2121 (100%) 4236/4236 (100%) 840/840 (100%) 3396/3396 (100%)

HS channels 6135/6135 (100%) 2043/2043 (100%) 4092/4092 (100%) 807/807 (100%) 3285/3285 (100%)

EUL channels 5691/5691 (100%) 1884/1884 (100%) 3807/3807 (100%) 747/747 (100%) 3060/3060 (100%)

\------------------------------------------------------------------------------------------------------------------

**4.2.24 rinp\[c\]\[m\] &lt;/path/to/rinpm.json&gt;**

Live Node Migration to RNC in Pool. Only applicable for RNC <= 21.Q1.

**Options:**

- - c: perform a precheck to make sure both nodes are in correct state prior to the migration.
    - m: perform the live node migration.

**Arguments:**

- - rinpc: no arguments are necessary if the other cluster member has been specified in the uservariable cluster_members. If the uservariable cluster_members is empty, then the IP address of the other cluster member can be specified in the second argument, eg: rinpc . &lt;ip_of_other_RNC&gt; (same syntax as irc command)
    - rinpm: mandatory argument is the path of a .json file where all parameters shall be listed. Example of json file can be found under moshell/commonjars/rinpm/rinpm.json

**4.2.25 gr\[acdfprsx\] \[&lt;IubLink&gt;\] \[&lt;OtherRNC&gt;\]**

Geo-Redundancy operations for RNC.

For more details regarding feature configuration for multiple RNCs, refer to RNC CPI document "Configure Geo-Redundancy". Note: in the CPI, the terms "set redundancy" and "delete redundancy" are referred in this help as "protect" and "remove protection".

**Arguments**:

- - &lt;IubLink&gt;: MO filter specifying the Iub links which should be affected. Mandatory argument for all options except c and r. usage examples: ’IubLink=’, ’IubLink=Iub-123’, ’IubLink=(Iub-123|Iub-456)’
    - &lt;OtherRNC&gt;: the address of the other RNC, which can be an IP address or the full path to an MO dump (relative path is not supported).

Command argument &lt;OtherRNC&gt; must be an IP address or MO dump of the other RNC from the RNC pair.

If command is executed with argument &lt;OtherRNC&gt; of a wrong RNC, returned results are invalid and unexpected errors could be returned.

In non-interactive mode uses variables $grr_external_cells_file, $grxcommandfile and $grr_variant. See r option description for details.

**Options**:

- - a: Minimize WCDMA cell relations reconfiguration during Iub switchover (option x), so ANR feature can handle it. Can be used only together with option x. ANR feature must be active on the RNC.
    - c: Consistency check of the Geo-Redundancy feature.

Generates a printout listing all the checks and their result.

IubLink argument is not supported.

If redundant Iub links are detected without corresponding primary Iub links in the other RNC, they will be saved in the variable $grc_orphan_iublinks and can be removed with the command grd $grc_orphan_iublinks.

If missing redundant Iub links are detected for primary Iub links configured in the other RNC, they will be saved in the variable $grc_new_iublinks and can be protected with the command grp $grc_new_iublinks &lt;OtherRNC&gt;.

- - d: Generate a command file to delete protection for redundant Iub links.

Only Iub links with poolRedundancy set to SECOND_GEO_INACTIVE(5) are affected. Use option f to also delete

protection for Iub links with poolRedundancy set to SECOND_GEO_ACTIVE(4).

A command file will be generated to delete the redundant Iub links and all associated configuration.

The command file shall be executed in the same RNC where the command was run and the file path can be accessed from the variable $grdcommandfile.

- - f: Force deleting protection of active redundant Iub links - poolRedundancy set to SECOND_GEO_ACTIVE(4). Can be only used together with option d.
    - p: Generate a command file to protect Iub links.

OtherRNC argument is mandatory.

Only Iub links with poolRedundancy set to PRIMARY_GEO(3) in the other RNC are considered by the command.

Command file will be generated to create redundant Iub links and all associated configuration.

The command file shall be executed in the same RNC where the command was run and the file path can be accessed from the variable $grpcommandfile. Command execution with option p is aborted if used towards more than one primary RNCs.

- - r: Generate the Iub rollback command file for the current RNC.

The &lt;IubLink&gt; argument is not supported.

The &lt;OtherRNC&gt; argument is mandatory for variant 2 (see the description below).

A command file will be generated to deactivate redundant Iub links and reconfigure affected cell relations.

The command file shall be executed in the same RNC where the command was run and the file path can be accessed from the variable $grrcommandfile.

The command uses input file generated by grx command to restore external cell relations (stored by grx command in

$grr_external_cells_file location).

The command has two variants - if ANR is active on the RNC, only variant 2 is supported.

Variant 1. Based only on specified input files generated on the same RNC by grx command. Generates undo command file for input files selected from the list or specified by the path. Variant 1 omits IubLink parameter.

Variant 2. Based only on current RNC configuration in state after Iub switchover action and input file generated by grx command. Generates a command file that updates all cell relations for the specified Iub links. Variant 2 is only supported in state after Iub switchover action execution.

The variant and input files are chosen by the user in interactive mode. In non-interactive mode variant is selected by the variable $grr_variant (default 2) and input files are specified by the variables $grxcommandfile (variant 1 only) and $grr_external_cells_file (optional).

• s: Generate a command file to synchronize the configuration of redundant Iub links.

OtherRNC argument is mandatory.

Only Iub links with poolRedundancy set to SECOND_GEO_INACTIVE(5) will be considered by the command.

A command file will be generated to update the configuration of redundant Iub links with the one from other RNC, where those Iub links have poolRedundancy set to PRIMARY_GEO(3).

The command file shall be executed in the same RNC where the command was run and the file path can be accessed from the variable $grscommandfile.

If redundant Iub links are detected without corresponding primary Iub links in the other RNC, they will be saved in the variable $grs_orphan_iublinks and can be removed with the command grd\[f\] $grs_orphan_iublinks. If missing redundant Iub links are detected for primary Iub links configured in the other RNC, they will be saved in the variable $grc_new_iublinks and can be protected with the command grp $grs_new_iublinks &lt;OtherRNC&gt;.

• x: Generate the Iub switchover command file for the current RNC.

OtherRNC argument is mandatory.

Only Iub links with poolRedundancy SECOND_GEO_INACTIVE(5) will be considered by the command.

A command file will be generated to activate redundant Iub links and reconfigure affected cell relations. Use option a to minimize reconfiguration of WCDMA cell relation, so the ANR feature can handle it instead

The command file shall be executed in the same RNC where the command was run and the file path can be accessed from the variable $grxcommandfile.

Additional command file can be generated to be used later by grr command to restore external cell relations, if applicable. The file path can be accessed from the variable $grr_external_cells_file. It is recommended to copy both files to safe location for future use.

In case of mismatch between the primary and redundant Iub links configuration of the RNCs the error will be shown and faulty Iub links will be omitted.

Two additional command files will be generated for the later use.

1.The first file can be accessed from the variable $grr_external_cells_file and it can be used by grr command to restore external cell relations, if applicable.

2.The second file can be accessed from the variable $grx_drnc_file and it can be used to update external cell relations in the connected DRNC nodes after Iub switchover.

**Examples:**

- Configuration check with other RNC (IP address 127.0.0.1):

grc 127.0.0.1

- Configuration check with other RNC (MO dump path /home/user/OTHER_RNC_MO_dump.zip):

grc /home/user/OTHER_RNC_MO_dump.zip

- Generate a command file to protect all Iub links with poolRedundancy set to PRIMARY_GEO in other RNC (IP address

127.0.0.1):

grp IubLink= 127.0.0.1

- Generate a command file to protect selected Iub links Iub-1523 and Iub-1524 with poolRedundancy set to PRIMARY_GEO in other RNC (IP address 127.0.0.1):

grp IubLink=(Iub-1523|Iub-1524) 127.0.0.1

- Generate a command file to protect selected Iub links stored in variable $grs_new_iublinks with poolRedundancy set to PRIMARY_GEO in other RNC (IP address 127.0.0.1):

grp $grs_new_iublinks 127.0.0.1

- Generate a command file to perform Iub switchover for all Iub links with poolRedundancy set to SECOND_GEO_INACTIVE: grx IubLink= 127.0.0.1
- Generate a command file to perform Iub switchover for all Iub links with poolRedundancy set to SECOND_GEO_INACTIVE, minimize WCDMA cell relations reconfiguration , so ANR feature can handle it grxa IubLink= 127.0.0.1
- Generate a command file to perform Iub rollback for all redundant Iub links, Iub switchover not performed - variant 1 of grr command: grr

In interactive mode choose proper command files generated by the grx command.

- Generate a command file to perform Iub rollback for all redundant Iub links, Iub switchover already performed - variant 2 of grr command (IP address of other RNC 127.0.0.1): grr 127.0.0.1

In interactive mode choose proper command file generated by the grx command.

- Generate a command file to perform Iub rollback in non-interactive mode for all redundant Iub links, Iub switchover not performed - variant 1 of grr command:

$grr_variant = 1

$grxcommandfile = &lt;path to the command file generated by grx command&gt;

$grr_external_cells_file = &lt;path to the additional command file generated by grx command, optionally used to restore external cell relations&gt; grr

- Generate a command file to perform Iub rollback in non-interactive mode for all redundant Iub links, Iub switchover already performed - variant 2 of grr command (IP address of other RNC 127.0.0.1):

$grr_variant = 2

$grr_external_cells_file = &lt;path to the additional command file generated by grx command, optionally used to restore external cell relations&gt; grr 127.0.0.1

- Generate a command file to remove protection for all redundant Iub links (IP address of other RNC 127.0.0.1):

grd IubLink= 127.0.0.1

- Generate a command file to remove protection for all redundant Iub links, including active redundant Iub links (IP address of other RNC 127.0.0.1):

grdf IubLink= 127.0.0.1

- Generate a command file to synchronize configuration of all redundant Iub links (IP address of other RNC 127.0.0.1):

grs IubLink= 127.0.0.1

**4.2.26 tg\[r\]\[c\]\[d\]**

Print Resource Object information for all MOs in LmCell (RNC only).

Command Syntax:

tg\[c\]\[r\] \[&lt;mofilter&gt;|&lt;mogroup&gt;|&lt;fro&gt;\]\[:&lt;actorChildren&gt;\] \[&lt;rrt-cmd&gt;\] \[|&lt;unix-cmds&gt;\] tgd \[&lt;mofilter&gt;|&lt;mogroup&gt;|&lt;fro&gt;\]\[:&lt;actorChildren&gt;\] \[&lt;cell-parameter(s)&gt;\]

Purpose:

- To print the relation MO&lt;—&gt;FRO&lt;—&gt;ACTOR&lt;—&gt;CCDEVICE for **IubLink** and **UtranCell** MOs.
- To send RRT commands to Cell/Iub actors or their children in the actor tree.

**Arguments:** By specifying the first argument, it is possible to filter the Cell/Iubs matching a specific FroId or MOid.

By specifying a second argument consisting of an RRT command or a list of cell parameters, it is possible to run an RRT-command or display certain cell parameters on all the actors that are matched by the first argument.

The list of available RRT commands can be seen by typing:

- lhsh 001400 ? rrt

The list of available cell parameters can be seen by typing:

- lhsh 001400 rrt-CXC132xxxx_Ryyyy 1/1/1/1/2/1.1 info (for cell parameters)
- lhsh 001400 rrt-CXC132xxxx_Ryyyy 1/1/1/1/7/1.1/4/1 info (for nbap common parameters)

The printout can be piped into unix commands, like grep and sort.

**Options:**

- r : to refresh the MO/FRO/ACTOR data. Otherwise this data is reused within the moshell session and from session to session, using a cache on the workstation disk. A tg refresh (tgr) needs to be done after a node upgrade or if some **IubLinks** or **UtranCells** have been added/removed/remoduled. Otherwise you may get error messages such as unknown command rrt-CXC1328831_Rxxx (eg, the rrt LM has changed after an upgrade).
- c : print the following extra extra fields:
    - Common Channel Device (**ccDevice**): shows which SPM is used to handle the common channels of this cell
    - ccDevice Module (**ccMod**): shows if a ccDevice is running on an SPM that doesn’t belong to the same module as the Cell/Iub. This can be fixed by locking/unlocking the cell. It is always best to make sure that all cells are using a ccDevice located in their own module so that the load will be spread equitably on all ccDevices.

Note that ccDevice data is not kept in the cache, only MO/fRO/Actor relation is kept in the cache.

- d : to print certain cell-parameters for all cells matching the first argument.

**Examples:**

1.  tg - to view the fRO/Actor data for each **UtranCell** and **IubLink**
2.  tg cell=302 - to view the fro/actor data for all UtranCell MOs matching regex cell=302
3.  tg cellmod1 - to view the fro/actor data for all MOs belonging to the MO group cellmod1 (use **ma** command to make a MO group)
4.  tg 67 - to view the mo/actor data for the MOs that have fro=67
5.  tgr - to refresh the fro/actor data
6.  tgc - to view all cells/iubs and their respective fro/actor and ccDevice (Note: ccDevice data is not cached so if it is not necessary to do tgr to refresh ccDevice data)
7.  tg iublink=3.\*1$ info - to run the rrt info command on all actors whose MO matches iublink=3.\*1\\$
8.  tgc | grep 0019 to see all cells that are on ccdevice of board 001900
9.  tg cell getattr cellData - to send the rrt command getattr cellData on all actors whose MO matches cell
10. tg iubmod3 state - to run the rrt command state on all MOs belonging to the MO group iubmod3 (use **ma** command to make a MO group)
11. tgd cell ulinterference celldata:errorstatus cellRoState - to view the cell parameters ulinterference,celldata:errorstatus,etc. on all cells (P3/P4)
12. tgd cell:/8/3 cellLoadMonitor:totAseDl cellLoadMonitor:totAseUl cellLoadMonitor:currDlCode
    - to view the admission tree usage on all cells (P5 and after) 13. tgd cell ulinterference celldata:errorstatus celldata:spconfigflag cellRoState
    - to view the cell parameters ulinterference,celldata:errorstatus,etc. on all cells.

14\. tgd cell cellLoadMonitor:totAseDl cellLoadMonitor:totAseUl cellLoadMonitor:currDlCode - to view the admission tree usage on all cells. 15. tgd cell ulinterference celldata:spblocked celldata:spconfigflag cellRoState celldeleted cellTraceActivated celldata:errorstatus

16\. tgd iub:/4/1 activeStatus standbyStatus currentCause

currentAvailabilityStatus rncRbsLinkLossOfRedundancy rncRbsLinkDown rncRbsDeactivated

\- to view those attributes on all the NbapCommon actors

Output examples:

• tgc

\------------------------------------------------------------------------------------

MOD MFRO ModMP UtranCellId IubLinkId CfRO IfRO CellActor IubActor CcDev

\------------------------------------------------------------------------------------

1 0 001400 90121 9012 5 1 1/1/1/1/2/1.3 1/1/1/1/7/1.1/4 0019SP2

1 0 001400 90122 9012 4 1 1/1/1/1/2/1.2 1/1/1/1/7/1.1/4 0020SP0

1 0 001400 90123 9012 3 1 1/1/1/1/2/1.1 1/1/1/1/7/1.1/4 0020SP0

- tgd cell=9012 ulinterference celldata:spblocked celldata:spconfigflag cellRoState celldeleted cellTraceActivated celldata:errorstatus

\---------------------------------------------------------------------------------------------------------------------------

MO ulinterference spblocked spconfigflag cellrostate celldeleted errorstat celltraceactivated

\---------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| UtranCell=90121 | \-106 | 0   | 0   | 2   | 0   | 0 0 |
| UtranCell=90122 | \-100 | 0   | 0   | 1   | 0   | 16002:CellNoDrhResources 0 |
| UtranCell=90123 | \-100 | 0   | 0   | 1   | 0   | 16002:CellNoDrhResources 0 |

Description:

- spblocked=1 means that the CCdevice has crashed and Rnh got the signal clearResourceReq.
- spconfigflag says if the cell has allocated SP resources or not. Should be 0 if spblocked=1.
- cellrostate is defined in the header file rlibRncConst.h: roStateNOK=1, roStateOK=2, roStateDepNOK=3
- celldeleted means that the cell has been deleted by the operator, i.e. FRO has sent a deleteInd.
- celltraceactivated says if the feature "Selective Cell Tracing" is active or not. See CR WRNac20241
- errorstatus is different to 0 if there is a fault in the cell unlock procedure. Range 16000-16014 is specified in the file rlibEventNr.h. Cellrostate shall be equal to 1 if the errorstatus is different to 0.
- tgd iub:/4/1 activeStatus standbyStatus currentCause currentAvailabilityStatus rncRbsLinkLossOfRedundancy rncRbsLinkDown rncRbsDeactivated to view those attributes on all the NbapCommon actors

\----------------------------------------------------------------------------------------------------------------

MO activestatus standbystatus currentcause currentavailabilitystatus rncrbslinkdown rncrbsdeactivated

\----------------------------------------------------------------------------------------------------------------

IubLink=1001 1 1 2 2 0 0

IubLink=1002 1 1 2 2 0 0

\----------------------------------------------------------------------------------------------------------------

Description:

- activeStatus and standbyStatus are boolean (0 or 1). It’s the FRO’s way to say if it’s ok or not to attach to USAAL. UserPlaneCepId for active and standby shall be different to -1 if active/standby status equals 1.
- currentCause is sent by FRO in the signals opStateChdInd and setAttribInd and is defined by the dataclass CpxUsaalEfi_OpStateChangeCauseD. Valid values are:
    - - CELLO_USAALEFI_SERVER_RESTARTED == 1
        - CELLO_USAALEFI_OTHER == 2
        - CELLO_USAALEFI_SERVER_MOVED == 3 (introduced in the feature Moveable CEP in P5MD)
- currentAvailabilityStatus comes together with opStateChdInd and is about "regular" state propagation, i.e. if bit 5 is set to NBAP RO Dependency Failed.
- rncRbsLinkLossOfRedundancy & rncRbsLinkDown are internal flags that say if the events linkDown and linkLossOfRedundancy are active or not. If rncRbsLinkDown=1 then currentAvailabilityStatus will be "Dependency Failed" and linkUsedForTraffic will be equal to -1.
- linkUsedForTraffic says which iublink we are using at the moment. Active == 0, Standby == 1. If linkUsedForTraffic equals 1 (standby) then rncRbsLinkLossOfRedundancy is also equal to 1.
- rncRbsDeactivated says if the event linkDeactivated is active or not. All 3 events are defined in header file rlibEventNr.h.
- tgd cell:/8/3 cellLoadMonitor:totAseDl cellLoadMonitor:totAseUl cellLoadMonitor:currDlCode to view those attributes on all the NbapCommon actors

\-------------------------------------------------------------------------------------------------------------------------------

MO totasedl totaseul currdlcode

\-------------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |
| --- | --- | --- | --- |
| UtranCell=30101 | 320 | 160 | 3750 |
| UtranCell=30102 | 0   | 0   | 3593 |
| UtranCell=30103 | 0   | 0   | 3593 |
| UtranCell=30104 | 1940 | 969 | 4218 |
| UtranCell=30105 | 2064 | 1568 | 4375 |
| UtranCell=30106 | 991 | 911 | 3984 |

\-------------------------------------------------------------------------------------------------------------------------

Description:

- totAseDl is the total amount of DL ASE that is currently in use in the cell. The value is scaled by a factor 100 to get a resolution of 0.01 ASE, i.e. totalAseDl = 1280 means 12.80 ASE DL load in the cell.
- totAseUl is the same as totAseDl but for UL ASE. DL and UL ASE values are controlled by UEH (by signals admissionRequest, admissionDecreaseLoadInd, admissionAseUlIncreaseInd and admissionAseUlDecreaseInd).
- currDlCode reflects the last reported value of DL code tree load utilization in the cell (reported from the RnhCode block by signal codeTreeLoadInd). The value is scaled by factor 100 to get a resolution of 0.01

**4.2.27 ueregprint/uer\[d\]\[t\]\[i\]\[s\]\[p\]\[v\] \[-m &lt;mod&gt;|-i &lt;imsi&gt;|-u &lt;ueref&gt;|-n &lt;maxUes&gt;|-c &lt;utrancell&gt;|-r &lt;iublink&gt;\] \[&lt;attribute-filter&gt;\[=&lt;value&gt;\]|all\]**

Print UE registry or UE context data (serving or drifting) for all active calls (RNC only).

The command ueregprint is a moshell alias that runs the coli command "ueregprint" on all RNC RANAP boards. It allows all the same arguments as the regular ueregprint command but does not require to specify the board on which it should run. This is especially useful for EvoC node where the UE registry is running in all the blades.

Example:

- ueregprint sum
- ueregprint all

The command uer is a moshell command that prints the UE contexts in each module MP in order to show the details of call.

The following COLI commands are used: ueregprint (on C2/Ranap MP), drh_trbr rab (on PDR module MPs), and printUeCtxt (on module MP). No RRT commands are used.

**Options:**

- s: for showing the traffic summary tables at the end of the printout.

When no filtering options are used (e.g. uers command is run on its own) then only the summary tables are shown, not the individual calls.

When filtering options are used but the s switch is not given (e.g. uer \[-option &lt;filter&gt;\]), then the summary tables are not shown, only the individual calls.

- d: for printing drift UEs.
- i: for printing UEs that have a IMSI only.
- t: for printing UEs that have a TMSI or IMEI only.
- p: for skipping the PDR device check, faster.
- v: for printing UE context attributes vertically, only applies when used with the attribute-filter

Filtering Options:

- \-m &lt;mod&gt;: to show calls belonging to certain module(s) only. Eg: -m 1,8 ==> calls in modules 1 and 8 are printed.
- \-i &lt;imsi&gt;: to show calls whose IMSI match a specific filter only. Eg: -i 3014235.
- \-u &lt;ueref&gt;: to show the calls related to a specific UE ref. Eg: -u 4728.
- \-n &lt;maxUes&gt;: to show a maximum number of calls only. Eg: -n 50 ==> a maximum of 50 calls are printed.
- \-c &lt;utrancell&gt;: to show the calls that have a radio link or common channel in certain utrancells.
- \-r &lt;iublink&gt; : to show the calls that have a radio link or common channel in certain iublinks.

Note regarding the options -c/-r:

- on RNC >= P6, a regular expression filter can be used, e.g. uer -c 30.\*a
- on RNC =< P5, the exact utrancell or iublink must be given, e.g. uer -r iub_10

The attribute-filter can be:

- empty. Some default tables will be printed, see below.
- "all". All UeContext data for the UEs matching the first argument will be printed
- a regular expression matching one or more UeContext attributes. Only the attributes matching the string will be printed.
- an attribute name followed by "=" and a value (e.g. sccpConnId=6). Only the UEs that have an attribute matching that value will be printed.

If the attribute-filter is empty, then three tables are printed:

- The first table contains for each UeContext:
    - - MOD: the module handling the call
        - IMSI: the IMSI of the UE
        - CTXT: the UeContext (UeRef) id of the UE
        - SRNC: the Serving RNC. Read from the variable sRncId.
        - CommCh: the rbsid and cell id (cid) of the serving cell providing the Common Channels for this UE. Read from the variable commonResData.cId
        - RL1-4: the rbsid and cell id (cid) of the serving cells providing the radio links for this UE (up to 4 radio links per UE). Read from the variables radioLink\[0-3\].cId
        - DCdev: the DC device handling the call. Read from the variable drhRcSpId.
        - PDRdev: the PDR device and PacketDataRouter froId handling the call. Read from the command lh mod drh_trbr rab.
        - CoreNetId: the Type of Core Network connecting the call: CS or PS. Read from the variables isCNConnected.\*Circuit and isCNConnected.\*Packet. Also shows the Id of the Core Network used for the call (mcc/mnc/cnId). Read from the variables globalCnIdPs and globalCnIdCs.
        - AGE: the duration of the call. Read from lh ranapmp ueregprint all **–** UERC: the UeRc used by the call. Read from the variable connType.
- the second table shows the current number of Ue Contexts associated to each UeRc type in each module.
- the third table shows the same as the second table but for the whole node.

Examples (with empty attribute-filter):

- uer - print UeContext data for all UEs in the node
- uer -n 25 - print UeContext data for 25 UEs only (randomly selected across the node and proportionately spread across all the modules)
- uer -i 0001 - print UeContext data for all UEs whose IMSI match 0001.
- uer -m 8 - print UeContext data for all UEs in module 8.
- uer -m 8,9,10 - print UeContext data for all UEs in modules 8, 9 and 10.
- uer -r iub-17 - print UeContext data for all UEs that have a radio link or common channel in a cell of IubLink "Iub-17"
- uer -c iub-17-1 - print UeContext data for all UEs that have a radio link or common channel in the UtranCell "Iub-17-1"
- uer -r iub.\*1$ - print UeContext data for all UEs that have a radio link or common channel in the IubLinks whose name matches iub.\*1$ (works only on RNC P6 and above) See output example below:

\=========================================================================================================================

MOD IMSI/TMSI CTXT CommCh RL1 RL2 RL3 DCdev PDRdev CoreNetId AGE UERC + ESTAB_CAUSE

\=========================================================================================================================

1 301020430130001 1826 746:2907 20:1174 0923sp3 P 24099 5 Interact. PS (64/64) (2:origInteractive)

1 301001920070001 287 68:1178 0022sp2 0019sp0:1 P 24099 00:00:52 5 Interact. PS (64/64) (2:origInteractive)

1 301000310030000 309 298:1875 0021sp3 0019sp0:0 CP 24099 00:01:28 9 Conv. CS speech 12.2 + Interact. PS (0/0) (2:origInteractive)

1 301010330100000 5778 680:2951 0923sp3 0019sp0:0 P 24099 00:01:59 4 Interact. PS (RACH/FACH) (2:origInteractive) 1 301001630000000 5565 582:2848 71:1205 0023sp2 C 24099 00:00:14 2 Conv. CS speech 12.2 (0:origConversational)

...&lt;cut&gt;...

\=====================================================

UeRc M1 M8 M13 userLabel

\=====================================================

1.  14 13 4 Standalone RRC on DCH
2.  75 55 55 Speech
3.  18 30 22 64kbps CS data, fixed rate
4.  13 9 17 Packet RACH/FACH
5.  5 1 2 PACKET 64/64

7 1 0 0 Packet 64/384

9 0 0 1 Speech + Packet 0kbps

14 0 0 1 CS data 64kbps + Packet 8/8

16 1 0 0 PS Interactive 384/HS - HS-DSCH

18 1 0 0 Packet 128/128

\=====================================================

Tot: 128 108 102

\=====================================================

Cause M1 M8 M13 EstablishmentCause

\=====================================================

0 65 46 57 origConversational

2 22 13 22 origInteractive

5 30 40 19 termConversational

12 11 9 4 registration

\=====================================================

Tot: 128 108 102

\===============================================

UeRc Total % userLabel

\===============================================

1.  31 9.2 Standalone RRC on DCH
2.  185 54.7 Speech
3.  70 20.7 64kbps CS data, fixed rate
4.  39 11.5 Packet RACH/FACH
5.  8 2.4 PACKET 64/64

7 1 0.3 Packet 64/384

9 1 0.3 Speech + Packet 0kbps

14 1 0.3 CS data 64kbps + Packet 8/8

16 1 0.3 PS Interactive 384/HS - HS-DSCH

18 1 0.3 Packet 128/128

\===============================================

Tot: 338 100

\===============================================

Cause Total % EstablishmentCause

\===============================================

0 168 49.7 origConversational

2 57 16.9 origInteractive

5 89 26.3 termConversational

12 24 7.1 registration

\===============================================

Tot: 338 100

Examples (with attribute-filter not empty):

- uer -i 301001800040001 all - print all UeContext data for the UE with IMSI 301001800040001

\==================================================================================

MOD IMSI ATTRIBUTES

\==================================================================================

|     |     |
| --- | --- |
| 8 301001800040001 $ UehUexCtxtD\[1022\]=0x4FE0D058 |     |
| 8 301001800040001 | \[1022\].isActive() = 1 |
| 8 301001800040001 | \[1022\].isCNConnected(uehCNidCircuit) = 0 |
| 8 301001800040001 | \[1022\].isCNConnected(uehCNidPacket) = 1 |
| 8 301001800040001 | \[1022\].sRncId = 301 |
| 8 301001800040001 | \[1022\].softHoDone = 1 |
| 8 301001800040001 | \[1022\].isPmRecordingActive = 0 |
| 8 301001800040001 | \[1022\].recordingProt = 1 |
| 8 301001800040001 | \[1022\].dlPcMethod = 3 |
| 8 301001800040001 | \[1022\].dlRefPwrVal = -165 |
| 8 301001800040001 | \[1022\].supportOfGsm = 1 |
| 8 301001800040001 | \[1022\].tmpRanapConnId = -1 |
| 8 301001800040001 | \[1022\].recordingMeas = 0 |
| 8 301001800040001 | \[1022\].measBERrequested = 0 |
| 8 301001800040001 etc..... | \[1022\].measBLERrequested = 0 |

- uer . aal2.\*cepid$|softho|\\.rcindex$ - for all UEs, print UeContext attributes that match the regexp

"aal2.\*cepid$|softho|˙rcindex$"

\=========================================================================================================================

MOD IMSI ATTRIBUTES

\========================================================================================================================= 1 301001800060003 softHoDone=1 rcIndex=4

1 301001701000000 softHoDone=0 rcIndex=2 aal2Arr\[0\].cepId=477 aal2Arr\[1\].cepId=494

1 301001810040000 softHoDone=1 rcIndex=4

1 301001700000001 softHoDone=1 rcIndex=2 aal2Arr\[0\].cepId=76 aal2Arr\[1\].cepId=77 aal2Arr\[2\].cepId=141 aal2Arr\[3\].cepId=142

1 301001720000003 softHoDone=1 rcIndex=2 aal2Arr\[0\].cepId=507 aal2Arr\[1\].cepId=508 aal2Arr\[2\].cepId=332 aal2Arr\[3\].cepId=333

1 301001720110001 softHoDone=1 rcIndex=2 aal2Arr\[0\].cepId=424 aal2Arr\[1\].cepId=425

1 301001810000003 softHoDone=1 rcIndex=2 aal2Arr\[0\].cepId=476 aal2Arr\[1\].cepId=482 aal2Arr\[2\].cepId=166 aal2Arr\[3\].cepId=167

1 301001711000002 softHoDone=1 rcIndex=2 aal2Arr\[0\].cepId=52 aal2Arr\[1\].cepId=57 aal2Arr\[2\].cepId=170 aal2Arr\[3\].cepId=171

- uer -i 001 sccpConnId=6 - for all UEs whose IMSI match "001", print the UeContact attributes that match sccpConnId=6

Note: to abort the printout, do Ctrl-z, then: touch &lt;stopfile&gt; ; fg The path to the _stopfile_ can be found in the window title.

**4.2.28 ced\[h\]\[p\]\[s\]\[g\]\[r\] \[-m &lt;module(s)&gt;|-c &lt;utrancell&gt;|-r &lt;iublink&gt;|-s &lt;rsite&gt;\] \[ | &lt;unix-cmds&gt;\]**

Print consumption of cell resources and rbs hw, cell supported features, cell coordinates (RNC only).

**Options:**

- ced : consumption of air interface resources for each UtranCell. Read from the coli command "celldata" on module MPs.
- cedh : CE consumption (Channel Element) and number of RadioLinks/UEs for each IubLink. Read from the coli command "hwm" on module MPs.
- cedhp: same as above but the CE usage is expressed in percentage.
- cedg : state and geographical coordinates of each UtranCell. Read from MO data on UtranCell and children.
- ceds : state and supported features of each UtranCell. Read from MO data on UtranCell and children.

The r option can be used together with any of the above, in order to clear the moshell cache and fetch latest values from the node.

Filters:

- \-m &lt;module(s)&gt;: only fetch/parse the data for certain RncModules, e.g. -m 8 or -m 1,2,3
- \-c &lt;utrancell&gt;: only fetch/parse the data for specific UtranCells, e.g. -c cell304A (not case sensitive)
- \-r &lt;iublink&gt; : only fetch/parse the data for specific IubLinks, eg. -r iub_304 (not case sensitive)
- \-s &lt;rsite&gt; : only fetch/parse the data for specific RSites, eg. -s iub-304-305-306 (not case sensitive) The output can be filtered by piping through some unix commands, eg. grep or sort.

**Examples:**

|     |     |     |
| --- | --- | --- |
| •   | ced \| grep 0019sp0 | : print all cells configured on CC device 001900/sp0 |
| •   | ced \| sort -k 5 | : print cell data sorted on the fifth field |
| •   | cedh -m 8,9,10 | : print CE usage for all sites in modules 8, 9, 10. |
| •   | ced -r iub_304 | : print cell data for all cells belonging to IubLink=Iub_304 |
| •   | cedh -c cell304a | : print CE usage for the site connected to UtranCell=cell304A |
| •   | cedg -c cell40 | : print state and geographical coordinates for all cells matching "cell40" |
| •   | ceds -r iub_56 | : show state and supported features for all cells connected to Iubs matching "iub_56" |

Printout format:

\> ced

\---------------- ------------------------------------------------------------------------------------------------------------------------------------------------

MOD CELL cid fro ro PwrDl/Adm dlCode ulInt sf8d sf8u sf16d sf16u sf32d sf4u dlASE ulASE CPMcnt HScnt EULs EULns Eul2 Spch Fdcph Crn Hrn Ern CC_SP

\---------------- ------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 Iub-1-1 1031 | 0 0 7.0% 75% 6.2% -111.8 0/8 0/8 0/16 0/16 0/32 0/4 0/500 0/500 | 0/15 0/10 1/32 0/100 0/4 | 0   | 0/0 | 0   | 0   | 0 1:0019sp1 |
| 1 Iub-1-2 1032 | 1 2 7.0% 75% 6.2% -111.8 0/8 0/8 0/16 0/16 0/32 0/4 0/500 0/500 | 0/15 0/10 4/32 0/100 0/4 | 0   | 0/0 | 0   | 0   | 0 1:0021sp1 |
| 1 Iub-1-3 1033 | 2 3 7.0% 75% 22.9% -111.8 1/8 0/8 0/16 1/16 0/32 0/4 39/500 8/500 | 0/15 0/10 3/32 0/100 0/4 | 0   | 0/0 | 0   | 0   | 0 1:0019sp1 |
| 1 Iub-2-1 1037 | 6 1 7.0% 75% 24.6% -111.8 1/8 0/8 0/16 2/16 1/32 0/4 53/500 20/500 | 0/15 0/10 0/32 0/100 0/4 | 0   | 0/0 | 0   | 0   | 0 1:0019sp1 |
| 1 Iub-2-2 1038 | 7 4 7.0% 75% 10.8% -111.8 0/8 0/8 0/16 2/16 1/32 0/4 12/500 19/500 | 0/15 1/10 0/32 0/100 0/4 | 0   | 0/0 | 0   | 0   | 0 8:0023sp1(!) |

The fields in the "ced" printout correspond to the following variables in the "celldata" printout on Module MP:

- MOD: RNC Module
- cid: cId
- fro: cellFroId (facade resource object, a unique id in the node)
- ro: cell RO (resource object, a unique id in the module. Same as capsule index.)
- PwrDl/PwrAdm: Filtered DL Power / pwrAdm
- dlCode: DL Code Allocation Level
- ulInt: UL Interference
- sf8dl: SF8 RL DL Count / sf8Adm
- sf8ul: SF8 RL UL Count / sf8AdmUl
- sf16dl: SF16 RL DL Count / sf16Adm
- sf16ul: SF16 RL UL Count / sf16AdmUl
- sf32dl: SF32 RL DL Count / sf32Adm
- sf4ul: SF4 RL UL Count / sf4AdmUl
- dlASE: Total ASE DL / aseDlAdm
- ulASE: Total ASE UL / aseUlAdm
- HScnt: HSDPA UE Count / hsdpaUsersAdm
- EULs: EUL UE Count serving / eulServingCellUsersAdm
- EULns: EUL UE Count non-serving / eulNonServingCellUsersAdm
- EUL2ms: EUL2ms UE Count serving / eulServingCellUsersAdmTti2
- Spch: Speech Only UE Count
- SpchG: Speech General UE Count
- CPMcnt: CPM RL Count / compModeAdm
- Crn: Crnti allocation count
- Hrn: Hrnti allocation count
- Ern: Ernti allocation count
- Fdcph: This columns is read from the command "admtimeposdata". The first number corresponds to the number of opened codes and the second number is the number of time positions.
- CC_SP: The RncModule and SPM of the CC device handling the Cell. If the RncModule controlling the CC device is different from the one controlling the cell, an exclamation mark (!) is printed. This used to be an issue in older RNC SW (PLM info 510), but is now fixed with TR HN89801, refer to PLM info 749.

\> cedh

\-------------------------------------------------------------------------------------------------------------------------------------------

MOD GRP IUBLINK fro ro nCell usedCEdl usedCEul gHoCEdl gHoCEul OtherCEdl OtherCEul dlRL ulRL nrUE leakingCellFroIds

\-------------------------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 0 b0157MDN | 0 0 | 3   | 34/64 98/256 | 30/64 | 158/256 | 29/63 | 155/253 | 46  | 46  | 46  |
| 1 4 b0423MDN | 5 2 | 2   | 2/64 6/128 | 62/64 | 122/128 | 61/63 | 120/126 | 3   | 3   | 3   |
| 1 8 b0407MDN | 8 4 | 1   | 8/64 42/256 | 56/64 | 214/256 | 55/63 | 211/253 | 15  | 15  | 15  |
| 1 10 b0106MDN | 9 5 | 3   | 40/96 125/256 | 56/96 | 131/256 | 55/95 | 128/253 | 48  | 48  | 49 147 |

\> cedhp

\-------------------------------------------------------------------------------------------------------------------------------------------

MOD GRP IUBLINK fro ro nCell usedCEdl usedCEul gHoCEdl gHoCEul OtherCEdl OtherCEul dlRL ulRL nrUE leakingCellFroIds

\-------------------------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 0 b0157MDN | 0 0 | 3   | 53.1% | 38.3% | 46.9% | 61.7% | 46.0% | 61.3% | 46  | 46  | 46  |
| 1 4 b0423MDN | 5 2 | 2   | 3.1% | 4.7% | 96.9% | 95.3% | 96.8% | 95.2% | 3   | 3   | 3   |
| 1 8 b0407MDN | 8 4 | 1   | 12.5% | 16.4% | 87.5% | 83.6% | 87.3% | 83.4% | 15  | 15  | 15  |
| 1 10 b0106MDN | 9 5 | 3   | 41.7% | 48.8% | 58.3% | 51.2% | 57.9% | 50.6% | 48  | 48  | 49 147 |

The fields in the "cedh/cedhp" printout correspond to the following variables in the "hwm print grp" printout on Module MP:

- MOD: RNC Module
- GRP: Cell Group (one to four per IubLink)
- IUBLINK: the MO id of the IubLink
- fro: the froId of the IubLink (facade resource object id, a unique id in the node)
- ro: the RO Id of the IubLink (resource object id, unique in the module. Same as capsule index).
- nCell: the number of UtranCells in the Cell Group
- usedCEdl/usedCEul: Consumed Credit / Capacity Credit . The number of used CE out of the total amount of available CE. The total amount of available CE is calculated in each RBS, based on the HW capability and the licensed capacity.
- gHoCEdl/gHoCEul: Guaranteed, HO (Channel Elements availability for Guaranteed, Handover traffic)
- OthrCEdl/OthrCEul: Other (Channel Elements availability for Guaranteed, Other traffic)
- dlRL, ulRL: number of Radio Links used in the RBS. The two values (downlink and uplink) should always be equal.
- nrUE: number of UEs in the RBS. This should be equal to the number of Radio Links.
- leakingCellFroIds: the froId of Cells where dlRL, ulRL, nrUE are not equal. This indicates that some resource has not been released properly in the cell. To release the resources in a leaking Cell, the corresponding IubLink MO must be locked and unlocked.
- leakingCellFroIds: the froId of Cells where the following condition is not met:
    - - until W10: dlRL=ulRL=nrUE
        - from W11: nrUE=nrDlRL and and nrUlRL >= nrDlRL and nrDlRL >= nrDchUlRL and nrUlRL not more than double nrDlRL

This indicates that some resource has not been released properly in the cell. To release the resources in a leaking Cell, the corresponding IubLink MO must be locked and unlocked.

\> cedg

\--------------------------------------------------------------------------------------------------------------------------------------------

Mod UtranCell CFRPHEMU Antenna and Cell Coordinates, feed into http://maps.google.com/maps?q=

\--------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| 21 CTU20847 | 111111-- 41.2383,-73.1937 41.2383,-73.193665 41.2424,-73.140621 41.2157,-73.149569 41.1996,-73.179159 41.2016,-73.215508 |
| 21 CTU20848 | 111111-- 41.2383,-73.1937 41.2383,-73.193665 41.2016,-73.215508 41.2208,-73.241665 41.2482,-73.245378 41.2710,-73.224885 |
| 21 CTU20849 | 111111-- 41.2383,-73.1937 41.2383,-73.193665 41.2710,-73.224885 41.2785,-73.189759 41.2672,-73.156478 41.2424,-73.140621 |
| 21 CTV20841 | 111111-- 41.2383,-73.1937 41.2383,-73.193665 41.2424,-73.140621 41.2157,-73.149569 41.1996,-73.179159 41.2016,-73.215508 |

The fields in "cedg" printout correspond to:

- MOD: RNC Module
- CFRPHEMU: status of UtranCell, Fach, Rach, Pch, Hsdsch, Eul, MbmsCch, EulFach (L=locked, S=ShuttingDown, T=tpsPowerLocked, U=tpsPowerShuttingDown, 1=unlocked&enabled, 0=unlocked&disabled)
- first coordinates: value of attribute UtranCell::antennaPosition
- all following coordinates: value of attribute UtranCell::utranCellPosition

The coordinates are expressed in degree of latitude and longitude and can be fed in google maps to see the location of the cell, eg: http://maps.google.com/maps?q=41.2383,-73.1937

\> ceds

\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Mod UtranCell CFRPHEMU ABCDEFGHIJKLMNOPQRST cpc dBMC edchT2 enhDrx enhL2 eulDch eulTd fdpch hsAqm hsFach impL2 lBHo mC mCMimo q64 q64Mimo eulMC hsThp hs3MC db3MC -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1111 cell17711 111111-L 00100000001100000100 | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 0 0 | 1   | 0   | 0   |
| 1111 cell17712 111111-- 00100000001100010100 | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 1 0 | 1   | 0   | 0   |
| 1111 cell17713 111111-- 00100000001100010100 | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 1 0 | 1   | 0   | 0   |
| 1111 cell17714 T00000-- 00100000001100000100 | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 0 0 | 1   | 0   | 0   |
| 1111 cell17715 T00000-- 00100000001100010100 | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 1 0 | 1   | 0   | 0   |

The fields in "ceds" printout correspond to the following attributes:

- MOD: RNC Module
- CFRPHEMU: status of UtranCell, Fach, Rach, Pch, Hsdsch, Eul, MbmsCch, EulFach (L=locked, S=ShuttingDown, T=tpsPowerLocked, U=tpsPowerShuttingDown, 1=unlocked&enabled, 0=unlocked&disabled)
- A=cpc: UtranCell::cpcSupport
- B=dBMC: MultiCarrier::dualBandMultiCarrierSupport
- C=edchT2: Eul::edchTti2Support
- D=enhDrx: Hsdsch::enhUeDrxSupport
- E=enhL2: Hsdsch::enhancedL2Support
- F=eulDch: Eul::eulDchBalancingSupport
- G=eulTd: Eul::eulTdSchedulingSupport
- H=fdpch: UtranCell::fdpchSupport
- I=hsAqm: Hsdsch::hsAqmCongCtrlSupport
- J=hsFach: Hsdsch::hsFachSupport
- K=impL2: Eul::improvedL2Support
- L=lBHo: UtranCell::loadBasedHoSupport
- M=mC: MultiCarrier::multiCarrierSupport
- N=mCMimo: MultiCarrier::multiCarrierMimoSupport
- O=q64: Hsdsch::qam64Support
- P=q64Mimo: Hsdsch::qam64MimoSupport
- Q=eulMC: MultiCarrier::eulMultiCarrierSupport
- R=hsThp: UtranCell::ueHsThpMeasSupport
- S=hs3MC: MultiCarrier::hsdpa3McSupport
- T=db3MC: MultiCarrier::hsdpaDb3McSupport

**4.2.29 al\[atkcg\]\[u\]\[z\] \[-tz &lt;hrs&gt;\] \[-a|-u &lt;alarm-id&gt;\] \[ | &lt;unix-cmds&gt;\]**

Print the list of active alarms. Acknowledge/Unacknowledge an alarm.

**Output options:**

- al : active alarm list is printed in overview format, only four fields are shown per alarm.
- ala : same as al, but the full detailed list is added underneath the overview table.
- alt : same as al, but the time field is added to the table and the alarms are sorted chronologically.
- alk : same as al, but the list is separated in two parts, one for the unacknowledged alarms, and one for the acknowledged alarms. Only applicable for CPP nodes.
- alc : same as al, but each alarm is displayed in CSV format and all fields are shown for each alarm. • alg : same as al, but the MO instances with alarms are saved to a MO group called al_group

**Time options:**

- u : timestamps are printed in UTC time. This is default on COM nodes.
- z : timestamps are printed in local time. This is default on CPP nodes.

\-tz &lt;hrs&gt; : timestamps are printed in the specified timezone, eg "-tz -3.5" for UTC-3.5 , "-tz +10" for UTC+10 Note: this setting can be saved in the moshellrc uservariable tz_option, eg tz_option=+10

**Notes:**

- It is possible to combine several options, eg: al, ala, altk, alatk, altkc, etc.
- The output can be piped through external unix utilities like "sort", "grep", "less", "more", etc.
- On CPP nodes, the options -a/-u can be used for acknowledging/unacknowledging an alarm. The alarm is identified by its alarm id which can be printed with "ala" or "alc". Only the number after the underscore is needed. If the alarm id contains the mibPrefix, the mibPrefix shall not be included. Example: if the alarm id is shown as SubNetwork=OSS38_ROOT_MO,MeContext=MGW1_21, then the alarm id is 21.

**Examples:**

- altk : sort active alarm list by timestamp and show alarms in two separate tables depending on acknowledgment state
- altkc : same as above but alarms are displayed in CSV format and more fields are shown
- alt -tz +3.5 : print alarms in UTC+3.5 timezone
- al | grep -i atmport : only print the alarms that match "atmport" (case insensitive)
- al -a 18 : acknowlege alarm number 18 (the alarm id is shown in "alc" or "ala"). Only applicable for CPP nodes.

Note: in alt and alk, the severity field is shortened to one character:

- **C** for Critical
- **M** for Major
- **m** for minor
- **w** for warning

**Moshell generated alarms:**

On CPP nodes, the alarm list is read from the Alarm Client Interface (ALCI), however, some additional alarms are generated from moshell in the case where some CPP features are activated and disabled or if TimDevice MOs are missing on RNC, since these MOs would not generate an alarm otherwise. This moshell feature is controlled by the uservariable "mosalarm" and is turned on by default which means that the "al" command takes about 1 or 2 seconds more to execute due to reading the status of those CPP features from the MO Client Interface.

**Correlated alarm info:**

In RCS nodes, alarms have a special "CI" field ("Correlation Info") to identify primary and their correlated secondary alarms. This field is shown in a simplified way in "al", with the indication "P" for primary alarms, "S" for secondary alarms, and a unique number for the alarm ID. For instance: "P:11->17,18" means alarm 11 is primary and related to secondary alarms 17 and 18. "S:17->11" means alarm 17 is secondary and related to primary alarm 11. This correlated alarm information is always shown by default but can be turned off via the uv show_related_alarms.

It is also possible to display the full correlation info field in json format. This field is hidden by default but can be turned on via the uv show_correlation_info.

**ProbableCause/AdditionalText:**

By default, only the AdditionalText field is shown (in brackets). However if it is empty, then the ProbableCause is shown instead, appended with the prefix "PC:".

It is possible to change this behaviour by setting the uservariable alarm_format. Refer to the description in the file moshell/moshell for more info about this uservariable.

**Cloud RAN:**

In Cloud RAN, where the alarm list is read over SNMP, the following uservariables need to be configured in the ipdatabase file:

- snmp_username : the username for the SNMP connection to the node
- snmp_sha_password and snmp_aes_password : the SHA and AES passwords to use for the SNMP connection (only needed in case SNMP is configured with "AuthPriv" security)

**4.2.30 lg\[abcdefghijklmnopqrstuvwxyz012345678\] \[-l &lt;input-directory|logfile|zipfile&gt;\] \[-m &lt;minustime&gt;\] \[-p &lt;plustime&gt;\]**

**\[-s &lt;startdate&gt;\] \[-e &lt;enddate&gt;\] \[-g &lt;boardgroup&gt;\] \[-r &lt;mogroup&gt;\] \[-n &lt;nodefilter&gt;\] \[-x &lt;XBlog-filter|ESIlog-filter&gt; \]**

**\[-b &lt;xb&gt; \] \[-d &lt;nrdumps&gt;|&lt;esiGranularity&gt;\] \[-z\] \[-tz &lt;hrs&gt;\] \[-c &lt;collector-profile&gt;\] \[-ps &lt;startdate&gt;\] \[-pe &lt;enddate&gt;\]**

**\[-pm &lt;minustime&gt;\] \[-pp &lt;plustime&gt;\] \[&lt;destination-directory&gt;\] \[|&lt;unix-cmds&gt;\]**

Fetching and processing of node logs

All options can be combined together, except options d, w, x, f which can only be combined with options r and c.

**CPP Log Options:**

1.  : Print the list of logs from the node.
2.  : T&E disk and ramdisk logs (/d/usr/cello/telogs and /r000x00/telogs on CPP OSE nodes; /tsRamdisk/Snapshots on Evo8300 ). See examples at the end for usage.

- 3 : RNC SON log (/c/logfiles/SON/ANR_EVENTLOG.xml , /c/logfiles/SON/TPS_EVENTLOG.xml, and /c/logfiles/SON/ANR_EUTRAN_EVENTLOG.xml)
- 4 : MGW BGF log (/c/logfiles/BGF)
- 5 : MGW IPCS log (/c/logfiles/ipcs_logs)
- 6 : WebServer log (/c/logfiles/webserver/CELLO_WEBSERVER_LOG.xml)
- 7 : SwErrorAlarm log (/c/logfiles/SwErrorAlarmLog)
- 8 : RNC GeoRedundancy log (/c/logfiles/Roam/ROAM_GEO_LOG.xml)
- a : Alarm log (ALARM_LOG.xml). History of alarms raising and ceasing. Note: Updated alarms are hidden by default but this can be changed with the uv show_updated_alarms.
- j : Alarm durations (ALARM_LOG.xml). Same as option a except that raising and ceasing are combined into one entry, together with the total duration of the alarm.
- x : Active alarms (ALARM_LOG.xml). Snapshot of alarms active on a specific date/time given in -m/-s option.
- e : Event log (EVENT_LOG.xml). History of MO events.
- v : Availability log (CELLO_AVAILABILITY2_LOG.xml). History of node/board/program restarts.
- s : System log (/c/logfiles/systemlog). History of node/board/program restarts.
- p : Post Mortem Dumps (/c/pmd) and LTE ENodeB error files (/c/logfiles/troubleshooting/error). History of board/program crashes. PMD files are saved permanently in moshell_logfiles/logs_moshell/pmdfiles/&lt;nodeaddress&gt;/pmd .
- u : Upgrade log (Trace.log/Trace.txt). History of system upgrades.
- d : Downtime log. History of node outages and partial outages.
- o : MO command log (CORBA_AUDITTRAIL_LOG.xml and PNP_LOG.xml). History of MO write commands

(set/action/create/delete).

- q : MO command log in "trun" format (CORBA_AUDITTRAIL_LOG.xml). Useful for recovering configuration data which was not saved to CV before node restart.
- l : COLI command log (SHELL_AUDITTRAIL_LOG.xml). History of COLI commands.
- y : SecurityEvent log (CELLO_SECURITYEVENT_LOG.xml). History of O&M connection setups.
- w : Active O&M connections (CELLO_SECURITYEVENT_LOG.xml). Snapshot of O&M connections on a specific date/time given in -m/-s option.
- z : IP Transport log (CELLO_IPTRAN_LOG.xml).
- t : Trace and Error log (lh all te log read. to specify a different boardgroup than all, use the -g option).
- g : Board Restart error log (lh allpd llog -l ; lh ru llog -l -n 5).
- h : HW Inventory log (CELLO_HWINVENTORY_LOG.xml). This file must first be generated with the command hili mk on O&M MP.
- k : XB log. Fetches CMXB logs (HCS and Evo nodes) and SCXB logs (Evo nodes). Use -b &lt;xb&gt; to limit log fetching from a single board. Use -x &lt;xblogfilter&gt; to determine which logs are processed (see below).
- b : RLIB log (/c/logfiles/Rlib/RLIB_PM_LOG.xml), applicable to RNC only.
- f : collect all logs except XB logs and ENB DSP dumps, and save to a zipfile. To specify number of ENB DSP dumps to collect, use option -d &lt;n&gt;, eg lgf -d 2 to collect the last 2 ENB DSP dumps.
- f1: collect all logs and last ENB DSP dump, and save to a zipfile.
- f2: collect only XB logs, and save to a zipfile. To only collect XB logs from a specific board, use option -b, eg lgf2 -b 000100 **Pico Log Options:**

- a: Alarm log (/var/volatile/log/permanent/oss/alarmlog.log). Note: Updated alarms are hidden by default but this can be changed with the uv show_updated_alarms.
- e: FmEvent log (/var/volatile/log/permanent/oss/fmevents.log) g: Runtime log (/var/volatile/log/runtime)

h: AutoIntegration log (/var/volatile/log/permanent/oss/AutointegrationLog.txt)

- o: Audit Trail logs (/var/volatile/log/runtime\* and /var/volatile/log/permanent/oss/runtime\*)
- s: SystemEvent log (/var/volatile/log/permanent/oss/sysevent)
- u: Upgrade log (/var/volatile/log/permanent/oss/SWUpgradeLog.txt)
- y: SecurityEvent log (/var/volatile/log/security)
- f: collect all logs and save to a zipfile

**vBGF/vSBG/vMRF/vMTAS/vCSCF Log options:**

- a: Alarm log (FaultManagementCfgLogAlarmStream)
- e: Alert log (FaultManagementCfgLogAlertStream)
- s: System log (saLogSystem)
- y: Security log (ComSecLogStream)
- 6: LM SA log (LmSaCfgLogStream)
- 7: COM SA log (ComSaCfgLogStream)
- f: collect all logs and save to a zipfile

**RCS Log Options (MSRBS):**

- a: Alarm log (AlarmLog). History of alarms raising and ceasing. Note: Updated alarms are hidden by default but this can be changed with the uv show_updated_alarms. Correlation information is hidden by default but this can be changed with the uv show_correlation_info.
- e: Alert log (AlertLog). History of alerts.
- j: Alarm durations. Same as option "a" except that raising and ceasing are combined into one entry, together with the total duration of the alarm.
- x: Active alarms. Snapshot of alarms active on a specific date/time given in -m/-s option.
- b: TN Application log (TnApplicationLog)
- d: Downtime log. History of node outages and partial outages.
- g: Board Restart log ("llog -l" on DU/RU/XMU).
- h: AutoIntegration log (AiLog) and HwInventoryHistory log (HwInventoryHistoryLog)
- k: Ericsson Support Information log (EsiLog) - parsed
- k1: Ericsson Support Information log (EsiLog) - not parsed (transparent display: useful for "lgk -x hw", "lgk -x ricm", "lgk -x fru", "lgk -x nc", "lgk -x ic", ...)
- k2: Applicable for offline mode, to load the "dcg run" and "te log read" printouts from ESI in case the dcgm does not contain them (eg if dcg_no_telog=1 and/or dcg_no_coli=1)
- l: COLI command log (AuditTrailLog)
- o: MO command log (AuditTrailLog)
- p: Post Mortem Dumps (from /rcs/dumps/pmd). History of CPM crashes. PMD files are saved permanently in moshell_logfiles/logs_moshell/pmdfiles/&lt;nodeaddress&gt;/pmd .
- q: Health Check Log (HealthCheckLog)
- v: Availability log (RBS_CS_AVAILABILITY_LOG)
- t: T&E log (lh all te log read. to specify a different boardgroup than "all", use the "-g" option). Trace and Error Log.
- u: Upgrade log (SwmLog)
- y: Security log (SecurityLog)
- z: TN Network log (TnNetworkLog)
- 3: VES log (VesLog)
- 4: APC Logs (BatteryLog, ClimateLog, PowerDistributionLog, PowerSupplyLog, UnitTemperatureLevelLog, SupportUnitLog)
- 5: OOT log (OotLog)
- 6: Consul log (Consul)

7: SwErrorAlarm log (SwErrorAlarmLog)

- 8: License log (LicenseLog)
- f: collect all logs with small ESI and save to a zipfile. If small ESI fails, try lgf -d -1 to collect a static ESI (= small without callbacks)
- f0: collect all logs except the ESI and save to a zipfile
- f1: collect all logs with large ESI and save to a zipfile
- f2: collect only export logs and ESI and save to a zipfile (no llog/telog/pmd)
- f3: collect only export logs and save to a zipfile (no ESI/llog/telog/pmd)
- f4: collect only ESI and save to a zipfile (no exportlogs/llog/telog/pmd)

**ESI options:**

1.  When collecting ESI with lgf/lgf1, the "-r &lt;mogroup&gt;" option can be used to specify

Cells/SectorCarrier/FieldReplaceableUnit whose logs shall be included in the ESI. Without this option then all FRU logs are collected in the ESI. The "&lt;mogroup&gt;" must be first made with the command "ma".

1.  The option "-d &lt;n&gt;" can be used to specify the ESI granularity:
    - \-d 1: large - means that all Logs will be part of ESI.
    - \-d 0: small - means that only Logs with a size of up to 20 MB will be part of ESI.
    - \-d -1: static - same as small but with an addition that no callback modules will be invoked. This alternative is to be used if the callbacks cause the ESI generation to fail. Note: the ESI will of course not contain the accurate log files normally generated by the callbacks; such logs may be missing or containing files generated in an older ESI.
    - \-d -2: refresh - means that only possible crash log files will be part of ESI. It is typically used for automatic log collection.
    - \-d -101: sp1 - sp\[n\] generates a filtered ESI with less data, used for a special purpose (sp) where \[n\] is an integer, currently only sp1 is supported.

**Note:**

If the lg command fails on the RCS node (possibly due to firewall restrictions), try setting the following uservariables in the file /.moshellrc:

- - export_method: use value 1 (SFTP export to the current workstation) or value 2 (SFTP export to a different workstation).
    - export_username: the username for the SFTP server to which the logs will be exported
    - export_password: the password for the SFTP server. Can be encrypted with the command encpw. If the password is not set, then it will be prompted at the command line.
    - export_server: the IP address of the SFTP server. Only applicable if export_method=2.

More information about export uservariables can be found in the file moshell/moshell.

**YANG Log Options (Cloud RAN):**

- - f: collect all logs (ESI, DDB, DIA logs, moshell command log) and save to a zipfile.

Use option -c &lt;collector-profile-name&gt; to specify the colletor-profile to use for the DDB export. If unspecified, the collector-profile HelmChartValues is used as default. The export will be done via the sftp-server specified in the collector-profile. The list of sftp-servers and corresponding passwords must be specified in the uservariables yang_sftp_servers and yang_sftp_passwords respectively. See example in the file moshell/moshell . • a: alarm log

- - o: audit trail log
    - v: availability log
    - y: security log
    - 8: kubernetes event log

**Common Options (CPP/Pico/RCS/YANG):**

- - m : merge the different logs together (eg: lgaevm will merge alarm/event/availability logs).
    - i : inverse chronological order.
    - r : refetch the logs from the node. Logs are only fetched once and kept in cache. This option is used to refresh the session cache.
    - c : print the output in csv format (semicolon separation).

n : Moshell command log. To specify different or all nodes, use the -n &lt;node-filter&gt; option. If -m or -s option are not specified, the default is to show command history of the last 30 days. Note: the Moshell command log entries are given by default in the workstation’s local timezone. In order to display them in UTC timezone, please combine with "m" option, i.e. "lgnm".

**Time filtering (CPP/Pico/RCS/YANG):**

- The -s and -e options are used for specifying an absolute timespan: -s gives the starting date and -e gives the ending date. The format is yyyymmdd\[.hhmm\], for instance 20071230, or 20071230.0800.
- The -m and -p options are used for specifying a timespan relative to today’s date: -m gives how long time backward and -p gives how long time forward. The format is in days, hours, or minutes, eg. 10d (10 days), 2h (2 hours), 30m (30 minutes).
- \- The options -ps, -pe, -pm and -pp options are identical to the options -s, -e, -m and -p but apply only for the timespan for collection of periodic DDB in YANG nodes. Whereas -s, -m and -p apply for the manual DDB.

**Time conversion (CPP/Pico/RCS/YANG):**

- \-z : to print the timestamps in the timezone of the workstation where moshell is executing. Eg: lga -z will show the alarm log timestamps in the workstation’s timezone
- \-tz &lt;hrs&gt; : for printing the timestamps a specific timezone.

Eg: lga -tz +10 will show the alarm log timestamps in UTC+10 timezone

Note: this setting can be saved in the moshellrc uservariable tz_option . If tz_option is used then the "lgn" command needs to be run with "m" option ("lgnm") in order to show correct timestamps.

**Offline usage:**

The -l option allows to process the logfiles in offline mode, when not connected to the node. The argument of the -l option specifies the location where the logfile(s) are locally stored on the workstation. It can be:

- a single logfile
- a directory containing several logfiles.
- a zipped archive containing one or more logfiles.

By running the command lgf while connected to the node, it is possible to download all the logfiles to a local directory for later offline processing. The local directory can be specified as argument. If not specified, a default location is chosen

(~/moshell_logfiles/logs_moshell/lg/nodeaddress/date_time). The local directory is then automatically compressed and saved in a zipped archive.

**XB log filters (CPP):**

The XB log filter is specified with -x &lt;filter&gt; in the command lgk on nodes containing CMXB/SCXB boards, to specify the type of logs that will be displayed. The XB log filter shall be given as a combination of one or more of the following letters: • o: OS log (default)

- s: SNMP log
- c: COLI command log
- b: Board manager log
- w: Switching event log
- m: Software management log
- e: Security log
- f: Firewall log
- h: Shelf manager log
- a: Application log
- t: Timing unit manager log
- p: Power and fan log
- x: All of the above listed logs

Example:

- lgk -x oscb - show the XB log entries from OS log, SNMP log, COLI command log and Board manager log

**ESI log filters (RCS):**

The ESI (Ericsson Support Information) log filter is specified with -x &lt;filter&gt; in the command lgk on RCS nodes (MSRBS), to specify the type of logs that will be displayed. The ESI log filter shall be given as a combination of one or more of the following

strings, separated by commas:

- 1) ai : rcs/log/AiLog/AiLog.\*
- 2) al : rcs/saf_log/saLogAlarm/saLogAlarm_\*\__\*.log
- 3) a_t : rcs/log/AuditTrailLog/AuditTrailLog.\* (MO part)
- 4) atr : rcs/log/AuditTrailLog/AuditTrailLog.\* (COLI part)
- 5) capi : cpu_load.log (generated after running COLI command "capistart" and "capistop" on the DUS)
- 6) com : rcs/comte/com.log.\*
- 7) coma : rcs/comte/com_alarm.log.\*
- 8) comi : rcs/log/ComInterfaceLog/ComInterfaceLog.\*
- 9) erl : rcs/bootlogs/erlang.log.1 AND rcs/erlang/erlang.log.\*
- 10) ev : rcs/log/NotificationLog/NotificationLog.\*
- 11) lic : rcs/log/LicensingLog/LicensingLog.\*
- 12) ltt : rcs/log/LttngLog/LttngLog.\*
- 13) mmi : rcs/log/MMILog/MMILog.\*
- 14) nl : rcs/bootlogs/nl_log.\* and rcs/networkloader/nl_log.\*
- 15) notif : rcs/saf_log/saLogNotification/saLogNotification_\*\__\*.log
- 16) pnp : rcs/saf_log/PnpApplicationLog/PnpApplicationLog_\*\__\*.log
- 17) sys : rcs/saf_log/saLogSystem/saLogSystem_\*\__\*.log
- 18) sec : rcs/log/SecurityLog/SecurityLog.\*
- 19) swmi : rcs/log/SwmInternal/SwmInternal.\*
- 20) tnapp : rcs/saf_log/TnApplicationLog/TnApplicationLog_\*\__\*.log
- 21) tnnet : rcs/saf_log/TnNetworkLog/TnNetworkLog_\*\__\*.log
- 22) tri : rcs/log/TriLog/TriLog.\*
- 23) swm : rcs/log/SwmLog/SwmLog.\*
- 24) upg : rcs/saf_log/saLogUpgrade/upgrade_\*\__\*.log
- 25) pmc : rcs/log/RcsPmCounters/RcsPmCounters.\*
- 26) pmev : rcs/log/RcsPmEvents/RcsPmEvents.1
- 27) syslog : var/log/syslog
- 28) llog : var/log/llog/llog
- 29) hw : tmp/ee_esi/ee_esi.log
- 30) sync : applicationlogs/SyncDusg\*/sync-dcg.log
- 31) nc : applicationlogs/RBSNC\*2020082_1/esiNC/esiNC.log
- 32) ic : applicationlogs/RBSIC\*/esiIC/esiIC.log
- 33) ricm : applicationlogs/RICM\*/ricm_esi.log
- 34) fru : applicationlogs/RBSNC\*/esiFRUs/BXP_xxx.log or fru_xxx.log
- 35)lratcaps: applicationlogs/LRAT-RACOAM-ARM_\*/lrat_esi_capsule_info.log
- 36) vesi : rcs/log/VesInternalLog/VesInternalLog.\*
- 37) hci : rcs/log/HealthCheckInternalLog/HealthCheckInternalLog.\*
- 38) loglog : rcs/log/LogLog/LogLog.\*
- 39) ugtri : rcs/log/TriLog/UgTriLog.\*
- 40) comsa : rcs/log/ComSALog/ComSALog\*
- 41) l1pm : rcs/saf_log/PlmLog/l1pm\*
- 46) relog : var/log/relog\*
- 47) wrat : rcs/applicationlogs/WRAT\*/WratDcg.log
- 48) rexlog : lh ru relog --read
- 49) ntp : rcs/log/NtpLog
- 50) hc : rcs/log/HealthCheckLog
- 51) ecoli : rcs/log/RcsEcoli
- 52) crash : var/log/clog/crash_log

Example:

- lgk -x coma,erl,tri –> show the log entries from com_alarm.log, erlang.log and TriLog in the ESI
- lgk -x 7,9,22 –> same as above
- lgkm -x 2-4,7 –> show the log entries from saLogAlarm, com_alarm, and AuditTrail (both MO and COLI parts), and merge them chronologically

**Notes:**

- The output of the lg command can be filtered by piping to a unix command such as grep, sort, less, etc.
- In options a and x, the alarm severity field is shortened to one character: C=Critical, M=Major, m=minor, w=warning,\*=cleared.
- In option j, the alarm severity field consists of one letter if the alarm is still active. If the alarm is ceased then we see a character followed by a star, eg: M\* means Alarm was raised with severity Major, then ceased.
- In lgd, the reason code for manual restarts can be translated with the command mom restartreason
- In lgd on CPP nodes, the downtime values correspond to the following stages:
    - CPP downtime is the time elapsed between the row CRIT Node down and the row Node operational. in syslog or the row NODE IN Operational in avlog (whichever row comes first).
    - Application downtime is the time elapsed between the row CRIT Node down in syslog and the row

RNC Node Restart Completed (RNC) , Cell .\* enabled (WRBS) ,

VMGWs Unlocked/First VMGw Enabled (MGW), or NODE IN Operational RestartCompleted (ERBS) in avlog.

- - Jvm downtime is the time elapsed between the row CRIT Node down in syslog and the row

JVM Load Module is now operational in avlog or the row The Configuration Service is up and running in upgradelog.

- - JvmRestart: For individual Jvm restarts, the Jvm downtime is the time elapsed between the row Program CXCxxxx started in syslog (or the row Current properties in upgradelog) and the row The Configuration Service is up and running in upgradelog. Though the Jvm downtime is shown in the CPP downtime column, it is nevertheless only a Jvm downtime.
    - The node downtime figures in the summary table at the end of the printout represent the highest value between CPP downtime and Application downtime. The partial downtime figures are weighted against percentage of availability (when applicable).
- In lgd on RCS nodes, the downtime values correspond to the following stages:
    - The start of the downtime is counted from the line NODE OUT UnOperational, using the timestamp at the end of the line
    - The RCS downtime is counted until the line NODE IN Operational or

NODE IN Operational ExtUpgradeRequest

- - The Application downtime is counted until the first occurrence of a RAT RestartCompleted line (Grat, Wrat, Lrat, or NR). So this is the time until the first RAT is up.
    - The TN downtime is counted until the line Tn RestartCompleted
    - The RATs downtime indicates the individual downtime for each RAT

**Examples:**

- lga -s 20050705 -e 20050710 - show alarm log entries between the dates 20050705 and 20070710
- lgaemc | grep -i atmport - show all entries from the alarm/event logs matching the word atmport (case insensitive), display in CSV format (semicolon separated), and pipe to grep

|     |     |
| --- | --- |
| • lgx -m 14 | \- show alarms that were active 14 days ago |
| • lgxc 20080704.1330 CSV format | \- show alarms that were active on the 2008-07-04 at 13:30 and print output in |

- lgvsm -s 20050705.1000 - show all entries from system log and availability log since the 20070705 at 10:00, merged in chronological order
- lgar -m 10d -p 30m - refetch the alarm log and show all its entries starting from 10 days ago and until 30 minutes from then.
- lgf - fetch all logs from the node and put them in the default location

~/moshell_logfiles/logs_moshell/lg/nodeaddress/date_time/node_logfiles.zip

- lgf /home/user/logs/rnc10 - fetch all logs from the node and put them in the zipped file /home/user/logs/rnc10/&lt;node&gt;\_logfiles.zip
- lgaemic -m 10h -l ~/moshell_logfiles/logs_moshell/lg/rnc10/20071122_1425 - parse the last 10 hours of the alarm and event logs stored in the folder ~/moshell_logfiles/logs_moshell/lg/rnc10/20071122_1425, merge them and display them in CSV format and reverse chronological order
- lgd -m 30d - show all node restarts and related downtime from the past 30 days
- lgt -g mp - show the T&E logs of the boards of the board group "mp", sorted in chronological order
- lgtaom -m 12h - show the T&E logs of all boards merged with the alarm log and audit trail, for the past 12 hours
- lgn -m 5 -n 137.58 - show the moshell command log for the past 5 days for all nodes whose address matches 137.58
- lgk -m 5d -b 000100 - show OS status on SCXB in 000100 for past 5 days
- lgk -m 10d -x ce - show security events and COLI command history on XBs for past 10 days
- lgk -x coma,erl,swmi -m 30 - shown ESI log entries from com_alarm.log, erlang.log, and swminternal log for the last 30 days
- lgf2 - collect all XB logs
- lgf2 -b 000100 - collect XB logs only from board 000100
- lg2 - collect all CPP T&E disk/ramdisk logs
- lg2 -b mp -m 3h - collect all CPP T&E disk/ramdisk logs of the last 3 hours from board group "mp"

**4.2.31 mfa\[grcp\] \[-m &lt;hrs&gt;\]**

Miscellaneous Functions - Find Faulty Antenna for LTE cells

**Prerequisite**: the PM counters SectorCarrier::pmBranchDeltaSinrDistrX must be included in an active Scanner/PmJob Refer to RAN CPI "Antenna System Monitoring" and ENIQ CPI "Find Faulty Antenna" for more info.

**Limitations:**

- not supported on AAS (AIR16xx, AIR32xx, AIR64xx) , IRU/DOT, LPRU

**Options:**

- g: generate excel graphs for the pmBranchDeltaSinrDistrX counters
- r: refresh the data locally cached in the moshell session.
- c: display the printout in CSV format
- p: skip the antenna polarization check ("Pol" column)

**Time options:**

- m &lt;hrs&gt;: to specify the number of hours of ROP to include in the measurement. Default: 1 hour **Command example:**
- mfac - check faulty antenna based on the last hour of ROP data and print in CSV format
- mfar -m 3 - check faulty antenna based on the last 3 hours of ROP data while re-reading data from the node instead of cache
- mfag - same as "mfa" but a excel graph is generated **Printout example:**

\================================================================================================================================

SC;SE;Tx/Rx;BrPair ;RfPort1 - RfPort2 ;HW ;Serial ;Cell (State) ;Samples; Med; Mean; SDev;Pol;Res;Issue ================================================================================================================================

11;11; 4/4;0 (1,2);RRU-11(E) RRU-11(G);RRU4449 ;CF86278347 ;FDD=043086_1 (1) ; 75616; 0.5; 0.2; 6.0; S; OK;Passed

11;11; 4/4;1 (2,3);RRU-11(G) RRU-11(F);RRU4449 ;CF86278347 ;FDD=043086_1 (1) ; 75616; -0.5; -0.4; 6.9; S; OK;Passed

11;11; 4/4;2 (3,4);RRU-11(F) RRU-11(H);RRU4449 ;CF86278347 ;FDD=043086_1 (1) ; 75616; -0.5; -0.2; 6.1; S; OK;Passed

12;12; 4/4;0 (1,2);RRU-12(E) RRU-12(G);RRU8843 ;CF86795711 ;FDD=043086_1_2 (1); 188256; -0.5; 0.0; 3.4; C; OK;Passed

12;12; 4/4;1 (2,3);RRU-12(G) RRU-12(F);RRU8843 ;CF86795711 ;FDD=043086_1_2 (1); 188256; -0.5; -0.4; 7.1; X; OK;Passed

12;12; 4/4;2 (3,4);RRU-12(F) RRU-12(H);RRU8843 ;CF86795711 ;FDD=043086_1_2 (1); 188256; 0.5; 0.1; 3.6; C; OK;Passed

16;12; 4/0;0 (1,2);RRU-12(A) RRU-12(C);RRU8843 ;CF86795711 ;FDD=043086_1_6 (B); 0; 0; 0; 0; ?; NT;No data

21;21; 4/4;0 (1,2);RRU-21(E) RRU-21(G);RRU4449 ;CF86275705 ;FDD=043086_2 (1) ; 184511; 0.5; 2.1; 8.5; X;OKW;Check Polarization

21;21; 4/4;1 (2,3);RRU-21(G) RRU-21(F);RRU4449 ;CF86275705 ;FDD=043086_2 (1) ; 184511; -2.5; -2.6; 7.2; C;OKW;Check Polarization

21;21; 4/4;2 (3,4);RRU-21(F) RRU-21(H);RRU4449 ;CF86275705 ;FDD=043086_2 (1) ; 184511; 0.5; 0.7; 6.1; C;OKW;Check Polarization

29;21; 4/4;0 (1,2);RRU-21(A) RRU-21(C);RRU4449 ;CF86275705 ;FDD=043086_2_9 (1); 13128; 4.5; 6.6; 8.6; ?;NOK;RF Loss at RRU-21(A

29;21; 4/4;1 (2,3);RRU-21(C) RRU-21(B);RRU4449 ;CF86275705 ;FDD=043086_2_9 (1); 13128; -1.5; -1.6; 6.0; ?; OK;Passed

29;21; 4/4;2 (3,4);RRU-21(B) RRU-21(D);RRU4449 ;CF86275705 ;FDD=043086_2_9 (1); 13128; 0.5; 0.2; 4.7; ?; OK;Passed

**Printout description:**

- SC: SectorCarrier
- SE: SectorEquipment
- Tx/Rx: SectorCarrier::noOfUsedTxAntennas / SectorCarrier::noOfUsedRxAntennas
- BrPair: RfBranch pair 0 to 7, corresponding the counters SectorCarrier::pmBranchDeltaSinrDistr0-7. Pair 0: Branches 1&2, Pair 1: Branches 2&3, etc
- RF1-RF2 : FRU and RfPort connected to the first and second RfBranch in the pair respectively
- HW: HW type for the FRU(s) connected each branch in the pair
- Serial: Serial number for the FRU(s) connected to each branch in the pair
- Cell: LTE Cell FDD or TDD connected to the SectorCarrier
- State: State of the LTE Cell: 1: Unlocked&Enabled, 0: Unlocked&Disabled, D: Unlocked&Enabled&Degraded, L: Locked, B: EUtranCellxDD::cellBarred=BARRED, R: EUtranCellxDD::primaryPlmnReserved=true, S: EUtranCellxDD,CellSleepFunction::sleepState=ACTIVATED
- Samples: the number of samples available in the pmBranchDeltaSinrDistrX counter for the RfBranch pair. If less than 3000 samples then no result will be shown for the pair as there is insufficient data.
- Med: the median value for the pmBranchDeltaSinrDistrX counter
- Mean: the mean value for the pmBranchDeltaSinrDistrX counter
- SDev: the standard deviation for pmBranchDeltaSinrDistrX counter
- Pol: Antenna polarization is estimated based on the relative SINR Standard Deviation of antenna branch pairs of a SectorCarrier. Structures near the antenna or unusual antenna configurations may affect the SINR Standard Deviation and therefore the Antenna Polarization estimate. Only shown if all RfBranch pairs in the SectorCarrier are "OK" or "OKW" and there are 4 or 8 TX branches.
    - C=Co-polar, X=Cross-polar: Shown when the delta in Standard Deviation between any branch pair is greater than or equal to 1.1 dB and no branch pair delta is less than 0.8 dB. Co-polar (C) is a RfBranch pair where the Standard deviation is below the average Standard Deviation for the SectorCarrier. Cross-polar (X) is a RfBranch pair where the Standard deviation is above the average Standard Deviation for the SectorCarrier.
    - S=Spatial-diversity: Shown when the delta in Standard Deviation between any branch pair is less than 1.1 dB and no branch pair delta is greater than or equal to 0.8 dB.
    - ?=Polarization unknown. Shown when neither the criteria for Co-Polar/Cross-Polar or Spatial-diversity are met.
- Res: OK, OKW (OK with Warning), NT (Not Tested, due to insufficient data), NOK (Not OK)
- Issue: the type of issue found on the RfBranch pair. Can be one of: Possible RF Loss, RF Loss, Disconnected Feeder,

Check Polarization

**Description of issues and corrective actions:**

- Possible RF Loss or PIM: SINR distribution is skewed off 0 dB mean/median due to possible RF loss or PIM degrading SINR of an RF branch, or possibly mismatched antenna orientation or tilt causing unequal SINR. Use the mfi command to check for unusually high RF delta between RF ports. Use a PIM analysis tool to check if IM2 or IM3 is possible on the carrier uplink and if so check for possible sources of PIM (e.g., rusty bolts or metal flashing near antenna, defective RF connector, etc.). Check that the antennas connected to the branch pair have the same tilt and azimuth. Also check the connectors of the feeders are correctly tightened.
- RF Loss or PIM: SINR distribution is significantly skewed off 0 dB mean/median due to possible high RF loss or strong PIM degrading SINR of an RF branch. Use the mfi command to check for high for unusually high RF delta between RF ports. Check that the connectors are correctly tightened, check weather proofing (no water inside the feeders/connectors), check bend radius of the feeders, etc. Use a PIM analysis tool to check if IM2 or IM3 is possible on the carrier uplink and if so

check for possible sources of PIM (e.g., rusty bolts or metal flashing near antenna, defective RF connector, etc.). Also check if one of the feeders is connected to the wrong sector.

- Disconnected feeder: one of the feeders is disconnected or connected to the wrong sector. Check neighbouring sectors. If there is a similar problem, the antennas may be swapped between the two sectors.
- Check Polarization: the polarization pattern is not according to expectation. This could happen if the feeders are connected to the wrong antenna ports within the Sector.

**Criteria for evaluating Result and Issue:**

- Res=OK: abs(Mean)<=3 AND SDev<25.5
- Res=OKW with Issue="Possible RF Loss": abs(Mean)>3 AND abs(Mean)<=4.5 AND SDev<25.5
- Res=NOK with Issue="RF Loss" : abs(Mean)>4.5 AND abs(Mean)<16.5 and SDev<25.5
- Res=NOK with Issue="Disconnected feeder" : abs(Mean)>=16.5 AND SDev>=25.5 Note: abs(Mean) is the absolute value (always positive) of the "Mean" column.

**4.2.32 mfc\[rc\] \[&lt;Filter&gt;\]**

Miscellaneous Functions - Radio Carrier list and Cell mapping in MSRBS/ERBS.

**Limitations:**

- Cell to carrier mapping not supported for ERBS
- Cell to carrier mapping not yet supported for GSM/WCDMA, planned for a future release.

**Options:**

- r: refresh the data locally cached in the moshell session.
- c: display the printout in CSV format

**Argument:**

- The argument allows to only show the lines matching the filter string. Negative filter is supported by putting a exclamation mark in front of the filter. See examples further down.

**Description:**

The command is based on the output of the COLI command "lh ru carrierListHandler print".

Each radio carrier and certain selected fields are printed as well as the corresponding LTE or NR cell, when found.

Mapping to GSM or WCDMA cells is currently not supported, nor against cells located in another node, in case of shared radio.

**Command example:**

- mfc ,ul -> show all the UL carriers
- mfcc !tdd -> show all carriers except tdd and print in csv format
- mfc BXP_5.\*ul -> show all carriers located on BXP_5 and with direction "UL" **Printout example:**
- LNH: the linkhandler of the radio unit on which the carrier is located
- BOARD: the radio HW type. An asterisk (\*) at the end of the name indicates that the radio is shared with an external ManagedElement.
- RF: the RF port on the radio
- carrierId, devId, clId: corrspond to the fields "carrierId", "deviceId", and "clientId" in carrierListHandler printout
- ETB: correspond to the fields "carrierEnable", "tr", and "bdconf" in carrierListHandler printout. 1=enabled/setup , 0=disabled/released
- carrierType, FreqMHz, Band, Pwr, fBList: correspond to the fields "carrierType", "carrierFrequency", "carrierBand", "carrierPower", "filterBranchIdLIst" in carrierListHandler printout
- Cell: the LTE or NR cells served by the carrier. Disabled or locked cells configured on the same frequency and radio as the carrier will be shown in brackets together with their status.

\====================================================================================================================================

LNH BOARD RF carrierId devId clId ETB carrierType FreqMHz Band Pwr (W/dBm) fBList Cells

\====================================================================================================================================

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| BXP_2 RRU4449B71B85A A | 768,dl-0 |     | 0 304 111 lte100_11520 | 735.0 85.A |     | 20 (43) | 42 FDD=C77AXA |
| BXP_2 RRU4449B71B85A A | 770,ul-2 |     | 2 304 111 lte100_11520 | 705.0 85.A |     | 0   | 6 FDD=C77AXA |
| BXP_2 RRU4449B71B85A A | 774,dl-6 |     | 6 304 111 essFdd100_Id1 | 622.0 71 |     | 40 (46) | 6 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A A 778,ul-10 |     | 10 304 111 essFdd100_Id1 |     | 668.0 71 | 0   |     | 0 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A B 769,dl-1 |     | 1 304 111 lte100_11520 |     | 735.0 85.A | 20 (43) |     | 36 FDD=C77AXA |
| BXP_2 RRU4449B71B85A B 772,ul-4 |     | 4 304 111 lte100_11520 |     | 705.0 85.A | 0   |     | 18 FDD=C77AXA |
| BXP_2 RRU4449B71B85A B 776,dl-8 |     | 8 304 111 essFdd100_Id1 |     | 622.0 71 | 40 (46) |     | 0 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A B 780,ul-12 |     | 12 304 111 essFdd100_Id1 |     | 668.0 71 | 0   |     | 12 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A C 771,ul-3 |     | 3 304 111 lte100_11520 |     | 705.0 85.A | 0   |     | 30 FDD=C77AXA |
| BXP_2 RRU4449B71B85A C 775,dl-7 |     | 7 304 111 essFdd100_Id1 |     | 622.0 71 | 40 (46) |     | 18 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A C 779,ul-11 |     | 11 304 111 essFdd100_Id1 |     | 668.0 71 | 0   |     | 24 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A D 773,ul-5 |     | 5 304 111 lte100_11520 |     | 705.0 85.A | 0   |     | 42 FDD=C77AXA |
| BXP_2 RRU4449B71B85A D 777,dl-9 |     | 9 304 111 essFdd100_Id1 |     | 622.0 71 | 40 (46) |     | 12 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_2 RRU4449B71B85A D 781,ul-13 |     | 13 304 111 essFdd100_Id1 |     | 668.0 71 | 0   |     | 36 FDD=C77AXX:D NRC=C77AN1:D |
| BXP_3 RRU4478B5\* A 768,dl-0 |     | 0 308 111 lte50 |     | 872.6 V | 13 (41.1) |     | 0 FDD=C77AXG |
| BXP_3 RRU4478B5\* A 770,ul-2 |     | 2 308 111 lte50 |     | 827.6 V | 0   |     | 0 FDD=C77AXG |
| BXP_3 RRU4478B5\* B 769,dl-1 |     | 1 308 111 lte50 |     | 872.6 V | 13 (41.1) |     | 6 FDD=C77AXG |
| BXP_3 RRU4478B5\* B 772,ul-4 |     | 4 308 111 lte50 |     | 827.6 V | 0   |     | 6 FDD=C77AXG |
| BXP_3 RRU4478B5\* C 771,ul-3 |     | 3 308 111 lte50 |     | 827.6 V | 0   |     | 12 FDD=C77AXG |
| BXP_3 RRU4478B5\* D 773,ul-5 |     | 5 308 111 lte50 |     | 827.6 V | 0   |     | 18 FDD=C77AXG |

**4.2.33 mfi\[trc\] \[-s &lt;startdate&gt;\] \[-e &lt;enddate&gt;\] \[-p &lt;hrs&gt;\]**

Miscellaneous Functions - display RSSI per branch on LTE cells

Prerequisite:

- the counters pmRadioRecInterferencePwr and pmRadioRecInterferencePwrPucch must be included in a PM profile.
- the feature "CXC4011820" must be operational, PmUlInterferenceReport MOs must be defined on the node and corresponding counters included in a PM profile.

Refer to RAN CPI description of "Uplink Interference Reporting" for more info.

**Options**

- t: use real-time counter values read via pget. Without this option the counter values from the last ROP file are used.
- r: refresh the data locally cached in the moshell session.
- c: display the printout in CSV format

**Time options**

- \-s &lt;startdate&gt; : to specify the starting date for the time period to check. The format is yyyymmdd\[.hhmm\], for instance 20071230, or 20071230.0800
- \-e &lt;enddate&gt; : to specify the end date for the time period to check. The format is same as above.
- \-p &lt;hrs&gt; : to specify the number of hours to check from the starting date.

The -e and -p options are mutually exclusive. The length of the period to check is defined either by the end date or the number of hours to check.

**Command example**

- mfi : check the RSSI for the latest ROP
- mfit : check the RSSI for the ongoing ROP in real-time
- mfi -s 20210310.0900 -p 3 : check the RSSI since 20210310.0900 and for 3 hours onward

**Printout example**

- CELL: EUtranCellxDD or NbIotCell
- SC: SectorCarrier
- FRU: the FieldReplaceableUnit or AuxPlugInUnit MO representing the RU/RRU on which the Cell is served
- BOARD: the board type of the RU/RRU
- PUSCH/PUCCH: the uplink interference level on the Pusch/Pucch channels in the cell
- A-H: RSSI in dBm on each applicable RF port (A to H)
- DELTA: the difference between the highest and lowest RSSI value on each of the RF ports.

\==========================================================================================

CELL ;SC;FRU ;BOARD ;PUSCH ;PUCCH ; A; B; C; D;DELTA

\==========================================================================================

FDD=168272_1 ;1 ;1/2/RU-1-2;RUL01B13 ;-119.3;-119.0;-121.0;-121.3;-118.0;-117.9; 3.4

FDD=168272_1_2;4 ;RRU-2 ;AIR21B41,3M;-120.3;-119.6;-119.9;-119.9;-120.3;-119.8; 0.5

FDD=168272_2 ;2 ;1/4/RU-1-4;RUL01B13 ;-119.7;-120.4;-121.6;-121.3;-118.3;-119.0; 3.3

FDD=168272_2_2;5 ;RRU-4 ;AIR21B41,3M;-120.4;-120.1;-120.3;-119.7;-120.1;-119.8; 0.6

FDD=168272_3 ;3 ;1/6/RU-1-6;RUL01B13 ;-119.6;-120.3;-121.0;-121.3;-118.3;-118.7; 3

FDD=168272_3_2;6 ;RRU-6 ;AIR21B41,3M;-120.7;-120.3;-120.8;-120.5;-121.0;-120.6; 0.5 ==========================================================================================

**4.2.34 mfs\[hrc\] \[&lt;rfports&gt;\] \[&lt;samplingstep&gt;\]**

Miscellaneous Functions - returnloss (vswr) frequency Sweep

**Options**

- h: simplified printout
- r: refresh the data locally cached in the moshell session
- c: display the printout in CSV format

**Arguments (both optional)**

- first argument: the rfport MOs on which to run the sweep , eg "rfport=a" or "rru-1.\*rfport=a". Without argument all RF ports are swept.
- second argument: the sampling step in kHz, eg 5000. Default is 1000 (1 MHz)

### Printout format

- FRU: the MO name of the FRU or AuxPiu
- RF: the RfPort
- gId: the globalId of the carrier as specified in the tag "globalId" of the measurementInfo for the CarrierBranch in the parsed log
- RAT: the ratType tag of the CarrierBranch in the parsed log
- Freq: the frequency tag of the CarrierBranch in the parsed log (in MHz)
- BW: the bandwidth tag of the CarrierBranch in the parsed log (in MHz)
- RL (Freq): the list of ReturnLoss values for each sample (in dB), followed by each corresponding frequency (in MHz) **Printout examples**

- mfs:

\===================================================================================================

FRU RF gId RAT Freq BW RL (Freq)

\===================================================================================================

2 A 9 WCDMA 2135 5 32.7,32.6,32.9,32.5 (2133.5,2134.5,2135.5,2136.5)

2 A 15 WCDMA 2145 5 28.3,27.8,27.5,27.1 (2143.5,2144.5,2145.5,2146.5)

2 B 12 WCDMA 2140 5 37.8,36.0,34.0,32.2 (2138.5,2139.5,2140.5,2141.5)

5 A 0 GSM 948 24.6 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 (

5 A 6 GSM 948 24.6 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 (

5 B 3 GSM 948 24.6 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 (

5 B 18 WCDMA 932 5 26.0,26.1,27.0,28.3 (930.9,931.9,932.9,933.9)

\=================================================================================================== • mfsh:

\===================================================================================================

FRU RF gId RAT Freq BW RL (Freq)

\===================================================================================================

2 A 9 WCDMA 2135 5 33,33,33,32

2 A 15 WCDMA 2145 5 28,28,28,27

2 B 12 WCDMA 2140 5 38,36,34,32

5 A 0 GSM 948 24.6 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1

5 A 6 GSM 948 24.6 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1

5 B 3 GSM 948 24.6 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1

5 B 18 WCDMA 932 5 26,26,27,28

\===================================================================================================

**4.2.35 mft\[adshy\] \[-c &lt;cellId&gt;\] \[-u &lt;ues&gt;\] \[-t &lt;timeout&gt;\] \[-n\] \[-d &lt;duration&gt;\] \[-i &lt;interval&gt;\] \[-o &lt;outputfile&gt;\]**

**&lt;TraceProfile(s)&gt;|&lt;MtdCounterProfile(s)&gt;**

Miscellaneous Functions - Trace profile handling

**Options:**

without option: reset all traces to default and activate trace profile(s) - or: run a MTD counter profile d: disable trace profile(s) - or: Reset MTD counters

- a: append trace profile(s) to existing trace conditions
- s: save trace conditions to survive board restart
- h: show trace profile(s) help text
- y: dont prompt for confirmation

**TraceProfile Parameters (currently only applicable for LTE):**

- \-c &lt;cellId&gt; : the value of the parameter "-cellid" in the "/lrat/ue" command. Optional. If not specified, the parameter "-allCell" will be sent
- \-u &lt;ues&gt; : the value of the parameter "&lt;maxUeInCell&gt;" in the "/lrat/ue" command (must be a number between 1 and 8). Optional. If not specified, the parameter "-allUe" will be sent
- \-t &lt;timeout&gt;: the value of the parameter "-timeout" in the "/lrat/ue" command. Optional. If not specified, then default timeout of 120 minutes will be used.
- \-n : will add the parameter "-traceNewUes" in the "/lrat/ue" command. Optional. If specified then only newly setup UEs will be traced on.

**MtdCounterProfiles Parameters:**

- \-d &lt;duration&gt;: total duration (default: 60 seconds)
- \-i &lt;interval&gt;: wait interval between each loop (default: 10 seconds)
- \-o <outputfile: the output file where the printouts will be stored (default: $tempdir/mtdcounters.log)

### TraceProfiles

- 0 : reset all traces to default
- 1 : LTE_VOLTE_RET_BASIC
- 2 : LTE_VOLTE_RET_OPT
- 3 : Common_CAT_NC_MemoryCrash
- 4 : Common_CAT_CRA_MemoryCrash
- 5 : Common_CAT_IC_MemoryCrash
- 6 : Common_FM_ServiceDegraded_Alarm
- 7 : Common_FM_NoConnection_APCAlarm
- 8 : Common_FM_NoConnection_FRUAlarm
- 9 : Common_FM_InconsistentConfiguration_Alarm
- 12 : LTE_L3_Basic_Traces
- 13 : EN-DC_Setup_Traces
- 14 : LTE+NR Packet_Loss_Traces
- 15 : LTE+NR_CA_Band_Selection_Traces
- 16 : LTE+NR_CA_Throughput_DL_Traces
- 17 : LTE+NR_CA_Throughput_UL_Traces
- 18 : NR_BLER_DL_Traces
- 19 : NR_BLER_UL_Traces
- 20 : ESS Alarm_Traces
- 21 : Intra-Frequency gNB HO_Traces

**PmCounterProfiles:**

- 10 : LTE_Random_Access_Counters **MtdCounterProfiles:**
- 11 : reset/read LTE/NR MTD counters (use -d/-i options to specify loop parameters)

**Examples**

mft 0 ==> reset traces to default mft 1 ==> reset traces and activate profile 1

- mfts 3-5 ==> reset traces, activate and save profiles 3,4,5
- mfta 1,6-8 ==> activate profiles 1,6,7,8 (traces will be appended to existing trace conditions without first resetting the existing traces to default)
- mftds 1,3-5,9 ==> disable profiles 1,3,4,5,9 and save trace conditions
- mft 1 -c 3 -u 8 -t 60 => activate trace profile 1 with parameters "cellId 1", "maxUeInCell 8", "timeout 60 minutes"
- mfth 1-2 ==> show help text for profiles 1 and 2
- mftdy 11 ==> reset MTD counters
- mfty 11 ==> collect MTD counters for the default duration of 60 seconds with 10 seconds interval between each loop and save to the default logfile in $tempdir
- mfty 11 -d 300 -i 30 -o $logdir/mtd.log ==> collect MTD counters for 300 seconds with 30 second interval between each loop and save output to the file mtd.log in the $logdir folder

**4.2.36 occ \[get|logs\] \[-h|...\]**

OpenShift Client emulator for offline mode to a Cloud RAN decrypted dcgm. For Ericsson only!

This command is only available for Ericsson personnel.

It works while connected in offline mode to a Cloud RAN dcgm containing a decrypted DDB. For help, type "occ get -h" or "occ logs -h".

To run in WSL, certain python modules are required, which can be installed with below command:

sudo apt install python3.8 python3-pip && pip3 install numpy pandas

To run in Cygwin, the following modules need to be installed: python39-pip, python39-yaml, python39-numpy, python39-devel, wget, gcc-g++, gcc-fortran, make, libgfortran5

Then follow the below procedure:

setup-x86_64.exe -q -P wget wget https://raw.githubusercontent.com/transcode-open/apt-cyg/master/apt-cyg chmod +x apt-cyg mv apt-cyg /usr/local/bin apt-cyg install gcc-g++ gcc-fortran make

/usr/bin/python3.9.exe -m pip install --upgrade pip pip3 install pandas (takes ~75 minutes to complete)

More info: https://eteamspace.internal.ericsson.com/display/RANI/simple+DDB+reader+-+OpenShift+Emulator (internal

Ericsson)

**4.2.37 orx\[acglpr\] \[-r &lt;radios&gt;\]**

Open-Radio miscellaneous commands (list, get, alarm, restart).

Running orx with no option will list all ORadios and their ID. New option l will read the YANG schemas from the ORadio. This is done implicitly in Moshell, but if the RU is not restarted via Moshell after a software activation or is swapped, this command will have to be run.

**Options**

- a: active alarm list
- r: restart ORadio.
- g: perform a netconf "get" operation
- gg: perform a netconf "get-config" operation
- c: print the active alarm list in csv format

l: reload YANG schemas

p: poll until the ORadio becomes ENABLED after restart.

**Flags**

- \-r &lt;radios&gt;: the list of all radio ids on which the command shall run.

Eg: "-r 1-3" will run on radios 1,2,3. "-r 1,2" will run on radios 1 and 2. Without "-r &lt;radios&gt;" the command will run on all radios.

**Examples**

- orx –> list all ORadios. Example printout:

\===================================================================================================

Id MO LDN

\===================================================================================================

1.  ManagedElement=1,Equipment=1,FieldReplaceableUnit=2,ORadio=1
2.  ManagedElement=1,Equipment=1,FieldReplaceableUnit=3,ORadio=1

\=================================================================================================== • orxa –> print active alarms for all ORadios. Example printout:

\===================================================================================================

Id Fault-Id Date & Time (+00:00) Severity Source Affected objects Text

\===================================================================================================

1 1 2019-07-24T14:56:33 MINOR module/slot0 module/slot0; Unit tempera

\===================================================================================================

- orxg -r 1 –> perform netconf "get" on ORadio with Id 1
- orxgg –> perform netconf "get-config" on all ORadios
- orxr -r 1,3 –> restart ORadio 1 and 3

**4.2.38 ori\[shxc\] \[-r &lt;radios&gt;\]**

Open-Radio HW/SW inventory.

The software inventory table is used to determine the build and version of specific ORadio Software. This can be used to manually verify which software is running and also to validate new upgrade packages. An automated validation (though manually triggered) can be done on demand (see orsv).

**Options**

- s (oris): Show software inventory only.
- h (orih): Show hardware inventory only.
- c : Print tables as csv.
- x (orix): Show execution data.

**SW Inventory tables columns**

First table(listing software slot info):

- Id - Id of the ORadio (see orx)
- SWSlot - Name of the Software Slot.
- ProdCode - Product code for the ORadio hardware component.
- VendorCode - Two Symbol code for the product vendor.
- BuildId - Identifier for the particular software build.
- Version - Software build version.
- Status - Status of the current software slot. If a valid UP is installed on the slot, the status should be VALID.
- AR - Active-Running states, 00 means not-active/not-running, 10 means active/not-running, 11 means active/running, 01 means not-active/running. This state should never occur and if you get this, it is likely a SW bug.
- Access - Access identifier for the software slot. READ_WRITE normally means the slot is available for doing upgrade, while a READ_ONLY slot is used for factory reset.

**Hardware inventory columns**

First table (listing hardware components):

- Id - Id of the ORadio (see orx).
- Component - Type of the hardware component.
- Name - Name of the component.
- S - State of the component. Values may be L-locked; 0-unlocked,disabled; l-unlocked-enabled.
- U - Usage state of the component. Values are A-active; I-idle; B-busy.
- ProdCode - Product code for the hardware component.
- Rev - Revision of the hardware component.
- Serial - Hardware component serial number.
- ProdDate - Product date of the Hardware component.
- Mfg - Name of the company manufacturing the hardware component.

Second table (listing interfaces):

- Id - Id of the ORadio (see orx).
- Interface - Name of the interface.
- Port - port number of the interface.
- S - state of the interface. The states may be 1-Up, or 0-Down.
- Speed - The nominal speed of the interface.
- Type - Interface type.
- ComponentRef - Reference to physical port. **Orix columns**

First table:

- FRU - FRU MO ID.
- Name - RU component name.
- Board - Board type
- FB - FRU-Board state, 1 for DISABLED L for locked 0 for DISABLED. F will list the FRU state and B will list the state red from the RU.
- FAULT - Currently not applicable.
- OPER - Currently not applicable.
- MAINT - Currently not applicable.
- ProductNumber - RU product number.
- Rev - RU product revision.
- Serial - RU product serial number.
- Date - RU production date.
- UPT - Time since the last RU restart. Not applicable for xRAN.
- Cells - Cells connected to the RU.

Second table (RU SFP operational information):

- RiL - RiLink ID.
- T - Link type, O-optical, E-electrical.
- Rate - Maximum link bitrate.
- FRU - FRU MO ID.
- BOARD - Board type.
- IF - RU interface, which the link is connected to.
- Port - RU port number.
- FP - FRU state and port state.
- Vendor - SFP vendor.
- VendorProd - SFP product ID.
- Rev - SFP product revision.
- Serial - SFP serial number.
- EricssonProd - Ericsson product ID if any.
- WL - Currently not applicable.
- Temp - SFP operating temperature.
- Txbs - TX-bias current in mA.
- TXdBm - TX-power in dBm.
- RXdBm - RX-power in dBm.
- BER - Currently not applicable.

**Example**

\>>oris -r 1-2

\=======================================================================================================

Id SWSlot ProdCode VendorCode BuildId Version Status AR Access

\=======================================================================================================

1 slot1 ABC123-10A SS 1 1.0 VALID 00 READ_WRITE

1.  default_slot ABC123-10A SS 1 1.0 VALID 11 READ_ONLY

\-------------------------------------------------------------------------------------------------------

1.  slot1 ABC123-10A SS 1 1.0 VALID 00 READ_WRITE

2 default_slot ABC123-10A SS 1 1.0 VALID 11 READ_ONLY

\=======================================================================================================

**4.2.39 ors\[vdiacp\] \[-r &lt;radios&gt;\]**

Open-Radio SW upgrade.

**Options**

- v: Validate software package.
- d: Download software package
- i: Install software package.
- a: Activate software package.
- p: Poll until O-RU ENABLED after activation.
- c: Show tables in CSV format.

**Flags**

- r: Which ORadio where PM objects are created. Eg. -r 1-3 for ORadio with Id 1,2 and 3 (see orx), -r 1,3 for ORadio with Id 1 and 3. Default is for all ORadios

Detailed description of the options with examples:

**orsv \[-r &lt;radios&gt;\] &lt;manifest file&gt;**

Validate the software package by comparing the manifest.xml with the software inventory. The call passes silently if no Errors. Otherwise fails with possible Errors:

If not possible to read the manifest file. Recomended action: Verify path to manifest.xml

\> Error! Manifest file does not exist.

If the product cannot be verified. Recommended action: Run oris to troubleshoot parameters.

\> Error! SW validation failed on RU_1! Product, vendor or build-id does not match

Version number is not higher than current version. New software cannot be installed. Recommended action: Run invs to verify current software version.

\> Error! SW validation failed on RU_1! Software version must be newer than the current version.

In case the -r flag is used, it will run for specific radios (see orx) otherwise it will run for all radios. Examples:

- orsv -r 1-3 /home/user/manifest.xml –> Run software validation for ORadio 1 to 3.
- orsv -r 2,5 /home/user/manifest.xml –> Run software validation for ORadio 2 and 5.

**orsd \[-r &lt;radios&gt;\] user@host/path \[&lt;password&gt;\]**

Download ORadio software. Password is optional, prompts for password if no password is given.

If the password will be entered on the command line, it is recommended to encrypt it, using the "encpw" command.

If a COMPLETED notification is received. >Download completed.

If the RU returns a FAILED RPC reply on download request. Recommended action: see detailed error message from RU.

\>Failed to start download.

If a notification is received and status is not completed. Recommended action: See detailed error message from RU.

\>Software operation failed with status "status" >Failed to complete download.

If another error occurs. This will normally be followed by an error message. Recommended action: Read detailed error message. >Error occured during software download.

When the download process is completed, the result is listed in a table.

Columns:

- Id - Id for the RU given from orx.
- Status - Final Status of the installation.
- Filename - Name of the downloaded file.
- ErrorMsg - Error message from the RU if any.

In case the -r flag is used, it will run for specific radios (see orx) otherwise it will run for all radios. Examples:

- orsd -r 1-3 sftp://user@host.domain:/home/user/up.sw –> Run software install for ORadio 1 to 3.
- orsd -r 2,5 sftp://user@host.domain:/home/user/up.sw –> Run software install for ORadio 2 and 5.

**orsi \[-r &lt;radios&gt;\] &lt;filename&gt; \[&lt;slot&gt;\]**

Install software on ORadio. Slot is optional. If not given, the first available slot will be selected.

If a COMPLETED notification is received. >Installation completed.

If the RU returns a FAILED RPC reply on install request. Recommended action: see detailed error message from RU.

\>Failed to start installation.

If a notification is received and status is not completed. Recommended action: See detailed error message from RU.

\>Software operation failed with status "status >Failed to complete installation.

If another error occurs. This will normally be followed by an error message. Recommended action: Read detailed error message.

\>Error occured during software installation.

When the install operation is completed the result is listed in a table:

Columns:

- Id - Id for the RU given from orx.
- Status - Final Status of the installation.
- Slot - Slot where the installation was performed.
- SwVersion - SwVersion of the installed SW.
- ErrorMsg - Error message from the RU if any.

In case the -r flag is used, it will run for specific radios (see orx) otherwise it will run for all radios. Examples:

- orsi -r 1-3 up.sw –> Run software install for ORadio 1 to 3 to the first available slot.
- orsi -r 2,5 up.sw slot1 –> Run software install for ORadio 2 and 5 in slot1.

**orsa \[-r &lt;radios&gt;\] \[&lt;slot&gt;\]**

Activate ORadio software. If activation is completed, the RU will be restarted. Slot is optional. If not given, the first available slot will be selected.

If a COMPLETED notification is received. >Activation completed.

If the RU returns a FAILED RPC reply on activation request. Recommended action: see detailed error message from RU.

\>Failed to start activation.

If a notification is received and status is not completed. Recommended action: See detailed error message from RU.

\>Software operation failed with status "status >Failed to complete activation.

If another error occurs. This will normally be followed by an error message. Recommended action: Read detailed error message.

\>Error occured during software activation.

Restart failed or node does not come back up after restart. >Restart failed after Activation.

When the activation operation is completed the result is listed in a table:

Columns:

- Id - Id for the RU given from orx.
- Status - Final Status of the activation.
- Slot - Slot which was activated.
- SwVersion - SwVersion of the activated SW.
- RunningSw - Software running on the O-RU after restart. This will only show if the p option is used.
- ErrorMsg - Error message from the RU if any.

**4.2.40 orf\[elptb\] \[-r &lt;radios&gt;\] \[directory\]**

Open-Radio File Management.

It is possible to list all files in the standardized xRAN/O-RAN directories with the flags \[lptb\], or use the directory option to list files in non-standardized directories. With the e option it is possible to request the RU to upload files. This can be done according to normal procedures.

**Options**

- e: Export files.
- l: Select the xRAN/log directory.
- p: Select the xRAN/PM directory.
- t: Select the xRAN/transceiver directory.
- b: Select the xRAN/beamforming directory.

Note: when run from AMOS toward Samsung radios the orfet command works only if AMOS was started with the option -v amos_enm_accountlookup=0

The export option may give the following error messages.

If receiving a FAILURE RPC reply >Error: unable to start upload due to cause "errcause" If receiving a FAILURE notification >Error: unable to finish upload due to cause "errcause" If an unexpected Error occur the call will fail with relevant error message.

Example: export single file from ORadio with Id 1 (see orx)

\>> ore -r 1 xRAN/PM/C201805181300+0900_201805181330+0900_ABC0123456.csv

\=======================================================================================================

Id Result Files

\=======================================================================================================

1 OK xRAN/PM/C201805181300+0900_201805181330+0900_ABC0123456.csv

\======================================================================================================= Example: List PM files for radio with Id 1 (see orx)

\>> orfp -r 1

Id Files

1 xRAN/PM/C201805181300+0900\\\_201805181330+0900\\\_ABC0123456.csv

**4.2.41 ort\[se\] -r &lt;radio&gt;**

Open-Radio troubleshooting Options:

- s: Start troubleshooting.
- e: End troublehooting.

Troubleshooting can be run on single ORadio. When the troubleshooting is start it will pass or fail with the following messages:

If RPC reply is SUCCESS >Troubleshooting started...

If RPC reply is FAILURE >Error: Unable to start troubleshooting due to "errcause"

Fails with proper error message for unexpected errors.

When troubleshooting is stopped it will hold wait until all troubleshooting logs are generated and list them in a table. If troubleshooting fails it will fail with the message ’Error: Unable to stop troubleshooting due to "errcause"’ Example: stop troubleshooting on radio with Id 1 (see orx)

\> orte -r 1}

Troubleshooting stopped. Wait for troubleshooting logs to generate.

\=======================================================================================================

Troubleshooting logs generated

\======================================================================================================= log1_name log2_name =======================================================================================================

**4.2.42 orp\[cdeirstux\]**

Open-Radio Performance Monitoring.

The ORadio variant of the Ericsson counters are called measurement-objects. Compared to the Ericsson counter structure, where each MO Object have a set of counters, the ORadio will have a set of measurement-objects tied to specific object-units. An object-unit then determines where the measurement-objects will do measurements. These will then have a set of parameters which they will measure.

Available measurement-objects on the tranceiver are:

- RX_POWER
- TX_POWER
- TX_BIAS_COUNT
- VOLTAGE
- TEMPERATURE

With report options: MAXIMUM, MINIMUM, FIRST, LAST, FREQUENCY TABLE.

Available measurement-objects for rx-window measurements are:

- RX_ON_TIME
- RX_EARLY
- RX_LATE
- RX_CORRUPT
- RX_DUPL
- RX_TOTAL

The objects which may be measured on are RU, TRANSPORT, EAXC_ID. The rx-window PM measurement-objects will count the number of events.

According to xRAN and O-RAN 1.0 measurement-objects need to be activated and automatic upload must be configured before PM data will be generated.

Options:

- i: Set PM intervals (only for orpu).
- c: create measurement-object, or csv format. The measurement-object argument is mandatoryi, unless switches t,x are used. If used with orpl, orplc will show the list in csv format.
- d: delete measurement-object. The measurement-object argument is mandatory, unless switches t,x are used. If used with the u, option (orpud) it will instead delete an upload server.
- s: Start/activate measurement-object. The measurement-object argument is optional. If used after u, it will instead start/enable automatic upload. Also possible to use with orpc.
- e: End/deactivate measurement-object. The measurement-object argument is optional. If used after u, it will instead stop/disable automatic upload
- u: PM file upload.
- r: Enable random file upload. Only works if used after u.
- l: List measurement-objects.
- x: Create or delete all rx-window measurement-objects.
- t: Create or delete all transceiver measurement-objects.

Flags:

- \-r &lt;Radios&gt; : Which ORadio to operate. Eg. -r 1-3 for ORadio with Id 1,2 and 3 (see orx), -r 1,3 for ORadio with Id 1 and 3. Default is for all ORadios
- \-x &lt;rx-window-measurement-interval&gt;: set transceiver-measurement-interval (only for orpi)
- \-t &lt;transceiver-measurement-interval&gt;: set rx-window-measurement-interval (only for orpi)
- \-o &lt;object-unit&gt;: Set object-unit when creating measurement-objects. Default is PORT_NUMBER for transceiver-measurement-objects and RU for rx-window-measurement-objects.
- \-f &lt;bin:min_bin:max_bin&gt;: Set bin data for enabling FREQUENCY_TABLE ReportInfo, when creating measurement-objects. The format is as this 4,0.2,3.6 (nbr-of-bins,min-bin,max-bin).
- \-i &lt;file-upload-interval&gt;: set PM file upload interval for automatic upload. Only works if used with the u option.

Example:

\>> orpl -r 1

\=======================================================================================================

Id Type MeasObj ObjUnit Active FreqTableData ReportInfo

\=======================================================================================================

1 Transceiver RX_POWER PORT_NUMBER true 4:0.2:3.0 FREQUENCY_TABLE,MINIMUM,FIRST,LATEST,MAX

\=======================================================================================================

When creating a new measurement-object, the old measurement-object with the same name will be deleted prior to creating a new one. By default all ReportInfo data will be available except for FREQUENCY_TABLE. It is only possible to measure on one object-unit at the time.

Example:

- orpc -o PORT_NUMBER -f 5,0.2,3.6 RX_POWER –> Create a new transceiver-measurement-object with all ReportInfo, including FREQUENCY_TABLE
- orpi -x 300 -t 300 –> Set transceiver-measurement-interval and rx-window-measurement-interval for all ORadios to 300 seconds.
- orpd -r 1 RX_POWER –> Delete RX_POWER measurement-object on ORadio with id 1.
- orps -t 300 -x 300 –> Start all measurement-objects on all ORadios and set measurement intervals to 300 seconds.
- orpe -> End all measurement-objects on all Radios.
- orpus sftp://user@host:/upload/path secret –> Configure upload SFTP server and enable automatic upload of PM data.
- orpus sftp://user@host:/upload/path –> Configure upload SFTP server with prompt for password and enable automatic upload of PM data.
- orpud sftp://user@host:/upload/path –> Delete SFTP server
- orpcts –> Create all supported transceiver measurement-objects and start them.
- orpctxs –> Create all supported measurement-objects and start them.

## 4.3 Other commands

**4.3.1 uv \[&lt;string&gt;|&lt;var&gt;=value\]**

Display or change moshell configuration settings (also called "user variables").

The uv command used without any argument displays the values of all user variables that are usually specified in the **moshell** file and/or the **~/.moshellrc**. See Section 2.4 and **moshell** file for more info about the functionality of these variables.

If a string is given as argument, then only the variables matching the string will be displayed.

The uv command also allows to change a variable’s value from within the moshell session.

For instance, if the variable _secure_shell_ is set to 0 in the **~/.moshellrc**, it will be possible to run an moshell session in secure shell mode by just typing uv secure_shell=1 at the moshell prompt. From that point on, all node connections that would have been performed using telnet will be performed using ssh.

Example:

1.  uv - to print all variables
2.  uv sec - to print all variables matching the string "sec"
3.  uv secure_shell=1 - to change a variable

Similar to the get command, it is possible to store the output of this command into a variable

Example:

uv ^credential > $credential

**4.3.2 pv \[&lt;string&gt;\]**

To print all scripting variables or just those matching the &lt;string&gt;.

For example:

- pv print all scripting variables and their current value
- pv ver just print the scripting variables whose name match ver

The number of variables printed is saved to the variable $nr_of_vars Please refer to the "scripting" chapter for how to set a variable.

Note: To print a variable it is also possible to do: l echo $variable

**4.3.3 !/l &lt;unix-command&gt;**

Execute a unix command on the PC/workstation

Either the ! or l can be used.

**Examples:**

1.  l pwd (or the alias lpwd) - to know the current unix working directory
2.  l cd scripts/rbs3 (or the alias lcd) - to change the current working directory
3.  ! less define_sectors.mo - to view the command file that is about to run
4.  ! vi define_sectors.mo - to make a modification in the command file

Note:

- unix commands that are called with "!" are never logged
- unix commands that are called with "l" are logged if the user has started the logging with "l+"

**4.3.4 l+\[m\]\[m\]\[s\]\[o\]/l-\[s\]/l? \[&lt;logfile&gt;\]**

Open/close moshell logfiles.

- l+ is to _open a logfile_. If no logfile is given, then a default unique logfile is chosen.

The path of the default logfile is:

**~/moshell_logfiles/logs_moshell/sessionlog/&lt;DATE&gt;\_&lt;NODE&gt;.log**

The m option is for _mute_, i.e.: no output will be displayed on the screen until the log is closed. All output will go to the logfile.

(the mm option is for extra mute, even less will be displayed on screen than with l+m).

The s option is for not printing the header "log open". Can also be set with the _loginfo_print_ user variable.

The o option is for overwriting the logfile, otherwise it is appended.

- l- is for closing the logfile.

The "s" option is for not printing the header "log close". Can also be set with the _loginfo_print_ uservariable.

- l? is for checking if a logfile is currently open.

It is possible to open several logfiles but only one at a time will be active. When one logfile is closed, logging will resume in the previous one. Examples:

l+ logfile1 #starts logging to logfile1, $logfile set to "logfile1" get pr l+ logfile2 #stops logging to logfile1 and starts logging to logfile2

#$logfile is set to "logfile2" vii

l- #stops logging to logfile2 and resumes logging to logfile1

#$logfile set to "logfile1" vols

l- #stops logging to logfile1, $logfile stays set to "logfile1"

In this example, **logfile1** will contain the printouts from get, pr and vols, while **logfile2** will contain the printout from vii.

**4.3.5 dbc\[s\]\[a\] \[&lt;cvname&gt;|&lt;dbdat-file&gt;|&lt;cvzip-file&gt;|&lt;mobatch-folder&gt;\]**

Database consistency check

**Purpose**

When there are inconsistencies in the SQL database, it can lead to problems such as traffic performance degradation, upgrade failures, or cyclic restarts. Often the symptoms appear only after the next node restart or upgrade so it is not easy to know since how long the data has been corrupted and how far back we should rollback to find a non-corrupted CV. Therefore it is a useful preventative measure to regularly perform a database consistency check.

Please refer to RAN PLM info 662, 664, 808, 914, 941, for more details on the different types of corruptions and possible remedies.

**Command argument**

When the command is run on its own without option nor argument, it will make a CV (cvmk), fetch the db.dat file (ftget), remove the cv (cvrm), then analyse the db.dat on the workstation and look for corruptions.

The argument (optional) can either be:

- the name of the CV to fetch and process.
- the path to a db.dat file, cv.zip, or dbdump.zip that has been fetched previously and is located on the workstation.
- the path of a folder containing logs of the dbc printout run from mobatch ("a" option).

**Command options**

- s (dbcs): to fetch and check the startable CV. Only applicable in online mode.
- a (dbca): to analyse existing dbc logs, taken with mobatch from many nodes or db.dat files. The dbca command combines the multiple dbc printouts into one single dbc printout showing all exceptions found in the different nodes or db.dat files.

**Running a consistency check on the whole network**

- If the db.dat, cv.zip, or dbdump.zip files have already been collected, it is possible to audit them all in parallel with mobatch. The syntax is:

mobatch \[-r\] -d /path/to/folder dbc

In this case mobatch will run the moshell sessions in sql mode against the files instead of against the nodes.

The first argument must specify the path to the folder containing the db.dat, cv.zip, or dbdump.zip files.

The -r option is for recursive search in the folder, otherwise only the files directly under the folder are examined.

- If the dbdat/cvzip files have not previously been collected, it is possible to run : mobatch /path/to/sitefile dbc In this case mobatch will run the moshell sessions in online mode against each node specified in the sitefile and audit the current CV.

**Background info**

The configuration data of the node is kept in a SQL database in RAM memory on the central MP and can be backed up on disk (/d/configuration/cv) for permanent storage. The main purpose of the database is to store the persistent data of the MOs. An MO is made of up to three layers:

- the MAO layer (Management Adaption Object)
- the FRO layer (Facade Resource Object)
- the RO layer (Resource Object)

An MO always consists of one MAO. There is a one to one relation between the MO and its MAO.

Underneath the MAO there can be one or more FROs, or in some cases no FRO. Examples: The SwAllocation MO consists only of a MAO without FRO/RO. The Mtp3bSpItu MO consists of one MAO and one FRO/RO. The Aal2PathVccTp MO consists of one MAO and two FROs/ROs. The FROs are used for controlling the actual resources, the ROs.

The MAOs and FROs use separate SQL tables for data storage. The ROs do not store any persistent data as this is handled by FRO.

The MAOs keep their persistent data in the SQL table modata_r2 or modata_r3. For the FROs, there is a separate table for each MO class. For instance the FROs of PlugInUnit MOs use the table cspiuresource, the FROs of Program MOs use the table cspgmresource, etc.

**Printout example and comments**

Important to keep in mind: the same fault can have appear in several of the checks below. For instance, an MO which has not been correctly deleted from the node could result in corruption shown in checks 8, 12, 13. A UtranRelation with incorrect frequencyRelationType will result in corruption shown in checks 17 and 18. Usually when the same fault appears in several checks, the fault that is higher up in the list is the one that should be fixed first.

\------------------------------------------------------------------------------

1) MAOs with non-recommended characters in the MAO name

(recommended range: -\_/.A-Za-z0-9!%:\*): YES

2039 TransportNetwork=1,AtmTrafficDescriptor=UBR+\_230_QoS3 MAO name: UBR+\_230_QoS3

5642 RncFunction=1,IubLink=iub 45 MAO name: iub 45

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The MOs above contain a "+" and space sign in their MO id. These characters are not known to have a system impact on the node but it is not recommended to use them as they may not be handled properly by the O&M client (moshell/AMOS/OSSRC). Having MOs in this list will give the result "OK with warnings". MOs can be renamed by using the "rset" command.

\------------------------------------------------------------------------------

2) MAOs with dangerous characters in the MAO name ‘,=^"|’Â (HL11572/UABtr75948): YES

5631 TransportNetwork=1,Aal2PathVccTp=TransportNetwork=1,Aal2PathVccTp=88

MAO name: TransportNetwork=1,Aal2PathVccTp=88

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The MO above contains strictly forbidden characters in the MO id: "," and "=". Using these characters can cause cyclic node restarts, see TR HL11572/UABtr75948.

\------------------------------------------------------------------------------

3) MAOs without FROs: YES

3321 Aal2PathVccTp=Iuc-2300-2351-7-95 : aal2pathepfroid=5 not found in table aal2pathepfrotable_6 5644 IubLink=503 : theclientsuniqueid=33 not found in table roamfroiublinkdbtable_09

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Here we have some MOs where the MAO is pointing to a non-existing FRO. Start moshell in sql mode towards the db.dat file

(moshell -d /path/to/db.dat) and run the "get" command on these MOs. For instance, the "get" command will show that the IubLink MO has froId value 33 but when looking in the corresponding FRO table roamfroiublinkdbtable_09 with "sql select" command, we will see that there is no entry with this id.

1.  FROs without MAOs: YES

theclientsuniqueid=198 in roamfroexternalgsmcelldbtable_06 (ExternalGsmCell)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Here we have the reverse situation than above. There is no entry in the MAO table which has a froId pointing to this FRO. We can run the command "fro externalgsmcell" to print the froId value of all MAO instances and we will see that none has the froId 198.

\------------------------------------------------------------------------------

1.  MAOs with duplicate LDN: YES

13 SystemFunctions=1,Licensing=1 (known issue: TR UABtr63243 - no impact)

65 SystemFunctions=1,Licensing=1 (known issue: TR UABtr63243 - no impact)

85 SystemFunctions=1,Licensing=1 (known issue: TR UABtr63243 - no impact)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This indicates that there are several entries in the table modata_r2 which refer to the same MAO. Sometimes this can be a problem, especially if the MAO is connected to a FRO. In this case, Licensing MO is made only of a MAO layer so no FRO are affected. This particular problem is known in CPP5/CPP6 and fixed in CPP7. It has no system impact.

\------------------------------------------------------------------------------

6) MAOs with duplicate froId: YES

3440 IubLink=Iub-11 froid=30

3443 IubLink=Iub-22 froid=30

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Here we have two different MAOs that point to the same FRO, this is not allowed since a FRO can only be connected to one MAO. We could check this by starting moshell in sql mode and running the "get" or "fro" command on these MOs to print the froid.

\------------------------------------------------------------------------------

1.  Mismatch between number of MAO and FRO instances: YES

Aal2PathVccTp : 21 MAOs, 41 FROs

(For Aal2PathVccTp, there should be 2 FROs per MAO).

ExternalGsmCell : 1133 MAOs, 1134 FROs

IubLink : 33 MAOs, 32 FROs

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is a summary of issues found in points 3,4,5,6. We count the number of MAO and FRO instances for each MO class and show those where there is a mismatch. The faulty MO instances can be found in one of the previous four checks.

\------------------------------------------------------------------------------

1.  MAOs referring to non-existent MAOs: YES

429 Subrack=MS reservedBy RncFunction=1,IubLink=80

1709 RncModule=1 reservedBy RncFunction=1,IubLink=80

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This indicates that some MOs have a reference to an MO that does not exist on the node. This can happen when a MO is deleted from the node, sometimes the system fails to remove it from reference attributes pointing to it. In example above, the reservedBy attribute of some MOs did not get updated properly when the MO IubLink=80 was deleted from the node.

\------------------------------------------------------------------------------

9) MAOs defined under a different parent than FRO: YES 3441 IubLink=Iub-11,NodeSynch=1 maoParent: IubLink=Iub-11 (30) froParent: 30 (IubLink=Iub-11 IubLink=Iub-22)

3444 IubLink=Iub-22,NodeSynch=1 maoParent: IubLink=Iub-22 (30) froParent: 31 ()

3568 UtranCell=Iub-54-1,UtranRelation=9875a maoParent: UtranCell=Iub-54-1 (145) froParent: 223 (UtranCell=Iub-57-2)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The MAO knows its parent from the LDN. In some cases, the parent address is also stored in FRO by an attribute giving the froid of the parent MO in the MO tree. This check shows if the parent reference stored in MAO is different to the parent reference stored in FRO.

In the first example, the discrepancy is due to the fact that two MAOs have the same froid (problem highlighted in check 6), this issue has a repercussion here since the children of this MO do not know which of the two MOs with froid 30 are the parent.

In the second example, we see the froid of the parent points to a FRO that either does not exist or is not connected to any MAO.

In the third example, we see that the froid of the parent points to a different MO than the one given in the LDN by MAO. Note: the number in brackets next to the LDN is the froId of that MAO.

\------------------------------------------------------------------------------

10) Inconsistent MO references between MAO and FRO: YES

3443 IubLink=Iub-22 sctpRef: Sctp=MS-15 (3) sctpfroid: 2 (Sctp=MS-14)

4135 UtranCell=Iub-11-1 iubLinkRef: IubLink=Iub-11 (30) iublinkfroid: 30 (IubLink=Iub-11 IubLink=Iub-22) 5789 UtranCell=U30717,UtranRelation=U05938 utranCellRef: IurLink=rncka62,ExternalUtranCell=U05938 (1743) nutrancellfroid: 1999 () 2406 IpAccessHostPool=Iub ipAccessHostRef: IpAccessHostEt=ES1-27 IpAccessHostEt=MS-26 IpAccessHostEt=MS-7 ipaccesshostfroid: IpAccessHostEt=ES1-02 IpAccessHostEt=ES1-27 IpAccessHostEt=MS-26

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MO references are sometimes kept in MAO or FRO only, but sometimes they are kept in both parts. It is important that an MO reference kept both in MAO and FRO should be the same in both.

In the first example, the MO has a reference stored in MAO which is different to the one stored in FRO.

In the second example, the reference stored in FRO points to two different MAOs, this is due to the problem highlighted in check 6 with duplicated froid.

In the third example, the FRO reference points to a FRO that either does not exist or does not have a MAO.

In the fourth example, the list of MO references is different in the MAO attribute ipAccessHostRef compared to the FRO attribute ipaccesshostfroid Note: the number in brackets next to the LDN is the froId of that MAO.

\------------------------------------------------------------------------------

11) MAOs missing from reservedBy list: YES

2401 IubLink=Iub-1226 sctpRef Sctp=MS-15 reservedBy

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check indicates that the MO on the left has a reference to the MO on the right (via the attribute stated in the middle) but does not appear in the reservedBy list of the MO on the right. To check this we start moshell in sql mode (moshell -d dbdat/cvzip) and perform the get command on the MO on the right and we see that the MO on the left cannot be found in the reservedBy list eventhough it has a reference to that MO. This is a one-way relation between the MOs and is a fault.

\------------------------------------------------------------------------------

12) MAOs found only in reservedBy list: YES

858 RncModule=11 reservedBy IubLink=Iub-198

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This is the opposite problem than the previous check. It indicates that the MO on the right (in this case the IubLink) appears in the reservedBy list of the MO on the left, even though it has no reference to that MO. To check this we start moshell in sql mode (moshell -d dbdat/cvzip) and perform the get command on the MO on the right. We will see no attribute containing any reference to the MO on the left. When we do the get command on the MO on the left we see that the MO on the right appears in the reservedBy list anyway. This is a one-way relation between the MOs and is a fault.

\------------------------------------------------------------------------------

13) Inconsistent sequence of moRefs in MAO: YES

1003 SectorAntenna=1,AuxPlugInUnit=RRU-1 persistentReservers: 5, actual: 7

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check applies to MAO attributes of type sequence:moRef. It indicates if there is a discrepancy between the announced number of MO references in the attribute (shown at the beginning of the attribute value, in square brackets, eg: \[5\]), and the actual number of MOs listed in the attribute. In the example above, the attribute is supposed to be a sequence of 5 MOs but in fact it contains 7 MOs. To check, start moshell in sql mode and perform the "get" command on the MO.

\------------------------------------------------------------------------------

14) FROs referring to non-existent FROs (CSR1473974): YES

6513 SpDevicePool=DcDevice,DcDevice=1 subrackfroid 9 ()

6494 RncModule=13 piufroid 45 ()

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check shows the FROs that have a reference to a FRO that does not exist on the node. Only MOs which have not already been displayed in check number 10 will be displayed here. To find out the faulty FRO table and row, start moshell in sql mode and perform the "get" command on the MO.

\-----------------------------------------------------------------------------15) Remaining old FRO table versions (HL93894/WRNae89948/HM76376/HS48645/HR63086): YES cspgmresource_03 (current): cspgmresource_02 (old) csxpresource_01 (current): csxpresource (old)

ecnprsectordata_4 (current): ecnprsectordata_3, ecnprsectordata_2, ecnprsectordata_1 (old)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check shows the FRO tables which exist in multiple versions: the latest table version is shown on the left-hand side, and the list of old table versions is shown on the right-hand side. The old table versions should normally be removed at system upgrade.

\------------------------------------------------------------------------------

16) Corrupted MAO entries in modata table: YES

3280 Aal2QosProfile=adoffbdoff reservedBy incorrect nrOfElements: qF3||rF1=1,5=1,141=aal2pathvcctp=99||rF1=1,5=1,141=TransportNetwork=1,141=88|rF1=1,5=1,141=TransportNetwork=1,169=88

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* This check looks at the syntax of the attribute data of the MAOs listed in the modata_r2/modata_r3 table. Any corrupted attribute data will be shown as an exception in the get printout for that MO. The correct syntax of each entry should be: MoType^Revision^LDN^PrimaryKey^attributeName^attributeData^ And the syntax of the attribute data should be: dataType AVCflag Data . With:

dataType: s=String, r=Reference, t=Struct, f=Float, q=Sequence, i=Integer, l=Long, b=Boolean

AVCflag: T=isAVCNotifier , F=notAVCNotifier

Sequence: dataType AVCflag noOfElements|attributeName|attributeData|....

Struct: dataType AVCflag noOfElements attributeName attibuteData ....

17) MAOs without parent: YES

14498 AtmPort=ES-1-2-1-ima55,VplTp=vp1,VpcTp=1 missingParent: AtmPort=ES-1-2-1-ima55,VplTp=vp1

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check reports the list of MAOs whose parent does not have an entry in the modata_r2/modata_r3 table.

\------------------------------------------------------------------------------

18) MAOs with invalid froId: YES

22458 Subrack=ES-2,Slot=21,PlugInUnit=1,GeneralProcessorUnit=1,LoadControl=1 froId=

22485 Subrack=ES-2,Slot=20,PlugInUnit=1,GeneralProcessorUnit=1,LoadControl=1 froId=

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check reports the list of MAOs that have a invalid FRO id, e.g. empty value instead of integer.

\------------------------------------------------------------------------------

19) Instance-based PM Scanners containing missing MO instances (HR95951/CSR2375943/CSR2375969/ER690205): YES 533 USERDEF.RNC_CNHH_RNC71_3.Profile=982.Continuous=Y.STATS missing MO instances: UtranCell=BU317L,UtranRelation=BU980L

536 USERDEF.RNC_CNHH_RNC71_4.Profile=983.Continuous=Y.STATS missing MO instances:

UtranCell=BU530L,UtranRelation=BU279L

UtranCell=BU530L2,UtranRelation=BU279L2

624 USERDEF.RNC_CNHH_RNC71_2.Profile=981.Continuous=Y.STATS missing MO instances:

UtranCell=BU279M,UtranRelation=BU279N

UtranCell=BU279K,UtranRelation=BU279N

UtranCell=BU279L,UtranRelation=BU279N

UtranCell=BU279L,UtranRelation=BU530L

UtranCell=BU279M2,UtranRelation=BU279N

UtranCell=BU279L2,UtranRelation=BU279N

UtranCell=BU279L2,UtranRelation=BU530L2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check reports the list of Instance-based PM scanners that contain MO instances which don’t exist anymore in the node. Any such scanners should be deleted and replaced with Class-based scanners or Instance-based scanners containing existing MO instances. The scanners can be printed in dbdat mode with pst/pgets. Refer to TR HR95951 or PLM info 914 for more info.

\------------------------------------------------------------------------------

20) Instance-based PM Scanners containing more than 1000 MO instances (HR95951/CSR2375943/CSR2375969/ER690205): YES

533 USERDEF.RNC_CNHH_RNC71_3.Profile=982.Continuous=Y.STATS number of MO instances: 10118

536 USERDEF.RNC_CNHH_RNC71_4.Profile=983.Continuous=Y.STATS number of MO instances: 10271

624 USERDEF.RNC_CNHH_RNC71_2.Profile=981.Continuous=Y.STATS number of MO instances: 10602 627 USERDEF.RNC_CNHH_RNC71_1.Profile=881.Continuous=Y.STATS number of MO instances: 10892

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check reports the list of instance-based PM scanners that contain more than 1000 MO instances. It is recommended to replace these scanners with Class-based scanners due to impact on the node JVM performance. The scanners can be printed in dbdat mode with pst/pgets. Refer to TR HR95951 or PLM info 914 for more info.

\------------------------------------------------------------------------------

21) Jvm admClassPath containing LoadModules not part of the current UpgradePackage (CSR2447811): YES

7 Jvm=1 incorrect LMs in admClassPath: CXC1720482_R73D61 CXC1727628/2_R5X02 CXC1726723_R73D03 CXC1725907_R73D62 CXC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check reports if the Jvm admClassPath contains any LMs that are not listed in the current UpgradePackage (attribute: ConfigurationVersion::currentUpgradePackage::loadModuleList)

\------------------------------------------------------------------------------

22) Missing FRO tables: YES dnsclient (IpOam) httpsdb (WebServer)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check reports if there are MAO instances where the corresponding FRO table is missing. The output shows the name of the missing FRO table and the corresponding MO class. This is a complement to check 3 which detects MAO instances where the FRO entry is missing from the FRO table but does not detect cases where the whole FRO table is missing.

\------------------------------------------------------------------------------

101) FRO attributes containing the froId field but not the ldn field (HR88263): YES

1.  EUtraNetwork=1,ExternalENodeBFunction=5051-530675,ExternalEUtranCellFDD=5051-530675-2 parentref,eutranfrequency
2.  EUtranCellFDD=SHBDEM2,EUtranFreqRelation=1275,EUtranCellRelation=5051-530675-2 parentref,neighborcellref

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RBS/ERBS only and does not appear in other node types (RNC/MGW). This check shows if there are any attributes containing the text "<attr name="froId"" but not the text "<attr name="ldn"".

\------------------------------------------------------------------------------

1.  MTP3 pointCode collision (WRNae82362, SCS695737): YES

Point code 13749348 used by Mtp3bSpAnsi=1 and Mtp3bSpAnsi=1,Mtp3bSrs=r821s

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC/MGW nodes only and does not appear in other node types (RXI/RBS).

This check shows if there are any MTP3 routes that use the same destinationPointCode as the node’s own point code. To check this, start moshell in sql mode and run the "get" command on both MOs listed to crosscheck that the pointcode is the same. The fault is described in TR WRNae82362.

\------------------------------------------------------------------------------

1.  Number of Fans mismatch (CSR 2101402/HQ64197): YES

23 Equipment=1,Subrack=MS nrOfFans: 4 nr_denib: 2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC/MGW nodes only and does not appear in other node types (RXI/RBS).

In addition, it only applies to the nodes that use Subracks with fanConfiguration BFD528, eg. RNC3820, MGW GMPv4.

The purpose is to check if the number of Fan MOs defined under each Subrack is the same as the number of fans specified in the attribute numberOfDenibDevices (if >0) or in the attribute Subrack::subrackProdType::fanConfiguration (if numberOfDenibDevices <0).

\------------------------------------------------------------------------------

103) Inconsistency in UtranRelation nodeRelationType or frequencyRelationType

(HP94489/WRNae68940/WRNae72810): YES

5596 UtranCell=Iub-10-1,UtranRelation=Softer-Iub-10-3 nodeRelationType: 1, actual: 0 (cellRef:UtranCell=Iub-10-3)

22205 UtranCell=U31618,UtranRelation=U31477 frequencyRelationType: 1, actual: 0 (f1=f2=1007)

37068 UtranCell=85276B,UtranRelation=1 frequencyRelationType: 0, actual: 1 (f1=10737, f2=10713)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC only and does not appear in other node types. It is only for MO instances of type "UtranRelation" and cross-checks the value of the attributes nodeRelationType and frequencyRelationType against the real setting.

The first UtranRelation in the example has nodeRelationType set to 1 (Inter-RNC, meaning it is supposed to be a relation to an ExternalUtranCell) but the cellReference to which it is pointing to is an internal UtranCell, so it should actually have the nodeRelationType 0 instead of 1.

The second UtranRelation MOs in the example has a discrepancy in the frequencyRelationType which is set to 1

(Inter-frequency) whereas the originating Cell and destination Cell have the same frequency, so it should actually be 0 (Intra-frequency). The third UtranRelation is the opposite scenario where the frequency of the originating Cell and destination Cell are different but the frequencyRelationType is set to 0 (Intra-frequency).

\------------------------------------------------------------------------------

104) Inconsistency in UtranCell interFreqRelCntr or intraFreqRelCntr

(HP94489/WRNae68940/WRNae72810): YES

364 UtranCell=85162B intraFreqRelCntr: 27, actual: 28 (by frequencyRelationType and uarfcnDl)

364 UtranCell=85162B interFreqRelCntr: 1, actual: 0 (by frequencyRelationType and uarfcnDl)

680 UtranCell=85276B intraFreqRelCntr: 25, actual: 24 (by uarfcnDl)

680 UtranCell=85276B interFreqRelCntr: 0, actual: 1 (by uarfcnDl)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC only and does not appear in other node types. It is only for MO instances of type "UtranCell" and cross-checks the value of the attributes intraFreqRelCntr and interFreqRelCntr against the real setting.

The real setting is checked by checking the frequencyRelationType of the UtranRelations defined underneath the UtranCell. Both the frequencyRelationType attribute and the real frequencyRelationType (found out by looking at the uarfcn of originating and destination cell) are checked.

To check this manually, start moshell in sql mode (moshell -d cvzip/dbdat) and run the command "lget utrancell=xxx cntr|freq.\*type". It will show the value of the cell’s freqRelCntr and frequencyRelationType of underlying relations. If they mismatch, the cell is shown as mismatching "by frequencyRelationType and uarfcnDl". If they match but some of the frequencyRelationType settings are incorrect (see previous check 17) then the mismatch will by shown "by uarfcnDl".

In the first two lines we can see that the UtranCell 85162B has 27 intra-frequency relations and 1 inter-frequency relations. When we check the frequencyRelationType attribute and the uarfcn of the originating and destination cells, both indicate that this is not correct. It appears that there is actually 28 intra-frequency relations and 0 inter-frequency relations. In the next two lines we can see that the UtranCell 85276B has 26 intra-frequency relations and 0 inter-frequency relations, but in reality there are 24 intra-frequency and 1 inter-frequency. In this case the frequencyRelationType setting of the UtranRelation is misleading and has been flagged in check 15.

\------------------------------------------------------------------------------

1.  Inconsistency in RncFunction cellRelCntr (HT37388): YES

RncFunction=1 cellRelCntr=21743, nrOfRelations=21410 (1304 CoverageRelation, 6 EutranFreqRelation, 12 GsmRelation, 2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC only and does not appear in other node types. It checks that the value of the attribute cellRelCntr in the RncFunction MO should be equal to the total number of MO instances of type

CoverageRelation+EutranFreqRelation+GsmRelation+UtranRelation. It can be checked manually with the command: prs relation=

Note: from W15B onward, this inconsistency can be fixed by running the command facc rncfunction=1 recalculateInternalCounters

1.  Inconsistency in UtranCell gsmRelHoAndCellReselCntr: YES

5289 UtranCell=U32194C gsmRelHoAndCellReselCntr: 21, actual: 22

17389 UtranCell=G32105C gsmRelHoAndCellReselCntr: 25, actual: 22

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC only and does not appear in other node types. It checks that the value of the attribute gsmRelHoAndCellReselCntr in each UtranCell MO should be equal to the actual number of children GsmRelation MOs with mobilityRelationType=0. It can be checked manually with the command: get utrancell=xxx,gsmrelation mobilityRelationType ^0 Note: from W15B onward, this inconsistency can be fixed by running the command facc utrancell=xxx recalculateInternalCounters

\------------------------------------------------------------------------------

107) Inconsistency in UtranCell cellReselectionCntr: YES

2749 UtranCell=32S1C1 cellReselectionCntr: 1, actual: 6

2753 UtranCell=32S1C2 cellReselectionCntr: 12, actual: 9

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC only (>= W15B) and does not appear in other node types or older SW releases. It checks that the value of the attribute cellReselectionCntr in each UtranCell MO should be equal to the actual number of children UtranRelation MOs with frequencyRelationType=1 and mobilityRelationType=0 or 2. It can be checked manually with the command: hget utrancell=xxx,utranrelation frequencyRelationType|mobilityRelationType 1 ^\[02\]

Note: from W15B onward, this inconsistency can be fixed by running the command facc utrancell=xxx recalculateInternalCounters

\------------------------------------------------------------------------------

108) Inconsistency in UtranCell handoverOnlyCntr: YES

2749 UtranCell=32S1C1 handoverOnlyCntr: 12, actual: 9

2753 UtranCell=32S1C2 handoverOnlyCntr: -4, actual: 2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Comment \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This check is specific for RNC only (>= W15B) and does not appear in other node types or older SW releases. It checks that the value of the attribute handoverOnlyCntr in each UtranCell MO should be equal to the actual number of children UtranRelation MOs with frequencyRelationType=1 and mobilityRelationType=0 or 1. It can be checked manually with the command: hget utrancell=xxx,utranrelation frequencyRelationType|mobilityRelationType 1 ^\[01\]

Note: from W15B onward, this inconsistency can be fixed by running the command facc utrancell=xxx recalculateInternalCounters

**4.3.6 dbd\[p\] \[&lt;cvname&gt;|&lt;dbdat-file&gt;|&lt;cvzip-file&gt;\] \[&lt;cvname&gt;|&lt;dbdat-file&gt;|&lt;cvzip-file&gt;\]**

Purpose: To compare the data of two CVs or db.dat files

**Options:**

- p: to compare only the Program MOs. For instance, can be used to find out if some Program MOs were accidentally deleted in the executing CV compared to the loaded CV.

**Arguments:**

- the name of the CV to fetch and process.

or:

- the path to a db.dat, cv.zip or dbdump.zip that has been fetched previously and is located on the workstation.

Uservariables:

- dbd_exclude_moclasses : to exclude certain MO classes from the comparison • dbd_exclude_attributes : to exclude certain attributes from the comparison **Examples:**
- dbd Rb_CXP9021775_R1BF04_121217_2155 Fi_CXP9021775_R1BF04_121217_2201 - comparing the CV before upgrade and the CV after upgrade
- dbd /home/userid/rnc1.db.dat /home/userid/rnc2.db.dat - comparing a db.dat from one node against the db.dat of another node

**4.3.7 dbcv\[r\]**

Perform a DB consistency check (dbc) on the db.dat files of the CVs stored on the node.

The result of the dbcv execution is stored on the node at /c/public_html/dbcv.txt and is read by the cvls and al commands, if the uservariable use_dbcv is set to 1. The dbcv command only checks CVs with unknown DBC status, unless option r is given (dbcvr) in which case all CVs are checked again.

When use_dbcv=1 (and mosalarm=1), a Moshell generated alarm with severity Warning will appear in the al printout indicating the number of CVs where DBC status is NOK.

Example:

Warn DBC NOT OK on 7 CVs ConfigurationVersion=1 (Moshell generated alarm)

When use_dbcv=1, the cvls printout will contain an additional column DBC, showing the DB consistency status of each CV.

Example:

\=================================================================================================

Id CV Name Creation Date UpgradePackage Release Type Operator DBC Comment

\=================================================================================================

1.  RNC11_W12.0 2013-07-24 12:23 CXP9014711/4_R4LB W12.0.2.10 other eanzmagn NOK none
2.  RNC11_W14.0_OK 2014-02-16 11:23 CXP9021776/1_R3AA03 W14.0.1.0 other eanzmagn OK none
3.  RNC11_W14.1.2.2 2014-12-22 06:58 CXP9021776/2_R4CA06 W14.1.2.2 other eanzmagn OK none =================================================================================================

The DBC column can show four different results:

- - OK : the DBC command did not detect any inconsistencies in the db.dat file of this CV
    - NOK (NOT OK): the DBC command detected one or more inconsistencies with negative impact in the db.dat file of this CV
    - OKW (OK with Warnings): some inconsistencies were found in the db.dat file of this CV, but there is no negative impact
    - ? (unknown): the DBC check has not yet been done for this CV, please run the "dbcv" command to populate the missing status

**4.3.8 &lt;ose/coli command&gt; \[|&lt;unix-cmds&gt;\]**

Send a COLI command to the CPP node’s OSE shell. Type "h ose" for syntax help and "?" to view available commands.

The command are sent to the node using either telnet or ssh, depending on the value of the moshell setting secure_shell (See Section **??**)

The password is not required if it is defined in the ipdatabase or the $password variable (otherwise, the user will be prompted to enter the password).

To find out all available COLI commands, type ? or lhsh &lt;lnh&gt; ?

It is possible to pipe the command to any external utility the machine which moshell is running on has installed (such as **grep**). Example:

- - ls -l /d/loadmodules | sort -nk 3 : to sort LMs by size
    - te log read | /home/eric/tools/decoder.pl | /home/eric/tools/flow.pl
    - lhsh 001400 te log read | grep -i error : to show errors in TE log

Several commands can be run on the same line by separating each command with a semicolon.

If more than 5 commands are specified on the line, then these will be sent via a command file on the node (quicker).

The user variable fast_coli_threshold controls the number of commands above which a command file will be transferred to the node.

By default it is 5 but it is possible to reduce or increase this setting with the uv command (see chap 2.5 for more info on uservariables).

For instance by setting fast_coli_threshold to 0, COLI commands will always run via command file, this can help to avoid printout corruptions (certain commands producing large printouts can sometimes get corrupted by spurious echo characters when run directly without command file).

**Examples:**

- - vii ; pwd ; cd /d/loadmodules ; pwd ; llog
    - lhsh 001100 ; vii ; te e trace1 NBAP\*
    - lhsh 001400 ; te filter set "(\[1\]&lt;8)OR(\[1\]&gt;=9)AND(LEN<>33)" NBAP\*
    - lhsh 001400 ; te filter set "(\[1\]&lt;>8)AND(\[1\]<&gt;$12)AND(\[1\]&lt;>$14)AND(\[1\]<&gt;$11)" NBAP\*
    - lhsh 001400 ; te log freeze -grp state_change

"WaitForActivation -> WaitForCapacity" 100

- - lhsh 012000 ; MsbHostMo_StartPing -d 10.173.137.130 -z 10.173.137.1

- - lhsh 000200 ; EtHostMo_startPing -d 10.164.41.132 -h 1 -c 20 -s 54

Note that it is safer to do lhsh &lt;lnh&gt; &lt;command&gt; instead of lhsh &lt;lnh&gt; ; command in case the board is not reachable. Example: if you want to format /d on board 001400: if you do lhsh 001400 ; formathd /d and the board 001400 is not reachable then the command is sent to the Hub MP whereas with the command lhsh 001400 formathd /d, if the board

001400 is not reachable then the command is not sent at all. But for certain commands like "te filter set", "te log freeze", "EtHostMo_startPing" or "MsbHostMo_StartPing", the semicolon has to be entered after the "lhsh" in order to force moshell to actually log into the board.

**Running SQL commands**

**Examples:**

- - sql+ (start the sqlc client on the node)
    - sql select name from tables
    - sql select \* from tables where name like ’%iur%’
    - sql select \* from cspgmresource_01 where pno=’CXC 132 0784’
    - sql update cspgmresource_01 set poolsize=20000000 where pno=’CXC 132 0784’; commit;

Note: If the osa_coli program is running on a different board than the hub MP, semicolons must be put around sqlc:

- - lhsh 001100 ; sqlc ; select \* from tables

**Running 3GSIM/CORBEN/LOCO commands**

**Examples:**

- 1.  crb st
    2.  crb rf -f /c/corben/uefile.cmd;crb rf -f /c/corben/cellfile.cmd
    3.  3gsim lb
    4.  3gsim lss
    5.  loco ls
    6.  corben ; ts ; statistics
    7.  corben ts ; corben statistics

**Running NCLI commands**

Note: ncli command completion not supported when run from moshell

**Examples:**

- - ncli alarms - Active alarm list
    - ncli help ; man search - List ncli commands. Print help of the ncli command "search"
    - ncli search . "" - List all MOs
    - ncli search . "" operationalState==0 - List all disabled MOs
    - ncli search . "" operationalState==0 AND administrativeState==1 - List all MOs unlocked and disabled
    - ncli group -a -e ( . "" operationalState==0 ) ; get -group userLabel - Put all disabled MOs in a group, then read the userLabel attribute of these MOs
    - ncli ; get . userLabel ; set . userLabel=(String)RNC11 ; get . userLabel - Read and change userLabel attribute on ManagedElement MO

Adding/Removing a static route:

- - ncli action IpOam=1,Ip=1,IpRoutingTable=1 addStaticRoute (String)"0.0.0.0" (String)"0.0.0.0" (String)"137.58.152.1" (int)110 (boolean)false
    - ncli action IpOam=1,Ip=1,IpRoutingTable=1 deleteStaticRoute { destinationIpAddr=(String)"0.0.0.0" destinationNetworkMask=(String)"0.0.0.0" nextHopIpAddr=(String)"137.58.152.1" routeMetric=(int)110 }

Other examples:

- - ncli ; cd TransportNetwork=1 ; search . AtmPort ; search . AtmPort operationalState==0
    - ncli group -a -e(. UpgradePackage);group -l;get -group state;

action SwManagement=1,UpgradePackage="CXP9013831_R9YC/6" verifyUpgrade **Running CMXB commands on HCS node (RNC3820/MGW GMPv4).**

**Examples:**

- - lhsh 000100 cmxbsh ; help ; ls /bin ; ls /usr/bin ; iss ; help
    - lhsh 000000 cmxbsh ; iss ; show interfaces status; show mac-address-table
    - lh scb cmxbsh ; iss ; show interfaces status; show mac-address-table **Running CMXB/SCXB commands on EvoC (RNC8200).**

**Examples:**

- - xbsh 000200 ; help ; ls /bin ; ls /usr/bin ; iss ; help
    - lh cmxb help ; ls /bin ; ls /usr/bin ; iss ; help
    - lh scxb help ; ls /bin ; ls /usr/bin ; iss ; help
    - lh xb help ; ls /bin ; ls /usr/bin ; iss ; help

**Running telnet commands in MSB4 (MGW)**

The telnet username (and password if applicable) must be entered after the telnet command, separated by semicolons and the exit command must be given at the end.

**Examples:**

- - lhsh 000700 telnet 10.7.0.5 ; root ; shroot ; pwd ; ls -l /var ; exit

**Changing shell password**

**Examples:**

- - passwd ; &lt;old password&gt; ; &lt;new password&gt;
    - secmode -l 2 ; &lt;new password&gt;

**Running commands towards an AXE node (prerequisite: uservariable "lincli" must be set to 3).**

**Examples:**

- - allip
    - rxmsp:mo=rxotg-17,subord
    - rxbli:mo=rxotrx-17-1 (command will be auto-confirmed)

Limitations: it is not possible to release the terminal in order to view "ordered" printouts.

- - 1.  **coli**

Open an interactive COLI or RCS-COLI session to the node.

- - 1.  **comcli**

Open an interactive COMCLI/ECLI session to the node. Only applicable for COM nodes.

- - 1.  **ecli**

Open an interactive ECLI session to the node. Only applicable for COM nodes.

- - 1.  **esci**

Start Ericsson Support Command Interface mode. Only applicable for EMCLI (RCS nodes).

- - 1.  **netconf\[y\]\[g\]\[gx\] \[&lt;commandfile&gt;\]**

Open an interactive NETCONF session to the node or execute a NETCONF command file. Only applicable for COM and YANG nodes.

**Options:**

- - y: to execute a netconf/yang command file.
    - g: no processing of the output. More suitable for doing a netconf "get".
    - gx: same as "g" but only with the "&lt;data&gt;" part and without xmlns tags.

Witout option, the output is processed showing each command and reply on a individual line. More suitable for netconf "write" operations.

Note: The idle timeout of the netconf session can be configured in the uservariable netconf_timeout. Default 300 seconds.

Examples of netconf files can be found under moshell/commonjars/scripts/netconf.

**4.3.14 c+/c1/c2/c-/c?/c0**

Switch between the COM node’s linux shell, rcs-coli shell or comcli shell.

To switch between the linux/rcs-coli shell and the comcli shell, use the command c+/c1/c2 :

- - c+ sets the uservariable comcli to 2, giving access to the comcli shell
    - c1 sets the uservariable comcli to 1 and coli_shell to 1, giving access to the rcs-coli shell
    - c2 sets the uservariable comcli to 1 and coli_shell to 2, giving access to the linux shell

If the node does not have a rcs-coli shell then the commands c1 and c2 will be equivalent, and it is also possible to use the command c-.

The c? command is for checking what is the current shell.

By default, moshell will automatically send comcli/coli/linux commands to the appropriate shell.

This feature can be deactivated by setting the uservariable smart_shell to 0 (1 is default).

It is also possible to force a command to be sent to a specific shell by typing c+, c1, or c2.

To return to automatic shell detection, it is possible to use the command c0.

**4.3.15 &lt;linux/rcs-coli/comcli command&gt; \[|&lt;unix-cmds&gt;\]**

Send CLI commands to the COM node’s linux shell, rcs-coli shell or comcli shell.

The commands are sent to the node over ssh. The password is not required if it is defined in the ipdatabase or the $password variable (otherwise, the user will be prompted to enter the password).

To print the list of linux commands, type "ls" on the list of directories shown in the $PATH environment variable (echo $PATH). To print the list of rcs-coli commands, type "help". To print the list comcli commands, type "?" in comcli mode.

To switch between the linux/rcs-coli shell and the comcli shell, use the command c+/c1/c2 :

- - c+ sets the uservariable comcli to 2, giving access to the comcli shell
    - c1 sets the uservariable comcli to 1 and coli_shell to 1, giving access to the rcs-coli shell
    - c2 sets the uservariable comcli to 1 and coli_shell to 2, giving access to the linux shell

If the node does not have a rcs-coli shell then the commands c1 and c2 will be equivalent, and it is also possible to use the command c-.

To switch between linux shell and rcs-coli shell, the uservariable linux_shell can be used:

- - linux_shell=0 -> rcs-coli shell
    - linux_shell=1 -> linux shell

Within the comcli shell, there are two modes: exec mode and config mode. Exec mode is the default. To switch to config mode type "configure". The comcli allows to perform MO commands (get, set, create, delete, action, etc). More information about the comcli shell can be found in the document 1/1553-FAE 151 01 ("CLI Style"). All MO commands can also be performed using moshell’s own MO commands.

It is possible to pipe a shell command to any external unix utility, eg "grep", "sort", etc. The pipe sign must be surrounded by a blank space on each side. It is also possible to use the built-in COMCLI command "filter", in that case no spaces shall be around the pipe sign. See examples below.

Each command line is sent in a separate ssh session, so in order to send several commands within the same ssh session, they need to be run on the same line by separating each command with a semicolon.

**Examples:**

- - ls -l /d/loadmodules | sort -nk 3 - to sort files by size
    - ps -ef | grep com - to see the list of com processes
    - find /bin -ls - recursive list all files and directories in /bin
    - bash && for file in /bin/\*; do echo $file ; done ; exit - open a bash shell and do a for loop on all files inside the /bin directory
    - c+ - to switch to comcli shell
    - show ManagedElement=1,Equipment=1,RbsUnit=1 ; configure ;

ManagedElement=1,Equipment=1,RbsUnit=1,userLabel="test" ; end

- - show all | grep Schema
    - show all|filter Schema
    - c2 to switch back to linux shell

Refer to the moshell file for more information about the uservariables for COM nodes:

- - comcli
    - linux_shell
    - cliss
    - comcli_columns
    - comcli_timeout
    - comcli_cfg
    - comcli_model
    - comcli_retry_maxtime
    - comcli_retry_interval
    - comcli_port
    - comcli_mom

**4.3.16 mcl\[d\] \[&lt;moClass-filter&gt;\] \[&lt;command-filter&gt;\]**

List the available MO-Context COMCLI commands.

**Examples:**

- - mcl - List all MO-Context COMCLI commands
    - mcl bridg - List all MO-Context COMCLI commands available on MO class "Bridge"
    - mcl . clear - List all MO-Context COMCLI commands matching the word "clear"
    - mcld - List only the MO-Context COMCLI commands without parameter description

**4.3.17 mcc/lmcc &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; &lt;comcli commands(s)&gt; \[|&lt;unix-cmds&gt;\]**

Execute MO-Context COMCLI commands.

Execute a COMCLI command from within a specific MO.

**Examples:**

List all COMCLI commands applicable to all Router MOs and their children (the command ? or __can be used to list COMCLI commands)

- - lmcc router= ?
    - lmcc router= \\t

Print more help on the ping command in the MO InterfaceIPv4=TNA

- - mcc interfaceipv4=tna ping ?

Run the ping command from all AddressIPv4 MOs and pipe the output through grep

- - mcc addressip ping --count 3 10.18.30.2 | grep transmitted

**4.3.18 bo\[ar\]/ba\[swdpmu\]/br\[wdm\]/be\[0-50\]/bp**

Manage board groups that can be used for running COLI commands on multiple boards.

Syntax:

- - bo\[a\]\[r\]
    - ba\[s\]/br/bp &lt;boardGroup&gt; &lt;boardLNH&gt;|&lt;boardGroup&gt;|&lt;boardType&gt;
    - baw\[s\]/brw &lt;boardGroup&gt; &lt;swa&gt; \[&lt;rncMod&gt;\]
    - bam\[s\]/brm &lt;boardGroup&gt; &lt;MO Group&gt;

|     |     |
| --- | --- |
| • bad/brd | &lt;boardGroup&gt; &lt;devType&gt; \[&lt;rncMod&gt;\] |
| • bap | &lt;boardGroup&gt; &lt;pgm&gt; |
| • bau | &lt;boardGroup&gt; &lt;rpuLabel&gt; |
| • be\[0-50\] | &lt;boardGroup&gt; &lt;boardGroup&gt; |

The following board groups are always created by default after running any of the board commands (bo/ba/br/lh, etc) the first time:

- - all contains all boards (MP/BP) as well as PiuDevices (d0000x) and SPMs (spx.lnh).
    - allp contains all boards (MP/BP) but not PiuDevices and SPMs.
    - allpd contains all boards (MP/BP) and PiuDevices but not SPMs.
    - alld contains all PiuDevices and SPMs.
    - mp contains all MP boards.
    - bp contains all BP boards.
    - coremp contains the core MP(s), one or two depending on the configuration.
    - ommp contains the O&M MP(s), one or two depending on the configuration.
    - sccpmp contains the SCCP MP(s) (RNC/MGW only).
    - tu contains TU boards.
    - scx contains SCB and SXB boards.
    - et contains ET boards.
    - aal2ap, aal2nccadm, aal2cpsrc, aal2rh contain MP boards running the corresponding aal2 programs.

In RNC, the following board groups are also created by default, containing MPs/SPMs connected to the various RNC modules:

- - mod\[x\]
    - cc\[x\]
    - dc\[x\]
    - pdr\[x\]

In RBS, the following board groups are created by default: rax, tx, ru, asc.

In MGW the following board groups are created by default: mesc, licdb, ch, stc, gra, imra, raa, msb.

It is recommended to start by running the bo command (_board overview_) to view the available boards in the node.

The very first time bo is run on a node, it will take more time because it has to fetch data from the node. The following times, the existing data is shown again unless the r swith is used (command bor), in which case the data is fetched again from the node.

By default the bo command only shows slots that contain boards defined in the configuration (i.e. boards which are associated with a PlugInUnit MO) but by using option a it is possible to view all slots, even those which do not contain a PlugInUnit.

The ba command is used for adding boards into a group. The boards shall be identified by their position or a string matching the board type. The s switch adds any related SPMs to the board group.

**Examples:**

- - ba group1 1 2 4-8 114-119 - boards 000100, 000200, 000400 to 000800, 011400 to 011900 are added to _group1_
    - bas group1 223-226 - boards 022300 to 022600 are added to _group1_, together with their related SPs (if these boards

are SPBs).

- - ba group1 spb scb 3 4 - all boards of type matching **spb** and **scb** are added to _group1_ as well as boards 000300 and 000400
    - ba group1 coremp mod scb - all boards belonging to the groups **coremp** and **mod** are added to _group1_ as well as boards with type matching **scb**.
    - ba gpb gpb - all boards of type matching **gpb** are added to the group called _gpb_.
    - ba ru28 rus02b28 - all boards of HW type matching **rus02b28** are added to the group called **ru28**.

The baw command is similar to the ba command except that the boards are identified by their SwAllocation and/or RncModule. Examples:

- - baw moduleMPs module - all boards belonging to the SwAllocation maching **module** will be added in the group called _moduleMPs_
    - baw module1 .\* 1 - all boards belonging to rncModule 1 will be added to the group called _module1_

The bad command is for adding SPMs into a board group based on their device type. This is applicable to RNC only. Examples:

- - bad dc dc - add all SPMs handling a DC device to the group called _dc_.
    - bad dc1 dc 1 - add all SPMs handling a DC device on module 1 to the group called _dc1_.

The bap command is for adding boards into a board group based on what program(s) they are running. The string is matched against the name of the Program MOs. All PlugInUnit MOs which contain a Program MO whose name matches the string are added to the group. Examples:

- - bap mesc cxc1324881|upcf_\*mesc - add all boards containing a Program MO whose name matches cxc1324881 or upcf_\*mesc into the board group mesc

The bau command is for adding boards into a board group based on what RPU(s) they are running. The string is matched against the reliableProgramLabel of the RPU MOs. All PlugInUnit MOs that have a RPU MO whose reliableProgramLabel matches the string are added to the group. **Examples:**

- - bau ranap rnc_ranap - add all boards that have a RPU whose reliableProgramLabel match the word rnc_ranap into the board group ranap

The bam/brm command is for adding/removing boards corresponding the PlugInUnit/Spm/PiuDevice MOs of an existing MO group. When specifying the "s" option ("bams") the children Spm/PiuDevice of the PlugInUnit will be included in the board group.

**Examples:**

- - st plug dis - makes a MO group called st_group containing the disabled PlugInUnit MOs
    - bam boardsdown st_group - makes a board group containing the boards corresponding the disabled PlugInUnits found above

The br command is for removing a whole group or certain boards out of a group.

Negative filter (!) is supported in order to remove all boards except those matching the filter.

**Examples:**

- - br group1 1 3 gpb - boards 000100, 000300 and all boards of type matching **gpb** are removed from _group1_
    - br group2 - _group2_ is removed
    - br group1 !gpb - all boards are removed from the group _group1_ except those of type matching **gpb**

The brw command is similar to the br command except that the boards are identified by their SwAllocation and/or RncModule. Examples:

- - brw group3 dc - all boards whose SwAllocation matches **dc** will be removed from _group3_

The bp command is for printing existing groups or the contents of a particular group. Examples:

- - bp - all existing groups are shown, eg: _group1_ and _all_
    - bp all - the contents of the group _all_ is shown.

The be command is for extracting a number of boards from a group. To be used in conjunction with "mon" to handle board groups that contain more than 50 boards (the current limit on target monitor). Examples:

- - be10 partial_mod mod
    - be20 partial_dc dc
    - partial_mod_dc partial_mod partial_dc
    - mon partial_mod_dc

Once the group is created, the lh command is used to run an OSE command on all boards of the group. See help of the "lh" command in next chapter for more info.

It is also possible to run MO commands on board groups. In this case, the MO command will execute against the MOs connected to these boards, ie the **PlugInUnit** or Spm MOs.

**Examples:**

- - acc mod1 restart - restart the MP found in board group "mod1"
    - st mp view state of all MP PlugInUnits
    - acc cc1 restart restart the SPMs found in board group "cc1"

Note: in RNC, the bo command also creates a number of default MO groups ccXdev, dcXdev, pdrXdev, where X is the module number.

So, in order to lock/unlock some devices, use the MO group instead of the board group since the board group connects to the SPMs which don’t have an administrative state.

For example, bl cc1dev.

More info in h syntax.

**4.3.19 lh\[z\]\[x\] &lt;boardGroup&gt;|&lt;moGroup&gt; &lt;OSE-command&gt;|run &lt;commandfile&gt; \[ | &lt;unix-cmds&gt;\]**

Run COLI commands on all boards of a board group or MO group.

The first argument of the "lh" command is the board group or MO group.

- - Board groups are made by default after running the commands lh, bo, or bp. Type "bp" to see the list of board groups and "bp &lt;boardgroup&gt;" to see what boards are inside a group. The user can also define their own board groups with the command "ba". Type "h ba" for info.
    - MO groups are made with the commands "ma", "st", or "hget", type "h ma" and "h syntax" for info. If the MO group contains MOs of type PlugInUnit/Spm/PiuDevice then it can be used with the "lh" command.

The second argument is the COLI command or list of COLI commands. If several COLI commands will be run on the boards they can either be separated by semicolons or run from a commandfile stored on the workstation.

Option:

- - z: transfers the printout in gzipped format. Can save time on very large printouts. Only applies when the number of commands to send is greater than fast_lh_threshold. See more information further down.
    - x: run commands in reverse order of the boards’ hunt path. This means that Radio Units which are further away from the DU in the cascaded links will be run first. This is useful for instance when restarting boards, so the ones further away on the cascade will restart firt, eg lhx ru restart.

**Examples:**

- - lh group1 te log read
    - lh group1 te log read | grep ERROR:
    - lh all vii OR: all vii
    - lh all te log read | grep ERROR: OR: all err (special shortcut)
    - lhz all ps -w
    - lhx xp restart

It is possible to send multiple commands to each board of the board group by separating them with semicolons. Examples:

- - lh mp te log read ; llog -l ; te log clear ; llog -c
    - lh dc te e trace1 SP_HIST ; te log read

It is also possible to send a command file to each board of the group. Example:

- - lh spb run sp_traces.txt
    - lhz all ps -w; rld -a

When many commands are to be sent, the lh function will put them into a command file, transfer that file to the node (using (s)ftp) and run that file from within the node, using the shell -f command. This will save a lot of time instead of having to send each command one by one to the node.

There is a user variable called _fast_lh_threshold_ which decides the number of commands above which a command file will be transferred to the node. See Section 2.4 and **moshell** file for more info about user variables.

**4.3.20 mon\[?\]\[d\]\[u\]\[c\]\[f\]\[s\]\[t\]\[k\]\[a\]\[x\]\[e\]\[-\] \[&lt;board(s)|<boardGroup(s)&gt;\] \[&lt;/path/to/logfile&gt;\]**

Start/stop/check CPP target monitor or Linux monitor session in TCP mode, UDP mode, or disk mode.

The mon command issues a set of COLI commands (tm, or ts) in order to open TCP or UDP ports from the boards on the node to the client. The boards address and/or board groups are given as argument to specify which boards the client will connect to.

**Arguments:**

- - board(s)/boardgroup(s): the list of board or board groups to monitor. See examples below.
    - path to logfile: only applicable with option "u" (monu). The logfile must have the extension .pcap or .log. If the logfile has extension .pcap, then moshell/capture will be used as trace client. If the logfile has extension .log, then ltng-decoder will be used as trace client. Note that the path of ltng-decoder shall be specified in the uservariable ltedecoder.

**Cleanup:**

- - monc: to clean the files and folders used for MSRBS trace streaming. The command first lists the affected files and folders and space occupied, then asks if it is ok to proceed with deletion.

**Single Board Monitor (monx)**

Syntax: monx &lt;linkhandler&gt; \[&lt;logfile&gt;\] \[&lt;nr_lines_buffer&gt;\]

Example: Example: monx BXP_2048 /path/to/logfile.txt 10 -> trace streaming from board BXP_2048 , display on terminal as well as to file /path/to/logfile.txt which will be written to in blocks of 10 lines at a time.

This monitor works by doing repeated "te log read" on a board. It does not use any trace streaming functionality and therefore can work even when streaming ports are blocked in firewall.

It also works on RU/XMU/PIMCU connected to DUS Gen2 (which are currently not supported by the trace streaming monitors listed below).

The second argument is optional and can be used to log the output to a file.

**TCP Monitor for Linux nodes (EvoC8300, MSRBS):**

T&E Trace Streaming for Linux nodes is performed by using lttng-relayd (as server) and babeltrace/babelwrap (as client). By default, the mon command will use a lttng-relayd process on the current workstation unless a different workstation ip is specified in the uservariable lttng_dest. More info in the file moshell/moshell regarding this uservariable. The TCP ports 5342 (control) and 5343 (data) are used by default for transfer of traces from the node to the lttng server on the workstation. If those ports are occupied, then other consecutive ports will be automatically selected in the range up until 6342. The moshell uservariables lttng_port and lttng_range can be modified in order to change the starting TCP port and port range used for lttng trace streaming. The traces are flushed every 1 second for EvoC8300, and every 2 seconds for MSRBS. This can be changed via the uservariables lttng_flush_cpp / lttng_flush_rcs (value is in microseconds). The default buffer size is 4x4 MB for EvoC8300 and 4x1 MB for MSRBS. This can be changed via the uservariables lttng_buff_cpp or lttng_buff_rcs (value is in MB).

The tracefiles stored on the lttng-relayd server are rotated according to the settings in lttng_tracefilesize_rcs/cpp and lttng_tracefilecount_rcs/cpp.

The babeltrace client will by default connect to the IP address of the server where lttng-relayd is running. However if a firewall is blocking TCP connections to the workstation’s own IP then it is possible to set the uservariable lttng_localhost to 1 so that the babeltrace will connect to localhost instead.

Applicable options:

- mon? : to print the list of trace streaming sessions defined on the node
- mon\[s\] \[&lt;boards&gt;|&lt;boardgroup&gt;\] : to start a trace streaming session. If boards or board groups are not specified then the monitor is started on the core MPs only. Option "s" is for saving the streaming session so it will survive a board restart. With option "s", babelwrap is used as client instead of babeltrace as it has reconnect capability.
- mont\[s\] \[&lt;boards&gt;|&lt;boardgroup&gt;\] : to start a monitor session in tunnel mode, can be used in case the firewall is blocking the TCP ports for lttng. For option "s", see above. Note that this option is only supported if TCP port 22 is accessible to the node, this is not the case on commercial MSRBS nodes.
- monk : to kill all lttng-relayd and ssh port forwarding processes on the workstation (only those processes belonging to the current user and which were started by mon command will be affected).
- mon\[s\]- : to kill all active lttng sessions on the node. Option "s" is to also disable any saved streaming sessions.
- mon\[s\]k- : same as monk and mon\[s\]- combined
- mona\[s\] : to start trace streaming toward the ramdisk logs. Only applicable for Evo8300. Option "s" is for saving the session so it will survive restart.

**UDP Monitor for MSRBS (HiCap):**

On MSRBS, the TCP monitor can only be used for trace streaming of MP traces. Baseband traces are monitored via the UDP HiCap monitor which uses router (as server) and viewer/capture/ltng-decoder (as client). By default:

- moshell tries to start the trace router on the current workstation. It is possible to specify a different workstation by specifying its ip address in the uservariable bbte_router. But in that case the router process must be started manually on that workstation as it cannot be started remotely by moshell.
- buffered mode is used with bitrate of 200000 kb/s but this can be changed in the uservariable bbte_buffer_rate. In order to not used buffered mode, then set the uservariable bbte_buffer_rate to 0.
- the UDP port used for transfering the baseband traces from the node the router process is by default 33079. To use a different port, set the uservariable bbte_port.
- the dscp value is 0 and the mode is "normal" but these can be changed in the uservariables bbte_dscp and bbte_mode respectively. Type bbte log setdest for more details on those values.

Applicable options:

- monu\[c\] : start a HiCap trace monitor session on the O&M interface. With option c a client-server connectivity test is done prior to printing the monitor client command.
- monut : start a HiCap trace monitor session on the Traffic interface.
- monu\[k\]\[f\]- : stop a HiCap trace monitor session. Option "k" can be used to kill the user’s router process on the workstation. Option "kf" to kill the router process on the workstation even if it belongs to a different user.
- monu? : check whether the trace monitor is using buffered mode or not.
- monus/monue : start a HiCap trace streaming in silent mode (monus). start the export (monue) .
- monuz : to gzip the pcap trace files

Trace streaming client:

- if the path to a .pcap file has been specified as argument, then capture is used as client and the output will be saved to a .pcap file
- if the path to a .log file has been specified as argument, then ltng-decoder will be used as client and the output will be saved to a .log file
- otherwise the viewer or capture client will be used: $moncommand for the viewer client and $capcommand for the capture client.

Special settings for the capture client:

- bbte_dir : the path of the folder where the .pcap/.stats files will be stored by the capture client. Default: $logdir/sessionlog
- bbte_capture_duration : the value for the parameter --duration &lt;time&gt;, e.g. "10s". Default: empty.
- bbte_capture_size : the value for the parameter --size &lt;size&gt;, e.g. "260M". Default: empty.
- bbte_capture_rotate : the value for the parameter --rotate &lt;count&gt;, e.g. "2". Default: empty.

**Options for CPP (OSE) nodes:**

- mon?: print the target monitor status (TCP or UDP) and list of monitored boards.
- mon\[s\]: start the OSE target monitor in TCP mode. In TCP mode, only one session can be connected to a specific board and the "mon" command must be run before each time a new monitor client will be started. The TCP monitor client is "nc6" but it is possible to use "monitor6054" instead by setting the uservariable use_monitor6054 to 1. Option "s" is to save the target monitor configuration so the monitoring session will survive a board restart. Note: If the target monitor is already running on the node in UDP or DISK mode, then the existing mode is kept and the respective monitor client command will be shown.
- monu\[s\]: start the monitor in UDP mode with router/viewer or router/capture. By default router/viewer will be used, unless the path to .pcap logfile has been specified, in which case router/capture will be used instead, and the output will be saved in a pcap logfile instead of displayed on screen. In UDP mode, unlimited number of sessions can be connected to the same board(s). The "monu" command does not have to be run again if a handle is already open to the board(s) that will be monitored. Option "s" is to save the target monitor configuration so the monitoring session will survive a board restart. The uservariable udp_router allows to setup the monitoring session toward a trace router running in a different workstation rather than using one in the own workstation.
- monuk\[f\]: to kill the trace router process running on the own workstation. Only works if the router process is owned by the same user, unless option "f" ("force") is specified, in which case it can kill a router process owned by a different user.
- mond: start the monitor in UDP mode with dispatcher/monitor. Currently assumes the dispatcher is already running and

starts only the monitor. Currently only supported with dispatcher/monitor installed in AFS (/app/monitor/0/bin).

- monf\[s\]: start the monitor in DISK mode. The output will be saved locally on the hard disk of the node, the path will be shown in the monf printout. Option "s" is to save the target monitor configuration so the monitoring session will survive a board restart.
- mona\[s\]: start the monitor in RAMDISK mode. The output will be saved locally on the ram disk of the node, the path will be shown in the mona printout. Option "s" is to save the target monitor configuration so the monitoring session will survive a board restart. Note: RAMDISK monitor is only applicable for CBM3 based LTE targets (DUS, mRBS, ODS41)
- mont\[s\]: start the monitoring session in TLS mode
- mon\[s\]-: close all monitoring handles on the node. Option "s" is to also disable any saved monitoring sessions.

**Examples:**

- mon 000800 000900 : open a monitoring session in TCP mode to the boards 000800 and 000900
- mons coremp : open, and save, a monitoring session in TCP mode to the boards in board group "coremp"
- monu mod tu : open a monitoring session in UDP mode with router/viewer to the boards belonging to board groups "mod" and "tu"
- monu 000100 $logdir/board01.pcap : open a monitoring session in UDP mode with router/capture to the board 000100 and save to a file called board01.pcap
- mond mod tu : open a monitoring session in UDP mode with dispatcher/monitor to the boards belonging to board groups "mod" and "tu"
- monf mp et : open a monitoring session in DISK mode for all boards in the groups "mp" and "et"
- monas mp : open, and save, a monitoring session in RAMDISK mode on all boards in the group "mp".
- monts mp : start and save a monitoring session in TLS encrypted mode on all boards of the group "mp".
- mon- : close all active monitoring sessions
- mons- : close all active monitoring sessions and also remove any saved sessions.
- mon? : print monitor sessions

The command to start the monitor client is printed on the screen and also it is stored in the scripting variable $moncommand.

It is usually better to run the monitor client in a separate window than the moshell window but if this is not possible then it is also possible to run it from the moshell prompt, either in foreground or in background, eg:

- l $moncommand
- l $moncommand > $logdir/mylogfile &

The second method is especially useful when running moshell scripts. Then it is possible to put a wait statement while monitor is storing the traces in the logfile, then kill the monitor process using the command l kill -9 $background_pid, since the PID of the background process has been automatically stored in the variable $background_pid.

Notes:

- more information about the OSE target monitor: type "tm" from moshell prompt, or refer to the document 6/15518-CRX10201/1
- more information about the Linux trace monitor: type "ts" from moshell prompt.

**4.3.21 sql+/sql-/sql? \[&lt;heap&gt;\]**

Start/stop/check the SQL client on the node (CXC1325608).

This command checks if the SQL client LM is already loaded or started. If not, it finds the latest version stored on disk, loads it and starts it. The argument can be used to specify a different heap size than the one that is pre-compiled in the LM. The heap size given will be in MB, should be an integer between 1 and 300. If no heap is given, the LM is loaded without specifying any heap value which means that it will use the default heap size that is specified in the LM.

Warning: This command should be used for trouble-shooting purposes only. SQL commands must be entered with great care since they can cause a crash on the node when printing SQL tables that are very large.

**4.3.22 pgu\[c\]\[f\]\[r\] \[-p &lt;board1,board2,...&gt;\] /path/to/newLM \[&lt;cvcomment&gt;\]**

Program Upgrade. For lab use only, eg, to load black LMs.

**Arguments**

- the first argument specifies the location of the loadmodule on the workstation.
- the second argument (optional) is a text string that will be given as comment when making the PGU CV.

**Options**

- c: causes pgu to skip the CV and restart part. This is useful when many LMs need to be upgraded, avoids having heaps of CVs and restart.
- f: causes pgu to skip the confirmation questions.
- r: uses the same method as in system upgrade. A temp CV is made and old programs are removed after restart. Useful for core programs such as basic_OS.

### Switches

- \-p &lt;boardlist&gt;: Restrict the program upgrade to the specified boards

**Examples**

- pgu /home/userid/CXC132456_R1A02 - will update an LM that has a Program MO
- pgu /home/userid/CXC132789_R1B03.jar - will update an LM that is in the JVM classpath
- pgu /home/eric/blackLMs/CXP9010472%1-R4C98 - will update a RBS DSP container LM
- pgu /vobs/mmgw/r5/mgwr5_tc_mesc/build/mesc.ppc@@/main/llv21_corr/58 - the CXC number of this LM will be found automatically by pgu through the bswhat command
- pgu /home/userid/CXC12345678%2_R99A01 Black LM for HL12345 - will upgrade the program CXC12345678
- pgu -p 001200,001300 /home/userid/CXC1320787_P90A01 Black system manager - Will upgrade the program CXC1320787 only on boards 001200 and 001300, and include a CV comment.

The programs that are connected to an LM with the same product number will be identified and shown to the user. If the user confirms to go ahead, a loadmodule connected to the new LM will be created (if there isn’t already one on the node) and the programs using the old LM will be deleted and recreated towards the new LM. Then a cv is made and the user is prompted to restart the node so that the change will take effect.

**Options**

- c: causes pgu to skip the CV and restart part. This is useful when many LMs need to be upgraded, avoids having heaps of CVs and restart.
- f: causes pgu to skip the confirmation questions.
- r: uses the same method as in system upgrade. A temp CV is made and old programs are removed after restart. Useful for core programs such as basic_OS.

This procedure is "cleaner" than hacking the sql tables since it uses the MO interface.

This command is implemented as an moshell script, the script can be seen in **moshell/commonjars/scripts/pgu.mos**. This shows that the user can define any new commands they need by adding an alias in the .moshellrc which will point to a script file. The parameters to the command will be sent to the script file via the positional parameters $1, $2, $3, etc. The variable $0 will be set to the whole line contents. See Section 4.1.38 for info.

**4.3.23 procload/proctemp \[|&lt;unix-cmds&gt;\]**

Print processor load or temperature.

The procload command is a wrapper for the COLI command capi (capi tot and capi core all) The proctemp command is a wrapper for the COLI command boardtemp all or temprt It can be run on individual boards or board groups.

**Examples:**

- procload : Check processor load on the current board
- lhsh 001900 procload : Check processor load on another board
- lh mp procload : Check processor load on all boards of a board group
- lh all procload : Check processor load on all boards of the node
- lh allp proctemp : Check temperature on all boards of the node

The output of procload shows the total processor load of each processor in the board, followed by the processor load of the individual cores of each processor.

- Example output on a GPB75: 72.3 (76.8 68.1) The first number is the total load of the Main Processor, the next two numbers in brackets are the individual load of the two cores.
- Example output on a EPB1:

12.2 ( 6.2 11.9 7.1 17.0 5.5 28.0 9.4) 25.5 ( 3.3 29.3 36.6 24.7 26.9 28.1 29.6) The first

number is the total load of the primary Processor, then the individual load of the cores of that processor, then the total load of the secondary processor, then the individual load of the cores of that processor. Note: on EPB1, the load of the second core (ip bare metal) cannot be shown (it is usually 100

The output of proctemp shows the temperature displayed by each sensor of the board as well as the alarm limit for each sensor. The alarm limit for each sensor is displayed in brackets next to each sensor’s temperature. All temperature values are in Celcius.

**4.3.24 proglist/progkill \[-e\] \[&lt;string&gt;\] \[|&lt;unix-cmds&gt;\]**

List or restart programs on boards or board groups.

These two commands are wrappers for the COLI commands pglist/pm_pginfo and pgkill/pm_kill.

The proglist command lists the OSE programs running on MP, BP, or SP processor. The program handle, state, program number and name are shown. With option -e, the heap and pool size are also shown. It is also possible to add a filter after the -e option in order to show other program settings apart from the heap and pool. Eg: proglist -e stack shows all program settings matching the word stack. A list of all available program settings is shown at the end of the printout (when option -e is used).

The progkill command is used for restarting an individual program on a MP. If this command is used on a BP or SP then the whole processor restarts. A string which matches the program number or program name must be given as argument to the command. Eg: progkill java, or progkill 2844 **Examples:**

- proglist : List programs on central MP:
- lhsh 001400 proglist | grep 0787 : List programs on board 001400, whose product number match "0787"
- lh all proglist -e : List programs on all MP/BP/SP processors together with heap and pool info
- lh ommp proglist -e stack_size$ : Show the stack size for all programs running in the O&M MPs
- lh mp proglist | grep system : List programs on all boards of the boardgroup "mp", whose name match "system"
- lhsh 001400 progkill 2417 : Restart the program whose product number matches "2417" on board 001400
- lh mp progkill aal2ap : Restart the programs whose name matches "aal2ap" on all boards of the boardgroup "mp"

**4.3.25 fte &lt;te-command&gt; \[&lt;trace-groups&gt;|all\] \[&lt;string&gt;\] \[|&lt;unix-cmds&gt;\]**

Filtered te (trace and error) command.

This command is a wrapper for the COLI commands te or bbte and works in two ways:

- fte s \[all\] : to print trace status.

Without the option all, only the trace objects and processes that have additional trace conditions are shown.

With option all, all traces objects and processes are shown, even those whose trace conditions are default. To filter this printout, pipe it to grep.

- fte &lt;subcommand&gt; \[&lt;trace-groups&gt;|all\] \[&lt;string&gt;\]

Any te subcommand can be specified, e.g. e (enable), save, config, default, preset, etc.

The string is matched against all processes and trace objects in that board and a list of te commands are run against every matching process.

The pattern matching follows regular expression syntax and is non-case sensitive.

Note: In the case of DUS Gen2, the fte s printout may highlight certain trace conditions with asterisks in front (\*\*\*\*). This is to indicate the trace conditions which have been enabled in te but not in ts, meaning that the corresponding traces will then only be visible in te log read but not in a trace streaming session (mon). In order for those traces to appear in the trace streaming, they would need to be enabled with the command ts e 1 &lt;categories&gt; &lt;traceobject&gt;.

**Examples:**

- lh all fte s : List all non-default trace conditions in all boards of the node
- lh mp fte s all | grep -i ose : List all trace conditions in boards that belong to the board-group mp and pipe the output to grep lines matching the word ose
- lhsh 000800 fte e all dsp.\*meas : Enable all traces on processes and trace objects that match the string dsp.\*meas on board 000800
- lh mod fte config -run bus_send bus_receive rrc|nbap|ranap : Enable and save bus_send and bus_receive on trace objects and processes matching the string nbap|rrc|ranap on all boards of board group mod
- lh gcpu fte e all hspa : Enable all traces on MSRBS BB processors for trace objects whose name matches "hspa"

**4.3.26 goxb\[acib\] \[-p &lt;advpw&gt;\] &lt;commands&gt; \[|&lt;unix-cmds&gt;\]**

Run shell commands in XB boards (CMXB/SCXB/SMXB)

One or more XB commands can be run, each command to be separated by semicolons.

Syntax:

- lhsh &lt;board&gt; goxb\[acib\] \[-p &lt;advpw&gt;\] &lt;command&gt;\[;&lt;command&gt;;....\] \[ |&lt;unix-cmds&gt;\] or: • lh &lt;bdgroup&gt; goxb\[acib\] \[-p &lt;advpw&gt;\] &lt;command&gt;\[;&lt;command&gt;;....\] \[ |&lt;unix-cmds&gt;\]

**Options:**

- a : to run a command in the advanced user’s shell, eg "lh cmxb goxba listsw current"
- b : to run a command in the BCM shell, eg: "lh cmxb goxbb show counters"
- i : to run a command in the ISS/IMISH shell, eg "lh cmxb goxbi show interface status"
- c : to run a command in the C2 shell, eg "lh smxb goxbc help" (only applicable for SMXB)
- cb: to run a command in the C2 BCM shell, eg "lh smxb goxbcb show counters" (only applicable for SMXB)
- ci: to run a command in the C2 IMISH shell, eg: "lh smxb goxbci show interface status" (only applicable for SMXB)
- \-p &lt;password&gt;: to specify the advanced user’s password. Not needed if the board uses default password.
- without option: to run a command in the basic user’s shell, eg "lh cmxb goxb ls /tmp" (also works without goxb)

**Examples:**

- lhsh 000300 goxba listsw current
- lhsh 002600 goxbi show interfaces status; show mac-address-table
- lhsh 002800 goxbi sh version
- lhsh 002600 goxbb show counters
- lh xb goxba listsw current; find /bin -ls | grep CX
- lh cmxb goxbi show interface status; show mac-address-table
- lh smxb goxbci show apbf-access-list

Dependencies:

- goxb is a perl script requiring access to the perl module IO::Tty. The path to perl can be specified in the uservariable "perl". If the specified perl installation does not have IO::Tty then goxb will try to use the perl located in the decoder package (decoder/mini_local_perl). Make sure that the correct decoder path is given in the uservariable "decoder".
- if the perl module IO::Tty is not found in the specified perl installation, nor a correct path to decoder is found, then goxb will revert to using expect instead of perl. The path to the expect installation can be specified in the uservariable "expect".

**4.3.27 ftree\[f\]\[d\]\[1\] \[&lt;lnh&gt;/\]\[&lt;directory&gt;\] \[| &lt;unix-cmds&gt;\]**

Recursive listing of a directory on the file system of the node or the workstation.

This command first checks if the directory exists on the workstation and if yes, its contents is printed from the workstation.

Otherwise the command logs into the OSE shell of the node, checks if the directory exists on the node and prints its contents.

The directory can be entered either as a relative path or an absolute path.

To list a directory on a different board, enter the linkhandler of the board followed by the absolute path. If no directory is entered then the current working directory will be listed.

The option d is for printing the subdirectories only.

The option f is for printing files only. Mainly useful on /c/pmd for increased speed and sorting by timestamp.

The option 1 is for non-recursive listing of a folder, same as ls -l.

It is possible to pipe the output to a unix command for filtering/sorting purposes.

**Examples:**

1.  ftree /home/myuserid/moshell - list all files and directories from the local folder /home/myuserid/moshell on the workstation.
2.  ftree /c/loadmodules_norepl - list all files and directories from the folder /c/loadmodules_norepl on the node.
3.  ftree /c/loadmodules_norepl | grep xml - all files/directories matching **xml** are listed
4.  ftree 001900/f - all files and directories on the **/f** drive on board 001900 are listed
5.  ftreef /c/pmd - list all PMD files, sorted by date and time
6.  ftreed /var - list all the subdirectories under /var in the PRBS node

It is possible to run ftree on several boards by using the lh command. Example:

ba bp 0-9999 # put all boards in a group called "bp" br bp gpb # remove all gpb boards from the "bp" group lh bp ftree /f # recursive listing of the /f drive on all bp boards

**4.3.28 ftget\[1\]\[c\]/ftput\[1\]\[c\]/ftdel\[1\]\[a\]/ftrun \[&lt;options&gt;\] &lt;source&gt;\[/\*\] \[&lt;destination&gt;\]**

Transfer files or directories to/from the node, using ftp or sftp.

**Syntax:**

- ftput\[1\]\[c\] \[&lt;options&gt;\] localfile/localdir\[/\*\] \[remotefile/remotedir\]
- ftget\[1\]\[c\] \[&lt;options&gt;\] remotefile/remotedir\[/\*\] \[localfile/localdir\]
- ftdel\[1\]\[a\] \[&lt;options&gt;\] remotefile/remotedir
- ftrun &lt;commandfile&gt;

Where "local" refers to the workstation and "remote" refers to the CPP node.

It is possible to transfer a whole directory to/from the node by specifying a source directory instead of a source file.

A subdirectory with the same name as the source directory will then be created under the destination folder, unless a asterisk is specified at the end of the source folder, eg:

ftget /d/usr/\*

To fetch the contents of a folder located on a local volume of the node, the path must be preceded by the board address following by exclamation mark.

Eg: ftget 000900!/d/systemfiles

Note that in this case, only the files directly located under the folder will be collected and not the contents of the subfolders.

The ftdel command removes an individual file or a set of files/directories inside a directory. With "a" option, also the directory itself will be removed.

The ftrun command allows to execute a command file containing a list of ftget/ftput/ftdel commands. This is quicker than executing the commands via "run" as all commands will be run within the same ftp/sftp session.

**Options:**

- The c option in ftget/ftput stands for conditional and means that if the file(s) already exists on the workstation/node, they will not be overwritten.
- The a option in ftdel means that also the remote directory itself will be deleted. Otherwise only its contents will be deleted.
- The 1 option stands for non-recursive, meaning that only the files directly under the source folder will be transferred and not the files in any of the subfolders

The options can be placed anywhere on the comand line but the source must be given before the destination.

If the destination is omitted then the current working directory is chosen.

**Filtering option:**

The -f option allows to specify a regular expression to only transfer the files matching that expression. See examples below.

Exclamation mark ! can be used as negative filter, meaning that any files that do NOT match the filter will be transferred, eg. ftget -f !tmp /c/usr

**Time options:**

The -s and -e options are used for specifying an absolute timespan: -s gives the starting date and -e gives the ending date. The format is yyyymmdd\[.hhmm\], for instance 20071230, or 20071230.0800.

The -m and -p options are used for specifying a timespan relative to today’s date: -m gives how long time backward and -p gives how long time forward. The format is in days, hours, or minutes, eg. 10d (10 days), 2h (2 hours), 30m (30 minutes).

**Examples:**

- ftget /c/logfiles - fetch the folder /c/logfiles and all of its contents and store it in the current working directory on the workstation
- ftget /c/logfiles /home/eric - fetch the folder /c/logfiles and all of its contents and store it in the folder /home/eric on the workstation
- ftputc /home/eric/rnc10/configuration/cv/cv-10 /d/configuration/cv - put the folder cv-10 from the workstation to the node, files that already exist on the node will not be overwritten (conditional transfer)
- ftget -f A.\*xml.gz -m 3h /c/pm_data /home/eric/rnc10 - download files from the folder /c/pm_data whose path matches the string A.\*xml.gz and whose timestamp is from the last 3 hours.
- ftget -f !(.xml.gz|.bin)$ /c /home/eric/backup - download all files from the folder /c except those whose path match .xml.gz or .bin
- ftget /c/loadmodules_norepl /home/eric/rnc10 -f (xml|jar)$ - fetch all files matching who have the extension xml or jar from the folder /c/loadmodules_norepl and any of its subfolders.
- ftdel /c/pm_data -f .tmp$ -m 900 -p 870 - delete files with the extension .tmp in the folder /c/pm_data , with timestamp older than 30 days.
- ftput /home/eric/backup/\* /d/loadmodules - transfer all the files and folders under /home/eric/backup to /d/loadmodules without making the folder called "backup"
- ftget 000900!/d/systemfiles /home/eric/rnc10 - transfer the contents of the local volume /d/systemfiles from board 000900 to /home/eric/rnc10

**Notes:**

- By running ftput/ftget from **mobatch**, it is possible to get/put files to/from many nodes in parallel.
- Only active mode is supported for unsecure ftp. If active mode is not allowed by the firewall, then use _secure_ftp_ instead (see Section **??** for info about _secure_shell_/_secure_ftp_).
- By default, the original file timestamps and permissions are NOT preserved after transfer. In order to preserve them, it is necessary to set uv ftp_preserveprops to 1 (get), 2 (put), or 3 (get and put).

**4.3.29 htget &lt;remotefile&gt; \[&lt;localfile/localdir&gt;\]**

Download files using http or https.

This command allows to download a file to the workstation using http or https. Whether http or https will be used is decided from the uservariable secure_http (0=http, 1=https).

The _remotefile_ can be specified with or without ipaddress.

If no ipaddress is specified then the file is fetched from the current node. If an ipaddress is specified the file can be fetched from a different server. It is also possible to specify the tcp port after the ip address eg &lt;ipaddress&gt;:&lt;port&gt; The prefix http:// or https:// is optional.

**Examples:**

- htget /cello/oe/xml/rnc_node_mim.xml - file will be transfered to ./rnc_node_mim.xml
- htget 10.1.128.17/cello/oe/xml/rnc_node_mim.xml ~/rnc_mom.xml - file will be transfered to /rnc_mom.xml
- htget http://10.1.128.17/cello/oe/xml/rnc_node_mim.xml /home/eratoto- file will be transfered to /home/eratoto/rnc_node_mim.xml
- htget http://10.68.110.44:8080/em/index.html
- htget https://10.68.110.44:443/em/index.html

**4.3.30 edit &lt;remotefile&gt;**

Edit a file on the node.

Moshell will download the file, spawn the text editor allowing to edit it and then upload it once the text editor is closed. If the file does not exist on the node it will be created.

The editor is specified in the editor user variable. By default, editor is set to the bash environment variable $EDITOR. If $EDITOR is not set, then vi will be used. To use another editor, add the following line in the ~/.moshellrc file:

editor=/path/to/your/favorite/editor

**4.3.31 fclean\[f|ff|a|d|e\] \[&lt;lnh&gt;/\]\[&lt;directory&gt;\] \[-f &lt;filename-filter&gt;\]**

Removal of obsolete loadmodules OR recursive removal of a directory on the node.

1.  Remove a directory (equivalent to "rm -Rf" in unix). Syntax:
    - fclean &lt;directory&gt; to remove all contents in the directory but not the directory itself
    - fclean &lt;directory&gt; -f &lt;filename-filter&gt; to remove part of the directory, ie, only files whose name matches the filter
    - fcleana &lt;directory&gt; to remove all contents in the directory as well as the directory itself
    - fcleand &lt;directory&gt; to remove all empty folders in the directory. Useful to clean up the /c/pmd and /c/loadmodules_norepl which often contain a number of empty directories.
    - fcleane &lt;directory&gt; to empty all files in the directory (files are replaced with an empty file). This is mainly intended to clear the logfiles in /c/logfiles. For STP use only !

Note: The "d" and "e" options cannot be used together !

1.  Examples (all files in that directory will get removed (after confirmation from the user):
    - fclean /c/pmd
    - fclean /c/pmd -f 0x00
    - fclean /p001200/pm
    - fclean 001900/f
2.  All empty folders in those directories will get removed (after confirmation from the user).
    - fcleand /c/loadmodules_norepl
    - fcleand /c/pmd
3.  All files in that directory are removed and replaced with empty files.
    - fcleane /c/logfiles
4.  Deleting loadmodules that are not in use by the system. Examples:
    - fclean
    - fcleanf
    - fcleanff

This means any loadmodules that are present on the disk but are not defined in the current cv (_ARMAMENT_ file and database) nor are listed in any of the existing upgrade packages on the node.

The directories which are "cleaned up" are:

- - on the central MP:
    
    1.  **/c/loadmodules**
    2.  **/c/loadmodules_norepl**
    3.  **/c/java**
    4.  **/c/dsp_load_files**
    5.  **/c/fpga_load_files**, • on all MPs: **/d/loadmodules**
- on all BPs:
    1.  **/f/loadmodules**
    2.  **/f/satloadmodules**
    3.  **/f/dsp_load_files**
    4.  **/f/fpga_load_files**
    5.  **/f/dp_loadmodules**

It is possible to specify a list of loadmodules that are not to be cleaned up in the variable _keepLmList_ in the **moshell** file. When the command has completed, a command file containing all remove commands is generated and the user is prompted with the choice to run it at once or at a later time.

**Options:**

- f : to clean the **/f** drives. Only files that are in use by the current cv will be left on the **/f** drives.
- ff: to remove all loadmodules from the **/f** drives, including those that are in use by the current cv. This will force the device boards to refetch their software from the **/c/loadmodules** directory.

Note: the fclean command will also clean up the **/f** drives but will leave all loadmodules that are specified in other upgrade packages as well as the current one. So the cleanup is not as drastic with **fclean** as with **fcleanf** or **fcleanff**.

**4.3.32 hi \[&lt;commandFilter&gt;\], !&lt;commandNr&gt;**

Print history of moshell commands entered during the current session.

By using the filter, it will only show those command matching that pattern. Example:

moshell> hi

1.  lt e1
2.  st all dis
3.  get 4 oper

To rerun e.g. command number 2, do:

!2

**4.3.33 time\[t\] &lt;command&gt;|&lt;logfile&gt;**

Measure time taken by an moshell command or by each command in a moshell command file.

**Arguments:**

- - &lt;command&gt; : the command is executed and its duration, in seconds, is shown on the last line of the printout. The duration is also saved in a moshell scripting variable called $duration. If the "t" option was specified ("timet" command), the duration is also saved in a hashtable called $durationtable, where the index is the command executed.
    - &lt;logfile&gt; : the logfile is parsed by the time function and the duration of each command contained in this log is displayed as output. The logfile can be in gzipped format.

Example:

- - time get all - Measure the time taken by the "get all" command
    - timet lh all te log read - Measure the time taken by the "lh all te log read" command and save it in a hashtable
    - time /path/to/NODE_dcg_m.log.gz - Show the duration of each command contained in the logfile of the "dcg" command:

**4.3.34 pipe &lt;command&gt; | &lt;unix-command&gt;**

Execute a moshell command and pipe the output to a unix command.

This is useful for commands that don’t natively support direct piping, such as "mom", "h", "inv", etc It is not needed for commands that natively support direct piping, such as "lg", "pmx", "lh", etc

Example:

- - pipe mom . . | less : Run the "mom" command on all MO/attributes and pipe to "less"

pipe h lg | less : Read the help of "lg" and pipe to "less"

- - pipe get ^eutrancellfdd= ^cellid$ | sort -nk 3 : Read the cellId attribute on all cells and sort by order of ascending cellId

**4.3.35 lmid\[c\]\[h\]/upid\[om\] &lt;pattern&gt;|refresh**

Print translation of loadmodule/upgradepackage product number or T&E error codes.

**Examples:**

- - lmid 2517 - to lookup the name of any LM whose product number matches 2517
    - upid 2014 - to lookup the release and cpp version of the UP whose product number matches 2014
    - lmid aal2 - to lookup the product number(s) of any LM(s) whose name matches aal2

In addition, the LM name is printed beside the product number when using certain OSE shell commands:

- - ls, pglist and ps for uservariable _print_lmid=1_
    - same as above, plus te log read for uservariable _print_lmid=2_

For instance, when printing the contents of a directory such as **/d/loadmodules** or **/c/loadmodules_norepl**, the LM name will appear next to the product number. This functionality can be disabled by setting the user variable _print_lmid_ to 0.

See Section 2.4 and Section **??** for more info about user variables.

If some names are missing from the printout, just run lmid refresh or bo and it will update the moshell LM reference file with all missing LM names. The refresh also happens automatically if no LM name is found for the pattern given.

The "c" option in lmid is to print the error codes list (aal2/mtp3/sccp/utrancell) which is used to decode error codes from the "te log read".

The "h" option in lmid is to print the HW translation table.

The "m" option in upid is to print the CXP to MOM version table.

The "o" option in upid is to print an overview, mapping of major SW releases only.

**4.3.36 p/w/pw/b**

Change moshell prompt and/or window title.

**Examples:**

- - p &lt;newPrompt&gt; - to change the prompt. Can also be changed before startup with the uservariable prompt, eg moshell -v prompt=xxx &lt;node&gt;. The prompt can contain a carriage return, use the \\n sign, eg moshell -v prompt=’moshell\\nNode’ , or p moshell\\nNode
    - w &lt;newWindowTitle&gt; - to change the window title
    - pw &lt;newText&gt; - to change the prompt and window title
    - b - to make the prompt bold or unbold. When the prompt is in bold, command lines that are longer than the screen width do not wrap correctly.

**4.3.37 prox\[+-\]**

Toggle display of proxy identities in printout of get &lt;mo&gt; &lt;attribute&gt; command.

To print the proxy identities, type prox and the proxys will be printed for the remaining of the session. By typing prox one more time, the proxys will not be printed anymore.

**Options:**

- - \+ : activate the feature, proxy identities will be printed at the beginning of the line (get_format=1)
    - \- : return the feature to its original value, proxy identities will not be printed (get_format=0)

The default behaviour is to not show the proxy identities (get_format=0) To change the default behaviour, it is possible to use the uservariable get_format, eg, adding the line get_format=1 in the file /.moshellrc.

- - 1.  **col**

Toggle display of colors.

By default, some lines will appear in different color in the te log read and cabrd printouts.

To disable the coloring, type col once; to reenable it, type col again.

This setting can be saved permanently in the uservariable show_colors.

- - 1.  **ul**

Toggle display of _userLabel_ in st/lst and pget/lpget printouts.

By default, the _userLabel_ is not shown.

Type ul to display this information for the remaining of the session. Type ul again to hide it.

This setting can be saved permanently in the uservariable show_userlabel.

- - 1.  **conf\[bld\]\[+-\]**

Toggle confirmation on various MO commands.

- - confb - bl/deb.set/acc commands
    - confl - lt/lc commands
    - confbl - both type of commands
    - confd - del/rdel commands

By default, these commands require confirmation (y/n). Type one of these commands to disable confirmation. Type the command again and confirmation is re-enabled.

These settings can be saved permanently in the uservariables bldebset_confirmation, lt_confirmation, del_confirmation.

**Options:**

- - \+ : disable confirmation, instead of toggling it (sets the uservariable to 0)
    - \- : return confirmation to its previous value.

**4.3.41 gs\[+-\]/gsg\[+-\]**

Toggle display of old/new attribute value in setbldeb commands.

Purpose:

- - gs - old value is displayed before setting the attribute. Ie, a get is performed before the set.
    - gsg - old value is displayed before setting the attribute, then new value is displayed after setting the attribute. Ie, a get is performed before and after the set.

Notes:

- - The set will not take place if the new value is the same as the old value. The result **\-No Change-** is printed.
    - If the set is accepted (no exception given) but the final value is still the same as the old value, then the result **»> Fail** is printed.
    - These toggles don’t affect setting attributes whose value take up several lines such as _Array of MoRef_ and _Struct_.

**Options:**

- - \+ : activate the feature, instead of toggling it.
    - \- : return the feature to its previous value.

These settings can be saved permanently in the uservariable gs_gsg:

- - gs_gsg=0 : gs and gsg both disabled
    - gs_gsg=1 : gs enabled and gsg disabled

gs_gsg=2 : gs disabled and gsg enabled

**4.3.42 ip2d &lt;ip-address&gt;**

Convert an IP address to a decimal number.

This can be used for instance when editing an entry in the ip fro table in the sql database, where ip addresses are stored in decimal format.

Example:

- - ip2d 10.1.2.3 —> would print: 10.1.2.3: -4127129085

Similar to the get command, it is possible to store the output of this command into a variable. Example:

- - ip2d 10.1.2.3 > $ip_db —> stores -4127129085 into variable $ip_db

**4.3.43 d2ip/h2ip &lt;number&gt;**

Convert a decimal or hexadecimal number to an IP address.

This can be used for instance when decoding T&E traces or COLI printouts where ip addresses are written in decimal or hexadecimal format.

**Examples:**

$ lhsh 001400 drh_trbr_data iphost ipHostFroId admState opState availStatus piuId smn apn ern atmPortId ipAddress linkHandlerName msgBoard

7 1 1 0 7 0 7 0 29 0xa641002 000700 hostReady applSciRunning

$ lhsh 000200 te log read

\[06:52:40.228\] Ipet_app3dr_proc(IPET_APP3DR_SH_OBJ) app3dr_sh.c:5692 REC SIG:signo:190071 sender :100dc Rec: IPET_IPPSI_UDPSESSIONSETUP_IND. Ipet_remoteIpAddress = 174329861

- h2ip 0xa641002 –> will print: 0xa641002: 10.100.16.2
- d2ip 174329861 –> will print: 174329861: 10.100.16.5

Similar to the get command, it is possible to store the output of this command into a variable. Example:

- d2ip 174329861 > $ip —> stores 10.100.16.5 into variable $ip
- h2ip 0xa641002 > $ip —> stores 10.100.16.2 into variable $ip

**4.3.44 h2d/d2h &lt;number&gt;**

Convert an integer to hexadecimal or viceversa.

Example:

- d2h 10 would return 0xA
- h2d a would return 10
- h2d 0xa would also return 10

Similar to the get command, it is possible to store the output of this command into a variable. Example:

- d2h 10 > $var - stores 0xA into variable $var
- h2d a > $var - stores 10 into variable $var

**4.3.45 h2b/b2h &lt;number&gt;**

Convert a binary to hexadecimal or viceversa.

Example:

- b2h 101011 would return 2B
- h2b a would return 1010
- h2d 0xa would also return 1010

Similar to the get command, it is possible to store the output of this command into a variable. Example:

- b2h 10100011 > $var stores the value "A3" into variable $var

h2b a > $var stores 1010 into variable $var

**4.3.46 d2b/b2d &lt;number&gt;**

Convert a binary to decimal or viceversa.

Example:

- b2d 101011 - would return 43
- d2b 45 - would return 00101101

Similar to the get command, it is possible to store the output of this command into a variable Example:

- b2d 10100011 > $var - stores the value "163" into variable $var
- d2b 10 > $var - stores 1010 into variable $var

**4.3.47 rb2ip \[&lt;iublink&gt;\]**

Print the mapping of RNC IubLink MOs to RBS O&M IP addresses. Only supported in OSSRC.

Example:

- rb2ip print the RBS O&M IP addresses for all IubLinks in the RNC
- rb2ip Iub-14 print the RBS O&M IP address for IubLink=Iub-14

Similar to the get command, it is possible to store the output of this command into a variable Example:

- rb2ip Iub-14 > $var stores the RBS O&M IP address of IubLink=Iub-14 to the variable $var

**4.3.48 z2f \[&lt;zipfile&gt;\]**

Convert a Evo8300 T&E ramdisk zipfile to a text file.

The Evo8300 T&E ramdisk logs (located on the node at /tsRamdisk/Snapshots) shall first be collected with the command lg2. See examples below and check also the help of the command h lg.

- lg2 - collect all CPP T&E disk/ramdisk logs
- lg2 -b mp -m 3h - collect all CPP T&E disk/ramdisk logs of the last 3 hours from board group "mp"

The lg2 command produces a zipfile whose path will be shown at the end of the lg2 execution. To convert this zipfile into a readable T&E text file, run the command: z2f /path/to/zipfile

**4.3.49 encpw\[f\]**

Create an encoded password or encrypt a .mos or .xml command file.

**Syntax 1:** encpw \[&lt;password&gt;\]

To create an encoded password.

The command can be run on its own, without argument, in which case it will prompt for the password to encode.

Or the password can be specified on the command line as argument.

The command will return an encoded string that can be used as password for input into moshell uservariables or commands. Encoded passwords can be used in moshellrc, ipdatabase files, scripts, on the command line and as input to MO operations.

Example:

- encpw SecretSLSPassword Prints: ENC@:U2FsdGVkX1+r/ult+DVXg5vLcc34ZSv5uKKfFXUovE7j9A==

Similar to the get command, it is possible to store the output of this command into a variable Example: encpw mypassword > $pw

Encoding prefix:

- if the uservariable encpw_type is set to 1 (default, supported from moshell 21J), then the encoded passwords will be prefixed by "ENC@:"

if the uservariable encpw_type is set to 0 (legacy), then the encoded passwords will be prefixed by "ENC?:"

Make sure to keep this prefix when using the encoded password.

**Syntax 2: encpwf &lt;file&gt; \[&lt;password&gt;\]**

To encrypt a .mos or .xml command file.

The path of the command file to encrypt shall be given in the first argument.

If the second argument is not specified then the password to be used for encrypting the file will be prompted on the next line. The encrypted command file can be executed as usual from the "run" command (.mos file) or "netconf" command (.xml file). The only difference is that the file password will be prompted in order to be able to decrypt the file.

It is also possible to store the file password in the uservariable file_password in moshellrc to avoid having to enter it at the prompt. This is useful for running an encrypted command file via mobatch for instance.

Example:

- encpwf /path/to/file.mos - creates a encrypted file file.mos.enc
- run /path/to/file.mos.enc -> execute the encrypted command file with the run command
- encpwf /path/to/netconf_commands.xml -> creates a encrypted netconf file netconf_commands.xml.enc
- netconf /path/to/netconf_commands.xml.enc -> execute the encrypted netconf file with the netconf command

**4.3.50 mos2ro &lt;moshell.zip&gt; \[/path/to/destinationfolder/\]**

Generate an installation package for moshell read-only version.

Example:

- mos2ro /home/userid/moshell10.0v.zip - generate a file called moshellreadonly10.0v.zip which can be used to install a read-only version of moshell

The following operations are blocked in the read-only version: MO and Scanner create/delete/set/action. Also certain commands such as mon, fro, sql, pgu.

Arguments:

- /path/to/moshellxxx.zip : the path to the moshell installation package from which the moshellreadonly installation package will be generated.
- /path/to/destinationfolder : the path of the folder where the moshellreadonly package will be stored. If this argument is not specified, the readonly package will be stored in the moshell session’s temporary folder.

Example:

- mos2ro /home/userid/moshell20.0c.zip /home/userid/ : generate a file called moshellreadonly20.0c.zip and store it under /home/userid

**4.3.51 gpg &lt;file&gt;**

Decrypt a gpg-encrypted ESI/DDB or PMD file, standalone or contained in a zip/tgz archive.

**Example:**

- gpg ~/ENB34_170516_012256_AEST_MSRBS-L_CXP9024418-6_R12A164_dcgm.zip - the ESI file inside the dcgm.zip will be decrypted and the dcgm.zip containing the decrypted ESI will be renamed to xxx_esidec_dcgm.zip
- gpg ~/ENB34_logfiles.zip - the ESI file inside the logfiles.zip will be decrypted and the logfiles.zip containing the decrypted ESI will be renamed to xxx_esidec_logfiles.zip
- gpg ~/esi.du1.20170515T152801+0000.tar.gz.gpg - the gpg-encrypted ESI file will be decrypted and stored in the same folder as the encrypted ESI file
- gpg ~/pmd-cliss-28849-20161117-062032.tgz.gpg_with_llog.tgz - the gpg-encrypted PMD file will be extracted from the tgz file and stored in the same folder as the tgz file

**Note:**

This command is for Ericsson personnel only. IDM role "CSDP ESI Decrypter" is needed.

The gpg-encrypted file is decrypted on a remote CSDP server, accessible only from Ericsson Corporate Network with a Ericsson Corporate login.

The Ericsson Corporate login for the CSDP server can be saved in the uservariables csdp_username and csdp_password.

If the CSDP server is not reachable directly but only via a https proxy then it is possible to set the environment variable https_proxy in the unix shell to allow successful https transfer by the gpg command. Example in the .bashrc file , add a line like: export https_proxy=http-proxy.sero.gic.ericsson.se:8080

Note: The gpg command will retry decryption up to 5 times in case of failure. The number of retries can be configured in the uservariable gpg_retry.

**4.3.52 enm &lt;command&gt;**

Run a ENM-CLI command ("cmedit" or "alarm") or a ENM-CLI command file.

For more info on available commands and syntax, please refer to the ENM-CLI documentation https://cpistore.internal.ericsson.com/elex?LI=EN/LZN7030220R2CY&FN=1_1553-CNA4032979Uen.CV.html

Examples:

- enm alarm get \* -cri -maj -min -war -> show all active alarms in the whole network
- enm cmedit get \* NetworkElement -> list all connected nodes
- enm cmedit get \* MeContext.\* -t -> show MeContext data for all connected nodes
- enm cmedit get &lt;nodename&gt; ManagedElement.\* -> show the ManagedElement attributes for a given node
- enm cmedit get \* EUtranCellFDD.(operationalState,administrativeState) -t -> show state all EUtranCellFDD MOs in the whole network
- enm cmedit get \* EUtranCellFDD.(operationalState==DISABLED,administrativeState) -t -> show state of all disabled EUtranCellFDD MOs in the whole network
- enm run /path/to/commandfile.txt -> run a commandfile containing cmedit and/or alarm commands

Restrictions:

- the "enm" command is blocked from running from mobatch
- only "cmedit" and/or "alarm" commands are allowed
- the "cmedit" subcommands import/export/blacklist are blocked

**4.3.53 wait &lt;delay&gt;|&lt;newtime&gt;**

Wait for a specific duration in hrs, mins, secs, rops, or until specified time.

Default duration is in seconds. Use "u" for microseconds, "m" for minutes, "h" for hours and "r" for ROPs. Default ROP duration is 15 minutes but can be changed with the uv rop_period (eg: to change rop duration to 5 minutes, type uv rop_period=5) **Examples:**

- wait 2 - wait 2 seconds
- wait 90 - wait 90 seconds
- wait 500000u - wait 500,000 microseconds
- wait 3m - wait 3 minutes
- wait 4h - wait 4 hours
- wait 5r - wait 5 ROP periods
- wait 5r-60 - wait 5 ROP periods minus 60 seconds (the prompt will return 60 seconds before the end of the five ROPs)
- wait 16:30 - wait until 16:30
- wait 9:45:30 - wait until 9:45:30
- wait 20130728.094530 - wait until 2013-07-28 at 09:45:30
- wait 2013-07-28.09:45:30 - same as above

If a ROP period is already started, it will wait until it finishes, then wait additionally the number of ROP periods specified.

To wait only until the current ROP is finished, use the command "wait 0r"

If the new time is before the current time (e.g. if current time is 9:30 and new time is 8:00), then the waiting will continue to the next day at that time.

Note: the new time shall be given in same time zone as the workstation where moshell is running.

To abort a wait statement, just type CTRL-C

**4.3.54 wf\[o\]\[a\]\[t\] &lt;file&gt;**

Write lines to a file.

Argument: the path to the file to be written to **Options:**

- o : if file already exists it will be overwritten
- a : if file already exists, the line will be appended to the end of the file
- t : translate scripting variables before writing to the file Without options, the command will abort if the file already exists.

Example:

- the file $tempdir/myfile.txt will be created and all the subsequent lines will be written to that file until the line "eof" or "EOF" (as in "End Of File") is reached

wf $tempdir/myfile.txt

EUtranCellFDD administrativeState 0

EUtranCellTDD operationalState 1 EOF

**4.3.55 return**

To exit from a command file without exiting from MoShell (scripting).

Typically, the return command would be executed upon validation of a specific condition in the command file.

Note that the return cannot be put in a for loop, only in a if(/else) that is not contained in a for loop.

In order to use it in for loop, the break command has to be used in order to get out of the for loop, first.

In this example, we run a restart followed by running a trun script, 60 times.

If the trun script fails then we set the $return variable to 1 and break from the loop (note: the $command_result is a default variable which gets automatically set after running trun, see Section 6)

After the loop, there is a check to see if $return is 1, if yes, then "test failed" is printed, the commandfile is aborted and we are returned to the moshell prompt.

If $return was not set to 1, then it means we have completed all 60 iterations successfully and the final part of the script will be executed.

for 60 $return = 0 facc 0 manualrestart 0 0 0

trun $moshelldir/cmdfiles/rnc_commands.mos if $command_result = 1

$return = 1 break fi done

if $return = 1 l echo "TEST FAILED" return fi l echo "TEST OK"

Another example of using the return command can be found in Section 6.5

**4.3.56 print**

To print a line or variable (scripting).

Handy when doing scripting to see what values will be substituted to a variable.

**Examples:**

print $var print $table\[$var\]

**4.3.57 alias\[f\]/unalias &lt;alias&gt; &lt;command&gt;**

Print or define command aliases.

Options:

- f : to create a multi-command alias. The commands shall be written on one line, separated with semicolons.

Example:

- alias ter te log read - to create an alias with the name "ter" which runs the command "te log read"
- aliasf test lt all;st cell;al -> to create an alias that will run these 3 commands, the option "f" is needed so that the commands will be put in a file and executed with run

Type alias on its own to list all defined aliases.

Use command "unalias" to undefine aliases. Example:

- unalias ter - to undefine the alias called "ter"
- unalias all - to undefine all aliases

Aliases can be stored permanently in the **~/.moshellrc** file, using the same syntax as above.

Note: moshell commands take precedence over aliases. This means that if an alias has the same name as an moshell command, the moshell command will be executed instead of the alias.

**4.3.58 lf\[c\] &lt;file&gt;**

Load a moshellrc file or a offline COLI file.

**Examples:**

- lf /home/eraaldr/tools/moshell/jarxml/moshellrc - Load a moshellrc file
- lfc /home/moshell/moshell_logfiles/logs_moshell/dcg/RNC12/140101_1453/RNC12_dcg_m.log.gz Load a offline COLI file (only applicable in offline mode)

Note: The lf command can be run from the moshell prompt or called from within a moshellrc file in order to source additional moshellrc files.

**4.3.59 bg\[g\]/bgs/bgw \[&lt;commands&gt;|&lt;id(s)&gt;|all\] \[&lt;maxtime&gt;\]**

Run some moshell commands in background or check status of background jobs.

Syntax:

- bg\[g\] &lt;commands&gt; : to execute some moshell commands in background. The "g" option is to gzip the log upon completion.
- bgs : check the status of all background jobs.
- bgw \[&lt;id(s)&gt;|all\] \[&lt;maxtime&gt;\] : wait for one, several, or all jobs to complete. Specifying maxtime (in seconds) will lead to stop waiting after a job has been running for longer than that amount of time.

The following variables and arrays keep track of the list of background jobs and their properties:

- $bg_id : the job id
- $bg_pid\[id\] : the PID of the moshell process corresponding to each background job
- $bg_status\[id\] : the status of each background job, RUNNING or FINISHED
- $bg_log\[id\] : the path of the logfile containing the printout of each background job
- $bg_runtime\[id\] : the current duration in seconds of each job

**Examples:**

- bg dcgm - Run some moshell commands in background
- bgg cabx;al;str - Run some moshell commands in background and gzip the logfile upon completion
- bg l+ $logdir/$ipaddress_kget.log ; lt all ; kget ; l- - Run some moshell commands in background using a user defined logfile
- bgs - Check status of background jobs
- bgw 2 - Wait for job number 2 to complete
- bgw 2,3,5 - Wait for jobs number 2, 3, and 5 to complete
- bgw - Wait for all jobs to complete
- bgw all 1800 - Wait for all jobs to complete but stop waiting if the running time of a job exceeds 1800 seconds (30 mins)

**4.3.60 - smd\[slcr\] \[-m &lt;days&gt;\] \[-s &lt;size&gt;\] \[-f &lt;filter&gt;\] \[-o a|s|n\] \[-u &lt;user&gt;|all\] \[-d &lt;directory&gt;\] \[-n &lt;max&gt;\]**

Server Maintenance - disk usage

**Options:**

- l: list files
- r: remove files
- c: compress files (using gzip)

**Switches:**

- \-d &lt;directory&gt;: the directory to process. Default: $logdir.
- \-u &lt;user&gt;|all : the user who owns the file. Default: if running as root, all users - otherwise, the current user.
- \-n &lt;max&gt; : max number of files to list (eg: -n 30). Default=20.
- \-m &lt;days&gt; : minimum age of the files in days (eg: -m 10 ==> all files which were modified 10 days ago or more).

Default=1.

- \-s &lt;size&gt; : minimum file size in B/K/M/T/G (eg: -s 100B ==> all files of size at least 100 Bytes). Default=0.
- \-f &lt;name&gt; : file name filter (eg: -f A.\*.xml.gz ==> all files whose name file path A.\*.xml.gz).
- \-o \[a|s|n\] : printout order (eg: -o a ==> sort files/processes by age, -o s ==> sort by size, -o n ==> sort by name).

Default=s

Examples - diagnostics with smd:

- smds -n 15 : show disk usage summary of the log folder, max 15 largest files/directories displayed (default: 20)
- smds -d /home/user/moshell : show disk usage of the folder /home/user/moshell (default: the folder /home/user/moshell_logfiles)
- smd -d /var/opt/ericsson : show disk usage of the folder /var/opt/ericsson (default in amos: the folder /var/opt/ericsson/amos/moshell_logfiles)
- smdl -m 30 -s 1M -f /logs_mobatch/.\*\\.log$ -o a : show files of size at least 1M, aged at least 30 days, files located in logs_mobatch folder and file name ends with .log, sort printout by file age.
- smdl -d /home/user/moshell_logfiles/logs_mobatch -m 10 -s 1M -o s : show files in

/home/user/moshell_logfiles/logs_mobatch, aged at least 10 days, size at least 1M, sort printout by file size

Examples - cleanup with smd:

- smdr -m 30 -f /A.\*.xml.gz$ : remove files in moshell_logfiles, aged at least 30 days, with file name matching

A.\*.xml.gz

- smdr -m 30 -n \_ropfiles.zip$ : remove files in moshell_logfiles, aged at least 30 days, with file name matching \_ropfiles.zip
- smdc -m 30 -o n : compress logfiles aged at least 30 days, show file list sorted by filename (note: files already in compressed format will not be affected)
- smdr -m 7 -f logs_moshell/(tempfiles|cache)/ : remove all the moshell tempfiles older than 7 days

Examples - cleanup with cronjobs:

Example of some cronjobs to remove ropfiles older than 30 days and compress logfiles older than 30 days (contents of "crontab -e" is shown). In this example the jobs are performed every saturday at 1:00 am.

\# minute (0-59),

\# | hour (0-23),

\# | | day of the month (1-31),

\# | | | month of the year (1-12),

\# | | | | day of the week (0-6 with 0=Sunday).

\# | | | | | command(s)

\# | | | | | |

00 01 \* \* 6 find /home/user/moshell_logfiles -type f -name ’A\*.1.xml.gz’ -mtime +30 -exec rm -f {} \\;

00 01 \* \* 6 find /home/user/moshell_logfiles -type f -name ’\*\_ropfiles.zip’ -mtime +30 -exec rm -f {} \\;

00 01 \* \* 6 find /home/user/moshell_logfiles -type f -name ’\*.log’ -mtime +30 -exec gzip -f {} \\;

00 03 \* \* \* find /home/user/moshell_logfiles/logs_moshell/lttng-traces -type f -mtime +3 -exec rm -f {} \\;

**4.3.61 split \[&lt;size&gt;\] &lt;file&gt;**

Split a file into smaller files for upload to MHWeb or SMSWeb.

**Arguments:**

- &lt;size&gt;: the maximum size of the chunks into which the file will be split. Optional (default: 250M , needed for CSRs in SMS).
- &lt;file&gt;: the path of the file to split. Example: path to a dcgm.zip .

The file will be split into several files named as &lt;filename&gt;.x\[00-99\] , i.e. same filename but with extension "x" follewed by numbers from 00 to 99.

To recombine the split files into one file, do: cat filename.x?? > filename

Eg: cat enb101_191016_123959_dcgm.zip.x?? > enb101_191016_123959_dcgm.zip

**4.3.62 - dia\[g|gu||k|kf|ls|ds|os|pn|ln|dn|le|lv|ac|pc|lc|sa|pfs|lfs|pfm|lns\] \[&lt;ME addr|ME Name&gt; &lt;ME addr|ME name&gt; &lt;ME addr|ME name&gt;\]**

To create a DIA user session with connections to primary ME(s) and neighbor ME(s). When several MEs are specified with the dia command they shall be of same type, RN (RadioNode), vPP, etc

If the dia command is going to be used in the moshell session, it is recommended to be connected to the node via TLS. Check chapter 2.7 for more info on how to connect the moshell session over TLS. If the session is connected over TLS then the diagw_\* uservariables containing the credentials paths and workstation addresses will all be set automatically.

**Options:**

- g : Start the dia gateway binary and lttng-relayd on the host and create session with ME ip addresses provided. If no input is given with this option, it only starts dia gateway process. Input to option can be ip addresses or a yaml file with ME ipaddresses. Example yaml file for option g can be found under moshell/examples/misc/yaml.txt.
- gu : same as option "g" but also starts the TraceRouter utility, for EMCA trace streaming.
- k : Terminate dia gateway, lttng-relayd, and TraceRouter processes running on the host
- kf : Same as option "k" but force close of TraceRouter even when owned by another user
- ls : List session details based on input parameter &lt;sessionid|userid&gt;. If no value is provided all the session details will be printed
- ds : Delete a session based on the sessionid
- os : override Dia-Agents connected to other user(s) and/or Gateways in DIA Gateway
- pn : Stores the entities from a load file for a specific sessionid into DIA Gateway.
- ln : Lists the entities of a specific sessionid in DIA Gateway.
- dn : Deletes the entities for a specific sessionid in DIA Gateway.
- le : List enabled events of ME from DIA-Agent.
- lv : List available events of ME from DIA-Agent.
- ac : Activate the configuration for a specific sessionid.
- pc : Passivate the configuration for a specific sessionid.
- lc : List the configuration for a specific sessionid.
- sa : Get agent status for specific instance name.
- pfs : To change default storage location of snapshots.
- lfs : Get flight recorder status for specific instance name.
- pfm : Set Maximum number of snapshots on diagateway per session.

lns : Get entities status, including status of collections and configuration state, from DIA-Agents in a specific session.

**Examples:**

- diag : start dia gateway and lttng-relayd process on host
- diag 127.0.0.1 127.0.0.2 : start dia gateway and lttng-relayd processes on host and create a session with ME ipaddresses 127.0.0.1 and 127.0.0.2
- diag 127.0.0.1,127.0.0.2 : start dia gateway and lttng-relayd processes on host and create a session with ME ipaddress 127.0.0.1 and neighbour address 127.0.0.2
- diag /home/ephanch/setup.yaml : start dia gateway and lttng-relayd processes on host and create a session with ME ipaddresses given in setup.yaml file
- dials : will list all the sessions in dia gateway
- dials 1 : will list the session details of session id 1
- diads 1 : will delete session with sessionid 1
- diaos 1 : will steal/override Dia-Agents connected to other user(s) and/or Gateways in DIA Gateway
- diapn 1 xyz.yaml : will store the entities from a load file for a sessionid 1
- diapn 1 xyz.yaml 3 : will store entities from a load file for session id 1 and set reactivated parameter to 3
- dialn 1 : will list the entities of a sessionid 1
- diadn 1 : will delete the entities for a sessionid 1
- diale 1 12121212 : will list enabled events of ME for sessionid 1 and instanceid 12121212
- diale 1 /path/to/instance.yaml : will list enabled events for sessionid 1 and instanceids of all nodes listed in the yaml file
- dialv 1 12121212 : will list available events of ME for sessionid 1 and instanceid 12121212
- dialv 1 /path/to/instance.yaml : will list available events for sessionid 1 and instanceids of all nodes listed in the yaml file
- diaac 1 config_xyz : will activate the configuration for sessionid 1 and config name "config_xyz"
- diaac 1 config_xyz 3 : will activate the configuration for sessionid 1 and config name "config_xyz" and set reactivated parameter to 3
- diapc 1 : will passivate the configuration for sessionid 1
- diapc 1 config_xyz : will passivate the configuration for sessionid 1 and config name "config_xyz"
- dialc 1 : will list the configuration for sessionid 1
- diasa 1 12121212 : will get DIA-Agent specific status information for session id 1 and instance id 12121212.
- diapfs /home/ekavnit : will set the snapshots storage path to /home/ekavnit.
- dialfs 1 12121212 : will list all the snapshots stored matching with the filters.
- diapfm 3 : will set the maximum number of snapshots to 3.
- dialns 1 : will get entities status, including status of collections and configuration state, from DIA-Agents in a specific session.
- dialns -i 12121212 1 : will get entities status with instanceid 12121212 and session id 1.
- Flags for dialns:
- \-i &lt;instanceid&gt;
- \-n &lt;nodeid&gt;
- \-d &lt;datatype&gt;
- \-s &lt;status&gt;

**4.3.63 pe\[c\]\[l\]\[k\] \[&lt;polling interval&gt;|&lt;pid&gt;\] \[&lt;trigger&gt;\] \[&lt;action script&gt;\] \[&lt;number of iterations&gt;\]**

CPP post event functions **Options:**

- c: create moshell hook. The hook is waiting for the event(restart, alarm/event or any other trigger) and then execute the

user script.

- l: show all the hooks on the node with their states.
- k: stop the running hook.

Arguments of the "pec" command (first three are mandatory):

- polling interval: the time between every check of the event occurrence.
- trigger: the interaction trigger. It can be:
    - - attribute: hook will be triggered after MO attribute change
        - restart: hook will be triggered after restart of specified board
        - alarm: hook will be triggered after specific alarm raise
        - pm: hook will be triggered after specific pm counter stepped
        - coli: hook will be triggered after counter (printed by coli command) stepped
        - telog: hook will be triggered after specific trace in T&E log appeared in concrete board
        - nodelog: hook will be triggered after specific log appeared in concrete node log (look at "lg" moshell command description to get more information about node log)
        - kpi: hook will be triggered after increase/decrease specific kpi metric
        - &lt;another&gt;: hook will be triggered once the custom trigger script is done
- action script: the MO script to run once the hook is triggered
- number of iterations: the number of the same events after which action script will be executed

Argument of the "pek" command (mandatory):

- pid: the pid of the hook. The pid can be taken from the "pel" output.

**Examples:**

- pec 2 attribute /home/&lt;user&gt;/script.mos 6 : Create hook for MO attribute. The action script will be executed after 6th change of the specified attribute. The trigger will be checked every 2 seconds.
- pek 12345: Stop hook with pid "12345".
- pel: Show list of hooks.

**4.3.64 q/by/exit/quit \[&lt;exitcode&gt;\]**

Exit moshell.

Any of the following commands can be used to exit moshell: q, by, exit, quit

The exit command supports specifying an exit code, eg: exit 1

## 4.4 PM commands

**4.4.1 pmom\[acdpo\] \[&lt;moclass&gt;\] \[&lt;counter&gt;\] \[&lt;data-type&gt;\] \[&lt;flags&gt;\] \[&lt;description&gt;\]**

Print description of PM counters.

**Options:**

- a: shows what regular attributes can be included in scanners.
- c: show all the MO classes specified in the filter as well as their children/grandchildren/etc classes.
- d: gives a shorter printout, without the description part.
- p: show only the definitions relating to platform MOs (CPP)
- o: show only the definitions relating to application MOs

The type field refers to the data type of the counter value, e.g. an integer (long), or a sequence of integers.

The flags field refers to the properties of the counter, eg:

- deprecated: means that the counter is obsolete and will never be stepped.

notInMOM: means that the counter is implemented in RNC SW but not specified in the MOM. Should only happen on pre-GA SW.

notImplemented: means that the counter is specified in the MOM but not implemented in RNC SW. Should only happen on pre-GA SW.

- ropReset: indicates that the counter value is reset to 0 before each ROP period.
- noReset: indicates that the counter value is not reset to 0 at the ROP period and will only be reset at node restart or when the value reaches 231ˆ
- PEG,GAUGE,PDF,CC,DER,etc: this is the counter type, whose description can be found in CPI for CPP nodes, or from the command mom \\.(collectionme|aggre) . for COM nodes.
- a number in square brackets: shown on PDF counters to indicate the number of elements in the array.

**Examples:**

1.  pmom atmp - List all PM counters for the **AtmPort** MO
2.  pmom atmp cell - View description of all **AtmPort** counters that match the word "cell"
3.  pmom atmp . - View description of all **AtmPort** counters
4.  pmomd . reject - List all counters matching the word "reject"
5.  pmomd . . . . reject - List all counters whose description contain the word "reject"
6.  pmomd . . sequence:long - List all counters of type sequence:long
7.  pmomd . . . peg - List all counters of type PEG
8.  pmomd . . . noreset - List all counters which do not reset at the ROP period boundary

**4.4.2 kmom\[d\] \[&lt;area&gt;\] \[&lt;kpiname&gt;\] \[&lt;MOclass&gt;\] \[&lt;formula&gt;\] \[&lt;kpidescription&gt;\]**

Print description and formulas of KPIs.

**Options:**

- d : gives a shorter printout, without the description and formula part.

**Examples:**

- kmomd access - List all accessibility KPIs
- kmomd . sp - List all KPIs whose name matches the word "sp"
- kmomd . . utrancell - List all KPIs reported on MO class UtranCell
- kmomd . . . pmTotNoRrcConnectReqCsSucc - List all KPIs containing the counter pmTotNoRrcConnectReqCsSucc in the formula
- kmomd . . . . multi - List all KPIs containing the word "multi" in the description text
- kmom . sp_a - Show the description and formula for the KPI Sp_A

**4.4.3 pget\[m\]/lpget\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\]**

Read PM attribute(s) from MO(s).

The "m" option is for reading the attributes via MibManager instead of Corba. Only applicable on CPP nodes with C15.1 or higher.

Note1: Does not work on RNC MOs (UtranCell, IubLink, etc).

Note2: A counter value -2 indicates that this counter instance is suspected faulty.

Note3: Differences between pget on MSRBS vs pget on Cloud RAN:

- In MSRBS the real-time counter capability will always provide a counter value, if the counter is active, however with Cloud RAN the counter value will be blank if no pegging of the counter has occurred in over 2 hrs.
- In MSRBS the real-time counter value resets at the start of each ROP period for the majority of the MOs (except certain transport-related MOs such as RiEthernetPort where the counters are only reset at Baseband restart or when the maximum counter value is reached)
- In Cloud RAN, the counter behaviour is configurable via the moshell uservariable yang_pget_delta. See description

below:

- - yang_pget_delta=0 (default): display the latest value for a counter.
    - yang_pget_delta=1: display the counter value since the start of the last ROP. The ROP period is by default 15 minutes but can be changed in the uservariable rop_period.
    - yang_pget_delta=2: display the counter value increase since the duration of the uservariable pm_wait. Note: intervals smaller than 60 seconds are currently not supported by the system. Note: For received invalid counter values 9223372036854776, pget will display the value "NaN" (Not a Number). If no value is received for a counter a empty counter value is displayed.
        1.  **spget/lspget \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\]**

Read PM attribute(s) one by one ("slow pget").

Slow but useful in case the standard "pget" command is not working due to some attribute returning an exception.

Note: Does not work on RNC MOs (IubLink, UtranCell, etc).

- - 1.  **hpget\[c\]\[m\]/lhpget\[c\]\[m\] &lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt; \[&lt;attribute-filter&gt;\] \[&lt;value1-filter&gt;\] \[&lt;value2-filter&gt;\] \[&lt;value3-filter&gt;\] etc...**

Read PM attribute(s) from MO(s), print horizontally one line per MO (instead of one line per attribute).

**Options:**

- c: display the output in CSV format for easier export to excel (for instance). • m: print all MOs in a single table instead of separate tables per MO class

Example:

- hpget vcltp print the counter values for vclTp MOs (pmreceivedcells, pmtransmittedcells)
- hpget vcltp . ^0$ !^0$ print all vcltps that have 0 receivedCells and more than 0 transmittedCells

Note: A counter value -2 indicates that this counter instance is suspected faulty.

- - 1.  **pdiff/lpdiff \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value-filter&gt;\]**

Print incrementation of PM attributes.

Runs two consecutive pget commands separated by a time interval equal to the value of the uservariable pm_wait (default 25 seconds). Displays the value by which the counter(s) incremented in the interval pm_wait. The list of MOs displayed are stored in an MO group called pdiff_group. Example1: check all VclTp MOs whose transmittedcells have incremented but whose receivedcells have not incremented (could point towards a transmission problem)

\>> pdiff vcltp= transmit !^0

\>> pdiff pdiff_group receive ^0

\>> acc pdiff_group eteloopback (we can now perform a loopback test on those VclTp to check if they rea

Example2: check all Os155SpiTtp MOs whose errored seconds have incremented.

\>> pdiff os155 es !^0

- - 1.  **hpdiff\[m\]/lhpdiff\[m\] \[&lt;moGroup&gt;|&lt;moFilter&gt;|&lt;proxy(s)&gt;|all\] \[&lt;attribute-filter&gt;|all\] \[&lt;value1-filter&gt;\] \[&lt;value2-filter&gt;\] \[&lt;value3-filter&gt;\]**

Print incrementation of PM attributes, horizontally one line per MO (instead of one line per attribute)

This is the same functionality as "pdiff" except that the counters are printed side by side, one line per MO. For more information, refer to the help of the "pdiff" command.

**Options:**

- m : print all MOs in a single table instead of separate tables per MO class

Example:

hpdiff vcltp transmit|receiv —> print the counter values for vclTp MOs (pmreceivedcells, pmtransmittedcells)

hpdiff vcltp transmit|receiv ^0$ !^0$ —> print all vcltps that have 0 receivedCells and more than 0

transmittedCells

**4.4.8 pmx\[hfdnsckwlb3zeity\] \[&lt;mofilter&gt;|&lt;mogroup&gt;\] \[&lt;counter-filter&gt;|&lt;kpi(s)&gt;\] \[-z &lt;mogroup&gt;\] \[-l &lt;zipfile&gt;|&lt;directory&gt;\]**

**\[-w &lt;webdirectory&gt;\] \[-m &lt;minushours&gt;\] \[-p &lt;plushours&gt;\] \[-s &lt;startdate&gt;\[.&lt;starttime&gt;\]\] \[-e &lt;enddate&gt;\[.&lt;endtime&gt;\]\]**

**\[-a|-d|-h|-u\] \[-o &lt;outputFormat&gt;\] \[-tz &lt;hrs&gt;\] \[-f &lt;formulafile&gt;\] \[-j &lt;precision&gt;\] \[-mo &lt;regexp&gt;\] \[| &lt;unix-cmds&gt;\]**

Display counter or KPI values, extracted from the statistics ROP files, or from the MOs in real-time.

**Arguments**

- The first argument (mofilter/mogroup) is to specify the MO instances whose counters shall be printed: can be identified by an MO group or by a regular expression matching the LDN of the MOs. It is also possible to use the exclamation mark (!) to print all MOs except those matching the filter.
- The second argument can be either:
    - a regular expression matching the name(s) of the counter(s) that shall be printed, eg rrc.\*success
    - a regular expression matching the name(s) of the KPIs(s) that shall be printed, eg rrc.\*success. The KPI formulas are read from the default formula file in moshell/commonjars/pm or from the formula file specified in the "-f" option.

If the first and second arguments are omitted, the XML ROP files are parsed and the result is stored on file instead of being displayed to screen. The result files will be stored in the same location on the workstation as where the XML ROP files are stored, ie: **~/moshell_logfiles/logs_moshell/pmfiles/nodeipaddress**. This location can be changed with the user variable _pm_logdir_.

**Options**

- e : to display KPI values instead of counter values. The KPI name argument is a non case sensitive regular expression. The KPI formulas are taken from the default formula file or from the formula file specified with the -f option.
- t : to print real-time counter/KPI values from "pget". See examples further down. Not applicable for RNC radio network KPIs
- td: to print real-time counter/KPI values from "pdiff". See examples further down. Not applicable for RNC radio netowork KPIs.
- y : to print KPI values from the ropfiles in the kpiDataPath (/c/kpi_data). Only applicable to CPP nodes that support PmKpi definitions.
- h : to display the counters side-by-side (h as in _horizontal_). Otherwise, there is one line for each MO instance and counter.
- f : to prevent pmx from rechecking if there are any newer xml files (f as in _fast_).
- d : needed for parsing PEG counters which are not reset at the end of each ROP period. In pmom command, these counters are marked with the tag PEG,noReset. The command pmomd . . . peg,noreset will show all such counters.
- dd: same as d but allows negative delta values.
- n : to aggregate all counters on MO level.
- k : to keep the counters marked with the suspected faulty tag &lt;sf&gt;TRUE&lt;/sf&gt;, without this option they are discarded.
- s : to flag the counters with negative or empty value, or those marked with the suspected faulty tag &lt;sf&gt;TRUE&lt;/sf&gt;. The counters are then displayed with a label showing SuspectedFaulty, NegativeCounter, or, EmptyCounter.
- c : to display the number of counter instances in the ROP file. Should be identical to the number of active counter instances shown in pgetsn.
- 3 : to print 3GSIM instantaneous counters from /c/3gsim/stats
- i : to print ETIPG counters from CELLO_IPTRAN_DEBUG_LOG
- w : to generate a web report in table and graph format. The -w switch can be used to specify the location of the webpage. Currently works best with Firefox. The generated html files cannot be opened locally but must be uploaded to a web server and viewed via a URL.
- z : to print the timestamps in the timezone of the workstation where moshell is executing
- l : to generate an excel graph. Can be combined with b option (pmxlb) for treating buckets in PDF counters as separate counters. To generate a graph comparing two different periods, specify the periods with the options:

\-s1 &lt;startperiod1&gt; -e1 &lt;endperiod1&gt; -s2 &lt;startperiod2&gt; -e2 &lt;endperiod2&gt;. See examples in the examples section below.

### Switches

- \-m, -p, -s, -e : for specifying a time span, see h pmr (Section 4.4.10) for more information. By default, the time span will only cover the latest ROP file (equivalent to -m 0.25).
- \-a, -d, -h, -u : for specifiying if any time aggregation should be used. Time aggregation can be done on hour basis ("-h"), day basis ("-d") or on the whole timespan ("-a"). If the switch is not included, then no time aggregation will occur but the timestamps will be shown to the minute. If timestamps should be shown per second (e.g. in case of ROP shorter than a minute) then the "-u" option can be used.
- \-z &lt;mogroup&gt; : to save the MOs listed in the printout to a MO group.
- \-l &lt;file&gt;|&lt;dir&gt; : for specifying a directory containing ROP files. In this case, pmx will parse the ROP files stored in that directory instead of from the node. Can also be used in offline mode. To parse the ENM ropfiles located in a dcgm, the variable $enmfiles.zip can be used to point to the path of the ENM ropfiles. Eg: -l $enmfiles.zip
- \-o &lt;fmt&gt; : for specifying the output format. By default, the output is text but it is possible to specify: csv, html, or htmltab
- \-w &lt;dir&gt; : for specifiying the path where the web report will be stored. Only applicable with option w (pmxw). When -w is not given, a default location will be chosen for the web report.
- \-tz &lt;hrs&gt; : for printing the timestamps a specific timezone. Eg: -tz +10 will show the timestamps in UTC+10 timezone. Note: this setting can be saved in the moshellrc uservariable tz_option .
- \-j &lt;precision&gt; : to specify the number of digits after the decimal point (eg: -j 2 => 2 digits after the decimal point). Only applicable with "pmxe"
- \-mo &lt;regexp&gt; : to specify a regular expression for aggregation at MO level. Eg: -mo ManagedElement=(\[^,\]+) => aggregate at ManagedElement level. The field specified in the "-mo" option will correspond to the field specified in the "-m" option in pmXtab. More info on this field can be found in the help of pmXtab (moshell/pmXtab –help).
- \-f &lt;formulafile&gt; : to specify a different formula file than the default one (when using "pmxe").

It is possible to pipe the command into a unix command (eg: **grep**, **sort**, etc).

**Examples:**

- pmx utrancell downtime - all counters matching "downtime" on all MOs matching "utrancell" will be displayed for the last ROP period
- pmxz utrancell downtime - same as above but timestamps will be displayed in the workstation local time instead of utc time
- pmx utrancell downtime -tz -5 - same as above but timestamps will be displayed in the timezone UTC-5
- pmxh utrancell downtime - same as above but the counters will be displayed side-by-side
- pmxh utrancell downtime -m 3 -a same as above but the last 3 hours (12 ROP periods) will be read and aggregated into one value
- pmxhf utrancell downtime -m 3 -a | sort -k 2 print same as above without rechecking for new ROP files ("f" option), then sort on the second field ("| sort -k 2")
- pmx -m 2 - fetch and parse all ROP files from the last two hours, result to be stored on disk • pmxf -s 19000101 - parse all ROP files that currently exist in the pmlog directory in the workstation
- pmxs -m 0.25 - show the counters marked as suspected faulty for the last 15 minute ROP period.
- pmxn !utrancell=iub-10 pmTotNoRrcConnectReq$ - show the counter pmTotNoRrcConnectReq aggregated on all cells except cell iub-10.
- pmxw utrancell=iub-10-1 pmTotNoRrcConnectReq$ -m 24 - show the evolution in graphical format (web) over the past 24 hours of the pmTotNoRrcConnectReq counter on the MO utrancell=iub-10-1
- pmxl utrancell=iub-10-1 pmTotNoRrcConnectReq$ -m 24 - show the evolution in graphical format (excel) over the past 24 hours of the pmTotNoRrcConnectReq counter on the MO utrancell=iub-10-1
- pmxlb utrancell=iub-10-1 pmTotNoRrcConnectReq$ -s1 20140101.0900 -e1 20140101.1000

\-s2 20140101.1100 -e2 20140101.1200

\- Compare the evolution of the counter pmTotNoRrcConnectReq in the period 20140101 from 9:00 to 10:00 , with the period from 11:00 to 12:00 , and use bucket option. pmxi slot=24 reject - print the ETIPG counters from slot 24 whose name match the word reject

- pmxel utrancell drop -m 24 - print the utrancell KPIs whose name match the word "drop" for the last 24 hours and output in excel format
- pmxen utrancell drop - print the utrancell KPI whose name match the word "drop" and aggregate at node level for the last 15 minutes
- pmxet fdd interferencepwr$ - print the KPI Int_RadioRecInterferencePwr on all EUtranCellFDD
- pmxetd fdd interferencepwrprb\[0-9\]$ - print the KPI Int_RadioRecInterferencePwrPrb on all EUtranCellFDD
- pmxetd giga giga - print the KPIs matching "giga" on all MOs matching "giga" (eg "gigabit" MOs)
- pmxetd eth eth - print the KPIs matching "eth" on all MOs matching "eth" (eg "ethernetport" MOs)
- pmxetd atm atm - print the KPIs matching "atm" on all MOs matching "atm" (eg "atmport" MOs)
- pmxet fdd acc_ - print all accessiblity KPIs on all EUtranCellFDD MOs
- pmxe sctp sctp -m 4 -a -z tadek | $gawk ’($3>0 && $3!="N/A")’ –> make a mogroup called "tadek" containing all SctpAssociation MOs that have PacketLossRatio>0

Note: only counters that are included in an **active** performance scanner will be displayed.

Performance scanners can be read with the pgets command and created with the pcr command or from OSS/ENM.

In the case of RAN nodes (RNC, RXI, RBS, eNodeB), the OSSRC/ENM does not allow external tools (such as moshell) to create/delete/modify a PM scanner. Any attempt to do this will result in OSSRC/ENM reverting the change. This is a feature of OSS/ENM and applies only to RAN nodes, not MGW.

Note: Handling of duplicated counter instances

Counter instances that are defined in several PM scanners will be reported by CPP as duplicated entries in the ROP files.

This can lead to unexpected results, such as counters with doubled values.

Usually the pmr/pmx commands can successfully ignore the duplicated counter entries but only when all the processed ROP files have the same type of counter duplication.

Unexpected values will occur when some of the processed ROP files have a duplication while other dont.

Therefore it is highly recommended to make sure that none of the counters are defined in several scanners at the same time.

The commands pgets and pmxs will show if there are any duplicated counter instances in the PM scanners.

**4.4.9 pmx2\[h\]\[f\] &lt;mo-filter&gt; &lt;counter-filter&gt; \[-u\] \[-i 0|1|2\] \[&lt;time options&gt;\] \[-o &lt;outputFormat&gt;\] \[ | &lt;unix-cmds&gt;\]**

Display real-time radio performance counter values.

**Switches:**

- h: to print the counter names horizontally and timestamps vertically. Useful if a long timespan will be printed. Without "h" option the counter names are printed vertically and the timestamps horizontally.
- f: to read the counter values from local cache file instead of the node, this is quicker. Without "f" option, the counter values are re-read from the radios. If the output is empty or out of date, just re-run the command without "f" once, then it should be possible to use "f" again.

**Options:**

- \-u: to display timestamps with seconds. Without "-u" the timestamps are shown by the minute. If using the "-u" option then it is recommended to combine with the "h" switch, otherwise the line can become very long.
- \-i 0: to skip counters with 6-second granularity (default)
- \-i 1: to skip counters with 900-second granularity
- \-i 2: include all granularities, both 6-second and 900-second

**Time options:**

- \-m/-p/-s/-e : refer to "h pmx" for more info about the time options

**Format options:**

- \-o &lt;fmt&gt; : for specifying the output format. By default, the output is text but it is possible to specify: "csv", "html", or

"htmltab".

**Argument:**

- the first argument refers to the MO, usually the FieldReplaceableUnit corresponding to the radio. Put a dot sign (wildcard) to show all radios.
- the second argument refers to the counter name. Any text string can be put here but the suggested ones are powersupply|inputvoltage|antenna|txpower|rxpower|cpri|ltu in order to see the major counter categories. To see all counters a dot (wildcard) can be used instead.

**Examples:**

- pmx2 . ltu|cpri -m 300 -> print ltu and cpri counters for the last 300 hours, with timestamps on X-axis and counter names and MOs on the Y-axis

|     |     |
| --- | --- |
| • pmx2f . ltu\|cpri -m 300 | \-> same as above but read from cache |
| • pmx2f rru-4 ltu\|cpri -m 300 | \-> same as above but only for fieldreplaceableunit=rru-4 |
| • pmx2fh rru-4 ltu\|cpri -m 300 and MOs on the Y-axis | \-> same as above but with counter names on the X-axis and timestamps |
| • pmx2fh rru-4 ltu\|cpri -m 300 -u | \-> same as above but with timestamps in seconds instead of minutes |
| • pmx2fh . dbm_avg -m 1 -i 1 -u<br><br>6-second granularity , for the last 1 hour | \-> print average tx/rx power values in dbm, displayed at second level with |

**4.4.10 pmr\[agfkwop3z\] \[-g &lt;mofilter&gt;|&lt;mogroup&gt;\] \[-z &lt;mogroup&gt;\] \[-r &lt;report(s)&gt;\] \[-l &lt;zipfile&gt;|&lt;directory&gt;\] \[-w**

**&lt;webdirectory&gt;\] \[-i &lt;iubCellModule-file&gt;\] \[-f &lt;formulafile&gt;\] \[-c &lt;configfile&gt;\] \[-m &lt;minushours&gt;\] \[-p &lt;plushours&gt;\] \[-s &lt;startdate&gt;\[.&lt;starttime&gt;\]\] \[-e &lt;enddate&gt;\[.&lt;endtime&gt;\]\] \[-o &lt;outputFormat&gt;\] \[-t &lt;thresholdfile&gt;\] \[-tz &lt;hrs&gt;\]**

**\[|&lt;unix-cmds&gt;\]**

Produce PM KPI reports, based on counter values in statistics ROP files and formulas in CPI documentation.

**Report choice**

- if the command pmrg is used then all available reports are printed.
- if the option -r is used then it is possible to specify which reports to print. Eg: pmr -r 1,3,5-10,12 —> reports 1,3,5,6,7,8,9,10,12 are printed
- if the option f is used then the ropfiles are simply fetched and stored in a zipfile. The zipfile is called

&lt;node&gt;\_ropfile.zip and its location is &lt;logdir&gt;/pmfiles/&lt;nodeaddress&gt;/&lt;date_time&gt; . A different location can be specified by running: pmrf &lt;directory&gt;. The zipfile can then be used for offline processing with the -l option.

- otherwise, a menu is printed, prompting the user to enter a report number, or x to exit the pmr menu.

**Options**

- a : for fetching all available ROP files from the node.
- f : for fetching and saving the ROP files to a zipfile, which will be called &lt;node&gt;\_ropfiles.zip. No reports are printed. In case of CPP nodes, a file containing MO data needed for certain reports is included.
- ff: same as f but the MO data file is not included which makes the collection quicker. This option is used when collecting a DCG since MO data will already be available in the MO dump.
- g : for printing all available reports, the menu will not be shown.
- k : for keeping the counters marked with the suspected faulty tag &lt;sf&gt;TRUE&lt;/sf&gt;, without this option they are discarded.
- w : for generating a web report in table and graph format. The -w switch can be used to specify the location of the webpage. Currently works best with Firefox. The generated html files cannot be opened locally but must be uploaded to a web server and viewed via a URL.
- o : for printing official KPI reports, using the KPI names of the CPI. Currently available for RNC only.
- p : for generating PNG files, using GnuPlot.
- 3 : for printing 3GSIM instantaneous counters from /c/3gsim/stats
- z : for printing the timestamps in the timezone of the workstation where moshell is executing

**MO filtering**

- The option -z &lt;mogroup&gt; can be used to save the MOs printed by a report into a MO group.

Example: to save the MOs printed by the RNC report Worst 20 cells for RRC, run

pmr -r &lt;report&gt; -z &lt;mogroup&gt;.

- The option -g can be used to calculate KPIs for a smaller group of MOs instead of all. The processing time will be quicker and it is then possible to filter results on smaller groups of resources. Example:
    - pmr -g tdmterm will show KPIs based on TdmTermGrp counters only
    - pmr -g cellmod8 will show KPIs based on counters of cells belonging to module 8 only (where cellmod8 is a MO group created with the commands ma iubmod8 iublink module =8$ and ma cellmod8 iubmod8 reserved)
- The option -g can also be used to exclude certain MOs from the reports, by using the exclamation mark (!) as a negative filter.

Example: to exclude the MOs printed in the report Worst 20 cells for RRC, run pmr -r &lt;report&gt; -z worstcellsgroup, then pmr -g !worstcellsgroup.

### Threshold file

To check that the KPIs are within certain criteria, a threshold file can be specified with the option -t.

Example of threshold file and syntax explanation can be found at moshell/examples/pm_files/thresholds.txt.

Any KPI that are outside the the criteria specified in the threshold file will be marked in red or purple, depending on the severity. **Generate Web report**

Example:

- pmrwg : all reports will be saved to a web page in a default chosen location which is printed at the end of the pmr printout
- pmrw -r 1-10,14 -w /home/user/public_html/RNC14 : reports 1-10 and 14 are saved to a web page located under /home/user/public_html/RNC14

Each pmr report in the web page shows up as a table and in some cases a graph is also generated. Currently works best with Firefox, avoid IE.

### Generate PNG files

The option "p" can be used to generate PNG files, using GnuPlot.

(\*\* Note : you may have to do a new re-install of cygwin to get gnuplot working)

The GnuPlot package can be installed from cygwin "select packages" window: Graphics > gnuplot

Example:

- pmrp -m 24

For RNC, it is recommended to run the plot on selected cell by using MO group. Example:

- ma myrbs iublink=1234 reservedby
- pmrp -m 24 -g myrbs

**Suspected faulty counters**

If some ROP files contain counters marked with the "suspected faulty" tag (&lt;sf&gt;TRUE&lt;/sf&gt;) then they are silently discarded unless the user has given the option k (e.g. pmrk) in which case the suspected faulty counter values will be kept. To identify which counter values are marked with the suspected faulty tag, the command pmxs can be used. **Online/Offline**

1.  Online:

To use pmr online (ie when connected to a node) just skip the -l option.

The function will check if there are any new XML files on the node, download any new XML files to the workstation as long as their timestamp is within the timespan specified by the -m/-p/-s/-e options, get some MO configuration data and print the menu.

1.  Offline:

To run pmr offline, specify the location of the ROP files with the -l option. The location can be a folder or a zipfile produced by the pmrf command. Refer to the "Offline mode" chapter for more info. To parse the ENM ropfiles located in a dcgm, the variable $enmfiles.zip can be used to point to the path of the ENM ropfiles. Eg: -l $enmfiles.zip

**Time options**

If the command pmra is used then all ROP files are fetched. Otherwise, the ROP files of the last hour are fetched.

The -m and -p options are used for specifying the timespan that the reports should cover, in hours or parts of hours.

The timespan is relative to the node’s current date/time if online, and relative to the most recent file timestamp if offline.

Example:

- pmr -m 5 - will show statistics for the last 5 hours.
- pmr -m 5 -p 3 - will show statistics starting 5 hours ago and 3 hours from then on (ie: up to 2 hours ago).
- pmr -m 0.25 - will show statistics for the last 15 minutes
- pmr -m 0.5 - will show statistics for the last 30 minutes
- pmrf -m 18 /path/to/ropfiles - fetch the ropfiles of the last 18 hours and put them in a zipfile called &lt;node&gt;\_ropfiles.zip in the folder /path/to/ropfiles By default the timespan is for the last 1 hour.

The -s and -e options are used for specifying an absolute timespan. The timestamp should be in the format yyyymmdd\[.hhmm\] Example:

- pmr -s 20050705 -e 20050710
- pmr -s 20050705.1000
- pmr -s 20050705.1000 -e 20050705.1915

The -tz &lt;hrs&gt; switch is for printing the timestamps a specific timezone. Eg: -tz +10 will show the timestamps in UTC+10 timezone. Note: this setting can be saved in the moshellrc uservariable tz_option .

**Piping**

It is possible to pipe each report into some unix commands. The pipe is done at the "Your Choice" prompt, after the menu listing all the reports. Example:

- 4 | sort -k3 -n - to view report 4 and sort it numerically on the third column
- 5 | grep 205 to view report 5 and grep for lines matching "205"
- 3 | sort -k4 -n -r to view report 3 and reverse sort it numerically on the fourth column

**Output format**

The output format can be specified with the -o option.

By default, the output is text but it is also possible to specify the following formats:

- csv Comma separated
- html HTML
- htmltab HTML tables only (use for embedding into a web page)

Note: HTML reports are best generated with the option "w", e.g. "pmrw". See description further up.

### IubCellModule file

This file is only needed when offline, when printing reports aggregated on Iub/Module/AtmPort/Subrack level.

If ROP files have been collected with "pmrf" then the file is automatically included with the ROP files and will be used when parsing the ROP files offline. Otherwise, the path of the file can also be specified with the option "-i".

This file contains the following printouts:

get ^aal5tpvcctp= vcltpid get ^unisaaltp= aal5tpvcctpid get ^nbapcommon= unisaaltpref get ^iublink= rncmoduleref get ^utrancell= iublinkref get device= spmreference

get ^ipaccesshostet= ipInterfaceMoRef get ^sctp= rpuid

pr ^(ipinterface|pluginunit|atmport|vpltp|vcltp|ethernetswitchport|ethernetswitchmoduleport|internaleth

Note: Handling of duplicated counter instances

Counter instances that are defined in several PM scanners will be reported by CPP as duplicated entries in the ROP files.

This can lead to unexpected results, such as counters with doubled values.

Usually the pmr/pmx commands can successfully ignore the duplicated counter entries but only when all the processed ROP files have the same type of counter duplication.

Unexpected values will occur when some of the processed ROP files have a duplication while other dont.

Therefore it is highly recommended to make sure that none of the counters are defined in several scanners at the same time. The commands pgets and pmxs will show if there are any duplicated counter instances in the PM scanners.

**4.4.11 pme\[fd\]\[cgurvxyz\] \[&lt;pm_logdir|uehexcep.zip&gt;\] \[-b &lt;boardgroup&gt;\] \[-f\] \[-m &lt;minushours&gt;\] \[-p &lt;plushours&gt;\] \[-s &lt;startdate&gt;\[.&lt;starttime&gt;\]\] \[-e &lt;enddate&gt;\[.&lt;endtime&gt;\]\] \[-o &lt;uehoptions&gt;\]**

Fetch/decode event ROP files (RNC/RBS/ERBS/MSRBS).

**Main options:**

- f for fetching the ROP files
- d for decoding/parsing the ROP files

**Secondary options:**

- c for CTR/CellTrace
- u for UETR/UeTrace
- g for GPEH. Make sure the attribute RncFunction::gpehDataLevel is set to 1 (ALL_DATA). Otherwise the GPEH ROP files will only contain header data.
- r for RNC_Exception (/pxxyy00/RNC_Exceptions) or ENB Exceptions

(/c/logfiles/troubleshooting/exception) or MSRBS Exceptions (/lrat/exception)

- v for ENB LocalEvents (/r00xx00/localevent)
- x for RNC UEH Exception basic files (add option "z" to store them in a zipfile)
- y for RNC UEH Exception detailed files (add option "z" to store them in a zipfile)

Note: If none of these options are specified then all applicable ROP files are fetched/decoded.

**Argument**

The argument is optional and can either be:

- the storage folder for the ROP files (applicable for all types of ROP files)
- or the path of a uehExceptions.zip file , previouly collected by the command pmefxyz -m 28d

The default location is /path/to/moshell_logfiles/logs_moshell/pmfiles/&lt;nodeip&gt; .

It is also possible to change the default location in the uservariable pm_logdir.

**Other options:**

- \-b &lt;boardgroup&gt; : to fetch GPEH files on certain modules only, eg: pmefdg -b mod1
- \-f : to run the wcdma decoder with option "–force".
- \-o &lt;ueh-options&gt; : to specify various options for the parsing of RNC UEH exceptions. See below.

**Time options:**

The "-m" and "-p" options are used for specifying the timespan that the reports should cover, in hours or parts of hours. Note: To specify in days, add the letter "d".

The timespan is relative to the node’s current date/time if online, and relative to the most recent file timestamp if offline. By default the timespan is for the last 0.25 hour (15 minutes). Examples:

- pmefgd -m 5 : fetch and decode gpeh rop files for the last 5 hours.
- pmefd -m 5 -p 3 : fetch and decode all event rop files, starting 5 hours ago and 3 hours from then on (ie: up to 2 hours ago).
- pmedu -m 0.25 : decode uetr rop files for the last 15 minutes
- pmef -m 0.5 : fetch all event rop files for the last 30 minutes
- pmefxz -m 28d : fetch all basic UEH exception files for the last 28 days
- pmed -s 20050705 -e 20050710 : decode all event rop files between the dates 20050705 and 20050710
- pmefc -s 20050705.1000 : fetch all ctr rop files from the 20050705 at 10:00 to now
- pmefdu -s 20050705.1000 -e 20050705.1915 : fetch and decode uetr rop files between the 20050705 at 10:00 to the 20050705 at 19:15

**RNC UEH exceptions:**

There are two kind of reports: basic and detailed.

- basic reports ("x") contain 4 fields: EC (Exception Code), CC (Cause Code), Effect (eg: call drop), and Nr (Number of Exceptions of this type that occurred in the node).
- detailed reports ("y") contain 4 more fields in addition to the above 4: Cell (the Cell Id where the exception occurred), sUeRc/tUeRc (the source and target bearer of the UE), procedure (the procedure during which the exception occurred).

The options below are specified with the "-o" option.

- time=a/d/h : to aggregate on the whole period (a) , or on daily basis (d), or on hourly basis (h). If unspecified then "a" is the default. More than one value can be given, eg "time=adh" will print all three reports (whole period, daily, and hourly). Basic reports are not applicable on hourly basis.
- fmt=c : to print the output in csv format. Unspecified will print tab-separated.
- min=&lt;value&gt; : to filter out UEH exceptions that occurred less than a certain number of times, eg "min=100" will only show UEH exceptions that occurred 100 times or more. Unspecified will print all UEH exceptions.
- sort=&lt;field&gt; : to specify the field (1,2,3,4...) on which to sort the output. Eg: "sort=4" means to sort on the 4th column.
- sum=&lt;list of fields&gt; : to specify the list of fields (1, 2, 3, 4...) to be included in the report. Eg: "sum=12347" means to include fields 1,2,3,4, and 7 in the report.

Examples:

- pmefxy -m 10d : fetch all basic and detailed files for the last 10 days
- pmedx -m 10d -o time=d,fmt=c,sort=3 : print the basic report for the last 10 days printed on daily basis , in csv format, and sorted on the 3rd column
- pmedy -m 10d -o time=adh,sum=12347 : print only the columns 1,2,3,4,7 for the detailed reports on daily, hourly, and full period basis
- pmedy -s 20200604.0000 -e 20200604.1200 -o time=h,fmt=c,sum=123 : print detailed report in csv format on hourly basis for the first 12 hours on 20200604, aggregate on the first 3 columns.
- pmedxy -m 10d -o time=a,min=100,sum=123,sort=4 : print both basic and detailed reports for last 10 days aggregated on the whole period, including only the first 3 fields and sorting on the 4th column

**4.4.12 pst \[&lt;scan-filter&gt;|&lt;scan-proxy&gt;\] \[&lt;scan-state&gt;\]**

List all PM scanners and their state. Examples:

- pst
- pst . act - list all active scanners
- pst gpeh susp - list all gpeh scanners that are suspended

**4.4.13 pgets\[m\]\[n\]\[r\] \[&lt;scan-filter&gt;|&lt;scan-proxy&gt;\] \[&lt;contents-filter&gt;\]**

Print the counters defined in the scanner(s).

Without argument, all scanners/jobs are printed.

For a STATS/PM scanner, we see the following:

- a header showing the proxy number, the scanner name, the state, the granularity period in seconds and the total number of counters activated (CPP) or the number of MeasurementReaders defined (ECIM/COM).
- the list and number of counters grouped by MoClass
- with the option n we see the number of counter instances for each scanner (only applicable when the contents-filter is empty).
- for each counter, some optional tags may be shown:
    - deprecated: means that the counter is obsolete and will never be stepped.
    - a number in square brackets: shown on PDF counters to indicate the number of elements in the array.
    - notInMOM: means that the counter is implemented in RNC SW but not specified in the MOM. Should only happen on pre-GA SW.

For an EVENT scanner (GPEH/UETR/CTR), we see the following:

- a header showing the proxy number, the scanner name, the state, and the total number of events activated in the filter
- a list of filters such as IMSI, ACCESS_CELL, CELL, etc
- the list and number of event filters grouped by event category

It is possible to use a _contents-filter_. If used, then only the scanners containing a string matching the filter (not case sensitive) will be displayed.

**Options:**

- m : groups the printout by MO and counter instead of by scanner. It shows for each counter in how many scanners they are defined and which ones.
- n : shows the number of counter instances defined in each scanner. The number of counter instances for each scanner are kept in a cache which stays for the duration of the moshell session. To refresh the cache, run pgetsn with the option r, ie pgetsnr.

**Examples:**

|     |     |
| --- | --- |
| • pgets | \- show contents of all scanners/jobs |
| • pgets stats\|pmjob | \- show contents of all statistics scanners or pmjobs |
| • pgets . receive | \- list all scanners whose contents matches "receive" |
| • pgets . atmport.\*receive | \- list all scanners whose contents matches "atmport.\*receive" |
| • pgets . cell=12345 | \- list all whose contents match the string "cell=12345" |
| • pgetsn . | \- show the number of counter instances defined in each statistics scanner |
| • pgetsm . load | \- for all counters matching the word load, show if they are defined in a scanner |

and if yes, in how many scanners and which ones

|     |     |
| --- | --- |
| • pgetsm . utrancell | \- same as above but for all counters belonging to utrancell |
| • pgetsm . 2 | \- show all counters which are defined in two scanners |

**4.4.14 pcr\[pcfpdazg\]/lpcr\[pcfpdazg\] &lt;ScannerName|JobName&gt; &lt;moclass-filter&gt;|&lt;moinstance-filter&gt;|&lt;mo-group&gt;|&lt;counter-file&gt; \[&lt;counter-filter&gt;\] \[&lt;granularity&gt;\]**

Create a Statistics Scanner or PmJob.

Note: EVENT scanners are already created by default and shall be set with the "pset" command.

The granularity field is optional.

- On CPP nodes, it can be set to 300, 900, or 3600 seconds.
- On COM nodes, it can be set to 10, 30, 60, 300, 900, 1800, 3600, 43200, or 86400 seconds.

By default it will be set to 900 (15 minutes).

Note: In RCS commercial nodes, only 900 seconds is supported. In RCS lab nodes (unsecure DUS) it may be necessary to run the following command (followed by node restart) before being able to select other granularity values: /pms/rp ecim

**Options:**

- c: for activating counters on all MO classes matching the filter as well as all their children/grandchildren, etc.
- f: for adding counters even if they are already included in another scanner.
- g: for creating PmJob with MeasurementReaders on PmGroup only (all counters in each MO class will be included). Applicable for COM nodes only.
- p: for creating a PREDEF scanner. By default a USERDEF scanner is created.
- z: for specifying a custom name without prefix or suffix and/or with spaces in the name (which will be represented by "@" sign).
- d\[a\]: for debug. The syntax of "pcrd" is: pcrd/pcrda &lt;counter-file&gt; where the format of the counter-file shall be as per below. The purpose of "pcrd" is to test a counter file and identify any pm counters that are not supported by the node SW. With option "a" (pcrda), it is also possible to test which regular attributes can be included in a scanner.

A negative filter (!) can be used on the moclass or counter filter in order to exclude certain MOs or counters. See more info about regular expressions used in the filters in Section 3.

Note: for certain MO classes, the configuration attributes can be included in the scanner. The user variable include_nonpm must be set to 1.

**Examples:**

- pcr atmport_vcltp atmport|vcltp - A new user defined scanner is created for all MOs of class AtmPort and VclTp
- pcr atmport_vcltp atmport=ms-6-1 received 300 - Only the MO instances whose RDN match "atmport=ms-6" are included. Only counters matching "received" will be activated. The granularity period will 5 minutes (300 seconds).
- lpcr vc_scanner atmport=ms-6-1,vptlp=1,.\*vcltp=100 –> only the MO instances whose LDN match

"atmport=ms-6-1,vptlp=1,.\*vcltp=100" are included.

- pcr atmport atmportgroup - All counters for MO group _atmportgroup_ are added to a new scanner called _atmport_.
- pcr atmport_utrancell ~/mycounters.txt - All counters stored in the file /mycounters.txt are added to the scanner _atmport_utrancell_ . See format of the counter file below.
- pcrc all_transport transportnetwork - All counters for all MO classes lying under the TransportNetwork MO are added to the scanner _all_transport_
- pcrc all_transport_notMtp transportnetwork!mtp3 - All counters for all MO classes lying under the TransportNetwork except Mtp3 MOs are added to the scanner _all_tranport_notMtp_
- pcrc all_rnc_without_utranrel rncfunction!utranrelation|utrancell !rej - All counters for all MOs lying under RncFunction except UtranRelation and UtranCell MOs and not counters matching "rej"
- pcrp myscanner atmport - all counters in MO classes matching "atmport" are included in the scanner PREDEF.myscanner.STATS (CPP) or PREDEF_myscanner.NOOSSCONTROL (COM)
- pcrp PRIMARY ~/primarycounters.txt - all counters stored in the file /primarycounters.txt are included in the scanner PREDEF.PRIMARY.STATS (CPP) or PREDEF_PRIMARY.NOOSSCONTROL (COM)
- pcrz my@scanner plug|ipint - create a scanner with name "my scanner"

Notes:

- If certain counters are already defined in another scanner of that node, they will be automatically excluded from the new scanner in order not to have duplicate lines in the XML file. This can be bypassed by using the f option, eg: pcrf atmport_vcltp atmport|vcltp (not recommended)
- By default, the counters that are marked as deprecated or notInMOM are not included by the pcr command. This behaviour can be changed by setting the uservariable exclude_deprecated to 0.

**Interaction with OSSRC/ENM:**

Scanners/Jobs created from moshell/AMOS on a node controlled by OSS/ENM will be automatically deleted by OSS/ENM after a few minutes. It is possible to avoid this by:

- creating the PM scanner with the command "pcrp", since PREDEF scanners are not touched by OSS/ENM. To delete predefined scanner, use "pdelp"
- or, in the case of OSSRC, setting the OSSRC setting scannerConfigMaster to OFF

**Format of the counter file:** The spaces at the beginning of the line are not necessary, they are just shown for readability purposes. To comment out some lines, just precede the line with a hash sign (#). Any words after the first word are ignored.

Example:

AtmPort pmReceivedAtmCells pmSecondsWithUnexp UtranCell pmCellDowntimeAuto pmCellDowntimeMan pmChSwitchDch128Fach pmChSwitchDch384Fach pmChSwitchDch64Fach

It is also possible to take the printout from pmom as is. This will work as well and saves having to do any editing.

#############################################

MO Class Pm Counters

#############################################

UtranCell 296

pmCellDowntimeAuto

pmCellDowntimeMan pmChSwitchDch128Fach pmChSwitchDch384Fach pmChSwitchDch64Fach pmChSwitchFachDch pmChSwitchFachIdle

It is also possible to use the following format for the counter file (for creating counters on MO instances where each MO instance will use a different set of counters).

Example:

ManagedElement=1,RncFunction=1,UtranCell=30124 pmRes1 pmRes2 ManagedElement=1,RncFunction=1,UtranCell=30125 pmRes3 ManagedElement=1,RncFunction=1,UtranCell=30126 pmRes2 pmRes4

It is also possible to take the printout of pgets as is. This is useful to clone an existing scanner, eg with a different rop period. Example:

l+ pgets &lt;oldscanner&gt; lpbl &lt;oldscanner&gt;

pcrf &lt;newscanner&gt; $logfile . 300

**4.4.15 pcrk\[f\]\[v\]\[d\] \[&lt;kpidefinitionfile&gt;\] \[&lt;granularity&gt;\]**

Create PmKpi definitions on the node.

The command first generates a copy of the existing PmKpi definitions, this can then be used to restore the current PmKpi MOs if needed. Then the kpidefinition file specified in the argument is used to generate a new set of PmKpi MOs which are then activated on the specified granularity.

**Arguments:**

- if no argument is specified then the command will only display the current PmKpi definitions with number of KPI counter instances that are currently in use and generate a kpidefinition file based on the existing PmKpi MOs.
- the first argument is the path of the kpidefinition file on the workstation, which will be used to generate a new set of PmKpi MOs.
- the second argument is the granularity in seconds: 300, 900, or 3600. In case this argument is omitted, 900 will be used as default.

**Options:**

- f: to force activate all PmKpi MOs on the specified granularity. Without this option, any already enabled PmKpi MOs will remain on their current granularity which may be different than the specified granularity.
- v: to validate a kpidefinitionfile
- d: to delete existing kpi definitions (no argument needed)

**4.4.16 pbl &lt;scan-filter&gt;|&lt;scan-proxy&gt;**

Suspend a scanner. This means that counters defined in this scanner will not be recorded in XML files each granuality period.

**4.4.17 pdeb &lt;scan-filter&gt;|&lt;scan-proxy&gt;**

Resume a scanner.

**4.4.18 pdel &lt;scan-filter&gt;|&lt;scan-proxy&gt;**

Delete a scanner.

Note: only statistics scanners can be deleted or created. Event scanners (GPEH/UETR/CTR) are fixed and can only be set.

**4.4.19 emom \[uetr|gpeh|ctr|all\] \[&lt;event-filter&gt;\]**

Display list of events available for each kind of event-based scanner (RNC/RBS only).

The event reference files are stored in **moshell/commonjars/eventfiles** and are SW dependent.

MoShell automatically chooses the appropriate version of the event files so the user does not have to worry about this.

**Examples:**

- emom u ranap - display all ranap related events for uetr
- emom all audit - display all events containing the word "audit" for all kind of event based scanners

**4.4.20 pset\[d\]**

Set the contents of an event-based scanner (RNC/RBS/LTE/ENB/MSRBS).

Following syntaxes apply:

- set filters for UETR/UETRACE:

pset\[d\] \[-s/-f &lt;ip&gt;:&lt;port&gt;\] &lt;scan-filter&gt;|&lt;scan-proxy&gt; &lt;event-filter&gt;|&lt;event-file&gt;|all &lt;imsi&gt;

- set filters for GPEH/CELLTRACE:

pset\[d\] \[-s/-f &lt;ip&gt;:&lt;port&gt;\] &lt;scan-filter&gt;|&lt;scan-proxy&gt; &lt;event-filter&gt;|&lt;event-file&gt;|all \[&lt;moGroup&gt;|&lt;moFilter&gt;|all\] \[&lt;ue-fraction&gt;\] \[&lt;filter&gt;=&lt;value&gt;\]

- set filters for CTR:

pset\[d\] \[-s/-f &lt;ip&gt;:&lt;port&gt;\] &lt;scan-filter&gt;|&lt;scan-proxy&gt; &lt;event-filter&gt;|&lt;event-file&gt;|all &lt;moGroup&gt;|&lt;moFilter&gt; \[&lt;trigger-event&gt;\]

Use the emom command to view the list of events that apply for each measurement type.

Event scanners UETR/CTR are applicable for RNC only; UETRACE/CELLTRACE are applicable to LTE eNB; GPEH scanners are applicable to RNC and WRBS only.

The first argument is the scanner name or scanner proxy.

The second argument indicates the list of events to include, either using regular expression matching or from a file containing one event on each line. It is possible to use negative filter (!) to exclude certain events.

The following fields are optional, if no value is entered (or all in the case of GPEH/CELLTRACE _utrancell-filter_), no filter will be sent to the node who will then use a default setting:

- _trigger-event_ default=RRC_RRC_CONNECTION_SETUP
- _ue-fraction_ default=200
- _utrancell-filter in GPEH/CELLTRACE_ default= all cells
- _filter_ additional filters, see the list below.

List of additional filters that can be specified at the end of the command line with the syntax &lt;filter&gt;=&lt;value&gt;:

- ASN1: true/false (CPP) or Include/Exclude (ECIM/COM). Only applicable for ENB.
- GUMMEI: list of gummei values separated by comma. Only applicable for ENB.
- PERIODICITY: one of 2,3,4,6,8,12,16,20,24,28,32,64 (value in seconds). If invalid value is given, then default will be 8 seconds. Only applicable for RNC RDT filters PREDEF.600XX.GPEH
- UE_POS_MEAS_VALIDITY: one of 0 (cellDch) or 2 (allStates). If invalid value is given, default will be 0. Only applicable for RNC RDT filters PREDEF.600XX.GPEH
- UERC: a list of UeRc numbers, eg 1-200. Any invalid or unsupported UeRc numbers will be automatically excluded from the filter. Only applicable for RNC RDT filters PREDEF.600XX.GPEH

For LTE eNB, the options -s/-f can be used to specify the output mode of the scanner:

- s: output mode STREAM
- f: output mode FILE_AND_STREAM

If these options are used then the ip address and port for the stream must be given as argument to the option, example: -f 10.12.45.38:3402. If these options are not specified the the output of the scanner will be to FILE only.

**Examples:**

- pset 10000 S1 cell=2A 300 - set a LTE CELLTRACE scanner for S1 events on cell=2A, UE fraction=300
- pset 4 X2 all ASN1=true GUMMEI=0x214365ABCD00,0x214365ABCD01 - set a LTE CELLTRACE scanner for X2 events on all cells with filter ASN1 and GUMMEI filters
- pset 20001 ranap cell=30456 - set a CTR scanner for ranap events on cell=30456 using the default triggering event
- pset 30006 all - set a GPEH scanner for all events using no cell filter and no ue-fraction filter. All cells will be selected and the default ue-fraction will be used (200).
- pset 30006 all all 1000 - set a GPEH scanner for all events on all cells using the ue-fraction 1000
- pset 30004 handover 304\[0-6\] 1000 - set a GPEH scanner for all events matching "handover" on cells 3040 to 3046 with ue-fraction=1000
- pset 30004 nbap mycellgroup - set a GPEH scanner for all nbap events on all cells of the MO-group _mycellgroup_
- pset 10002 rrc|nbap!connection 123456789012345 - set a UETR scanner on imsi 123456789012345, for all events matching "rrc" or "ranap" but not "connection".
- pset 30005 .!rrc_paging_type_1 - set a GPEH scanner for all events except RRC_PAGING_TYPE_1
- pset 30005 ~/myevents.txt - set a GPEH scanner for all events listed in /myevents.txt, no filter to be used for the cells nor the ue-fraction.
- pset 10004 -s 10.34.75.12:5443 . all 1000 - set a LTE CELLTRACE scanner for all events, without a cell filter and with UE fraction=1000, output stream to ip 10.34.75.12 and port 5443

•

pset 60000 ^measurement cell=iub-10 1000 PERIODICITY=4 UE_POS_MEAS_VALIDITY=2 UERC=22,24-25,100-200

\- set a RNC RDT scanner for all measurement events, on cell iub-10 with UE fraction 1000, periodicity 4 seconds

Note: The d option ("debug") can only be used on its own. The syntax of psetd is: psetd &lt;scanner&gt; &lt;event-file&gt; where the format of the event-file shall be as per above. The purpose of psetd is to test an event file and identify any events that are not supported by the node SW. The functionality of psetd is implemented as an moshell script, the script can be seen in moshell/commonjars/scripts/psetd.mos. The psetd command is called via an alias listed in the moshell file. Type alias to see the list of aliases. This shows that the user can define any new commands they need by adding an alias in the .moshellrc which will point to a script file. The parameters to the command will be sent to the script file via the positional parameters $1, $2, $3, etc. The variable $0 will be set to the whole line contents. See h run for info.

Note: For RBS GPEH, the _utrancell_ and _ue-fraction_ fields are not applicable. If the event-filter does not match any events, the RBS GPEH scanner will be set to empty.

# 5 Lazy

## 5.1 Software Upgrade CPP

Delete some old UpgradePackage if necessary to free up some disk space: del upgradepackage=&lt;oldpackage&gt; Create the UpgradePackage MO: cr swmanagement=1,upgradepackage=&lt;name&gt;

At the prompt, enter _FTP Server Address_ where the UP is stored and the path to the _UCF (Upgrade Control File)_. At the next prompts, enter FTP Server _UserID_ and _Password_, or just d for default value (will be **anonymous**) Perform the SW installation:

acc upgradepackage=&lt;name&gt;$ nonblockinginstall

Monitor installation progress:

polu

Perform the SW upgrade: acc upgradepackage=&lt;name&gt;$ rebootnodeupgrade

Monitor upgrade progress (confirmUpgrade will be done automatically): polu

Check that the new cv is using the new upgrade package

cvls

Note: if polu was not run after performing rebootnodeupgrade, the upgrade will have to be manually confirmed:

- get upgradepackage=&lt;name&gt;$ state —> wait until state "awaitingconfirmation"
- acc upgradepackage=&lt;name&gt;$ confirmupgrade

## 5.2 Software Upgrade ECIM/COM

Delete some old UpgradePackage if necessary to free up some disk space: del upgradepackage=&lt;oldpackage&gt; Create the UpgradePackage MO: acc swm=1 createupgradepackage

At the firt prompt, enter the URI from where to fetch the package, eg sftp://&lt;username&gt;@&lt;ipaddress&gt;/&lt;path&gt;

At the next prompt, enter the server password

Perform the SW installation:

acc upgradepackage=&lt;name&gt;$ prepare

Monitor installation progress:

polu

Perform the SW upgrade: acc upgradepackage=&lt;name&gt;$ activate

Monitor upgrade progress (confirmUpgrade will be done automatically): polu

Check that the new cv is using the new upgrade package

cvls

Note: if polu was not run after performing rebootnodeupgrade, the upgrade will have to be manually confirmed:

- get upgradepackage=&lt;name&gt;$ state —> wait until state "awaitingconfirmation"
- acc upgradepackage=&lt;name&gt;$ confirm

## 5.3 RNC Iub operations

- str - view state of all Iub/Cells/Channels/Nbap/Nodesynch in a table format (type h str for more info)
- bl/deb iublink=&lt;iubname&gt;$ - block/deblock an iublink
- bl/deb cell=&lt;cellname&gt; - block/deblock a cell
- str -i &lt;iubname&gt; - view states for sites related to a particular iub filter only

## 5.4 Common RNC Iub Integration Problems

When trying to integrate a new RBS, some data mismatch might cause the _Iub_, _Cell_, or _Channels_ not to come up. Things to check are the values of:

- Transmission
- AAL2 Addresses
- VCI values
- localCellId

Take a print of all MOs related to the Iub and check that the vci values match on both sides, check if any related MOs are down:

lk iublink=&lt;iub&gt; #in RNC lk iub=&lt;iub&gt; #in RBS

Find out the Aal2Ap used by that Iublink in RNC: lk iublink=&lt;iub&gt;

Check that the AAL2 addresses match on all sides:

get aal2routingcase=&lt;rbsroutingcase&gt; (in RNC and RXI) get aal2sp=1 (in RBS and RXI)

Check that the AAL2 path id’s match on both sides:

get aal2pathvcctp=&lt;pathname&gt; pathid (in RNC, RBS, and RXI if applicable)

Check that the aal2 continuitycheck match on both sides:

get aal2pathvcctp=&lt;pathname&gt; continu (in RNC, RBS, and RXI if applicable)

Check that localcellid match on both sides:

get cell=&lt;cell&gt; local (in RBS and RNC)

Perform a loopback test on all VCIs of that iub, to see if transmission is ok

lacc atmport=&lt;port&gt;,vpltp=&lt;vp&gt;,vpctp=1,vcl eteloopback Check RNC/RBS alarms

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

Take a print of all MOs related to the Iu and check that the VCI values match on both sides. Also check if any related MOs are down: lk mtp3bsrs=&lt;name&gt;

Perform a loopback test on all VCs of that interface, to see if transmission is OK: lacc atmport=&lt;port&gt;,vpltp=&lt;vp&gt;, eteloopback Check that the pointcodes matches on both sides

get mtp code

Activate/deactivate a C7 link

lacc mtp3bsls=&lt;name&gt;, deactivate/activate

Block/deblock an Aal2Path, check that the _pathId_s and _a2ea_ addresses match on both sides:

bl/deb aal2pathvcctp=&lt;pathname&gt; get aal2pathvcctp=&lt;pathname&gt; pathid get routingcase=&lt;name&gt;

# 6 Scripting

Moshell supports the use of variables and logical constructs. These can be used directly from the command line or within MoShell command files.

## 6.1 Preset Variables

The following variables are set immediately after MoShell startup:

- $logdir - path to the **moshell_logfiles/logs_moshell** directory
- $moshelldir - path to the moshell directory
- $gawk - path to gawk
- $ipaddress - IP address of the node that MoShell is connected to
- $moshell_version - the MoShell version
- $tempdir - path to the directory containing all temporary files for this moshell session. Gets deleted at the end of the session.
- $uname - output from the "uname -a" command, showing the operating system of the workstation running moshell.

The following variables are set after the MOM has been parsed:

- $momversion - the MOM version of the node (eg: RNC_NODE_MODEL_E_5_3, MGW_NODE_MODEL_R3_9_0)
- $cellomomversion - the CPP MOM version (3.3, 4.3, 5.1, etc) of the node
- $momdocnumber and $momdocrevision - the document number and revision of the MOM (eg: 15554-AXD10503/1 , rev: Z1)
- $background_pid - the process id of a process started into background from moshell command line, eg: l $moncommand > $logfile &
- $rats - the list of RATs supported by the node, eg G, L, W, N. Looks for presence of MOs such as BtsFunction=1, ENodeBFunction=1, etc. Set after running lt all.
- $gnbfunctions - the list of NR functions supported by the node, eg C (CUCP), U (CUUP), D (DU) . Set after running lt all.
- $ratsconfig - the LTE/NR deployment scenario (eg: TDD/FDD, LB/HB/MB). Set after running "cvls" .

These variables can be handy to have when a script needs to know what SW revision is running in the node or what kind of node it is.

The following variables are set after running certain MO commands:

- $mibprefix the MibPrefix of the FDN. Eg: SubNetwork=OSS,SubNetwork=RNC1,MeContext=RBS3
- $cppversion the CPP version of the node, according to the information in the current UpgradePackage.
- $nr_of_mos the number of MOs that were printed on screen by the last run of the pr/st/get/prod/fro/set/del/acc commands.
- $nr_of_mos_ok the number of MOs that were successfully operated upon by the last run of the set/del/acc commands.
- $command_result set after running the cr/pcr/pset/trun commands. Possible values: 0 for success, 1 for failure.
- $returncode set after running any moshell command. Possible values: 0 for success, 1 for failure.
- $action_result set after running the acc command. Contains the return value of the action.
- $nr_of_alarms the number of active alarms on the node. Set after the last run of the al command.
- $nr_of_cvs the number of CV:s that exist on the node, is set after the last run of the cvls command.
- $nr_of_scanners the number of scanners printed by the last run of the pst/pgets/pdel/pbl/pdeb commands.
- $nr_of_counter_instances the number of counter instances printed by the last run of the pgetsn command.
- $moncommand the command to start the monitor client after having run the "mon" command.

The following variables are set after running the commands bp/bo:

- $coremp_pos the positions of the core MPs, eg: 001000:001100
- $coremp_type the board types of the core MPs, eg: GPB53:GPB53
- $coremp_hw the HW platform of MSRBS Baseband board, eg G2, G3.0, G3.1, G4
- $nr_of_boards the number of boards belonging to a board group

The following variables are set after running the cvcu/cvls command:

- $nr_of_cvs the number of CV’s that exist on the node.
- $currentUP the product number and revision of the UpgradePackage shown in the field "Current UpgradePkg"
- $currentSW the release name (eg L17A.3) of the UpgradePackage shown in the field "Current UpgradePkg"
- $swName the product name of the active SwVersion (eg MSRBS, vRC, vPP, etc). Usually corresponds to the node type. Only applicable to COM nodes.

The following variables are set after running one of the l+/u+/u-/u!/diff commands:

- $logfile the logfile that is currently open. Set immediately after executing the l+ command, stays set even after l- and will only be reset the next time a new logfile is open with l+
- $undologfile the logfile used by the undo command. Set immediately after executing the u+/u+s command, stays set even after u- and will only be reset the next time a new undo mode is started with u+/u+s.
- $undocommandfile the command file that can be used to undo the commands that were run between u+/u+s and u-. Set immediately after executing the u- command.
- $undodelcommandfile - the file containing the delete commands. Only applicable to simulated undo mode u+s
- $undotrunfile / $undoxmlfile - the path of the file generated by the u! command
- $diffcsvfile / $diffcmdfile - the path of the result file and command file generated by the diff command

The following variable is set after having logged on to the node via telnet/SSH or FTP/SFTP.

- $password

The contents of the variable can not be printed, it will only show if it’s empty or not. By setting this variable to empty (by doing: $password = ), this will force MoShell to check the password again. Useful in case the password has changed on the node during the MoShell session.

The $nr_of_vars variable is set after running the pv command.

This variable indicates the number of scripting variables that were printed in the last pv printout. By using pv together with a filtering pattern (eg: pv $table), it is possible to find out the number of variables that had matched the pattern, for instance the number of elements in a hashtable.

The $nr_of_lines variable is set after using the functions "readfile" or "testfile".

After using the function "testfile", this variable is set to 0 if the file does not exist and to 1 if the file exists.

After using the function "readfile", this variable is set to 0 if the file does not exist and to the number of liens in the file if the file exists. The difference between testfile and readfile is that testfile won’t actually read the file, it will just check if the file exists whereas readfile will test the file, then read it.

Example1:

$lineContent = testfile(/path/to/myfile) if $nr_of_lines = 0 l echo "File not found!" return fi

Example2:

$lineContent = readfile(/path/to/myfile) if $nr_of_lines = 0 l echo "File not found!" return fi for $lineNumber = 1 to $nr_of_lines if $lineContent\[$lineNumber\] ~ thispattern print We found it! The line is $lineNumber.

return fi done

Example (list all scripting variables currently set via pv):

- $logdir = /home/eanzmagn/moshell_logfiles/logs_moshell
- $momversion = RNC_NODE_MODEL_E_5_3
- $moshelldir = /home/eanzmagn/tools/moshell
- $cellomomversion = 4.3.1
- $gawk = /home/eanzmagn/tools/moshell/gawk
- $ipdaddress = 10.1.128.17
- $moshell_version = 6.1
- $nr_of_mos = 1
- $password = \*\*\*\*\*\*\*

## 6.2 Variable assignment

A variable value can be assigned in six ways, see below.

A variable can also be unassigned, using the unset command.

By using the command unset small, all variables are unset, except:

- the "system" variables ($gawk, $ipaddress, $password, $moshell_version, $moshelldir, $logdir, $momversion, $cellomomversion)
- the "global" variable(s) (ie: assigned with the ":=" sign, instead of "=").

By using the command unset all, all variables are unset except the "system" variables.

NOTE: It is always good practice to unset a variable as soon as it is not needed anymore since having too many variables defined slows down the processing of the command line. It is also good to do unset all at the beginning and end of a command file (and before doing the return command) in order to avoid interference from un-needed variables. See the script examples in **moshell/commonjars/scripts**

To print all currently assigned variables, use the command printvar. To just print one variable, type: pv &lt;pattern&gt; (where the pattern matches the variable(s) to print)

print "$variable"

The variable value can be assigned in six ways:

1.  From the command line.

The variable to be assigned is on the left side of the equal sign and the value is on the right side. Each element must be separated by spaces. Example:

$i = 3

$node = RNC

$password =

By running password = this sets the password to an empty value and will force MoShell to ask for the password again.

1.  At moshell startup, using the -v option. In this case, the "$" sign should be omitted. (otherwise it gets interpreted by the Unix shell) Example: moshell -v upmo=CXP9011008_R1A03,ftpserv=10.1.0.16,secure_shell=1,secure_ftp=1 rnc34}

In this case, we can see that scripting variables ($upmo and $ftpserv) and user variables (secure_shell and secure_ftp) have been mixed in the same statement. This is OK because any variable that is not recognised as a user variable will be treated as a scripting variable.

1.  From the following commands: get, pget, fro, ip2d/d2ip, h2d/d2h, uv

The mo-filter and attribute-filter must be specified, then comes the redirection sign (>), then the variable name. If several attributes are printed, only the last attribute value gets assigned into the variable. Examples:

- 1.  get 0 productName > $nodeType (result: $nodeType = RBS3202)
    2.  get ethernetlink ipaddress > $ipaddress (result: $ipaddress = 10.1.128.17)
    3.  On CPP node: get configurationversion currentupgrade > $currentUp (result: $currentUp = UpgradePackage=CXP9011123_R12F)
    4.  get $currentUp administrativedata > $swRev (result: $swRev = Struct{5} >>> 1.productNumber = CXP9011123 >>> 2.productRevision = R12F etc.)
    5.  pget EUtranCellFDD=1 pmRaSuccCbra > $pmra (result: $pmra = 157)
    6.  lfro subrack=ms,slot=1,pluginunit=1$ ^r > $froid (result: $froid = 0)
    7.  d2ip -4127129085 > $ip_addr (result: $ip_addr = 10.1.2.3)
    8.  h2d 0xa > $res (result: $res = 10)
    9.  uv ^credential > $credential (result: /home/ericsson/moshell/commonjars/host.p12)

1.  Using an arithmetic operation

The following numeric operations are supported:

- - - **\+** addition
        - **\-** substraction
        - **\*** muliplication
        - **/** division
        - **% modulo** (returns the remainder of an integer division operation)

**Examples:**

- 1.  $i = 1 (result: $i=1)
    2.  $i = $i + 1 (result: $i=2)
    3.  $j = $i \* 3 (result: $j=6)
    4.  $k = $i \* $j (result: $k=12)
    5.  $l = $i / $j (result: $l=0.333)
    6.  $m = $k % 5 (result: $m=2)

Note: Only one operation per line is allowed. A space must exist between each element of the operation. There cannot be more than two members in the operation (ie: $i = $j + $k ==> OK. But $i = $j + $k + $l ===> NOTOK)

1.  Using the output from a Unix command:

The Unix command must be surrounded by back-quotes (‘). Variables can be used within the Unix command. Examples:

• Example

$date = ‘date +%y%m%d-%H%M‘ (result: $date = 040930-1745) get ethernetlink ipaddress > $ipaddress

(result: $ipaddress = 10.1.128.17)

$logfile = $ipaddress_$date.log

(result: $logfile = 10.1.128.17_040930-1745.log) l+m $logfile

(open a logfile, don’t display anything on the screen) te log read l-

(close logfile)

$errors = ‘grep -c ERROR $logfile‘

(result: $errors = the number of ERRORs found in the logfile) l rm $logfile

(remove the logfile)

• Example: Making a cv that has the same name as the current startable cv but the last digit is incremented by 1

lt configurationversion get configuration startable > $startable (result: $startable = RBS3045_P2.1.5_CU3_A_01) $cvname = ‘$gawk -v cvname=$startable ’BEGIN { print gensub(/..$/,"",1,cvname) sprintf("%02s",substr(cvname,length(cvname)-1)+1) }’‘ cvms $cvname

(result: $cvname = RBS3045_P2.1.5_CU3_A_02)

1.  Using result from a unix command

If the built-in function system is used instead of the back-quotes (‘) then the exit code of the unix command is saved to the variable (instead of its output).

Example:

$result = system(cp $file1 $file2)

(result: 0 if the copy was successful, or some other number if the copy failed)

1.  Using String manipulation

The following string operations are supported: _concatenation_ and _substitution_ / _replacement_.

The concatenation is performed by juxtaposing the strings. Syntax for concatenation: $var = string1string2string3 (the strings are concatenated without space in between) or $var = string1 string2 string3 (the strings are concatenated with spaces in between)

Syntax for concatenation:

- 1.  $var = string1string2string3 (the strings are concatenated without space in between)
    2.  $var = string1 string2 string3 (the strings are concatenated with spaces in between)

The substitution/replacement is performed using the -s switch to specify the string to substitute and the -r switch to specify the string it should be replaced with. If the -r switch is not used, then the string will be replaced by nothing. If the -g switch is specified, then all instances of the string to substituted, otherwise, only the first instance.

Syntax for substitution/replacement:

a) $var = origString -s strToSubstitute \[-r strToReplaceItWith \[-g\]\] Regular expressions can be used in the string manipulations. Examples:

$var = abc_defabc ghi

$var1 = $var -s abc

Result: $var1 = \_defabc ghi, only first instance of **abc** was replaced

$var2 = $var -s \\x20

Result: $var2 = abc_defabcghi, the space sign was removed

$var3 = $var -s abc -g

Result: $var3 = \_def ghi, all instances of **abc** were replaced

$var4 = $var -s abc -r xyz

(result: $var4 = xyz_defabc ghi, first instance of **abc** was replaced)

$var5 = $var -s abc -r xyz -g

(result: $var5 = xyz_defxyz ghi, all instances of **abc** were replaced with **xyz**)

$var6 = $var -s a.\*c -r xyz

(result: $var6 = xyz ghi, the regular expression **a.\*c** was replaced with **xyz**)

$var7 = $varABC$var6

(result: $var7 = abc_defabc ghiABCxyz ghi, the three strings **$var**, **ABC** and **$var6** have been concatenated)

$var8 = $var ABC $var6

(result: $var8 = abc_defabc ghi ABCxyz ghi, there are spaces in between the three strings)

Note: if more advanced string manipulation is needed, it is always possible to use an external program such as gawk to do the string manipulation. See the example above about using Unix programs.

8\. Using output from a predefined function

Currently, the following functions exist:

- fdn(proxy) input is the proxy id, output is the FDN
- ldn(proxy) input is the proxy id, output is the LDN
- rdn(proxy) input is the proxy id, output is the RDN
- motype(proxy) input is the proxy id, output is the MO type
- proxy(string) input is the LDN or FDN (NOT RDN!), output is the proxy id
- readinput(string) input is a prompt that should appear on the screen, so that the user can input an answer which will then be assigned to the variable.
- readinputsilent(string) same as readinput() but without echoing the user input. useful for entering passwords.
- readfile(file) input is a filename. Each line of the file is assigned into an element of the hashtable into which we have assigned the result of the function. If the file is not found, the variable $nr_of_lines is set to 0, otherwise it is set to the number of lines in the file. Note, this should not be used on large files as it will slow down things very much.
- testfile(file) input is a filename. If the file is not found, the variable $nr_of_lines is set to 0, otherwise it is set to 1.
- testzip(zipfile) input is a filename. If the file is a valid zipfile, the function returns 1. If the file is tarfile (but with .zip at the end, eg a CV.zip generated from EvoC8300), then the function returns 2. Else (file not found or zipfile corrupted), the function returns 0.
- split(string) The string is split into the array specified on the left side of the equal sign (see example below). The separator used to split the string can be specified in the variable "$split_separator". By default it is a space. If the

$split_separator has been changed and needs to be reset to the default value, just run the command "unset

$split_separator". The number of elements in the array is stored in the variable $split_last

- mod2nr(string) Convert a RncModule name into a module number. Eg: mod2nr(MS-6-1) returns 1061 , mod2nr(ES-1-24-0) returns 241 .
- check_ip_contact(ipaddress,port) Check connectivity to a given ip address and tcp port. Returns 0 if ok, or 1 if not ok.
- asort($table,$sortedtable) Creates a new table $sortedtable containing the values of an existing table $table, sorted in ascending alphanumerical order. The function returns the number of elements in $sortedtable.

Usage: $n = asort($table,$sortedtable) . See example 5 below.

Example 1:

lt iublink ma iub iub for $mo in iub $mordn = rdn($mo) if $mordn ~ 1023 lcc $mordn lbl $mordn, fi done

Example 2:

$var = readinput(Please confirm \[y/n\]: ) if $var !~ ^y return fi

Example 3:

$table = readfile(/path/to/myfile) for $lineNumber = 1 to $nr_of_lines print $table\[$lineNumber\]

$word = split($table\[$lineNumber\]) if $word\[1\] ~ ^#

$nr_of_comments = $nr_of_comments + 1 fi unset $word unset $table\[$lineNumber\] done

(Note: by unsetting the entry we’ve just read - provided we don’t need it anymore - will make things faster)

Example 4:

Logging in to an unknown node with moshell -n option (no ip connectivity check) and checking the type of node The loop is intended to keep checking if the node happens to be down at the time of the check.

for 10

$var80 = check_ip_contact($ipaddress,80)

$var9830 = check_ip_contact($ipaddress,9830)

$var4912 = check_ip_contact($ipaddress,4192) if $var4192 = ok uv comcli=21 uv username=expert $password = expert break else if $var9830 = ok uv comcli=11 uv username=root $password = root break

else if $var80 = ok uv comcli=0 break else wait 30

$i = $i + 1

fi done

Example 5:

A table $t is defined with following values: $t\[0\]=2 ; $t\[1\]=bye ; $t\[a\]=3 ; $t\[b\]=hello

Execute the command: $n = asort($t,$s)

This will return $n=4 and define a table $s with values: $s\[1\]=2 ; $s\[2\]=3 ; $s\[3\]=bye ; $s\[4\]=hello Example: The purpose of the little moshell script below is to make a customized CV name like: date_nodeType_swRev

cvls

$date = ‘date +%y%m%d‘ (result: $date = 040930) get 0 productName > $nodeType (result: $nodeType = RBS3202) $nodeType = $nodeType -s RBS (result: $nodeType = 3202) get configurationversion currentupgrade > $currentUp (result: $currentUp = UpgradePackage=CXP901913%2_R12N) get $currentUp administrativedata > $swRev

(result: $swRev = Struct{5} >>> 1.productNumber = CXP901913/2 >>>

2.productRevision = R12N >>> 3.productName = CXP901913%2_R12N ....)

$swRev=‘gawk -v currentsw="$swRev" ’BEGIN{ swrev=gensub(/\\r|\\n/,"","g",currentsw); print gensub(/^.\*Revision = | >>> 3.product.\*$/,"","g",swrev) }’‘

(result: $swRev = R12N)

cvms $date_$nodeType_$swRev (result: cvms 040930_3202_R12N )

## 6.3 Hashtables (arrays)

The index and the value of the hashtable can be a variable, a constant, or a mix of both.

All variable assignment methods described in Section 6.2 apply for assigning values into hashtables as well.

To print a hashtable, do: pv &lt;table&gt; **Examples:**

Assigning constants into a hashtable

\>> $table\[1\] = hello

\>> $table\[2\] = hej

\>> $table\[hoho\] = 5

\>> pv tab (result printout:)

$table\[hoho\] = 5

$table\[1\] = hello

$table\[2\] = hej

Assigning variables into a hashtable:

\>> $mo = AtmPort=MS-6-1

\>> $proxy = proxy($mo)

\>> $proxylist\[$mo\] = $proxy

\>> $mo = AtmPort=MS-6-2

\>> $proxy = proxy($mo)

\>> $proxylist\[$mo\] = $proxy

\>> pv proxylist (result printout:)

$proxylist\[AtmPort=MS-6-1\] = 103

$proxylist\[AtmPort=MS-6-2\] = 112

More examples on how to use hashtables are described in Section 6.5.

## 6.4 If/Else constructs

The if statement must be followed by a _condition_. The comparison operator of the condition must be surrounded by spaces. Zero or more else if statements can be used after the if statement. Zero or one else statements can be after the if or else if statements.

The end of the if/else structure must be specified with a fi statement. Each statement must be on its own line and can be followed by one or more commands. Several conditions can be combined, using the logical AND (&&), or the logical OR (||). Any number of AND/OR can be put on a line but NOT BOTH on the same line.

Grouping conditions with brackets is NOT supported.

The return command can be used to exit from the command file in case a certain condition is met. Type h return for more information on how to use this command.

Syntax examples:

1.  if &lt;condition&gt; command1 command2 fi
2.  if &lt;condition1&gt; || &lt;condition2&gt; command1 command2 else command3 fi
3.  if &lt;condition&gt; && &lt;condition2&gt; && &lt;condition3&gt; command1 else if &lt;condition4&gt; command2 else command3 fi

A condition can use the following comparison operators:

- \= equals
- ~ matches (as in pattern match)
- != is not equal to
- !~ does not match
- \> greater than
- < less than
- \>= greater than or equal to
- <= less than or equal to

The words around the operator can be either a variable or a single word but NOT a string containing spaces or a concatenation of a variable and string. Following conditions are syntaxically correct:

if $var1 = $var2 if mystring ~ $var if 10 > 3 if $i < 2

Following conditions are NOT syntaxically correct and will return unexpected results:

if mystring_$var1 ~ $var2 if mystring is this ~ your string

A condition can also just contain one variable, in which case it will check if the variables exists. The words around the operator can be either a variable or a single word but NOT a string containing spaces or a concatenation of a variable and string. Following conditions are syntaxically correct:

if $var1 = $var2 if mystring ~ $var if 10 > 3 if $i < 2

Following conditions are NOT syntaxically correct and will return unexpected results:

if mystring_$var1 ~ $var2 if mystring is this ~ your string

A condition can also just contain one variable, in which case it will check if the variables exists.

Example to check if a variable $var exists. If $ exists (i.e. has any value set) then it will do something..

if $var ...do something fi

Example to check for node type and see attenuation accordingly:

get 0 productname > $nodeType

if $nodeType ~ 3202 || $nodeType ~ 3104 get feeder attenuation set feeder attenuation 4 else if $nodeType ~ 3101 get feeder attenuation set feeder attenuation 16 else

get feeder attenuation fi

## 6.5 For constructs

The parameter to the for construct can be:

1.  ever - to repeat the loop an infinite number of times
2.  &lt;numberOfIterations&gt; - to repeat the loop a specific number of times
3.  $mo in &lt;moGroup&gt; - to run the body of the loop on each MO of the specified moGroup. MO groups are created using ma/lma. See h ma (Section 4.1.10) for more info.
4.  $board in &lt;boardGoup&gt; - to run the body of the loop on each board of the specified board group. Board groups are crated using ba/ba. See h bo (Section 4.3.18) for more info.
5.  $var in $table for each iteration of the loop, $var will cycle through the index values of the hashtable $table
6.  $var = $start to $stop$var is assigned every integer value between $start and $stop. $start and $stop can be variables or constants but must be an integer. If $start is smaller than $stop than the order will be ascending, otherwise it will be descending.

The end of the for structure must be specified with a done statement.

The wait command can be used in the body of the loop to specify a delay to wait in between each iteration. The delay can be in seconds, minutes, hours, or even ROP periods. (Type h wait, Section 4.3.53 for info.)

Do not use the sleep command as this will result in hanging if the loop is aborted.

The loop can be aborted any time by typing ctrl-z , then touch &lt;stopfile&gt;, then fg. The &lt;stopfile&gt; path is shown in the window title bar. Type h ctrl-z for more info about aborting.

The break command can be used within the loop to exit from the loop.

Note: Regardless of where the break is located in the loop, the current loop iteration will be completed before breaking out of the loop.

Syntax examples:

1.  for ever command1 command2 done
2.  for &lt;numberOfTimes&gt; command1 wait &lt;numberOfSeconds&gt; done
3.  for $mo in &lt;moGroup&gt; get $mo &lt;attribute&gt; > $variable $variable1 = ....

set $mo &lt;attribute&gt; $variable1 etc... done

1.  for $board in &lt;boardGroup&gt; bl $board facc $board restart 0 1 wait 10 deb $board lhsh $board vii done
2.  for $proxy in $proxytable bl $proxy st $proxy deb $proxy st $proxy

get $proxy operational > $opstate if $opstate != 1 break fi done

1.  for $var = $maxproxy to $minproxy del $var done

for $var = 1 to 6

te e trace$min process done

Practical examples:

1\. Checking the progress of a UP installation, every 10 seconds. Break from the loop if the result is

1 (INSTALL_COMPLETED), and continue with upgrade action. Abort the command file if the result is

6 (INSTALL_NOT_COMPLETED)

lt upgrade acc upgradepackage=xxx nonblockinginstall for ever $return = 0

wait 10 get upgradepackage=xxx state > $upstate if $upstate ~ ^1 break else if $upstate ~ ^6 $return = 1 break fi done

if $return = 1

return fi

acc upgradepackage=xxx upgrade

1.  Run a testcase 50 times

for 50 run testcase_3.1.1.cmd wait 2m done

1.  Increase the primaryCpichPower by 0.1 dBm on each UtranCell

lt ^utrancell ma cell ^utrancell for $mo in cell get $mo primarycpichpower $pich

$pich = $pich + 1 set $mo primarycpichpower $pich done

1.  restart all boards in a board group

ba spb spb for $board in spb facc $board restart 0 1 done

1.  Save the fRO values of all programs into a table and then restart every program

lma programs_on_slot_19 subrack=ms,slot=19,.\*program for $prog in programs_on_slot_19

$i = $i + 1

fro $prog ^res > $frolist\[$i\] done

for $fro in $frolist restartObj pgm $fro done

1.  Restart some boards in a specific order

for $var = 20 to 14 $board = 00$var00 facc $board restart 0 1 done

## 6.6 User-defined functions

Users can define their own functions, using the func/endfunc construct.

If the function is called with arguments, these are assigned to the variables $1, $2, $3, etc The variable $0 is set to the whole line contents.

Example:

1\. Define the function (the function definitions can be run in a different command file)

Here we are defining a function which checks the state of the mirrored disks and returns once the disks are in sync

func check_disk_state

#if $1 is undefined or different to an integer value

#then we set it to 10 seconds

if $1 ~ ^\[0-9\]+$ $wait_interval = $1 else

$wait_interval = 10 fi for ever wait $wait_interval l+om $tempdir/diskstate lh coremp mirror s l-

$res = ‘grep -c "Peer Disk Status: \*Valid" $tempdir/diskstate if $res > 0

break fi done endfunc

func waitforuser

$date = ‘date "+%Y-%m-%d %H:%M:%S"‘ for ever

$reply = readinput(Waiting from \[$date\]. Type "y" when ready: ) if $reply ~ ^\[yY\] break fi done

$date = ‘date "+%Y-%m-%d %H:%M:%S"‘ print "Finished waiting at \[$date\]" endfunc endfunc

2\. Call the function Here we have made a small script which makes use of our user-defined function.

First we are running a file containing all the definitions for our user-defined functions.

(Note that the functions can also be defined within the same script, but by keeping all functions in a separate file means that several command files can use the same functions)

We have called the function check_disk_state with an argument "5" which in this case will be used as the

"$wait_interval" parameter in the function

run ~/myfunctions_define.mos for ever check_disk_state 5 waitforuser facc 0 manualrestart 0 0 0 pol done

## 6.7 Nesting for and if statements

It is possible to nest one or more if/else statement within a loop statement and vice-versa. But it is currently not possible to nest an if/else statement within an if/else statement and a loop statement within another loop statement.

The current workaround is to put the for/if constructs into functions. See Section 6.6 for more info on functions.

Example:

The following script starts the install, then checks the state of the install every 10 seconds. Once the upgradepackage is installed, it starts the upgrade. Then it checks the state again and once the upgrade is in state **awaitingconfirm**, it confirms the upgrade.

$UP = upgradepackage=CXP9011123_R12F acc $UP nonblockinginstall for ever wait 10 get $UP state > $state if $state ~ ^1

break fi done get $UP state > $state if $state ~ ^1

acc $UP upgrade fi wait 120 for ever wait 10 get $UP state > $state if $state ~ ^3

break fi done

if $state ~ ^3 acc $UP confirmupgrade fi

Some more examples:

1.  Example to check the mirror stat status of the node (i.e. to check whether the passive FTC MP is ready to take over or not)

for ever board_status -d 00 10 -c "mirror stat" | tee tmpfile.tmp board_status -d 00 11 -c "mirror stat" | tee -a tmpfile.tmp $tmp = ‘grep -c "Peer Disk Status: Valid" tmpfile.tmp‘ if $tmp > 0

break else wait 60 fi done

1.  Example to check if an upgrade is complete (i.e. the upgradepackage is in state 3)

wait 300 #give it some time to run first for ever pol 1 1

get upgradepackage=mypkg state > $state if $state ~ ^1 break #upgrade failed else if $state ~ ^3 break #upgrade complete fi wait 60 done

## 6.8 Example scripts

Example scripts can be found under **moshell/commonjars/scripts** and **moshell/examples/scripting/**

Note two types of comments can be used in scripts:

- _visible comments_ start with the "#" sign. These comments are printed on the screen while the script is executing.
- _invisible comments_ start with the "//" sign. These comments are not printed on the screen.

# 7 Utilities

The below two utilities are separate from moshell and shall be run stand-alone:

- mobatch: to execute a number of moshell sessions to multiple nodes in parallel. Type "/path/to/moshell/mobatch" on its own for help.
- pstool: to list or manage moshell processes on the workstation. Type "/path/to/moshell/pstool" on its own for help. More info about pstool is mentionned in chapter 8.

Regarding mobatch:

The list of nodes on which to perform the operations shall be stored in a file called the "sitefile".

The ip-addresses/DNS-names and passwords of all nodes of the network must be stored in a reference file called the "ipdatabase".

The ipdatabase uses the following syntax:

&lt;nodeName&gt; &lt;nodeIpAddress&gt;|&lt;nodeDNSAddess&gt; &lt;nodePassword&gt;|&lt;dummytext&gt; \[&lt;uservariables&gt;\] An example of a sitefile and an ipdatabase can be found in moshell/examples/mobatch_files .

# 8 Server Maintenance

When running moshell on a server in a multi-user environment, there needs to be regular maintenance in order to clean up the disk and any hanging processes.

## 8.1 Hanging Processes

A known bug of moshell is that it doesn’t always shut down all of its spawned processes upon exiting which leads to CPU overload and run out of RAM memory. This problem should now be fixed thanks to the use of various timeouts but if this does not help, then it is recommended to regularly check the rogue processes using the unix command top.

Once the top command is running, you can type the following commands in the top screen:

- - n followed by the number of processes to display (e.g n 40) -> to show more than the default number of 15 processes
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

# 9 Modes of operation

The list of commands that are supported in a specific mode can then be printed with the "h" command.

E.g. if connected in offline mode, the "h" printout will show only the commands that are applicable in this particular mode. Type "h &lt;command&gt;" for information on a specific command.

## 9.1 Offline Mode

The offline mode allows to run an moshell session against a modump.zip (collected with command "dcgk") or dcgm.zip (collected with command "dcgm").

When running moshell commands in offline mode, all information is from the zipfile, no communication is taking place with the node.

## 9.2 SQL Mode for CPP Nodes

The SQL mode allows to run an offline moshell session against the configuration database of a CPP node (db.dat, zipped CV, or dbdump).

- The db.dat file can be fetched using the ftget command, eg: ftget /d/configuration/cv/&lt;cvname&gt;/db.dat
- The CV can be fetched using the "cvget" command, eg: cvget &lt;cvname&gt;
- The dbdump can be fetched with the "cvgetd" command, eg: cvgetd &lt;cvname&gt;

To start moshell in SQL mode, use option -d, eg: moshell -d &lt;cv.zip&gt;, moshell -d &lt;db.dat&gt;, or moshell -d &lt;dbdump.zip&gt;

Moshell then opens an SQL client session to the file and loads all the MO data into memory.

To prevent loading MO data (for faster startup time), use the option -v nomo=1. Only sql commands will then be available. Note that the MO data when read from a CV/db.dat/dbdump only contains the MO configuration attributes, not the MO state attributes.

During startup, moshell also performs a consistency check on the various SQL tables of the database, to detect if there are any inconsistencies or corruptions.

Currently not all moshell commands are supported in SQL mode, type h at the moshell prompt to see the list of supported moshell commands.

It is also possible to run sql commands directly, e.g. sql select \* from tables.

## 9.3 Multi Mode for CPP Nodes

The multi mode allows an moshell session to be connect to several nodes CPP at the same time.

The command syntax for starting moshell in multi mode is: moshell -m &lt;sitelist&gt;|&lt;sitefile&gt;

The sitelist consists of a comma separated list containing all the node names or ip/dns addresses.

The sitefile is a text file containing the list of nodes names or ipaddresses, on node per line.

Example:

- moshell -m rnc2,10.1.128.17,rbs34,rxi2.ericsson.se,mgw3
- moshell -m /path/to/sitefile

If node names are used, they must be defined in the ipdatabase. For more information about ipdatabase and sitefile, see the help of the mobatch utility by typing "mobatch" from the unix prompt.

To print the list of commands which are supported in multi-mode, type h at the moshell prompt.

More information about a specific command can be obtained by typing h &lt;command&gt;.

The multi mode is primarily geared towards commands that use the corba services CS/FM/PM.

Moshell commands that access the node via telnet/ssh/ftp/sftp are currently not supported in multi mode.

When moshell is running in multi mode, a prefix is appended in front of certain objects in order to distinguish between different nodes and MOM versions:

- the RDN/LDN in MO commands are prefixed with the string "Me=&lt;nodename&gt;".
- the scanner names in PM commands are prefixed with the node name.
- the MO class in mom/pmom command are prefixed with the MOM version.

MOM handling in multimode:

- at startup, the MOM version of each node is checked, so it is supported to connect to nodes running different MOM versions.
- it is also possible to skip the MOM check by parsing a MOM file with the parsemom command. Then all nodes will use the same MOM, which may have unexpected effects.

**Known limitations in multi mode**

- u+, emom, pset: currently only work when all nodes have the same MOM version.
- u!: conversion of .mos to .mo script does not work correctly yet. Avoid using the u! command in multimode.
- pol: options (c/h/s/u) not supported in multimode. Syntax is: pol &lt;node&gt;. E.g: pol rnc2
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
    - "lt &lt;motype&gt;" : to load all MO instances of a particular class. Eg: lt nrcelldu -> loads all MO instances of class

"NRCellDU"

- - "ltc &lt;motype&gt;": to load all MO instances of a particular class and all the underlying children MOs. Eg: ltc gnbdufunction -> loads the GNBDUFunction MO and all underlying children MOs.
- MO LDNs are prefixed with the string "Me=&lt;nodename&gt;" in order to distinguish MO instances from different nodes in the same session. This prefix is always used, even in single-node sessions.
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

# 10 Revision History

The revision history has been moved into a file called **ReleaseHistory.txt** in the moshell directory.