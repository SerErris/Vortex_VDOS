# VORTEX X Drives F1-X and M1-X

**User Manual** · Rev. 1 / 4/17/1986 · 1st edition · © 1986 vortex Computersysteme GmbH

**Revised edition for VDOS 2.11-X** · 2026 · The original manual describes VDOS 2.0. This edition has been adapted to the actual behavior of VDOS 2.11-X from 1986 (checked in the emulator); the known bugs are listed in the chapter [Known bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x).

---

## Contents

- [Preface](#preface)
- [Important Notes](#important-notes)
- [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance)
- [Setting Up the CPC464+DDI-1 with X Drive](#setting-up-the-cpc464ddi-1-with-x-drive)
- [Setting Up the CPC664/CPC6128 with X Drive](#setting-up-the-cpc664cpc6128-with-x-drive)
- [Disks, Disks and More Disks](#disks-disks-and-more-disks)
  - [Which Disks Do We Need?](#which-disks-do-we-need)
  - [Never](#never)
  - [Always](#always)
- [VDOS – Vortex Disk Operating System](#vdos--vortex-disk-operating-system)
- [Basics](#basics)
- [The VDOS Command |FORMAT](#the-vdos-command-format)
- [Running and Saving a BASIC Program](#running-and-saving-a-basic-program)
- [What Is a File, Anyway?](#what-is-a-file-anyway)
- [The VDOS Commands |A and |B](#the-vdos-commands-a-and-b)
- [The VDOS Command |X](#the-vdos-command-x)
- [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir)
- [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut)
- [The VDOS Command |ERA](#the-vdos-command-era)
- [The VDOS Command |REN](#the-vdos-command-ren)
- [The VDOS Command |SELECT](#the-vdos-command-select)
- [The VDOS Command |RESET](#the-vdos-command-reset)
- [The VDOS Command |CODE](#the-vdos-command-code)
- [The VDOS Command |AMSDOS](#the-vdos-command-amsdos)
- [Cassette Recorder on the CPC](#cassette-recorder-on-the-cpc)
  - [The VDOS Command |DISC](#the-vdos-command-disc)
  - [The VDOS Command |CAS](#the-vdos-command-cas)
  - [The VDOS Command |DISC.IN](#the-vdos-command-discin)
  - [The VDOS Command |CAS.IN](#the-vdos-command-casin)
  - [The VDOS Command |DISC.OUT](#the-vdos-command-discout)
  - [The VDOS Command |CAS.OUT](#the-vdos-command-casout)
- [The VDOS Command |XMON – The vortex Z80 Monitor](#the-vdos-command-xmon--the-vortex-z80-monitor)
- [The VDOS Command |ROMOFF](#the-vdos-command-romoff)
- [The VDOS Command |ROMCAT](#the-vdos-command-romcat)
- [The VDOS Commands |FAST, |SLOW and |FRAME](#the-vdos-commands-fast-slow-and-frame)
- [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling)
- [The VDOS Command |FILES](#the-vdos-command-files)
- [The VDOS Command |OPEN](#the-vdos-command-open)
- [The VDOS Command |FIELD](#the-vdos-command-field)
- [The VDOS Command |GET](#the-vdos-command-get)
- [The VDOS Command |PUT](#the-vdos-command-put)
- [The VDOS Command |CLOSE](#the-vdos-command-close)
- [Two Small Applications](#two-small-applications)
- [Ways of Trapping Disk Errors](#ways-of-trapping-disk-errors)
- [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- [The VDOS Turnkey Function](#the-vdos-turnkey-function)
- [X Drives on the CPC464 with DDI-1, CPC664 and CPC6128](#x-drives-on-the-cpc464-with-ddi-1-cpc664-and-cpc6128)
- [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk)
- [CPC464, CPC664 with X Drive and vortex RAM Card](#cpc464-cpc664-with-x-drive-and-vortex-ram-card)
- [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only)
- [Loading the CP/M Operating System](#loading-the-cpm-operating-system)
  - [The VDOS Command |CPM](#the-vdos-command-cpm)
  - [The VDOS Command |CPM,1](#the-vdos-command-cpm1)
  - [The VDOS Command |CPM,2](#the-vdos-command-cpm2)
- [CP/M with Your vortex X Drive](#cpm-with-your-vortex-x-drive)
- [The CP/M Command FILECOPY](#the-cpm-command-filecopy)
- [The CP/M Command XMON](#the-cpm-command-xmon)
- [The CP/M Command SYSGEN](#the-cpm-command-sysgen)
- [The CP/M Command DISKTOOL](#the-cpm-command-disktool)
- [The CP/M Command INSTALL](#the-cpm-command-install)
- [The CP/M Command CASCOPY](#the-cpm-command-cascopy)
- [The CP/M Command VDOS](#the-cpm-command-vdos)
- [The CP/M Command FAST](#the-cpm-command-fast)
- [CP/M Error Messages and How to Fix Them](#cpm-error-messages-and-how-to-fix-them)
- [VDOS and CP/M Internals](#vdos-and-cpm-internals)
  - [BIOS – Basic Input Output System](#bios--basic-input-output-system)
  - [DOS – Disk Operating System](#dos--disk-operating-system)
  - [RAM Variables of BIOS and DOS](#ram-variables-of-bios-and-dos)
- [CP/M Under the Magnifying Glass – The CP/M Operating System](#cpm-under-the-magnifying-glass--the-cpm-operating-system)
- [Finally, a Few Words About the Hardware](#finally-a-few-words-about-the-hardware)
- [Pin Assignment of the Connectors](#pin-assignment-of-the-connectors)
- [Index](#index)
- [Appendix: The EOF Problem](#appendix-the-eof-problem)
- [Known Bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x)

---

## Preface

**vortex floppy disk drives F1-X and M1-X for all CPC464+DDI-1, CPC664, CPC6128**

Dear CPC owners,

almost exactly one year ago (in April '85) the first "vortex baby" saw the light of day: the **vortex floppy disk drive F1-D**, designed for the CPC464, which was still brand new back then. Our offspring has been called a "little revolution". And rightly so, because the specs of this device are truly revolutionary: high storage capacity (1.4 megabytes), a common disk format (5.25"), cheap, readily available disks, state-of-the-art drives, mature controller electronics and intelligent, fast operating system software.

Our customer service is groundbreaking too. Whether it is just a matter of explaining how to format a disk, or whether you need hands-on help adapting a program, you will always find a competent expert on our team who is glad to help you.

Nobody is perfect. There is no program that doesn't have at least one weak spot. Usually it is not just one, but… Where others leave you on your own, we keep improving and polishing, and most importantly, you are part of it: whenever there is something new, or whenever bugs have been fixed, you can equip your floppy with the new software – even if you bought it a year ago.

Put all of this together and you know why we are so successful.

The rapid arrival of the CPC664 and then the CPC6128 prompted us to provide for more offspring. Almost in one go, a whole range of new floppy drives and, as the crowning glory, a hard disk came into being.

Once again we have proven what we can do, although it remained completely unclear to us why we should be the only ones. It must be because we are better than good.

A major part of our work was a project that we nicknamed the "K project" within the company. Behind it is a whole group of drives that are intended exclusively to work together with an existing 3" drive and 3" floppy controller – CPC464+DDI-1, CPC664, CPC6128. Ruled out from the start, of course, was the simple and already completed development of a second drive with low storage capacity (vortex drives F1-Z and M1-Z). No, it had to be something that would make buying a "second drive" completely pointless.

…said: "First of all we need a high storage capacity, so that the misery finally comes to an end: 700 KB really ought to be enough. And please, finally a common disk format with disks available always and everywhere at low prices: 5.25", 3.5". Then a professional operating system: VDOS 2.0 and of course CP/M 2.2 and CP/M plus too. And please not yet another box 'dangling around'. Above all, please no 'sending it in', no 'soldering', oh, and then that business with the copyrights… Performance and price: sensational."

**The result: vortex X drives F1-X and M1-X**

- High storage capacity: 708 KB formatted
- Common disk formats: 5.25" or 3.5"
- Cheap disks, no supply shortages
- Professional operating system VDOS 2.0
- VDOS plug-in module into which the DDI-1 controller is inserted
- Random-access (relative) file handling under BASIC
- Z80 machine language monitor
- Fully compatible with existing VDOS 2.0 and AMSDOS software!
- CP/M 2.2 and CP/M plus
- prepared for an RS232C serial interface
- 128 possible directory entries
- The price… a dream!

And you have decided on it too – obviously, since there is no alternative.

This manual describes all the commands and details of the vortex X drives. For more detailed information on CP/M 2.2 and CP/M plus, please refer to the manuals you received when you bought your CPC.

This manual consists of 3 major parts:

- Description of all VDOS commands
- Description of all vortex CP/M commands
  The chapter "X Drives on the CPC464 with DDI-1, CPC664 and CPC6128" specifically describes how you can make yourself a CP/M system disk.
- Technical information about VDOS and CP/M in connection with the X drives

Please take the time to read everything through calmly once. That helps you and us!

And now we wish you lots of fun with your new vortex floppy.

*Your vortex team*

---

## Important Notes

> **(!) Important**
>
> Reproduction and distribution of this manual – even in part – require the prior written permission of vortex Computersysteme GmbH.
>
> Subject to change without notice.
>
> All maintenance and warranty work must be carried out by vortex or by vortex-authorized dealers. In any other case, all warranty claims are void.
>
> If devices are not properly packed when they are sent back to vortex for maintenance and warranty work (in particular, if the cardboard transport protection disk is missing from the drive), all warranty is void in any case.
>
> **Always ship devices in their original packaging!**
>
> vortex accepts no responsibility for the suitability of the product for particular applications.

> Z80 is a registered trademark of Zilog Inc.
>
> vortex and vortex VDOS are registered trademarks of vortex GmbH.
>
> CP/M 2.2 and CP/M plus are registered trademarks of Digital Research Inc.
>
> WordStar is a registered trademark of MicroPro Inc.
>
> dBase II is a registered trademark of Ashton Tate.
>
> Multiplan is a registered trademark of Microsoft.

---

## vortex X Drives at a Glance

Our X drives are available in two different versions:

- with a 5.25" drive
- or a 3.5" drive

each with 708 KB of formatted storage capacity.

| Name | Drive |
|-------------|----------|
| **F1-X**    | 5.25" drive |
| **M1-X**    | 3.5" drive  |

The following device combinations (sets) are possible:

| Computer | + Drive | Format | Capacity | Operating systems |
|----------|------------|--------|-----------|-----------------|
| CPC464+DDI-1 | F1-X | 5.25" | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC464+DDI-1 | M1-X | 3.5"  | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC664       | F1-X | 5.25" | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC664       | M1-X | 3.5"  | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC6128      | F1-X | 5.25" | 708 KB | VDOS, AMSDOS, CP/M 2.2/+ |
| CPC6128      | M1-X | 3.5"  | 708 KB | VDOS, AMSDOS, CP/M 2.2/+ |

(`+` = CP/M plus operating system)

In the rest of this manual we will always speak of **X drives**, since all commands are absolutely identical for the M1-X and F1-X drives.

All vortex X drives require 220 V mains power at 50 Hz.

Every X drive comes with the so-called **VDOS module** (a small interface in an elegant plastic case; it essentially carries the VDOS EPROM). This module is also prepared to take the vortex RS232C interface. If you have a CPC464+DDI-1, your DDI-1 floppy controller "disappears" into this module.

The drive itself and the power supply are housed in a solid metal case.

To switch the drive on and off, there is a push-button switch on the back of the metal case. If it sticks out only slightly from the back panel, the drive is switched on. The drive's power plug can stay in the outlet even when the device is not used for a long time.

On all X drives you can switch between the VDOS and the AMSDOS operating system. Right after the set is switched on, the VDOS operating system is always available immediately.

On all sets that include the CPC6128, you also have the CP/M plus operating system available as an alternative to the CP/M 2.2 operating system.

When the X drive is run under VDOS or CP/M (with the vortex BIOS), it has 128 directory entries.

The 3" drive can handle at most 64 directory entries in every operating mode (AMSDOS, VDOS, CP/M).

If you have a set consisting of a CPC464+DDI-1 with X drive, the following power-on sequence must be observed:

1. Switch on the DDI-1 floppy
2. Switch on the vortex X drive
3. Switch on the CPC464

For the sets with the CPC664 or CPC6128 there is no power-on sequence to observe.

The CPC464+DDI-1 set with X drive has the "turnkey function". After every reset (switching off/on or pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time), the 3" disk in the 3" drive is searched for a file `HELLO.BAS`. If it is found, it is run. The search can be suppressed by pressing, for example, the `ESC` key immediately (after the reset). With this function the system can be brought up into a particular operating mode (e.g. CP/M) right from the start.

None of the sets with the CPC664 and CPC6128 have this function.

---

## Setting Up the CPC464+DDI-1 with X Drive

> **(!) Important:** Unplug all plugs from the outlet.

Setting up this set takes place in two stages:

- Mounting the DDI-1 floppy controller in the case of the VDOS module (gray plastic case shaped like a "truncated pyramid")
- Connecting the X drive to the ribbon cable of the DDI-1 floppy controller.

All the tools you need for this is a small Phillips screwdriver, that's all. You should also bring along a little patience, so that you actually live to see your device up and running.

**A.** Take the VDOS module out of its packaging. On the underside of the case you will see four small Phillips screws. Undo them and put them in a safe place. Now you can take the cover off.

**B.** When you look into the case, you now see a small circuit board (from the component side, that is). Standing vertically on this board, pointing toward you, you see another small board, which however carries no components. It has 50 "contact tongues". This small board is also called a "card-edge connector".

**C.** Now get the DDI-1 floppy controller (you have previously unplugged it from your CPC. You have also unplugged the 3" drive).

**D.** If you look at the controller, you will find the counterpart of the "card-edge connector" on it, namely the "card-edge socket" (it is also what connects the controller to the CPC without an X drive).

**E.** If you look at the VDOS module more closely, you will see a 50-pin ribbon cable with a card-edge socket sticking out through a slot on one side.

**F.** Now hold the VDOS module in your left hand so that you can look into it from below and the 50-pin ribbon cable mentioned under "E." points away from you.

**G.** Take the DDI-1 floppy controller in your right hand so that the 50-pin card-edge socket points into the open module and the 34-pin ribbon cable leads off to the right.

**H.** Plug the DDI-1 floppy controller into the VDOS module so that the small vertical board in the VDOS module sits in the 50-pin card-edge socket of the DDI-1 floppy controller. Press the DDI-1 floppy controller in firmly.

**I.** Get the bottom cover of the VDOS module again and screw the VDOS module shut (with the four Phillips screws from before – you still have them, don't you?).

**J.** You see, vortex has thought things through: not yet another second box dangling around, but a neat, compact unit that even provides enough room for the vortex RS232C interface.

**K.** Plug the VDOS module – now a complete floppy controller with AMSDOS and VDOS! – onto the 50-pin "expansion bus" at the back of the CPC464 (the same place where the DDI-1 floppy controller was plugged in on its own). The VDOS module ends up positioned so that the 34-pin ribbon cable points to the right (toward the cassette recorder).

**L.** Now place the X drive to the right of your CPC (the side with the cassette recorder), with the disk slot facing forward, and put the 3" drive on top of it.

**M.** Now everything is actually clear already. The 34-pin socket strip at the end of the 34-pin ribbon cable goes into the top of the 3" drive; the 34-pin plug hanging out of the X drive goes into the second socket on the 34-pin ribbon cable.

**N.** All plugs into the outlet, switch on the 3" drive, then the X drive (see the push button on the back of the X drive) and then the CPC – done!

Your "new" computer system is now ready for use.

### Power-On Sequence

1. Switch on the DDI-1 floppy
2. Switch on the X drive
3. Switch on the CPC464

Right after the set is switched on:

- VDOS is switched on
- drive A is the 3" drive
- drive B is the X drive
- the 3" drive can handle at most 64 directory entries
- the X drive can handle at most 128 directory entries

---

## Setting Up the CPC664/CPC6128 with X Drive

> **(!) Important:** Unplug all plugs from the outlet.

Setting up this set could hardly be simpler. Take the VDOS module out of its packaging. You will see a 50-pin ribbon cable hanging out of the module, with a 50-pin socket at its end. Place the VDOS module behind your CPC so that the cable points toward you and the vortex lettering is on top. Plug the socket onto the 50-pin "expansion bus" of your CPC.

Now the X drive still has to be connected. At the back of your CPC you will find a connector labeled **Disc drive 2**, and on the X drive a 34-pin cable with a 34-pin socket at its end that fits exactly onto the connector labeled "Disc drive 2". The socket is plugged on so that the ribbon cable leads out upward (watch for the "OBEN" (TOP) sticker!).

All plugs into the outlet, switch on the CPC, switch on the X drive (see the push button at the back of the X drive), done.

Right after any set is switched on:

- VDOS is switched on
- drive A is the 3" drive
- drive B is the X drive
- the 3" drive can handle at most 64 directory entries
- the X drive can handle at most 128 directory entries

---

## Disks, Disks and More Disks

### Which Disks Do We Need?

All vortex floppies are equipped with 80-track drives and have two read/write heads (front and back of the disk). Depending on whether you have chosen the 5.25" format or the 3.5" format, you need disks of the following type for safe, trouble-free operation of the vortex drive:

| Drive | Disk type |
|----------|--------------|
| 5.25" drives | DS/DD/96tpi |
| 3.5" drives  | DS/DD/135tpi |

DS stands for **DoubleSided**. DD stands for **DoubleDensity**. 96tpi (135tpi) stands for 96 (135) tracks per inch, i.e. 80 tracks.

You should use only disks with this designation. Please buy only quality disks, since poor disk material not only costs you data safety but can also damage the drives.

For 5.25" disks we can recommend the **2/96 FlexyDisk 5.25 from BASF**, for 3.5" disks the **MF2DD 135tpi from FUJI FILM**. Both disks have been put through their paces in our long-term tests.

### Never

- touch the magnetic disk surface directly
- bend or fold the disk
- go outside the temperature range given on the disk
- expose the disk to magnetic fields
- write on the label while it is on the disk
- smoke at the same time (you should give that up anyway!)
- put heavy, sharp-edged objects on the disk
- stack many disks on top of each other and store them that way

### Always

- put disks back into their protective sleeve after use
- store disks standing upright in a suitable box
- slide them carefully into the drive slot, without bending or tilting them
- insert the disk so that the disk label faces up and the read/write opening points toward the drive, and the disk clicks into place

You should definitely observe these points.

When the disk has clicked into place, press the eject button in firmly. To "eject" the disk from the drive, press the eject button again.

> **(!) Note:** Never take the disk out of the drive while the drive is working.

---

## VDOS – Vortex Disk Operating System

**VDOS** is an abbreviation for **Vortex Disk Operating System**.

### What Is That, a DOS?

DOS, translated into plain words, means **disk operating system**.

An operating system is nothing more than a program that takes over control of a particular piece of hardware. The hardware is a logical interconnection of several electronic components (integrated circuits, chips). In the case of your Schneider computer these are, in detail, the Z80 microprocessor, the RAM (read/write memory), the ROM (read-only memory), the video controller, the interface chip, the sound generator and a few more chips.

To make this hardware work the way you are used to and expect from your computer, you need the operating system. It works nonstop behind the scenes and holds all the strings in its hands. It gives you the simplest commands, which let you handle the hardware with ease without ever having to understand how the whole computer actually works.

A disk drive or floppy disk drive is basically nothing more than a piece of hardware, too. It consists of the drives themselves, a power supply and a controller, also called an interface. To be able to operate the floppy disk drive together with your computer, an operating system extension, a DOS, is needed. Here too the principle applies that everything should be as uncomplicated as possible and usable without any special prior knowledge.

When I spoke of an operating system extension just now, that was actually something of an understatement. The DOS is a very complicated thing, since on the one hand it has to operate the entire disk drive, and on the other hand it has to be fitted into the existing operating system in such a way that no contradictions or conflicts may arise anywhere.

VDOS, the disk operating system from vortex, was developed specifically for the Schneider computers. It is able to serve drives with high capacity (700 KByte) and contains all the functions a professional DOS should have.

A special feature of VDOS is **random-access (relative) file handling** under BASIC. Whereas under AMSDOS you could only use two sequential files at the same time, under VDOS you can use two sequential and 16 random-access files at the same time. Only "random" access to the data of a random-access file makes it possible, for example, to develop a professional database system under BASIC.

VDOS also offers something very special for fans of machine-language programming: the **Z80 machine language monitor**. While under AMSDOS there was no sensible way to "look inside the system", with VDOS that is no longer a problem.

All in all, VDOS is an operating system that goes far beyond the capabilities of an AMSDOS. But see for yourself.

---

## Basics

All VDOS commands have one thing in common: they begin with a vertical bar `|`. This bar tells the CPC that a VDOS command is coming now and not a BASIC command. Commands that begin with a vertical bar are often also called "RSX commands" or "external commands" and are not a "specialty" of the VDOS operating system.

### How Do We Type the Vertical Bar?

Between the `P` key and the key with the opening square bracket `[` is the key with the "at sign" `@` (in German the "Klammeraffe", the "clinging monkey"). If we press the `SHIFT` key together with this key, the vertical bar `|` is output.

To tell the CPC that what we have just typed should be understood as a command, we have to press the `ENTER` key. From now on we will symbolize this by `<ENTER>`.

A general command entry therefore looks like this:

```
|VDOS-BEFEHL<ENTER>
```

For example, type in the following:

```
|DIR<ENTER>

Laufwerk A: User  0

TEST    .BAS  INSTALL .COM  TEST    .BIN  RUNNER  .BAS

 60K in   4 Files, 109K frei

Ready
```

This shows us which files are on the 3" disk in the 3" drive.

There is one more peculiarity to note with the VDOS commands (they are external commands). If some variable is to be passed along with a VDOS command, then in some cases the variable must be given an "at sign" `@`. In other cases you can also pass the contents of the variable directly. For example:

```
A$="*.BAS"<ENTER>
|DIR,@A$<ENTER>

Laufwerk A: User  0

TEST    .BAS  RUNNER  .BAS

 60K in   2 Files, 109K frei
```

With the `|DIR` command we could also have said directly:

```
|DIR,"*.BAS"<ENTER>
```

and would have got the same result as above.

With the `|GET` command (part of random-access file handling), on the other hand, only the notation with the "at sign" may be used:

```basic
NAME$="otto"
ORT$="Essen"
TELE$="0123456"
|GET,1,173,@NAME$,@ORT$,@TELE$
```

The "at sign" is not the result of a "bad" operating system, but a peculiarity of the BASIC built into your CPC. I will point it out to you when only the notation with the "at sign" is allowed. In all other cases you can use either, and the second option shown above is certainly the more convenient one.

---

## The VDOS Command |FORMAT

**Formatting a disk**

Before you can work with a new disk, it first has to be prepared for it. You can picture it like this: there is nothing at all on the new, empty disk platter; it is completely homogeneous. So that the drive (and of course VDOS too) can do something with this disk, a basic structure has to be written onto the disk.

This basic structure consists of a certain number of tracks and sectors. Instead of track you could also say circle. On the front and on the back of a vortex disk, 80 tracks of 9 sectors each are marked. In addition, all areas between the marks are written with a particular value. This is also called formatting the disk.

Let's think right away about what happens when we format a disk that has already been written to. Because formatting not only writes the marks but also "fills" the areas between the marks, this naturally has a catastrophic effect on any data that might be there: it is all erased, every last bit of it. So be careful!

> **(!) Important:** Formatting erases all data on the disk!

Insert a brand-new disk, fresh from the package, into your vortex X drive. Formatting is done with the VDOS command `|FORMAT`. Type in this here:

```
|FORMAT,2<ENTER>

Laufwerk B: Diskette eingelegt J/N ?
J

Seite 1 Spur 79
Ready
```

This disk is now formatted. Now type

```
|B<ENTER>
|DIR<ENTER>

Laufwerk B: User  0

  0K in   0 Files, 704K frei
Ready
```

As you can see, the disk is completely empty ("0 Files").

Now type in the following:

```
|A<ENTER>
|FORMAT,1<ENTER>
Laufwerk A: Diskette eingelegt J/N ?
J
Format (S,D) ? S
Seite 0 Spur 39
Ready
```

This formats the 3" disk in drive A (the 3" drive). As you can see, here you can also choose between two formats (S/D): system and data format.

As a rule, you are asked the question `Format (S,D) ?` (after the question `Diskette eingelegt J/N ?`) whenever `|FORMAT,1<ENTER>` or `|FORMAT,2<ENTER>` "hits" the 3" drive. `|FORMAT,2<ENTER>` "hits" the 3" drive if you have previously swapped drive A and drive B with the VDOS command `|X`, so that drive A is then the vortex X drive and drive B the 3" drive.

If you enter "S", the 3" disk is formatted with 40 tracks of 9 sectors each (sector numbers `41H`–`49H`). This format is identical to the "system format" and the "vendor format". Both formats have two reserved tracks, but only the system format contains the CP/M operating system. The vendor format is intended for the case where you want to sell, for example, CP/M software you have developed yourself on 3" disk. Of course you cannot ship these disks with CP/M, so you copy your software onto a disk formatted in vendor format ("VerkaufsfORMAT", the "selling format"), which does contain the two tracks that can hold CP/M, but CP/M itself is missing. Your customer can very easily copy "his" CP/M onto this disk (e.g. with `BOOTGEN` and `SYSGEN`).

If you enter "D", the disk is formatted in DATA-only format. This format has 40 tracks of 9 sectors each, but no reserved tracks, so it can never contain a CP/M operating system. The sector numbering is `C1H`–`C9H`. Because the system tracks are missing, a disk formatted in DATA-only format has a somewhat higher storage capacity than a disk formatted in system/vendor format.

It should also be mentioned here that disks can also be formatted under CP/M. The program `DISKTOOL` is available there for this purpose.

---

## Running and Saving a BASIC Program

When you switch on your CPC with the vortex X drive connected, you get, among other things, the following message:

```
(C)1986   VDOS 2.11-X by vortex GmbH

Ready
```

It shows us that the X drive is working, VDOS 2.11-X is present and the CPC is waiting for input from us (signaled by "Ready"). I want to show you briefly here – you should really know this already – how to save a BASIC program, i.e. write it to disk, and how you can load it again and run it.

Just type in the following little program:

```basic
10 MODE 2
20 PRINT "* Dies ist ein Test-Programm *"
30 FOR A=1 TO 10
40 PRINT A
50 NEXT A
60 PRINT "* Das war's ... *"
70 END
```

If you switch off the computer now, everything is gone. Here that doesn't matter, this is just a test program without any real purpose anyway. But if you have spent a whole weekend "hatching" a program, never saved it and then switch off the computer, the hunt for the guilty party probably begins…

That is why we save the program away to disk. It can then be loaded again from there at any time, even if you switch the computer off and on in between. We think of a simple name for our little program: how about `TEST`? But before we get to saving, we first need a disk we can save to.

Get a completely new disk (fresh from the package); it still has to be formatted as described for the `|FORMAT` command. Insert the disk into the vortex X drive and also type `|X<ENTER>` (so that drive A is the X drive and drive B the 3" drive). Now we can save our little program to the disk. Of course you don't have to start a new disk every time!

To do this, type in the following:

```
SAVE "TEST"<ENTER>
```

The drive will start up, the little program is saved and you're already done. Now type in this:

```
CAT<ENTER>

Laufwerk A: User  0

TEST    .BAS  1K

  1K in   1 Files, 700K frei
```

On the disk we find our `TEST` program again. Now, as "proof", type in this here:

```
NEW<ENTER>
LIST<ENTER>

Ready
```

Yes, we have deleted our program! Don't worry, we saved it. Bring it back "in" with the following line:

```
LOAD "TEST"<ENTER>
Ready
LIST<ENTER>
```

```basic
10 MODE 2
20 PRINT "* Dies ist ein Test-Programm *"
30 FOR A=1 TO 10
40 PRINT A
50 NEXT A
60 PRINT "* Das war's ... *"
70 END
```

Yes indeed, it's back! Now we run the program with `RUN<ENTER>`. The screen is cleared and then essentially the numbers 1 to 10 are output, nothing great, just something for demonstration. You could also have typed `RUN "TEST"<ENTER>` directly. Then the file `TEST.BAS` would have been loaded from the disk and run immediately.

A few more words about the `SAVE` command. There are actually 4 ways to use this command:

1. `SAVE "DATEI"<ENTER>`
2. `SAVE "DATEI",A<ENTER>`
3. `SAVE "DATEI",P<ENTER>`
4. `SAVE "BILD",B,&C000,&4000<ENTER>`

We have already understood the first variant above. Here the program is saved in a "compressed form" that needs little disk space.

The second option creates a so-called ASCII file. That is a pure text file that contains no special characters etc. at all. The program is actually stored just the way we see it listed on the screen.

With the third option the program is saved "protected". It can no longer be "LISTed".

The last option does the following: all data in memory between address `&C000` and `&FFFF` (= `&C000` + `&4000`) (that is the screen contents) is stored in the file `BILD.BIN` (BIN stands for binary).

---

## What Is a File, Anyway?

You don't know? Never mind, I will explain it to you briefly. Imagine you have a filing cabinet in your office containing a whole row of binders ("Leitz binders"). In each binder the papers for a particular matter are filed. If that is not the case, then your filing system is a disaster!

And now the analogy: the filing cabinet is the disk, the binders are the files and the papers are the data stored in a file. Just as you give each binder a label so you can find it more easily, each file also gets a name. By the way, the German word for file is "Datei".

The file name is subject to certain restrictions: a name such as "This is my first file" is not allowed. The file name that VDOS (and, by the way, CP/M too) accepts is:

```
Dateiname.Dateityp
```

The file name can be up to 8 characters long; at most 3 characters are allowed for the file type. The period between name and type is mandatory.

You can use all characters in a file name except the following:

```
< > . ; : = ? * [ ] % ! ( ) / \
```

The file type often gives some indication of the contents of the file. Examples of file names are: `TEST.BAS`, `SPIELE`, `BILD.BIN`, `PROGRAMM.BAS`.

Under BASIC you will mostly come across the following file types (also called *extension*):

- **BAS** – This is a BASIC program that can be run with `RUN` or loaded with `LOAD`, e.g. `SPIEL.BAS` or `PROGRAMM.BAS`.

- **BAK** – Backup file. When you want to save a BASIC program with `SAVE`, VDOS "looks" on the disk to see whether a file with the name you have chosen already exists there. If there is one, its type is changed to `BAK` (previously `BAS`). The file you actually wanted to save, however, gets the type `BAS`. For example:

  ```
  SAVE "TEST"<ENTER>
  ```

  This file is stored on the disk under the name `TEST.BAS`. But there already is a file there called `TEST.BAS`. VDOS simply renames it to `TEST.BAK`. So it cannot happen that you delete a file by mistake.

- **BIN** – `BIN` stands for "binary". The contents of a BIN file can be, for example, a complete screen image or a machine program. A file of this type is created, for example, by the following `SAVE` command:

  ```
  SAVE "BILD",B,&C000,&4000<ENTER>
  ```

  On the disk we find the file `BILD.BIN`. The "B" after `"BILD"` forces a binary file to be created.

If a file is to be loaded and no file type is given in the load command, the first file found with the given file name is loaded, following the search order `' '`, `'BAS'`, `'BIN'`, `'BAK'`.

---

## The VDOS Commands |A and |B

**Switching between drives**

Under VDOS you have at most two drives available. We have christened them "drive A" and "drive B" (more simply just A and B). The special thing about your set is that you have drives of different formats (3" and 5.25" or 3" and 3.5") with different capacities (approx. 170 KB and 708 KB).

After the CPC and the X drive are switched on, drive A is the 3" drive and drive B the X drive.

Commands you enter now refer to drive A, the 3" drive:

```
|DIR<ENTER>

Laufwerk A: User  0

TEST    .BAS    TEST    .BIN
PROGRAMM.BAS    TEST    .BAK

100K in   4 Files,  69K frei
```

If we want to see, for example, what is on the disk in the X drive, we first have to "switch" to it:

```
|B<ENTER>
```

Commands you enter now "act" on drive B, the X drive:

```
|DIR<ENTER>

Laufwerk B: User  0

PIP     .COM    M80     .COM    VDOS    .MAC
STAT    .COM    L80     .COM    WS      .COM
WSMSGS  .OVR    WSOVLY1 .COM

304K in   8 Files, 400K frei
```

You can see that we have considerably more storage space available here.

This is how we switch back to the 3" drive:

```
|A<ENTER>
```

We can imagine, for example, the following little program:

```basic
10 MODE 2
20 PRINT "Dies ist die Directory der Diskette in Laufwerk A"
30 CAT
40 |B
50 PRINT "Dies ist die Directory der Diskette in Laufwerk B"
60 CAT
70 |A
80 END
```

```
Ready
RUN<ENTER>
```

When you have run this program (with `RUN`), the screen is cleared and the directories of the disks in drive A (3" disk) and drive B (3.5" or 5.25" disk) are output one after the other, each accompanied by the little text. At the end, it switches back to drive A (line 70).

If you don't know what `MODE 2`, `PRINT` and `END` mean, then before you read any further here you should first pick up the BASIC manual you received with your CPC and gather "certain" basic knowledge there!

---

## The VDOS Command |X

**Swapping drive A and B**

Switch on all devices, insert a disk into the 3" drive and into the vortex X drive, then type `CAT<ENTER>`, and you get the directory of the 3" disk. Type `|B<ENTER>` and `CAT<ENTER>`, and you get the directory of the disk in the vortex X drive.

The power-on state of the CPC and the X drive is therefore:

- Drive A -> 3" drive (built in on the CPC664 and CPC6128, external with the DDI-1 on the CPC464)
- Drive B -> vortex drive (5.25" on the F1-X and 3.5" on the M1-X)

But if you now type

```
|X<ENTER>
```

you swap ("exchange") drive A with drive B. That is, the new assignment is:

- Drive A -> vortex drive (5.25" on the F1-X and 3.5" on the M1-X)
- Drive B -> 3" drive (built in on the CPC664 and CPC6128, external with the DDI-1 on the CPC464)

Now switch back to A (we switched to B above, after all) by typing `|A<ENTER>`. Now start `CAT<ENTER>` and you get the directory of the disk in the vortex X drive (now drive A).

Reset the computer – to have a clearly defined starting state – by pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time.

Insert a 3" disk into the 3" drive and a 5.25"/3.5" disk into the X drive. Both disks should already have something on them. Now take a look at this little program here:

```basic
10 MODE 2
20 PRINT "Dies ist der Inhalt der 3" Diskette in Laufwerk A"
30 CAT
40 CLS
50 |B
60 PRINT "Dies ist der Inhalt der 5.25"/3.5" Diskette in"
70 PRINT "Laufwerk B"
80 CAT
90 |A:REM Wieder Umschalten auf Laufwerk A (3" Laufwerk)
100 |X:REM Vertauschen Laufwerk A und Laufwerk B
110 CLS
120 PRINT "Dies ist der Inhalt der 5.25"/3.5" Diskette in"
130 PRINT "Laufwerk A"
140 CAT
150 |B
160 PRINT "Dies ist der Inhalt der 3" Diskette in Laufwerk B"
170 CAT
180 |A:REM Wieder Umschalten auf Laufwerk A (X-Laufwerk)
```

> **(!) Important**
>
> If you start CP/M or reset the computer (pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time, switching the computer off/on), drive A is the 3" drive again and drive B the X drive. That is, the drive configuration under CP/M is fixed when CP/M is loaded (booted).

---

## The VDOS Commands CAT and |DIR

**Viewing the disk directory**

Just as every book has a table of contents listing all of its chapters, every disk has a directory listing all of the files that are on it. Instead of the German word "Inhaltsverzeichnis", the English word "directory" is usually used. You will also often come across the English word "catalog".

VDOS has two commands that show the directory on the screen. We have already used one of them several times: it is the `|DIR` command (derived from DIRectory). The other command is called `CAT` (from CAtalog) and has a small peculiarity: you don't need the vertical bar `|` to use it. The reason is simply that you will find this command in your CPC even without a vortex X drive, and as already mentioned, only external commands (commands that are added by plugging in the floppy or other peripherals) need the vertical bar.

The simpler of the two commands is `CAT`. Here is how it is used:

```
CAT<ENTER>

Laufwerk A: User  0

| Datei      | Größe | Datei       | Größe |
|------------|-------|-------------|-------|
| $OSC   .SYS | 3K   | PIP    .COM | 8K   |
| FAST   .COM | 1K   | READ   .BAK | 1K   |
| HELLO  .BAS | 1K   | READ   .ME  | 1K   |
| MAN    .003 | 19K  | STAT   .COM | 6K   |
| MAN    .004 | 27K  | VDOS   .BAK | 6K   |
| MAN    .005 | 5K   | WS192N .COM | 16K  |
| MAN    .006 | 1K   | WSMSGS .OVR | 30K  |
| MAN    .007 | 15K  | WSOVLY1.OVR | 34K  |
| MAN    .BAK | 15K  |             |      |
228K in  17 Files, 480K frei
Ready
```

This is, for example, the contents of my WordStar work disk. We get information about the size of the individual files, how many files are on the disk and how much space is still free or already used. In addition, the files are sorted alphabetically.

One more important note here: with the vortex X drive, a maximum of 128 files can be created per disk. On a 3" drive there are only 64.

> **(!) Note:** On the vortex floppy, 128 directory entries are possible. On the 3" floppy only 64!

So `CAT` is a simple command that quickly gives you important information. But this command lacks one important feature: "filtering out" very specific files.

This is where the `|DIR` command becomes interesting. In connection with this feature I have to briefly explain the meaning of the term **wildcard**:

It may often happen that you use one and the same disk for BASIC/VDOS and CP/M. So there are files on this disk that are of no use to you under CP/M, and vice versa. Further above I showed you that, for example, files of type `BIN` are typical for BASIC, whereas a file of type `COM` is a typical CP/M file. It would be very handy if, under BASIC, we could "search" the disk for files of type `BIN` only. That is, only these files should be shown to us.

So we need a command that makes it possible to output certain files or groups of files selectively. For exactly this job we have the `|DIR` command. Here is an example:

```
|DIR,"*.COM"<ENTER>

Laufwerk A: User  0

FAST    .COM    PIP     .COM
STAT    .COM    WS192N  .COM

228K in   4 Files, 480K frei
```

All files of type `COM` were shown.

```
|DIR,"MAN.*"<ENTER>

Laufwerk A: User  0

MAN     .003    MAN     .004
MAN     .006    MAN     .005
MAN     .007    MAN     .BAK

228K in   6 Files, 480K frei
```

We were shown all files with the file name "MAN".

```
|DIR,"MAN.00?"<ENTER>

MAN     .003    MAN     .004
MAN     .006    MAN     .005
MAN     .007

228K in   5 Files, 480K frei
```

Here only those files were output whose file name is `MAN` and whose type is 3 characters long, where the first two characters must be "00" and the 3rd character can be anything, but must be present (a file `MAN.00` would not have been shown).

The two characters `*` and `?` are so-called wildcard characters.

- A `?` always allows any character only in the position where it stands (but a character must be present).
- An asterisk `*` always allows all remaining characters to be anything.

The difference between the two characters is also demonstrated by the following equation (not a mathematical one!):

```
????????.??? = *.*
```

As you have surely noticed, `CAT` and `|DIR` always show this message in the first line:

```
Laufwerk A: User  0
```

What is that all about? Quite simple: the text `Laufwerk A` tells us that a directory of the disk in drive A is being output here. It is one of 16 possible directories. When VDOS was developed, it was taken into account that several users might have to share a single disk. So that there is no confusion (who owns which file?), the disk can be divided into up to 16 user areas (see the `|SELECT` command). Note, however, that the total number of files – from all user areas – may never exceed 128 and that the total size of all files never exceeds 704 KB. In both cases the disk is then full.

On the 3" drive, the total number of files must not exceed 64. The total of all file sizes must stay at or below 169 KB.

---

## The VDOS Command |ATTRIBUT

**Protecting a file / making a file "invisible"**

You are surely familiar with the option of protecting an entire disk from being "written to" (erasing is writing too!). It is a mechanical protection: on a 5.25" disk simply by a small sticker folded around the edge, on 3" and 3.5" disks by a small slider on the disk itself.

But if you want to write-protect one particular file, you need the VDOS command `|ATTRIBUT`. This command can give files a so-called **attribute**. The attribute gives us information about the "state" of the file. VDOS distinguishes the following common attributes:

| Attribute | Meaning |
|----------|-----------|
| **S** | The file is a so-called "SYS" or "system" file. It is no longer shown when you enter the commands `CAT` and `|DIR`; it is "invisible". |
| **D** | The file is a so-called "DIR" or "directory" file. It is shown by the commands `CAT` and `|DIR`. If you don't change anything in the file attributes, all files have this attribute and the next one. |
| **W** | The file is R/W (read/write), i.e. it can be written and read. It can also be erased. |
| **R** | The file is R/O (read only), write-protected. So it cannot be erased either. |

As already mentioned, all files in their "original state" (without you having changed anything!) have the two attributes "D" and "W".

The `|ATTRIBUT` command is used like this:

```
|ATTRIBUT,"PIP.COM","R"<ENTER>
```

The file `PIP.COM` is marked as "read only". So it can no longer be erased. If we take a look at the disk with `CAT`, we see that this file has been marked.

```
CAT<ENTER>

Laufwerk A: User  0
```

| File      | Size | File       | Size |
|------------|-------|-------------|-------|
| $OSC   .SYS | 3K   | PIP    .COM# | 8K  |
| FAST   .COM | 1K   | READ   .BAK | 1K   |
| HELLO  .BAS | 1K   | READ   .ME  | 1K   |
| MAN    .003 | 19K  | STAT   .COM | 6K   |
| MAN    .004 | 27K  | VDOS   .BAK | 6K   |
| MAN    .005 | 5K   | WS192N .COM | 16K  |
| MAN    .006 | 1K   | WSMSGS .OVR | 30K  |
| MAN    .007 | 15K  | WSOVLY1.OVR | 34K  |
| MAN    .BAK | 15K  |             |      |

```
228K in  17 Files, 480K frei
Ready
```

All files marked with `#` are write-protected.

Let's jump ahead a little: try to erase the file `PIP.COM` by entering the following line:

```
|ERA,"PIP.COM"<ENTER>

PIP    .COM hat Schreibschutz

Ready
```

As you can see, this file cannot be erased this way.

> **(!) Note:** Please be aware, though, that this "protection" is of course useless when you use the `|FORMAT` command. That command ruthlessly destroys everything on the disk!

Of course you can also undo this attribute again:

```
|ATTRIBUT,"PIP.COM","W"<ENTER>
```

The file can now be erased again.

---

## The VDOS Command |ERA

**Erasing a file**

With this command you can erase files, groups of files or even entire disks. This command always refers to the currently set user area (see `|SELECT`). ERA is derived from "Erase".

With the following line

```
|ERA,"TEST.BAS"<ENTER>
```

the file `TEST.BAS` is erased from the disk currently inserted. Had it carried the "R" attribute, we could not have erased it. If this file does not exist on this disk at all, VDOS tells us:

```
TEST    .BAS wurde nicht gefunden
```

With this line here

```
|ERA,"TEST.*"<ENTER>
```

all files (e.g. `TEST.BAS`, `TEST`, `TEST.COM`, `TEST.123`, `TEST.12`) in the current user area on this disk are erased. Besides this wildcard character `*`, the other one, `?`, can also be used.

The following line should only be entered when you are fully aware of what you are doing, because it erases the disk completely:

```
|ERA,"*.*"<ENTER>
```

All files "match" this wildcard (`*.*`), so all of them are erased. So please always be careful here. Cases where you have to erase entire disks are surely very rare anyway.

If `|ERA` with a wildcard comes across a write-protected file, VDOS reports `<datei> hat Schreibschutz` and stops: the files that come before it in the directory have then already been erased, all following ones are kept.

> **(!) Important: CAUTION!**
>
> `|ERA,"*.*"<ENTER>` erases the whole disk!

The following would also be possible:

```
|B<ENTER>
|ERA,"A:PIP.COM"<ENTER>
```

With this we first switched to drive B and from there erased the file `PIP.COM` on the disk in A.

---

## The VDOS Command |REN

**Changing a file name**

It will surely happen at some point that you no longer like a file name you already gave, or that you need it somewhere else. To change the file name we have the command `|REN` (REN stands for Rename). No wildcards are allowed here, because they would make no sense.

```
|REN,"DATEI.NEU","DATEI.ALT"<ENTER>
```

The file named `DATEI.ALT` is renamed to `DATEI.NEU`. If a file named `DATEI.NEU` already exists, the command is aborted and VDOS tells us:

```
DATEI   .NEU existiert bereits
```

You must first erase this file or copy it somewhere else. If the file `DATEI.ALT` does not exist, VDOS outputs this:

```
DATEI   .ALT wurde nicht gefunden
```

The following line

```
|REN,"B:TEST.123","B:SPIEL.BAS"<ENTER>
```

renames, from drive A, the file `SPIEL.BAS` on the disk in B to `TEST.123`, also on B.

> **(!) Note:** Note that renaming can only ever take place on one and the same disk. A line such as `|REN,"A:DDT.COM","B:SID.COM"<ENTER>` would make no sense.

---

## The VDOS Command |SELECT

**Setting the user areas**

Under VDOS (and, by the way, also under CP/M) the disk can be divided into up to 16 user areas. This division can make sense when several users share a disk and don't want to get in each other's way. But of course, even as the only user of the disk you can set up several user areas. That way it is possible to give the disk a clean structure. Usually, however, you will use this command rarely and stick to user area 0.

The following line

```
|SELECT,"6"<ENTER>
```

switches to user area 6. If we now enter `CAT`, its top line shows the information:

```
Laufwerk A: User  6
```

and then lists the files that are in this user area on the screen.

In addition to the user number, you can also give the drive letter (A or B). The user number must come **before** the drive letter:

```
|SELECT,"5B"<ENTER>
```

switches to user area 5 on drive B. (With `|SELECT,"B5"` only drive B is selected; everything after the drive letter is ignored.)

If we now enter, for example,

```
CAT<ENTER>
```

then we get as the first line of the "catalog":

```
Laufwerk B: User  5
```

If you make use of the notation with the "at sign" `@` here, the user number and the drive letter can be given "dynamically" within a BASIC program:

```basic
10 INPUT "Laufwerkskennung ",A$
20 INPUT "USER-Nummer ",B$
30 C$=B$+A$
40 |SELECT,@C$
50 CAT
```

Depending on the drive letter and user number entered, we get the directory of the corresponding area on the corresponding disk.

Valid user numbers are 0 to 15. On a wrong entry VDOS reports `Eingabefehler`. Note: if the error only comes after the user number (e.g. `|SELECT,"3C"`), user area 3 has already been set anyway.

**The VDOS commands |USER and |DRIVE**

VDOS 2.11-X knows two more commands for this:

```
|USER,9<ENTER>
```

switches only the user area (here to 9); the number must be between 0 and 15, the drive stays unchanged. `|DRIVE` is just another name for `|SELECT` (so `|DRIVE,"B"` works like `|SELECT,"B"`).

---

## The VDOS Command |RESET

**Changing disks**

Imagine you have opened a file for writing, and data is written into this file from time to time. If you now swap the disk in between, this can lead to data loss, because the file is still "open".

This command serves to tell VDOS that you have changed the disk in one and the same drive during a write operation.

You should get into the habit of entering this command before changing the disk, especially if you are not sure whether a file is still open for writing. If that is the case and you forget `|RESET<ENTER>`, the last 64 KB of data may be lost. If you closed the file properly (`CLOSEOUT`, `|CLOSE`) before changing the disk, `|RESET` is unnecessary.

If you have already dealt a little with CP/M, you will recognize a certain kinship with `CTRL`+`C` under CP/M here.

---

## The VDOS Command |CODE

**Program protection!**

Earlier I mentioned the option of protecting a program from "listing" with the `SAVE` command and the "P" (simply P protection). Unfortunately this protection (which you also have without the vortex floppy) has become rather useless, because it was "cracked" early on. In principle you can say: there is no protection that cannot be bypassed. You can only make things harder, but never stop them.

With the VDOS command `|CODE` you can build in a personal program protection. Say you want to protect the program `TEST.BAS`:

With the following lines

```
|CODE,12325<ENTER>
SAVE "TEST",P<ENTER>
```

you have given `TEST` a personal encoding key (12325). Now enter `|CODE,0<ENTER>`. With this, or also by resetting the computer (press `CTRL`+`SHIFT`+`ESC` at the same time), you activate the protection.

Now enter `RUN "TEST"<ENTER>`. Complete nonsense comes out, because the "key" was not given. So enter `|CODE,12325<ENTER>` and start `TEST` again. Everything works!

The number for the `|CODE` command must lie between `-32768` and `32767`; that still gives you 65536 ways to protect your program.

---

## The VDOS Command |AMSDOS

**Switching on the AMSDOS operating system**

Entering `|AMSDOS<ENTER>` switches VDOS off and AMSDOS on at the same time. If you have programs that do not work under VDOS without adaptation, you can switch to AMSDOS and all problems are solved.

Once you have switched to AMSDOS, it is as if you had connected a simple second drive to your CPC.

This command performs a RESET. That is, all data that was in memory before is erased!

> **(!) Important:** `|AMSDOS<ENTER>` erases all data in memory.

When you have switched to AMSDOS, note that the X drive then has not 708 KB but only 169 KB (like the 3" drive) of formatted storage capacity. This is because AMSDOS can only handle drives with 40 tracks and one read/write head (which also gives the storage capacity of about 170 KB).

All X drives are 80-track drives with two read/write heads. Under AMSDOS the disk in the X drive is used on one side only and with only 40 tracks. Note, however, that the 40 tracks are not spread evenly over the radius of the disk but use only the outer half. So it is as if the drive handled 80 tracks but actually used only the first 40.

It is important that a disk created under AMSDOS in the X drive must never be used under VDOS in the X drive.

> **(!) Important**
>
> A disk created under VDOS must never be used under AMSDOS. Conversely, a disk created under AMSDOS must never be used under VDOS either.
>
> If you ignore this, the contents of the disks concerned will be destroyed beyond recovery.

Resetting the CPC (pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time) switches VDOS on again.

---

## Cassette Recorder on the CPC

The first of the CPCs, the CPC464, comes with a built-in cassette recorder as standard; the others, the CPC664 and the CPC6128, can be fitted with a cassette recorder later. If you also have a disk drive, it is of course important to be able to transfer data between disk and cassette.

On the CPCs there is a so-called input channel and a so-called output channel between the computer and the mass storage (= floppy or cassette recorder). If you have connected a floppy and a cassette recorder and want, for example, to move data from the floppy to the recorder, you only have to route the output channel to the recorder and the input channel to the floppy.

It should be mentioned that after switching on the CPC with a floppy connected, the input and output channels are assigned to the floppy, no matter whether a cassette recorder is also present.

There are exactly six ways to "wire" the two channels. For each case there is a corresponding VDOS command.

### The VDOS Command |DISC

The input and output channels are assigned to the disk drive. This is the "power-on state" of the CPC with a floppy connected. When data is read or written, it is read from the floppy or written to the disk in the floppy.

### The VDOS Command |CAS

The input and output channels are assigned to the cassette recorder. If you have a CPC464 and disconnect the floppy, this corresponds exactly to this state. Read/write operations always refer to the recorder.

If you enter, for example, `|CAS<ENTER>` and `CAT<ENTER>` here, the message `Press PLAY then any key` appears. So we are supposed to press the Play key on the recorder. We would then get a directory – if there is one – of the cassette in the recorder. That this will of course take a while is obvious.

### The VDOS Command |DISC.IN

The input channel is assigned to the disk drive. That is, when data is read now, it comes from the floppy.

### The VDOS Command |CAS.IN

The input channel is assigned to the recorder. That is, when data is read now, it comes from the recorder.

### The VDOS Command |DISC.OUT

The output channel is assigned to the floppy. When a write operation now takes place, the data is written to the disk in the drive.

### The VDOS Command |CAS.OUT

The output channel is assigned to the recorder. The data is now written to the cassette in the recorder.

If you want, for example, to copy a file from disk to cassette, it could look like this:

```
|CAS.OUT<ENTER>
|DISC.IN<ENTER>
LOAD "TEST"<ENTER>
SAVE "TEST"<ENTER>
```

The `LOAD` command would refer to the disk and the `SAVE` command to the cassette. After pressing the last ENTER, the following would then be reported:

```
Press REC and PLAY then any key:
```

the request to set the recorder to recording mode.

VDOS 2.11-X also has the commands `|TAPE`, `|TAPE.IN` and `|TAPE.OUT`. They are just other names for `|CAS`, `|CAS.IN` and `|CAS.OUT` and work exactly like them.

---

## The VDOS Command |XMON – The vortex Z80 Monitor

Behind this command hides a very powerful and capable Z80 machine-code monitor. **Monitor** has nothing to do with a screen or the like. A monitor is a program that helps you test other machine-code programs. You use it to find the errors that may still be in this machine-code program.

For errors, people also like to use the English word "bug" (German "Wanze"). That is why the name "debugger" has also become established for a monitor.

Then it also says "Z80". You probably know why long ago. Right, it is because your CPC has the Z80 microprocessor built in.

The main functions of the monitor are:

- Disk monitor
- HEX/ASCII dump
- Mnemonic listing/disassembly
- Breakpoints
- Tracer

It must be said quite clearly that the monitor is not a toy. You will only understand what it is good for and everything it can do once you have worked your way at least a little into Z80 machine language (for this I recommend the book by Rodnay Zaks "Der Z80", published by Sybex Verlag).

If you know nothing at all, you should keep your hands off `|XMON` for the time being. Insiders will hardly need me to explain the undreamed-of possibilities this "tool" opens up.

The monitor is started by entering

```
|XMON<ENTER>
```

The screen is cleared and the monitor prompt `*` appears. XMON now expects command input from us.

You leave the monitor by pressing the `ESC` key. If, for example, you called the monitor from within a program and leave it again with `<ESC>`, that program continues exactly at the point where the monitor was called before.

Below, all monitor commands are shown in alphabetical order. Note that requested or displayed values are always shown in hexadecimal form, where 8-bit values are, or must be, two digits and 16-bit values four digits.

### `Aadresse<ENTER>` – Enter a Text String

```
*A3000<ENTER>
```

Allows a whole text string to be entered into memory starting at address `3000H`:

```
*A3000,Dies ist ein Test String<ENTER>
```

The string can contain at most 255 characters.

### `@` – Start the Disk Monitor

The character `@` is called the "at sign" (in German the "Klammeraffe", the "clinging monkey") and is produced by pressing the corresponding key (between `P` and `[`). XMON has a small disk monitor. It is called with

```
*@
```

(no `<ENTER>`) and then reports with

```
L:01  T:02  S:00  B:A8BA  G:00
>
```

The `>` is the prompt of the disk monitor. The individual entries in the status line have the following meaning (numeric values are shown in hexadecimal and must also be entered in hexadecimal):

| Entry | Meaning |
|---------|-----------|
| `L:xx` | Drive number `xx=00` or `01` for logical drive A or B. On entry, `xx` contains the number of the currently selected drive. |
| `T:yy` | Track number. Range `0..27H` (3" drive), `0..9FH` (5.25"/3.5"). On entry, this shows the first track after the reserved system tracks. |
| `S:zz` | Record number (one record = 128 bytes) within the track, counted from `00`. Range `00` to number of records per track – 1 (e.g. `00..23H` on the vortex X drive). You don't need to give the physical sector numbers (`41H..49H`, `C1H..C9H`, `01..09`); the format of a 3" disk is detected automatically. |
| `B:abcd` | Buffer address for record writing/reading. When the disk monitor starts, this holds a record buffer 80H bytes below the BIOS host buffer (see the internals part). |
| `G:xx` | CP/M block number of the set position. Only shown outside the reserved system tracks. |

Here now is the explanation of the individual disk monitor commands:

| Command | Function |
|--------|----------|
| `>Lxx<ENTER>` | Change drive number (T, S and B are set to their start values) |
| `>Sxx<ENTER>` | Change record number |
| `>Txx<ENTER>` | Change track number |
| `>Gxx<ENTER>` | Go to the start of CP/M block `xx` (T and S are calculated). Only blocks `00..FFH` can be given. |
| `>Babcd<ENTER>` | Set buffer address |
| `>R` | Read the record with the coordinates defined by L, T and S into the buffer |
| `>W` | Write the buffer contents into the record with the coordinates L, T and S |
| `>Cabcd<ENTER>` | Change the contents of memory locations in the buffer. Fully corresponds to the monitor command S (see there as well). |
| `>Aabcd<ENTER>` | Enter a string (see above) |
| `>Fadresse1,adresse2,wert<ENTER>` | Fill a memory area. Corresponds to the monitor command F |
| `>P` | Switch printer on/off. Corresponds to the monitor command P |
| `>Dabcd<ENTER>/,xx<ENTER>/` | Output the buffer contents as a HEX/ASCII dump on the screen. Optionally you can also give the total number of records to be dumped; they are then read in and output one after the other. |
| `><ESC>` | Return to the monitor |

All entries are checked both syntactically and logically. If you make an input error, the disk monitor jumps back to its main command loop and reports with `>>` to show you the error – nothing has been changed then. (Exception: with the commands T and G the wrong position stays set, see [Known bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x).)

If a disk error occurs while reading or writing, the disk monitor reports with

```
E:xx
```

and jumps back into the command loop. `xx` contains the error code (hexadecimal) (see the section "Ways of Trapping Disk Errors").

### `B<ENTER>` – View/Change Breakpoints

The monitor lets you set up to eight breakpoints (test points) anywhere you like (B stands for Breakpoints). When the program being tested arrives at such a point, it is stopped, the prompt `*` is output and you can take your time looking at the registers and checking whether everything has gone right so far.

The breakpoints are set with the B command:

```
*B<ENTER>

-B1-   -B2-   -B3-   -B4-   -B5-   -B6-   -B7-   -B8-
0000   0000   0000   0000   0000   0000   0000   0000
```

You can then change the first breakpoint or move on to the next breakpoint with `<ENTER>`, and so on, until after the eighth breakpoint, or by pressing `<ESC>`, the monitor prompt `*` appears again.

### `Dadresse1,adresse2<ENTER>` – Listing in HEX/ASCII Form

The D command (D stands for Dump) lets you display memory contents in the following format:

```
0100 00 00 41 00 33 57 00 00 00 51 00 35 00 00 00 00  ..A.!9...3.#.
```

At the start of the line you are shown the address (`0100H`) in memory from which 16 address contents are shown in this line. Then come the 16 values (hexadecimal) and on the far right their ASCII translations: if the value is less than 32 or greater than 127, a dot `.` is output, otherwise the actual ASCII character.

If, after pressing the D key, you enter only one address (`adresse1`), the following `100H` memory contents are output. But if after `adresse1` you press the comma key instead of `<ENTER>`, you can enter a second address (`adresse2`). The memory contents from `adresse1` to `adresse2` are then "dumped" in HEX/ASCII form. You can pause such a listing briefly by pressing any key (the space bar is a good choice) and restart it by pressing again. If you press `<ESC>` after pausing, the monitor prompt `*` appears again.

### `Fadresse1,adresse2,wert<ENTER>` – Filling a Memory Area with a Particular Value

It often happens that certain memory areas are to be cleared, for example. With the F command (F stands for Fill) this is no problem. But you should watch what you fill. There are areas where a program is actively running. If you simply fill those, the whole computer may crash, so be careful!

```
*FC000,FFFF,FF<ENTER>
*
```

fills the screen memory (addresses `&C000` to `&FFFF`) with the value `FF`.

### `Gadresse<ENTER>` – Running a Machine-Code Program

This command (G stands for Go) runs a machine-language program located at the given `adresse`. If a breakpoint (see further above) is reached, control returns to the monitor and the prompt `*` appears.

```
*GBD19<ENTER>
```

runs the machine-language program starting at address `BD19`.

### `Idateiname.dateityp<ENTER>` – Loading a Binary File from Disk/Cassette

With this command (I stands for Input) a binary file (file type `BIN`) can be loaded into the monitor. If, for example, you entered `|CAS.IN<ENTER>` before starting XMON, the file you request in XMON is loaded from cassette. If you entered nothing, it is loaded from disk.

The binary file is loaded into its original memory, i.e. into the memory area from which it was created. The load address, the length and a start address, if there is one, are displayed.

```
*ITEST.BIN<ENTER>
(2000 0380 2140)
*
```

loads the file `TEST.BIN` into memory. The determined start address is `2000H`, the length `380H` and the entry address `2140H`.

The file must have a file header, like the one written e.g. by `SAVE "name",B`. Files without a header (e.g. files created under CP/M) are reported with length 0.

### `Ladresse1,adresse2` – Disassembling a Memory Area

Entering the addresses and their meaning are the same as for the D command (see further above), except that the memory contents are shown as mnemonics.

```
*L0100,0106<ENTER>
0100 3E64       LD A,64H
0102 ED5B3204   LD BC,(0432H)
0106 E3         EX (SP),HL
*
```

Lists the area from `100` to `106`. First comes the address, then its contents in hexadecimal form and then the readable Z80 mnemonic.

### `Madresse1,adresse2,adresse3<ENTER>` – Moving Memory Areas

The contents of the memory area between `adresse1` and `adresse2` are copied into the memory area starting at `adresse3`. You have to be a little careful here that `adresse3` does not lie within the area `adresse1`/`adresse2`, or so close before `adresse1` that the areas overlap.

```
*M0000,3FFF,C000<ENTER>
```

copies the area `0`-`3FFF` into the memory area starting at address `&C000` (= screen memory).

### `Odateiname.dateityp<ENTER>adresse1,länge,adresse2` – Saving a File

Once you have entered a valid file name after the O (O stands for Output), you are asked, like with the BASIC command `SAVE "name",B`, for the start address of the memory area, its length and an entry address. This memory area is then written to disk/cassette under the name you entered.

```
*OTEST.BIN<ENTER> C000,4000,0000
*
```

The memory area from `&C000` to `&FFFF` is saved into the binary file `TEST.BIN` without an entry address.

### `P` – Printer On/Off

If a printer is connected, pressing the P key once makes it record the screen output as well. Pressing the P key again switches the printer off again. (P stands for Print.)

### `R` – Displaying/Changing the Register Contents

This command (R stands for Registers) lets you change the register contents used for running a machine-language program (with the G command or T command). They are shown like the breakpoints and changed the same way. Only the main register set can be changed.

### `Sadresse<ENTER>` – Displaying and Changing Memory Contents

After entering S (S stands for Substitute) and the `adresse`, you see its contents and can change them in a third column. By pressing `<ENTER>` you move on to the next memory location; the possibly changed value of the old address is stored into it. Pressing `<ESC>` takes you back to the monitor prompt `*`.

```
*S4000<ENTER>
4000  24  34<ENTER>
4001  43  32<ENTER>
4002  58  44<ENTER>
4003 <ESC>
*
```

Changing from memory location `4000`. The old values of the addresses `4000`, `4001` and `4002` (`24`, `43` and `58`) are replaced by the new values (`34`, `32` and `44`).

### `Tadresse,anzahl<ENTER>` – Running a Machine-Code Program Step by Step

With this command a machine-code program can be run step by step in order to discover any errors it may contain. It starts from the register values entered with the R command, and control is returned to the monitor after each step, i.e. you see the possibly changed registers and can also interrupt the run if you gave an optional number of steps. You make this interruption, as usual, with `ESC`.

> **(!) Note:** Please note that programs in ROM, or instructions that work with the Z80's alternate register set, cannot be run step by step. Furthermore, the stack pointer SP should not lie under a ROM, as this can crash the system.

```
*T4000,0007<ENTER>
```

runs seven steps from address `4000H`. The register contents are always displayed, and the run can be paused (press the space bar) or aborted (`<ESC>`) as with the D command.

### `X` – Firmware ROM On/Off

Just like the command `P` (see above), the command `X` is also a toggle. After the monitor is started with `|XMON<ENTER>`, `X` is off, i.e. the internal RAM is visible in the address space from `0000H` to `3FFFH`. If you now enter the `X` command (like `P`, it does not need to be sent with `<ENTER>`), you see the firmware ROM from `0000H` to `3FFFH`.

### `Y` – Selecting the Upper ROM

If you enter a `Y`, the monitor gives you a list of all expansion ROMs in the system (it is the same list that the VDOS command `|ROMCAT` outputs, only without the "Himem" line). This list is structured as follows:

```
xy rssbvw name
......
......
```

Here:

| Field | Meaning |
|------|-----------|
| `xy` | Number of the expansion ROM |
| `rs` | ROM mark number |
| `ab` | ROM version number |
| `vw` | ROM modification number |
| `name` | RSX name of the ROM WALK routine |

Directly after the ROM list comes

```
Vac   (ac=aktueller Erweiterungs-ROM)
```

and the monitor waits for your input. You can now change the expansion ROM number (finish the input with `<ENTER>`). Allowed expansion ROM numbers are between `00` and `FBH`.

`ac` is always the ROM you see in the address range `&C000` to `&FFFF`. If you enter the number of a ROM that does not exist, the monitor always switches in the built-in BASIC ROM. If you want to see the contents of the screen memory, enter a ROM number between `FCH` and `FFH`. With `<ESC>` the old ROM number is kept.

> **(!) Note:** The command `Y` uses the same memory area as the breakpoints. Breakpoints set before `Y` are lost afterwards. Under CP/M (CP/M command `XMON`) `Y` has no effect; there you always see the VDOS ROM in the range `&C000` to `&FFFF`.

### `C` – Searching for Byte Sequences

With the C command you can search memory for single bytes or for whole byte sequences. The maximum length is 255 bytes.

```
Cabcd<ENTER>,xy<ENTER>
```

| Parameter | Meaning |
|-----------|-----------|
| `abcd` | Address of the byte sequence |
| `xy` | Length of the byte sequence |

You must first place the byte sequence in memory with the S or A command (see above).

The C command then gives you a list of all addresses where it found the byte sequence.

### `Z` – Selecting the RAM Bank of the vortex RAM Expansion

This command is new in VDOS 2.11-X. With `Z` you select which bank of the vortex RAM expansion the monitor switches in for its memory accesses (D, L, S, ...). The monitor shows the current setting and waits for your input (two digits, finished with `<ENTER>`; `<ENTER>` alone keeps the value):

| Input | Meaning |
|---------|-----------|
| `00` | no bank, the normal memory of the CPC |
| `01`..`08` | bank 0 to 7 of the RAM expansion |

```
*Z03<ENTER>
```

switches in bank 2.

---

## The VDOS Command |ROMOFF

The command `|AMSDOS` selectively switches off only the VDOS ROM, i.e. none of the RSX commands of the VDOS ROM are available any more. Among others, the command `|DISBOS` of the vortex RAM card works in exactly the same way as `|AMSDOS` – it selectively switches off the BOS ROM. The conflict is obvious, because these two commands cannot switch off the VDOS ROM and the BOS ROM at the same time. For this reason the command `|ROMOFF` was built in, which lets you switch off several ROMs at once.

```
|ROMOFF<ENTER>
```

switches off all background ROMs.

```
|ROMOFF,6,7<ENTER>
```

switches off only the background ROMs with numbers 6 and 7. (ROM numbers 0..7 can be given here.)

Of course you can switch the background ROMs on again by resetting your CPC (power off/on or pressing the keys `CTRL`+`SHIFT`+`ESC` at the same time).

---

## The VDOS Command |ROMCAT

The VDOS command `|ROMCAT` (in VDOS 2.0 it was called `|ROMS`) first outputs the current HIMEM value and then builds a table of all ROMs with numbers between 0 and 7 that looks like this:

```
|ROMCAT<ENTER>

Himem: A677
...
05 01 01 21 03 A6FC V ROM
...
07 01 00 05 00 A700 CPM ROM
```

Each line contains the ROM number, the ROM type (`01` = background ROM, `80` = BASIC), the ROM mark, version and modification numbers, the address of the data area the ROM has reserved for itself (`----` for ROMs that have none), and the name of the ROM. For an empty slot the built-in BASIC ROM is shown.

With

```
|ROMCAT,5<ENTER>
```

all commands of ROM number 5 are listed with their entry addresses. If you hold down `<ESC>`, the list pauses; another `<ESC>` aborts it, any other key continues it.

So if you want to work with the VDOS command `|ROMOFF`, you can first find out with the VDOS command `|ROMCAT` the numbers of the background ROMs you want to switch off.

---

## The VDOS Commands |FAST, |SLOW and |FRAME

These three commands are new in VDOS 2.11-X.

`|FAST<ENTER>` speeds up text output on the screen, similar to the CP/M command `FAST`. It only works in MODE 2; in MODE 0 and MODE 1 everything stays as it was.

`|SLOW<ENTER>` switches the fast text output off again (the firmware output is restored).

`|FRAME<ENTER>` waits for the next frame flyback (like `MC WAIT FLYBACK` in the firmware), e.g. to produce flicker-free graphics.

None of the three commands needs parameters; any parameters given are ignored.

---

## Random-Access (Relative) and Sequential File Handling

So far we have only ever talked about files whose contents were a program (program files).

Imagine you want to write a small address book program in BASIC that lets you manage the addresses (name, street and so on) of your friends, i.e. enter, change and search them. But that requires that you can store this "data" permanently (on disk or cassette). So you have to build your program in such a way that it creates an address file holding all the addresses. This file would be a pure data file; its contents would not be an executable program.

If you do not have a vortex floppy connected to your CPC, then you also lack the VDOS operating system. You then have two so-called "channels" (an input channel and an output channel, see also the `|CAS` and `|DISC` commands, section "Cassette Recorder on the CPC") through which you can send data to the cassette recorder or to the 3" drive, if you have one, and also receive data from there (the English technical terms for these are INPUT stream and OUTPUT stream).

That means you can only ever have one file "open" for writing and one file open for reading at the same time. Before you can "access" a file, it first has to be "opened". When you no longer need the file for the moment, it has to be closed again.

So you cannot open two files for writing at the same time, or two files for reading at the same time. This is of course a certain limitation, but one you can live with.

A far bigger drawback is that the contents of these files can only be read one after the other and can only be written one after the other. This "one after the other" describes the way these files are "managed" by the operating system. That is why this kind of file handling is called **"sequential file handling"**.

If, for example, you have 1000 addresses in your address file and want to read the last one, you first have to read your way through the 999 addresses before it. That takes time and does not bring much efficiency to the whole affair.

The existence of sequential file handling has historical reasons. The first Schneider (the CPC464) was equipped only with a cassette recorder. It is really obvious that file handling can only be sequential there, because the storage medium is a tape. If you want to get from X to Y, the whole tape in between has to run past.

Then came the 3" drives. Practically little was changed in the operating system; the cassette recorder was "simply" replaced by the drive. Sequential file handling stayed, even though a lot more can be done with a disk drive.

Below you will find a small example of sequential file handling.

Typical BASIC commands that come up in connection with reading a sequential file are:

```
OPENIN   EOF   INPUT#9   LINE INPUT#9   CLOSEIN
```

Typical BASIC commands that come up in connection with writing a sequential file are:

```
OPENOUT   PRINT#9   WRITE#9   CLOSEOUT
```

```basic
10 OPENOUT "ZAHLEN.DAT"
20 FOR A=1 TO 100
30 A$=STR$(100)
40 PRINT#9,A$
50 NEXT
60 CLOSEOUT
70 OPENIN "ZAHLEN.DAT"
80 INPUT "Welche Zahl suchen Sie",ZAHL
90 ZAHL$=STR$(ZAHL)
100 INPUT#9,VAR$
110 IF ZAHL$=VAR$ THEN GOTO 140
120 Z=Z+1
130 GOTO 100
140 PRINT "Die Zahl steht an der",Z,"ten Position in der Datei"
150 CLOSEIN
160 END
```

Line 10 opens the file `ZAHLEN.DAT` for writing. If it did not exist before, it is created now. Inside the `FOR/NEXT` loop the numbers 1 to 100 – converted into strings – are written into this file with `PRINT#9,A$`. Line 60 closes the file properly.

In 70 the file is opened again for reading. We are looking for a certain number, or rather its position in the file `ZAHLEN.DAT`.

Line 110 shows a comparison that is typical for sequential files: you have to "compare your way through" the file until you have found the record you were actually looking for.

So, now we connect the vortex X drive and with it we have VDOS! Of course it also handles the sequential file handling just described. But it can do a great deal more. It gives you **"random-access (relative) file handling"**.

What distinguishes random-access file handling is that a record can be fetched from, or written to, any position in the file without having read all the records before it first. Any record can be accessed at random by its record number, which of course saves time and programming effort.

In addition to the 2 sequential channels, VDOS also lets you open up to 16 (!) random-access channels at the same time. With that, just about any problem you are faced with should turn into a program in the best possible way.

Like sequential files, random-access files consist of records. Unlike in a sequential file, however, these records are completely independent of one another in a random-access file. Every record has a number by which it can be selected. They can be read or written in any order. The length of a record can be chosen freely within certain limits.

For every open random-access file a certain area is reserved in RAM, the so-called "record buffer". Whenever a record is read or written, the record always passes through this buffer on its way out of the file or into the file. Clearly the size of this buffer depends on the record length that has been chosen.

Note that the record length cannot be changed while a random-access file is open.

Another difference between the two "kinds of file handling" is that in a random-access file the records can be given a further structure; you also say the record can be divided into several "fields".

So you can say that a random-access file consists of a certain number of records, with every record divided into a certain number of fields. The division into fields in a random-access file must be the same for all records.

Every open random-access file needs memory in RAM for its record buffer, for its FCB (File Control Block, which also holds the name of the random-access file) and for a number of internal pointers and counters (all in all 90 bytes + record buffer per channel).

This memory is reserved when the channel is defined (see the `|FILES` command) in the upper memory area of the CPC by dynamically lowering `HIMEM`. Once a channel has been defined, a random-access file can be opened on it (see the `|OPEN` command). Note that record lengths have to be given both when defining the channel (`|FILES`) and when opening a file on this channel (`|OPEN`).

There is an easily understood reason for this: it is perfectly possible to open and close several random-access files one after the other on one channel without having to define the channel (`|FILES`) every time. You give the largest record length you expect only once, when defining the channel, and later open the individual files (`|OPEN`) with their own individual record lengths.

After a random-access file has been opened (`|OPEN`), the record buffer has to be structured for the file before the first access to the file (`|PUT`, `|GET`), i.e. divided into fields (`|FIELD`); that is, you have to state which parts of the record are to be read into variables on access.

Now the random-access file is ready for data transfer, and until the file is closed (`|CLOSE`) you can read and write records at random (people often also say randomly, which is where the English term "random file" that you sometimes come across comes from).

> **(!) Note:** Note that only string variables can be written into records and read back out of them. If you want to store numeric variables or arrays (string arrays too) in random-access files, you first have to convert them into string variables, or assign them to a string variable, and then store that (see the BASIC command `STR$` in your CPC BASIC manual). If, for example, you want to "get back" a numeric value, it has to be converted back with the BASIC command `VAL` after reading it from the file.

After the file has been opened, a record can certainly be segmented anew (`|FIELD`) several times without the file having to be closed and reopened each time.

But now on to the VDOS commands that let you work with random-access files.

---

## The VDOS Command |FILES

**Reserving working memory for one or more random-access files**

Before you can work with a random-access file, a channel and a record buffer have to be defined for it. Opening a random-access file without first reserving a buffer for this channel number with the `|FILES` command gives the error message:

```
Feld nicht definiert
```

For this reason the `|FILES` command should (but does not have to!) be at the beginning of a BASIC program, and a sufficient record buffer should be reserved for all channel numbers used later.

The `|FILES` command works with pairs of numbers, i.e. a maximum record length has to be given with every channel number. The channel number may take values from 0 to 127 (a total of 16 channels may be open at the same time); the maximum record length can be chosen freely and is limited only by the available working memory.

Every further `|FILES` cancels the one before. If you enter just `|FILES<ENTER>`, all working areas of random-access files in RAM are cleared.

Entering:

```
|FILES,1,128,2,64,12,20<ENTER>
```

reserves a 128-byte record buffer for channel 1, a 64-byte record buffer for channel 2 and a 20-byte record buffer for channel 12. Random-access files can now be opened on these 3 channels.

---

## The VDOS Command |OPEN

**Opening a random-access file**

With the `|FILES` command we have created the precondition for being able to use a random-access file at all. The next step is to "open" the random-access file so that we can write data into it or read data from it. That is what the `|OPEN` command is for.

```
|FILES,3,300<ENTER>

|OPEN,"DATEI.REL",145,3<ENTER>
```

Let us take a closer look at the `|OPEN`. Obviously a random-access file called `DATEI.REL` is opened here. If it already exists on the disk, it is simply opened; if it does not exist yet, it is newly created and then opened.

`145` is the current record length, which must be less than or equal to the maximum record length (set to 300 in the `|FILES`). The file is opened on channel 3, on which no other file may be open at this time.

> **(!) Note:** Only one file may be open on one and the same channel at a time. But if you need more files, simply choose another channel number.

If you open a file that is already open, we get the following message:

```
Kanal bereits offen
```

If you ever forget the `|OPEN` command and then use the `|PUT` or the `|GET` command anyway, you get the following message:

```
Kanal nicht offen
```

You get the message `Kanal nicht definiert` if no buffer was reserved with `|FILES` for the channel number.

---

## The VDOS Command |FIELD

**Structuring the record buffer**

After a random-access file has been opened, its record buffer has to be segmented, i.e. you have to state how many variables of which length are to be held in one record of the file.

Say you want to have the following three variables in a record: `NAME$` with a maximum length of 12 bytes, `ORT$` with a maximum length of 20 bytes and `TEL$` with a maximum length of 15 bytes. The `|FIELD` command for this combination looks, for example, like this:

```
|FIELD,4,12,20,15<ENTER>
```

So the current length of the buffer in the `|OPEN` command must have been 12+20+15=47 or more. This segmentation applies to the record buffer of channel 4.

In connection with the `|FIELD` command we can get the following messages:

**`Feld zu lang`** – We have defined a field length that exceeds the length of the record buffer – set with `|FILES`.

**`Feld nicht definiert`** – In a `|PUT` or `|GET` command we have given a variable for which no space is provided in the `|FIELD` command.

**`Feld nicht segmentiert`** – We tried to write or read a record with `|PUT` or `|GET` although we have not yet divided it into individual fields (segmented it) with the `|FIELD` command at all.

---

## The VDOS Command |GET

**Reading a record**

With the `|GET` command you read the record with the given number from the file on this channel into the given variables, which must have been defined beforehand. If the variables were not defined, we get the error message:

```
improper argument
```

```basic
10 NAME$="":ORT$="":TEL$=""
20 |FILES,1,100
30 |OPEN,"ADRESS.REL",47,1
40 |FIELD,1,12,20,15
60 |GET,1,174,@NAME$,@ORT$,@TEL$
70 PRINT NAME$,ORT$,TEL$
80 |CLOSE,1
```

Here the variables are defined first (line 10), and then the record with the number 174 is read from the file on channel 1 into the variables `NAME$`, `ORT$` and `TEL$`.

> **(!) Note:** Please note that only the form with the `@` (at sign) is allowed here!! Proper `|FILES`, `|OPEN` and `|FIELD` commands must have been run before.

If the record read contains no data, we get the message:

```
Record leer
```

(In VDOS 2.11-X this message does not appear: such a record is read as an empty record, see [Known bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x).)

---

## The VDOS Command |PUT

**Writing a record**

`|PUT` works just like the `|GET` command, except that it writes the contents of the given variables into the file on the selected channel.

```basic
10 NAME$="" : ORT$="" : TEL$=""
20 |FILES,1,100
30 |OPEN,"ADRESS.REL",47,1
40 |FIELD,1,12,20,15
50 INPUT NAME$,ORT$,TEL$
60 |PUT,1,174,@NAME$,@ORT$,@TEL$
70 |CLOSE,1
```

The `|PUT` command can also be used without the `@` (at sign):

```
|PUT,1,15,"Mueller","Koeln","123456"
```

Here the three words are written directly into the record with the number 15 in the file on channel 1. (In VDOS 2.11-X this form works only a few times in a row, then BASIC reports `String expression too complex`; so you had better use variables with `@`, see [Known bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x).) It is of course clear – and this also applies to the `|GET` command – that the record number can also be replaced by a variable. For example:

```basic
10 NAME$="" : ORT$="" : TEL$=""
20 |FILES,1,100
30 |OPEN,"ADRESS.REL",47,1
40 |FIELD,1,12,20,15
45 INPUT "Geben Sie die Datensatznummer ein",REC
50 INPUT NAME$,ORT$,TEL$
60 |PUT,1,REC,@NAME$,@ORT$,@TEL$
70 |CLOSE,1
```

By choosing `REC` you can decide the record number into which the contents of the three variables are written. If you ever give a record number that goes beyond the bounds of the file, you get the message:

```
Recordnummer zu gross
```

---

## The VDOS Command |CLOSE

**Closing a random-access file**

For the use of a random-access file to run properly, the random-access file has to be closed again at the end.

```
|CLOSE,1 <ENTER>
```

Closes the file that was open on channel 1. If there is no file on this channel, you get the message:

```
Kanal nicht offen
```

---

## Two Small Applications

Here now are the listings of two small programs that should make working with random-access files even clearer to you. In the first example the file `TEST.REL` is opened, and either a selectable record is read and displayed or a record is written with contents you can enter.

```basic
10 |FILES,1,600
20 |OPEN,"TEST.REL",520,1
30 |FIELD,1,250,250
40 X$="":Y$=""

50 PRINT "(L)esen oder (S)chreiben eines Rekords oder (E)nde"
60 K$=UPPER$(INKEY$):IF K$<>"L" AND K$<>"S" THEN GOTO 60
70 INPUT "Rekordnummer",REC
80 IF K$<>"L" THEN GOTO 110
90 |GET,1,REC,@X$,@Y$
100 PRINT X$,Y$:GOTO 50
110 IF K$<>"S" THEN GOTO 160
120 INPUT "1. Variable",X$
130 INPUT "2. Variable",Y$
140 |PUT,1,REC,@X$,@Y$
150 GOTO 50
160 |CLOSE,1:END
```

| Line | Explanation |
|-------|-----------|
| 10 | Set up a buffer 600 bytes long for the channel with the number 1 |
| 20 | Open the file `TEST.REL` with the current record length of 520 bytes on channel 1 |
| 30 | Only the contents of two variables are written into the buffer. The contents of both variables may have a maximum length of 250 bytes. |
| 40 | Define the two variables for the `|GET` command |
| 50 | Ask what is to be done |
| 60 | Input loop |
| 70 | Enter the record number |
| 90 | You arrive here if you entered "L" above. The contents of the record selected by `REC` are read into the variables `X$` and `Y$`. |
| 100 | Print the contents |
| 120 | You arrive here if you entered "S" above. You give the variables `X$` and `Y$` (line 130) a value. |
| 140 | The contents of the two variables are written into the record selected by `REC`. |
| 150 | Jump back to line 50 for a new entry |
| 160 | You arrive here if you entered "E". The file is closed properly. |

You should choose only "S" at least a few times, so that the file `TEST.REL` gets some contents at all, which can then be read with "L".

In the second example 1000 records are written one after the other into the random-access file `ZUFALL.REL`. After that the records of the file are accessed "purely at random" in the truest sense of the word, using the random function (`RND` = random).

```basic
10 |FILES,10,120
20 |OPEN,"ZUFALL.REL",25,10
30 |FIELD,10,25
40 X$=""
50 FOR REC=1 TO 1000
60 X$="Rekord Nr. "+STR$(REC)
70 |PUT,10,REC,@X$
80 NEXT REC
90 REC1=INT(1000*RND(1))+1
100 |GET,10,REC1,@X$
110 PRINT X$
120 GOTO 90
```

| Line | Explanation |
|-------|-----------|
| 10 | Reserve a 120-byte buffer for channel 10. |
| 20 | Open the random-access file `ZUFALL.REL` on channel 10 with the current record length of 25 |
| 30 | Segment the buffer. Only one variable is set up. |
| 40 | Define the variable `X$` for the `|GET` command. |
| 60 | 1000 records: "Rekord Nr. 1", "Rekord Nr. 2", …, "Rekord Nr. 1000" are written into the file `ZUFALL.REL`. |
| 90 | Generate a random number between 1 and 1000 |
| 100 | Read the record with the number of the random number. |
| 110 | Display the record |
| 120 | Generate another random number and read the record. |

This example demonstrates very well the high speed of access to the data of the random-access file.

The following program does the same jobs as the example just shown, except that sequential files are used here. Go ahead and type it in. You will be amazed how much slower everything runs here. This shows once again that the "tool" of random-access file handling is indispensable for professional work.

```basic
10 OPENOUT "ZUFALL.SEQ"
20 FOR REC=1 TO 1000
30 X$="Rekord Nr."+STR$(REC)
40 PRINT #9,X$
50 NEXT
60 CLOSEOUT
70 OPENIN "ZUFALL.SEQ"
80 REC1=INT(1000*RND(1))+1
90 VGL$="Rekord Nr."+STR$(REC1)
95 FOR A=1 TO 1000
100 INPUT#9,X$
110 IF X$=VGL$ THEN GOTO 120
115 NEXT
120 PRINT X$
125 CLOSEIN
130 GOTO 70
```

Lines 10 to 60 create the file `ZUFALL.SEQ`. You can see that the data is written out without any numbering at all. In line 110 the string produced by the random generator in line 90 is compared with the one just read. If the two are identical, the string is displayed (line 120). If they are not the same, the comparing has to go on, until perhaps the 1000th record matches (worst case). If the very first comparison (Rekord Nr. 1) matches, we have the best case.

With random-access file handling there are no best and worst cases; they are all the same. As you will easily find out, one and the same task is solved about 10 times faster by the random-access file handling of VDOS than by sequential file handling.

---

## Ways of Trapping Disk Errors

**The VDOS command `|DERROR`**

To prevent a BASIC program from being aborted by a drive message (usually error messages) with BASIC coming back with `Ready`, the error messages can be trapped with the `|DERROR` command and handled in the program. That means "bailing out" can be prevented altogether. This is especially important for PRO applications: bailing out there would mean "game over".

After entering `|DERROR,0<ENTER>` disk errors are no longer shown on the screen. `|DERROR,1<ENTER>` switches the error output back on. This is also the power-on state of the CPC with a vortex floppy connected. When the error messages are switched off, entering `|DERROR<ENTER>` (that is, without parameters) creates the error code variable `DERR`. Following this command description you will find a list of all error codes.

```basic
10 |DERROR,0
20 CAT
30 |DERROR
40 IF DERR=72 THEN INPUT "Bitte Diskette einlegen und irgendeine Taste druecken",A:GOTO 20
50 ....
```

Error code 72 means that there is no disk in the drive. In line 10 we switched the error output off. In line 30 we have the error code variable created. If it has the value 72, the message appears; in all other cases the program simply carries on.

> **(!) Caution:** Certain errors cannot be trapped by `|DERROR,0` alone; you also have to work with `ON ERROR GOTO`.

Let us assume that in the following there is no disk in the drive. Without error trapping, an access to the drive would therefore produce the message

```
Laufwerk d: Diskette fehlt
```

If we trap this error with `|DERROR,0`, BASIC still reports an error. Just go ahead and run the following little program:

```basic
10 |DERROR,0
20 LOAD,"TEST"
30 ..
```

You will get the following error message:

```
File already open in 20
```

and the program stops. Now test the following program:

```basic
10 ON ERROR GOTO 100
20 |DERROR,0
30 LOAD "TEST"
40 ..
100 |DERROR:PRINT DERR:RESUME 40
```

Now no error message appears any more, and the error trapping routine in line 100 prints a "72" on the screen. (72 = `&48`, i.e. bit 6 and bit 3 are set, and this in turn means it is the FDC error – Floppy Disc Controller error – "Drive not ready", i.e. there is no disk in the drive.)

---

## Error Codes and What They Mean

Here you will find a list of all VDOS error messages: error code and message. The possible causes are also given. `<...>` is a placeholder for a file name. `FDC` stands for Floppy Disk Controller. `d:` means a drive letter, namely the one on which the error occurred (e.g. `A:` or `B:`). All error codes are given in decimal.

| Code | Message | Meaning |
|------|---------|-----------|
| 17 | Drucker nicht bereit | This error message can only come up under CP/M, and there only when the printer is still not ready about 40 sec after the attempt to output a character to it. Possible causes: printer cable not plugged in, printer not switched on, printer not selected. |
| 10 | Laufwerk d: Diskette wurde gewechselt `<...>` wurde geschlossen | A file was opened with `OPENOUT` and then the disk was changed without giving a `CLOSEOUT`. |
| 21 | Laufwerk d: Diskette voll | The disk in drive `d:` is full. |
| 22 | Laufwerk d: Directory voll | The disk directory is full. Note that this message can come up before you actually see 128 entries with, e.g., `CAT<ENTER>`. Reason: one directory entry is needed per 64 KB of data per program. A file that is, e.g., 129 KB in size already takes up 3(!) entries in the directory. |
| 23 | `<...>` wurde nicht gefunden | Reported whenever an attempt is made to access a file that is not in the directory. The error can occur with the following commands: `LOAD`, `SAVE`, `RUN`, `OPENIN`, `OPENOUT`, `|ERA`, `|REN` and `|ATTRIBUT`. |
| 24 | `<...>` existiert bereits | An attempt is made to give a file a new name although another file with this name already exists. |
| 25 | `<...>` hat Schreibschutz | An attempt is made to delete (with the `|ERA` command) or to write to a file that carries the "read-only" attribute (set with the `|ATTRIBUT` command). |
| 33 | Eingabefehler | A typing mistake was made (syntax error), or the command format of a particular command was not followed (semantic error). |
| 39 | Feld zu lang | The current field length is greater than the one given in the `|FILES` command. It may only be "less than or equal". This message can come up if: the current length in `|OPEN` is too large, or the sum of the individual field lengths in `|FIELD` is greater than the one defined in `|OPEN`. |
| 40 | Feld nicht definiert | An attempt is made to open a file on a channel (with `|OPEN`) without the `|FILES` command having been entered first. |
| 41 | Feld nicht segmentiert | An attempt is made to work with the `|GET` or `|PUT` commands without the record buffer having been segmented with `|FIELD` first. |
| 42 | Kanal bereits offen | An attempt was made to open a channel again that had already been opened with `|OPEN`. |
| 43 | Kanal nicht offen | An attempt was made to carry out one of these commands (`|FIELD`, `|CLOSE`, `|GET` or `|PUT`) with a file on a channel that is not open. |
| 44 | Kanalnummer falsch | An illegal channel number was given in connection with the commands `|CLOSE`, `|FIELD`, `|OPEN`, `|GET`, `|PUT` or `|FILES`. Valid channel numbers lie between 0 and 127 (both inclusive). |
| 45 | Recordnummer zu gross | VDOS can manage at most 65536 records of 128 bytes each. The maximum number of records changes depending on the current record buffer length defined in `|OPEN`. E.g. with a buffer size of 512 bytes at most 16384 records can be managed. |
| 53 | Kanal nicht definiert | An attempt was made to open a channel that had not been defined before. |
| 55 | Record leer | (Never reported by VDOS 2.11-X because of a bug, see [Known bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x).) An attempt was made to read a record that is no longer listed in the block allocation table. **Caution:** This error cannot necessarily be used to test for the end of a random-access file. Reason: if the current record length is smaller than the block length (4 KB on vortex floppies, 1 KB on the 3" drive), several records go into one block. If, e.g., only the first record in the last block listed in the block allocation table is still in use, error 55 only comes when you try to address a record in the next block. With small field lengths its record number may differ greatly from that of the last record actually in use. So you should always work with index files, i.e. keep a second, so-called index file alongside the data file, in which data record numbers and other information are managed. |
| 14 | (no message text) | File not open. An attempt was made to close a sequential file that was not open with `CLOSEIN` or `CLOSEOUT`. |
| 15 | (no message text) | The physical (actual) end of a sequential file was reached. |

All the messages listed above are produced by the VDOS operating system.

Error codes that come directly from the FDC (type µPD 765 from NEC) have bit 6 set and bit 7 cleared, and therefore lie between 64 and 127. The individual bits mean the following:

| Bit | Meaning (if the bit is set) |
|-----|-------------------------------|
| 7 | always 0 |
| 6 | always 1 |
| 5 | CRC error in the data or ID field |
| 4 | The FDC was not serviced by the computer within a certain time during a data transfer. |
| 3 | The drive reports "not ready". Usually means that there is no disk in the slot, or the eject button was not properly locked. |
| 2 | The FDC cannot find the requested sector while carrying out a read operation. |
| 1 | The FDC receives a "Write protect" signal from the drive during a write or format operation. I.e. the disk is write-protected. |
| 0 | The FDC cannot find the ID field after "passing over" the index hole for the second time. |

A common error code is likely to be 72, or binary `01001000`, and it means that there is no disk in the drive.

If the floppy disk error messages were not switched off with `|DERROR`, they are output on the screen. To show the programmer this, in that case bit 7 of the error byte is set, i.e. 128 is added to the error codes above. E.g.

| Error code | Meaning | Error message |
|------------|-----------|---------------|
| 21  | Disk full | switched off |
| 149 | Disk full | switched on |

> **(!) Important**
>
> Floppy errors that do not lead to a BASIC error cannot be trapped with `ON ERROR GOTO` either; instead you have to check for errors after each command:
>
> ```basic
> 10 ON ERROR GOTO 100
> 20 |DERROR,0:'meldungen unterdrücken
> 30 CAT
> 40 |DERROR:'anlegen der fehlervariable DERR
> 50 IF DERR=..........
> ..........
> 100 'fehlerbehandlung
> ```
>
> If there is no disk in the drive at line 30, `CAT` goes "nowhere" but does not produce a BASIC error message in the process, i.e. it does not branch to line 100. The error is trapped in line 40 and line 50.

> **(!) Important**
>
> The `|DERROR` command without parameters is not needed on the CPC664 and CPC6128, because BASIC 1.1 already creates the variable `DERR` by itself in the event of a disk error, and this no longer has to be requested first as with BASIC 1.0 (CPC464). Of course you can still use the commands `|DERROR,0` and `|DERROR,1` to switch the disk error messages on or off.

Please also see the appendix "The EOF Problem" at the end of this manual.

---

## The VDOS Turnkey Function

**For CPC464+DDI-1 and X drive**

Turnkey has nothing to do with Turkey or a turkey. Turnkey means something like "put the key in, turn it, done". For your computer system that means: "insert the disk, switch the machine on, done".

With the turnkey function the system can indeed be brought up into a particular operating state right from power-on. Here is an example: imagine you only want to use the CPC to do your correspondence with WordStar. That means it is really very annoying for you to first load CP/M before every use, then start WordStar and perhaps also load an old letter. You would like it best if you only had to insert the disk, switch on the machine and then immediately "land" in your letter in WordStar.

This task is no problem for VDOS. That is because we have built in the turnkey function: every time the computer is reset (pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time) – switching off and on is also a reset –, VDOS looks on any disk that may be inserted in the 3" drive for a file named `HELLO.BAS`. If VDOS finds this file, it is started automatically (equivalent to `RUN "HELLO"<ENTER>`).

The hello file looks, for example, like this:

```basic
10 |CPM
Ready
SAVE "HELLO"<ENTER>
```

With the `SAVE` command we have "put the file in a safe place" right away. Yes, it is that simple. This little one-liner starts CP/M. That would be the first step.

Now we also make use of the **autostart string** feature. This is a line consisting of CP/M commands that is executed directly after CP/M has been loaded. We can create this autostart string with the CP/M command `INSTALL`. The string could look like this, for example:

```
WS BRIEF.TXT<0D>
```

That means that after CP/M has been loaded, WordStar (`WS.COM`) would be started immediately. At the same time the correspondence `BRIEF.TXT` would then be loaded, and we would have achieved what we wanted.

If you want to prevent the search for the hello file, simply hold down, e.g., the `ESC` key or the `ENTER` key during the RESET or when switching on. Then there is no lengthy searching at all; instead `Ready` appears right away.

---

## X Drives on the CPC464 with DDI-1, CPC664 and CPC6128

Everything discussed here applies to the following equipment sets:

| Computer | + Drives |
|----------|-------------|
| CPC464 + DDI-1 | vortex F1-X and M1-X |
| CPC664         | vortex F1-X and M1-X |
| CPC6128        | vortex F1-X and M1-X |

What distinguishes these CPCs is that they come equipped with a 3" drive from the start. So of course they also have a floppy controller. Because of this, the CP/M 2.2 operating system is supplied with these machines too, and with the CPC6128 also CP/M 3.0 (also called CP/M Plus).

In the package of your vortex X drive you will find a vortex system disk that does not contain CP/M. And why should it? You have already "bought" it; it just has to be put onto the vortex system disk. I will show you right away how we do that.

**For the skeptics…**

> Please note that this is in no way "license shifting". The decisive point is that the number of computers (workstations) on which you use CP/M (2.2 and Plus) does not increase. You still have only one computer!

---

## Creating a vortex CP/M 2.2 System Disk

Since under CP/M 2.2 the vortex floppies can manage not just 64 (as on the 3") but 128 entries in the disk directory, and since managing the directory also costs RAM, before actually creating the vortex system disk we first have to shrink the CP/M 2.2 on your 3" disk.

So insert a copy of your 3" CP/M 2.2 system disk (never the original!!) into the 3" drive and start the CP/M 2.2 operating system by entering `|CPM<ENTER>`. It announces itself with the sign-on message:

```
CP/M 2.2 - Amstrad Consumer Electronics plc

A>
```

If you look at the contents of the disk with `A>DIR<ENTER>`, you will also find the two CP/M commands `MOVCPM.COM` and `SYSGEN.COM`. These are exactly the two programs we need to make CP/M a little smaller. Don't worry, we don't need much memory. Only 256 bytes (a so-called page). Your CP/M 2.2 now has 179 pages; we turn that into 178 pages.

First we start the program `MOVCPM`:

```
A>MOVCPM 178 *<ENTER>

CONSTRUCTING 44k CP/M vers 2.2
READY FOR "SYSGEN" OR "SAVE 34 CPM44.COM"
```

Then we start `SYSGEN`, with which we write the CP/M we have just shrunk onto the system tracks of the 3" disk. Please make sure that the "write-protect slider" of this disk has not been moved into the protect position.

```
A>SYSGEN *<ENTER>

SYSGEN V2.0

Please insert DESTINATION disc into drive A then press any key:
Do you wish to reconfigure another disc (Y/N) ? :N

Please insert a CP/M system disc into drive A then press any key:

SYSGEN V2.0 finished

A>
```

You leave this disk in the 3" drive all the time, answer "N" once and otherwise just keep pressing any key until the CP/M prompt `A>` appears again.

Now also enter the following:

```
A>AMSDOS<ENTER>

(C)1986   VDOS 2.11-X by vortex GmbH
BASIC 1.1

Ready
```

You are now back in BASIC. Now please insert the supplied vortex disk into the X drive and start the modified CP/M 2.2 operating system by entering

```
|CPM,1<ENTER>
```

It now announces itself with the sign-on message:

```
CP/M 2.2 - Amstrad Consumer Electronics plc
44K CP/M vers. 2.2-07/86 vortex GmbH

A>
```

With this we have access to the X drive, which is now drive B with a capacity of 708 KB.

Next we fetch CP/M 2.2 from the 3" disk over to the vortex disk. To do this, please enter the following:

```
A>B:<ENTER>
B>SYSGEN<ENTER>

SYSGEN 2.0   (C)1985 vortex GmbH

Quelldiskette in Laufwerk A,B oder RETURN ? A
Quelldiskette in Laufwerk A einlegen und irgendeine Taste druecken

Zieldiskette in Laufwerk A,B oder RETURN ? B
Zieldiskette in Laufwerk B einlegen und irgendeine Taste druecken

Noch eine Diskette J/N ? N
Diskette mit Systemspur in Laufwerk A einlegen und irgendeine Taste druecken
```

With that we have transferred CP/M. Now we also fetch the CP/M commands:

```
XSUB    .COM   SUBMIT  .COM   LOAD    .COM
DUMP    .COM   MOVCPM  .COM   ED      .COM
STAT    .COM   PIP     .COM   DDT     .COM
```

over to the vortex disk. To do this we enter:

```
B>A:<ENTER>
A>PIP<ENTER>
*B:=XSUB.COM<ENTER>
*B:=SUBMIT.COM<ENTER>
*
*B:=STAT.COM<ENTER>
*B:=PIP.COM<ENTER>
*<ENTER>
A>
```

So, now we are done. In the X drive there is now your new vortex CP/M 2.2 system disk, which you need when you want to load CP/M from the X drive.

Now enter

```
A>AMSDOS<ENTER>
```

which switches us back to BASIC:

```
(C)1986   VDOS 2.11-X by vortex GmbH
BASIC 1.1

Ready
```

By entering

```
|CPM,2<ENTER>
```

start CP/M 2.2 from the vortex drive. We get the following sign-on message:

```
44K CP/M vers.2.2-07/86 vortex GmbH

A>
```

Drive A is now the vortex X drive with 708 KB and 128 directory entries. Drive B is the 3" drive with about 170 KB and 64 directory entries.

> **(!) Important:** The following utilities on the 3" disk must not be run under this CP/M:
>
> `BOOTGEN.COM`, `DISCKIT2.COM`, `SETUP.COM`, `FORMAT.COM`, `SYSGEN.COM`, all LOGO files

To be able to work with LOGO and the X drive, you have to insert a copy of the LOGO disk into the 3" drive and start it with `|CPM<ENTER>`. Note that the X drive here only has a capacity of about 170 KB with 64 directory entries.

It is best to make a working copy of the vortex CP/M 2.2 system disk we have just created right away. From now on we should only work with this working copy and any copies of it, and no longer with the system disk created before.

To make the copy, the system disk just created stays in the drive; we do not need the 3" disk any more now. We also need a new blank vortex disk. We have not left the CP/M loaded earlier, and now, by entering

```
A>DISKTOOL<ENTER>
```

we start the vortex utility that can also copy whole disks. We then get the following screen:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!                                                                        !
!                                                                        !
+------------------------------------------------------------------------+

        +------------------------------------------+
        ! 1 - Formatieren einer Diskette           !
        ! 2 - Komplettkopie einer Diskette erzeugen!
        ! 3 - CP/M-Systemspuren uebertragen        !
        ! 4 - nur den Parametersektor uebertragen  !
        ! ESC - zurueck ins CP/M                   !
        +------------------------------------------+

    Bitte entsprechende Taste druecken !
```

You press the "2" key, because we want to copy a complete disk. After pressing it we get a new screen:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  KOMPLETTKOPIE ERSTELLEN                          !
!                                                                        !
+------------------------------------------------------------------------+

        +------------------------------------------+
        !              Quell-Laufwerk ?            !
        !              Ziel  -Laufwerk ?           !
        ! mit formatieren der Ziel-Diskette (J/N) ?!
        ! mit testen der Ziel-Diskette (J/N) ?     !
        !       ESC - zurueck ins letzte Menue     !
        +------------------------------------------+

    Bitte entsprechende Taste druecken !
```

The source is the vortex system disk created earlier. The destination is the new, still empty vortex disk. Source drive and destination drive are both "A".

So answer the following questions like this:

```
Quell-Laufwerk ? A
Ziel-Laufwerk  ? A
```

You answer the question "mit formatieren..." with "J", because the new empty disk first has to be formatted. We also answer the question "mit testen..." with "J", because we want to rule out even the smallest copy errors.

The scrolling text always tells you when to insert which disk into drive A.

> **(!) Important:** If you ever forget to swap the disk, your copy original (!!) will be destroyed. Caution!

The copy just made should now be in the drive. Leave it there and press the `ESC` key. DISKTOOL is left and the CP/M prompt `A>` appears again. The disk in the X drive is an exact image of the CP/M 2.2 system disk created before.

---

## CPC464, CPC664 with X Drive and vortex RAM Card

Have you installed a vortex RAM card in your CPC? If not, it's about time - you're missing out on far too much! You'll never get to enjoy a 62K CP/M 2.2. No "dBase", no "Multiplan", no real "WordStar", no…

But if you have already installed the card, you can also run the "big CP/M" with your new vortex floppy. All you have to do is start the program `XPATCH.COM`, which is on the vortex CP/M 2.2 system disk you just made. This program works exactly like the program `PATCH.COM` – it replaces it completely – that comes with the RAM card.

---

## Making a vortex CP/M Plus Disk (CPC6128 Only)

If you own a CPC6128, there's still CP/M plus, of course. We certainly won't sweep that under the rug. Here, too, we'll make a matching vortex disk from which you can then load CP/M plus.

Before you can make the vortex CP/M plus system disk, you must have made a vortex CP/M 2.2 disk (as explained above). Put the 3" CP/M 2.2 system disk you modified earlier into the 3" drive. Put the vortex CP/M 2.2 system disk into the X drive and start, by entering

```
|CPM,1<ENTER>
```

the modified CP/M 2.2 operating system from the 3" drive. It greets you with:

```
CP/M 2.2 - Amstrad Consumer Electronics plc
44K CP/M vers. 2.2-07/86 vortex GmbH
A>
```

Now start, by entering

```
A>B:<ENTER>
B>XPATCH30<ENTER>
```

the CP/M plus patch program that is on the vortex disk supplied – now your original vortex CP/M 2.2 system disk. `XPATCH30` can only be used under a CP/M 2.2 that was started with `|CPM,1<ENTER>` on a CPC6128. Should you try to start `XPATCH30` under CP/M plus, you get the message:

```
XPATCH30 kann nur unter CP/M 2.2 gestartet werden
```

and the program aborts. So let's assume everything goes according to plan; then after starting `XPATCH30` you get the message:

```
**********************************************
*                                            *
*      CP/M 3.0 (V1.1-X) MASTER PROGRAMM     *
*                                            *
*      (C) 1986 vortex GmbH                  *
*                                            *
**********************************************

(XPATCH30 ändert eine CP/M Plus Systemdatei fuer die Benutzung des X-Laufwerks ab.)

Eine Kopie der 3" CP/M Plus Systemdiskette in das 3" Laufwerk
einlegen und irgendeine Taste druecken
```

So now put a copy of your CP/M Plus system disk into the built-in 3" drive and press any key. `XPATCH30` shows the message:

```
C10CPM3.EMS Datei wird gelesen...
```

`XPATCH30` now fetches the CP/M Plus operating system (on the 6128 it is in a file with the extension `EMS`) from the copy of the 3" CP/M Plus disk and modifies it for use with the X drive. `XPATCH30` now asks whether you want a 3" or a 5.25" CP/M Plus disk. Let's assume we want a 5.25" disk, so we answer the question:

```
Soll 3" Laufwerk = Laufwerk A sein (J/N) ? N
```

with N(o). `XPATCH30` now writes the modified CP/M Plus operating system, which gets the name `CPM3.EMS`, to the 5.25" disk in drive B (there is a formatted disk in there, of course, right?).

```
CPM3.EMS wird geschrieben...
```

Naturally, the 5.25" disk also needs a new boot sector that is able to load the CP/M Plus operating system. So in this case `XPATCH30` reports:

```
Bootsektor wird angelegt.

5.25"/3.5" CP/M Plus-X MASTER-DISKETTE wurde hergestellt.
```

Then `XPATCH30` tells you once more, in short form, which ways you have to start CP/M Plus:

**You now have three ways to start CP/M Plus:**

1. **CP/M Plus original disk in the 3" drive:** `|CPM<ENTER>` starts CP/M Plus from the 3" drive. Drive B is handled as a single-sided 40-track drive with 64 directory entries.
   > **(!) Caution:** 5.25" disks that are used in this mode must never (!) be used under VDOS or under a CP/M (2.2 and Plus) started with `|CPM,1` or `|CPM,2`.

2. **Patched CP/M Plus disk in the 3" drive:** `|CPM<ENTER>` or `|CPM,1<ENTER>` starts CP/M Plus from the 3" drive. Configuration: drive A = 3", drive B = 5.25" with 708 kB and 128 directory entries.

3. `|CPM,2<ENTER>` starts CP/M Plus from the 5.25"/3.5" drive. Drive A = 5.25" with 708 kB and 128 directory entries, drive B = 3".

```
3" CP/M 2.2 Diskette mit XPATCH30 wieder in 3" Laufwerk
einlegen und irgendeine Taste druecken
```

It's best to make a working copy of the CP/M plus system disk you just made right away (with `DISKTOOL`, as described for making a vortex CP/M 2.2 system disk).

### A Few More Notes

1. The screen accelerator `FAST.COM` and the Z80 monitor `XMON` only work under the 44K CP/M 2.2 operating system, not under CP/M plus. The utilities `DISKTOOL`, `FILECOPY`, `SYSGEN`, `INSTALL`, `CASCOPY`, `VDOS` also only work under a CP/M 2.2 (62K too!).

2. If you start CP/M plus from BASIC (`|CPM,2<ENTER>`), make sure there is a disk in the 3" drive. If there isn't one, CP/M plus recognizes only one drive. (By the way, this also happens to you without a vortex floppy, for example when you connect the 3" second drive to your CPC6128.) The proper load message then looks like this:

   ```
   CP/M Plus Amstrad Consumer Electronics plc

   v 1.0, 61K TPA, 2 disc drives

   A>
   ```

3. All CP/M plus programs except the program `DISCKIT3.COM` may be transferred from the 3" disk to the vortex disk.

> **(!) Important:** If you use `DISCKIT3.COM` together with the X drives, the consequences may be disastrous.

So if, for example, you want to transfer files under CP/M Plus from drive A to B or vice versa, use the program `PIP` for this. If you want to copy whole disks, leave CP/M Plus, start CP/M 2.2 and work with `DISKTOOL` there.

---

## Loading the CP/M Operating System

With the X drives there are 3 ways to load CP/M:

### The VDOS Command |CPM

CP/M is loaded from the 3" drive from a copy of the original Schneider CP/M system disk. We get the following load message:

```
|CPM<ENTER>
CP/M 2.2 - Amstrad Consumer Electronics plc
A>
```

- Drive A is the 3" drive with approx. 170 KB.
- Drive B is the X drive with approx. 170 KB.

Here drive B is operated as a 40-track/single-sided drive with a capacity of approx. 170 KB. That's because the original AMSDOS – only it guarantees 100% compatibility with existing 3" software – can simply only handle drives of this capacity.

Note, however, that these 40 tracks are not spread over the whole radius of the disk (the normal case); instead, the drive can still step over 80 tracks but uses only the first 40 on the front side. This way of loading is identical to the case where you have no X drive at all, but, for example, only a 3" second drive.

> **(!) Note:** The disks that are made and used under this CP/M cannot be used when VDOS is switched on. Keep these two "kinds of disk" strictly apart (label them on the outside!). If you use them anyway, you must expect a complete loss of data.

The disks you need here for your X drive must be formatted in this special format with the CP/M command `FORMAT` or `DISCKIT` (on the copy of the original Schneider CP/M system disk).

### The VDOS Command |CPM,1

CP/M is loaded from the 3" drive from a modified copy of the original Schneider CP/M system disk. We get the following load message:

```
|CPM,1<ENTER>
X-Laufwerke Benutzerhandbuch VDOS und CP/M   (C)1986 vortex GmbH

CP/M 2.2 - Amstrad Consumer Electronics plc
44K CP/M vers. 2.2-07/86 vortex GmbH

A>
```

- Drive A is the 3" drive with approx. 170 KB.
- Drive B is the X drive with 708 KB.

What was modified in this CP/M you saw in the section "X Drives on the CPC464 with DDI-1, CPC664 and CPC6128". This CP/M is only 178 pages in size (instead of 179 pages as before; that's because the X drive is handled with 128 directory entries).

### The VDOS Command |CPM,2

CP/M is loaded from the system disk in the X drive. (For making this disk, see the section "X Drives on the CPC464 with DDI-1, CPC664 and CPC6128".) We get the following load message:

```
|CPM,2<ENTER>

44K CP/M vers. 2.2-07/86 vortex GmbH

A>
```

- Drive A is the X drive with 708 KB.
- Drive B is the 3" drive with approx. 170 KB.

> **(!) Important**
>
> On the CPC6128 with a CP/M plus disk inserted, all three CP/M load commands shown naturally load CP/M plus. If you reset the computer (pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time), switch the computer OFF/ON or load CP/M, the swap set with the `|X` command is lost again.

---

## CP/M with Your vortex X Drive

You need the vortex CP/M commands described here to work with the vortex X drive under CP/M 2.2. So if you have loaded CP/M 2.2 with `|CPM,1<ENTER>` or `|CPM,2<ENTER>`, you can use these commands.

For information about CP/M and its commands, please refer to the corresponding manuals you received when you bought your CPC (664 and 6128) or your DDI-1 floppy station (CPC464).

---

## The CP/M Command FILECOPY

**Copying files**

While with the CP/M command `PIP` it was not possible for owners of just one drive to copy files or even whole disks (you remember, it was always the BDOS errors and the `CTRL`+`C`), with `FILECOPY` this is no problem at all. What's more, `FILECOPY` is much more convenient and simpler to operate.

The tedious copying of files between different user areas is gone, too. Besides the source and destination drive you can also give a source user area and a destination user area.

In addition, all 16 possible "drives" (floppies, hard disks or RAM floppies) are supported. As soon as you start `FILECOPY` you see which drives are present and what formatted (actual) storage capacities they have.

One small special feature is worth mentioning here: if you have installed a vortex memory expansion in your CPC, then from 128 KB of additional RAM on you have a RAM floppy under CP/M. The drive letter "C" is always reserved for this RAM floppy.

> **(!) Note:** Note, however, that `FILECOPY` cannot transfer data between external devices. `FILECOPY` is purely a utility for drive-to-drive data transfer.

We start `FILECOPY` by entering

```
A>FILECOPY<ENTER>
```

`FILECOPY` has two menus:

- The **"settings" menu**, in which you set the source and destination
- The **"copy" menu**, in which you can then "pick" the files that are to be copied.

In both menus we will mainly need the cursor keys, the `COPY` key and the `ENTER` key. Other keys are rarely needed.

The screen is always divided into five "windows":

- **Window 1** shows the files that are on the source disk or that are to be copied (inverse video display).
- **Window 2** always shows us "which" keys do "what".
- **Window 3** shows which drive and which user area is the source and which drive and which user area is the destination.
- **Window 4** shows us the drives present and their formatted storage capacities. Here we have two possibilities, depending on whether we load CP/M with `|CPM,1<ENTER>` (drive A = 3" drive with 169 KB and drive B = X drive with 704 KB) or with `|CPM,2<ENTER>` (drive A = X drive with 704 KB and drive B = 3" drive with 169 KB). The user numbers can also be changed in window 3. They run from 0 to F; these are hexadecimal digits. Here is a short "translation":

  | Decimal | Hexadecimal |
  |---------|-------------|
  | 0 – 9   | 0 – 9       |
  | 10      | A           |
  | 11      | B           |
  | 12      | C           |
  | 13      | D           |
  | 14      | E           |
  | 15      | F           |

- **Window 5** is a so-called "ticker". The text output here runs along the bottom edge of the screen at a continuous speed. Error messages, the request to change the disk and similar messages are shown here.

FILECOPY V3.0       (C)1986 by vortex GmbH

```
+-------+ +--------------------------------------------+ +-------+
!       ! !              Kopieren                      ! !       !
!       ! !          von Laufwerk A User 0             ! !       !
!  F    ! !          nach Laufwerk A User 0            ! !  F    !
!  E    ! !                 FENSTER 3                  ! !  E    !
!  N    ! +--------------------------------------------+ !  N    !
!  S    !                                                !  S    !
!  T    !                                                !  T    !
!  E    !                                                !  E    !
!  R    ! +--------------------------------------------+ !  R    !
+--   --+ ! ↑ u ↓  - Quell- und Ziel-Laufwerke aendern ! !       !
!  1    ! ! ← u ->  - User-Bereiche aendern             ! !  4    !
!       ! ! COPY   - Inhaltsverzeichnis Quell-Diskette ! !       !
!       ! ! ENTER  - Weiter zum naechsten Menue        ! !       !
!       ! ! ESC    - Zurueck ins CP/M                  ! !       !
!       ! !                FENSTER 2                   ! !       !
!       ! +--------------------------------------------+ !       !
!       !                                                !       !
!       !                                                !       !
+-------+                                                +-------+
+----------------------------------------------------------------+
!                            FENSTER 5                           !
+----------------------------------------------------------------+

    Bitte entsprechende Taste druecken !
```

Window 5 reports "Bitte entsprechende Taste druecken!"
Of interest here is window 2:

- With the "cursor up" key you can change the source drive. There are as many choices here as there are drives shown in window 4.
- With the "cursor down" key you can set the destination drive.
- With the "cursor left" key you can set the user area on the source disk, i.e. the data to be copied is fetched from this area.
- With the "cursor right" key you can set the user area on the destination disk, i.e. the data coming from the source disk is copied into this area.

Do you still remember how tedious that was with the `PIP` command?

If you press the `COPY` key, the alphabetically sorted directory of the source disk is shown in window 1. By pressing any key you can pause this output, and by pressing again start it again.

If we press the `ESC` key, `FILECOPY` ends and we return to CP/M, but first this ticker text appears:

```
CP/M-Diskette in Laufwerk A einlegen und beliebige Taste druecken!
```

If you press the `ENTER` key, you should have set the source and destination beforehand. Window 2 gets new contents, window 1 is cleared and the directory of the source is scrolled from bottom to top up to the markers (to the right and left of window 1).

The new window 2 then looks like this:

```
        +----------------------------------------------+
        ! ↑ u ↓  - einen Dateinamen vor / zurueck      !
        ! COPY   - Datei als zu kopieren kennzeichnen  !
        ! W      - mittels Wildcards kennzeichnen      !
        ! ENTER  - diese Dateien kopieren              !
        ! ESC    - zurueck ins letzte Menue            ! 
        !                                              !
        +----------------------------------------------+
```

The ticker again shows `Bitte entsprechende Taste druecken!`.

With the "cursor up/down" keys you can bring any file in window 1 between the two markers. If we now press the `COPY` key, this file is shown in "inverse video". We have marked this file as to be copied. In this way we can mark a whole series of files, or even all of them (to do so, move to the start of the directory and keep pressing the `COPY` key), for copying. If we move to a file that has already been marked and then press the `COPY` key, the mark is removed again.

If we then press the `ENTER` key, the copying starts.

If the source and destination are not the same (two drives, or 1 drive and a RAM floppy), we don't need to swap disks. `FILECOPY` tells us when it is reading from the source and when it is writing to the destination disk.

If we have only one drive, or deliberately want to copy with just one drive, the ticker keeps telling us when we have to take out the source disk and put in the destination disk instead.

There is also the option of copying by means of **wildcards**. Type a "W", and window 2 is cleared and you can enter a wildcard specification there. As before, you can change the source and destination with the "cursor up" and "cursor down" keys in the previous menu. In any case, with `W` and the wildcard specification entered, the source disk is "scanned" (examined) and all files that match the wildcard pattern are copied to the destination. The permitted wildcard characters are, as usual under CP/M, the asterisk `*` and the question mark `?`.

A wildcard pattern could, for example, look like this:

```
WS*.*
```

All files on the source disk that begin with `WS` (WordStar files) and then have any characters in the file name and file type (e.g. `WS.COM`, `WSOVLY1.OVR`, `WSMSGS.OVR` or `WSU.COM`) are copied to the destination disk.

Another wildcard pattern would be, for example:

```
*.*
```

This would transfer all files from the source disk to the destination disk. The file name and file type are completely arbitrary. All files on the source disk match this pattern.

### Example

Start `FILECOPY` by entering the following:

```
A>FILECOPY<ENTER>
```

The screen is cleared and the `FILECOPY` screen appears. 

```
FILECOPY V3.0       (C)1986 by vortex GmbH

+-------+ +--------------------------------------------+ +-------+
!       ! !              Kopieren                      ! !       !
!       ! !          von Laufwerk A User 0             ! !       !
!  F    ! !          nach Laufwerk A User 0            ! !  F    !
!  E    ! !                 FENSTER 3                  ! !  E    !
!  N    ! +--------------------------------------------+ !  N    !
!  S    !                                                !  S    !
!  T    !                                                !  T    !
!  E    !                                                !  E    !
!  R    ! +------------------------------------------..+ !  R    !
+--   --+ ! ↑ u ↓  - Quell- und Ziel-Laufwerke aendern ! !       !
!  1    ! ! ← u ->  - User-Bereiche aendern             ! !  4    !
!       ! ! COPY   - Inhaltsverzeichnis Quell-Diskette ! !       !
!       ! ! ENTER  - Weiter zum naechsten Menue        ! !       !
!       ! ! ESC    - Zurueck ins CP/M                  ! !       !
!       ! !                FENSTER 2                   ! !       !
!       ! +--------------------------------------------+ !       !
!       !                                                !       !
!       !                                                !       !
+-------+                                                +-------+
+----------------------------------------------------------------+
!                            FENSTER 5                           !
+----------------------------------------------------------------+

    Bitte entsprechende Taste druecken !
```

In WINDOW 3, drive A user 0 is preset as both the source and the destination drive.

WINDOW 4 shows the drives present. In our case (drive A = X drive, drive B = 3" drive; so CP/M was loaded with `|CPM,2<ENTER>`), WINDOW 4 looks like this:

```
          +-----------+
          | vorhandene|
          | Laufwerke/|
          | Kapazitaet|
          |           |
          | A: 704 KB |
          | B: 169 KB |
          | C: ------ |
          | D: ------ |
          | E: ------ |
          | F: ------ |
          | G: ------ |
          | H: ------ |
          |           |
          | K: ------ |
          | L: ------ |
          | P: ------ |
          +-----------+
```

You see, `FILECOPY` is pretty "intelligent": it can handle all the drives possible under CP/M (16 of them, A…P).

In WINDOW 5 we see a ticker with the following text:

```
Bitte entsprechende Taste druecken !
```

Let's assume that the disk from which we started `FILECOPY` is not the source disk; then we now take out the disk still in the X drive and put in the source disk instead. Let's just take a look at which files are on this disk. To do so, press the `COPY` key. WINDOW 1 then looks like this, for example:

```
          +-------------------+
          ! INSTALL .COM      !
          ! TEST    .BAS      !
          ! TEST    .COM      !
          ! UTIL    .COM      !
          ! VDOS    .COM      !
          ! WS      .COM      !
          ! WSMGGS  .OVR      !
          ! WSOVLY1 .OVR      !
          +-------------------+
```

So these are the files that are on the source disk. We are interested in one particular file, `VDOS.COM`. We want to transfer it to the destination disk – it's lying next to us.

In WINDOW 2 you find the menu item `ENTER - Weiter zum naechsten Menue`. In the next menu we can pick the file(s) we want to copy. So press the `ENTER` key. WINDOW 2 then gets new contents and WINDOW 1 is cleared.

```
FILECOPY V3.0       (C)1986 by vortex GmbH

+-------+ +---------------------------------------------+ +-------+
!       ! !              Kopieren                       ! !       !
!       ! !          von Laufwerk A User 0              ! !       !
!  F    ! !          nach Laufwerk A User 0             ! !  F    !
!  E    ! !                 FENSTER 3                   ! !  E    !
!  N    ! +---------------------------------------------+ !  N    !
!  S    !                                                 !  S    !
!  T    !                                                 !  T    !
!  E    !                                                 !  E    !
!  R    ! +---------------------------------------------+ !  R    !
+--   --+ ! ↑ u ↓  - einen Dateinamen vor / zurueck     ! !       !
!  1    ! ! COPY   - Datei als zu kopieren kennzeichnen ! !  4    !
!       ! ! W      - mittels Wildcard kennzeichnen      ! !       !
!       ! ! ENTER  - diese Dateien kopieren             ! !       !
!       ! ! ESC    - Zurueck ins letzte Menue           ! !       !
!       ! !                FENSTER 2                    ! !       !
!       ! +---------------------------------------------+ !       !
!       !                                                 !       !
!       !                                                 !       !
+-------+                                                 +-------+
+-----------------------------------------------------------------+
!                            FENSTER 5                            !
+-----------------------------------------------------------------+
```
Window 1 is filled again with the directory of the source disk (see figure 1)

```
        (Bild 1)                        (Bild 2)
        +---------------+               +---------------+
        !               !               !               !
        !               !               !               !
        !               !               !               !
        !               !               ! INSTALL .COM  !
        !               !               ! TEST    .BAS  !
        !               !               ! TEST    .COM  !
        !               !               ! UTIL    .COM  !
Marke-> +-INSTALL .COM-+<-Marke  Marke->+-VDOS    .COM-+<-Marke
        ! TEST    .BAS  !               ! WS      .COM  !
        ! TEST    .COM  !               ! WSMSGS  .OVR  !
        ! UTIL    .COM  !               ! WSDVLY1 .OVR  !
        ! VDOS    .COM  !               !               !
        ! WS      .COM  !               !               !
        ! WSMSGS  .OVR  !               !               !
        ! WSDVLY1 .OVR  !               !               !
        !               !               !               !
        !               !               !               !
        !               !               !               !
        +---------------+               +---------------+
```

With the "cursor up/down" keys we move the whole directory upward until the file `VDOS.COM` comes to stand between the two "markers".

Now press the `COPY` key. `VDOS.COM` is marked in inverse video. By pressing the `ENTER` key we start the copying. WINDOW 1 is cleared and the single file `VDOS.COM` is shown. WINDOW 5 shows us the following:

```
Bitte Quell-Diskette einlegen und beliebige Taste druecken!
```

WINDOW 2 is cleared and we are told:

```
Einlesen von Daten. Bitte warten ...
```

The ticker changes to:

```
Bitte Ziel-Diskette einlegen und beliebige Taste druecken !
```

We take out the source disk, put in the destination disk instead (it must have been formatted beforehand!) and then press any key.

WINDOW 2 then contains a new piece of information:

```
Schreiben von Daten. Bitte warten ...
```

When the copying has finished, WINDOW 2 is filled again with the first menu text. Press `<ESC>` once more, and the ticker message changes to:

```
CP/M Diskette in Laufwerk A einlegen und beliebige Taste druecken!
```

Take out the destination disk and put in the disk with which you started CP/M earlier and from which you also loaded `FILECOPY`. Then press any key, and the prompt `A>` appears again.

---

## The CP/M Command XMON

**The Z80 monitor under CP/M**

The monitor can also be used under CP/M.

> **(!) Caution:** Only CP/M 2.2 without RAM expansion!

The following commands are blocked under CP/M for system reasons:

```
I, O, Y
```

All other commands can be used without restriction.

The monitor is called by means of the program `XMON.COM`. The command syntax is:

```
XMON<ENTER>
```

or

```
XMON Dateiname.Typ<ENTER>
```

So, for example,

```
A>XMON<ENTER>
```

or

```
A>XMON STAT.COM<ENTER>
```

The first variant only calls the monitor, while the second also loads the file `Dateiname.Typ` into memory from `100H` on. After entry, the monitor greets you with:

```
<start länge 0100>
*
```

| Value | Meaning |
|------|-----------|
| `start` | Start of the loaded file (under CP/M always `0100`) |
| `länge` | Length of the loaded file |

After you have left the monitor again with `<ESC>`, you can save the memory from `0100H` on to disk with the CP/M command `SAVE`.

---

## The CP/M Command SYSGEN

**Writing CP/M to the system tracks**

As you know, the command `MOVCPM` builds a CP/M of a "new" size. What we still need now is a way to get the modified CP/M, which is in memory or in the form of a file on disk, onto the system tracks of our system disk.

That is exactly what the program `SYSGEN` (SYStem GENerator) on the system disk is for. `SYSGEN` is a transient CP/M command.

Before we go on here, I'd like to show you briefly what the two system tracks actually look like.

| Track | Sector 01 | 02   | 03   | 04   | 05   | 06   | 07   | 08   | 09   |
|------|-----------|------|------|------|------|------|------|------|------|
| 0    | Boot      | PARA | empty | empty | empty | empty | empty | CP/M | CP/M |
| 1    | CP/M      | CP/M | CP/M | CP/M | CP/M | CP/M | CP/M | CP/M | CP/M |

Each sector has a storage capacity of 512 bytes. The "Boot" sector, the first sector on the whole disk, contains the so-called "bootstrap loader". This is a small program that is loaded into memory from the vortex disk directly by entering `|CPM,2<ENTER>` and then started. This small "loader" fetches the actual CP/M from track 0 and track 1, installs it in memory and starts it in a controlled way. After this process the CP/M load message has already been shown and the prompt `A>` with the cursor blinking behind it has appeared.

The "PARA" sector contains, for example, keyboard redefinitions or the screen color, which is then set automatically when CP/M is loaded. The contents of this sector can be changed with the program `INSTALL` (described further on).

Sectors 3, 4, 5, 6 and 7 on track 0 are still empty. If you have a vortex RAM expansion, these sectors are used as well.

All sectors marked "CP/M" contain the CP/M operating system. Exactly these sectors (and only these) are written by `SYSGEN`.

```
A>SYSGEN<ENTER>

SYSGEN 2.0   (C)1985 vortex GmbH

Quelldiskette in Laufwerk A,B oder RETURN ? <ENTER>
Zieldiskette in Laufwerk A,B oder RETURN ? A
Zieldiskette in Laufwerk A einlegen und irgendeine Taste druecken
Noch eine Diskette J/N ? N
Diskette mit Systemspur in Laufwerk A einlegen und irgendeine Taste druecken
```

With the first `<ENTER>` we tell `SYSGEN` that the new CP/M is in memory and is to be fetched from there. By entering "A" at the question "Zieldiskette Laufwerk A,B oder RETURN ?" we specify that the new CP/M is to be written to the system tracks of the disk in drive A.

```
A>SYSGEN<ENTER>

SYSGEN 2.0   (C)1985 vortex GmbH

Quelldiskette in Laufwerk A,B oder RETURN ? A
Quelldiskette in Laufwerk A einlegen und irgendeine Taste druecken

Zieldiskette in Laufwerk A,B oder RETURN ? B
Zieldiskette in Laufwerk B einlegen und irgendeine Taste druecken

Noch eine Diskette J/N ? N
Diskette mit Systemspur in Laufwerk A einlegen und irgendeine Taste druecken
```

In this example the CP/M was not modified with `MOVCPM` beforehand. It is simply read from the system tracks of the disk in drive A and then written to the system tracks of the disk in drive B.

```
A>SYSGEN<ENTER>

SYSGEN 2.0   (C)1985 vortex GmbH

Quelldiskette in Laufwerk A,B oder RETURN ? <ENTER>
Zieldiskette in Laufwerk A,B oder RETURN ? <ENTER>
Diskette mit Systemspur in Laufwerk A einlegen und irgendeine Taste druecken
```

With this use of `SYSGEN` nothing happens at all. A "new" CP/M is read from memory, but then it is not written to any system tracks.

---

## The CP/M Command DISKTOOL

**Formatting disks, copying whole disks, copying the system tracks, copying the parameter sector**

The CP/M command `DISKTOOL` (transient) is a "disk tool" in the truest sense of the word. It has a large number of important functions that make working with the disks in the drive possible in the first place.

Like `FILECOPY`, `DISKTOOL` is a fully menu-driven program that carries out the desired functions at the push of a button, so to speak.

When you have started `DISKTOOL` with `A>DISKTOOL<ENTER>`, the screen is cleared and the following main menu is shown:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!                                                                        !
!                                                                        !
+------------------------------------------------------------------------+

        +-------------------------------------------+
        ! 1 - Formatieren einer Diskette            !
        ! 2 - Komplettkopie einer Diskette erzeugen !
        ! 3 - CP/M-Systemspuren uebertragen         !
        ! 4 - nur den Parametersektor uebertragen   !
        ! ESC - zurueck ins CP/M                    !
        +-------------------------------------------+

    Bitte entsprechende Taste druecken !
```

As you see, from here you can branch into 4 submenus or leave `DISKTOOL` with `<ESC>` and return to CP/M.

In addition, as with `FILECOPY`, we have a ticker text here that prompts us for any actions connected with a selected function.

The screen is divided into two windows: the upper window shows which function we have just selected, the lower window shows us information about the start and the progress of that function.

Let's now go through the main menu item by item to see what is behind the individual functions.

### 1 – Formatting a Disk

If we press the "1" key, the screen changes:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  FORMATIEREN VON DISKETTEN                        !
!                                                                        !
+------------------------------------------------------------------------+

        +------------------------------------------+
        !                                          !
        !          Formatieren in Laufwerk ?       !
        !                                          !
        !          ESC - zurueck ins Hauptmenue    !
        !                                          !
        +------------------------------------------+

    Bitte entsprechende Taste druecken !
```

Clearly, we can only give disk drives here. A RAM floppy (vortex SP512) or a hard disk (vortex WD10 or WD20) cannot be handled with this "formatter". The drive is selected with the corresponding drive letter (normally A or B). Simply press the `A` key or the `B` key.

If you tried to select a drive that cannot be formatted with `DISKTOOL` (the C RAM floppy or the hard disk), the ticker shows the following error text:

```
Kein Diskettenlaufwerk - irgendeine Taste druecken!
```

If, for example, you have only one drive available (e.g. F1-S) and you then select drive B, it simply and plainly does not exist (one more reason to upgrade your F1-S to an F1-D). `DISKTOOL` answers this with the following ticker:

```
Laufwerk nicht verfügbar - irgendeine Taste druecken!
```

If the input is correct, two more submenus may follow, depending on whether a 3" drive is connected (automatically with X drives, with S/D stations via the vortex adapter cable FDA-1). The 3" drive, you see, has several formats. If the drive letter you entered belongs to the 3" drive, we get this screen:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  FORMATIEREN VON DISKETTEN                        !
!                                                                        !
+------------------------------------------------------------------------+

        +-------------------------------------------+
        ! 1 - Formatieren im Systemformat mit CP/M  !
        ! 2 - Formatieren im Systemformat ohne CP/M !
        ! 3 - Formatieren im Data-Only Format       !
        !                                           !
        !        ESC - zurueck ins letzte Menue     !
        +-------------------------------------------+

    Bitte entsprechende Taste druecken !
```

We can choose between three formats here, because exactly these three formats are also supported by the DDI-1 Schneider 3" controller, and we do want to stay compatible. There, however, these three formats only serve to tease a few kilobytes more storage capacity out of the 3" disk, because the storage capacity of a 3" disk is not exactly lavish (approx. 170 KB). The hefty 700 KB of a vortex disk are a different story, which is why one format is enough here.

The "teasing out" is done by, for example, leaving out the system tracks so that 2 more tracks can be filled with data. Now a quick word on what these formats look like:

**System format with CP/M:**

- 512 bytes per sector
- 40 tracks (0…39)
- 64 directory entries
- 9 sectors per track (`41HEX`…`49HEX`)
- 2 reserved tracks, with CP/M

**System format without CP/M (also called vendor format):**

- 512 bytes per sector
- 40 tracks (0…39)
- 64 directory entries
- 9 sectors per track (`41HEX`…`49HEX`)
- 2 reserved tracks, but without CP/M

**Data-only format:**

- 512 bytes per sector
- 40 tracks (0…39)
- 64 directory entries
- 9 sectors per track (`C1HEX`…`C9HEX`)
- no reserved tracks

Press the number for the format you want, and you're done. The following messages appear:

```
mit testen der Zieldiskette (J/N) ?

Formatieren Spur 039
```

We should answer the question "mit testen..." with "J" so that no write errors can "sneak in".

If the drive letter you entered selects a vortex drive, you get the following screen:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  FORMATIEREN VON DISKETTEN                        !
!                                                                        !
+------------------------------------------------------------------------+

        +------------------------------------------+
        ! 1 - Formatieren und CP/M uebertragen     !
        ! 2 - Nur Formatieren                      !
        !                                          !
        !                                          !
        !        ESC - zurueck ins letzte Menue    !
        +------------------------------------------+

    Bitte entsprechende Taste druecken !
```

- With "1", CP/M is copied to the newly formatted disk right away. If the 62K CP/M 2.2 of the vortex RAM expansion is present, the file `$OSC.SYS` is also copied automatically.
- With "2", the disk is only formatted.

The vortex format is a standard format:

- 9 sectors per track (1…9)
- 512 bytes per sector
- 80 tracks per side (0…79)
- 2 sides
- 2 reserved tracks
- 128 directory entries

Once you have started formatting, we get the messages:

```
mit testen der Zieldiskette (J/N) ?

Formatieren Spur 159
```

We should answer the question "mit testen..." with "J" so that no write errors can "sneak in".

### 2 – Making a Complete Copy

If we press the "2" key in the main menu, the screen changes:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  KOMPLETTKOPIE ERSTELLEN                          !
!                                                                        !
+------------------------------------------------------------------------+

        +-------------------------------------------+
        !              Quell-Laufwerk ?             !
        !              Ziel  -Laufwerk ?            !
        ! mit formatieren der Ziel-Diskette (J/N) ? !
        ! mit testen der Ziel-Diskette (J/N) ?      !
        !       ESC - zurueck ins letzte Menue      !
        +-------------------------------------------+

    Bitte entsprechende Taste druecken !
```

With this function we are able to copy whole disks. Unlike copying single files, where reading and writing is "file-oriented", this process reads track by track and writes track by track. This kind of copying is often also called "physical".

> **(!) Note:** Please note that a complete copy always requires the source disk and destination disk to have the same format. Copying from 3" to 5.25" and vice versa is therefore not allowed.

Answer the questions "Quell-Laufwerk ?" and "Ziel-Laufwerk ?" with the corresponding drive letters.

If you want to use a completely new disk (not yet formatted), enter a "J" at the question "mit formatieren...". If the disk is already formatted, enter "N".

> **(!) Important:** If you copy from drive A to drive A with formatting and forget to swap the source and destination disks, the source disk is destroyed!!!!!!

The question "mit testen..." should be answered with "J". It makes the program check continuously whether all data was transferred without errors (this is also called "verify").

### 3 – Copying the CP/M System

If we press the "3" key in the main menu, the screen changes:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  CP/M - SYSTEM KOPIEREN                           !
!                                                                        !
+------------------------------------------------------------------------+

        +------------------------------------------+
        !              Quell - Laufwerk ?          !
        !              Ziel  - Laufwerk ?          !
        !                                          !
        !       ESC - zurueck ins letzte Menue     !
        +------------------------------------------+

    Bitte entsprechende Taste druecken !
```

In the explanation of the CP/M command `SYSGEN` (earlier on) we already explained what the CP/M system tracks (track 0 and track 1) "look like". You remember that `SYSGEN` did not copy track 0 and track 1 completely, but only a part, albeit the largest one. These were the pure CP/M sectors. As we saw, however, there is also a BOOT sector (it contains the CP/M loader) and the parameter sector (contains, for example, keyboard translation tables). Then there are a few empty sectors, which, however, are also "full" in the case of the 62K CP/M together with our RAM expansion.

If you want to copy the complete system tracks, i.e. copy a working CP/M, you need a special function, and that is exactly what we have here. The source drive holds the disk from which the complete CP/M is to be read. The destination drive holds the disk to which this CP/M is to be copied. If we have only one drive, the ticker shows us when we have to swap the disks.

Please note that this function also copies the `$OSC.SYS` file of a 62K CP/M. In any case, after copying we get a bootable CP/M.

### 4 – Copying the Parameter Sector

If we press the "4" key in the main menu, the screen changes:

```
DISKTOOL 1.0        (C)1986 vortex GmbH

+------------------------------------------------------------------------+
!                                                                        !
!        Unterprogramm  PARAMETERSEKTOR KOPIEREN                         !
!                                                                        !
+------------------------------------------------------------------------+

        +------------------------------------------+
        !              Quell - Laufwerk ?          !
        !              Ziel  - Laufwerk ?          !
        !                                          !
        !       ESC - zurueck ins letzte Menue     !
        +------------------------------------------+

    Bitte entsprechende Taste druecken !
```

As mentioned before, the parameter sector is part of the boot tracks (sector 2 of track 0, to be precise). It contains, for example, keyboard redefinitions, autostart strings… The contents of this sector can be changed with the CP/M command `INSTALL`. Often you want to transfer a particular "CP/M setting" to other disks as well. You don't need to copy the whole CP/M; the parameter sector is enough.

The parameter sector to be copied is read from the disk in the source drive and written to the disk in the destination drive. If we have only one drive, the ticker shows us when we have to swap the disk.

---

## The CP/M Command INSTALL

**Changing the keyboard layout**

Sector 2 of track 0 of a vortex disk holds certain parameters, such as a different keyboard layout or the floppy disk timing constants. You can change (install) these values with the `INSTALL` command. `INSTALL` is menu-driven and divided into several "levels". Below you will find an example for each level that shows you how to work with `INSTALL`. `INSTALL` is a transient command, i.e. the file `INSTALL.COM` must be present on your disk.

### Example: Changing the Floppy Disk Timing Constants

```
A>INSTALL <ENTER>

INSTALL 1.0 - Power up Installationen   (C)1985 vortex GmbH

Im Parametersektor sind noch 458 Bytes frei

Änderung der

1 - Floppy Disk Zeitkonstanten
2 - Tastaturbelegung
3 - CP/M Parameter (I/O Byte, Power-up Strings)
4 - Communication Interface Parameter
5 - Installation/Ende

Ihre Wahl: 1
```

| No. | Parameter | Range | Default |
|----|-----------|---------|---------|
| 1 | Motor on Delay | 1,2,…,99 sec | 01 sec |
| 2 | Motor off Delay | 1,2,…,99 sec | 03 sec |
| 3 | Step rate 5.25" vortex drives | 2,4,…,14 msec | 04 msec |
| 4 | Step rate 3" Schneider drive | 2,4,…,14 msec | 12 msec |
| 5 | Main menu | | |

```
Ihre Wahl: 1
Neuer Wert: 4 <ENTER>
Ihre Wahl: 5

Neue Parameter installieren J/N ? J
CP/M neu starten J/N ? J

44k CP/M vers. 2.2 - 07/86 vortex GmbH
A>
```

In this example we went from the main menu into the submenu "Floppy Disk Zeitkonstanten" (floppy disk timing constants) and there increased the "Motor on Delay" time from 1 sec to 4 sec. We installed the new parameter right away (i.e. it was written to the parameter sector) and restarted CP/M.

Restarting CP/M makes sure that the new parameter takes effect at once. The contents of the parameter sector are only read when CP/M is loaded.

- The **"Motor on Delay"** is the time (delay) between the drive motor starting up and the read/write operation.
- The **"Motor off Delay"** is the time the motor keeps running after a read/write access. If this time were 0 sec, drive access would be extremely jerky. Imagine we had periodic drive access, say one per second: the motor would keep switching on and off all the time. If, on the other hand, you set a "motor off delay" longer than one second (e.g. 3 sec), the motor stays on and we get very "smooth" access, which of course also increases the life of the drives in the end.
- The **"Step rate"**, also called track-to-track time, is the time the read/write head, driven by a stepper motor (stepper), needs to move from one track to the track right next to it. This time cannot be changed at will. The smallest value is set by the maximum "nimbleness" of the stepper, the largest by vibrations of the read/write heads, since the operation of the read/write heads gets more and more "rough" as the step rate gets larger.

All these functions are mainly meant for those users who bought the vortex floppy controller separately, i.e. without drives, and perhaps want to use drives other than ours (e.g. TEAC or EPSON) (which might need somewhat different values). Otherwise you should never get into a situation where you have to change anything here.

### Example: Keyboard Layout

```
A>INSTALL <ENTER>

INSTALL 1.0 - Power up Installationen   (C) 1985 vortex GmbH

Im Parametersektor sind noch 458 Bytes frei

Änderung der

1 - Floppy Disk Zeitkonstanten
2 - Tastaturbelegung
3 - CP/M Parameter (I/O Byte, Power-up Strings)
4 - Communication Interface Parameter
5 - Installation/Ende

Ihre Wahl: 2

Im Parametersektor sind noch 458 Bytes frei

Tastatur Installationen

1 NORM Tabelle ist leer
2 SHIFT Tabelle ist leer
3 CTRL Tabelle ist leer
4 Funktionstasten Tabelle ist leer
5 Hauptmenue

Ihre Wahl: 4

Im Parametersektor sind noch 458 Bytes frei

EXPANSION Tabelle:

1=Alles löschen   2=Eintrag löschen   3=Neueintrag   4=Menue

Ihre Wahl: 3
Erlaubte Werte: <80>...<9F>
Token: <80>

(max. 128 Zeichen. CTRL H=HEX Eingabe, <ENTER>=Beenden.)
String: STAT <CTRL H>
(Es müssen 2 Zeichen eingegeben werden. CTRL C=Umschalten auf ASCII Eingabe)
HEX Werte: <0D> <CTRL C>
String weiter eingeben: <ENTER>

Im Parametersektor sind noch 450 Bytes frei

EXPANSION Tabelle:

Token   String
<80>    STAT<0D>

1=Alles löschen   2=Eintrag löschen   3=Neueintrag   4=Menue
Ihre Wahl: 4

Im Parametersektor sind noch 450 Bytes frei

Tastatur Installationen

1 NORM Tabelle ist leer
2 SHIFT Tabelle ist leer
3 CTRL Tabelle ist leer
4 Funktionstasten Tabelle ist belegt
5 Hauptmenue

Ihre Wahl: 1

Im Parametersektor sind noch 450 Bytes frei

NORM Tabelle:

1=Alles löschen   2=Eintrag löschen   3=Neueintrag   4=Menue

Ihre Wahl: 3

Tastennummer (0,...,79): 64
Token: <80>

Im Parametersektor sind noch 448 Bytes frei

NORM Tabelle:

Tastennummer        Token (<XY>=HEX Wert)
64                  <80>

1=Alles löschen   2=Eintrag löschen   3=Neueintrag   4=Menue

Ihre Wahl: 4

Im Parametersektor sind noch 448 Bytes frei

Tastatur Installationen

1 NORM Tabelle ist belegt
2 SHIFT Tabelle ist leer
3 CTRL Tabelle ist leer
4 Funktionstasten Tabelle ist belegt
5 Hauptmenue

Ihre Wahl: 5

Im Parametersektor sind noch 448 Bytes frei

Änderung der

1 - Floppy Disk Zeitkonstanten
2 - Tastaturbelegung
3 - CP/M Parameter (I/O Byte, Power-up Strings)
4 - Communication Interface Parameter
5 - Installation/Ende

Ihre Wahl: 5

Neue Parameter installieren J/N ? J
CP/M neu starten J/N ? J

44k CP/M vers. 2.2 - 07/86   vortex GmbH

A>
```

In this example we made use of the option of assigning a function (starting the program `STAT`) to a key.

As you have seen, besides assigning functions you can also simply assign a different value to any key. You can, for example, put a capital "Z" on the "Y" key and vice versa.

The term "token" keeps coming up here. The token is nothing other than the character we have assigned to a particular key. If we want to assign several characters, i.e. a function, to a key, we need the so-called "expansion tokens" (extended tokens). The character `<80>` in our example is one such expansion token.

Key 64, by the way, is the key directly to the right of the `ESC` key. You can find the keys and their numbers in your Schneider CPC manual.

In our example we gave key 64 a different meaning only in the NORM level. If we use the key together with the `SHIFT` key (SHIFT level) or the `CTRL` key (CTRL level), it has the same function as before.

`<0D>` has the same meaning as pressing the `ENTER` key.

Once we have left `INSTALL` and then press key 64, `STAT` is started.

So with the help of `INSTALL` you can redefine all keys (including the cursor keys and the numeric keypad). With expansion tokens you can assign whole functions to a key.

> **(!) Note:** Please note that you cannot make an unlimited number of reassignments. You can see that the free space in the parameter sector gets smaller with every new assignment.

Free keyboard assignment becomes important, for example, when you want to adapt a program like WordStar to your CPC. Instead of laboriously working with the control codes (e.g. `CTRL`+`S` moves the cursor one character to the left), we simply assign the codes to the keys (e.g. the "cursor left" key gets `CTRL`+`S`).

### Example: Autostart String

```
A>INSTALL <ENTER>

INSTALL 1.0 - Power up Installationen   (C) 1985 vortex GmbH

Im Parametersektor sind noch 448 Bytes frei

Änderung der

1 - Floppy Disk Zeitkonstanten
2 - Tastaturbelegung
3 - CP/M Parameter (I/O Byte, Power-up Strings)
4 - Communication Interface Parameter
5 - Installation/Ende

Ihre Wahl: 3

Im Parametersektor sind noch 448 Bytes frei

CP/M Installationen

1 Momentanes I/O Byte 81H
2 Autostart String ist nicht vorhanden
3 Drucker Initialisierung ist nicht vorhanden
4 3" Laufwerk ist nicht aktiviert
5 BIOS Fehlermeldungen sind eingeschaltet
6 Hauptmenue

Ihre Wahl: 2

(max. 128 Zeichen. CTRL H=Umschalten auf HEX Eingabe.
CTRL C=Abbrechen ohne Änderung. <ENTER>=String beenden)
String: INSTALL <CTRL H>
(Es müssen 2 Zeichen eingegeben werden. CTRL C=Umschalten auf ASCII Eingabe)
HEX Werte: <0D> <CTRL C>
String weiter eingeben: <ENTER>

Im Parametersektor sind noch 439 Bytes frei

CP/M Installationen

1 Momentanes I/O Byte 81H
2 Autostart String ist vorhanden
3 Drucker Initialisierung ist nicht vorhanden
4 3" Laufwerk ist nicht aktiviert
5 BIOS Fehlermeldungen sind eingeschaltet
6 Hauptmenue

Ihre Wahl: 6

Ihre Wahl: 5

Neue Parameter installieren J/N ? J
CP/M neu starten J/N ? J

44k CP/M vers. 2.2 - 07/86   vortex GmbH

A>
```

Every time CP/M starts, it checks whether there is an autostart string. If there is one, the commands it contains are executed one after the other.

If, for example, you only need CP/M to work with WordStar, you can define an autostart string as follows:

```
WS TEXT.TXT<0D>
```

This automatically starts WordStar and loads the text file `TEXT.TXT`. The `<0D>` has the same meaning as pressing the `ENTER` key.

### Example: Communication Interface Parameters

```
A>INSTALL <ENTER>

INSTALL 1.0 - Power up Installationen   (C)1985 vortex GmbH

Im Parametersektor sind noch 439 Bytes frei

Änderung der

1 - Floppy Disk Zeitkonstanten
2 - Tastaturbelegung
3 - CP/M Parameter (I/O Byte, Power-up Strings)
4 - Communication Interface Parameter
5 - Installation/Ende

Ihre Wahl: 4

Im Parametersektor sind noch 439 Bytes frei

Communication Interface Parameter

1   Baudrate Kanal A: Senden 19200
2   Baudrate Kanal A: Empfangen 19200
3   Baudrate Kanal B: Senden/Empfangen 9600
4   Kanal A: 8 Datenbits, 1 Stopbit, keine Paritaet
5   Kanal B: 8 Datenbits, 1 Stopbit, keine Paritaet
6   Hauptmenue

Ihre Wahl: 1

Mögliche Werte: 50, 75, 110, 150, 200, 300, 600, 1200, 1800,
2000, 2400, 3600, 4800, 9600, 19200

Neuer Wert: 3600 <ENTER>
```

If you have a vortex RS232C interface (serial interface) on your CPC, you can use this menu item to set parameters such as the baud rate.

### Special Application: Changing the Screen Colors

Finally, I would like to show you a very special use of the "autostart string" function: changing the screen colors when CP/M is loaded.

We choose "gray" as the background color and "black" as the pen color. For owners of a color monitor, this color pair gives a very good contrast, especially in 80-column mode.

```
A>INSTALL <ENTER>

INSTALL 1.0 - Power up Installationen   (C)1985 vortex GmbH

[Wahl: 3 -> CP/M Parameter, dann Wahl: 2 -> Autostart String]

String: <CTRL H>
HEX Werte:
<1C> <40> <77> <77> <1C> <61> <40> <40> <1D> <77> <77> <0D>
<CTRL C>
String weiter eingeben: <ENTER>

[Wahl: 6, dann Wahl: 5, dann installieren und neu starten]

44k CP/M vers. 2.2 - 07/86   vortex GmbH

A> ^\@ww^a@@^]ww^M
?
A>
```

Immediately after the string above has been sent, the screen colors change.

> **(!) Note:** Please note that you do not have to type the "<" and ">" when entering the string in `INSTALL`.

---

## The CP/M Command CASCOPY

**Copying between disk and cassette**

With a CPC464, or a CPC664 or CPC6128 with a cassette recorder, you have the cassette recorder in addition to the floppy. It should by no means be forgotten, even though CP/M is hardly ever seen together with a cassette recorder.

The cassette recorder with its ordinary music cassettes is a very cheap storage medium that can certainly be used, for example, for backups of not-too-important data.

```
A>CASCOPY<ENTER>

CASCOPY 2.0   (C)1985 vortex GmbH

Kopierrichtung (<,>) angeben:
Diskette > Cassette

Name der Diskettendatei: ED.COM<ENTER>
Name der Cassettendatei: E1.COM<ENTER>

Soll mit 2000 Baud aufgezeichnet werden J/N ? J
Press REC and PLAY then any key:

Saving E1.COM block 1
```

This example shows how we can transfer the file `ED.COM` from disk to cassette (`>`). We chose `E1.COM` as the name of the file on the cassette. Had we entered just `<ENTER>` instead of `E1.COM`, the file on the cassette would also have been named `ED.COM`.

The transfer runs at high speed (it is faster). As we are used to from a normal music recorder, the recorder is switched to "record" by pressing the REC and PLAY keys at the same time.

```
A>CASCOPY<ENTER>

CASCOPY 2.0   (C)1985 vortex GmbH

Kopierrichtung (<,>) angeben:
Diskette < Cassette

Name der Cassettendatei: TEST<ENTER>
Name der Diskettendatei: <ENTER>

Press PLAY then any key:
Loading TEST block 1
```

Exactly the reverse case: transferring a file from cassette to disk. On the disk the file will also be named `TEST` (no file type). Had we simply pressed the `ENTER` key at the question "Name der Cassettendatei:" (name of the cassette file), the next file found would have been transferred.

If the transferred file already exists on the disk, you are asked whether it should be deleted or not.

---

## The CP/M Command VDOS

**Switching back to VDOS/BASIC**

This CP/M command leaves the CP/M operating system properly.

There is also the option of a reset: pressing the `CTRL`+`SHIFT`+`ESC` keys at the same time resets your CPC.

```
A>VDOS<ENTER>
```

The screen is then cleared and the CPC's power-on messages appear.

---

## The CP/M Command FAST

**Speeding up the screen**

If you have already worked with CP/M on other computers, you may have noticed that CP/M screen output on your CPC is not exactly the fastest. The sometimes almost "agonizingly" slow output has surely annoyed you already.

The low output speed is not due to poor programming of the video controller, but to the fact that the CPC's screen memory is pixel-oriented. That is essential for the many graphics capabilities the CPC has. In addition, 3 different modes (20, 40 and 80 columns) can be set. The program parts that are constantly "run through" because of this make the screen output slow.

But if you consider that under CP/M really only the 80-column display is needed and that you can do without all the "graphics magic", then screen output could be much faster. The small program `FAST`, by the way also a transient command, takes advantage of these facts to provide a certain speed-up (about a factor of 2).

Please note that `FAST`, despite these restrictions, supports the complete "window technique".

`FAST` works like a switch.

```
A>FAST<ENTER>
```

`FAST` is switched on.

```
A>FAST<ENTER>
```

`FAST` is switched off again.

> **(!) Note:** Please note that a reset also switches off the "FAST routine".

---

## CP/M Error Messages and How to Fix Them

The German messages are all generated by the BIOS. It can therefore happen that a German error message is followed by an English one. Please note that the output of the German messages can be suppressed with the `INSTALL` command (see above).

### `Laufwerk d: Schreibfehler – Wiederholen J/N ?`

The write operation on the disk in the drive given by `d:` was interrupted by an error. If you answer "J", it is tried again. If you enter "N", the operation is aborted.

### `Laufwerk d: Lesefehler – Wiederholen J/N ?`

An error occurred while reading data from the disk in drive `d:`. If you answer "J", it is tried again. If you enter "N", the operation is aborted.

### `Laufwerk d: Diskette fehlt – Wiederholen J/N ?`

The drive that was accessed contains no disk, or is not locked properly. Insert a disk, or press the push button in properly, and enter "J".

### `Laufwerk d: Diskette hat Schreibschutz – Wiederholen J/N ?`

You wanted to write data to a disk that has a write-protect tab on it. Take the disk out, remove the tab and insert the disk again. Enter "J" and the operation is repeated. If you do not want this disk to be written to, simply enter "N" and thereby abort the operation.

### `keine CP/M Diskette – Wiederholen J/N`

You wanted to start CP/M from this disk with `|CPM<ENTER>`. But this disk is not a system disk. Either it lacks the boot sector (track 0 sector 1), or it has no CP/M. You may still be able to try with another disk by swapping it and entering "J".

### `Laufwerk d: Formatierfehler – Wiederholen J/N`

An error occurred while formatting this disk. Perhaps the disk is damaged, or simply try again.

### `Drucker nicht bereit - Wiederholen J/N`

You want to output something to the printer with `CTRL`+`P`, or you have a program that wants to access the printer. Perhaps the printer is still switched off, or not selected. Do you have a printer connected at all? If you find one of these points, fix the problem and then enter "J".

### `Operation wird wiederholt`

If you enter "J" at the question "- Wiederholen J/N ?", the system acknowledges with "Operation wird wiederholt" (operation is being repeated).

### `Operation wird abgebrochen`

If you enter "N" at the question "- Wiederholen J/N ?", the system acknowledges with "Operation wird abgebrochen" (operation is being aborted). It can often happen that a BDOS Error (always those annoying BDOS Errors!!) is printed after the aborted operation. Try to get around it with `CTRL`+`C`.

### `erlaubte Laufwerkskennungen sind A oder B!`

`SYSGEN`. If you entered a drive other than A or B here, you get the error message above.

### `SYSGEN wurde durch ^C abgebrochen`

`SYSGEN`. You entered `CTRL`+`C` at some input in `SYSGEN` and thereby aborted the program early.

### `Die Directory ist voll!`

`CASCOPY`. With the copy operation just performed (from cassette to disk), you want to write more than 128 entries into the directory of this disk. Delete useless files and start `CASCOPY` again.

### `Die Diskette ist voll!`

`CASCOPY`. This copy operation (cassette to disk) fills up the disk. Delete useless files, or insert a new disk.

### `Fehler! Cassettenstream war nicht offen.`

`CASCOPY`. An error occurred while transferring the data.

### `Geschützte Datei! Kann nicht gelesen werden.`

`CASCOPY`. Copy-protected cassette files cannot be transferred to disk with `CASCOPY`.

### `File konnte auf Diskette nicht gefunden werden.`

`CASCOPY`. The file that was to be transferred from disk to cassette cannot be found on the disk. Perhaps you made a typo, or you inserted the wrong disk.

### `Fehler! CASCOPY wird abgebrochen`

`CASCOPY`. A fatal error occurred during the transfer.

### `Ungültiger Dateiname:`

`CASCOPY`. The name of the file to be transferred is invalid. Perhaps it is too long, or it contains illegal characters.

### `<DATEI> ist bereits vorhanden. Löschen J/N ?`

`CASCOPY`. The name of the file to be copied to cassette or disk already exists there. It can be deleted ("J") or kept ("N").

### `Parametersector konnte nicht geladen werden`

When CP/M was loaded, the parameter sector was found to be damaged. Check this sector and, if necessary, install a new one.

### `Falscher Parametersector`

The contents of the parameter sector are "incomprehensible" to CP/M.

### `Expansion Buffer voll oder unerlaubtes Token`

There are errors in the keyboard reassignment table. Perhaps you used an illegal token.

### `Druckerstring konnte nicht abgeschickt werden.!`

The printer is probably not switched on, not connected, or not selected. Fix the cause and load CP/M again.

### `Loader: 3" Laufwerk=Laufwerk B.`

This additional loader message shows that the 3" drive is permanently drive B under CP/M. This setting can be fixed with `INSTALL`.

### `Parametersektor overflow! Installation nicht möglich! Abbrechen J/N?`

`INSTALL`. You want to pack more than 512 bytes of data into the parameter sector. That is too much!

### `INSTALL wird abgebrochen, da Parametersector nicht lesbar!`

`INSTALL`. When `INSTALL` starts, the parameter sector is read. But something is wrong with this sector; it cannot be read, or not read correctly.

### `Achtung! Parametersector konnte nicht korrekt geschrieben werden`

`INSTALL`. When you leave `INSTALL`, the new parameter sector is written to the disk. This time, unfortunately, it did not work. An error occurred while writing.

### `Diskette nicht eingelegt - Wiederholen J/N ?`

`DISKTOOL`. You forgot to insert a destination disk or to lock the drive button properly. Fix the problem and enter "J".

### `Diskette hat Schreibschutz - Wiederholen J/N ?`

`DISKTOOL`. The inserted destination disk has a write-protect tab. Remove it, if permitted, and enter "J".

### `Kein Diskettenlaufwerk!`

`DISKTOOL`. You wanted to work on the RAM floppy or the hard disk with a DISKTOOL function. That is not possible! `DISKTOOL` can only handle disk drives.

### `Disketten haben unterschiedliche Formate!`

`DISKTOOL`. You tried to copy a complete vortex disk to a 3" disk, or to transfer the system tracks of a vortex disk to a 3" disk. These functions only work if we have drives of the same format.

### `Laufwerk nicht verfügbar!`

`DISKTOOL`. You tried to select a drive that does not exist (e.g. drive D).

### `Diskette hat keine reservierten Systemspuren`

`DISKTOOL`. Let us assume you want to transfer the system tracks of a 3" disk to another 3" disk. If this disk has the Data-Only format, we get this message.

### `DISKTOOL 1.0 benoetigt unter dem RAM-Karten CP/M aktive System-Vektoren !`

`DISKTOOL`. If you also want to work with `DISKTOOL` under the 62K CP/M of the vortex RAM cards, you must switch on the system vectors when "patching".

### `Laufwerk d: Diskette hat Schreibschutz - Wiederholen J/N ?`

`FILECOPY`. The destination disk has a write-protect tab. Once you have removed it – if permitted – you can start the copy operation with "J".

### `<datei> existiert bereits ! Ueberschreiben J/N ?`

`FILECOPY`. The file that is about to be copied to the destination disk under this name already exists on the destination disk. If you simply want to overwrite it, enter "J". Otherwise answer "N" here.

### `FILECOPY 3.0 benoetigt unter dem RAM-Karten CP/M aktive System-Vektoren !`

`FILECOPY`. If you also want to work with `FILECOPY` under the 62K CP/M of the vortex RAM cards, you must switch on the system vectors when "patching".

---

## VDOS and CP/M Internals

Greatly simplified, the VDOS 2.11-X ROM can be divided into the following parts:

```
FFFF
+---------------------+
| |ROMCAT             |
| Fast-Routine        |  |FAST, |SLOW, |FRAME
+---------------------+  ca. FD5A
| Monitor             |  |XMON mit Diskettenmonitor
+---------------------+  ca. EA9E
| D O S               |  Disk Operating System, RSX-Befehle, Meldungstexte
+---------------------+  ca. CE5B
| B I O S             |  Basic Input Output System
+---------------------+  C000
```

All three areas are more or less independent units. The monitor and the extra commands at the end of the ROM in particular can be clearly separated, whereas DOS and BIOS are closely tied to each other.

### BIOS – Basic Input Output System

First of all, don't let yourself get confused – Basic has nothing to do with the programming language BASIC; here it means "fundamental" or "actual". The BIOS is the actual link between the floppy controller (hardware) and your CPC (software). It in turn falls into two logical blocks:

1. Modules for controlling the drives
2. Modules for controlling the printer, keyboard, screen – in short, the peripherals

The subroutines (modules) from item 2 actually have nothing to do with the drives, but they are needed for installing a CP/M operating system (see also Appendix: CP/M Under the Magnifying Glass).

Block 1 – the drive control – can itself be divided into three hierarchically successive levels:

- 1.0 Floppy disk driver routines
- 1.1 Basic functions
- 1.2 Record management (blocking/deblocking routine)

The floppy disk driver routines talk to the floppy disk controller directly through the corresponding PORTS. If you want to understand how they work and how they are structured, you have to study the hardware of the actual controller and of the drives in depth. That would lead too far here, so we refer you to the relevant specialist literature and data sheets.

The basic functions are subroutines which in turn use the floppy disk driver routines and can already be called by the user or the experienced machine-code programmer. The following basic functions are implemented in the BIOS of the VDOS ROM:

- 1.10 Read a physical sector
- 1.11 Write a physical sector
- 1.12 Format a whole track
- 1.13 Position the head carriage
- 1.14 Check the drive status
- 1.15 Switch off the drive motor

Input values are passed according to the following convention (the letters denote the internal Z80 registers):

| Register | Meaning |
|----------|-----------|
| C  | Sector number |
| D  | Track number |
| E  | Drive number |
| HL | Buffer address |

The carry flag tells you whether a drive operation succeeded or failed:

- **Carry set** means that the operation was successful
- **Carry=0** tells us that something went "wrong"

Now, the smallest block of data that both CP/M and the DOS can manage is not a physical sector (512 bytes), but a so-called **record** (128 bytes). Each physical sector can hold four such records. The record is really a "historical quantity" and dates back to the pioneering days of floppies. Back then the physical sector size was also 128 bytes – exactly one record. With the increasing arrival of integrated controller chips it soon became possible to read/write larger sectors too (256, 512, … bytes), which cut access times drastically. By that time, however, certain operating systems – CP/M above all – had already become established, and the record was the common data format. The BIOS was therefore extended by so-called blocking/deblocking routines. These are subroutines that split a physical sector into records or assemble it from records in a controlled way and control the access accordingly. Because with a physical sector size of 512 bytes, in the best case we only have to actually access the disk once every four records.

The following BIOS routines belong to the subject of record management:

- 1.20 Set track number
- 1.21 Set record number
- 1.22 Set record buffer (DMA) address
- 1.23 Read record into record buffer
- 1.24 Write record from record buffer
- 1.25 Translate track number if necessary

Each of these routines corresponds to an entry in the so-called CP/M BIOS vector (see Appendix: CP/M Under the Magnifying Glass).

The BIOS also contains a few additional functions, which we will only list briefly here:

- `SELDSK` selects a particular drive
- `BOOT` performs a CP/M cold start
- `WBOOT` performs a CP/M warm start

### DOS – Disk Operating System

The DOS is the actual heart of the VDOS ROM. As we have seen, the BIOS is only able to manage disk data by record or by sector. Files were not mentioned anywhere. For this reason, some basic knowledge is needed to work with the BIOS "without destroying anything", whereas direct access to the DOS usually ends with nothing worse than a "black eye".

Just like CP/M, VDOS is a file-oriented disk operating system. Similar to the index cards in a card file box, the data is not managed as single bytes (letters), but as higher-level logical units (files). So how does the DOS find a particular file on the disk again? If we dump all the index cards into a big box and stir them well, we hardly stand a chance of finding a particular card quickly. So what do we do? We sort the cards into a card file box and create a table of contents. The DOS does exactly the same: every file gets a name that identifies it uniquely(!). These names are stored, together with the place on the disk where the file can be found, in the so-called directory – the table of contents of the disk. This picture is greatly simplified, but it hits the nail right on the head.

Before we go into the DOS in more detail, a few basic words about data structures – indispensable for a deeper understanding:

As you may already know, or will very soon find out for yourself, you can use the same disks you use under BASIC for CP/M too. This is not a matter of course; the reason is that VDOS manages files in the same way as CP/M. This saves you the trouble of carefully keeping "CP/M disks" and "BASIC disks" apart – nothing can really go wrong. The following explanations therefore apply equally to VDOS and CP/M:

**Record:** Block of data of 128 bytes. The smallest amount of data in the data exchange with the floppy.

**Block:** The DOS has to keep books, so to speak, on the data stored on a disk. It works like this: take the disk apart into its tracks, cut the tracks open and attach one track to the next. This gives a long tape in which byte follows byte – we get a linear map of the disk. One way of managing the data would now be to give each byte a number according to its position on the tape. The administrative effort would be immense. With a capacity of 708 KB the DOS would have to remember 724992 numbers – that is not feasible in practice. So the tape (the disk) is divided into larger subunits – the blocks – and these blocks are given numbers. The block size on the vortex floppies is 4 KB (= 4096 bytes). As you can easily see, in this case – the division into blocks – far fewer numbers are needed, just under 200. No matter how small a file is, it always occupies at least one block on the disk. Unfortunately the matter has one small flaw: you inevitably always waste storage space. Imagine you have 20 files on the disk, each containing only 1 KB of data. But each file occupies one block, and so we lose 20·3 KB = 60 KB, although we actually only need 20·1 KB = 20 KB. You have to live with that. One way out would be to make the block size smaller, but that in turn would mean that we need more numbers to number the blocks. So you have to make compromises.

To understand the meaning of the block as a data structure in the DOS even better, let's take a closer look at the directory and its structure:

The directory – the table of contents of the disk – falls into so-called **entries**. Each entry is exactly 32 bytes long and has the following structure:

| Byte | Meaning |
|------|-----------|
| 0 | User number |
| 1-8 | File name |
| 9-11 | Extension |
| 12 | Extent number |
| 13,14 | DOS work variables |
| 15 | Record count (number of records in the current extent) |
| 16-31 | Block allocation table |

Our attention here goes to bytes 16-31 – the block allocation table. This holds, in order, the numbers of the blocks occupied by the file. Let's imagine we want to find a particular file on the disk. This is how the DOS goes about it: it searches the directory for an entry that contains the name of the file being looked for. If it finds such an entry, it can immediately tell from the block allocation table where the file lies. So far, so good. As we can easily work out, the block allocation table of a directory entry has room for at most 16 block numbers. With a block size of 4 KB we can therefore place at most a file of 64 KB length uniquely on the disk. But what if the file is 65 KB or larger? This is where the last data structure in our little excursion comes into play: the **extent**.

**Extent:** The extent denotes a block of data of 16 KB in size. Why 16 KB of all things? Well, this again results from "history": for disk drives with a small capacity it makes sense to choose small blocks, so as to waste as little space as possible. The smallest possible block size is 1 KB (all CPCs with a 3" drive "run" 1 KB blocks). With this block size we can fit exactly 16 block numbers into a directory entry, i.e. in this case one entry can place exactly 16 KB of data. If a file is larger, the DOS simply creates further entries (extents = extensions) with the same file name and remembers the number of the current extent in byte 12. If the DOS manages files with larger blocks, practically nothing changes in this mechanism, except that several extents then go into one directory entry (4 KB blocks -> 4 extents).

So we now know what a record, a block and an extent is, and have learned that files are stored on the disk block by block. Now a few more words about another very important item in a directory entry: the **record count** (see above, byte 15). Its job is to fix the exact end of a file and thus its exact size (in records). An example: block size 4 KB, file with a length of 8 records (= 1 KB). This file occupies exactly one block, but strictly speaking only its first quarter. So how does the DOS know where the file ends within the block? That is exactly what the record count is for: it counts the records within an extent (so it runs from 0..127, since exactly 128 records go into one extent) and thus makes it possible to determine the absolute end of a file independently of the block size. In addition, the DOS can tell from the record count whether another extent follows or not (another extent always follows when the record count is 127).

So now to the actual learning goal of this section: how the DOS works.

The DOS – more or less a program library – roughly falls into two groups of modules:

- 2.0 Routines for file-oriented directory and data manipulation
- 2.1 Adaptation modules

Both groups are partly linked hierarchically again. The routines of the second group – we have called them adaptation modules, and the reason will soon become clear – reference routines from the first group, and these in turn access the disk via the BIOS.

First, the first group and its subdivision:

- 2.01 Open file
- 2.02 Close file
- 2.03 Write record sequentially to file
- 2.04 Read record sequentially from file
- 2.05 Write record randomly to file
- 2.06 Read record randomly from file
- 2.07 Delete file
- 2.08 Give file a new name
- 2.09 Output directory to screen
- 2.010 Manipulate file attributes

As we can see, group 1 of the DOS functions provides basic operations for file/directory manipulation. Unlike AMSDOS, VDOS supports two kinds of disk access: sequential and random access. With sequential access a file can only ever be read/written in order. Random (or relative) access allows any records of the file to be read and also written in any order.

Group 1 still sits in the core of the DOS, i.e. no standardized entries into these routines are provided. If you want to use these routines anyway, you can only reach them by jumping directly into the ROM. When doing so, however, be absolutely sure to keep in mind that non-standardized entries can change from ROM revision to ROM revision. So you should by all means avoid such entries, especially when you write commercial software.

Group 2 – the adaptation modules – unlike group 1 all have standardized entries and can therefore always be reached via the same entries, independently of the revision. Now to the term "adaptation module": for this we have to go back a bit further.

The CPC BASIC (1.0 and 1.1) supports an external mass storage device through its own so-called stream number (see BASIC manual). On the 464 this is the built-in cassette recorder, on the 664/6128 the built-in 3" drive. BASIC does not talk to this mass storage device directly, but uses the so-called "Main Jump Vector" for it. This is a row of so-called standardized module calls located in memory from address `BB00H`; it is version-independent and therefore the same on all CPCs. "The same" here by no means means that the corresponding jump blocks must match byte for byte; rather it means that each entry has defined entry and exit parameters and fulfills a particular function – this is also called "black box behavior".

An example: let's assume you want to output the letter A to the screen. A look into the CPC firmware manual tells us that function 30, called `TXT OUTPUT`, is responsible for this. Its entry is at `BB5AH`. On entry, the accumulator (= Z80 register) must hold the character to be output (here an A, ASCII code `41H`). There is no exit condition. So it is completely irrelevant which routine in particular hides behind the entry `BB5AH`; all that matters is what it does, what data it must be fed with, and what it returns as an answer (= status, exit condition). This is also called a (software) interface (not to be confused with hardware interfaces, e.g. Centronics, RS232C, …).

Another example from everyday life: the mailbox. A mailbox is, in a way, also an interface with well-defined input and output conditions. Its job is to carry letters from place x to place y. What exactly happens to a letter after you have dropped it through the slot is really beside the point (unless it gets lost).

So, to give the terms a concrete meaning: the letter is the input value (compare the character in the accumulator for `TXT OUTPUT`), the transport from x to y is the job, the interface function (compare outputting a character to the screen). As long as everything goes well, there is no exit condition. If the letter gets damaged in the mail, the post office tells you so, and that would then be a corresponding exit condition – the status message, so to speak.

After this little excursion into the postal (dis)service, back to our mass storage on the CPC: BASIC communicates with this mass storage via 13 entries in the "Main Jump Vector", functions 125 to 137 (see CPC firmware manual). For the sake of completeness we will list these functions here. Important: the function names follow the nomenclature of the firmware manual and therefore always begin with `CAS...`. This does not mean, however, that only the cassette recorder can be addressed with them; rather, any mass storage device can be addressed. All we have to do is replace the entries with others (bend the vector) that lead to routines with the same entry/exit conditions and the same jobs – for example a floppy drive.

Before we get in medias res, one more annoying but all the more important detail that will surely make the confusion complete. The function descriptions will often talk about a so-called **block**. However, the blocks meant here (unfortunately) have nothing at all to do with the blocks of the disk organization described above; instead they mean portions of data of 2 KB in size, which is simply the form in which BASIC needs them.

#### Function 125: `CAS IN OPEN` – Entry `BC77H`

**Job:** Open a file on the read channel and read its first block.

**Entry:**
- `HL` = pointer to file name
- `B` = length of the file name
- `DE` = pointer to 2 KB block buffer

**Exit:**
- File could be opened correctly: `Carry=1 Z=0`, `HL` = pointer to file header, `DE` = data destination address, `BC` = file length, `A` = file type
- Read channel was already in use: `Carry=0 Z=0`

#### Function 126: `CAS IN CLOSE` – Entry `BC7AH`

**Job:** Close the file on the read channel properly.

**Entry:** none

**Exit:**
- File could be closed: `Carry=1`
- No file was in use: `Carry=0`

#### Function 127: `CAS IN ABANDON` – Entry `BC7DH`

**Job:** Close the read channel immediately.

**Entry:** none. 

**Exit:** none.

#### Function 128: `CAS IN CHAR` – Entry `BC80H`

**Job:** Fetch the next character from the read channel, from the file currently open there.

**Entry:** none

**Exit:**
- Character could be fetched properly: `Carry=1 Z=0`, character in the accumulator
- End of file was detected: `Carry=0 Z=0`

#### Function 129: `CAS IN DIRECT` – Entry `BC83H`

**Job:** Read the file currently open on the read channel into memory in one go. Functions 129 and 128 are mutually exclusive. So you cannot, for example, first read the first 5 characters one by one and then fetch the rest in one piece.

**Entry:** `HL` = destination address where the data is to be read to

**Exit:**
- File could be read in properly: `Carry=1 Z=0`, `HL` = entry into the data area (only meaningful if it is a machine-code program)
- File was not open at all: `Carry=0 Z=0`

#### Function 130: `CAS RETURN` – Entry `BC86H`

**Job:** Send the character last read with `CAS IN CHAR` back into the read channel.

**Entry:** none. 

**Exit:** none.

#### Function 131: `CAS TEST EOF` – Entry `BC89H`

**Job:** Test whether the end of the file has been reached.

**Entry:** none

**Exit:**
- End of file not yet reached: `Carry=1 Z=0`
- End of file reached: `Carry=0 Z=0`

#### Function 132: `CAS OUT OPEN` – Entry `BC8CH`

**Job:** Open a file on the write channel.

**Entry:**
- `HL` = pointer to file name
- `B` = length of the file name
- `DE` = pointer to 2 KB block buffer

**Exit:**
- File could be opened properly: `Carry=1 Z=0`, `HL` = pointer to file header
- Write channel is already in use: `Carry=0 Z=0`

#### Function 133: `CAS OUT CLOSE` – Entry `BC8FH`

**Job:** Close the write channel properly.

**Entry:** none

**Exit:**
- File could be closed properly: `Carry=1 Z=0`
- No file was in use at all: `Carry=0 Z=0`

#### Function 134: `CAS OUT ABANDON` – Entry `BC92H`

**Job:** Close the write channel immediately.

**Entry:** none. 

**Exit:** none.

#### Function 135: `CAS OUT CHAR` – Entry `BC95H`

**Job:** Send a character into the write channel.

**Entry:** accumulator holds the character

**Exit:**
- Character could be delivered: `Carry=1 Z=0`
- Write file was not open at all: `Carry=0 Z=0`

#### Function 136: `CAS OUT DIRECT` – Entry `BC98H`

**Job:** Send a contiguous memory area into the write channel. Functions 135 and 136 are again mutually exclusive.

**Entry:**
- `HL` = pointer to memory area
- `DE` = length of the memory area
- `BC` = entry address (only meaningful for machine-code programs)
- `A` = file type

**Exit:**
- Writing worked properly: `Carry=1 Z=0`
- No file was open for writing: `Carry=0 Z=0`

#### Function 137: `CAS CATALOG` – Entry `BC9BH`

**Job:** Bring the directory to the screen. This function uses the read channel and therefore cannot be used while that channel is otherwise occupied.

**Entry:** `DE` = pointer to 2k work buffer

**Exit:**
- Everything OK: `Carry=1 Z=0`
- Read channel was in use: `Carry=0 Z=0`

If a floppy is connected to the system when the CPC is switched on, then during the so-called ROM WALK (here the operating system checks all the so-called background ROMs one after the other and thereby finds out which peripherals are available) the part of the "Main Jump Vector" that routes the mass storage interface toward the cassette recorder is bent over to the floppy. This is done simply by replacing the entries into the cassette recorder routines with corresponding entries into the floppy routines (adaptation modules).

---

### RAM Variables of BIOS and DOS

Although the routines themselves are in ROM, both BIOS and DOS also need RAM for their housekeeping. This RAM falls into two groups:

- 3.0 non-relocatable RAM
- 3.1 relocatable RAM

As the name already says, the non-relocatable RAM area cannot be moved, i.e. it is addressed absolutely by the DOS/BIOS. The relocatable RAM area, on the other hand, is only addressed indexed and can therefore be moved freely. The reason why this RAM area has to be movable lies in the firmware architecture of the CPCs: every peripheral (background) ROM can reserve RAM for itself during the ROM WALK. That alone is not earth-shattering yet; but in addition, every background ROM also has a so-called ROM number. The ROM WALK runs from number 7 -> 0 on the 464 and 15 -> 0 on the 664/6128. The ROM number is a hardware matter and is determined by the electronics around the ROM.

The RAM reservation now works as follows (464 only here; 664/6128 correspondingly): first ROM number 7 reserves its space in RAM, then ROM number 6 can reserve space directly below it, and so on. But that means that before the actual ROM WALK a ROM cannot know yet where its RAM area will be in memory, since it has no idea how much space the ROMs "above" it will reserve. That is why the ROM references all its variables in the relocatable RAM area indexed: it receives the base address of its RAM area from the kernel (in the IY register) and adds a corresponding offset to it.

If you write a program that is later to be "burned" into a (background) ROM, strictly observing the indexed addressing of RAM variables, the ROM can later be plugged into any ROM socket and will work correctly right away. The whole thing has just one catch, which usually does no harm: indexed addressing is more costly than absolute addressing, and this in turn makes the program somewhat "slower" (usually not measurable) and also longer (usually more of a nuisance, since space in the ROM is limited).

Since the whole memory layout (under BASIC) of the CPCs was designed around this dynamic space reservation, "absolute" RAM is available only to a very limited extent (most of the "absolute" RAM is occupied by the BASIC interpreter and the operating system). One of the few contiguous, large, "absolute" RAM areas is at `BE80H` (up to the stack), and it is also used by the floppy firmware.

> **(!) Important:** Below you will find the RAM areas used by the VDOS 2.11-X ROM, listed by their meaning. Of course we try not to change these areas in revisions either, but sometimes this cannot be avoided. So be careful before you go "poking around" to your heart's content ("peeking" is of course allowed).

#### Non-Relocatable RAM Area of the VDOS 2.11-X ROM

(all addresses hexadecimal)

> **(!) Note:** A `*` in the second column means that the same variable can also be found at the same place under AMSDOS. The number in the third column gives the length of the variable in bytes.

| Address | AMSDOS | Length | Meaning |
|---------|--------|-------|-----------|
| BE40 | * | 2 | DPH address drive A |
| BE42 | * | 2 | DPB address drive B |
| BE44 | * | 2 | Motor on counter: time in 50 msec units from switching on the motor until the first access. Must be observed so that the disk rotates at a constant speed. Default value: 50 |
| BE46 | * | 2 | Motor off counter: time in 50 msec units from the last access until the motor is switched off. If the motor were switched off right after the access, you would have to wait through the motor-on phase again if another access followed only a little later, i.e. access would be slowed down drastically. Default value: 250 |
| BE49 | * | 1 | Head settling time in 1 msec units. After the head carriage has moved to a track, the carriage keeps vibrating mechanically for a certain time. You have to wait for the carriage to settle in order to avoid read/write errors. Default value: 30 |
| BE4A | * | 1 | Combined step rate for the 5.25"/3.5" and the 3" drive. The upper 4 bits are the step rate of the 3" drive in 1 msec units and the lower 4 bits that of the 5.25"/3.5" drive in 1 msec units. Default value: 196 |
| BE4B | * | 8 | Result buffer for the µPD 765 (see data sheet) |
| BE53 | * | 1 | Seek disk number (logical drive number; set by the BIOS routine `SELDSK`) |
| BE54 | * | 1 | Seek track number (logical track number; set by the BIOS routine `SELTRK`) |
| BE55 | * | 1 | Seek sector number (logical sector number = record number; set by the BIOS routine `SELSEK`) |
| BE56 | * | 1 | Host disk number (number of the physical drive; determined in the BIOS) |
| BE57 | * | 1 | Host track number (physical track number; determined in the BIOS) |
| BE58 | * | 1 | Host sector number (physical sector number; determined in the BIOS) |
| BE59 |   | 1 | Seek/host flag (see below) |
| BE5A |   | 1 | unalloc record counter |
| BE5B |   | 1 | unalloc drive number |
| BE5C |   | 1 | unalloc track number |
| BE5D |   | 1 | unalloc sector number (logical) |

**Meaning of the seek/host flag bits (BE59):**

| Bit | Meaning |
|-----|-----------|
| 0–3 | Write type: 0 = allocated, 1 = directory, 2 = unallocated |
| 4 | 0 = write, 1 = read |
| 5 | 1 = pre-read |
| 6 | Host active flag |
| 7 | Host write flag |

Bits 5–7 are needed for blocking/deblocking.

**Note on the unalloc variables:** The BIOS basically has three ways of writing a record:

1. Directory write
2. Allocated write
3. Unallocated write

As we already know, in a "blocked" BIOS the physical write operation does not necessarily have to be carried out immediately for every record write. There is, however, one very important exception here, and that is write operations to the directory. Of course the directory must always be completely up to date, which is why every directory record to be written must also be put onto the disk immediately (no blocking!).

Before a record can be read or written, the "coordinates" of the record must be passed to the BIOS via `SELDSK`, `SELTRK`, `SELSEK` and `SETDMA` – such an access is also called **unallocated**, since the block the record is to be written to/read from is fully defined. But there is also another way of accessing records, namely exactly when the block coordinates have already been passed to the BIOS (**allocated**) and now all the following records of the block are to be read/written. This access is of course faster than the one into a new (unallocated) block.

| Address | AMSDOS | Length | Meaning |
|---------|--------|-------|-----------|
| BE5E |   | 1 | Seek/recalibrate/ID flag |
| BE5F |   | 1 | Temporary storage for the step rate of the currently selected drive |
| BE60 | * | 2 | Address of the current record buffer; 128 bytes (set by the BIOS routine `SETDMA`) |
| BE62 | * | 2 | Address of the host buffer (512 bytes). Sector buffer for one physical sector. |
| BE64 |   | 1 | Retry count: number of attempts in case of an error. Default value: 16 |
| BE65 |   | 2 | Temporary stack storage on BIOS entry |
| BE67 | * | 6 | Tick block for the motor on/off counter |
| BE6D | * | 7 | Event block for the motor on/off counter |
| BE74 |   | 1 | Temporary storage for the uPD command |
| BE75 |   | 2 | Base address of the relocatable DOS RAM area. Default value: `A700H` if VDOS is ROM number 7 |
| BE77 |   | 2 | One-time entry for the CAS functions: if the value is not 0, the next CAS call jumps to this address once, after which the value is cleared. Default value: 0 |
| BE79 |   | 2 | Code string for P protection (set with the RSX command `|CODE`) |
| BE7B |   | 1 | Message flag: 0 = error messages are shown, FFH = error messages are suppressed |
| BE7C |   | 1 | Under BASIC: EOF flag (0 = no test, only the physical end of file counts (`|DERROR,3`, default value), FFH = test for the EOF marker `1AH` (`|DERROR,2`)); under CP/M: FAST flag (0 = normal, FFH = sped up) |
| BE7D |   | 2 | No meaning under BASIC; under CP/M: base address of the relocatable RAM area |
| BE7F |   | 1 | X drive under BASIC only: configuration byte (0 = 5.25" drive is drive A, 1 = 5.25" drive is drive B); set by the RSX command `|X` |

The following variables differ greatly between BASIC and CP/M and are therefore dealt with separately:

#### BASIC

| Address | Length | Meaning |
|---------|-------|-----------|
| BE80 | 2 | Temporary storage for the stack pointer |
| BE82 | 1 | Temporary storage for the error code |
| BE83-BE8E | | no meaning |
| BE8F | 3 | Select disk DOS indirection (jumps to the BIOS routine `SELDSK`) |
| BE92 | 3 | Set track DOS indirection (jumps to the BIOS routine `SETTRK`) |
| BE95 | 3 | Set sector DOS indirection (jumps to the BIOS routine `SETSEK`) |
| BE98 | 3 | Set DMA DOS indirection (jumps to the BIOS routine `SETDMA`) |
| BE9B | 3 | Read record DOS indirection (jumps to the BIOS routine `READ`) |
| BE9E | 3 | Write record DOS indirection (jumps to the BIOS routine `WRITE`) |
| BEA1-BEB6 | | Routine for the error patch (BASIC 1.0) |
| BEBA | 2 | Base address for random-access file management |
| BEBF | 1 | Number of the first sector for disk I/O |
| BEC0 | 1 | Number of the last sector for disk I/O |

During the ROM WALK, up to the moment when BASIC has finished its initialization, the following variables have a different meaning:

| Address | Length | Meaning |
|---------|-------|-----------|
| BE24 | 2 | Original address of the firmware routine `KM DISARM BREAK` |
| BE26 | 3 | Far address of the VDOS routine that intercepts `KM DISARM BREAK` |
| BE2D | 1 | Number of `KM DISARM BREAK` calls still expected (initial value 2) |

**A few words on the meaning of the DOS indirections and on how the hello sequence works:**

The DOS indirections form a well-defined interface between DOS and BIOS. The DOS accesses the BIOS, and thus the drives, only via these indirections. You will find the description of the parameters passed in the CP/M part, in the explanation of the BIOS entry vector.

The hello sequence, the "turn key mechanism" – which only 464 owners get to enjoy, though – is based on the idea of intercepting BASIC after the ROM WALK, before it jumps into the READY loop. (This is only possible on the 464/BASIC 1.0!) However, there is no point in patching BASIC indirections already during the ROM WALK, since BASIC, after it has carried out the ROM WALK, first initializes all BASIC indirections and would thus erase the patch. That is why, during the ROM WALK, VDOS 2.11-X intercepts the firmware entry `KM DISARM BREAK` (`BB48H`), which BASIC 1.0 calls twice during its initialization. On the first call only the original routine is executed. On the second call VDOS copies the DOS indirections and the error patch to `BE8FH`, sets the BASIC error indirection to the error patch and – if no key is pressed – copies the hello loader into RAM at `BF00H` and starts it. The loader checks the drive status of drive A. If there is no disk in the drive, it aborts. If there is a disk in the drive, the loader looks for the file `HELLO.BAS`. If it has found it, it loads it into BASIC memory and starts it.

#### CP/M

| Address | AMSDOS | Length | Meaning |
|---------|--------|-------|-----------|
| BE80 | * | 3 | Message flag: 0 = messages on, FFH = messages off. Entry: accumulator = new value. Exit: accumulator = old value |
| BE83 | * | 3 | Initialize time constants. `HL` = pointer to parameter area |
| BE86 |   | 3 | Various functions: accumulator = FFH and E = drive number (0,1) -> HL = pointer to DPB flag byte; accumulator = FEH -> sets or clears the FAST flag; otherwise: accumulator = first sector number of the disk format (as in AMSDOS) -> select the format for the 3" drive |
| BE89 | * | 3 | Read a physical sector. Entry: HL=sector buffer, C=first sector, B=last sector (if multi-sector), E=drive, D=track. Exit: Carry=1/accumulator=0 successful, Carry=0/accumulator=error code |
| BE8C | * | 3 | Write a physical sector (parameters as for reading) |
| BE8F | * | 3 | Format a whole track. Entry: HL=sector buffer, E=drive, D=track |
| BE92 | * | 3 | Position the head carriage. Entry: E=drive, D=track |
| BE95 | * | 3 | Test the drive status. Entry: accumulator=drive number. Exit: Carry=1 -> accumulator=ST3, Carry=0 -> HL=pointer into the uPD result buffer |
| BE98 | * | 3 | Change the retry count. Entry: accumulator=new value. Exit: accumulator=old value |
| BE9B | * | 3 | BIOS entry. Saves the stack and ensures the correct ROM configuration |
| BE9E |   | 3 | Accumulator = 0 or FFH: register saving on BIOS entry on (0) or off (FFH, faster, but IX, IY and the alternate register set are changed). Exit: accumulator = old value. Any other value: switch off the motor immediately |
| BEA1 |   | 3 | Initialize SIO (SET SIO) |
| BEA4 | * | 3 | Initialize console buffer. Entry: HL=pointer to string, A=clear flag |
| BEA7 |   | 3 | Input status SIO 1 |
| BEAA |   | 3 | Input status SIO 2 |
| BEAD |   | 3 | Output status SIO 1 |
| BEB0 |   | 3 | Output status SIO 2 |
| BEB3 |   | 3 | Get character from SIO 1 |
| BEB6 |   | 3 | Get character from SIO 2 |
| BEB9 |   | 3 | Send character to SIO 1 |
| BEBC |   | 3 | Send character to SIO 2 |

In VDOS 2.11-X the SIO routines `BEA7`–`BEBC` drive the vortex RS232C interface (Z80 DART).

#### Variables of the Disk Monitor

| Address | Length | Meaning |
|---------|-------|-----------|
| BEC1-BEC7 | | not used in VDOS 2.11-X. The disk monitor works directly with the BIOS variables `BE53` (drive, L), `BE54` (track, T), `BE55` (record, S) and `BE60` (buffer address, B) |
| BE00 | 1 | 0 = monitor, FFH = disk monitor active |
| BEC8 | 1 | Number of the upper ROM (as set by the Y command) |
| BEC9 | 1 | 0 = firmware ROM off, FF = on (as set by the X command) |

#### Variables of the Monitor

| Address | Length | Meaning |
|---------|-------|-----------|
| BECD | 3 | Far address for the FAST indirection |
| BED0 | 3 | Far address for the breakpoint |
| BED3 | 2 | current address for the S command |
| BED5 | 2 | current address for the L command |
| BED7 | 2 | current address for the F and A commands |
| BED9 | 2 | current address for the D command |
| BEDD | 1 | CP/M flag: 0 = VDOS active, FF = CP/M active |
| BEDE | 2 | Stack pointer on entry into the monitor |
| BEE0 | 1 | RAM bank (as set by the Z command): 0 = off, 20H + bank number = on |
| BEE1 | 1 | internal variable |
| BEE2 | 1 | Opcode temporary storage |
| BEE3 | 2 | Temporary storage for program branches |
| BEE5 | 2 | Temporary storage for the stack pointer |
| BEE7 | 2 | Temporary storage for HL |
| BEE9 | 2 | Number of trace steps |
| BEEB | 2 | Temporary storage for AF |
| BEEC | 2 | User AF |
| BEEE | 2 | User BC |
| BEF0 | 2 | User DE |
| BEF2 | 2 | User HL |
| BEF4 | 2 | User IX |
| BEF6 | 2 | User IY |
| BEF8 | 2 | User SP |
| BEFA | 1 | internal variable |
| BEFB | 2 | User PC |
| BEFD | 1 | Displacement for relative Z80 instructions |
| BEFE | 1 | internal flag (temporary storage of the printer switch) |
| BEFF | 1 | Bit 0 = printer on (as set by the P command); bits 5-7 = internal flags of the T command |
| BF00 | 24 | Breakpoint work area |
| BF80 |   | Monitor stack |

#### Relocatable RAM Area of the VDOS 2.11-X ROM

The relocatable RAM area of the VDOS ROM differs largely from that of the AMSDOS ROM. All addresses given are relative and refer to the base of the RAM area. If AMSDOS is present, VDOS 2.11-X shares the RAM area of the AMSDOS ROM (base address `A700H`) and does not reserve its own; without AMSDOS it reserves `500H` bytes, and the base address is then also `A700H`. The base address is stored in `BE75`.

| Offset | Length | Meaning |
|--------|-------|-----------|
| 0 | 1 | Login flag drive A. 0 = drive not logged in yet, FFH = drive logged in |
| 1 | 1 | Login flag drive B (see above) |
| 2 | 1 | internal variable |
| 3 | 2 | DPH address of the default drive |
| 5 | 1 | current user number |
| 6 | 1 | current drive number |
| 7 | 2 | Pointer to the current FCB (file control block) |
| 9 | 1 | Row counter for the CAT/DIR command |
| A | 2 | Directory counter |
| C-12 | 7 | internal variables |
| 13 | 1 | Number of characters for the FCB - directory entry comparison |
| 14 | 1 | Drive number from the current FCB |
| 15 | 1 | DOS flag 2: bit 1 = read/write random (0 = read, 1 = write) |
| 16-18 | 3 | internal variables |
| 19 | 1 | DOS flag 1: bit 1: 0=random not active, 1=random active; bit 2: 0=write, 1=read; bit 3: 0=random, 1=sequential |
| 1A,1B | 2 | internal variables |
| 1C | 2 | Temporary storage for the DMA address |
| 1E | 1 | Storage for the number of CAT entries |
| 1F | 2 | Pointer into the CAT RAM buffer |
| 21,22 | 2 | internal variables |
| 23 | 2 | Storage for the stack pointer in case of an error |
| 25-44 | 32 | Work FCB |
| 45-68 | 36 | Input FCB |
| 69-8C | 36 | Output FCB |
| 92-B2 | 33 | Input header |
| B3-D3 | 33 | Output header |
| E0-15F | 128 | Record buffer |
| 164-178 | 21 | CAS input vector |
| 179-187 | 15 | CAS output vector |
| 188 | 3 | CAS CAT vector |
| 18B | 3 | Far address of the DOS entry handler |
| 190 | 23 | ALV 0 |
| 1A7 | 23 | ALV 1 |
| 1BE | 128 | Directory buffer |
| 23E | 512 | Host buffer |
| 43E | 16 | DPH 0 |
| 44E | 16 | DPH 1 |
| 45E | 39 | CSV 0 |
| 485 | 39 | CSV 1 |
| 4AC | 25 | DPB 0 |
| 4C5 | 25 | DPB 1 |

**Remarks:** The input and output FCBs have the standard CP/M structure (see CP/M Under the Magnifying Glass).

The headers have the following structure (all addresses refer to the start of the header):

| Address | Length | Meaning |
|---------|-------|-----------|
| 0 | 1 | Mode byte: 1 = CHAR mode, 2 = DIRECT mode |
| 1 | 2 | Address of the block buffer |
| 3 | 2 | Pointer to the next character in the block buffer |
| 5 | 1 | User byte |
| 6 | 8 | File name |
| E | 3 | Extension |
| 11 | 4 | not used |
| 15 | 1 | Number of the current block |
| 16 | 1 | 00 = not the last block yet |
| 17 | 1 | File type |
| 18 | 2 | File length |
| 1A | 2 | Data allocation address |
| 1C | 1 | 00 = not the first block |
| 1D | 2 | Length |
| 1F | 2 | Start address for a machine-code program |
| 21 | 3 | Byte counter for the DOS |
| 24 | 2 | Checksum |

#### Random-Access File Management

VDOS 2.11-X can manage 16 random-access files at the same time (16 channels). The field length on each channel is arbitrary and limited only by the available memory. The BASIC `HIMEM` is adjusted via the RSX command `|FILES`.

With random-access file management active, the BASIC RAM has the following structure:

![BASIC RAM layout](basic_mem.png)

The individual work areas are connected by link addresses, so the DOS only has to remember the base address of the whole area. The work area of a channel has the following structure (all addresses refer to the base address of the channel work area):

| Address | Meaning |
|---------|-----------|
| 0 | Channel number (possible numbers are between 0 and 127, both inclusive. If bit 7 is set, the channel is currently active.) |
| 1 | Link address to the next channel area |
| 3 | max. field length; defined in `|FILES` |
| 5 | current field length; defined in `|OPEN` |
| 7 | current record number |
| 9 | Pointer to the record buffer |
| B | unused |
| D | 36 FCB |
| 31 | Field masks (max. 16) |
| 51 | unused |
| 5A | Record buffer (length defined in `|FILES`) |

#### Structure of the Time Constants Area

| Offset | Length | Meaning |
|--------|-------|-----------|
| 0 | 2 | Motor on counter |
| 2 | 2 | Motor off counter |
| 4 | 1 | not used |
| 5 | 1 | Head settling time |
| 6 | 1 | combined step rate |
| 7 | 1 | HUT byte (see uPD data sheet) |
| 8 | 1 | HLT byte (see uPD data sheet) |

---

## CP/M Under the Magnifying Glass – The CP/M Operating System

Just like CPC BASIC, CP/M is an operating system in its own right. It consists of three components:

- the **Console Command Processor** – CCP
- the **Basic Disk Operating System** – BDOS
- the **Basic Input Output System** – BIOS

CP/M was developed by DRI (Digital Research Inc.), and DRI alone holds the sole right to grant licenses. So if you pass on one of your own programs on a disk, make sure there are no traces of CP/M on it, or you will be guilty of a copyright infringement.

Before we take a closer look at the individual parts of CP/M, here first of all is the memory layout:

![Memory layout of CP/M](cpm_memory.png)

### Zero Page

The Zero Page (page 0; address `00`–`FFH`) is needed by CP/M as a data and work area. Almost every byte has a meaning, and careless manipulation usually makes CP/M crash.

| Address | Meaning |
|---------|-----------|
| 00H-02H | Warm start; holds a jump to `biospage+3` |
| 03H | I/O byte |
| 04H | Default drive |
| 05H-07H | BDOS entry; holds a jump to `bdospage+6` |
| 08H-27H | Restart 1-5 |
| 30H-37H | Restart 6 |
| 38H-3AH | Restart 7 |
| 3BH-5BH | currently unused; reserved |
| 5CH-7CH | Default FCB |
| 7DH-7FH | random number (optional) |
| 80H-FFH | Default record buffer |

Of particular interest to the user here is, for example, the default FCB at `5CH`. Let's assume you call a command file (extension `COM`) by entering

```
DATEI filename.ext<ENTER>
```

then the CCP automatically sets up an FCB for the file `filename.ext` – that already takes work off your hands.

### TPA

The TPA – **Transient Program Area** – is the actual "working area" of CP/M. This is where your WordStar runs, for example. The TPA starts exactly at address `100H` and extends at most up to the `bdospage`, i.e. the CCP can be overwritten by a user program without losing the CP/M environment. The CCP (and the BDOS) are reloaded at the next warm start. A user program may under certain circumstances even overwrite the BDOS, but then it must not access a single BDOS function any more (or it crashes) – this seems to be rather a special case, though, that hardly ever occurs in practice.

### CCP

The CCP – **Console Command Processor** – is, so to speak, your "contact person" when you work with CP/M. The CCP is able to carry out commands that you enter following a strict syntax. Besides its most important ability, namely loading programs into the TPA and starting them there, the CCP also contains so-called resident commands such as `DIR`, `SAVE`, `TYPE` or `REN`. It is precisely the strict command syntax – in plain English, the low level of user comfort – that kept CP/M something for "specialists" for a long time and prevented it from reaching the popularity of BASIC operating systems. But you too will see that CP/M, once a minimum of understanding has been reached, is an extraordinarily elegant and versatile "tool".

### BDOS

The BDOS – **Basic Disk Operating System** – is the real heart of CP/M. As the name already suggests, its function corresponds to the DOS in the VDOS 2.0 ROM. The individual functions in the BDOS are listed in a table further below. At this point we would also like to refer you to the relevant literature – by now there are quite a few very good books on CP/M (for beginners too).

The CCP and BDOS are located on the so-called system tracks of a CP/M disk and are loaded into memory again and again during each warm start.

### BIOS

The BIOS – **Basic Input Output System** – is the link between the hardware and the BDOS. In a standard CP/M implementation the BIOS, like the BDOS and the CCP, is also located on the disk and is booted once at the cold start (bootstrap = pulling yourself out of the mud by your own hair -> Baron Münchhausen). In the CP/M implementations on the CPCs the BIOS was moved into a ROM (VDOS or AMSDOS) for reasons of efficiency, because only in this way can the DOS access the floppy in a simple manner. The BIOS is also a program library, which, roughly speaking, falls into two logical groups:

- Non-disk input output
- Disk input output

The first group enables CP/M to communicate with the outside world – which in this case is you – while the second group manages your data.

### The RAM Under CP/M

Since the non-relocatable RAM area is used largely by the BIOS, it is used in the same way under CP/M as well. In addition, CP/M uses the following variables (all addresses hexadecimal):

| Address | Length | Meaning |
|---------|-------|-----------|
| ACF8 | 23 | ALV 0 |
| AD0F | 23 | ALV 1 |
| AD26 | 128 | Directory buffer |
| ADA6 | 512 | Host buffer |
| AFA6 | 16 | DPH 0 |
| AFB6 | 16 | DPH 1 |
| AFC6 | 39 | CSV 0 |
| AFED | 39 | CSV 1 |
| B014 | 25 | DPB 0 |
| B02D | 25 | DPB 1 |
| B046 | 3 | Bios entry handler |
| B049 | 2 | Original interrupt entry |
| B04B | 2 | Gate Array status |
| B04D | 1 | Cursor flag |
| B04E | 1 | Console buffer flag |
| B04F | 2 | Console buffer pointer |
| B051 | 1 | Console buffer counter |
| B052 | 128 | Console buffer |
| B0D2 | 2 | Temporary storage for the stack |

### Structure of the Disk Parameter Block (DPB)

The Disk Parameter Block of a vortex floppy consists of two parts: the standard CP/M part and a VDOS-specific extension. Meaning of the individual entries (structure of the table: default value, number of bytes, short name, explanation; all values decimal):

**Standard part:**

| Default | Bytes | Short name | Explanation |
|---------|-------|-----------------|-----------|
| 36 | 2 | SPT | Number of records per track |
| 5  | 1 | BSH | Block shift factor |
| 31 | 1 | BLM | Block mask |
| 3  | 1 | EXM | Extent mask |
| 176 | 2 | DSM | Total number of blocks-1 |
| 127 | 2 | DRM | Total number of directory entries-1 |
| 128 | 2 | AL0,1 | first two bytes of the ALV |
| 32 | 2 | CKS | Length of the CSV |
| 2  | 2 | OFF | Number of system tracks |

**vortex-specific extension:**

| Default | Bytes | Short name | Explanation |
|---------|-------|-----------------|-----------|
| 1   | 1 | MASK | Sector mask = number of the 1st sector |
| 9   | 1 | ST   | Number of physical sectors per track |
| 42  | 1 | GP0  | Length of GAP0 (write/read) |
| 82  | 1 | GP1  | Length of GAP1 (format) |
| 229 | 1 | FILL | Filler byte for the format command |
| 2   | 1 | N    | Bytes/sector (-> 512) |
| 4   | 1 | BLK  | Blocking factor; 4 records per sector |
| 79  | 1 | ATRK | current physical track number |
| 79  | 1 | MTRK | max. number of tracks per side -1 |
| 1   | 1 | FLAG | Flag byte |

**Meaning of the individual bits in the flag byte:**

| Bit | Function |
|-----|----------|
| *flag of drive A only* | |
| 1 | Boot flag: 0 = boot message on, 1 = boot message off |
| 2 | not used (under VDOS 1.0: message flag) |
| 3 | Motor flag: 0 = motor off, 1 = motor on |
| *both drives* | |
| 0 | Number of heads -1 |
| 4 | Multi sector flag: 0 = single sector I/O, 1 = multi sector I/O |
| 5 | Drive type: 0 = 5.25"/3.5", 1 = 3" |
| 6 | Recalibrate flag: 0 = recalibrate the head carriage before the next positioning, 1 = no recalibrate |

### Structure of the Disk Parameter Header (DPH)

(Layout of the table: default value, number of bytes, explanation; all values decimal)

| Default | Bytes | Explanation |
|---------|-------|-----------|
| 0 | 2 | Work variable (address of the sector translation) |
| 0 | 2 | "-" |
| 0 | 2 | "-" |
| 0 | 2 | "-" |
| DIRBUFF | 2 | Address of the directory buffer |
| DPB | 2 | Address of the Disk Parameter Block |
| CSV | 2 | Address of the Check Size Vector |
| ALV | 2 | Address of the Allocation Vector |

### Layout of a File Control Block (FCB)

CP/M – or rather its BDOS – can only access files if a so-called File Control Block, FCB for short, has been assigned to them beforehand. The FCB contains all the information about the file that the BDOS needs to access it unambiguously. The standard FCB is 33 bytes long, the random FCB 36 bytes.

Here now is the meaning of the individual bytes in order (first column = short name, second column = length in bytes/decimal, third column explanation):

| Short name | Length | Explanation |
|----------|-------|-----------|
| DR | 1 | Drive code. 0 = default drive, 1-16 = autoselect drive A-P |
| FN | 8 | File name |
| EXT | 3 | Extension |
| EX | 1 | Number of the current extent |
| S1,S2 | 2 | internal variable |
| RC | 1 | Record counter within the current extent |
| ALLT | 16 | Block allocation table (loaded by the BDOS) |
| CR | 1 | current record number for the write/read operation |
| R0,R1,R2 | 3 | Random record number (optional) |

### The Allocation Vector

The ALV – Allocation Vector (allocation table) – plays a central role in the disk management of CP/M-like operating systems. Its structure is very simple:

```
Byte 0   | Byte 1   | Byte 2   ...........

Bit:    76543210   76543210   76543210
```

Each bit stands for one block on the disk (counting starts at 0). If a block is in use, the corresponding bit is set. The DOS must keep the ALV up to date at all times, as otherwise data will be stored wrongly on the disk. If you insert a new disk and log it in with `^C`, the DOS has the ALV built anew. Whether a disk has been changed is determined by the DOS with the help of the so-called CSV.

The length of the ALV is essentially the total number of blocks divided by 8.

### The Check Size Vector

The CSV – Check Size Vector – has the sole task of telling the DOS whether a disk has been changed. This works as follows: the DOS computes a one-byte checksum over each directory record (128 bytes; 4 entries of 32 bytes each) and stores these check bytes in order in the CSV. The CSV is updated continuously while you work with the disk. A `^C` forces the CSV to be built anew. If a disk is now changed without logging it in (`^C`), the DOS detects this in 99.9% of all cases from a mismatch in the CSV. It could, however, quite possibly happen that two directory records with different contents have the same checksum. That is a risk you have to/can live with.

You get the length of the CSV by dividing the total number of directory entries by 4.

### The BIOS Jump Vector

The BIOS jump vector has the structure shown below. You can find the BIOS vector under CP/M as follows: start a debugger, e.g. `DDT`, and look at which address is stored in memory location 1. There you will find the address `wboot` of the warm start routine in the jump vector.

Entries into the BIOS vector for non-disk I/O devices (e.g. console, list, …) are mostly harmless and at worst lead to a crash if you do something wrong. Jumps to disk routines can do a great deal more mischief. So: always take your disk out first and put in a "worthless" disk.

```
wboot:
JP BOOT      ; CP/M Kaltstart
JP WBOOT     ; CP/M Warmstart
JP CONST     ; teste Consolstatus
JP CONIN     ; hole Zeichen von der console
JP CONOUT    ; sende Zeichen zur Console
JP LIST      ; sende Zeichen zum Drucker
JP PUNCH     ; sende Zeichen zum Puncher
JP READER    ; hole Zeichen vom Reader
JP HOME      ; setze Kopfschlitten auf Spur 0
JP SELDSK    ; selektiere Laufwerk
JP SETTRK    ; setze Spurnummer
JP SETSEC    ; setze Recordnummer
JP SETDMA    ; setze DMA (=Recordpuffer) Adresse
JP READ      ; lese Record
JP WRITE     ; schreibe Record
JP LISTST    ; teste Druckerstatus
JP SECTRAN   ; übersetze Recordnummer
```

| Routine | Entry | Exit |
|---------|-----------|-----------|
| CONST   | — | A=FF character ready; A=00 no character ready |
| CONIN   | — | A = character read |
| CONOUT  | C = character | — |
| LIST    | C = character | — |
| PUNCH   | C = character | — |
| READER  | — | A = character (=1AH if EOF) |
| HOME    | — | — |
| SELDSK  | C = drive | HL = DPH address; HL = 0 drive not present |
| SETTRK  | BC = track number | — |
| SETSEC  | BC = record number | — |
| SETDMA  | BC = DMA address | — |
| READ    | — | A=0 all OK, otherwise error |
| WRITE   | C = write mode | A=0 all OK, otherwise error |
| LISTST  | — | A=0 printer not ready; A=FF printer ready |
| SECTRAN | BC = record number, DE = transtable | HL = translated record number |

### BDOS Entries

As we already know, the BDOS is an essential part of the CP/M operating system. The BDOS is really just a program library. If you want to write machine code programs under CP/M yourself, you can make use of the BDOS functions – and the nice thing is: calling a BDOS function is system-independent, i.e. if you now write a CP/M program on your CPC that works strictly with BDOS functions, it will (apart perhaps from a video adaptation) also run immediately and without restriction on, say, a KAYPRO – the BDOS entry at `5` is simply a standardized interface too.

The number of the BDOS function must be passed in the `C` register when calling.

#### BDOS Functions

| No. | Function | Entry | Exit |
|-----|----------|-----------|-----------|
| 0  | System Reset | - | - |
| 1  | Console Input | - | A = char |
| 2  | Console Output | E = char | - |
| 3  | Reader Input | - | A = char |
| 4  | Punch Output | E = char | - |
| 5  | List Output | E = char | - |
| 6  | Direct Console I/O | E = FF (input) / E = FE (status) / E = char (output) | - |
| 7  | Get I/O Byte | - | A = I/O Byte |
| 8  | Set I/O Byte | E = I/O Byte | - |
| 9  | Print String | DE = pointer | - |
| 10 | Read Console Buffer | DE = pointer | chars in buffer |
| 11 | Get Console Status | - | A = 00/non zero |
| 12 | Return Version | - | HL = Version |
| 13 | Reset Disk System | - | - |
| 14 | Select Disk | E = disk number | - |
| 15 | Open File | DE = fcb | A = FF not found |
| 16 | Close File | DE = fcb | A = FF not found |
| 17 | Search for first | DE = fcb | A = Dir code |
| 18 | Search for next | - | A = Dir code |
| 19 | Delete File | DE = fcb | A = FF not found |
| 20 | Read Sequential | DE = fcb | A = error code |
| 21 | Write Sequential | DE = fcb | A = error code |
| 22 | Make File | DE = fcb | A = FF no space |
| 23 | Rename File | DE = fcb | A = FF not found |
| 24 | Return Login Vector | - | HL = Vector |
| 25 | Return Current Disk | - | A = disk number |
| 26 | Set DMA Address | DE = DMA address | - |
| 27 | Get ALLC Address | - | HL = address |
| 28 | Write Protect Disk | - | - |
| 29 | Get R/O Vector | - | HL = Vector |
| 30 | Set File Attributes | DE = fcb | A = FF not found |
| 31 | Get DPB Address | - | HL = address |
| 32 | Set/Get User Code | E = FF (GET) / E = 0..F (SET) | A = user code / - |
| 33 | Read Random | DE = fcb | A = error code |
| 34 | Write Random | DE = fcb | A = error code |
| 35 | Compute File Size | DE = fcb | r0,r1,r2 |
| 36 | Set Random Record | DE = fcb | r0,r1,r2 |
| 37 | Reset Drive | DE = drive vector | A = 0 |
| 38 | Access Drive | not supported | A = 0 |
| 39 | Free Drive | not supported | - |
| 40 | Write Random + Fill | DE = fcb | A = error code |

For more detailed information, please consult the relevant literature.

---

## Finally, a Few Words About the Hardware

### X Drives

The hardware of the X drives consists merely of a ROM module with an RS232C (optional) interface. The ROM number can be set freely (two-row 16-pin header). The ROM socket can take both 16 KB and 32 KB ROMs. The latter are handled as two ROMs of 16 KB each -> own ROM number.

The control ports of the serial interface:

| Port | Function |
|------|----------|
| FADC | SIO data |
| FADD | SIO control |
| FBDC | Counter 0 |
| FBDD | Counter 1 |
| FBDF | Mode word |

### Drives + Controller

Drives with their own controller occupy by default the ports:

**CPC 464:**

| Port | Function |
|------|----------|
| FB7E | µPD control |
| FB7F | µPD data |
| FA7E | Motor |

**CPC 664 / 6128:**

| Port | Function |
|------|----------|
| FBF6 | µPD control |
| FBF7 | µPD data |
| FA7E | Motor |

for drive control.

With the controller with integrated ROM module/EPROM programmer, the port addresses can be set freely via a decoder ROM.

---

## Pin Assignment of the Connectors

### Floppy Disk Interface Connector(s) on the Controller

#### 5.25" Connector

| Pin | Signal |
|-----|--------|
| 6   | /DS3 |
| 8   | /INDEX |
| 10  | /DS0 |
| 12  | /DS1 |
| 14  | /DS2 |
| 16  | /MOTOR |
| 18  | /DIRECTION |
| 20  | /STEP |
| 22  | /WRDATA |
| 24  | /WRGATE |
| 26  | /TRACK 00 |
| 28  | /WRPROT |
| 30  | /RDATA |
| 32  | /SIDE |
| 34  | /READY |

Power supply:

- Pin 1: +12V (input) or ground
- Pin 3, 5, 7: +5V (input)
- all other odd pins: ground

#### 3" Connector

| Pin | Signal |
|-----|--------|
| 27 | /INDEX |
| 25 | /DS0 |
| 23 | /DS1 |
| 19 | /MOTOR |
| 17 | /DIRECTION |
| 15 | /STEP |
| 13 | /WRDATA |
| 11 | /WRGATE |
| 9  | /TRACK 00 |
| 7  | /WRPROT |
| 5  | /RDATA |
| 3  | /SIDE |
| 1  | /READY |

Power supply:

- Pin 21, 29, 31, 33: +5V (input)
- all even pins: ground

### RS 232C Connector

As a rule, all vortex RS 232C interfaces have a 25-pin "male" DTE connector.

| Pin | Signal |
|-----|--------|
| 2  | /TxD |
| 3  | /RxD |
| 4  | RTS |
| 5  | CTS |
| 7  | Ground |
| 8  | DCD |
| 20 | DTR |
| 22 | R. IN |

### DIN Socket on the X Drive

(socket seen from the rear)

```
      3
      •
  2 •   • 4
  1 •   • 5
```

| Pin | Function |
|-----|----------|
| 1, 2 | +5V (only 1 on a three-pin socket) |
| 4, 5 | +12V (only 5 on a three-pin socket) |
| 3 | Ground |

Both the controller with RS interface and the X/RS board also have a DIN socket; there the pin assignment is exactly the other way round:

| Pin | Function |
|-----|----------|
| 1, 2 | +12V |
| 4, 5 | +5V |
| 3 | Ground |

### Power Supply of the vortex Floppy Controller (Not X Drives)

The floppy controller receives +5V via the socket strip B3 in the drive housing (i.e. via a 34-wire ribbon cable).

![Power Connector](power_connector.png)

Power supply at the card connectors:

- Pin 3, 5, 7: +5V
- all other odd pins: ground

The labeling applies when looking into the opening of the socket strip. The socket strip sits about 12 cm away from the 2 (1) card connectors that are plugged onto the drives.

### Drives

The drive connected to the vortex controller meets the following specifications:

| Parameter | Value |
|-----------|------|
| Capacity (unformatted) | 1 MB |
| Data transfer rate    | 250K bits/sec |
| Track-to-track time          | min. 4 msec |
| Head settling time      | max. 20 msec |
| Motor start-up time         | max. 1 sec |
| Rotational speed                 | 300 rpm |
| Number of heads             | 2 |
| Tracks/surface        | min. 80 |
| Modulation               | FM/MFM |
| Track density               | 96 tpi |

> *All rights to changes reserved.*

---

## Index

> **(!) Note:** In this edition the page numbers of the printed original are replaced by links to the sections. For each entry the (at most four) most important sections are listed; use the search function to find all other places.

### A

- `|A` – [The VDOS Command |FORMAT](#the-vdos-command-format), [The VDOS Commands |A and |B](#the-vdos-commands-a-and-b), [The VDOS Command |X](#the-vdos-command-x)
- Accumulator – [DOS – Disk Operating System](#dos--disk-operating-system), [Function 128: `CAS IN CHAR` – Entry `BC80H`](#function-128-cas-in-char--entry-bc80h), [Function 135: `CAS OUT CHAR` – Entry `BC95H`](#function-135-cas-out-char--entry-bc95h), [CP/M](#cpm)
- ALV (allocation vector) – [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [The RAM Under CP/M](#the-ram-under-cpm), [Structure of the Disk Parameter Header (DPH)](#structure-of-the-disk-parameter-header-dph), [The Allocation Vector](#the-allocation-vector)
- AMSDOS – [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [What Is That, a DOS?](#what-is-that-a-dos), [The VDOS Command |AMSDOS](#the-vdos-command-amsdos), [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom)
- `|AMSDOS` – [The VDOS Command |AMSDOS](#the-vdos-command-amsdos), [The VDOS Command |ROMOFF](#the-vdos-command-romoff), [Further Notes (Not Bugs)](#further-notes-not-bugs)
- `|ATTRIBUT` – [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut), [|ATTRIBUT and |FORMAT](#attribut-and-format), [9. `|ATTRIBUT` with a Wildcard Changes Only the First Matching File](#9-attribut-with-a-wildcard-changes-only-the-first-matching-file), [10. `|ATTRIBUT` with an Empty Name](#10-attribut-with-an-empty-name)
- Autostart string – [The VDOS Turnkey Function](#the-vdos-turnkey-function), [4 – Copying the Parameter Sector](#4--copying-the-parameter-sector), [Example: Autostart String](#example-autostart-string), [Special Application: Changing the Screen Colors](#special-application-changing-the-screen-colors)

### B

- `|B` – [The VDOS Command |FORMAT](#the-vdos-command-format), [The VDOS Commands |A and |B](#the-vdos-commands-a-and-b), [The VDOS Command |X](#the-vdos-command-x), [The VDOS Command |ERA](#the-vdos-command-era)
- BAK – [What Is a File, Anyway?](#what-is-a-file-anyway), [The VDOS Commands |A and |B](#the-vdos-commands-a-and-b), [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut)
- BDOS – [TPA](#tpa), [BDOS](#bdos), [BDOS Entries](#bdos-entries), [BDOS Functions](#bdos-functions)
- BIOS – [BIOS – Basic Input Output System](#bios--basic-input-output-system), [RAM Variables of BIOS and DOS](#ram-variables-of-bios-and-dos), [BIOS](#bios), [The BIOS Jump Vector](#the-bios-jump-vector)
- BIOS jump vector – [BIOS – Basic Input Output System](#bios--basic-input-output-system), [DOS – Disk Operating System](#dos--disk-operating-system), [Function 137: `CAS CATALOG` – Entry `BC9BH`](#function-137-cas-catalog--entry-bc9bh), [The BIOS Jump Vector](#the-bios-jump-vector)
- Block – [Error Codes and What They Mean](#error-codes-and-what-they-mean), [DOS – Disk Operating System](#dos--disk-operating-system), [Structure of the Disk Parameter Block (DPB)](#structure-of-the-disk-parameter-block-dpb), [Layout of a File Control Block (FCB)](#layout-of-a-file-control-block-fcb)
- Block allocation table – [Error Codes and What They Mean](#error-codes-and-what-they-mean), [DOS – Disk Operating System](#dos--disk-operating-system), [Layout of a File Control Block (FCB)](#layout-of-a-file-control-block-fcb), [6. Up to 2K Too Much Free Space](#6-up-to-2k-too-much-free-space)
- Blocking/deblocking – [BIOS – Basic Input Output System](#bios--basic-input-output-system), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Structure of the Disk Parameter Block (DPB)](#structure-of-the-disk-parameter-block-dpb)
- Boot sector – [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only), [3 – Copying the CP/M System](#3--copying-the-cpm-system), [`keine CP/M Diskette – Wiederholen J/N`](#keine-cpm-diskette--wiederholen-jn)
- BOOTGEN – [The VDOS Command |FORMAT](#the-vdos-command-format)
- BOS – [The VDOS Command |ROMOFF](#the-vdos-command-romoff)
- Breakpoint – [The VDOS Command |XMON – The vortex Z80 Monitor](#the-vdos-command-xmon--the-vortex-z80-monitor), [`B<ENTER>` – View/Change Breakpoints](#benter--viewchange-breakpoints), [`Y` – Selecting the Upper ROM](#y--selecting-the-upper-rom), [Variables of the Monitor](#variables-of-the-monitor)
- Byte sequence – [`C` – Searching for Byte Sequences](#c--searching-for-byte-sequences)

### C

- `|CAS` – [The VDOS Command |CAS](#the-vdos-command-cas), [The VDOS Command |CAS.OUT](#the-vdos-command-casout), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling)
- CAS CATALOG – [Function 137: `CAS CATALOG` – Entry `BC9BH`](#function-137-cas-catalog--entry-bc9bh)
- CAS IN ABANDON – [Function 127: `CAS IN ABANDON` – Entry `BC7DH`](#function-127-cas-in-abandon--entry-bc7dh)
- CAS IN CHAR – [Function 128: `CAS IN CHAR` – Entry `BC80H`](#function-128-cas-in-char--entry-bc80h), [Function 130: `CAS RETURN` – Entry `BC86H`](#function-130-cas-return--entry-bc86h)
- CAS IN CLOSE – [Function 126: `CAS IN CLOSE` – Entry `BC7AH`](#function-126-cas-in-close--entry-bc7ah)
- CAS IN DIRECT – [Function 129: `CAS IN DIRECT` – Entry `BC83H`](#function-129-cas-in-direct--entry-bc83h)
- CAS IN OPEN – [Function 125: `CAS IN OPEN` – Entry `BC77H`](#function-125-cas-in-open--entry-bc77h)
- CAS OUT ABANDON – [Function 134: `CAS OUT ABANDON` – Entry `BC92H`](#function-134-cas-out-abandon--entry-bc92h)
- CAS OUT CHAR – [Function 135: `CAS OUT CHAR` – Entry `BC95H`](#function-135-cas-out-char--entry-bc95h)
- CAS OUT CLOSE – [Function 133: `CAS OUT CLOSE` – Entry `BC8FH`](#function-133-cas-out-close--entry-bc8fh)
- CAS OUT DIRECT – [Function 136: `CAS OUT DIRECT` – Entry `BC98H`](#function-136-cas-out-direct--entry-bc98h)
- CAS OUT OPEN – [Function 132: `CAS OUT OPEN` – Entry `BC8CH`](#function-132-cas-out-open--entry-bc8ch)
- CAS RETURN – [Function 130: `CAS RETURN` – Entry `BC86H`](#function-130-cas-return--entry-bc86h)
- CAS TEST EOF – [Function 131: `CAS TEST EOF` – Entry `BC89H`](#function-131-cas-test-eof--entry-bc89h)
- `|CAS.IN` – [The VDOS Command |CAS.IN](#the-vdos-command-casin), [The VDOS Command |CAS.OUT](#the-vdos-command-casout), [`Idateiname.dateityp<ENTER>` – Loading a Binary File from Disk/Cassette](#idateinamedateitypenter--loading-a-binary-file-from-diskcassette)
- `|CAS.OUT` – [The VDOS Command |CAS.OUT](#the-vdos-command-casout)
- CASCOPY – [The CP/M Command CASCOPY](#the-cpm-command-cascopy), [`Die Directory ist voll!`](#die-directory-ist-voll), [`Geschützte Datei! Kann nicht gelesen werden.`](#geschützte-datei-kann-nicht-gelesen-werden), [`Fehler! CASCOPY wird abgebrochen`](#fehler-cascopy-wird-abgebrochen)
- Cassette recorder – [Cassette Recorder on the CPC](#cassette-recorder-on-the-cpc), [The VDOS Command |CAS](#the-vdos-command-cas), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The CP/M Command CASCOPY](#the-cpm-command-cascopy)
- CAT – [The VDOS Command |X](#the-vdos-command-x), [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut), [CAT and |DIR](#cat-and-dir)
- CCP – [CP/M Under the Magnifying Glass – The CP/M Operating System](#cpm-under-the-magnifying-glass--the-cpm-operating-system), [Zero Page](#zero-page), [TPA](#tpa), [CCP](#ccp)
- Centronics – [DOS – Disk Operating System](#dos--disk-operating-system)
- Channel – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The VDOS Command |FILES](#the-vdos-command-files), [3. Channel Number 128 or Above in `|FILES`: Wrong Message](#3-channel-number-128-or-above-in-files-wrong-message), [12. Both SIO Channels Use One Shared Copy of Register 5](#12-both-sio-channels-use-one-shared-copy-of-register-5)
- `|CLOSE` – [The VDOS Command |RESET](#the-vdos-command-reset), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The VDOS Command |CLOSE](#the-vdos-command-close), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- CLOSEIN – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Two Small Applications](#two-small-applications), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- CLOSEOUT – [The VDOS Command |RESET](#the-vdos-command-reset), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Two Small Applications](#two-small-applications), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- `|CODE` – [The VDOS Command |CODE](#the-vdos-command-code), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom)
- CP/M 2.2 – [Preface](#preface), [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only)
- CP/M plus – [Preface](#preface), [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only), [A Few More Notes](#a-few-more-notes)
- `|CPM` – [The VDOS Turnkey Function](#the-vdos-turnkey-function), [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only), [The VDOS Command |CPM](#the-vdos-command-cpm)
- `|CPM,1` – [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only), [The VDOS Command |CPM,1](#the-vdos-command-cpm1), [CP/M with Your vortex X Drive](#cpm-with-your-vortex-x-drive)
- `|CPM,2` – [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only), [A Few More Notes](#a-few-more-notes), [The VDOS Command |CPM,2](#the-vdos-command-cpm2)
- CRC error – [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- CSV (check size vector) – [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [The RAM Under CP/M](#the-ram-under-cpm), [Structure of the Disk Parameter Header (DPH)](#structure-of-the-disk-parameter-header-dph), [The Check Size Vector](#the-check-size-vector)
- CTRL+C – [Example: Keyboard Layout](#example-keyboard-layout), [Example: Autostart String](#example-autostart-string), [`SYSGEN wurde durch ^C abgebrochen`](#sysgen-wurde-durch-c-abgebrochen), [The Check Size Vector](#the-check-size-vector)

### D

- DATA-only format – [The VDOS Command |FORMAT](#the-vdos-command-format), [1 – Formatting a Disk](#1--formatting-a-disk), [`Diskette hat keine reservierten Systemspuren`](#diskette-hat-keine-reservierten-systemspuren)
- `|DERROR` – [Ways of Trapping Disk Errors](#ways-of-trapping-disk-errors), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [Appendix: The EOF Problem](#appendix-the-eof-problem)
- `|DIR` – [How Do We Type the Vertical Bar?](#how-do-we-type-the-vertical-bar), [The VDOS Commands |A and |B](#the-vdos-commands-a-and-b), [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [CAT and |DIR](#cat-and-dir)
- Directory – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [`Die Directory ist voll!`](#die-directory-ist-voll), [DOS – Disk Operating System](#dos--disk-operating-system)
- `|DISC` – [The VDOS Command |DISC](#the-vdos-command-disc), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling)
- `|DISC.IN` – [The VDOS Command |DISC.IN](#the-vdos-command-discin), [The VDOS Command |CAS.OUT](#the-vdos-command-casout)
- `|DISC.OUT` – [The VDOS Command |DISC.OUT](#the-vdos-command-discout)
- Disk error – [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [Ways of Trapping Disk Errors](#ways-of-trapping-disk-errors), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- Disk monitor – [The VDOS Command |XMON – The vortex Z80 Monitor](#the-vdos-command-xmon--the-vortex-z80-monitor), [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [Variables of the Disk Monitor](#variables-of-the-disk-monitor), [25. @ (Disk Monitor): T and G Keep an Invalid Position](#25--disk-monitor-t-and-g-keep-an-invalid-position)
- DISKTOOL – [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [The CP/M Command DISKTOOL](#the-cpm-command-disktool), [1 – Formatting a Disk](#1--formatting-a-disk), [`DISKTOOL 1.0 benoetigt unter dem RAM-Karten CP/M aktive System-Vektoren !`](#disktool-10-benoetigt-unter-dem-ram-karten-cpm-aktive-system-vektoren-)
- DOS indirections – [BASIC](#basic), [Variables of the Monitor](#variables-of-the-monitor)
- DPB (disk parameter block) – [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [The RAM Under CP/M](#the-ram-under-cpm), [Structure of the Disk Parameter Block (DPB)](#structure-of-the-disk-parameter-block-dpb), [Structure of the Disk Parameter Header (DPH)](#structure-of-the-disk-parameter-header-dph)
- DPH (disk parameter header) – [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [The RAM Under CP/M](#the-ram-under-cpm), [Structure of the Disk Parameter Header (DPH)](#structure-of-the-disk-parameter-header-dph)
- `|DRIVE` – [The VDOS Command |SELECT](#the-vdos-command-select)

### E

- EOF – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Function 131: `CAS TEST EOF` – Entry `BC89H`](#function-131-cas-test-eof--entry-bc89h), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Appendix: The EOF Problem](#appendix-the-eof-problem)
- EOF problem – [Error Codes and What They Mean](#error-codes-and-what-they-mean), [Appendix: The EOF Problem](#appendix-the-eof-problem), [8. ASCII Files: The Rest of the Last Record Is Not Filled with `1AH`](#8-ascii-files-the-rest-of-the-last-record-is-not-filled-with-1ah)
- `|ERA` – [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut), [The VDOS Command |ERA](#the-vdos-command-era), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [24. O: `<ESC>` During Address Entry Leaves the File Open](#24-o-esc-during-address-entry-leaves-the-file-open)
- Error code – [Ways of Trapping Disk Errors](#ways-of-trapping-disk-errors), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [BDOS Functions](#bdos-functions), [1. `|GET` Never Reports "Record leer" (Error 55)](#1-get-never-reports-record-leer-error-55)
- Error message – [Ways of Trapping Disk Errors](#ways-of-trapping-disk-errors), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [CP/M Error Messages and How to Fix Them](#cpm-error-messages-and-how-to-fix-them), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom)
- Error patch – [BASIC](#basic), [5. Direct Strings in `|PUT` Exhaust BASIC's String Management](#5-direct-strings-in-put-exhaust-basics-string-management)
- Extension – [What Is That, a DOS?](#what-is-that-a-dos), [What Is a File, Anyway?](#what-is-a-file-anyway), [DOS – Disk Operating System](#dos--disk-operating-system), [Structure of the Disk Parameter Block (DPB)](#structure-of-the-disk-parameter-block-dpb)
- Extent – [DOS – Disk Operating System](#dos--disk-operating-system), [RAM Variables of BIOS and DOS](#ram-variables-of-bios-and-dos), [Structure of the Disk Parameter Block (DPB)](#structure-of-the-disk-parameter-block-dpb), [Layout of a File Control Block (FCB)](#layout-of-a-file-control-block-fcb)

### F

- F1-X / M1-X – see X drive
- `|FAST` – [The VDOS Commands |FAST, |SLOW and |FRAME](#the-vdos-commands-fast-slow-and-frame), [VDOS and CP/M Internals](#vdos-and-cpm-internals)
- FAST (CP/M command) – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut), [The VDOS Commands |FAST, |SLOW and |FRAME](#the-vdos-commands-fast-slow-and-frame), [The CP/M Command FAST](#the-cpm-command-fast)
- FCB (file control block) – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [Zero Page](#zero-page), [Layout of a File Control Block (FCB)](#layout-of-a-file-control-block-fcb)
- FDC – [Ways of Trapping Disk Errors](#ways-of-trapping-disk-errors), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- `|FIELD` – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The VDOS Command |FIELD](#the-vdos-command-field), [The VDOS Command |GET](#the-vdos-command-get), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- File – [What Is a File, Anyway?](#what-is-a-file-anyway), [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [DOS – Disk Operating System](#dos--disk-operating-system)
- File name – [What Is a File, Anyway?](#what-is-a-file-anyway), [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |REN](#the-vdos-command-ren), [The CP/M Command FILECOPY](#the-cpm-command-filecopy)
- File type – [What Is a File, Anyway?](#what-is-a-file-anyway), [`Idateiname.dateityp<ENTER>` – Loading a Binary File from Disk/Cassette](#idateinamedateitypenter--loading-a-binary-file-from-diskcassette), [The CP/M Command FILECOPY](#the-cpm-command-filecopy), [The CP/M Command CASCOPY](#the-cpm-command-cascopy)
- FILECOPY – [The CP/M Command FILECOPY](#the-cpm-command-filecopy), [Example](#example), [The CP/M Command DISKTOOL](#the-cpm-command-disktool), [`FILECOPY 3.0 benoetigt unter dem RAM-Karten CP/M aktive System-Vektoren !`](#filecopy-30-benoetigt-unter-dem-ram-karten-cpm-aktive-system-vektoren-)
- `|FILES` – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The VDOS Command |FILES](#the-vdos-command-files), [2. `|FILES` with a Maximum Record Length of 0 Is Accepted](#2-files-with-a-maximum-record-length-of-0-is-accepted), [3. Channel Number 128 or Above in `|FILES`: Wrong Message](#3-channel-number-128-or-above-in-files-wrong-message)
- Firmware ROM – [`X` – Firmware ROM On/Off](#x--firmware-rom-onoff), [Variables of the Disk Monitor](#variables-of-the-disk-monitor)
- `|FORMAT` – [The VDOS Command |FORMAT](#the-vdos-command-format), [Running and Saving a BASIC Program](#running-and-saving-a-basic-program), [|ATTRIBUT and |FORMAT](#attribut-and-format), [11. `|FORMAT` Checks Only the Low Byte](#11-format-checks-only-the-low-byte)
- Formatting – [The VDOS Command |FORMAT](#the-vdos-command-format), [1 – Formatting a Disk](#1--formatting-a-disk), [|ATTRIBUT and |FORMAT](#attribut-and-format), [11. `|FORMAT` Checks Only the Low Byte](#11-format-checks-only-the-low-byte)
- `|FRAME` – [The VDOS Commands |FAST, |SLOW and |FRAME](#the-vdos-commands-fast-slow-and-frame), [VDOS and CP/M Internals](#vdos-and-cpm-internals)

### G

- `|GET` – [The VDOS Command |FIELD](#the-vdos-command-field), [The VDOS Command |GET](#the-vdos-command-get), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [1. `|GET` Never Reports "Record leer" (Error 55)](#1-get-never-reports-record-leer-error-55)

### H

- HELLO.BAS – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut), [The VDOS Turnkey Function](#the-vdos-turnkey-function)
- HEX/ASCII – [The VDOS Command |XMON – The vortex Z80 Monitor](#the-vdos-command-xmon--the-vortex-z80-monitor), [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [`Dadresse1,adresse2<ENTER>` – Listing in HEX/ASCII Form](#dadresse1adresse2enter--listing-in-hexascii-form)
- HIMEM – [The VDOS Command |ROMCAT](#the-vdos-command-romcat), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Random-Access File Management](#random-access-file-management)
- Host buffer – [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [The RAM Under CP/M](#the-ram-under-cpm)

### I

- I/O byte – [Example: Changing the Floppy Disk Timing Constants](#example-changing-the-floppy-disk-timing-constants), [Example: Keyboard Layout](#example-keyboard-layout), [Example: Autostart String](#example-autostart-string), [BDOS Functions](#bdos-functions)
- Input channel – [Cassette Recorder on the CPC](#cassette-recorder-on-the-cpc), [The VDOS Command |DISC.IN](#the-vdos-command-discin), [The VDOS Command |CAS.IN](#the-vdos-command-casin), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling)
- INPUT#9 – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Two Small Applications](#two-small-applications)
- INSTALL – [Example](#example), [The CP/M Command INSTALL](#the-cpm-command-install), [Example: Keyboard Layout](#example-keyboard-layout), [`INSTALL wird abgebrochen, da Parametersector nicht lesbar!`](#install-wird-abgebrochen-da-parametersector-nicht-lesbar)

### K

- KM DISARM BREAK – [BASIC](#basic)
- Known bugs – [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [The VDOS Command |GET](#the-vdos-command-get), [The VDOS Command |PUT](#the-vdos-command-put), [Known Bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x)

### O

- `|OPEN` – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The VDOS Command |OPEN](#the-vdos-command-open), [The VDOS Command |GET](#the-vdos-command-get), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- Operating system – [VDOS – Vortex Disk Operating System](#vdos--vortex-disk-operating-system), [Loading the CP/M Operating System](#loading-the-cpm-operating-system), [DOS – Disk Operating System](#dos--disk-operating-system), [CP/M Under the Magnifying Glass – The CP/M Operating System](#cpm-under-the-magnifying-glass--the-cpm-operating-system)
- Output channel – [Cassette Recorder on the CPC](#cassette-recorder-on-the-cpc), [The VDOS Command |DISC](#the-vdos-command-disc), [The VDOS Command |CAS](#the-vdos-command-cas), [The VDOS Command |DISC.OUT](#the-vdos-command-discout)

### P

- `|PUT` – [The VDOS Command |FIELD](#the-vdos-command-field), [The VDOS Command |PUT](#the-vdos-command-put), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [5. Direct Strings in `|PUT` Exhaust BASIC's String Management](#5-direct-strings-in-put-exhaust-basics-string-management)

### R

- RAM bank – [`Z` – Selecting the RAM Bank of the vortex RAM Expansion](#z--selecting-the-ram-bank-of-the-vortex-ram-expansion), [Variables of the Monitor](#variables-of-the-monitor)
- RAM card – [`Z` – Selecting the RAM Bank of the vortex RAM Expansion](#z--selecting-the-ram-bank-of-the-vortex-ram-expansion), [The VDOS Command |ROMOFF](#the-vdos-command-romoff), [CPC464, CPC664 with X Drive and vortex RAM Card](#cpc464-cpc664-with-x-drive-and-vortex-ram-card), [The CP/M Command XMON](#the-cpm-command-xmon)
- RAM variables – [RAM Variables of BIOS and DOS](#ram-variables-of-bios-and-dos), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Relocatable RAM Area of the VDOS 2.11-X ROM](#relocatable-ram-area-of-the-vdos-211-x-rom), [The RAM Under CP/M](#the-ram-under-cpm)
- Random-access (relative) file – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Two Small Applications](#two-small-applications), [Random-Access File Management](#random-access-file-management), [Random-Access (Relative) File Management](#random-access-relative-file-management)
- Record – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Two Small Applications](#two-small-applications), [BIOS – Basic Input Output System](#bios--basic-input-output-system), [DOS – Disk Operating System](#dos--disk-operating-system)
- Record buffer – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [The VDOS Command |FILES](#the-vdos-command-files), [The VDOS Command |FIELD](#the-vdos-command-field), [BIOS – Basic Input Output System](#bios--basic-input-output-system)
- Record leer – [The VDOS Command |GET](#the-vdos-command-get), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [1. `|GET` Never Reports "Record leer" (Error 55)](#1-get-never-reports-record-leer-error-55), [Further Notes (Not Bugs)](#further-notes-not-bugs)
- `|REN` – [The VDOS Command |REN](#the-vdos-command-ren), [Error Codes and What They Mean](#error-codes-and-what-they-mean)
- Reserved tracks – [The VDOS Command |FORMAT](#the-vdos-command-format), [1 – Formatting a Disk](#1--formatting-a-disk)
- Reset – [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [The VDOS Command |RESET](#the-vdos-command-reset), [The VDOS Turnkey Function](#the-vdos-turnkey-function), [BDOS Functions](#bdos-functions)
- `|RESET` – [The VDOS Command |RESET](#the-vdos-command-reset)
- ROM WALK – [`Y` – Selecting the Upper ROM](#y--selecting-the-upper-rom), [Function 137: `CAS CATALOG` – Entry `BC9BH`](#function-137-cas-catalog--entry-bc9bh), [RAM Variables of BIOS and DOS](#ram-variables-of-bios-and-dos), [BASIC](#basic)
- `|ROMCAT` – [`Y` – Selecting the Upper ROM](#y--selecting-the-upper-rom), [The VDOS Command |ROMCAT](#the-vdos-command-romcat), [VDOS and CP/M Internals](#vdos-and-cpm-internals)
- `|ROMOFF` – [The VDOS Command |ROMOFF](#the-vdos-command-romoff), [The VDOS Command |ROMCAT](#the-vdos-command-romcat)
- RS232C – [Preface](#preface), [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [Setting Up the CPC464+DDI-1 with X Drive](#setting-up-the-cpc464ddi-1-with-x-drive), [RS 232C Connector](#rs-232c-connector)
- RSX – [Basics](#basics), [`Y` – Selecting the Upper ROM](#y--selecting-the-upper-rom), [The VDOS Command |ROMOFF](#the-vdos-command-romoff), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom)

### S

- SAVE – [Running and Saving a BASIC Program](#running-and-saving-a-basic-program), [What Is a File, Anyway?](#what-is-a-file-anyway), [The VDOS Command |CODE](#the-vdos-command-code), [The VDOS Command |CAS.OUT](#the-vdos-command-casout)
- Sector – [The CP/M Command SYSGEN](#the-cpm-command-sysgen), [1 – Formatting a Disk](#1--formatting-a-disk), [4 – Copying the Parameter Sector](#4--copying-the-parameter-sector), [BIOS – Basic Input Output System](#bios--basic-input-output-system)
- `|SELECT` – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ERA](#the-vdos-command-era), [The VDOS Command |SELECT](#the-vdos-command-select)
- Sequential file – [What Is That, a DOS?](#what-is-that-a-dos), [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling), [Two Small Applications](#two-small-applications), [Appendix: The EOF Problem](#appendix-the-eof-problem)
- SIO – [CP/M](#cpm), [X Drives](#x-drives), [12. Both SIO Channels Use One Shared Copy of Register 5](#12-both-sio-channels-use-one-shared-copy-of-register-5)
- `|SLOW` – [The VDOS Commands |FAST, |SLOW and |FRAME](#the-vdos-commands-fast-slow-and-frame), [VDOS and CP/M Internals](#vdos-and-cpm-internals)
- Step rate – [Example: Changing the Floppy Disk Timing Constants](#example-changing-the-floppy-disk-timing-constants), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Structure of the Time Constants Area](#structure-of-the-time-constants-area)
- String variable – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling)
- SYSGEN – [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [The CP/M Command SYSGEN](#the-cpm-command-sysgen), [3 – Copying the CP/M System](#3--copying-the-cpm-system), [`SYSGEN wurde durch ^C abgebrochen`](#sysgen-wurde-durch-c-abgebrochen)
- System disk – [X Drives on the CPC464 with DDI-1, CPC664 and CPC6128](#x-drives-on-the-cpc464-with-ddi-1-cpc664-and-cpc6128), [Creating a vortex CP/M 2.2 System Disk](#creating-a-vortex-cpm-22-system-disk), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only), [The VDOS Command |CPM](#the-vdos-command-cpm)
- System format – [The VDOS Command |FORMAT](#the-vdos-command-format), [1 – Formatting a Disk](#1--formatting-a-disk)
- System tracks – [The VDOS Command |FORMAT](#the-vdos-command-format), [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [The CP/M Command SYSGEN](#the-cpm-command-sysgen), [3 – Copying the CP/M System](#3--copying-the-cpm-system)

### T

- `|TAPE` – [The VDOS Command |CAS.OUT](#the-vdos-command-casout)
- Timing constants – [The CP/M Command INSTALL](#the-cpm-command-install), [Example: Changing the Floppy Disk Timing Constants](#example-changing-the-floppy-disk-timing-constants), [CP/M](#cpm), [Structure of the Time Constants Area](#structure-of-the-time-constants-area)
- TPA – [A Few More Notes](#a-few-more-notes), [TPA](#tpa), [CCP](#ccp)
- Track – [The VDOS Command |FORMAT](#the-vdos-command-format), [`@` – Start the Disk Monitor](#--start-the-disk-monitor), [The CP/M Command SYSGEN](#the-cpm-command-sysgen), [1 – Formatting a Disk](#1--formatting-a-disk)
- Turnkey – [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [The VDOS Turnkey Function](#the-vdos-turnkey-function)

### U

- `|USER` – [The VDOS Command |SELECT](#the-vdos-command-select)
- User area – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ERA](#the-vdos-command-era), [The VDOS Command |SELECT](#the-vdos-command-select), [The CP/M Command FILECOPY](#the-cpm-command-filecopy)

### V

- Vendor format – [The VDOS Command |FORMAT](#the-vdos-command-format), [1 – Formatting a Disk](#1--formatting-a-disk)

### W

- WBOOT (warm start) – [BIOS – Basic Input Output System](#bios--basic-input-output-system), [Zero Page](#zero-page), [The BIOS Jump Vector](#the-bios-jump-vector), [13. Warm Start on a Write-Protected Disk Reports "keine CP/M Diskette"](#13-warm-start-on-a-write-protected-disk-reports-keine-cpm-diskette)
- Wildcard – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ERA](#the-vdos-command-era), [The CP/M Command FILECOPY](#the-cpm-command-filecopy), [9. `|ATTRIBUT` with a Wildcard Changes Only the First Matching File](#9-attribut-with-a-wildcard-changes-only-the-first-matching-file)
- Write protection – [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut), [The VDOS Command |ERA](#the-vdos-command-era), [Error Codes and What They Mean](#error-codes-and-what-they-mean), [13. Warm Start on a Write-Protected Disk Reports "keine CP/M Diskette"](#13-warm-start-on-a-write-protected-disk-reports-keine-cpm-diskette)
- WRITE#9 – [Random-Access (Relative) and Sequential File Handling](#random-access-relative-and-sequential-file-handling)

### X

- `|X` – [The VDOS Command |FORMAT](#the-vdos-command-format), [Running and Saving a BASIC Program](#running-and-saving-a-basic-program), [The VDOS Command |X](#the-vdos-command-x), [The VDOS Command |CPM,2](#the-vdos-command-cpm2)
- X drive – [vortex X Drives at a Glance](#vortex-x-drives-at-a-glance), [Setting Up the CPC464+DDI-1 with X Drive](#setting-up-the-cpc464ddi-1-with-x-drive), [Setting Up the CPC664/CPC6128 with X Drive](#setting-up-the-cpc664cpc6128-with-x-drive), [X Drives on the CPC464 with DDI-1, CPC664 and CPC6128](#x-drives-on-the-cpc464-with-ddi-1-cpc664-and-cpc6128)
- `|XMON` – [The VDOS Command |XMON – The vortex Z80 Monitor](#the-vdos-command-xmon--the-vortex-z80-monitor), [`X` – Firmware ROM On/Off](#x--firmware-rom-onoff), [VDOS and CP/M Internals](#vdos-and-cpm-internals)
- XMON (CP/M command) – [`Idateiname.dateityp<ENTER>` – Loading a Binary File from Disk/Cassette](#idateinamedateitypenter--loading-a-binary-file-from-diskcassette), [The CP/M Command XMON](#the-cpm-command-xmon), [The Monitor XMON](#the-monitor-xmon), [Further Notes (Not Bugs)](#further-notes-not-bugs)
- XPATCH30 – [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only)

### Z

- Z80 – [Preface](#preface), [Important Notes](#important-notes), [What Is That, a DOS?](#what-is-that-a-dos), [The VDOS Command |XMON – The vortex Z80 Monitor](#the-vdos-command-xmon--the-vortex-z80-monitor)
- Zero page – [Zero Page](#zero-page)

### Special Characters / Numbers

- `$OSC.SYS` – [The VDOS Commands CAT and |DIR](#the-vdos-commands-cat-and-dir), [The VDOS Command |ATTRIBUT](#the-vdos-command-attribut)
- 3" drive – [Setting Up the CPC464+DDI-1 with X Drive](#setting-up-the-cpc464ddi-1-with-x-drive), [The VDOS Command |FORMAT](#the-vdos-command-format), [The VDOS Command |X](#the-vdos-command-x), [Making a vortex CP/M Plus Disk (CPC6128 Only)](#making-a-vortex-cpm-plus-disk-cpc6128-only)
- 62K CP/M – [CPC464, CPC664 with X Drive and vortex RAM Card](#cpc464-cpc664-with-x-drive-and-vortex-ram-card), [A Few More Notes](#a-few-more-notes), [1 – Formatting a Disk](#1--formatting-a-disk), [3 – Copying the CP/M System](#3--copying-the-cpm-system)
- µPD 765 – [Error Codes and What They Mean](#error-codes-and-what-they-mean), [Non-Relocatable RAM Area of the VDOS 2.11-X ROM](#non-relocatable-ram-area-of-the-vdos-211-x-rom), [Structure of the Time Constants Area](#structure-of-the-time-constants-area), [Drives + Controller](#drives--controller)

---

## Appendix: The EOF Problem

VDOS 2.0, like VDOS 1.0 before it, has a "weak spot", which, however, is not due to programming errors or carelessness, but is to be found largely in the structure of CPC BASIC and in the intended 3" compatibility.

As you may already know, AMSDOS has, among other things, the so-called "MERGE bug". It shows up in that, while "merging in" a BASIC program, you may suddenly run into an "EOF met" error even though the end of the file has not actually been reached. As simple as the diagnosis of the error is, it is just as hard to get rid of. True, there is, for example, the "DATA Becker patch", which apparently removes this problem, but creates other errors instead.

So as not to leave it at mere words, here is some background information:

By convention, the end of an ASCII file is marked by a `CTRL`+`Z` (= `1A` hexadecimal). This always matters when it is not enough to detect the end only modulo 128, i.e. record by record (this is the so-called **hard end** of a file), but when it is important to find it again exactly to the byte.

For this reason `1A` is used as the EOF marker in AMSDOS and, for compatibility reasons, of course also in VDOS. That is all well and good, as long as it is guaranteed that `1A` really can occur only at the end and not somewhere within the file itself.

But this is exactly where the difficulties begin: the firmware in the CPC provides two standardized ways of reading in data from the peripherals (cassette/disk):

1. **Function 128 (`BC80h`): CAS/DISC IN CHAR** – reads in single characters
2. **Function 129 (`BC83h`): CAS/DISC IN DIRECT** – reads in whole memory blocks

Function 128 causes the problems, because here we have the following return conditions (carry and zero are processor flags of the Z80):

```
Carry true
Zero false
```

if a character could be read from the peripheral unit, and

```
Carry false
Zero false
```

if this was not possible, i.e. the end of the file was reached.

Unfortunately, though, there are two criteria for the end of a file:

- **Criterion 1:** `CTRL`+`Z` (`1Ah`) was detected (soft end).
- **Criterion 2:** The physical end was reached, i.e. that was the last record (hard end).

Now CPC BASIC tests for the end of the file precisely via function 128, and it does so regardless of whether a pure ASCII file or a binary file (e.g. a BASIC program) is being loaded.

That is why you can get an "EOF met" in the middle of "merging" a BASIC program, for example – e.g. when a line number 26 (= `1Ah`) occurs. EOF criterion 1 strikes mercilessly there. The "DATA Becker patch", for example, removes this shortcoming, but on the other hand makes sure that the end of an ASCII file is no longer detected correctly. (The patch simply eliminates criterion 1.)

The dilemma lies simply in the fact that one and the same routine, namely firmware function 128, cannot load both ASCII and binary files with the same EOF marker; this inevitably leads to a contradiction that can only ever be resolved with an "either… or". Unfortunately this was not taken into account in CPC BASIC and/or AMSDOS.

Now to VDOS: in version 1.0 only criterion 1 was taken into account, which is why it was possible to "merge" to your heart's content. There were, however, difficulties with detecting the end of a sequential ASCII file; under certain circumstances 127 characters too many were read in.

VDOS 2.0 cuts the Gordian knot as follows: the user decides which EOF criteria he needs. The RSX function `|DERROR` serves this purpose.

- `|DERROR,2<ENTER>` activates both the pure hard-end detection and the test for the EOF marker `1Ah` (soft end) and is mainly intended for correctly detecting the end of sequential text files. Of course the "EOF met" problem mercilessly turns up here when "merging".

- That is why there is also `|DERROR,3<ENTER>` – incidentally this is the default state after switching on or after a RESET and corresponds to VDOS 1.0 – here only the physical end of the file (hard end) is tested, i.e. there is no "EOF met" problem when "merging", but there are difficulties with sequential text files instead.

So decide for yourself in your program what bothers you less.

VDOS 2.11-X behaves exactly like VDOS 2.0 here. But note: when writing an ASCII file, VDOS 2.11-X writes only a single `1Ah` after the data; the rest of the last record contains old data from the record buffer. With `|DERROR,3` this old data is read in as well (see [Known bugs in VDOS 2.11-X](#known-bugs-in-vdos-211-x)).

---

## Known Bugs in VDOS 2.11-X

The following bugs were found during the analysis of VDOS 2.11-X in the emulator (2026). For each bug you will find what happens, how you can work around it and – for machine code programmers – where it sits in the ROM and how it can be fixed. All addresses are hexadecimal and refer to the VDOS ROM (`C000H`–`FFFFH`). The detailed description with the patch values can be found in the file `bugs.md` of the source code project.

> **(!) Note:** "observed" means the bug was reproduced in the emulator; "read" means it follows from the program code but was not executed.

### Random-Access (Relative) File Management

#### 1. `|GET` Never Reports "Record leer" (Error 55)

If you read a record that lies in a part of the file that does not exist yet (e.g. `|GET,1,2000,@A$` on a file that contains only record 1), you do not get the message `Record leer` but an empty record (observed).

**Workaround:** Do not detect the end of the file via error 55, but – as already recommended in the section "Error Codes and What They Mean" – work with an index file.

**Cause and fix:** The BDOS routine `random_seek` (error exit `E66EH`) sets the error code FFH via `set_file_write_flag` (`E108H`). This uses `SET 7,(HL)`, which does not change the zero flag; as a result `read_random_body` (`E5EDH`) reads anyway and overwrites the error code. Fix: redirect the jump at `E678H` to a small routine in the free area `ED12H` that sets the bit with `OR 80H`.

#### 2. `|FILES` with a Maximum Record Length of 0 Is Accepted

`|FILES,1,0` is not rejected with `Eingabefehler` (read).

**Workaround:** Always give a record length greater than 0.

**Cause:** In `rsx_files` (`D197H`) the error code is loaded, but the carry flag is not set, so the error jump at `D1B6H` is not taken.

#### 3. Channel Number 128 or Above in `|FILES`: Wrong Message

With a channel number of 128 or more, `|FILES` reports `Eingabefehler` instead of `Kanalnummer falsch`.

**Cause:** Message 44 is loaded, but the error path jumps to `error_bad_name`, which itself loads message 33. Fix: on this path, jump directly to the error output with message 44.

#### 4. Record Lengths 256, 512, … Are Unusable

`|OPEN,"T.REL",256,1` is accepted, but `|FIELD` then reports `Kanal nicht offen` (observed).

**Workaround:** Do not use a record length that is a multiple of 256 (i.e. e.g. 255 or 257 instead of 256).

**Cause:** The "channel open" check (`CF4BH`, in `rsx_field`) tests only the low byte of the record length.

#### 5. Direct Strings in `|PUT` Exhaust BASIC's String Management

`|PUT` with strings given directly (e.g. `|PUT,1,15,"Mueller","Koeln","123456"`) works only a few times; on the fifth call with two strings BASIC reports `String expression too complex`, and BASIC may afterwards be in an unclean state (observed).

**Workaround:** Assign the strings to variables first and pass them with `@` (`|PUT,1,15,@NAME$,@ORT$,@TEL$`).

**Cause:** The error patch for BASIC 1.0 (`BEA1H`) does not release BASIC's temporary string descriptors again.

### CAT and |DIR

#### 6. Up to 2K Too Much Free Space

On a completely full 3" disk, `CAT` shows `167K in   5 Files,   2K frei`; correct would be 169K used, 0K free (observed).

**Cause:** `dir_print_free` (`D7C5H`) also counts, in the last byte of the block allocation table (ALV), bits for which there is no block at all. Fix: in the last byte, count only the bits up to the highest block number.

#### 7. Files Over 512K Are Shown Too Small

A file of 516K is shown as `512K` by `CAT` (the total line is correct; observed). This can only happen on the vortex X drive.

**Cause:** The size calculation takes only the extent number into account, not the module byte (byte 14 of the directory entry).

### Files

#### 8. ASCII Files: The Rest of the Last Record Is Not Filled with `1AH`

VDOS writes only a single `1AH` after the data of an ASCII file; the rest of the last record contains old data (observed). Programs that stop at the first `1AH` (CP/M, `|DERROR,2`) read the file correctly. In the power-on state (`|DERROR,3`) BASIC reads the old data as well: a file with 1200 lines gave 1202 lines when read.

**Workaround:** Read text files with `|DERROR,2` (see the appendix "The EOF Problem").

**Cause and fix:** `out_flush_buffer` (`D65CH`) – fill the rest of the record with `1AH`, as CP/M and AMSDOS do.

### |ATTRIBUT and |FORMAT

#### 9. `|ATTRIBUT` with a Wildcard Changes Only the First Matching File

`|ATTRIBUT,"*.BAS","R"` protects only the first BAS file found.

**Workaround:** Give each file individually.

**Cause:** On opening, the name found is written into the FCB, so that `set_attributes` (`E1C2H`) afterwards finds only this one file.

#### 10. `|ATTRIBUT` with an Empty Name

An empty name is not rejected with `Eingabefehler`, but searched for as a name made of spaces; the message is then `wurde nicht gefunden`.

#### 11. `|FORMAT` Checks Only the Low Byte

`|FORMAT,257` formats drive A as if you had entered `|FORMAT,1` (observed).

**Workaround:** Enter only 1 or 2.

### Interface and CP/M

#### 12. Both SIO Channels Use One Shared Copy of Register 5

When the vortex RS232C interface is initialized (`dart_init_channel`, `C767H`), the channel is distinguished by bit 0 of the port address; that is the same for `FADDH` and `FADFH`. As a result only the copy at `BE02H` is written, `BE01H` stays 0 (observed). Currently without effect, since both channels use the same value. Fix: test bit 1 of the port address.

#### 13. Warm Start on a Write-Protected Disk Reports "keine CP/M Diskette"

If the buffer contents cannot be written back during the warm start because the disk is write-protected, VDOS reports `keine CP/M Diskette - Wiederholen J/N ?`, even though the disk is fine (observed; `wboot_no_cpm_disc`, `C4A3H`).

**Note:** If this message appears with a good CP/M disk, the disk is in reality write-protected.

### The Monitor XMON

#### 14. L: `RST 28` (FIRM JUMP) Is Disassembled Wrongly

The disassembler treats `RST 28` as a 1-byte instruction, although (as with `RST 08`, `10`, `18`) an address follows it: `EF 34 12` is listed as `RST 28`, `INC (HL)`, `LD (DE),A` (observed). Fix: table byte at `F5F1H` from `26H` to `A6H`.

#### 15. L: `OUT (n),A` and `IN A,(n)` Always Show `(F4)`

Regardless of the port number, `(F4)` is shown (observed). Fix: jump distance at `F2D3H` from `57H` to `02H`.

#### 16. L: `ED 8B` Is Shown as `OTDR`

`ED 8B` is not a valid instruction, but is listed as `OTDR` (`OTDR` is `ED BB`; observed). Fix: compare value at `F1C6H` from `8BH` to `00H`.

#### 17. L: Weaknesses with IX/IY Instructions

- Invalid sequences `DD xx` / `FD xx` are shown with one byte too many.
- `DD CB d 36` (undocumented) is shown as `SRL`.
- Undocumented `DD CB d op` with a register target are shown like the normal `(IX+d)` form.
- The displacement is shown without a sign (`(IX+FD)` for the displacement -3).

#### 18. R: Switches the Printer Off

After the `R` command, printer output (command `P`) is switched off (observed).

**Workaround:** After `R`, switch the printer on again with `P`.

**Fix:** In `xmon_edit_word` (`F9D6H`), point the calls at `F9DFH` and `F9E3H` to `xmon_hex_byte` (`FA28H`) instead of `FA1BH`.

#### 19. A: Destroys the Memory Contents at `0080H`–`0094H`

After an `A` command, on a later memory access of the monitor above `8000H`, the area `0080H`–`0094H` contains spaces – under CP/M this is the buffer for the command line (observed).

**Cause:** The input buffer of the A command (255 characters) overlaps the copy that the monitor makes of `0080H`–`0094H`. Fix: set the maximum length at `FCD2H` from `FFH` to `D1H` (209 characters).

#### 20. T: Runs Away After a `RET`

After a single-stepped `RET`, the step count becomes the return address; in a loop like `JR $` the monitor lost control (observed). Fix: jump target at `F839H` from `31H` to `2AH`.

#### 21. T: Further Weaknesses in Single Step

- A conditional `RET cc` is always executed without checking the condition.
- `RST 00`, `20`, `30`, `38` are treated like a `RET`.
- With `RST 08` and `RST 28` a word from the monitor's stack is used as the next address.
- A jump to itself (`DJNZ $`, `JR $`) is never executed.
- After `RST 10` / `RST 18` the called program runs without single step.

**Workaround:** Skip such places with `G` and a breakpoint.

#### 22. M: An Overlapping Move Upward Lands One Byte Too High

`M4000,4003,4002` turns `11 22 33 44 55 66 77` into the sequence `11 22 33 11 22 33 44` instead of `11 22 11 22 33 44 77` (observed).

**Workaround:** Move overlapping areas in two steps via a free intermediate area.

**Fix:** Rearrange the five one-byte instructions at `F78EH`–`F792H`: `03 E1 EB 09 EB` → `E1 EB 09 EB 03`.

#### 23. M: End Address Lower Than Start Address

If `adresse2` is lower than `adresse1`, almost 64 KB are copied (read) – the computer usually crashes.

**Workaround:** Enter the addresses carefully.

#### 24. O: `<ESC>` During Address Entry Leaves the File Open

If you abort the O command with `<ESC>` while entering the start address, length or execution address, the output file stays open; a file `name.$$$` is left behind on the disk. The next O command then fails without a message; only the one after that works (observed).

**Workaround:** After an abort, give the O command twice more (the first one only releases the output channel) and later delete the leftover `.$$$` file with `|ERA`.

#### 25. @ (Disk Monitor): T and G Keep an Invalid Position

If you enter an invalid track or an invalid block with `T` or `G`, the disk monitor does report `>>`, but the wrong position stays set (e.g. `TA0` → `>>`, after that `R` returns the error `E:45`; observed). A `W` at this point could write outside the CP/M area.

**Workaround:** After `>>`, enter the position again correctly with `T` / `S` or `G` before using `R` or `W`.

**Cause:** `xdm_cmd_track` (`EB5FH`) and `xdm_cmd_block` (`EC66H`) store the new position before it is checked.

### Further Notes (Not Bugs)

- **`|CPM` without parameters** starts the CP/M loader of AMSDOS without a firmware reset. The RSX chain then still points into VDOS's RAM area, which is overwritten by CP/M. The CP/M command `AMSDOS` may then report `BASIC not found`. Workaround: enter `|AMSDOS` beforehand or reset the computer.
- **XMON under CP/M:** `Y` has no effect there; in the area `C000H`–`FFFFH` you always see the VDOS ROM.
- **XMON I** does not load files without a file header.
- **Message texts:** Some messages read differently from the VDOS 2.0 manual: `Kanal bereits offen`, `Kanal nicht offen`, `Recordnummer zu gross`, `Record leer`, `<datei> hat Schreibschutz`, `Eingabefehler`; the disk monitor reports `E:xx` instead of `ERR:xx`. This edition of the manual already uses the texts of VDOS 2.11-X.

---

*End of manual*
