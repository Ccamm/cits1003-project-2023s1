# Challenge

**Name:** Skipper's Cookie

**Category:** Vulnerabilities

**Difficulty:** Easy

**Flag:** `UWA{c0000k13s_N0m_n0m_n0M!!one11!}`

---

## Description

Skipper has developed a *secure website* to protect his **cookie**!

*Can you figure out a way to trick the website that you are **Skipper** to steal his **cookie**?

---

## Hint

Some **cookies** you cannot eat.

---

## Solution

On the website, inspect and go to the Storage tab and view the **Cookies** set for the website. You will see a cookie named `user` with a value of `Guest`. If you change the value to `Skipper` and refresh the page the website will think you are Skipper and give you the flag.