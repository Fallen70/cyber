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


# Reverse shell

 * https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
 * https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

# Escalation

 * https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
 * https://gtfobins.github.io/
