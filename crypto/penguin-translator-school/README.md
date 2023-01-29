# Challenge

**Name:** Penguin Translator School

**Category:** Cryptography

**Difficulty:** Easy

**Flag:** `UWA{wAa_wAA_w00_means_i_h4V3_l0sT_mI_5aN1tI!1one}` or `WAA_WAA_W00_MEANS_I_H4V3_L0ST_MI_5AN1TI!1ONE` (case insensitive)

---

## Description

It's your first day at the International Penguin Translator School. You were sent by the Australian government to learn the penguin language to eventually become a diplomat for the New Great Penguin Empire that is now the dominant global power. An emperor penguin wearing a monocle and a top hat waddled to the front of the class and start writing the following text on the whiteboard.

```
wawoowoo wawoo wawoo wawawoowoowawoo wawoowoo wawoo wawoo wawawoowoowawoo wawoowoo woowoowoowoowoo woowoowoowoowoo wawawoowoowawoo woowoo wa wawoo woowa wawawa wawawoowoowawoo wawa wawawoowoowawoo wawawawa wawawawawoo wawawawoo wawawawoowoo wawawoowoowawoo wawoowawa woowoowoowoowoo wawawa woo wawawoowoowawoo woowoo wawa wawawoowoowawoo wawawawawa wawoo woowa wawoowoowoowoo woo wawa woowawoowawoowoo wawoowoowoowoo woowoowoo woowa wa
```

You begin to panic, realising that you have procrastinated all of the prerequisite work before starting study and had no idea what the penguin was writing. However, you do remember that the penguin written language was based on an **old method of encoding text that was once used by humans**.

*Can you figure out what the emperor penguin wrote on the whiteboard using [CyberChef](https://gchq.github.io/CyberChef/)?*

When submitting the flag, wrap the message with `UWA{message here}`.

---

## Solution

There are two patterns written on the whiteboard, `wa` and `woo`. This is very similar to **morse code** that uses the characters `.` and `-` for encoding messages.

[Solution CyberChef recipe](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Simple%20string','string':'woo'%7D,'-',true,false,true,false)Find_/_Replace(%7B'option':'Simple%20string','string':'wa'%7D,'.',true,false,false,false)From_Morse_Code('Space','Line%20feed')&input=d2F3b293b28gd2F3b28gd2F3b28gd2F3YXdvb3dvb3dhd29vIHdhd29vd29vIHdhd29vIHdhd29vIHdhd2F3b293b293YXdvbyB3YXdvb3dvbyB3b293b293b293b293b28gd29vd29vd29vd29vd29vIHdhd2F3b293b293YXdvbyB3b293b28gd2Egd2F3b28gd29vd2Egd2F3YXdhIHdhd2F3b293b293YXdvbyB3YXdhIHdhd2F3b293b293YXdvbyB3YXdhd2F3YSB3YXdhd2F3YXdvbyB3YXdhd2F3b28gd2F3YXdhd29vd29vIHdhd2F3b293b293YXdvbyB3YXdvb3dhd2Egd29vd29vd29vd29vd29vIHdhd2F3YSB3b28gd2F3YXdvb3dvb3dhd29vIHdvb3dvbyB3YXdhIHdhd2F3b293b293YXdvbyB3YXdhd2F3YXdhIHdhd29vIHdvb3dhIHdhd29vd29vd29vd29vIHdvbyB3YXdhIHdvb3dhd29vd2F3b293b28gd2F3b293b293b293b28gd29vd29vd29vIHdvb3dhIHdh)