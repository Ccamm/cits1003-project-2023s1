# Challenge

**Multi Challenge:** `True`

**Ports Open:** `3000`

---

# Challenge 1

**Name:** Arctic File Storage Part 1: Surfing for Vulns

**Category:** Vulnerabilities

**Difficulty:** Medium

**Flag:** `UWA{CVE-2023-26492}`, `CVE-2023-26492`

---

## Description

The penguins have made the Arctic File Storage using a **modern Content Management System (CMS)**.

*Can you figure out what CMS is used and the **CVE ID for the latest Server-Side Request Forgery (SSRF) vulnerability**?

The flag is the CVE ID for the SSRF vulnerability.

---

## Hint 1

Maybe the `/robots.txt` has something interesting to point you in the right direction.

---

## Hint 2

*What if the challenge creator (Alex Brown AKA **ghostccamm**) is shamelessly plugging a vulnerability that they reported?*

---

## Solution

Reading the `/robots.txt` file on the website, you see the following Disallow list.

```
User-agent: *
Disallow: /admin/
Disallow: /localonly/flag.txt
```

Navigating to `/admin/` we see the admin sign in page for the CMS. Viewing the page source (right click on the page) we see the CMS is [Directus](https://github.com/directus/directus/).

Viewing the [Security Advisories for Directus](https://github.com/directus/directus/security/advisories), we can see that there was a [SSRF vulnerability reported recently (by me :))](https://github.com/directus/directus/security/advisories/GHSA-j3rg-3rgm-537h). On that page you get the CVE ID `CVE-2023-26492`

---

## Challenge 2

**Name:** Arctic File Storage Part 2: Rewind Rebind

**Category:** Vulnerabilities

**Difficulty:** Medium

**Flag:** `UWA{sUrFiNg_s3rV3r_r3qUeSt_f0rGry_1N_tH3_aRcT1c!!one11!!}`

---

## Description

There is a secret file located at `/localonly/flag.txt` on the website. However, you can only access this file from `localhost`.

*Using the vulnerability from Part 1, can you figure out a way to view the contents of `/localonly/flag.txt`?*

---

## Hint

Don't forgot the port that the server is listening on is **`3000`**. You need to include this in your URL, for an example `http://localhost:3000/localonly/flag.txt`.

---

## Solution

Reading my [SSRF vulnerability report](https://github.com/directus/directus/security/advisories/GHSA-j3rg-3rgm-537h), Directus was vulnerable to a SSRF forgery bypass called [DNS rebinding](https://en.wikipedia.org/wiki/DNS_rebinding). The DNS rebinding attack works by having a DNS server that resolves the same domain address to two different IP addresses quickly.

In the report, I gave the following domain `7f000001.8efa468e.rbndr.us` that will resolve between `142.250.70.142` (google.com) and **`127.0.0.1`**. Therefore, if you spam submitting the following URL it will eventually save the flag.

```
http://7f000001.8efa468e.rbndr.us:3000/localonly/flag.txt
```

Do note students will most likely to forget putting in the port `3000` into the URL.

To increase the odds of successfully getting the vulnerability to work you can click inspect on the site, navigate to the Network tab and spam clicking submit. When you see a `200` response to `/files/import`, view the request and copy the ID and visit `/assets/<ID>`.