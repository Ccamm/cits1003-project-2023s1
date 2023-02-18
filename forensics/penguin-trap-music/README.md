# Challenge

**Name:** Penguin Trap Music

**Category:** Forensics

**Difficulty:** Easy

**Flag:** `UWA{b455_i5_g00d_2_34t1!one!}`

---

## Description

Pingu recently torrented FL Studios and made a trap song to share with his friends. He thought it would be really cool to hide a secret message within the song using `steghide`, and was certain that his secret message was well hidden that he **did not set a passcode to hide his message**.

*Can you use `steghide` to extract the message from the song?*

---
## Hint

You can install `steghide` on your Linux container by running the following command.

```
apt install steghide
```

To see the available options for extracting files type the following command.

```
steghide --help
```

## Solution

Reading the help guide for `steghide`, the following command will extract the secret message with an empty passcode.

```bash
steghide extract -sf song.wav  -p '' -xf out.txt
```
