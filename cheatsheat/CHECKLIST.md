```
export IP=
```

# Decouverte

## nmap

```
nmap -sC -sV -oA nmap/initial -vv $IP
```

# Crawler Web

## gobuster

```
gobuster dir -u $IP -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x php,php3,html,py,css,asp
```

## nikto

```
nikto -h http://$IP | tee nikto.log
```

## User-Agent

### UA-Tester (peu convaincant)

https://code.google.com/archive/p/ua-tester/downloads

https://github.com/amenezes/ua-tester

Tourne en python2

## proxy web 

### Burp Suite


# Brute Force

## Hydra

```
hydra -l chris -P rockyou.txt $IP ftp -t 20
```

## John The Ripper

Il faut creer un fichier de hash pour john par example pour un zip:

```
zip2john monfichier.zip > crack.john
john crack.john
```

# Analyse de fichier

## exiftools

## binwalk

```
binwalk fichier
binwalk -e fichier #extraction
```

## strings

## gdb
 * https://reverseengineering.stackexchange.com/questions/3815/reversing-elf-64-bit-lsb-executable-x86-64-gdb

```
readelf -h DearQA.DearQA 
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x400590
  Start of program headers:          64 (bytes into file)
  Start of section headers:          5792 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         8
  Size of section headers:           64 (bytes)
  Number of section headers:         30
  Section header string table index: 27
```
Ouverture avec gdb en utilisant le point d'entrée **0x400590**.

```
gdb DearQA.DearQA        
GNU gdb (Debian 10.1-2) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from DearQA.DearQA...
(No debugging symbols found in DearQA.DearQA)
(gdb) break *0x400590
Breakpoint 1 at 0x400590
(gdb) run
Starting program: /home/kali/tryhackme/dearqa/DearQA.DearQA 

Breakpoint 1, 0x0000000000400590 in _start ()
(gdb) 
```
## ghidra

# Stenographie

## steghide

```
steghide extract -sf cute-alien.jpg
```

# encode / decode 

https://emn178.github.io/online-tools/index.html

https://cryptii.com/

## deocde base2

```python
print( ''.join( chr( int(x, 2) ) for x in "01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001".split(" ") ) )
```

## decode hexa /base16 

```python
print( ''.join( chr( int(x, 16) ) for x in "68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f".split(" ") ) )
```

# url encode
 * https://www.urlencoder.org/

# hash cracking

## hashcat

* guess hash

```
hashid F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85
Analyzing 'F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85'
[+] Snefru-256 
[+] SHA-256 
[+] RIPEMD-256 
[+] Haval-256 
[+] GOST R 34.11-94 
[+] GOST CryptoPro S-Box 
[+] SHA3-256 
[+] Skein-256 
[+] Skein-512(256) 
```
* trouver le code pour SHA2-256

```
hashcat --help | grep 256                            
 -u, --kernel-loops             | Num  | Manual workload tuning, set innerloop step size to X | -u 256
   1400 | SHA2-256                                         | Raw Hash
  17400 | SHA3-256                                         | Raw Hash
```


* brute force avec wordlist
  * m type de hash
  * a méthode 

```
hashcat -m 1400 -a 0 hash.txt /usr/share/wordlists/rockyou.txt 
```

# Reverse shell

 * https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
 * https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
 * https://0xss0rz.github.io/2020-05-10-Oneliner-shells/
 * https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/

# Spawning Shell
 * https://netsec.ws/?p=337

# Escalation

 * https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
 * https://gtfobins.github.io/
