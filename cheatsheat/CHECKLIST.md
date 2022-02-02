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

# Escalation

 * https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
 * https://gtfobins.github.io/
