# Challenge

**Name:** Fishy Doc

**Category:** Forensics

**Difficulty:** Medium

**Flag:** `UWA{f15hY_m4cR0s_nD_ch3353}`

---

## Description

Mumble accidentally opened a document that Pingu sent. Nekminit Mumble's computer was displaying warning messages that he has been hacked!

*Can you investigate the document Pingu sent and figure out how Mumble was hacked?*

---

## Solution

One of the most commonly methods of initial compromise using document files is by writing **malicious macros**. There are multiple ways to view Macros that students could use to view the macro.

**Method 1**

Document files are actually ZIP archives that you can extract the content from.

```bash
unzip fishy.odt
```

Macros are saved in the `Basic/` folder for odt files, and if we check the contents of the file we can see the malicious macro in `Basic/Standard/Module1.xml`.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="Module1" script:language="StarBasic" script:moduleType="normal">Sub AutoExec
	MsgBox &quot;You have been hacked!! Jk, this is a prank&quot;, vbMsgBoxSetForeground
	REM **** UWA{f15hY_m4cR0s_nD_ch3353} ****
End Sub
</script:module>
```

**Method 2 (Not recommended but most students would do this)**

You can open the document within word or libreoffice and edit the macros. There you can see the source code with the flag.
