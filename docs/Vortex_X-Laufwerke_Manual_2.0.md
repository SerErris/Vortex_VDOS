# VORTEX X-Laufwerke F1-X und M1-X

**Benutzerhandbuch** · Rev. 1 / 17.4.1986 · 1. Auflage · © 1986 vortex Computersysteme GmbH

---

## Inhaltsverzeichnis

- [Vorwort](#vorwort)
- [Wichtige Hinweise](#wichtige-hinweise)
- [vortex X-Laufwerke auf einen Blick](#vortex-x-laufwerke-auf-einen-blick)
- [Inbetriebnahme CPC464+DDI-1 mit X-Laufwerk](#inbetriebnahme-cpc464ddi-1-mit-x-laufwerk)
- [Inbetriebnahme CPC664/CPC6128 mit X-Laufwerk](#inbetriebnahme-cpc664cpc6128-mit-x-laufwerk)
- [Disketten, Disketten und nochmals Disketten](#disketten-disketten-und-nochmals-disketten)
  - [Welche Disketten benötigen wir?](#welche-disketten-benötigen-wir)
  - [Niemals](#niemals)
  - [Immer](#immer)
- [VDOS – Vortex Disk Operating System](#vdos--vortex-disk-operating-system)
- [Grundlagen](#grundlagen)
- [Der VDOS Befehl |FORMAT](#der-vdos-befehl-format)
- [Starten und Sichern eines BASIC-Programms](#starten-und-sichern-eines-basic-programms)
- [Was ist überhaupt eine Datei?](#was-ist-überhaupt-eine-datei)
- [Die VDOS Befehle |A und |B](#die-vdos-befehle-a-und-b)
- [Der VDOS Befehl |X](#der-vdos-befehl-x)
- [Die VDOS Befehle CAT und |DIR](#die-vdos-befehle-cat-und-dir)
- [Der VDOS Befehl |ATTRIBUT](#der-vdos-befehl-attribut)
- [Der VDOS Befehl |ERA](#der-vdos-befehl-era)
- [Der VDOS Befehl |REN](#der-vdos-befehl-ren)
- [Der VDOS Befehl |SELECT](#der-vdos-befehl-select)
- [Der VDOS Befehl |RESET](#der-vdos-befehl-reset)
- [Der VDOS Befehl |CODE](#der-vdos-befehl-code)
- [Der VDOS Befehl |AMSDOS](#der-vdos-befehl-amsdos)
- [Cassetten-Rekorder am CPC](#cassetten-rekorder-am-cpc)
  - [Der VDOS Befehl |DISC](#der-vdos-befehl-disc)
  - [Der VDOS Befehl |CAS](#der-vdos-befehl-cas)
  - [Der VDOS Befehl |DISC.IN](#der-vdos-befehl-discin)
  - [Der VDOS Befehl |CAS.IN](#der-vdos-befehl-casin)
  - [Der VDOS Befehl |DISC.OUT](#der-vdos-befehl-discout)
  - [Der VDOS Befehl |CAS.OUT](#der-vdos-befehl-casout)
- [Der VDOS Befehl |XMON – der vortex Z80-Monitor](#der-vdos-befehl-xmon--der-vortex-z80-monitor)
- [Der VDOS Befehl |ROMOFF](#der-vdos-befehl-romoff)
- [Der VDOS Befehl |ROMS](#der-vdos-befehl-roms)
- [Relative und Sequentielle Dateiverwaltung](#relative-und-sequentielle-dateiverwaltung)
- [Der VDOS Befehl |FILES](#der-vdos-befehl-files)
- [Der VDOS Befehl |OPEN](#der-vdos-befehl-open)
- [Der VDOS Befehl |FIELD](#der-vdos-befehl-field)
- [Der VDOS Befehl |GET](#der-vdos-befehl-get)
- [Der VDOS Befehl |PUT](#der-vdos-befehl-put)
- [Der VDOS Befehl |CLOSE](#der-vdos-befehl-close)
- [Zwei kleine Anwendungen](#zwei-kleine-anwendungen)
- [Abfangmöglichkeiten von Diskettenfehlern](#abfangmöglichkeiten-von-diskettenfehlern)
- [Fehlercodes und ihre Bedeutung](#fehlercodes-und-ihre-bedeutung)
- [Die VDOS Turnkey Funktion](#die-vdos-turnkey-funktion)
- [X-Laufwerke am CPC464 mit DDI-1, CPC664 und CPC6128](#x-laufwerke-am-cpc464-mit-ddi-1-cpc664-und-cpc6128)
- [Erzeugen einer vortex CP/M 2.2 Systemdiskette](#erzeugen-einer-vortex-cpm-22-systemdiskette)
- [CPC464, CPC664 mit X-Laufwerk und vortex RAM-Karte](#cpc464-cpc664-mit-x-laufwerk-und-vortex-ram-karte)
- [Erstellen einer vortex CP/M plus Diskette (nur CPC6128)](#erstellen-einer-vortex-cpm-plus-diskette-nur-cpc6128)
- [Das Laden des CP/M Betriebssystems](#das-laden-des-cpm-betriebssystems)
  - [Der VDOS Befehl |CPM](#der-vdos-befehl-cpm)
  - [Der VDOS Befehl |CPM,1](#der-vdos-befehl-cpm1)
  - [Der VDOS Befehl |CPM,2](#der-vdos-befehl-cpm2)
- [CP/M mit Ihrem vortex X-Laufwerk](#cpm-mit-ihrem-vortex-x-laufwerk)
- [Der CP/M Befehl FILECOPY](#der-cpm-befehl-filecopy)
- [Der CP/M Befehl XMON](#der-cpm-befehl-xmon)
- [Der CP/M Befehl SYSGEN](#der-cpm-befehl-sysgen)
- [Der CP/M Befehl DISKTOOL](#der-cpm-befehl-disktool)
- [Der CP/M Befehl INSTALL](#der-cpm-befehl-install)
- [Der CP/M Befehl CASCOPY](#der-cpm-befehl-cascopy)
- [Der CP/M Befehl VDOS](#der-cpm-befehl-vdos)
- [Der CP/M Befehl FAST](#der-cpm-befehl-fast)
- [CP/M Fehlermeldungen und ihre eventuelle Beseitigung](#cpm-fehlermeldungen-und-ihre-eventuelle-beseitigung)
- [VDOS und CP/M intern](#vdos-und-cpm-intern)
  - [BIOS – Basic Input Output System](#bios--basic-input-output-system)
  - [DOS – Disk Operating System](#dos--disk-operating-system)
  - [RAM Variablen von BIOS und DOS](#ram-variablen-von-bios-und-dos)
- [CP/M unter der Lupe – CP/M-Betriebssystem](#cpm-unter-der-lupe--cpm-betriebssystem)
- [Abschließend noch ein paar Worte zur Hardware](#abschließend-noch-ein-paar-worte-zur-hardware)
- [Pinbelegung der Connectoren](#pinbelegung-der-connectoren)
- [Stichwortverzeichnis](#stichwortverzeichnis)
- [Anhang: Das EOF Problem](#anhang-das-eof-problem)

---

## Vorwort

**vortex Floppy Disk Stationen F1-X und M1-X für alle CPC464+DDI-1, CPC664, CPC6128**

Liebe CPC Besitzer,

so ziemlich genau vor einem Jahr (im April 85) hat das erste "vortex Baby" das Licht der Welt erblickt: die **vortex Floppy Disk Station F1-D**, konzipiert für den damals noch brandneuen CPC464. Eine "kleine Revolution" hat man unseren Sprößling genannt. Mit Recht, denn die Leistungsdaten dieses Gerätes sind in der Tat revolutionär: hohe Speicherkapazität (1,4 MegaByte), gängiges Diskettenformat (5,25"), billige gut erhältliche Disketten, modernste Laufwerke, ausgereifte Controllerelektronik und intelligente schnelle Betriebssystemsoftware.

Bahnbrechend auch der Kundenservice. Ob es nur darum geht zu erklären, wie eine Diskette formatiert wird, oder ob tatkräftige Unterstützung bei der Anpassung eines Programms benötigt wird, immer finden Sie in unserem Team einen kompetenten Fachmann, der Ihnen gerne hilft.

Nobody is perfect. Es gibt kein Programm, das nicht mindestens eine Schwachstelle hat. Meistens ist es nicht nur eine, sondern… Sind Sie anderswo alleingelassen, bei uns wird ständig verbessert und gefeilt, und was das Wichtigste ist, Sie sind mit von der Partie: Gibt es Neuheiten, oder wurden eventuelle Fehler behoben, Sie können Ihre Floppy – auch wenn Sie sie schon vor einem Jahr gekauft haben – mit dieser neuen Software ausrüsten.

All dies auf einen Nenner gebracht und Sie wissen, warum wir so viel Erfolg haben.

Das schnelle Hinzukommen des CPC664 und dann des CPC6128 hat uns dazu veranlaßt, für weiteren Nachwuchs zu sorgen. Beinahe auf einen Schlag ist eine ganze Reihe neuer Floppy-Laufwerke und als Krönung eine Festplatte entstanden.

Einmal mehr haben wir bewiesen, was wir leisten können, wobei es uns aber vollkommen unklar blieb, warum wir die einzigen sein sollen. Es muß wohl daran liegen, daß wir besser sind als gut.

Einen wesentlichen Anteil an unserer Arbeit hatte ein Projekt, dem wir firmenintern den Spitznamen "K-Projekt" gegeben haben. Dahinter verbirgt sich eine ganze Gruppe von Laufwerken, die ausschließlich dafür gedacht sind, im Zusammenhang mit einem bereits vorhandenen 3"-Laufwerk und 3"-Floppy-Controller – CPC464+DDI-1, CPC664, CPC6128 – zu arbeiten. Ausgeschlossen war dabei natürlich die simple und bereits erledigte Entwicklung eines Zweitlaufwerks mit geringer Speicherkapazität (vortex Laufwerke F1-Z und M1-Z). Nein, es mußte etwas sein, was den Kauf eines "Zweitlaufwerkes" vollkommen sinnlos machen sollte.

…sagte: "Zuerst einmal brauchen wir eine hohe Speicherkapazität, damit die Not endlich ein Ende hat: 700 KB müßten eigentlich genug sein. Und bitte endlich ein gängiges Diskettenformat mit immer und überall erhältlichen Disketten zu niedrigen Preisen: 5,25", 3,5". Dann noch ein professionelles Betriebssystem: VDOS 2.0 und natürlich auch CP/M 2.2 und CP/M plus. Und bitte nicht noch ein 'herumbaumelndes' Kästchen. Vor allem bitte kein 'Einschicken', 'Löten', ach und dann die Sache mit den Copyrights… Leistung und Preis: sensationell."

**Das Ergebnis: vortex X-Laufwerke F1-X und M1-X**

- Hohe Speicherkapazität: 708 KB formatiert
- Gängige Diskettenformate: 5,25" oder 3,5"
- Billige Disketten, keine Lieferengpässe
- Professionelles Betriebssystem VDOS 2.0
- VDOS Steckmodul, in das der DDI-1 Controller eingesetzt wird
- Relative Dateiverwaltung unter BASIC
- Z80 Maschinensprache-Monitor
- Voll kompatibel zur bereits vorhandenen Software VDOS 2.0 und AMSDOS!
- CP/M 2.2 und CP/M plus
- vorbereitet für eine serielle RS232C Schnittstelle
- 128 mögliche Directory-Einträge
- Der Preis… traumhaft!

Und Sie haben sich auch dafür entschieden, eigentlich klar, denn es gibt keine Alternative.

Das vorliegende Handbuch beschreibt alle Befehle und Details der vortex X-Laufwerke. Genauere Informationen über CP/M 2.2 und CP/M plus entnehmen Sie bitte Ihren Handbüchern, die Sie beim Kauf des CPC's miterhalten haben.

Dieses Handbuch besteht aus 3 großen Teilen:

- Beschreibung aller VDOS Befehle
- Beschreibung aller vortex CP/M Befehle
  Das Kapitel "X-Laufwerke am CPC464 mit DDI-1, CPC664 und CPC6128" beschreibt speziell, wie Sie sich eine CP/M-Systemdiskette herstellen können.
- Technische Informationen über VDOS und CP/M im Zusammenhang mit den X-Laufwerken

Nehmen Sie sich bitte die Zeit, einmal alles in Ruhe durchzulesen. Das hilft Ihnen und uns!

Nun wünschen wir Ihnen viel Spaß mit Ihrer neuen vortex Floppy.

*Ihr vortex Team*

---

## Wichtige Hinweise

> **(!) Wichtig**
>
> Vervielfältigung und Weitergabe – auch nur auszugsweise – dieses Handbuches bedürfen einer vorherigen schriftlichen Genehmigung der Firma vortex Computersysteme GmbH.
>
> Alle Änderungen vorbehalten.
>
> Alle Wartungs- und Garantiearbeiten müssen von vortex bzw. vortex-autorisierten Händlern durchgeführt werden. In jedem anderen Fall erlischt jeglicher Garantieanspruch.
>
> Werden die Geräte zu Wartungs- und Garantiearbeiten nicht ordnungsgemäß verpackt zu vortex zurückgeschickt (fehlt im Besonderen die Transportschutz-Pappdiskette im Laufwerk), ist auf jeden Fall jegliche Garantieleistung verfallen.
>
> **Geräte immer in Originalverpackungen versenden!**
>
> vortex übernimmt keine Verantwortung, was die Eignung des Produkts für bestimmte Anwendungen anbetrifft.

> Z80 ist ein eingetragenes Warenzeichen der Firma Zilog Inc.
>
> vortex und vortex VDOS sind eingetragene Warenzeichen der Firma vortex GmbH.
>
> CP/M 2.2 und CP/M plus sind eingetragene Warenzeichen der Firma Digital Research Inc.
>
> WordStar ist ein eingetragenes Warenzeichen der Firma MicroPro Inc.
>
> dBase II ist ein eingetragenes Warenzeichen der Firma Ashton Tate.
>
> Multiplan ist ein eingetragenes Warenzeichen der Firma Microsoft.

---

## vortex X-Laufwerke auf einen Blick

Unsere X-Laufwerke sind in zwei verschiedenen Ausführungen erhältlich:

- mit einem 5,25" Laufwerk
- oder einem 3,5" Laufwerk

mit jeweils 708 KB formatierter Speicherkapazität.

| Bezeichnung | Laufwerk |
|-------------|----------|
| **F1-X**    | 5,25" Laufwerk |
| **M1-X**    | 3,5" Laufwerk  |

Folgende Gerätekombinationen (Sets) sind möglich:

| Computer | + Laufwerk | Format | Kapazität | Betriebssysteme |
|----------|------------|--------|-----------|-----------------|
| CPC464+DDI-1 | F1-X | 5,25" | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC464+DDI-1 | M1-X | 3,5"  | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC664       | F1-X | 5,25" | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC664       | M1-X | 3,5"  | 708 KB | VDOS, AMSDOS, CP/M 2.2 |
| CPC6128      | F1-X | 5,25" | 708 KB | VDOS, AMSDOS, CP/M 2.2/+ |
| CPC6128      | M1-X | 3,5"  | 708 KB | VDOS, AMSDOS, CP/M 2.2/+ |

(`+` = CP/M plus Betriebssystem)

Im nachfolgenden Handbuch werden wir immer von **X-Laufwerken** sprechen, da alle Befehle bei den Laufwerken M1-X und F1-X absolut identisch sind.

Alle vortex X-Laufwerke benötigen 220 V Netzspannung bei 50 Hz.

Zu allen X-Laufwerken gehört das sogenannte **VDOS Modul** (kleines Interface in formschönem Kunststoffgehäuse; trägt im wesentlichen das VDOS EPROM). Dieses Modul ist auch für die Aufnahme der vortex RS232C Schnittstelle vorbereitet. Haben Sie einen CPC464+DDI-1, so "verschwindet" Ihr DDI-1 Floppy Controller in diesem Modul.

Das Laufwerk selber und das Netzteil sind in einem soliden Metallgehäuse untergebracht.

Zum Ein-/Ausschalten des Laufwerks befindet sich an der Rückseite des Metallgehäuses ein Druckknopf-Schalter. Steht dieser nur wenig über die Rückwand heraus, so ist das Laufwerk eingeschaltet. Der Netzstecker des Laufwerks kann auch bei längerer Nichtbenutzung des Geräts in der Steckdose bleiben.

Bei allen X-Laufwerken kann wahlweise zwischen dem VDOS und dem AMSDOS Betriebssystem umgeschaltet werden. Nach dem Einschalten des Sets steht immer sofort das VDOS Betriebssystem zur Verfügung.

Bei allen Sets, die den CPC6128 enthalten, haben Sie alternativ zum CP/M 2.2 Betriebssystem auch das CP/M plus Betriebssystem zur Verfügung.

Wird das X-Laufwerk unter VDOS oder CP/M (mit vortex BIOS) betrieben, verfügt es über 128 Directory-Einträge.

Das 3"-Laufwerk kann in jedem Betriebszustand (AMSDOS, VDOS, CP/M) maximal 64 Directory-Einträge verwalten.

Haben Sie ein Set bestehend aus CPC464+DDI-1 mit X-Laufwerk, dann ist folgende Geräteeinschalt-Reihenfolge zu beachten:

1. DDI-1 Floppy einschalten
2. vortex X-Laufwerk einschalten
3. CPC464 einschalten

Bei den Sets mit dem CPC664 oder CPC6128 ist keine Einschalt-Reihenfolge zu beachten.

Das Set CPC464+DDI-1 mit X-Laufwerk verfügt über die "Turnkey-Funktion". Nach jedem Reset (Ein-/Ausschalten oder gleichzeitiges Drücken der `CTRL`+`SHIFT`+`ESC`-Tasten) wird auf der 3"-Diskette im 3"-Laufwerk nach einer Datei `HELLO.BAS` gesucht. Wird sie gefunden, so wird sie gestartet. Das Suchen kann durch das sofortige (nach dem Reset) Drücken z.B. der `ESC`-Taste unterbunden werden. Mit Hilfe dieser Funktion kann das System vom Start weg in einen bestimmten Betriebszustand (z.B. CP/M) hochgefahren werden.

Alle Sets mit dem CPC664 und CPC6128 verfügen nicht über diese Funktion.

---

## Inbetriebnahme CPC464+DDI-1 mit X-Laufwerk

> **(!) Wichtig:** Alle Stecker aus der Steckdose ziehen.

Die Inbetriebnahme dieses Sets erfolgt in zwei Stufen:

- Montage des DDI-1 Floppy Controllers in das Gehäuse des VDOS Moduls (graues "pyramidenstumpf"-artiges Kunststoffgehäuse)
- Anstecken des X-Laufwerkes an das Flachbandkabel des DDI-1 Floppy Controllers.

Was Sie hierzu an Werkzeug brauchen, ist ein kleiner Kreuzschraubenzieher, das ist alles. Außerdem sollten Sie auch etwas Ruhe mitbringen, damit Sie die Inbetriebnahme Ihres Gerätes überhaupt noch erleben.

**A.** Nehmen Sie das VDOS Modul aus der Verpackung heraus. Auf der Unterseite des Gehäuses sehen Sie vier kleine Kreuzschrauben. Lösen Sie diese und legen Sie sie an einen sicheren Ort. Jetzt können Sie den Deckel wegnehmen.

**B.** Sie sehen jetzt, wenn Sie in das Gehäuse hineinschauen, eine kleine Platine (und zwar von der Bauteileseite). Senkrecht auf dieser Platine, zu Ihnen herzeigend, sehen Sie eine kleine weitere Platine, die allerdings keine Bauteile trägt. Sie ist mit 50 "Kontaktzungen" versehen. Man nennt diese kleine Platine auch "Card-Edge Stecker".

**C.** Holen Sie jetzt den DDI-1 Floppy Controller her (Sie haben ihn zuvor von Ihrem CPC abgesteckt. Außerdem haben Sie auch das 3"-Laufwerk abgesteckt).

**D.** Wenn Sie sich den Controller anschauen, so finden Sie an ihm das Gegenstück zum "Card-Edge Stecker", nämlich die "Card-Edge Buchse" (über sie wird auch der Controller ohne X-Laufwerk an den CPC angesteckt).

**E.** Wenn Sie das VDOS Modul näher betrachten, so sehen Sie an einer Seite durch einen Schlitz ein 50-poliges Flachbandkabel mit Card-Edge Buchse herausragen.

**F.** Nehmen Sie das VDOS Modul nun so in die linke Hand, daß Sie von unten hineinsehen können und das unter "E." erwähnte 50-polige Flachbandkabel von Ihnen wegzeigt.

**G.** Nehmen Sie in die rechte Hand den DDI-1 Floppy Controller, so daß die 50-polige Cardedge-Buchse in das offene Modul hineinzeigt und das 34-polige Flachbandkabel nach rechts weggeht.

**H.** Stecken Sie den DDI-1 Floppy Controller so in das VDOS Modul ein, daß die kleine senkrechte Platine im VDOS Modul in der 50-poligen Card-Edge Buchse des DDI-1 Floppy Controllers steckt. Drücken Sie den DDI-1 Floppy Controller fest ein.

**I.** Holen Sie den Boden-Deckel des VDOS Moduls wieder her und schrauben Sie das VDOS Modul wieder zu (mit den vier Kreuzschrauben von vorhin – die haben Sie doch noch, oder?).

**J.** Sie sehen, vortex hat etwas gedacht: nicht noch ein herumbaumelndes zweites Kästchen, sondern eine saubere kompakte Einheit, die auch noch genügend Platz für die vortex RS232C Schnittstelle bereitstellt.

**K.** Stecken Sie das VDOS Modul – nunmehr ein kompletter Floppy Controller mit AMSDOS und VDOS! – hinten am CPC464 auf den 50-poligen "Expansion Bus" auf (selbe Stelle, an der der DDI-1 Floppy Controller alleine angesteckt war). Das VDOS Modul kommt so zu liegen, daß nach rechts (zum Cassettenrekorder hin) das 34-polige Flachbandkabel zeigt.

**L.** Stellen Sie jetzt rechts neben Ihren CPC (Seite mit dem Cassettenrekorder) das X-Laufwerk (Diskettenschacht nach vorne) und darauf das 3"-Laufwerk.

**M.** Jetzt ist eigentlich schon alles klar. Die 34-polige Buchsenleiste am Ende des 34-poligen Flachbandkabels kommt oben in das 3"-Laufwerk, der aus dem X-Laufwerk heraushängende 34-polige Stecker kommt in die zweite Buchse am 34-poligen Flachbandkabel.

**N.** Alle Stecker in die Steckdose, 3"-Laufwerk, dann X-Laufwerk (siehe Druckknopf an der Rückseite des X-Laufwerks) und dann CPC einschalten – fertig!

Damit ist Ihr "neues" Computersystem betriebsbereit.

### Einschaltreihenfolge

1. DDI-1 Floppy einschalten
2. X-Laufwerk einschalten
3. CPC464 einschalten

Sofort nach dem Einschalten des Sets gilt:

- VDOS ist eingeschaltet
- Laufwerk A ist das 3"-Laufwerk
- Laufwerk B ist das X-Laufwerk
- das 3"-Laufwerk kann maximal 64 Directory-Einträge verwalten
- das X-Laufwerk kann maximal 128 Directory-Einträge verwalten

---

## Inbetriebnahme CPC664/CPC6128 mit X-Laufwerk

> **(!) Wichtig:** Alle Stecker aus der Steckdose ziehen.

Die Inbetriebnahme dieses Sets ist denkbar einfach. Nehmen Sie das VDOS Modul aus der Verpackung heraus. Sie sehen aus dem Modul ein 50-poliges Flachbandkabel hängen, das an seinem Ende eine 50-polige Buchse trägt. Stellen Sie das VDOS Modul so hinter Ihren CPC, daß das Kabel zu Ihnen herweist und oben der vortex-Schriftzug ist. Stecken Sie die Buchse auf den 50-poligen "Expansion Bus" an Ihrem CPC auf.

Jetzt muß noch das X-Laufwerk angeschlossen werden. Sie finden hinten an Ihrem CPC einen Stecker mit der Bezeichnung **Disc drive 2** und am X-Laufwerk ein 34-poliges Kabel, an dessen Ende eine 34-polige Buchse ist, die genau auf den Stecker mit der Bezeichnung "Disc drive 2" paßt. Die Buchse wird so aufgesteckt, daß das Flachbandkabel nach oben herausgeht ("OBEN"-Kleber beachten!).

Alle Stecker in die Steckdose, CPC einschalten, X-Laufwerk einschalten (siehe Druckknopf hinten am X-Laufwerk), fertig.

Sofort nach dem Einschalten jedes Sets gilt:

- VDOS ist eingeschaltet
- Laufwerk A ist das 3"-Laufwerk
- Laufwerk B ist das X-Laufwerk
- das 3"-Laufwerk kann maximal 64 Directory-Einträge verwalten
- das X-Laufwerk kann maximal 128 Directory-Einträge verwalten

---

## Disketten, Disketten und nochmals Disketten

### Welche Disketten benötigen wir?

Alle vortex Floppies sind mit 80-Spur-Laufwerken ausgerüstet und verfügen über zwei Schreib-/Leseköpfe (Vorder- und Rückseite der Diskette). Je nachdem, ob Sie sich für das 5,25"-Format oder das 3,5"-Format entschieden haben, brauchen Sie für einen sicheren problemlosen Betrieb der vortex Station Disketten folgenden Typs:

| Laufwerk | Diskettentyp |
|----------|--------------|
| 5,25" Laufwerke | DS/DD/96tpi |
| 3,5" Laufwerke  | DS/DD/135tpi |

DS steht für **DoubleSided** (zweiseitig). DD steht für **DoubleDensity** (doppelte Datendichte). 96tpi (135tpi) steht für 96 (135) tracks per inch, d.h. 80 Spuren.

Sie sollten nur Disketten dieser Bezeichnung verwenden. Kaufen Sie bitte nur Qualitätsdisketten, da schlechtes Diskettenmaterial nicht nur auf Kosten der Datensicherheit geht, sondern auch den Laufwerken schaden kann.

Bei den 5,25"-Disketten kann die Diskette **2/96 FlexyDisk 5.25 von BASF**, bei den 3,5"-Disketten die Diskette **MF2DD 135tpi von FUJI FILM** empfohlen werden. Beide Disketten sind bei uns in Langzeittests auf "Herz und Nieren" geprüft worden.

### Niemals

- Magnetscheibe direkt berühren
- Diskette biegen oder knicken
- den auf der Diskette angegebenen Temperaturbereich verlassen
- Diskette Magnetfeldern aussetzen
- Aufkleber direkt auf der Diskette beschriften
- nebenher Rauchen (das sollten Sie überhaupt lassen!)
- auf die Diskette schwere kantige Gegenstände legen
- viele Disketten aufeinanderlegen und so aufbewahren

### Immer

- Disketten nach Gebrauch in die Schutztasche zurückstecken
- Disketten stehend in einer entsprechenden Box aufbewahren
- vorsichtig in den Laufwerksschacht schieben, ohne Knicken oder Verkanten
- Diskette so einlegen, daß der Diskettenaufkleber nach oben und die Schreib-/Leseöffnung zum Laufwerk zeigt und die Diskette einrastet

Diese Punkte sollten Sie unbedingt beachten.

Wenn die Diskette eingerastet ist, den Auswurfknopf fest eindrücken. Das "Auswerfen" der Diskette aus dem Laufwerk erreicht man durch nochmaliges Drücken des Auswurfknopfes.

> **(!) Hinweis:** Während das Laufwerk arbeitet, darf niemals die Diskette aus dem Laufwerk herausgenommen werden.

---

## VDOS – Vortex Disk Operating System

**VDOS** ist eine Abkürzung für **Vortex Disk Operating System**.

### Was ist das, ein DOS?

DOS, ins Deutsche übersetzt, heißt **Disketten Betriebssystem**.

Ein Betriebssystem ist nichts anderes als ein Programm, das die Steuerung einer bestimmten Hardware übernimmt. Die Hardware ist eine logische Verschaltung mehrerer elektronischer Bausteine (Integrierte Schaltungen, Chips). Im Falle Ihres Schneider Computers sind das im einzelnen der Z80 Microprozessor, der RAM-Speicher (Schreib-/Lesespeicher), ROM-Speicher (nur lesbarer Speicher), der Videocontroller, der Schnittstellenbaustein, der Sound-Generator und einige Chips mehr.

Damit diese Hardware so funktioniert, wie Sie das von Ihrem Computer gewohnt sind und auch erwarten, benötigt man das Betriebssystem. Es arbeitet ununterbrochen im Verborgenen und hält alle Fäden in der Hand. Es stellt Ihnen einfachste Befehle zur Verfügung, die einen spielenden Umgang mit der Hardware erlauben, ohne daß Sie je verstanden haben müßten, wie der ganze Computer überhaupt funktioniert.

Eine Disketten- oder Floppy Disk Station ist im Grunde auch nichts anderes als eine Hardware. Sie besteht aus den Laufwerken selbst, einem Netzteil und einem Controller, auch Interface oder Schnittstelle genannt. Um die Floppy Disk Station in Verbindung mit Ihrem Computer betreiben zu können, wird eine Betriebssystemerweiterung, ein DOS, benötigt. Auch hier gilt der Grundsatz, daß alles möglichst unkompliziert und ohne spezielle Vorkenntnisse bedient werden kann.

Wenn ich vorhin von einer Betriebssystemerweiterung gesprochen habe, so ist das eigentlich etwas untertrieben. Das DOS ist eine sehr komplizierte Sache, da es zum einen die gesamte Diskettenstation bedienen muß und zum anderen noch derart in das bereits vorhandene Betriebssystem eingefügt werden muß, daß nirgendwo Widersprüche und Spannungen entstehen dürfen.

Das VDOS, das Disketten-Betriebssystem der Firma vortex, wurde speziell für die Schneider Computer entwickelt. Es ist in der Lage, Laufwerke mit hoher Kapazität (700 KByte) zu versorgen und beinhaltet alle Funktionen, die ein professionelles DOS haben sollte.

Eine Besonderheit des VDOS ist die **Relative Dateiverwaltung** unter BASIC. Hatten Sie unter AMSDOS bislang nur die Möglichkeit, zwei sequentielle Dateien gleichzeitig zu benutzen, können Sie unter VDOS gleichzeitig zwei sequentielle und 16 relative Dateien verwenden. Erst der "wahlfreie" Zugriff auf die Daten einer relativen Datei ermöglicht z.B. die Entwicklung eines professionellen Datenbank-Systems unter BASIC.

Auch für die Freunde der Maschinenprogrammierung bietet VDOS etwas ganz Besonderes: der **Z80 Maschinensprache-Monitor**. Gab es unter AMSDOS keine vernünftige Möglichkeit, "ins System hineinzuschauen", mit VDOS ist das kein Problem mehr.

Alles in allem handelt es sich bei VDOS um ein Betriebssystem, das die Möglichkeiten eines AMSDOS weit übersteigt. Aber überzeugen Sie sich selbst.

---

## Grundlagen

Alle VDOS Befehle haben eines gemeinsam: sie beginnen mit einem senkrechten Strich `|`. Dieser Strich teilt dem CPC mit, daß jetzt ein VDOS Befehl kommt und nicht ein BASIC Befehl. Befehle, die mit einem senkrechten Strich beginnen, werden oft auch "RSX Befehle" oder "externe Befehle" genannt und sind keine "Spezialität" des VDOS Betriebssystems.

### Wie erzeugen wir den senkrechten Strich?

Zwischen der Taste `P` und der Taste mit der eckigen Klammer auf `[` liegt die Taste mit dem "Klammeraffen" `@`. Drücken wir die `SHIFT`-Taste und diese Taste, dann wird der senkrechte Strich `|` ausgegeben.

Um dem CPC mitzuteilen, daß das, was wir gerade eingegeben haben, als Befehl verstanden werden soll, müssen wir die `ENTER`-Taste drücken. Zukünftig werden wir das durch `<ENTER>` symbolisieren.

Eine allgemeine Befehlseingabe sieht also wie folgt aus:

```
|VDOS-BEFEHL<ENTER>
```

Geben Sie z.B. einmal folgendes ein:

```
|DIR<ENTER>

Laufwerk A: User 0

TEST    .BAS  INSTALL .COM  TEST    .BIN  RUNNER  .BAS

60K belegt, 4 Dateien, 109K frei

Ready
```

Hier wird uns angezeigt, welche Dateien auf der 3"-Diskette im 3"-Laufwerk sind.

Es gibt bei den VDOS Befehlen (sind externe Befehle) noch eine weitere Besonderheit zu beachten. Soll mit einem VDOS Befehl irgendeine Variable mitübergeben werden, dann muß in manchen Fällen die Variable mit einem "Klammeraffen" `@` versehen werden. In anderen Fällen kann man auch den Inhalt der Variablen direkt mitübergeben. So z.B.

```
A$="*.BAS"<ENTER>
|DIR,@A$<ENTER>

Laufwerk A: User 0

TEST    .BAS  RUNNER  .BAS

60K belegt, 2 Dateien, 109K frei
```

Beim `|DIR` Befehl hätten wir aber auch direkt sagen können:

```
|DIR,"*.BAS"<ENTER>
```

und hätten dasselbe Ergebnis wie oben erzielt.

Beim `|GET`-Befehl (gehört zur relativen Dateiverwaltung) hingegen darf nur die Schreibweise mit dem "Klammeraffen" verwendet werden:

```basic
NAME$="otto"
ORT$="Essen"
TELE$="0123456"
|GET,1,173,@NAME$,@ORT$,@TELE$
```

Der "Klammeraffe" ist nicht das Resultat eines "schlechten" Betriebssystems, sondern eine Eigenheit des BASIC's, das in Ihrem CPC eingebaut ist. Ich werde Sie darauf hinweisen, wenn nur die Darstellung mit dem "Klammeraffen" erlaubt ist. In allen anderen Fällen können Sie beides verwenden, wobei die zweite oben gezeigte Möglichkeit sicherlich die angenehmere ist.

---

## Der VDOS Befehl |FORMAT

**Formatieren einer Diskette**

Bevor Sie mit einer neuen Diskette arbeiten können, muß diese erst einmal dafür vorbereitet werden. Das kann man sich so vorstellen, daß auf der neuen leeren Diskettenscheibe überhaupt nichts steht, sie ist vollkommen homogen. Damit das Laufwerk (und natürlich auch VDOS) mit dieser Diskette etwas anfangen kann, muß auf die Diskette eine Grundstruktur aufgeschrieben werden.

Diese Grundstruktur besteht aus einer bestimmten Anzahl von Spuren (Tracks) und Sektoren (Sectors). Für Spur könnte man auch Kreislinie sagen. Es werden auf der Vor- und der Rückseite einer vortex Diskette jeweils 80 Spuren zu je 9 Sektoren markiert. Außerdem werden alle Bereiche zwischen den Markierungen mit einem bestimmten Wert beschrieben. Man sagt auch: die Diskette wird formatiert.

Überlegen wir uns gleich, was passiert, wenn wir eine bereits beschriebene Diskette formatieren. Aufgrund der Tatsache, daß beim Formatieren nicht nur die Markierungen geschrieben werden, sondern auch die Bereiche zwischen den Markierungen "gefüllt" werden, hat das natürlich einen katastrophalen Einfluß auf dort eventuell stehende Daten: sie werden alle samt und sonders gelöscht. Also Vorsicht!

> **(!) Wichtig:** Das Formatieren löscht alle Daten auf der Diskette!

Legen Sie einmal in Ihr vortex X-Laufwerk eine verpackungsneue Diskette ein. Formatiert wird mit Hilfe des VDOS Befehls `|FORMAT`. Geben Sie einmal dies hier ein:

```
|FORMAT,2<ENTER>

Laufwerk B: Diskette eingelegt J/N ?
J

Init-Seite 1 Spur 79
Ready
```

Damit ist diese Diskette formatiert. Geben Sie nun einmal

```
|B<ENTER>
|DIR<ENTER>

Laufwerk B: User 0

4K belegt, 0 Dateien, 704K frei
Ready
```

Wie Sie sehen, ist die Diskette vollkommen leer ("0 Dateien").

Geben Sie nun einmal folgendes ein:

```
|A<ENTER>
|FORMAT,1<ENTER>
FORMAT (S,D) ? S
Laufwerk A: Diskette eingelegt J/N ?
J
Init-Seite 0 Spur 39
Ready
```

Hiermit wird die 3"-Diskette im Laufwerk A (dem 3"-Laufwerk) formatiert. Wie Sie sehen, kann man hier noch zwischen zwei Formaten wählen (S/D): System- und Datenformat.

Grundsätzlich wird Ihnen dann die Frage `FORMAT (S,D) ?` gestellt, wenn Sie mit `|FORMAT,1<ENTER>` oder `|FORMAT,2<ENTER>` auf das 3"-Laufwerk "treffen". `|FORMAT,2<ENTER>` "trifft" dann auf das 3"-Laufwerk, wenn Sie zuvor Laufwerk A und Laufwerk B mit dem VDOS Befehl `|X` vertauscht haben, so daß dann Laufwerk A das vortex X-Laufwerk und Laufwerk B das 3"-Laufwerk ist.

Geben Sie "S" ein, dann wird die 3"-Diskette mit 40 Spuren zu je 9 Sektoren formatiert (Sektornummern `41H`–`49H`). Dieses Format ist identisch mit dem "Systemformat" und dem "Vendorformat". Beide Formate haben zwei reservierte Spuren, aber nur das Systemformat enthält das CP/M Betriebssystem. Das Vendorformat ist für den Fall vorgesehen, daß Sie z.B. eigenentwickelte CP/M Software auf der 3"-Diskette verkaufen wollen. Selbstverständlich können Sie diese Disketten nicht mit dem CP/M ausliefern, deshalb kopieren Sie Ihre Software auf eine im Vendorformat ("VerkaufsfORMAT") formatierte Diskette, die zwar die zwei Spuren enthält, die das CP/M aufnehmen können, das CP/M selbst fehlt aber. Ihr Kunde kann sich sehr einfach (z.B. mit `BOOTGEN` und `SYSGEN`) "sein" CP/M auf diese Diskette kopieren.

Geben Sie "D" ein, dann wird die Diskette im DATA-Only Format formatiert. Dieses Format hat 40 Spuren zu je 9 Sektoren, aber keine reservierten Spuren, kann also nie ein CP/M Betriebssystem enthalten. Die Sektornummerierung ist `C1H`–`C9H`. Eine im DATA-Only Format formatierte Diskette hat wegen der fehlenden Systemspuren eine etwas höhere Speicherkapazität als eine im System-/Vendor-Format formatierte Diskette.

Es sei hier noch bemerkt, daß Disketten auch unter CP/M formatiert werden können. Dort steht dafür das Programm `DISKTOOL` zur Verfügung.

---

## Starten und Sichern eines BASIC-Programms

Wenn Sie Ihren CPC mit angeschlossenem vortex X-Laufwerk einschalten, dann bekommen Sie unter anderem folgende Meldung:

```
(C)1985 VDOS 2.0-X by vortex GmbH

Ready
```

Sie zeigt uns, daß das X-Laufwerk arbeitet, VDOS 2.0 vorhanden ist und der CPC auf eine Eingabe von uns wartet (signalisiert durch "Ready"). Ich will Ihnen hier kurz zeigen – Sie sollten das eigentlich schon wissen –, wie Sie ein BASIC-Programm sichern, d.h. auf Diskette schreiben, und wie Sie es wieder laden und starten können.

Geben Sie einfach einmal das folgende kleine Programm ein:

```basic
10 MODE 2
20 PRINT "* Dies ist ein Test-Programm *"
30 FOR A=1 TO 10
40 PRINT A
50 NEXT A
60 PRINT "* Das war's ... *"
70 END
```

Wenn Sie jetzt den Computer ausschalten, ist alles weg. Hier macht das nichts, dies ist sowieso nur ein Test-Programm ohne eigentlichen Sinn. Wenn Sie aber ein ganzes Wochenende lang ein Programm "ausgebrütet", es nie gesichert haben und dann den Rechner ausschalten, dann beginnt vermutlich die Suche nach den Schuldigen…

Deshalb sichern wir das Programm auf Diskette weg. Es kann dann von dort jederzeit wieder geladen werden, auch wenn Sie den Rechner dazwischen ein-/ausschalten. Wir überlegen uns einen simplen Namen für unser kleines Programm: wie wär's mit `TEST`? Bevor wir aber ans Sichern gehen, müssen wir erst einmal eine Diskette haben, auf die wir sichern können.

Holen Sie eine ganz neue (verpackungsneue) Diskette her; sie muß noch, wie beim Befehl `|FORMAT` beschrieben, formatiert werden. Legen Sie die Diskette ins vortex X-Laufwerk ein und geben Sie noch `|X<ENTER>` ein (damit ist Laufwerk A das X-Laufwerk und Laufwerk B das 3"-Laufwerk). Jetzt können wir unser kleines Programm auf die Diskette speichern. Sie müssen natürlich nicht jedes Mal eine neue Diskette anlegen!

Geben Sie dazu folgendes ein:

```
SAVE "TEST"<ENTER>
```

Das Laufwerk wird angehen, das kleine Programm wird gespeichert und schon fertig. Geben Sie jetzt einmal dieses ein:

```
CAT<ENTER>

Laufwerk A: User 0

TEST    .BAS  1K

1K belegt, 1 Dateien, 700K frei
```

Auf der Diskette finden wir unser `TEST` Programm wieder. Geben Sie nun zum "Beweis" dies hier ein:

```
NEW<ENTER>
LIST<ENTER>

Ready
```

Ja, wir haben unser Programm gelöscht! Keine Angst, wir haben es gesichert. Holen Sie es wieder mit folgender Zeile "herein":

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

Jawohl, es ist wieder da! Jetzt starten wir das Programm mit `RUN<ENTER>`. Der Bildschirm wird gelöscht und dann werden im wesentlichen die Zahlen 1 bis 10 ausgegeben, nichts Tolles, nur etwas zur Demonstration. Sie hätten auch direkt `RUN "TEST"<ENTER>` eingeben können. Dann wäre die Datei `TEST.BAS` von der Diskette geladen und sofort gestartet worden.

Noch ein paar Worte zum `SAVE` Befehl. Es gibt eigentlich 4 Möglichkeiten, diesen Befehl zu verwenden:

1. `SAVE "DATEI"<ENTER>`
2. `SAVE "DATEI",A<ENTER>`
3. `SAVE "DATEI",P<ENTER>`
4. `SAVE "BILD",B,&C000,&4000<ENTER>`

Die erste Variante haben wir bereits oben verstanden. Das Programm wird hier in einer "komprimierten Form", die wenig Diskettenspeicherplatz benötigt, abgespeichert.

Mit der zweiten Möglichkeit wird eine sogenannte ASCII-Datei angelegt. Das ist eine reine Text-Datei, die keinerlei Sonderzeichen etc. enthält. Das Programm wird tatsächlich so abgelegt, wie wir es aufgelistet auf dem Bildschirm sehen.

Bei der dritten Möglichkeit wird das Programm "protected" (geschützt) gespeichert. Es ist nicht mehr "LISTbar".

Die letzte Möglichkeit beinhaltet folgendes: Alle Daten, die im Speicher zwischen Adresse `&C000` und `&FFFF` (= `&C000` + `&4000`) stehen (das ist der Bildschirminhalt), werden in der Datei `BILD.BIN` (BIN steht für Binär) abgelegt.

---

## Was ist überhaupt eine Datei?

Sie wissen das nicht? Macht nichts, ich werde es Ihnen kurz erklären. Stellen Sie sich vor, Sie haben in Ihrem Büro einen Aktenschrank stehen, in dem sich eine ganze Reihe Ordner ("Leitzer") befinden. In jedem Ordner sind die Papiere für einen bestimmten Vorgang eingeheftet. Ist das nicht so, dann haben Sie eine desolate Aktenablage!

So und jetzt die Analogie: Der Aktenschrank ist die Diskette, die Ordner sind die Dateien und die Papiere sind die Daten, die in einer Datei gespeichert sind. Wie Sie jedem Ordner zur leichteren Wiederauffindbarkeit eine Aufschrift geben, bekommt auch jede Datei eine Bezeichnung. Datei heißt im Englischen übrigens "FILE".

Die Dateibezeichnung unterliegt gewissen Einschränkungen: eine Bezeichnung wie z.B. "Dies ist meine erste Datei" ist nicht zulässig. Die Dateibezeichnung, die von VDOS (übrigens auch CP/M) anerkannt wird, ist:

```
Dateiname.Dateityp
```

Der Dateiname kann bis zu 8 Zeichen lang sein, für Dateityp sind maximal 3 Zeichen zugelassen. Der Punkt zwischen Name und Typ ist zwingend.

Sie können in einer Dateibezeichnung alle Zeichen außer den folgenden verwenden:

```
< > . ; : = ? * [ ] % ! ( ) / \
```

Der Dateityp gibt oft einen gewissen Aufschluß über den Inhalt der Datei. Beispiele für Dateibezeichnungen sind z.B.: `TEST.BAS`, `SPIELE`, `BILD.BIN`, `PROGRAMM.BAS`.

Unter BASIC treffen Sie meistens folgende Dateitypen (im Englischen sagt man dazu auch *Extension*) an:

- **BAS** – Dies ist ein BASIC-Programm, das mit `RUN` gestartet oder mit `LOAD` geladen werden kann, z.B. `SPIEL.BAS` oder `PROGRAMM.BAS`.

- **BAK** – Sicherheits-Datei oder BACKUP-Datei. Wenn Sie ein BASIC-Programm mit `SAVE` abspeichern wollen, "schaut" VDOS auf der Diskette nach, ob dort bereits eine Datei mit der von Ihnen gewählten Bezeichnung existiert. Ist eine vorhanden, dann wird ihr Typ gegen `BAK` ausgetauscht (vorher `BAS`). Die Datei, die Sie aber eigentlich speichern wollten, erhält den Typ `BAS`. Z.B.

  ```
  SAVE "TEST"<ENTER>
  ```

  Diese Datei wird mit der Bezeichnung `TEST.BAS` auf der Diskette abgelegt. Dort gibt es aber bereits eine Datei, die `TEST.BAS` heißt. VDOS benennt sie einfach in `TEST.BAK` um. Es kann Ihnen also nicht passieren, daß Sie aus Versehen eine Datei löschen.

- **BIN** – `BIN` steht für "Binär". Der Inhalt einer BIN-Datei kann z.B. ein komplettes Bildschirm-Abbild oder auch ein Maschinenprogramm sein. Eine Datei dieses Typs wird z.B. durch den folgenden `SAVE`-Befehl angelegt:

  ```
  SAVE "BILD",B,&C000,&4000<ENTER>
  ```

  Auf der Diskette finden wir die Datei `BILD.BIN`. Das "B" nach `"BILD"` erzwingt das Anlegen einer Binär-Datei.

Soll eine Datei geladen werden und man gibt beim Ladebefehl keinen Dateityp an, so wird nach der Suchreihenfolge `' '`, `'BAS'`, `'BIN'`, `'BAK'` die erste gefundene Datei mit dem angegebenen Dateinamen geladen.

---

## Die VDOS Befehle |A und |B

**Umschalten zwischen Laufwerken**

Unter VDOS stehen Ihnen maximal zwei Laufwerke zur Verfügung. Wir haben sie "Laufwerk A" und "Laufwerk B" getauft (einfacher nur A und B). Das Besondere bei Ihrem Set ist es, daß Sie Laufwerke unterschiedlichen Formats (3" und 5,25" oder 3" und 3,5") mit verschiedenen Kapazitäten (ca. 170 KB und 708 KB) haben.

Nach dem Einschalten des CPC's und des X-Laufwerks ist Laufwerk A das 3"-Laufwerk und Laufwerk B das X-Laufwerk.

Eingegebene Befehle beziehen sich nun auf Laufwerk A, das 3"-Laufwerk:

```
|DIR<ENTER>

Laufwerk A: User 0

TEST    .BAS    TEST    .BIN
PROGRAMM.BAS    TEST    .BAK

100K belegt, 4 Dateien, 69K frei
```

Möchten wir z.B. sehen, was sich auf der Diskette im X-Laufwerk befindet, dann müssen wir erst einmal auf dieses "umschalten":

```
|B<ENTER>
```

Eingegebene Befehle "wirken" nun auf Laufwerk B, dem X-Laufwerk:

```
|DIR<ENTER>

Laufwerk B: User 0

PIP     .COM    M80     .COM    VDOS    .MAC
STAT    .COM    L80     .COM    WS      .COM
WSMSGS  .OVR    WSOVLY1 .COM

304K belegt, 8 Dateien, 400K frei
```

Sie sehen, daß wir hier wesentlich mehr Speicherplatz zur Verfügung haben.

So schalten wir wieder auf das 3"-Laufwerk zurück:

```
|A<ENTER>
```

Wir können uns z.B. folgendes kleine Programmchen vorstellen:

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

Wenn Sie dieses Programm gestartet haben (durch `RUN`), dann wird der Bildschirm gelöscht und nacheinander werden die Inhaltsverzeichnisse der Disketten in Laufwerk A (3"-Diskette) und Laufwerk B (3,5"- oder 5,25"-Diskette), jeweils von dem kleinen Text begleitet, ausgegeben. Zum Schluss wird dann wieder auf Laufwerk A umgeschaltet (Zeile 70).

Wenn Sie nicht wissen, was `MODE 2`, `PRINT` und `END` bedeutet, dann sollten Sie, bevor Sie hier überhaupt weiter lesen, erst einmal das BASIC Handbuch hernehmen, das Sie mit Ihrem CPC erhalten haben, und dort "gewisse" Grundkenntnisse sammeln!

---

## Der VDOS Befehl |X

**Vertauschen von Laufwerk A und B**

Schalten Sie alle Geräte ein, legen ins 3"-Laufwerk und ins vortex X-Laufwerk eine Diskette ein, geben nun `CAT<ENTER>` ein, dann erhalten Sie das Inhaltsverzeichnis der 3"-Diskette. Geben Sie `|B<ENTER>` und `CAT<ENTER>` ein, dann erhalten Sie das Inhaltsverzeichnis der Diskette im vortex X-Laufwerk.

Der Einschaltzustand des CPC's und des X-Laufwerks ist also:

- Laufwerk A -> 3"-Laufwerk (eingebaut bei CPC664 und CPC6128, extern bei DDI-1 am CPC464)
- Laufwerk B -> vortex Laufwerk (5,25" bei F1-X und 3,5" bei M1-X)

Geben Sie aber nun

```
|X<ENTER>
```

ein, dann vertauschen ("exchangen") Sie Laufwerk A mit Laufwerk B. D.h. es ergibt sich die neue Zuordnung:

- Laufwerk A -> vortex Laufwerk (5,25" bei F1-X und 3,5" bei M1-X)
- Laufwerk B -> 3"-Laufwerk (eingebaut bei CPC664 und CPC6128, extern bei DDI-1 am CPC464)

Schalten Sie nun wieder auf A um (wir haben oben ja auf B umgeschaltet), indem Sie `|A<ENTER>` eingeben. Starten Sie nun `CAT<ENTER>` und Sie bekommen das Inhaltsverzeichnis der Diskette in dem vortex X-Laufwerk (jetzt Laufwerk A).

Setzen Sie den Rechner zurück – um einen eindeutigen Ausgangszustand zu haben –, indem Sie gleichzeitig die `CTRL`+`SHIFT`+`ESC`-Tasten drücken.

Legen Sie ins 3"-Laufwerk eine 3"-Diskette und ins X-Laufwerk eine 5,25"-/3,5"-Diskette ein. Beide Disketten sollen bereits einen Inhalt haben. Schauen Sie sich nun einmal dieses kleine Programm hier an:

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

> **(!) Wichtig**
>
> Starten Sie CP/M, oder setzen Sie den Rechner zurück (gleichzeitiges Drücken der `CTRL`+`SHIFT`+`ESC`-Tasten, Aus-/Einschalten des Rechners), so ist Laufwerk A wieder das 3"-Laufwerk und Laufwerk B das X-Laufwerk. D.h. die Laufwerkskonfiguration unter CP/M wird beim Laden (Booten) des CP/M's festgelegt.

---

## Die VDOS Befehle CAT und |DIR

**Anschauen des Disketteninhaltsverzeichnisses**

Wie wir in jedem Buch ein Inhaltsverzeichnis finden, in dem alle Kapitel aufgelistet sind, besitzt auch jede Diskette ein Inhaltsverzeichnis, in dem alle Dateien aufgeführt sind, die sich auf dieser Diskette befinden. Anstatt Inhaltsverzeichnis wird meistens das englische Wort "Directory" verwendet. Oftmals findet man auch das englische Wort "Catalog".

Unter VDOS gibt es zwei Befehle, mit denen das Inhaltsverzeichnis auf dem Bildschirm ausgegeben werden kann. Den einen Befehl haben wir vorhin schon des öfteren verwendet, es ist der `|DIR` Befehl (abgeleitet von DIRectory). Der andere Befehl heißt `CAT` (von CAtalog kommend) und weist eine kleine Besonderheit auf: Man benötigt nicht den senkrechten Strich `|`, um ihn zu verwenden. Das liegt ganz einfach daran, daß Sie diesen Befehl auch ohne vortex X-Laufwerk in Ihrem CPC finden, und wie schon erwähnt, brauchen nur externe Befehle (Befehle, die durch das Anstecken der Floppy oder auch andere Peripherie hinzukommen) den senkrechten Strich.

Der einfachere der beiden Befehle ist `CAT`. Hier seine Anwendung:

```
CAT<ENTER>

Laufwerk A: User 0

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
228K belegt, 17 Dateien, 480K frei
Ready
```

Das ist z.B. der Inhalt meiner WordStar Arbeitsdiskette. Wir bekommen Informationen über die Größe der einzelnen Dateien, wieviele Dateien sich auf der Diskette befinden und wieviel Speicherplatz noch frei bzw. schon verbraucht ist. Außerdem sind die Dateien alphabetisch geordnet.

Hier noch ein wichtiger Hinweis: Mit dem vortex X-Laufwerk können maximal 128 Dateien pro Diskette angelegt werden. Bei einem 3"-Laufwerk sind es nur 64.

> **(!) Hinweis:** Auf der vortex Floppy sind 128 Einträge ins Inhaltsverzeichnis möglich. Auf der 3"-Floppy nur 64!

`CAT` ist also ein einfacher Befehl, mit dem schnell wichtige Informationen gewonnen werden können. Eine wichtige Eigenschaft fehlt aber diesem Befehl: das "Herausfiltern" ganz bestimmter Dateien.

Hier wird der `|DIR` Befehl interessant. Im Zusammenhang mit dieser Eigenschaft muß ich Ihnen kurz die Bedeutung des Begriffs **Wildcard** erklären:

Es wird vielleicht des öfteren vorkommen, daß Sie ein und dieselbe Diskette für BASIC/VDOS und CP/M benutzen. Es gibt also Dateien auf dieser Diskette, mit denen Sie unter CP/M nichts anfangen, und umgekehrt. Weiter oben habe ich Ihnen gezeigt, daß z.B. Dateien des Typs `BIN` typisch für BASIC sind, wohingegen eine Datei mit dem Typ `COM` eine typische CP/M Datei ist. Es wäre doch nun sehr vorteilhaft, wenn wir unter BASIC die Diskette nur auf Dateien des Typs `BIN` "absuchen" könnten. D.h. es sollen uns nur diese Dateien gezeigt werden.

Wir brauchen also einen Befehl, mit dem es möglich ist, selektiv bestimmte Dateien oder Gruppen von Dateien auszugeben. Genau für diese Aufgaben haben wir den Befehl `|DIR`. Hier eine Anwendung:

```
|DIR,"*.COM"<ENTER>

Laufwerk A: User 0

FAST    .COM    PIP     .COM
STAT    .COM    WS192N  .COM

228K belegt, 4 Dateien, 480K frei
```

Alle Dateien vom Typ `COM` wurden angezeigt.

```
|DIR,"MAN.*"<ENTER>

Laufwerk A: User 0

MAN     .003    MAN     .004
MAN     .006    MAN     .005
MAN     .007    MAN     .BAK

228K belegt, 6 Dateien, 480K frei
```

Es wurden uns alle Dateien mit dem Dateinamen "MAN" angezeigt.

```
|DIR,"MAN.00?"<ENTER>

MAN     .003    MAN     .004
MAN     .006    MAN     .005
MAN     .007

228K belegt, 5 Dateien, 480K frei
```

Hier sind nur die Dateien ausgegeben worden, deren Dateiname `MAN` ist und deren Typ 3 Zeichen lang ist, wobei die ersten beiden Zeichen "00" sein müssen und das 3. Zeichen beliebig, aber vorhanden sein muß (eine Datei `MAN.00` wäre nicht angezeigt worden).

Die beiden Zeichen `*` und `?` sind sogenannte Wildcardzeichen.

- Ein `?` läßt nur immer das Zeichen, an dessen Stelle es steht, für beliebig zu (es muß aber vorhanden sein).
- Ein Stern `*` läßt immer alle verbleibenden Zeichen als beliebig zu.

Der Unterschied beider Zeichen wird auch durch folgende Gleichung (nicht mathematisch!) demonstriert:

```
????????.??? = *.*
```

Wie Sie sicherlich bemerkt haben, kommt bei `CAT` und `|DIR` in der ersten Zeile immer die Meldung:

```
Laufwerk A: User 0
```

Was hat es damit auf sich? Ganz einfach: Durch die Angabe `Laufwerk A` wird uns angezeigt, daß hier ein Inhaltsverzeichnis von der Diskette in Laufwerk A ausgegeben wird. Es ist eines von 16 möglichen Inhaltsverzeichnissen. Bei der Entwicklung von VDOS ist daran gedacht worden, daß sich unter Umständen mehrere Benutzer eine einzige Diskette teilen müssen. Damit hier kein Durcheinander entsteht (wem gehört welche Datei), kann die Diskette in bis zu 16 Benutzer-Bereiche (USER-Bereiche) unterteilt werden (siehe dazu den `|SELECT` Befehl). Es ist aber zu beachten, daß die Summe aller Dateien – aus allen USER-Bereichen – nie größer als 128 sein darf und daß die Summe aller Größen der Dateien nie 704 KB überschreitet. In beiden Fällen ist nämlich die Diskette voll.

Beim 3"-Laufwerk darf die Summe aller Dateien 64 nicht überschreiten. Die Summe aller Dateigrößen muß kleiner gleich 169 KB bleiben.

---

## Der VDOS Befehl |ATTRIBUT

**Schützen einer Datei / "Unsichtbarmachen" einer Datei**

Die Möglichkeit, eine ganze Diskette vor dem "Beschreiben" zu schützen, ist Ihnen sicherlich bekannt (Löschen ist auch Schreiben!). Es ist ein mechanischer Schutz: bei einer 5,25"-Diskette einfach durch einen kleinen Aufkleber um die Kante herum, bei 3"- und 3,5"-Disketten durch einen kleinen Riegel an der Diskette selbst.

Wenn Sie aber gezielt irgendeine Datei schreibschützen wollen, dann brauchen Sie dazu den VDOS Befehl `|ATTRIBUT`. Dieser Befehl ist in der Lage, Dateien mit einem sogenannten **Attribut** zu versehen. Das Attribut gibt uns Informationen über den "Zustand" der Datei. VDOS unterscheidet folgende übliche Attribute:

| Attribut | Bedeutung |
|----------|-----------|
| **S** | Die Datei ist eine sogenannte "SYS"- oder "System"-Datei. Sie wird bei der Eingabe der Befehle `CAT` und `|DIR` nicht mehr angezeigt, sie ist "unsichtbar". |
| **D** | Die Datei ist eine sogenannte "DIR"- oder "Directory"-Datei. Sie wird bei den Befehlen `CAT` und `|DIR` angezeigt. Wenn Sie an den Dateiattributen nichts ändern, dann haben alle Dateien dieses Attribut und das folgende. |
| **W** | Die Datei ist R/W (read/write), also schreib-/lesbar. Sie kann auch gelöscht werden. |
| **R** | Die Datei ist R/O (read only), schreibgeschützt. Sie kann also auch nicht gelöscht werden. |

Wie schon erwähnt, sind alle Dateien in ihrem "Urzustand" (ohne daß Sie etwas daran geändert haben!) mit den beiden Attributen "D" und "W" versehen.

Der `|ATTRIBUT` Befehl wird wie folgt angewendet:

```
|ATTRIBUT,"PIP.COM","R"<ENTER>
```

Die Datei `PIP.COM` wird als "nur lesbar" markiert. Sie kann also auch nicht mehr gelöscht werden. Schauen wir uns mit `CAT` einmal die Diskette an, so sehen wir, daß diese Datei markiert wurde.

```
CAT<ENTER>

Laufwerk A: User 0
```

| Datei      | Größe | Datei       | Größe |
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
228K belegt, 17 Dateien, 480K frei
Ready
```

Alle mit `#` markierten Dateien sind schreibgeschützt.

Greifen wir ein wenig vor: versuchen Sie einmal die Datei `PIP.COM` zu löschen, indem Sie folgende Zeile eingeben:

```
|ERA,"PIP.COM"<ENTER>

PIP    .COM nur lesbar

Ready
```

Sie sehen, diese Datei läßt sich so nicht löschen.

> **(!) Hinweis:** Bitte sind Sie sich aber im Klaren darüber, daß dieser "Schutz" natürlich bei der Anwendung des `|FORMAT` Befehls wirkungslos ist. Hier wird rigoros alles vernichtet, was auf der Diskette steht!

Man kann dieses Attribut natürlich auch wieder rückgängig machen:

```
|ATTRIBUT,"PIP.COM","W"<ENTER>
```

Die Datei kann jetzt auch wieder gelöscht werden.

---

## Der VDOS Befehl |ERA

**Löschen einer Datei**

Mit diesem Befehl können Dateien, Gruppen von Dateien oder aber auch ganze Disketten gelöscht werden. Dieser Befehl bezieht sich immer auf den gerade eingestellten USER-Bereich (siehe `|SELECT`). ERA ist von "Erase" abgeleitet (heißt auf Deutsch: löschen).

Mit folgender Zeile

```
|ERA,"TEST.BAS"<ENTER>
```

wird die Datei `TEST.BAS` von der gerade eingelegten Diskette heruntergelöscht. Wäre sie mit dem "R"-Attribut versehen gewesen, dann hätten wir sie nicht löschen können. Gibt es diese Datei auf dieser Diskette gar nicht, dann meldet uns VDOS:

```
TEST    .BAS wurde nicht gefunden
```

Mit dieser Zeile hier

```
|ERA,"TEST.*"<ENTER>
```

werden im momentanen USER-Bereich auf dieser Diskette alle Dateien (z.B. `TEST.BAS`, `TEST`, `TEST.COM`, `TEST.123`, `TEST.12`) gelöscht. Es kann neben diesem Wildcardzeichen `*` auch das andere `?` verwendet werden.

Die folgende Zeile sollte nur bei äußerstem Bewußtsein eingegeben werden, sie veranlaßt nämlich die Komplett-Löschung der Diskette:

```
|ERA,"*.*"<ENTER>
```

Auf dieses Wildcard (`*.*`) "passen" alle Dateien, also werden auch alle gelöscht. Also hier bitte immer vorsichtig. Die Fälle, wo Sie ganze Disketten löschen müssen, sind sicherlich auch sehr selten.

> **(!) Wichtig: VORSICHT!**
>
> Mit `|ERA,"*.*"<ENTER>` wird die ganze Diskette gelöscht!

Denkbar wäre auch folgendes:

```
|B<ENTER>
|ERA,"A:PIP.COM"<ENTER>
```

Damit haben wir zuerst auf Laufwerk B umgeschaltet und von dort aus dann auf der Diskette in A die Datei `PIP.COM` gelöscht.

---

## Der VDOS Befehl |REN

**Ändern einer Dateibezeichnung**

Es kommt sicherlich einmal vor, daß Ihnen ein bereits vergebener Dateiname nicht mehr gefällt, oder Sie ihn irgendwo anders brauchen. Um die Dateibezeichnung ändern zu können, haben wir den Befehl `|REN` (REN steht für Rename: Umbenennen). Hier sind keine Wildcards zulässig, weil nicht sinnvoll.

```
|REN,"DATEI.NEU","DATEI.ALT"<ENTER>
```

Die Datei mit der Bezeichnung `DATEI.ALT` wird in die Datei `DATEI.NEU` umbenannt. Existiert bereits eine Datei mit der Bezeichnung `DATEI.NEU`, dann wird der Befehl abgebrochen und VDOS meldet uns:

```
DATEI   .NEU existiert bereits
```

Sie müssen diese Datei erst löschen oder irgendwo anders hin kopieren. Gibt es die Datei `DATEI.ALT` nicht, dann gibt uns VDOS dies aus:

```
DATEI   .ALT wurde nicht gefunden
```

Folgende Zeile

```
|REN,"B:TEST.123","B:SPIEL.BAS"<ENTER>
```

benennt von Laufwerk A aus die Datei `SPIEL.BAS`, befindlich auf der Diskette in B, in die Datei `TEST.123`, auch auf B, um.

> **(!) Hinweis:** Beachten Sie, daß ein Umbenennen nur immer auf ein und derselben Diskette erfolgen kann. Eine Zeile, wie z.B. `|REN,"A:DDT.COM","B:SID.COM"<ENTER>` würde keinen Sinn machen.

---

## Der VDOS Befehl |SELECT

**Einstellen der USER-Bereiche**

Die Diskette kann unter VDOS (übrigens auch unter CP/M) in bis zu 16 Benutzerbereiche unterteilt werden. Die Unterteilung kann dann sinnvoll werden, wenn mehrere Benutzer eine Diskette gemeinsam benutzen und man sich nicht ins Gehege kommen will. Man kann sich aber natürlich auch als einziger Benutzer dieser Diskette mehrere USER-Bereiche einrichten. Es ist so möglich, eine saubere Struktur in die Diskette hineinzubekommen. Üblicherweise wird man aber diesen Befehl wenig benutzen und sich auf USER-Bereich 0 beschränken.

Folgende Zeile

```
|SELECT,"6"<ENTER>
```

schaltet auf USER-Bereich 6 um. Geben wir jetzt ein `CAT` ein, dann bringt dieses in seiner obersten Zeile die Information:

```
Laufwerk A: User 6
```

und listet uns dann die Dateien, die sich in diesem USER-Bereich befinden, auf dem Bildschirm auf.

Außerdem kann neben der USER-Nummer auch noch die Laufwerkskennung (A oder B) mit angegeben werden.

```
|SELECT,"B5"<ENTER>
```

schaltet in USER-Bereich 5 auf Laufwerk B um.

Geben wir jetzt z.B.

```
CAT<ENTER>
```

ein, dann erhalten wir als erste Zeile des "Catalogs":

```
Laufwerk B: User 5
```

Macht man hier von der Schreibweise mit dem "Klammeraffen" `@` Gebrauch, dann kann innerhalb eines BASIC-Programms die USER-Nummer und die Laufwerkskennung "dynamisch" angegeben werden:

```basic
10 INPUT "Laufwerkskennung ",A$
20 INPUT "USER-Nummer ",B$
30 C$=B$+A$
40 |SELECT,@C$
50 CAT
```

Abhängig von der eingegebenen Laufwerkskennung und der USER-Nummer erhalten wir das Inhaltsverzeichnis des entsprechenden Bereichs auf der entsprechenden Diskette.

---

## Der VDOS Befehl |RESET

**Wechseln von Disketten**

Stellen Sie sich vor, Sie haben eine Datei zum Schreiben geöffnet, und es werden von Zeit zu Zeit Daten in diese Datei hineingeschrieben. Wenn Sie jetzt zwischendurch die Diskette tauschen, dann kann das, weil die Datei noch "offen" ist, zu Datenverlust führen.

Dieser Befehl dient dazu, VDOS mitzuteilen, daß Sie in ein und demselben Laufwerk während einer Schreiboperation die Diskette gewechselt haben.

Sie sollten sich angewöhnen, vor dem Wechsel der Diskette diesen Befehl einzugeben, vor allem dann, wenn Sie sich nicht sicher sind, ob noch eine Datei zum Schreiben offen ist. Sollte das der Fall sein und Sie vergessen `|RESET<ENTER>`, so können unter Umständen die letzten 64 KB Daten verlorengehen. Haben Sie vor dem Wechsel der Diskette die Datei ordnungsgemäß (`CLOSEOUT`, `|CLOSE`) geschlossen, so ist `|RESET` überflüssig.

Wenn Sie sich schon ein bisschen mit CP/M befaßt haben, dann erkennen Sie hier eine gewisse Verwandtschaft mit dem `CTRL`+`C` unter CP/M.

---

## Der VDOS Befehl |CODE

**Programmschutz!**

Vorher habe ich die Möglichkeit erwähnt, daß man ein Programm mit dem `SAVE`-Befehl und dem "P" (einfach P-Schutz) vor "Auflistung" schützen kann. Leider ist dieser Schutz (den Sie auch ohne vortex Floppy haben) recht wirkungslos geworden, weil man ihn schon frühzeitig "geknackt" hat. Prinzipiell kann man sagen: es gibt keinen Schutz, der nicht umgehbar wäre. Man kann diese Sache nur erschweren, aber nie aufhalten.

Mit dem VDOS Befehl `|CODE` können Sie einen persönlichen Programmschutz einbauen. Sie möchten z.B. das Programm `TEST.BAS` schützen:

Mit folgenden Zeilen

```
|CODE,12325<ENTER>
SAVE "TEST",P<ENTER>
```

haben Sie `TEST` mit einem persönlichen Codierschlüssel versehen (12325). Geben Sie nun `|CODE,0<ENTER>` ein. Damit oder auch durch das Rücksetzen des Rechners (`CTRL`+`SHIFT`+`ESC` gleichzeitig drücken) aktivieren Sie den Schutz.

Geben Sie nun `RUN "TEST"<ENTER>` ein. Es kommt ein vollkommener Unsinn dabei heraus, der "Schlüssel" wurde nicht angegeben. Geben Sie deshalb `|CODE,12325<ENTER>` ein und starten Sie `TEST` erneut. Alles klappt!

Die Zahl beim `|CODE`-Befehl muß zwischen `-32768` und `32767` liegen, das sind dann immerhin 65536 Möglichkeiten, Ihr Programm zu schützen.

---

## Der VDOS Befehl |AMSDOS

**Einschalten des AMSDOS Betriebssystems**

Durch die Eingabe `|AMSDOS<ENTER>` wird VDOS abgeschaltet und gleichzeitig AMSDOS eingeschaltet. Besitzen Sie Programme, die ohne Anpassung unter VDOS nicht arbeiten, so können Sie auf AMSDOS umschalten und alle Probleme sind beseitigt.

Haben Sie auf AMSDOS umgeschaltet, dann ist es so, als hätten Sie ein simples Zweitlaufwerk an Ihren CPC angeschlossen.

Dieser Befehl führt einen RESET aus. D.h. alle Daten, die zuvor im Speicher waren, werden gelöscht!

> **(!) Wichtig:** `|AMSDOS<ENTER>` löscht alle Daten im Speicher.

Wenn Sie auf AMSDOS umgeschaltet haben, ist zu beachten, daß das X-Laufwerk dann keine 708 KB, sondern nur 169 KB (wie das 3"-Laufwerk) formatierte Speicherkapazität hat. Das liegt daran, daß AMSDOS nur Laufwerke mit 40 Spuren und einem Schreib-/Lesekopf verwalten kann (daraus ergibt sich auch die Speicherkapazität von ca. 170 KB).

Alle X-Laufwerke sind 80-Spur-Laufwerke mit zwei Schreib-/Leseköpfen. Unter AMSDOS wird die Diskette im X-Laufwerk nur einseitig und mit nur 40 Spuren bedient. Es ist hierbei aber zu beachten, daß die 40 Spuren nicht gleichmäßig über den Diskettenradius verteilt sind, sondern nur die äußere Hälfte benutzen. Es ist also so, als würde das Laufwerk 80 Spuren bearbeiten, aber nur die ersten 40 tatsächlich benutzen.

Wichtig ist, daß eine Diskette, die unter AMSDOS im X-Laufwerk erstellt wurde, nie unter VDOS im X-Laufwerk verwendet werden darf.

> **(!) Wichtig**
>
> Eine Diskette, die unter VDOS erstellt wurde, darf auf keinen Fall unter AMSDOS verwendet werden. Eine Diskette, die unter AMSDOS erstellt wurde, darf umgekehrt auch auf keinen Fall unter VDOS eingesetzt werden.
>
> Beachten Sie dies nicht, so wird der Inhalt der entsprechenden Disketten unwiederbringlich vernichtet.

Durch das Rücksetzen des CPC's (gleichzeitiges Drücken der `CTRL`+`SHIFT`+`ESC`-Tasten) wird VDOS wieder eingeschaltet.

---

## Cassetten-Rekorder am CPC

Der erste der CPC's, der CPC464, ist standardmäßig mit einem Datenrekorder ausgerüstet, die anderen, der CPC664 und der CPC6128, können noch mit einem Datenrekorder nachgerüstet werden. Hat man zusätzlich noch ein Diskettenlaufwerk, dann ist es natürlich wichtig, daß man Daten zwischen Diskette und Cassette transferieren kann.

Es gibt bei den CPC's einen sogenannten Eingabe- und einen sogenannten Ausgabekanal zwischen dem Rechner und dem Massenspeicher (= Floppy oder Datenrekorder). Hat man eine Floppy angeschlossen und einen Datenrekorder und will man z.B. Daten von der Floppy auf den Rekorder bringen, dann muß man nur den Ausgabekanal auf den Rekorder legen und den Eingabekanal auf die Floppy.

Es sei erwähnt, daß nach dem Einschalten des CPC's mit angeschlossener Floppy Ein- und Ausgabekanal der Floppy zugewiesen sind, egal ob noch ein Datenrekorder vorhanden ist.

Es gibt genau sechs Möglichkeiten, die beiden Kanäle zu "verschalten". Für jeden Fall gibt es einen entsprechenden VDOS Befehl.

### Der VDOS Befehl |DISC

Ein- und Ausgabekanal sind der Diskettenstation zugeordnet. Dies ist der "Einschaltzustand" des CPC's mit angeschlossener Floppy. Werden Daten gelesen oder geschrieben, dann werden sie von der Floppy gelesen bzw. auf die Diskette in der Floppy geschrieben.

### Der VDOS Befehl |CAS

Ein- und Ausgabekanal sind dem Datenrekorder zugeordnet. Haben Sie einen CPC464 und schließen Sie die Floppy ab, dann entspricht das genau diesem Zustand. Schreib-/Leseoperationen beziehen sich immer auf den Rekorder.

Geben Sie hier z.B. einmal `|CAS<ENTER>` und `CAT<ENTER>` ein, dann kommt die Meldung `Press PLAY then any key`. Wir sollen also am Rekorder die Play-Taste drücken. Wir würden dann – falls vorhanden – von der Cassette im Rekorder ein Inhaltsverzeichnis erhalten. Daß das natürlich eine gewisse Zeit dauern wird, ist klar.

### Der VDOS Befehl |DISC.IN

Der Eingabekanal ist der Diskettenstation zugeordnet. D.h. werden jetzt Daten gelesen, dann kommen sie von der Floppy.

### Der VDOS Befehl |CAS.IN

Der Eingabekanal ist dem Rekorder zugeordnet. D.h. werden jetzt Daten gelesen, dann kommen sie vom Rekorder.

### Der VDOS Befehl |DISC.OUT

Der Ausgabekanal ist der Floppy zugeordnet. Wenn jetzt eine Schreiboperation erfolgt, dann werden diese Daten auf die Diskette im Laufwerk geschrieben.

### Der VDOS Befehl |CAS.OUT

Der Ausgabekanal ist dem Rekorder zugeordnet. Die Daten werden jetzt auf die Cassette im Rekorder geschrieben.

Möchten Sie z.B. eine Datei von Diskette auf Cassette kopieren, dann könnte das wie folgt aussehen:

```
|CAS.OUT<ENTER>
|DISC.IN<ENTER>
LOAD "TEST"<ENTER>
SAVE "TEST"<ENTER>
```

Der `LOAD` Befehl würde sich auf die Diskette und der `SAVE` Befehl auf die Cassette beziehen. Nach dem Drücken des letzten ENTER's würde dann folgendes gemeldet werden:

```
Press REC and PLAY then any key:
```

die Aufforderung, den Rekorder auf Schreibbetrieb einzustellen.

---

## Der VDOS Befehl |XMON – der vortex Z80-Monitor

Hinter diesem Befehl verbirgt sich ein sehr mächtiger und leistungsfähiger Z80 Maschinensprache-Monitor. **Monitor** hat nichts mit Bildschirm oder ähnlichem zu tun. Ein Monitor ist ein Programm, mit dessen Hilfe andere Maschinenprogramme getestet werden können. Man will damit die Fehler finden, die sich eventuell noch in diesem Maschinenprogramm befinden.

Für Fehler verwendet man hier auch gerne das englische Äquivalent "Bug" (= Wanze). Es hat sich deshalb auch der Name "Debugger" (Entwanzer) für einen Monitor eingebürgert.

Dann heißt es da noch "Z80". Warum, wissen Sie wahrscheinlich schon längst. Richtig, das liegt daran, daß in Ihrem CPC der Z80-Microprozessor eingebaut ist.

Die wesentlichen Funktionen des Monitors sind:

- Diskettenmonitor
- HEX/ASCII Dump
- Mnemonic Listing/Disassemblierung
- Breakpoints
- Tracer

Es muß ganz klar gesagt werden, daß der Monitor kein Spielzeug ist. Sie werden erst dann verstehen, zu was er gut ist und was er alles kann, wenn Sie sich zumindest ein bißchen in Z80 Maschinensprache eingearbeitet haben (hierzu empfehle ich das Buch von Rodnay Zaks "Der Z80", erschienen im Sybex Verlag).

Wissen Sie überhaupt gar nichts, dann sollten Sie vorerst die Finger von `|XMON` lassen. Eingeweihten brauche ich wohl erst gar nicht zu erklären, welche ungeahnten Möglichkeiten sich mit diesem "Tool" ergeben.

Gestartet wird der Monitor über die Eingabe

```
|XMON<ENTER>
```

Der Bildschirm wird gelöscht und es erscheint das Monitor-Bereitschaftszeichen (Prompt) `*`. XMON erwartet nun von uns Befehlseingaben.

Verlassen wird der Monitor durch das Drücken der `ESC`-Taste. Haben Sie z.B. den Monitor aus einem Programm heraus aufgerufen und verlassen Sie ihn wieder durch `<ESC>`, dann geht es in diesem Programm wieder genau an der Stelle weiter, wo zuvor der Monitor aufgerufen wurde.

Nachfolgend werden Ihnen in alphabetischer Reihenfolge alle Monitor-Befehle gezeigt. Zu beachten ist hierbei, daß geforderte oder angezeigte Werte grundsätzlich in hexadezimaler Form dargestellt werden, wobei 8-Bit-Werte zweistellig und 16-Bit-Werte vierstellig sind bzw. sein müssen.

### `Aadresse<ENTER>` – Textstring eingeben

```
*A3000<ENTER>
```

Ermöglicht die Eingabe eines ganzen Textstrings in den Speicher ab Adresse `3000H`:

```
*A3000,Dies ist ein Test String<ENTER>
```

Der String kann maximal 255 Zeichen enthalten.

### `@` – Diskettenmonitor starten

Das Zeichen `@` heißt "Klammeraffe" und wird durch das Drücken der entsprechenden Taste (liegt zwischen `P` und `[`) erzeugt. XMON verfügt über einen kleinen Diskettenmonitor. Aufgerufen wird er durch

```
*@
```

(kein `<ENTER>`) und meldet sich dann mit

```
L:00 T:00 S:41 B:A93E
>
```

Der `>` ist das Prompt des Diskettenmonitors. Die einzelnen Einträge in der Statuszeile haben folgende Bedeutung (Zahlenwerte werden hexadezimal angezeigt und müssen auch hexadezimal eingegeben werden):

| Eintrag | Bedeutung |
|---------|-----------|
| `L:xx` | Laufwerksnummer `xx=00` oder `01` für das logische Laufwerk A oder B. Beim Einsprung enthält `xx` die Nummer des augenblicklich angewählten Laufwerks. |
| `T:yy` | Spurnummer. Wertebereich `0..27H` (3"-Laufwerk), `0..9FH` (5,25"/3,5") |
| `S:zz` | Sektornummer. Wertebereich `41H..49H` oder `C1H..C9H` oder `01..08` beim 3"-Laufwerk, `01..09` beim 5,25"/3,5"-Laufwerk. Das Format einer 3"-Diskette wird beim R-Kommando (s.u.) automatisch erkannt und die Sektornummer entsprechend geändert. |
| `B:abcd` | Pufferadresse für Sektorschreiben/-lesen. Beim Diskmonitorstart steht hier die Adresse des BIOS Hostbuffers (siehe Intern-Teil). |

Hier nun die Erklärung der einzelnen Diskmonitorbefehle:

| Befehl | Funktion |
|--------|----------|
| `>Lxx<ENTER>` | Laufwerksnummer ändern |
| `>Sxx<ENTER>` | Sektornummer ändern |
| `>Txx<ENTER>` | Spurnummer ändern |
| `>Babcd<ENTER>` | Pufferadresse setzen |
| `>R` | Sektor mit den über L, S und T definierten Koordinaten in den Puffer einlesen |
| `>W` | Pufferinhalt in den Sektor mit den Koordinaten L, S und T schreiben |
| `>Cabcd<ENTER>` | Inhalt von Speicherstellen im Puffer ändern. Entspricht voll dem Monitorbefehl S (siehe auch dort). |
| `>Aabcd<ENTER>` | String eingeben (s.o.) |
| `>P` | Drucker ein-/ausschalten. Entspricht dem Monitorbefehl P |
| `>Dabcd<ENTER>/,xx<ENTER>/` | Pufferinhalt als HEX/ASCII Dump auf Bildschirm ausgeben. Optional kann auch noch die Anzahl der Sektoren angegeben werden, die insgesamt gedumpt werden sollen. |
| `><ESC>` | Rücksprung in den Monitor |

Alle Eingaben werden sowohl syntaktisch als auch logisch überprüft. Machen Sie einen Eingabefehler, so springt der Diskettenmonitor zurück auf seine Hauptkommandoschleife und meldet sich mit `>>`, um Ihnen den Fehler anzuzeigen – geändert wurde dann selbstverständlich nichts.

Tritt ein Diskettenfehler beim Lesen oder Schreiben auf, so meldet sich der Diskettenmonitor mit

```
ERR:xx
```

und springt wieder in die Kommandoschleife. `xx` enthält den Error-Code (siehe Abschnitt "Abfangmöglichkeiten von Diskettenfehlern").

### `B<ENTER>` – Breakpoints ansehen/ändern

Der Monitor bietet die Möglichkeit, bis zu acht Breakpoints (Testpunkte) beliebig zu setzen (B steht für Breakpoints). Kommt das zu testende Programm an solch einem Punkt an, dann wird es angehalten, das Prompt `*` wird ausgegeben und man kann sich in Ruhe die Register ansehen und überprüfen, ob alles bis hierher richtig verlaufen ist.

Das Einstellen der Breakpoints erfolgt mittels des B-Befehles:

```
*B<ENTER>

-B1-   -B2-   -B3-   -B4-   -B5-   -B6-   -B7-   -B8-
0000   0000   0000   0000   0000   0000   0000   0000
```

Sie können dann den ersten Breakpoint ändern oder mittels `<ENTER>` zum nächsten Breakpoint gelangen, usw., bis nach dem achten Breakpoint oder durch das Drücken von `<ESC>` der Monitorprompt `*` wieder erscheint.

### `Dadresse1,adresse2<ENTER>` – Auflisten in HEX/ASCII Form

Der D-Befehl (D steht für Dump) gibt Ihnen die Möglichkeit, Speicherinhalte in folgendem Format anzuzeigen:

```
0100 00 00 41 00 33 57 00 00 00 51 00 35 00 00 00 00  ..A.!9...3.#.
```

Am Anfang der Zeile wird Ihnen die Adresse (`0100H`) im Speicher angezeigt, ab der in dieser Zeile 16 Inhalte von Adressen angezeigt werden. Dann kommen die 16 Werte (hexadezimal) und ganz rechts deren ASCII-Übersetzungen: ist der Wert kleiner 32 oder größer 127, so wird ein Punkt `.`, ansonsten aber das richtige ASCII-Zeichen ausgegeben.

Geben Sie nach Drücken der Taste D nur eine Adresse (`adresse1`) ein, so werden die nachfolgenden `100H` Speicherinhalte ausgegeben. Drücken Sie allerdings nach `adresse1` nicht `<ENTER>`, sondern die Komma-Taste, so können Sie eine zweite Adresse (`adresse2`) eingeben. Es werden dann von `adresse1` bis `adresse2` die Speicherinhalte in HEX/ASCII Form "gedumpt". Eine solche Auflistung können Sie durch das Drücken einer beliebigen Taste (es bietet sich die Leer-Taste an) kurzfristig anhalten und durch nochmaliges Drücken wieder starten. Drücken Sie nach dem Anhalten `<ESC>`, dann erscheint wieder das Monitorprompt `*`.

### `Fadresse1,adresse2,wert<ENTER>` – Füllen eines Speicherbereichs mit einem bestimmten Wert

Oft kommt es vor, daß bestimmte Speicherbereiche z.B. gelöscht werden sollen. Dies ist mit dem F-Befehl (F steht für Fill) kein Problem. Man sollte aber aufpassen, was man füllt. Es gibt Bereiche, wo aktiv ein Programm abläuft. Füllt man hier einfach, dann kann es passieren, daß der ganze Rechner abstürzt, also Vorsicht!

```
*FC000,FFFF,FF<ENTER>
*
```

füllt den Bildschirmspeicher (Adressen `&C000` bis `&FFFF`) mit dem Wert `FF`.

### `Gadresse<ENTER>` – Ausführen eines Maschinenprogramms

Dieser Befehl (G steht für Go) führt ein ab der eingegebenen `adresse` befindliches Maschinenspracheprogramm aus. Wird hierbei ein Breakpoint (siehe weiter vorne) erreicht, so geht die Kontrolle an den Monitor zurück und es erscheint das Prompt `*`.

```
*GBD19<ENTER>
```

führt das Maschinenspracheprogramm ab der Adresse `BD19` aus.

### `Idateiname.dateityp<ENTER>` – Laden einer Binärdatei von Diskette/Cassette

Mit diesem Befehl (I steht für Input) kann eine Binär-Datei (Dateityp `BIN`) in den Monitor hereingeladen werden. Haben Sie vor dem Start von XMON z.B. `|CAS.IN<ENTER>` eingegeben, so wird die von Ihnen in XMON angeforderte Datei von Cassette geladen. Geben Sie nichts ein, so wird sie von Diskette geladen.

Die Binär-Datei wird dabei in den originalen Speicher, d.h. in den Speicherbereich, aus dem sie erstellt wurde, geladen. Es werden die Ladeadresse, die Länge sowie eine eventuell vorhandene Startadresse angezeigt.

```
*ITEST.BIN<ENTER>
(2000 0380 2140)
*
```

lädt die Datei `TEST.BIN` in den Speicher. Die ermittelte Anfangsadresse ist `2000H`, die Länge `380H` und die Startadresse `2140H`.

### `Ladresse1,adresse2` – Disassemblieren eines Speicherbereichs

Die Eingabe und Bedeutung der Adressen entspricht denen des D-Befehls (siehe weiter vorne), wobei allerdings der Speicherinhalt in Form von Mnemonics dargestellt wird.

```
*L0100,0106<ENTER>
0100 3E64       LD A,64H
0102 ED5B3204   LD BC,(0432H)
0106 E3         EX (SP),HL
*
```

Listet den Bereich von `100` bis `106`. Am Anfang steht die Adresse, dann deren Inhalt in hexadezimaler Form und dann der lesbare Z80-Mnemonic.

### `Madresse1,adresse2,adresse3<ENTER>` – Verschieben von Speicherbereichen

Der Inhalt des Speicherbereichs zwischen `adresse1` und `adresse2` wird in den Speicherbereich beginnend mit `adresse3` kopiert. Man muß hier etwas vorsichtig sein, daß `adresse3` nicht innerhalb des Bereichs `adresse1`/`adresse2` liegt oder so knapp vor `adresse1`, daß eine Überlappung zustande kommt.

```
*M0000,3FFF,C000<ENTER>
```

kopiert den Bereich von `0`-`3FFF` in den Speicherbereich ab Adresse `&C000` (= Bildspeicher).

### `Odateiname.dateityp<ENTER>adresse1,länge,adresse2` – Speichern einer Datei

Wenn Sie nach dem O (O steht für Output) eine zulässige Dateibezeichnung eingegeben haben, wird entsprechend dem BASIC Befehl `SAVE "name",B` nach Anfangsadresse des Speicherbereichs, dessen Länge und einer Startadresse gefragt. Danach wird dieser Speicherbereich auf Diskette/Cassette unter der eingegebenen Bezeichnung geschrieben.

```
*OTEST.BIN<ENTER> C000,4000,0000
*
```

Es wird in die Binär-Datei `TEST.BIN` der Speicherbereich von `&C000` bis `&FFFF` ohne Startadresse abgespeichert.

### `P` – Drucker ein/aus

Wenn ein Drucker angeschlossen ist, wird die Bildschirmausgabe durch einmaliges Drücken der Taste P auf diesem mitdokumentiert. Nochmaliges Drücken der Taste P schaltet den Drucker wieder ab. (P steht für Print.)

### `R` – Anzeigen/Ändern der Registerinhalte

Die Registerinhalte für die Abarbeitung eines Maschinensprache-Programms (mit G-Befehl oder T-Befehl) sind mit diesem Befehl (R steht für Registers) änderbar. Sie werden ähnlich den Breakpoints dargestellt und genauso geändert. Es ist nur der Erst-Registersatz änderbar.

### `Sadresse<ENTER>` – Speicherinhalt anzeigen und ändern

Nach Eingabe von S (S steht für Substitute) und der `adresse` sehen Sie deren Inhalt und können diesen in einer dritten Spalte entsprechend ändern. Durch Drücken von `<ENTER>` gehen Sie weiter zur nächsten Speicherzelle, der eventuell geänderte Wert der alten Adresse wird in diese eingetragen. Durch Drücken von `<ESC>` kommen Sie wieder zum Monitorprompt `*`.

```
*S4000<ENTER>
4000  24  34<ENTER>
4001  43  32<ENTER>
4002  58  44<ENTER>
4003 <ESC>
*
```

Ändern ab Speicherzelle `4000`. Die alten Werte der Adressen `4000`, `4001` und `4002` (`24`, `43` und `58`) werden durch die neuen Werte (`34`, `32` und `44`) ersetzt.

### `Tadresse,anzahl<ENTER>` – Maschinenprogramm schrittweise ausführen

Ein Maschinenprogramm kann mit diesem Befehl schrittweise ausgeführt werden, um eventuell vorhandene Fehler zu entdecken. Es wird dabei von den mit dem R-Befehl eingegebenen Registerwerten ausgegangen und die Kontrolle wird nach jedem Schritt an den Monitor zurückgegeben, d.h. Sie sehen die eventuell geänderten Register und können die Abarbeitung auch unterbrechen, wenn Sie eine optionelle Schrittzahl angegeben haben. Diese Unterbrechung erreichen Sie wie gewohnt mit `ESC`.

> **(!) Hinweis:** Beachten Sie bitte, daß Programme im ROM oder Befehle, die mit dem Zweitregistersatz des Z80 arbeiten, nicht schrittweise abgearbeitet werden können. Desweiteren sollte der Stackpointer SP nicht unter einem ROM liegen, was zum Absturz des Systems führen kann.

```
*T4000,0007<ENTER>
```

führt sieben Schritte ab Adresse `4000H` aus. Die Registerinhalte werden immer angezeigt und der Ablauf kann wie beim D-Befehl angehalten (Leertaste drücken) oder abgebrochen (`<ESC>`) werden.

### `X` – Firmware ROM ein/ausschalten

Genauso wie der Befehl `P` (siehe oben) ist der Befehl `X` auch ein Schalter. Nach dem Starten des Monitors durch `|XMON<ENTER>` ist `X` ausgeschaltet, d.h. im Adressraum von `0000H` bis `3FFFH` wird der interne RAM eingeblendet. Wird nun der `X`-Befehl eingegeben (dieser muß genau wie `P` nicht mit `<ENTER>` abgeschickt werden), so sehen Sie nun von `0000H` bis `3FFFH` den Firmware ROM.

### `Y` – Oberen ROM anwählen

Geben Sie ein `Y` ein, so liefert Ihnen der Monitor eine Liste aller Erweiterungs-ROMs im System. Diese Liste hat folgenden Aufbau:

```
xy rssbvw name
......
......
```

Hier bedeutet:

| Feld | Bedeutung |
|------|-----------|
| `xy` | Nummer des Erweiterungs-ROMs |
| `rs` | ROM Mark Nummer |
| `ab` | ROM Versions-Nummer |
| `vw` | ROM Modifikations-Nummer |
| `name` | RSX Name der ROM WALK Routine |

Direkt nach der ROM-Liste kommt dann

```
Vac   (ac=aktueller Erweiterungs-ROM)
```

und der Monitor wartet auf Ihre Eingabe. Sie können nun die Erweiterungs-ROM-Nummer ändern (Eingabe mit `<ENTER>` beenden). Erlaubte Erweiterungs-ROM-Nummern liegen zwischen `00` und `FBH`.

`ac` ist hierbei immer der ROM, den Sie im Adressbereich von `&C000` bis `&FFFF` sehen. Geben Sie die Nummer eines ROMs ein, der nicht existiert, so schaltet der Monitor immer den eingebauten BASIC ROM ein. Möchten Sie den Inhalt des Bildspeichers sehen, so geben Sie eine ROM-Nummer zwischen `FCH` und `FFH` ein.

### `C` – Suchen von Bytefolgen

Mithilfe des C-Befehls können Sie den Speicher nach einzelnen Bytes oder auch nach ganzen Bytefolgen absuchen. Die maximale Länge ist hierbei 255 Bytes.

```
Cabcd<ENTER>,xy<ENTER>
```

| Parameter | Bedeutung |
|-----------|-----------|
| `abcd` | Adresse der Bytefolge |
| `xy` | Länge der Bytefolge |

Die Bytefolge müssen Sie vorher mit dem S- oder A-Befehl (siehe oben) im Speicher ablegen.

Der C-Befehl gibt Ihnen dann eine Liste aller Adressen aus, an denen er die Bytefolge gefunden hat.

---

## Der VDOS Befehl |ROMOFF

Der Befehl `|AMSDOS` schaltet selektiv nur den VDOS ROM ab, d.h. alle RSX Befehle des VDOS ROMs stehen dann nicht mehr zur Verfügung. Völlig äquivalent zum Befehl `|AMSDOS` arbeitet unter anderem auch der Befehl `|DISBOS` der vortex RAM-Karte – dieser schaltet selektiv den BOS ROM ab. Der Konflikt ist aufgezeigt, denn es ist nicht möglich, mit diesen beiden Befehlen gleichzeitig den VDOS ROM und den BOS ROM abzuschalten. Aus diesem Grunde wurde der Befehl `|ROMOFF` eingebaut, der es erlaubt, mehrere ROMs gleichzeitig auszuschalten.

```
|ROMOFF<ENTER>
```

schaltet alle Background-ROMs ab.

```
|ROMOFF,6,7<ENTER>
```

schaltet nur die Background-ROMs mit der Nummer 6 und 7 ab. (Hier können die ROM-Nummern 0..7 stehen.)

Einschalten können Sie die Background-ROMs selbstverständlich wieder dadurch, daß Sie Ihren CPC resetieren (Ein-/Ausschalten oder gleichzeitiges Drücken der Tasten `CTRL`+`SHIFT`+`ESC`).

---

## Der VDOS Befehl |ROMS

Der VDOS Befehl `|ROMS` erstellt eine Tabelle aller Background-ROMs mit Nummern zwischen 0 und 7 folgenden Aussehens:

| No | Name  | Version |
|----|-------|---------|
| 7  | V ROM | 0.31    |
| …  | …     | …       |

Möchten Sie also mit dem VDOS Befehl `|ROMOFF` arbeiten, so können Sie zuvor mit dem VDOS Befehl `|ROMS` die Nummern der Background-ROMs ermitteln, die Sie abschalten möchten.

---

## Relative und Sequentielle Dateiverwaltung

Bislang hatten wir nur immer über Dateien gesprochen, deren Inhalt ein Programm darstellte (Programm-Dateien).

Stellen Sie sich vor, Sie möchten ein kleines Adressverwaltungsprogramm in BASIC schreiben, mit dem Sie die Adressen (Name, Anschrift usw.) Ihrer Bekannten bearbeiten können, d.h. eingeben, ändern und suchen können. Das setzt aber voraus, daß Sie diese "Daten" permanent speichern können (auf Diskette oder Cassette). Sie müssen Ihr Programm also derart konstruieren, daß es eine Adress-Datei anlegt, in der alle Adressen stehen. Diese Datei wäre also eine reine Daten-Datei, ihr Inhalt wäre kein ausführbares Programm.

Haben Sie an Ihrem CPC keine vortex Floppy angeschlossen, dann fehlt Ihnen auch das VDOS Betriebssystem. Sie haben jetzt zwei sogenannte "Kanäle" (Ein- und Ausgabekanal, siehe auch `|CAS` und `|DISC` Befehle, Abschnitt "Cassettenrekorder am CPC"), über die Sie Daten zum Rekorder oder auch zum eventuell vorhandenen 3"-Laufwerk schicken und von dort auch empfangen können (die englischen Fachbegriffe sind hierfür INPUT-Stream und OUTPUT-Stream).

D.h. Sie können gleichzeitig immer nur eine Datei zum Schreiben und eine Datei zum Lesen "geöffnet" haben. Bevor Sie auf eine Datei "zugreifen" können, muß diese erst "geöffnet" werden. Wenn Sie die Datei im Moment nicht mehr brauchen, muß sie wieder geschlossen werden.

Es geht also nicht, daß Sie gleichzeitig zwei Dateien zum Schreiben öffnen oder gleichzeitig zwei Dateien zum Lesen öffnen. Dies ist natürlich eine gewisse Einschränkung, mit der man aber leben kann.

Ein weitaus größerer Nachteil ist es, daß der Inhalt dieser Dateien nur nacheinander gelesen und auch nur nacheinander geschrieben werden kann. Dieses "nacheinander" kennzeichnet die Art, wie diese Dateien vom Betriebssystem her "verwaltet" werden. Man nennt diese Dateiverwaltung deshalb auch **"Sequentielle Dateiverwaltung"**.

Wenn Sie z.B. 1000 Adressen in Ihrer Adresskartei haben und die letzte lesen wollen, dann müssen Sie sich erst durch die 999 Adressen davor durchlesen, das dauert und bringt wenig Effizienz in die ganze Sache.

Das Vorhandensein der sequentiellen Dateiverwaltung ist historisch bedingt. Der erste Schneider (der CPC464) war nur mit einem Cassettenrecorder ausgerüstet. Es ist eigentlich klar, daß eine Dateiverwaltung hier nur sequentiell sein kann, denn das Speichermedium ist hier ein Band. Will man von X nach Y, dann muß das ganze Band dazwischen durchlaufen werden.

Dann kamen die 3"-Laufwerke. Man hat hier praktisch am Betriebssystem wenig geändert, es wurde "einfach" der Rekorder durch das Laufwerk ersetzt. Es blieb bei der sequentiellen Dateiverwaltung, obwohl mit einem Disketten-Laufwerk wesentlich mehr gemacht werden kann.

Nachfolgend finden Sie ein kleines Beispiel für die sequentielle Dateiverwaltung.

Typische BASIC Befehle, die im Zusammenhang mit dem Lesen einer sequentiellen Datei auftauchen, sind:

```
OPENIN   EOF   INPUT#9   LINE INPUT#9   CLOSEIN
```

Typische BASIC Befehle, die im Zusammenhang mit dem Schreiben einer sequentiellen Datei auftauchen, sind:

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

Mit Zeile 10 wird die Datei `ZAHLEN.DAT` zum Schreiben geöffnet. War sie bislang noch nicht vorhanden, dann wird sie jetzt angelegt. Innerhalb der `FOR/NEXT`-Schleife werden die Zahlen 1 bis 100 – umgewandelt in Strings – mit `PRINT#9,A$` in diese Datei geschrieben. Zeile 60 schließt die Datei ordnungsgemäß.

In 70 wird die Datei wieder zum Lesen geöffnet. Wir suchen eine bestimmte Zahl bzw. deren Position in der Datei `ZAHLEN.DAT`.

Zeile 110 zeigt einen für sequentielle Dateien typischen Vergleich: Man muß sich durch die Datei "durchvergleichen", bis man den Datensatz gefunden hat, den man eigentlich gesucht hat.

So, nun schließen wir das vortex X-Laufwerk an und verfügen damit über VDOS! Sie beherrscht die gerade beschriebene sequentielle Dateiverwaltung natürlich auch. Sie kann aber noch wesentlich mehr. Sie ermöglicht Ihnen eine **"Relative Dateiverwaltung"**.

Auszeichnend für eine relative Dateiverwaltung ist es, daß ein Datensatz an jeder beliebigen Stelle der Datei herausgeholt oder hineingeschrieben werden kann, ohne jedoch vorher alle Datensätze davor gelesen zu haben. Es kann hier auf jeden Datensatz per Datensatznummer wahlfrei zugegriffen werden, das spart natürlich Zeit und Programmieraufwand.

Außerdem erlaubt Ihnen VDOS neben den 2 sequentiellen Kanälen noch bis zu 16 (!) relative Kanäle gleichzeitig zu öffnen. Damit dürfte sich jedes gestellte Problem optimal in ein Programm verwandeln lassen.

Relative Dateien bestehen wie die sequentiellen Dateien aus Datensätzen (auch Rekords genannt). Im Unterschied zu einer sequentiellen Datei sind aber bei der relativen Datei diese Rekords vollkommen unabhängig voneinander. Jeder Rekord hat eine Nummer, über die er selektiert werden kann. Sie können in beliebiger Reihenfolge gelesen bzw. geschrieben werden. Die Länge eines Datensatzes kann innerhalb gewisser Grenzen frei gewählt werden.

Es wird für jede geöffnete relative Datei im RAM-Speicher ein bestimmter Bereich reserviert, der sogenannte "Rekordpuffer". Wird ein Datensatz gelesen bzw. geschrieben, dann gelangt der Datensatz immer über diesen Puffer aus der Datei bzw. in die Datei. Es ist klar, daß die Größe dieses Puffers von der einmal gewählten Rekordlänge abhängt.

Es ist zu beachten, daß bei einer geöffneten relativen Datei die Datensatzlänge nicht änderbar ist.

Ein weiterer Unterschied zwischen beiden "Verwaltungsarten" besteht darin, daß bei einer relativen Datei die Datensätze (Rekords) noch strukturiert werden können; man sagt auch, der Rekord kann noch in verschiedene "Felder" unterteilt werden.

Man kann also sagen, die relative Datei besteht aus einer bestimmten Anzahl von Datensätzen, wobei alle Datensätze noch in eine bestimmte Anzahl von Feldern unterteilt sind. Die Feldaufteilung in einer relativen Datei muß bei allen Datensätzen dieselbe sein.

Jede geöffnete relative Datei benötigt für ihren Rekordpuffer, für ihren FCB (File Control Block, enthält auch die Dateibezeichnung der relativen Datei) und etliche interne Zeiger und Zähler Speicher im RAM (alles in allem 90 Bytes + Rekordpuffer pro Kanal).

Dieser Speicher wird bei der Definition des Kanals (siehe `|FILES` Befehl) im oberen Speicherbereich des CPC's durch dynamisches Herabsetzen des `HIMEM`'s reserviert. Wurde ein Kanal definiert, so kann eine relative Datei auf ihm eröffnet werden (siehe `|OPEN` Befehl). Es ist zu beachten, daß sowohl bei der Kanaldefinition (`|FILES`) als auch beim Öffnen einer Datei auf diesem Kanal (`|OPEN`) Rekordlängen angegeben werden müssen.

Dies hat folgenden leicht einsehbaren Grund: Es ist durchaus möglich, auf einem Kanal hintereinander mehrere relative Dateien zu öffnen und zu schließen, ohne daß jedesmal eine Kanaldefinition (`|FILES`) erfolgen muß. Man gibt nur bei der einmaligen Kanaldefinition die größte zu erwartende Rekordlänge an und öffnet dann später die einzelnen Dateien (`|OPEN`) mit ihren jeweils individuellen Rekordlängen.

Nachdem eine relative Datei geöffnet wurde (`|OPEN`), muß der Rekordpuffer vor dem ersten Zugriff auf die Datei (`|PUT`, `|GET`) auf die Datei strukturiert werden, also in Felder unterteilt werden (`|FIELD`), d.h. man muß angeben, welche Teile des Rekords beim Zugriff in Variablen eingelesen werden sollen.

Jetzt ist die relative Datei für Datenübertragung bereit und man kann bis zum Schließen der Datei (`|CLOSE`) wahlfrei (man sagt oft auch zufällig, daher kommt auch die manchmal gefundene englische Bezeichnung "Random File") Rekords lesen und schreiben.

> **(!) Hinweis:** Es ist zu beachten, daß ausschließlich Stringvariablen in Rekords geschrieben und auch wieder ausgelesen werden können. Will man numerische Variablen oder Felder (auch String-Felder) in relativen Dateien speichern, so muß man diese zuerst in Stringvariablen umwandeln, bzw. einer Stringvariablen zuweisen und diese dann abspeichern (siehe BASIC Befehl `STR$` in Ihrem CPC BASIC Handbuch). Will man z.B. wieder einen numerischen Wert "rückgewinnen", so muß er nach dem Auslesen aus der Datei mittels des BASIC Befehls `VAL` wieder umgewandelt werden.

Ein Rekord kann, nachdem die Datei geöffnet wurde, durchaus mehrmals neu segmentiert (`|FIELD`) werden, ohne daß die Datei jedesmal geschlossen und wieder neu geöffnet werden muß.

Doch nun zu den VDOS Befehlen, die den Umgang mit den relativen Dateien ermöglichen.

---

## Der VDOS Befehl |FILES

**Reservieren von Arbeitsspeicher für eine/mehrere relative Dateien**

Bevor mit einer relativen Datei gearbeitet werden kann, muß hierzu ein Kanal und ein Rekordpuffer definiert werden. Das Öffnen einer relativen Datei ohne vorhergehendes Reservieren eines Puffers für diese Kanalnummer mit dem `|FILES` Befehl ergibt die Fehlermeldung:

```
Feld nicht definiert
```

Aus diesem Grunde sollte (muß aber nicht!) der `|FILES` Befehl am Anfang eines BASIC Programmes stehen und für alle später verwendeten Kanalnummern ein ausreichender Rekordpuffer reserviert werden.

Der `|FILES` Befehl arbeitet mit Zahlen-Doubletten, d.h. zu jeder angegebenen Kanalnummer muß eine maximale Rekordlänge mit angegeben werden. Die Kanalnummer darf Werte von 0 bis 127 annehmen (es dürfen insgesamt 16 Kanäle gleichzeitig geöffnet sein), die maximale Rekordlänge kann beliebig gewählt werden und ist nur durch den zur Verfügung stehenden Arbeitsspeicher begrenzt.

Jeder weitere `|FILES` macht den zuvor erfolgten hinfällig. Wird nur `|FILES<ENTER>` eingegeben, so werden alle Arbeitsbereiche von relativen Dateien im RAM gelöscht.

Durch die Eingabe von:

```
|FILES,1,128,2,64,12,20<ENTER>
```

werden für Kanal 1 ein 128 Bytes großer Rekordpuffer, für Kanal 2 ein 64 Bytes großer Rekordpuffer und für Kanal 12 ein 20 Bytes großer Rekordpuffer reserviert. Es können jetzt auf diesen 3 Kanälen relative Dateien eröffnet werden.

---

## Der VDOS Befehl |OPEN

**Öffnen einer relativen Datei**

Mit dem `|FILES` Befehl haben wir die Voraussetzung dafür geschaffen, daß eine relative Datei überhaupt benutzt werden kann. Der nächste Schritt ist, daß die relative Datei "geöffnet" wird, damit wir Daten in sie schreiben oder Daten aus ihr lesen können. Dazu dient der `|OPEN` Befehl.

```
|FILES,3,300<ENTER>

|OPEN,"DATEI.REL",145,3<ENTER>
```

Schauen wir uns den `|OPEN` einmal genauer an. Offensichtlich wird hier eine relative Datei namens `DATEI.REL` geöffnet. Ist sie bereits auf der Diskette vorhanden, dann wird sie einfach geöffnet, existiert sie noch gar nicht, dann wird sie erneut angelegt und dann geöffnet.

`145` ist die aktuelle Rekordlänge, die kleiner gleich der maximalen Rekordlänge (im `|FILES` auf 300 eingestellt) sein muß. Geöffnet wird die Datei auf Kanal 3, auf dem zu diesem Zeitpunkt keine weitere Datei geöffnet sein darf.

> **(!) Hinweis:** Auf ein und demselben Kanal darf gleichzeitig nur eine Datei geöffnet sein. Brauchen Sie aber weitere Dateien, dann wählen Sie einfach eine andere Kanalnummer.

Wenn Sie eine Datei öffnen, die bereits offen ist, dann erhalten wir folgende Meldung:

```
Kanal bereits geöffnet
```

Vergessen Sie einmal den `|OPEN` Befehl und benutzen Sie dann trotzdem den `|PUT` oder den `|GET` Befehl, dann erhalten Sie folgende Meldung:

```
Kanal nicht definiert
```

---

## Der VDOS Befehl |FIELD

**Strukturieren des Rekordpuffers**

Nachdem eine relative Datei geöffnet wurde, muß deren Rekordpuffer segmentiert werden, d.h. man muß angeben, wie viele Variablen mit welcher Länge in einem Rekord der Datei stehen sollen.

Man will in einem Datensatz folgende drei Variablen haben: `NAME$` mit einer maximalen Länge von 12 Bytes, `ORT$` mit einer maximalen Länge von 20 Bytes und `TEL$` mit einer maximalen Länge von 15 Bytes. Der `|FIELD` Befehl für diese Kombination sieht z.B. wie folgt aus:

```
|FIELD,4,12,20,15<ENTER>
```

Die aktuelle Länge des Puffers im `|OPEN` Befehl müßte also 12+20+15=47 oder größer gewesen sein. Diese Segmentierung bezieht sich auf den Rekordpuffer des Kanals 4.

Im Zusammenhang mit dem `|FIELD` Befehl können wir folgende Meldungen erhalten:

**`Feld zu lang`** – Wir haben eine Feldlänge definiert, die die Länge des Rekordpuffers – festgelegt mit `|FILES` – überschreitet.

**`Feld nicht definiert`** – Wir haben in einem `|PUT` oder `|GET` Befehl eine Variable angegeben, für die im `|FIELD` Befehl kein Platz vorgesehen ist.

**`Feld nicht segmentiert`** – Wir haben mit `|PUT` oder `|GET` einen Datensatz schreiben oder lesen wollen, obwohl wir ihn noch gar nicht mit dem `|FIELD` Befehl in einzelne Felder unterteilt (segmentiert) haben.

---

## Der VDOS Befehl |GET

**Lesen eines Datensatzes**

Mit dem `|GET` Befehl liest man den Datensatz mit der angegebenen Nummer aus der Datei auf diesem Kanal in die angegebenen Variablen, die vorher definiert sein müssen. Wurden die Variablen nicht definiert, dann erhalten wir die Fehlermeldung:

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

Hier werden zuerst die Variablen definiert (Zeile 10) und dann wird der Datensatz mit der Nummer 174 aus der Datei auf Kanal 1 in die Variablen `NAME$`, `ORT$` und `TEL$` eingelesen.

> **(!) Hinweis:** Bitte beachten Sie, daß hier nur die Darstellung mit dem `@` (Klammeraffen) zugelassen ist!! Zuvor müssen ordnungsgemäße `|FILES`, `|OPEN` und `|FIELD` Befehle gestartet worden sein.

Enthält der gelesene Rekord keine Daten, so erhalten wir die Meldung:

```
Rekord enthaelt keine Daten
```

---

## Der VDOS Befehl |PUT

**Schreiben eines Datensatzes**

`|PUT` arbeitet genauso wie der `|GET` Befehl, nur schreibt er den Inhalt der angegebenen Variablen in die Datei auf dem angewählten Kanal.

```basic
10 NAME$="" : ORT$="" : TEL$=""
20 |FILES,1,100
30 |OPEN,"ADRESS.REL",47,1
40 |FIELD,1,12,20,15
50 INPUT NAME$,ORT$,TEL$
60 |PUT,1,174,@NAME$,@ORT$,@TEL$
70 |CLOSE,1
```

Der `|PUT` Befehl kann auch ohne den `@` (Klammeraffen) verwendet werden:

```
|PUT,1,15,"Mueller","Koeln","123456"
```

Hier werden direkt die drei Worte in den Datensatz mit der Nummer 15 in die Datei auf Kanal 1 weggeschrieben. Es ist natürlich klar – und das gilt auch für den `|GET` Befehl –, daß die Satz-Nummer auch durch eine Variable ersetzt werden kann. So z.B.

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

Durch die Wahl von `REC` kann die Datensatznummer bestimmt werden, in die der Inhalt der drei Variablen geschrieben werden kann. Wenn Sie einmal eine Rekordnummer angeben, die den Rahmen der Datei sprengt, dann erhalten Sie die Meldung:

```
Rekordnummer zu gross
```

---

## Der VDOS Befehl |CLOSE

**Schließen einer relativen Datei**

Soll die Benutzung einer relativen Datei ordnungsgemäß ablaufen, dann muß zum Schluß die relative Datei wieder geschlossen werden.

```
|CLOSE,1 <ENTER>
```

Schließt die Datei, die auf Kanal 1 geöffnet war. Ist auf diesem Kanal keine Datei vorhanden, dann bekommen Sie die Meldung:

```
Kanal nicht geoeffnet
```

---

## Zwei kleine Anwendungen

Hier folgen nun die Listings zweier kleiner Programme, die Ihnen das Arbeiten mit relativen Dateien nochmals verdeutlichen sollen. Beim ersten Beispiel wird die Datei `TEST.REL` geöffnet und es wird ein selektierbarer Rekord gelesen und angezeigt oder es wird ein Rekord mit eingebbarem Inhalt beschrieben.

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

| Zeile | Erklärung |
|-------|-----------|
| 10 | Einrichten eines Puffers von 600 Bytes Länge für den Kanal mit der Nummer 1 |
| 20 | Öffnen der Datei `TEST.REL` mit der aktuellen Satzlänge von 520 Bytes auf Kanal 1 |
| 30 | Es wird nur der Inhalt zweier Variablen in den Puffer geschrieben. Die Inhalte beider Variablen dürfen eine maximale Länge von 250 Bytes haben. |
| 40 | Definieren der beiden Variablen für den `|GET` Befehl |
| 50 | Abfrage, was getan werden soll |
| 60 | Eingabeschleife |
| 70 | Eingeben der Datensatz-Nummer |
| 90 | Hier kommen Sie an, wenn Sie oben "L" eingegeben haben. Der Inhalt des durch `REC` selektierten Satzes wird in die Variablen `X$` und `Y$` eingelesen. |
| 100 | Ausdrucken des Inhaltes |
| 120 | Hier kommen Sie an, wenn Sie oben "S" eingegeben haben. Sie geben den Variablen `X$` und `Y$` (Zeile 130) einen Wert. |
| 140 | Der Inhalt der beiden Variablen wird in den durch `REC` selektierten Datensatz geschrieben. |
| 150 | Rücksprung auf Zeile 50 für erneute Eingabe |
| 160 | Hier kommen Sie an, wenn Sie "E" eingegeben haben. Die Datei wird ordnungsgemäß geschlossen. |

Sie sollten zumindest ein paar Mal nur die Wahl "S" treffen, damit die Datei `TEST.REL` überhaupt einmal einen Inhalt bekommt, der dann mit "L" gelesen werden kann.

Im zweiten Beispiel werden nacheinander 1000 Rekords in die relative Datei `ZUFALL.REL` geschrieben. Danach wird über die Zufallsfunktion (`RND` = random) im wahrsten Sinne des Wortes "rein zufällig" auf die Datensätze der Datei zugegriffen.

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

| Zeile | Erklärung |
|-------|-----------|
| 10 | Reservieren eines 120 Bytes großen Puffers für Kanal 10. |
| 20 | Öffnen der relativen Datei `ZUFALL.REL` auf Kanal 10 mit der aktuellen Rekordlänge von 25 |
| 30 | Segmentierung des Puffers. Es wird nur eine Variable angelegt. |
| 40 | Definition der Variablen `X$` für den `|GET` Befehl. |
| 60 | Es werden 1000 Rekords: "Rekord Nr. 1", "Rekord Nr. 2", …, "Rekord Nr. 1000" in die Datei `ZUFALL.REL` geschrieben. |
| 90 | Erzeugen einer Zufallszahl zwischen 1 und 1000 |
| 100 | Auslesen des Datensatzes mit der Nummer der Zufallszahl. |
| 110 | Anzeigen des Datensatzes |
| 120 | Erneut eine Zufallszahl erzeugen und Datensatz auslesen. |

Mit diesem Beispiel wird sehr gut die hohe Zugriffsgeschwindigkeit auf die Daten der relativen Datei demonstriert.

Das nachfolgende Programm erfüllt dieselben Aufgaben wie das gerade gezeigte Beispiel, nur daß hier sequentielle Dateien verwendet werden. Geben Sie es einmal ein. Sie werden staunen, um wieviel langsamer hier alles läuft. Das zeigt einmal mehr, daß für professionelles Arbeiten das "Werkzeug" einer relativen Dateiverwaltung unerläßlich ist.

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

In Zeile 10 bis Zeile 60 wird die Datei `ZUFALL.SEQ` angelegt. Sie sehen, daß die Daten ohne jegliche Nummernkennzeichnung weggeschrieben werden. In Zeile 110 wird der vom Zufallsgenerator in Zeile 90 erzeugte String mit dem gerade ausgelesenen verglichen. Sind beide identisch, dann wird der String angezeigt (Zeile 120). Sind sie nicht gleich, dann muß weiter verglichen werden, bis vielleicht dann der 1000. Satz übereinstimmt (ungünstigster Fall). Stimmt gleich der erste Vergleich (Rekord Nr. 1) überein, dann haben wir den günstigsten Fall.

Bei der relativen Dateiverwaltung gibt es keine günstigen und ungünstigen Fälle, alle sind gleich. Wie Sie leicht feststellen werden, wird ein und dieselbe Aufgabe von der relativen Dateiverwaltung des VDOS ca. 10 mal schneller als von der sequentiellen Dateiverwaltung gelöst.

---

## Abfangmöglichkeiten von Diskettenfehlern

**Der VDOS Befehl `|DERROR`**

Um zu verhindern, daß ein BASIC Programm durch eine Laufwerks-Meldung (im allgemeinen Fehlermeldungen) abgebrochen wird und BASIC sich mit `Ready` meldet, können die Fehlermeldungen mit dem `|DERROR` Befehl abgefangen werden und im Programm bearbeitet werden. D.h. ein "Aussteigen" kann gänzlich unterbunden werden. Dies ist vor allem für PROFI-Anwendungen sehr wichtig: ein Ausstieg würde hier das "AUS" bedeuten.

Nach der Eingabe von `|DERROR,0<ENTER>` werden keine Diskettenfehler mehr auf dem Bildschirm ausgegeben. Mit `|DERROR,1<ENTER>` wird die Fehlerausgabe wieder eingeschaltet. Dies entspricht auch dem Einschaltzustand des CPC's mit angeschlossener vortex Floppy. Sind die Fehlermeldungen ausgeschaltet, so kann durch die Eingabe von `|DERROR<ENTER>` (also ohne Parameter) die Fehlercode-Variable `DERR` angelegt werden. Im Anschluß an diese Befehlserklärung finden Sie eine Liste aller Fehlercodes.

```basic
10 |DERROR,0
20 CAT
30 |DERROR
40 IF DERR=72 THEN INPUT "Bitte Diskette einlegen und irgendeine Taste druecken",A:GOTO 20
50 ....
```

Fehlercode 72 bedeutet, daß sich keine Diskette im Laufwerk befindet. In Zeile 10 haben wir die Fehlerausgabe abgeschaltet. In Zeile 30 veranlassen wir das Anlegen der Fehlercode-Variable. Hat sie den Wert 72, dann kommt die Meldung, in allen anderen Fällen läuft das Programm einfach weiter.

> **(!) Achtung:** Bestimmte Fehler können nicht alleine durch `|DERROR,0` abgefangen werden, sondern es muß noch zusätzlich mit `ON ERROR GOTO` gearbeitet werden.

Wir nehmen einmal an, daß sich im folgenden keine Diskette im Laufwerk befindet. Ein Zugriff auf das Laufwerk würde also ohne Fehlerabfang die Meldung

```
Laufwerk d: Diskette fehlt
```

erzeugen. Fangen wir diesen Fehler mit `|DERROR,0` ab, so meldet BASIC trotzdem einen Fehler. Lassen Sie das nachfolgende Programmchen einfach einmal laufen:

```basic
10 |DERROR,0
20 LOAD,"TEST"
30 ..
```

Sie werden folgende Fehlermeldung erhalten:

```
File already open in 20
```

und das Programm bricht ab. Testen Sie nun einmal folgendes Programm:

```basic
10 ON ERROR GOTO 100
20 |DERROR,0
30 LOAD "TEST"
40 ..
100 |DERROR:PRINT DERR:RESUME 40
```

Nun kommt keine Fehlermeldung mehr und die Fehlerabfangroutine in Zeile 100 gibt ein "72" auf den Bildschirm aus. (72 = `&48`, d.h. Bit 6 und Bit 3 sind gesetzt und dies wiederum bedeutet, es handelt sich um den FDC-Fehler – Floppy Disc Controller Fehler – "Drive not ready", d.h. es befindet sich keine Diskette im Laufwerk).

---

## Fehlercodes und ihre Bedeutung

Hier finden Sie eine Liste aller VDOS Fehlermeldungen: Fehlercode und Meldung. Außerdem werden noch die möglichen Ursachen mit angegeben. `<...>` ist Platzhalter für eine Dateibezeichnung. `FDC` steht für Floppy Disk Controller. Mit `d:` ist eine Laufwerkskennung gemeint, nämlich die, auf der der Fehler aufgetaucht ist (z.B. `A:` oder auch `B:`). Alle Fehlercodes sind dezimal angegeben.

| Code | Meldung | Bedeutung |
|------|---------|-----------|
| 17 | Drucker nicht bereit | Diese Fehlermeldung kann nur unter CP/M kommen und dort nur immer dann, wenn der Drucker ca. 40 sec nach dem Versuch, ein Zeichen auf ihm auszugeben, immer noch nicht bereit ist. Fehlerquellen sind: Druckerkabel nicht angesteckt, Drucker nicht eingeschaltet, Drucker nicht selektiert. |
| 10 | Laufwerk d: Diskette wurde gewechselt `<...>` wird geschlossen | Es wurde eine Datei mit `OPENOUT` geöffnet und dann, ohne ein `CLOSEOUT` zu geben, die Diskette gewechselt. |
| 21 | Laufwerk d: Diskette voll | Die Diskette in Laufwerk `d:` ist voll. |
| 22 | Laufwerk d: Directory voll | Das Inhaltsverzeichnis der Diskette ist voll. Beachten Sie, daß diese Meldung schon kommen kann, bevor Sie mit z.B. `CAT<ENTER>` auch wirklich 128 Einträge sehen. Grund: Pro 64 KB Daten pro Programm wird ein Directory-Eintrag benötigt. Eine Datei, die z.B. 129 KB groß ist, belegt bereits 3(!) Einträge im Inhaltsverzeichnis. |
| 23 | `<...>` wurde nicht gefunden | Wird immer dann gemeldet, wenn versucht wird, auf eine Datei zuzugreifen, die im Inhaltsverzeichnis nicht vorhanden ist. Der Fehler kann bei folgenden Befehlen auftauchen: `LOAD`, `SAVE`, `RUN`, `OPENIN`, `OPENOUT`, `|ERA`, `|REN` und `|ATTRIBUT`. |
| 24 | `<...>` existiert bereits | Es wird versucht, einer Datei eine neue Bezeichnung zu geben, wobei bereits eine andere Datei mit dieser Bezeichnung vorhanden ist. |
| 25 | `<...>` kann nur gelesen werden | Es wird versucht, eine Datei zu löschen (mit `|ERA` Befehl) bzw. zu beschreiben, die das "nur lesbar" Attribut trägt (mit dem `|ATTRIBUT` Befehl angebracht). |
| 33 | falsche Eingabe | Es wurde ein Schreibfehler gemacht (Syntax Error), oder das Befehlsformat eines bestimmten Befehls wurde nicht eingehalten (Semantik Error). |
| 39 | Feld zu lang | Die aktuelle Feldlänge ist größer als die im `|FILES` Befehl angegebene. Sie darf nur "kleiner gleich" sein. Diese Meldung kann kommen, wenn: aktuelle Länge in `|OPEN` zu groß ist, Summe der einzelnen Feldlängen in `|FIELD` größer als die in `|OPEN` definierte ist. |
| 40 | Feld nicht definiert | Es wird versucht, eine Datei auf einem Kanal zu öffnen (mit `|OPEN`), ohne daß zuvor der `|FILES` Befehl eingegeben worden wäre. |
| 41 | Feld nicht segmentiert | Es wird versucht, mit den `|GET` oder `|PUT` Befehlen zu arbeiten, ohne daß vorher der Rekordpuffer mit `|FIELD` segmentiert wurde. |
| 42 | Kanal bereits geöffnet | Es wurde versucht, einen bereits mit `|OPEN` geöffneten Kanal nochmals zu öffnen. |
| 43 | Kanal nicht geöffnet | Es wurde versucht, einen dieser Befehle (`|FIELD`, `|CLOSE`, `|GET` oder `|PUT`) mit einer Datei auf einem nicht geöffneten Kanal durchzuführen. |
| 44 | Kanalnummer falsch | Es wurde im Zusammenhang mit den Befehlen `|CLOSE`, `|FIELD`, `|OPEN`, `|GET`, `|PUT` oder `|FILES` eine unerlaubte Kanalnummer angegeben. Zulässige Kanalnummern dürfen zwischen 0 und 127 (je einschließlich) liegen. |
| 45 | Rekordnummer zu gross | VDOS kann maximal 65536 Rekords à 128 Bytes verwalten. Abhängig von der in `|OPEN` definierten aktuellen Rekordpufferlänge ändert sich die maximale Rekordanzahl. Z.B. bei 512 Bytes Puffergröße sind maximal 16384 Rekords verwaltbar. |
| 53 | Kanal nicht definiert | Es wurde versucht, einen Kanal zu öffnen, der zuvor nicht definiert wurde. |
| 55 | Rekord enthält keine Daten | Es wurde versucht, einen Rekord zu lesen, der nicht mehr in der Blockbelegungstabelle ausgewiesen ist. **Achtung:** Dieser Fehler kann nicht unbedingt dazu benutzt werden, das Ende einer relativen Datei zu testen. Grund: Ist die aktuelle Rekordlänge kleiner als die Blocklänge (4 KB bei vortex Floppies, 1 KB beim 3"-Laufwerk), so gehen mehrere Rekords in einen Block. Ist nun z.B. nur der erste Rekord im letzten in der Blockbelegungstabelle aufgeführten Block noch belegt, so kommt Fehler 55 erst dann, wenn man versucht, einen Rekord im nächsten Block anzusprechen. Bei kleinen Feldlängen kann sich dessen Rekordnummer unter Umständen stark von der des letzten tatsächlich belegten Rekords unterscheiden. Man sollte deshalb immer mit Indexdateien arbeiten, also zusätzlich zur Datendatei eine zweite sogenannte Indexdatei mitführen, in der Datenrecordnummern und sonstige Informationen verwaltet werden. |
| 14 | (kein Meldetext) | Datei nicht geöffnet. Es wurde versucht, mit `CLOSEIN` oder `CLOSEOUT` eine sequentielle Datei zu schließen, die nicht geöffnet war. |
| 15 | (kein Meldetext) | Physikalisches (tatsächliches) Ende einer sequentiellen Datei wurde erreicht. |

Alle oben aufgeführten Meldungen sind vom VDOS Betriebssystem erzeugt worden.

Fehlercodes, die direkt vom FDC (Typ µPD 765 von NEC) kommen, haben Bit 6 gesetzt, Bit 7 gelöscht und liegen deshalb zwischen 64 und 127. Die Bedeutung der einzelnen Bits ist folgende:

| Bit | Bedeutung (falls Bit gesetzt) |
|-----|-------------------------------|
| 7 | immer 0 |
| 6 | immer 1 |
| 5 | CRC Fehler im Daten- oder ID-Feld |
| 4 | FDC wurde in einem Datenübertragungsprozeß mit dem Rechner innerhalb eines bestimmten Zeitraums nicht bedient. |
| 3 | Das Laufwerk meldet "not ready". Bedeutet meistens, daß keine Diskette im Schacht ist, oder der Auswurfknopf nicht richtig arretiert wurde. |
| 2 | FDC kann während der Ausführung einer Leseoperation den gewünschten Sektor nicht finden. |
| 1 | FDC erhält während einer Schreib- oder Formatieroperation ein "Write protect" Signal vom Laufwerk. D.h. die Diskette hat einen Schreibschutz. |
| 0 | FDC kann nach dem zweiten "Überfliegen" des Indexlochs das ID-Feld nicht finden. |

Ein häufiger Fehlercode dürfte wohl 72 sein, oder binär `01001000`, und bedeutet, daß sich keine Diskette im Laufwerk befindet.

Wurden die Floppy Disk Fehlermeldungen nicht mit `|DERROR` abgeschaltet, so erfolgt eine Ausgabe auf dem Bildschirm. Um dem Programmierer dies anzuzeigen, wird deshalb in diesem Fall das 7. Bit im Fehlerbyte gesetzt, d.h. 128 zu obigen Fehlercodes addiert. Z.B.

| Fehlercode | Bedeutung | Fehlermeldung |
|------------|-----------|---------------|
| 21  | Diskette voll | abgeschaltet |
| 149 | Diskette voll | eingeschaltet |

> **(!) Wichtig**
>
> Floppy-Fehler, die in der Folge keinen BASIC-Fehler erzeugen, können auch nicht mit `ON ERROR GOTO` abgefangen werden, sondern es muß jeweils nach dem Befehl auf Fehler abgefragt werden:
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
> Befindet sich in Zeile 30 keine Diskette im Laufwerk, so geht `CAT` ins "Leere", erzeugt hierbei aber keine BASIC Fehlermeldung, d.h. verzweigt nicht nach Zeile 100. Abgefangen wird der Fehler in Zeile 40 und Zeile 50.

> **(!) Wichtig**
>
> Der `|DERROR` Befehl ohne Parameter entfällt beim CPC664 und CPC6128, da BASIC 1.1 im Falle eines Diskettenfehlers von sich aus bereits die Variable `DERR` anlegt und dies nicht mehr wie bei BASIC 1.0 (CPC464) erst veranlaßt werden muß. Die Befehle `|DERROR,0` und `|DERROR,1` können Sie natürlich weiterhin dazu verwenden, die Diskettenfehlermeldungen ein- bzw. auszuschalten.

Beachten Sie hier bitte auch den Anhang "Das EOF Problem" am Ende dieses Handbuches.

---

## Die VDOS Turnkey Funktion

**Für CPC464+DDI-1 und X-Laufwerk**

Turnkey hat nichts mit der Türkei oder einem Truthahn zu tun. Turnkey heißt so viel wie "Schlüssel reinstecken, rumdrehen und fertig". Bei Ihrem Computersystem bedeutet das: "Diskette einlegen, Gerät einschalten, fertig".

Mit der Turnkey-Funktion kann in der Tat vom Einschalten ab das System in einen bestimmten Betriebszustand hochgefahren werden. Dazu folgendes Beispiel: Stellen Sie sich vor, Sie möchten den CPC nur dazu benutzen, um mit dem WordStar Ihre Korrespondenz zu erledigen. D.h. es ist Ihnen eigentlich sehr lästig, vor jeder Benutzung erst einmal das CP/M zu laden, dann den WordStar zu starten und eventuell noch einen alten Brief hereinzuladen. Es wäre Ihnen am liebsten, nur die Diskette einlegen zu müssen, das Gerät einzuschalten und dann sofort im WordStar in Ihrem Brief zu "landen".

Diese Aufgabe ist für VDOS kein Problem. Wir haben nämlich die Turnkey-Funktion eingebaut: jedesmal wenn der Rechner rückgesetzt (resetiert, gleichzeitiges Drücken der `CTRL`+`SHIFT`+`ESC`-Tasten) wird – auch das Aus-/Einschalten ist ein Reset –, sucht VDOS auf einer eventuell ins 3"-Laufwerk eingelegten Diskette nach einer Datei mit der Bezeichnung `HELLO.BAS`. Findet VDOS diese Datei, dann wird sie automatisch gestartet (entspricht `RUN "HELLO"<ENTER>`).

Die Hello-Datei hat z.B. folgendes Aussehen:

```basic
10 |CPM
Ready
SAVE "HELLO"<ENTER>
```

Mit dem `SAVE`-Befehl haben wir die Datei gleich "in Sicherheit gebracht". Ja, so einfach ist das. Dieser kleine Einzeiler startet das CP/M. Das wäre der erste Schritt.

Jetzt machen wir noch von der Möglichkeit des **Autostart-Strings** Gebrauch. Das ist eine Zeile, die aus CP/M Befehlen besteht, die nach dem Laden von CP/M direkt ausgeführt wird. Diesen Autostart-String können wir mit dem CP/M Befehl `INSTALL` anlegen. Der String könnte z.B. folgendes Aussehen haben:

```
WS BRIEF.TXT<0D>
```

D.h. nach dem Laden von CP/M würde sofort der WordStar (`WS.COM`) gestartet werden. Gleichzeitig würde dann die Korrespondenz `BRIEF.TXT` hereingeladen werden, und wir hätten erreicht, was wir wollten.

Wollen Sie das Suchen nach der Hello-Datei unterbinden, dann bleiben Sie beim RESET oder beim Einschalten einfach z.B. auf der `ESC`-Taste oder auch der `ENTER`-Taste. Es wird dann gar nicht lange gesucht, sondern es erscheint gleich `Ready`.

---

## X-Laufwerke am CPC464 mit DDI-1, CPC664 und CPC6128

Alles hier Besprochene bezieht sich auf folgende Gerätesets:

| Computer | + Laufwerke |
|----------|-------------|
| CPC464 + DDI-1 | vortex F1-X und M1-X |
| CPC664         | vortex F1-X und M1-X |
| CPC6128        | vortex F1-X und M1-X |

Diese CPC's sind dadurch ausgezeichnet, daß sie bereits von Anfang an mit einem 3"-Laufwerk ausgerüstet sind. Natürlich verfügen sie deshalb auch über einen Floppy Controller. Auf Grund dieser Tatsache wird auch bei diesen Geräten das CP/M 2.2 Betriebssystem und beim CPC6128 zusätzlich noch das CP/M 3.0 (auch CP/M plus genannt) mitgeliefert.

Sie werden im Lieferumfang Ihres vortex X-Laufwerks eine vortex Systemdiskette finden, die das CP/M nicht enthält. Warum auch? Sie haben es ja bereits "gekauft", es muß nur noch auf die vortex Systemdiskette gebracht werden. Ich werde Ihnen gleich zeigen, wie wir das machen.

**Für Skeptiker…**

> Bitte beachten Sie, daß es sich hierbei keinesfalls um eine "Lizenzverschieberei" handelt. Das Entscheidende ist, daß sich die Anzahl der Computer (Arbeitsplätze), auf denen Sie das CP/M (2.2 und plus) benutzen, nicht vergrößert. Sie haben noch immer nur einen Computer!

---

## Erzeugen einer vortex CP/M 2.2 Systemdiskette

Da die vortex Floppies unter CP/M 2.2 nicht nur 64 (wie beim 3"), sondern 128 Einträge im Disketteninhaltsverzeichnis verwalten können und die Verwaltung des Inhaltsverzeichnisses auch RAM-Speicher kostet, müssen wir vor dem eigentlichen Erstellen der vortex Systemdiskette erst einmal das CP/M 2.2 auf Ihrer 3"-Diskette verkleinern.

Legen Sie also eine Kopie Ihrer 3" CP/M 2.2 Systemdiskette (auf keinen Fall das Original!!) in das 3"-Laufwerk ein und starten Sie durch die Eingabe `|CPM<ENTER>` das CP/M 2.2 Betriebssystem. Dies meldet sich durch die Lademeldung:

```
CP/M 2.2 - Amstrad Consumer Electronics plc

A>
```

Wenn Sie sich den Inhalt der Diskette mit `A>DIR<ENTER>` anschauen, dann finden Sie auch die beiden CP/M Befehle `MOVCPM.COM` und `SYSGEN.COM`. Genau diese beiden Programme brauchen wir, um das CP/M etwas zu verkleinern. Keine Angst, wir brauchen nicht viel Speicher. Nur 256 Bytes (eine sogenannte Page). Ihr CP/M 2.2 hat jetzt noch 179 Pages, wir machen daraus 178 Pages.

Zuerst starten wir das Programm `MOVCPM`:

```
A>MOVCPM 178 *<ENTER>

CONSTRUCTING 44k CP/M vers 2.2
READY FOR "SYSGEN" OR "SAVE 34 CPM44.COM"
```

Dann starten wir `SYSGEN`, mit dem wir das soeben verkleinerte CP/M auf die Systemspuren der 3"-Diskette schreiben. Bitte achten Sie darauf, daß bei dieser Diskette nicht der "Schreibschutzriegel" vorgelegt wurde.

```
A>SYSGEN *<ENTER>

SYSGEN V2.0

Please insert DESTINATION disc into drive A then press any key:
Do you wish to reconfigure another disc (Y/N) ? :N

Please insert a CP/M system disc into drive A then press any key:

SYSGEN V2.0 finished

A>
```

Sie lassen immer diese Diskette im 3"-Laufwerk liegen, antworten einmal mit "N" und drücken ansonsten immer irgendeine Taste, bis dann wieder das CP/M Prompt `A>` erscheint.

Geben Sie jetzt noch folgendes ein:

```
A>AMSDOS<ENTER>

(C)1985   VDOS 2.0-X by vortex GmbH
BASIC 1.1

Ready
```

Sie sind jetzt wieder ins BASIC zurückgekommen. Legen Sie jetzt bitte die mitgelieferte vortex Diskette ins X-Laufwerk ein und starten Sie durch die Eingabe von

```
|CPM,1<ENTER>
```

das modifizierte CP/M 2.2 Betriebssystem. Es meldet sich jetzt mit der Lademeldung:

```
CP/M 2.2 - Amstrad Consumer Electronics plc
44K CP/M vers. 2.2-03/86 vortex GmbH

A>
```

Damit haben wir Zugriff auf das X-Laufwerk, das jetzt Laufwerk B mit einer Kapazität von 708 KB ist.

Als nächstes holen wir uns von der 3"-Diskette das CP/M 2.2 auf die vortex Diskette herüber. Geben Sie dazu bitte folgendes ein:

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

Damit haben wir das CP/M transferiert. Jetzt holen wir uns noch die CP/M Befehle:

```
XSUB    .COM   SUBMIT  .COM   LOAD    .COM
DUMP    .COM   MOVCPM  .COM   ED      .COM
STAT    .COM   PIP     .COM   DDT     .COM
```

auf die vortex Diskette herüber. Dazu geben wir ein:

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

So, jetzt sind wir fertig. Im X-Laufwerk liegt jetzt Ihre neue vortex CP/M 2.2 Systemdiskette, die Sie brauchen, wenn Sie das CP/M vom X-Laufwerk laden wollen.

Geben Sie nun einmal

```
A>AMSDOS<ENTER>
```

womit wir auf BASIC zurückschalten:

```
(C)1985   VDOS 2.0-X by vortex GmbH
BASIC 1.1

Ready
```

Starten Sie durch die Eingabe von

```
|CPM,2<ENTER>
```

das CP/M 2.2 vom vortex Laufwerk. Wir erhalten folgende Lademeldung:

```
44K CP/M vers.2.2-03/86 vortex GmbH

A>
```

Laufwerk A ist jetzt das vortex X-Laufwerk mit 708 KB und 128 Directory-Einträgen. Laufwerk B ist das 3"-Laufwerk mit ca. 170 KB und 64 Directory-Einträgen.

> **(!) Wichtig:** Folgende Dienstprogramme auf der 3"-Diskette dürfen nicht unter diesem CP/M betrieben werden:
>
> `BOOTGEN.COM`, `DISCKIT2.COM`, `SETUP.COM`, `FORMAT.COM`, `SYSGEN.COM`, alle LOGO Dateien

Um mit LOGO und dem X-Laufwerk arbeiten zu können, müssen Sie eine Kopie der LOGO Diskette ins 3"-Laufwerk einlegen und mit `|CPM<ENTER>` starten. Beachten Sie, daß das X-Laufwerk hier nur über eine Kapazität von ca. 170 KB bei 64 Directory-Einträgen verfügt.

Am besten machen wir uns nun gleich eine Arbeitskopie von der gerade erstellten vortex CP/M 2.2 Systemdiskette. Von nun an sollten wir nur noch mit dieser Arbeitskopie und eventuellen Kopien davon arbeiten, nicht aber mehr mit der zuvor erstellten Systemdiskette.

Zum Erstellen der Kopie bleibt die gerade erstellte Systemdiskette im Laufwerk liegen, die 3"-Diskette brauchen wir jetzt nicht mehr. Außerdem benötigen wir eine neue blanke vortex Diskette. Wir haben das vorhin geladene CP/M nicht verlassen und starten jetzt durch die Eingabe

```
A>DISKTOOL<ENTER>
```

das vortex Dienstprogramm, mit dem auch ganze Disketten kopiert werden können. Daraufhin erhalten wir folgenden Bildschirm:

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

Sie drücken die Taste "2", weil wir ja eine komplette Diskette kopieren wollen. Nach dem Drücken erhalten wir einen neuen Bildschirm:

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

Die Quelle ist die vorhin erstellte vortex Systemdiskette. Das Ziel ist die neue, noch leere vortex Diskette. Quell-Laufwerk und Ziel-Laufwerk sind jeweils "A".

Beantworten Sie die nachfolgenden Fragen also wie folgt:

```
Quell-Laufwerk ? A
Ziel-Laufwerk  ? A
```

Die Frage "mit formatieren..." beantworten Sie mit "J", weil die neue leere Diskette auch erst einmal formatiert werden muß. Die Frage "mit testen..." beantworten wir auch mit "J", weil wir auch noch so kleine Kopierfehler ausschließen wollen.

Der Laufbandtext teilt Ihnen immer mit, wann Sie welche Diskette ins Laufwerk A einlegen müssen.

> **(!) Wichtig:** Vergessen Sie einmal die Diskette zu tauschen, so wird Ihr Kopieroriginal (!!) zerstört. Vorsicht!

Es sollte jetzt die gerade erstellte Kopie im Laufwerk liegen. Lassen Sie sie dort und drücken Sie die `ESC`-Taste. DISKTOOL wird verlassen und es erscheint wieder das CP/M Prompt `A>`. Die im X-Laufwerk liegende Diskette ist das genaue Abbild der zuvor erstellten CP/M 2.2 Systemdiskette.

---

## CPC464, CPC664 mit X-Laufwerk und vortex RAM-Karte

Haben Sie in Ihren CPC eine vortex RAM-Karte eingebaut? Wenn nicht, dann wird es Zeit, Sie versäumen zu viel! Sie kommen nie in den Genuß eines 62K CP/M 2.2. Kein "dBase", kein "Multiplan", kein richtiger "WordStar", kein…

Haben Sie die Karte aber schon eingebaut, dann können Sie das "Große CP/M" auch mit Ihrer neuen vortex Floppy betreiben. Sie müssen dazu lediglich das Programm `XPATCH.COM`, das sich auf der gerade erstellten vortex CP/M 2.2 Systemdiskette befindet, zu starten. Dieses Programm funktioniert genauso wie das Programm `PATCH.COM` – es ersetzt dieses vollständig –, das zum Lieferumfang der RAM-Karte gehört.

---

## Erstellen einer vortex CP/M plus Diskette (nur CPC6128)

Wenn Sie einen CPC6128 besitzen, haben wir da ja noch das CP/M plus. Das lassen wir auf keinen Fall unter den Tisch fallen. Auch hier werden wir uns eine entsprechende vortex Diskette erstellen, von der Sie dann das CP/M plus laden können.

Bevor Sie die vortex CP/M plus Systemdiskette erstellen können, müssen Sie (wie oben erklärt) eine vortex CP/M 2.2 Diskette erstellt haben. Stecken Sie ins 3"-Laufwerk die vorhin geänderte 3" CP/M 2.2 Systemdiskette. Stecken Sie die vortex CP/M 2.2 Systemdiskette ins X-Laufwerk und starten Sie durch die Eingabe von

```
|CPM,1<ENTER>
```

das geänderte CP/M 2.2 Betriebssystem vom 3"-Laufwerk. Es meldet sich mit:

```
CP/M 2.2 - Amstrad Consumer Electronics plc
44K CP/M vers. 2.2-03/86 vortex GmbH
A>
```

Starten Sie jetzt durch die Eingabe von

```
A>B:<ENTER>
B>XPATCH30<ENTER>
```

das auf der mitgelieferten vortex Diskette – nunmehr Ihre Original vortex CP/M 2.2 Systemdiskette – befindliche CP/M plus Patch-Programm. `XPATCH30` kann nur unter einem CP/M 2.2 benutzt werden, welches mit `|CPM,1<ENTER>` auf einem CPC6128 gestartet wurde. Sollten Sie versuchen, `XPATCH30` unter CP/M plus zu starten, so erhalten Sie die Meldung:

```
XPATCH30 kann nur unter CP/M 2.2 gestartet werden
```

und das Programm bricht ab. Nehmen wir also an, alles läuft nach Plan, so kommt nach dem Starten von `XPATCH30` die Meldung:

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

Legen Sie nun also eine Kopie Ihrer CP/M Plus Systemdiskette ins eingebaute 3"-Laufwerk ein und drücken Sie irgendeine Taste. `XPATCH30` bringt die Meldung:

```
C10CPM3.EMS Datei wird gelesen...
```

`XPATCH30` holt sich nun also das CP/M Plus Betriebssystem (dieses liegt beim 6128 in einer Datei der Extension `EMS`) von der Kopie der 3" CP/M Plus Diskette und ändert es für die Benutzung mit dem X-Laufwerk ab. `XPATCH30` fragt Sie nun, ob Sie eine 3"- oder eine 5,25"-CP/M Plus Diskette haben möchten. Nehmen wir einmal an, wir möchten eine 5,25"-Diskette, so antworten wir auf die Frage:

```
Soll 3" Laufwerk = Laufwerk A sein (J/N) ? N
```

mit N(ein). `XPATCH30` schreibt nun auf die 5,25"-Diskette im B-Laufwerk (dort ist natürlich eine formatierte Diskette, oder?) das abgeänderte CP/M Plus Betriebssystem, welches den Namen `CPM3.EMS` erhält.

```
CPM3.EMS wird geschrieben...
```

Selbstverständlich benötigt die 5,25"-Diskette auch einen neuen Bootsektor, der geeignet ist, das CP/M Plus Betriebssystem zu laden. `XPATCH30` meldet deshalb in diesem Fall:

```
Bootsektor wird angelegt.

5.25"/3.5" CP/M Plus-X MASTER-DISKETTE wurde hergestellt.
```

Anschließend teilt Ihnen `XPATCH30` nochmals in Kurzform mit, welche Möglichkeiten Sie haben, CP/M Plus zu starten:

**Sie haben nun drei Möglichkeiten, CP/M Plus zu starten:**

1. **CP/M Plus Originaldiskette im 3"-Laufwerk:** `|CPM<ENTER>` startet vom 3"-Laufwerk CP/M Plus. Laufwerk B wird als einseitiges 40-Spur-Laufwerk mit 64 Directories verwaltet.
   > **(!) Achtung:** 5,25"-Disketten, die in diesem Modus bearbeitet werden, dürfen niemals (!) unter VDOS oder unter einem CP/M (2.2 und Plus), das mit `|CPM,1` oder `|CPM,2` gestartet wurde, verwendet werden.

2. **Gepatchte CP/M Plus Diskette im 3"-Laufwerk:** `|CPM<ENTER>` oder `|CPM,1<ENTER>` startet vom 3"-Laufwerk CP/M Plus. Konfiguration: Laufwerk A = 3", Laufwerk B = 5,25" mit 708 kB und 128 Directories.

3. `|CPM,2<ENTER>` startet von 5,25"/3,5"-Laufwerk CP/M Plus. Laufwerk A = 5,25" mit 708 kB und 128 Directories, Laufwerk B = 3".

```
3" CP/M 2.2 Diskette mit XPATCH30 wieder in 3" Laufwerk
einlegen und irgendeine Taste druecken
```

Machen Sie sich von der gerade erstellten CP/M plus Systemdiskette am besten gleich eine Arbeitskopie (mit `DISKTOOL`, wie bei der Erstellung einer vortex CP/M 2.2 Systemdiskette beschrieben).

### Hier noch ein paar Hinweise

1. Die Bildschirmverschnellerung `FAST.COM` und der Z80 Monitor `XMON` arbeiten nur unter dem 44K CP/M 2.2 Betriebssystem, nicht aber unter CP/M plus. Die Dienstprogramme `DISKTOOL`, `FILECOPY`, `SYSGEN`, `INSTALL`, `CASCOPY`, `VDOS` arbeiten ebenfalls nur unter einem CP/M 2.2 (auch 62K!).

2. Wenn Sie das CP/M plus von BASIC aus starten (`|CPM,2<ENTER>`), so ist darauf zu achten, daß im 3"-Laufwerk eine Diskette liegt. Liegt dort keine, dann erkennt CP/M plus nur ein Laufwerk an. (Das passiert Ihnen übrigens auch ohne vortex Floppy, wenn Sie z.B. das 3"-Zweitlaufwerk an Ihren CPC6128 anschließen.) Die ordnungsgemäße Lademeldung sieht dann wie folgt aus:

   ```
   CP/M Plus Amstrad Consumer Electronics plc

   v 1.0, 61K TPA, 2 disc drives

   A>
   ```

3. Es dürfen alle CP/M plus Programme bis auf das Programm `DISCKIT3.COM` von der 3"-Diskette auf die vortex Diskette übertragen werden.

> **(!) Wichtig:** Verwenden Sie `DISCKIT3.COM` im Zusammenhang mit den X-Laufwerken, so kann das unter Umständen verheerende Folgen haben.

Möchten Sie also z.B. Dateien unter CP/M Plus von Laufwerk A nach B oder umgekehrt übertragen, so verwenden Sie hierzu das Programm `PIP`. Falls Sie ganze Disketten kopieren möchten, so verlassen Sie CP/M Plus, starten CP/M 2.2 und arbeiten dort mit `DISKTOOL`.

---

## Das Laden des CP/M Betriebssystems

Bei den X-Laufwerken gibt es 3 Möglichkeiten, das CP/M zu laden:

### Der VDOS Befehl |CPM

Das CP/M wird vom 3"-Laufwerk von einer Kopie der Original Schneider CP/M Systemdiskette geladen. Wir erhalten folgende Lademeldung:

```
|CPM<ENTER>
CP/M 2.2 - Amstrad Consumer Electronics plc
A>
```

- Laufwerk A ist das 3"-Laufwerk mit ca. 170 KB.
- Laufwerk B ist das X-Laufwerk mit ca. 170 KB.

Hier wird Laufwerk B als 40-Spur/Einseitig-Laufwerk mit einer Kapazität von ca. 170 KB bedient. Das liegt daran, daß das Original AMSDOS – nur das garantiert eine 100%ige Kompatibilität zu bestehender 3"-Software – eben nur Laufwerke dieser Kapazität verwalten kann.

Beachten Sie aber, daß diese 40 Spuren nicht über den ganzen Diskettenradius verteilt sind (Normalfall), sondern daß das Laufwerk noch immer 80 Spuren abfahren kann, aber nur die ersten 40 auf der Vorderseite benutzt. Diese Lademöglichkeit ist mit dem Fall identisch, wo Sie gar kein X-Laufwerk haben, sondern z.B. nur ein 3"-Zweitlaufwerk.

> **(!) Hinweis:** Die Disketten, die unter diesem CP/M erstellt und benutzt werden, können im Falle, daß VDOS eingeschaltet ist, nicht benutzt werden. Halten Sie diese beiden "Diskettensorten" sauber auseinander (von außen kennzeichnen!). Benutzen Sie sie trotzdem, müssen Sie mit einem kompletten Datenverlust rechnen.

Die Disketten, die Sie hier für Ihr X-Laufwerk benötigen, müssen Sie mit dem CP/M Befehl `FORMAT` oder `DISCKIT` (auf der Kopie der Original Schneider CP/M Systemdiskette) in diesem speziellen Format formatieren.

### Der VDOS Befehl |CPM,1

Das CP/M wird vom 3"-Laufwerk von einer modifizierten Kopie der Original Schneider CP/M Systemdiskette geladen. Wir erhalten folgende Lademeldung:

```
|CPM,1<ENTER>
X-Laufwerke Benutzerhandbuch VDOS und CP/M   (C)1986 vortex GmbH

CP/M 2.2 - Amstrad Consumer Electronics plc
44K CP/M vers. 2.2-03/86 vortex GmbH

A>
```

- Laufwerk A ist das 3"-Laufwerk mit ca. 170 KB.
- Laufwerk B ist das X-Laufwerk mit 708 KB.

Was an diesem CP/M modifiziert wurde, haben Sie im Abschnitt "X-Laufwerke am CPC464 mit DDI-1, CPC664 und CPC6128" gesehen. Dieses CP/M ist nur 178 Seiten groß (statt wie bislang 179 Seiten; das liegt daran, daß das X-Laufwerk mit 128 Directory-Einträgen verwaltet wird).

### Der VDOS Befehl |CPM,2

Das CP/M wird von der Systemdiskette im X-Laufwerk geladen. (Herstellung dieser Diskette siehe Abschnitt "X-Laufwerke am CPC464+DDI-1, CPC664 und CPC6128".) Wir erhalten folgende Lademeldung:

```
|CPM,2<ENTER>

44K CP/M vers. 2.2-03/86 vortex GmbH

A>
```

- Laufwerk A ist das X-Laufwerk mit 708 KB.
- Laufwerk B ist das 3"-Laufwerk mit ca. 170 KB.

> **(!) Wichtig**
>
> Alle drei gezeigten CP/M-Ladebefehle bewirken beim CPC6128 und eingelegter CP/M plus Diskette selbstverständlich das Laden des CP/M plus. Setzen Sie den Rechner zurück (gleichzeitiges Drücken der `CTRL`+`SHIFT`+`ESC`-Tasten), schalten Sie den Rechner AUS/EIN oder laden Sie das CP/M, so geht die mit dem `|X` Befehl eingestellte Vertauschung wieder verloren.

---

## CP/M mit Ihrem vortex X-Laufwerk

Die hier beschriebenen vortex CP/M Befehle benötigen Sie zum Arbeiten mit dem vortex X-Laufwerk unter CP/M 2.2. Haben Sie also das CP/M 2.2 mit `|CPM,1<ENTER>` oder `|CPM,2<ENTER>` geladen, dann können Sie diese Befehle verwenden.

Informationen über das CP/M und seine Befehle entnehmen Sie bitte den entsprechenden Handbüchern, die Sie beim Kauf Ihres CPC's (664 und 6128) oder Ihrer Floppy Station DDI-1 (CPC464) miterhalten haben.

---

## Der CP/M Befehl FILECOPY

**Kopieren von Dateien**

War es mit dem CP/M Befehl `PIP` nicht möglich, als Besitzer nur eines Laufwerks Dateien oder gar ganze Disketten zu kopieren (Sie erinnern sich, das lag immer an den BDOS Errors und dem `CTRL`+`C`), so ist das mit `FILECOPY` überhaupt kein Problem. Zudem ist `FILECOPY` von der Bedienung her noch wesentlich komfortabler und einfacher in der Handhabung.

Auch das umständliche Kopieren von Dateien zwischen verschiedenen USER-Bereichen entfällt. Neben Quell- und Ziel-Laufwerk können Sie noch einen Quell-USER-Bereich und einen Ziel-USER-Bereich angeben.

Außerdem werden alle 16 möglichen "Laufwerke" (Floppies, Harddisks oder RAM-Floppies) unterstützt. Sie sehen sofort beim Starten von `FILECOPY`, welche Laufwerke vorhanden sind und welche formatierte (tatsächliche) Speicherkapazitäten sie haben.

Hier ist eine kleine Besonderheit erwähnenswert: Haben Sie eine vortex Speichererweiterung in Ihren CPC eingebaut, dann haben Sie ab 128 KB zusätzlichem RAM eine RAM-Floppy unter CP/M. Für diese RAM-Floppy ist immer die Laufwerkskennung "C" reserviert.

> **(!) Hinweis:** Beachten Sie aber, daß mit `FILECOPY` kein Transfer von Daten zwischen externen Einheiten durchgeführt werden kann. `FILECOPY` ist ein reines Dienstprogramm für Laufwerk/Laufwerk Datenübertragung.

Wir starten `FILECOPY` durch die Eingabe von

```
A>FILECOPY<ENTER>
```

`FILECOPY` verfügt über zwei Menüs:

- Das **"Einstell-"-Menü**, in dem Sie Quelle und Ziel einstellen
- Das **"Kopier-"-Menü**, in dem Sie dann die Dateien "aussuchen" können, die kopiert werden sollen.

Hauptsächlich werden wir in beiden Menüs die Cursor-Tasten, die `COPY`- und die `ENTER`-Taste benötigen. Andere Tasten werden selten benötigt.

Der Bildschirm ist immer in fünf "Fenster" unterteilt:

- **Fenster 1** zeigt die Dateien an, die sich auf der Quell-Diskette befinden oder die kopiert werden sollen (Inverse Video Darstellung).
- **Fenster 2** zeigt uns immer, mit "welchen" Tasten "was" gemacht werden kann.
- **Fenster 3** zeigt, welches Laufwerk und welcher USER-Bereich Quelle und welches Laufwerk und welcher USER-Bereich Ziel ist.
- **Fenster 4** zeigt uns die vorhandenen Laufwerke und deren formatierte Speicherkapazitäten. Hier haben wir zwei Möglichkeiten, je nach dem, ob wir das CP/M mit `|CPM,1<ENTER>` (Laufwerk A = 3"-Laufwerk mit 169 KB und Laufwerk B = X-Laufwerk mit 704 KB) oder mit `|CPM,2<ENTER>` (Laufwerk A = X-Laufwerk mit 704 KB und Laufwerk B = 3"-Laufwerk mit 169 KB) laden. In Fenster 3 können auch die USER-Nummern geändert werden. Diese laufen von 0 bis F, dies sind Hexadezimalziffern; hier eine kurze "Übersetzung":

  | Dezimal | Hexadezimal |
  |---------|-------------|
  | 0 – 9   | 0 – 9       |
  | 10      | A           |
  | 11      | B           |
  | 12      | C           |
  | 13      | D           |
  | 14      | E           |
  | 15      | F           |

- **Fenster 5** ist ein sogenanntes "Laufband". Der Text, der hier ausgegeben wird, läuft mit kontinuierlicher Geschwindigkeit am unteren Bildschirmrand entlang. Hier werden Fehlermeldungen, die Bitte die Diskette zu wechseln und derartige Meldungen angezeigt.

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

Fenster 5 meldet uns "Bitte entsprechende Taste druecken!"
Interessant ist hier Fenster 2:

- Mit der "Cursor nach oben" Taste kann das Quell-Laufwerk geändert werden. Es gibt hier so viele Wahlmöglichkeiten, wie in Fenster 4 Laufwerke angezeigt werden.
- Mit der "Cursor nach unten" Taste kann das Ziel-Laufwerk eingestellt werden.
- Mit der "Cursor nach links" Taste kann der USER-Bereich auf der Quell-Diskette eingestellt werden, d.h. aus diesem Bereich werden die zu kopierenden Daten geholt.
- Mit der "Cursor nach rechts" Taste kann der USER-Bereich auf der Ziel-Diskette eingestellt werden, d.h. in diesen Bereich werden die Daten, von der Quell-Diskette kommend, kopiert.

Erinnern Sie sich noch, wie umständlich das mit dem `PIP` Befehl war.

Drücken Sie die `COPY`-Taste, so wird in Fenster 1 das alphabetisch geordnete Inhaltsverzeichnis der Quell-Diskette ausgegeben. Durch das Drücken irgendeiner Taste können Sie diese Ausgabe anhalten und durch ein nochmaliges Drücken wieder starten.

Drücken wir die `ESC`-Taste, dann wird `FILECOPY` beendet und wir kehren nach CP/M zurück, wobei zuvor noch dieser Laufbandtext:

```
CP/M-Diskette in Laufwerk A einlegen und beliebige Taste druecken!
```

Drücken Sie die `ENTER`-Taste, so sollten Sie zuvor Quelle und Ziel festgelegt haben. Fenster 2 wird mit einem neuen Inhalt versehen, Fenster 1 wird gelöscht und das Inhaltsverzeichnis der Quelle wird von unten nach oben bis zu den Markierungen (rechts und links am Fenster 1) gefahren.

Das neue Fenster 2 sieht dann wie folgt aus:

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

Das Laufband zeigt wieder `Bitte entsprechende Taste druecken!` an.

Mit den "Cursor hoch/runter" Tasten können in Fenster 1 beliebige Dateien zwischen die beiden Markierungen gebracht werden. Drücken wir nun die `COPY`-Taste, so wird diese Datei "Inverse Video" dargestellt. Wir haben diese Datei als zu kopieren markiert. So können wir eine ganze Reihe, auch alle Dateien (fahren Sie dazu auf den Anfang des Inhaltsverzeichnisses und drücken Sie permanent die `COPY`-Taste) zum Kopieren markieren. Fahren wir eine Datei an, die bereits markiert wurde, und drücken dann die `COPY`-Taste, dann wird die Markierung wieder aufgehoben.

Drücken wir dann die `ENTER`-Taste, so beginnt der Kopiervorgang.

Ist Quelle und Ziel nicht gleich (zwei Laufwerke oder 1 Laufwerk und RAM-Floppy), dann brauchen wir keine Disketten zu tauschen. `FILECOPY` teilt uns mit, wann es von der Quelle liest und wann es die Ziel-Diskette beschreibt.

Haben wir nur ein Laufwerk oder wollen wir bewußt nur mit einem Laufwerk kopieren, dann meldet uns das Laufband permanent, wann wir die Quell-Diskette herausnehmen müssen und dafür die Ziel-Diskette einlegen müssen.

Es gibt auch noch die Möglichkeit, mittels **Wildcards** zu kopieren. Geben Sie ein "W" ein, dann wird Fenster 2 gelöscht und Sie können dort eine Wildcardbezeichnung eingeben. An Quelle und Ziel können Sie wie gehabt mit den "Cursor nach oben" und "Cursor nach unten" Tasten im Menü davor etwas verstellen. Auf jeden Fall wird mit `W` und der eingegebenen Wildcardbezeichnung die Quell-Diskette "abgescanned" (untersucht) und alle Dateien, die in das Wildcardschema passen, werden auf das Ziel kopiert. Zugelassene Wildcardzeichen sind wie unter CP/M üblich der Stern `*` und das Fragezeichen `?`.

Eine Wildcardschema könnte z.B. wie folgt aussehen:

```
WS*.*
```

Alle Dateien auf der Quell-Diskette, die mit `WS` anfangen (WordStar-Dateien), dann beliebige Zeichen in Dateinamen und Dateityp haben (z.B. `WS.COM`, `WSOVLY1.OVR`, `WSMSGS.OVR` oder `WSU.COM`), werden auf die Ziel-Diskette kopiert.

Ein anderes Wildcardschema wäre z.B.:

```
*.*
```

Damit würden alle Dateien von der Quell-Diskette auf die Ziel-Diskette übertragen werden. Dateiname und Dateityp sind vollkommen beliebig. In dieses Schema passen alle Dateien der Quell-Diskette.

### Beispiel

Starten Sie durch folgende Eingabe `FILECOPY`:

```
A>FILECOPY<ENTER>
```

Der Bildschirm wird gelöscht und der `FILECOPY`-Bildschirm erscheint. 

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

In FENSTER 3 ist als Quell- und Ziel-Laufwerk jeweils Laufwerk A User 0 voreingestellt.

In FENSTER 4 werden die vorhandenen Laufwerke angezeigt. In unserem Fall (Laufwerk A = X-Laufwerk, Laufwerk B = 3"-Laufwerk; das CP/M wurde also mit `|CPM,2<ENTER>` geladen) sieht FENSTER 4 konkret so aus:

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

Sie sehen, `FILECOPY` ist ganz schön "intelligent", es kann alle unter CP/M möglichen Laufwerke (16 Stück A…P) verwalten.

In FENSTER 5 sehen wir ein Laufband mit folgendem Text:

```
Bitte entsprechende Taste druecken !
```

Nehmen wir einmal an, daß die Diskette, von der wir `FILECOPY` gestartet haben, nicht die Quell-Diskette ist, dann nehmen wir jetzt die nach ins X-Laufwerk eingelegte Diskette heraus und legen dafür die Quell-Diskette ein. Schauen wir uns doch einfach mal an, was auf dieser Diskette an Dateien vorhanden ist. Drücken Sie dazu die `COPY`-Taste. FENSTER 1 sieht dann z.B. so aus:

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

Das sind also die Dateien, die sich auf der Quell-Diskette befinden. Wir interessieren uns für eine bestimmte Datei `VDOS.COM`. Diese wollen wir auf die Ziel-Diskette – sie liegt neben uns – übertragen.

Sie finden in FENSTER 2 den Menüpunkt `ENTER - Weiter zum naechsten Menue`. Im nächsten Menü können wir die Datei(en) aussuchen, die wir kopieren wollen. Drücken Sie also die `ENTER`-Taste. Daraufhin erhält FENSTER 2 einen neuen Inhalt und FENSTER 1 wird gelöscht.

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
Fenster 1 wird erneut mit dem Inhaltsvereichnis der Quell-Diskette gefüllt (siehe Bild 1)

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

Mit den "Cursor hoch/runter" Tasten verschieben wir das ganze Inhaltsverzeichnis nach oben, bis zwischen den beiden "Marken" die Datei `VDOS.COM` zu stehen kommt.

Drücken Sie jetzt die `COPY`-Taste. `VDOS.COM` wird Inverse Video gekennzeichnet. Durch das Drücken der `ENTER`-Taste starten wir das Kopieren. FENSTER 1 wird gelöscht und die einzelne Datei `VDOS.COM` wird angezeigt. FENSTER 5 zeigt uns folgendes:

```
Bitte Quell-Diskette einlegen und beliebige Taste druecken!
```

FENSTER 2 wird gelöscht und uns wird mitgeteilt:

```
Einlesen von Daten. Bitte warten ...
```

Das Laufband ändert sich in:

```
Bitte Ziel-Diskette einlegen und beliebige Taste druecken !
```

Wir nehmen die Quell-Diskette heraus und legen dafür die Ziel-Diskette (diese muß zuvor formatiert worden sein!) ein und drücken dann eine beliebige Taste.

FENSTER 2 enthält dann eine neue Information:

```
Schreiben von Daten. Bitte warten ...
```

Ist das Kopieren beendet, dann wird FENSTER 2 wieder mit dem ersten Menütext gefüllt. Drücken Sie noch einmal `<ESC>`, dann ändert sich die Laufbandmeldung in:

```
CP/M Diskette in Laufwerk A einlegen und beliebige Taste druecken!
```

Nehmen Sie die Ziel-Diskette heraus und legen Sie die Diskette ein, mit der Sie vorhin CP/M gestartet haben und von der Sie auch `FILECOPY` geladen haben. Drücken Sie dann irgendeine Taste, und es erscheint wieder das Prompt `A>`.

---

## Der CP/M Befehl XMON

**Der Z80 Monitor unter CP/M**

Der Monitor kann auch unter CP/M benutzt werden.

> **(!) Achtung:** Nur CP/M 2.2 ohne RAM-Erweiterung!

Folgende Befehle sind aus Systemgründen unter CP/M blockiert:

```
I, O, Y
```

Alle anderen Befehle können uneingeschränkt benutzt werden.

Aufgerufen wird der Monitor mithilfe des Programms `XMON.COM`. Die Befehlssyntax ist:

```
XMON<ENTER>
```

oder

```
XMON Dateiname.Typ<ENTER>
```

Also z.B.

```
A>XMON<ENTER>
```

oder

```
A>XMON STAT.COM<ENTER>
```

Die erste Variante ruft lediglich den Monitor auf, während die zweite noch die Datei `Dateiname.Typ` ab `100H` in den Speicher lädt. Der Monitor meldet sich nach dem Einsprung mit:

```
<start länge 0100>
*
```

| Wert | Bedeutung |
|------|-----------|
| `start` | Anfang der geladenen Datei (unter CP/M immer `0100`) |
| `länge` | Länge der geladenen Datei |

Nachdem Sie den Monitor wieder mit `<ESC>` verlassen haben, können Sie mit dem CP/M Befehl `SAVE` den Speicher ab `0100H` auf Diskette sichern.

---

## Der CP/M Befehl SYSGEN

**CP/M auf Systemspuren schreiben**

Wie Sie wissen, wird mit dem Befehl `MOVCPM` ein CP/M "neuer" Größe konstruiert. Was wir jetzt noch brauchen, ist eine Möglichkeit, das geänderte CP/M, das im Speicher oder in Form einer Datei auf Diskette liegt, auf die Systemspuren unserer Systemdiskette zu bekommen.

Genau hierfür befindet sich das Programm `SYSGEN` (SYStem GENerator) auf der Systemdiskette. `SYSGEN` ist ein transienter CP/M Befehl.

Bevor wir hier fortfahren, möchte ich Ihnen kurz zeigen, wie die beiden Systemspuren tatsächlich aussehen.

| Spur | Sektor 01 | 02   | 03   | 04   | 05   | 06   | 07   | 08   | 09   |
|------|-----------|------|------|------|------|------|------|------|------|
| 0    | Boot      | PARA | leer | leer | leer | leer | leer | CP/M | CP/M |
| 1    | CP/M      | CP/M | CP/M | CP/M | CP/M | CP/M | CP/M | CP/M | CP/M |

Jeder Sektor hat eine Speicherkapazität von 512 Bytes. Der Sektor "Boot", der erste Sektor auf der ganzen Diskette, enthält den sogenannten "Bootstrap-Loader". Das ist ein kleines Programm, das direkt durch die Eingabe von `|CPM,2<ENTER>` von der vortex Diskette in den Speicher geladen und dann gestartet wird. Dieser kleine "Lader" holt das eigentliche CP/M von Spur 0 und Spur 1, installiert es im Speicher und läßt es gezielt anlaufen. Nach diesem Vorgang wurde bereits die CP/M Lademeldung ausgegeben und das Prompt `A>` mit dahinter blinkendem Cursor ist erschienen.

Der Sektor "PARA" enthält z.B. Tastaturumdefinitionen oder die Bildschirmfarbe, die beim Laden von CP/M dann automatisch eingestellt wird. Der Inhalt dieses Sektors läßt sich mit dem Programm `INSTALL` (weiter hinten beschrieben) ändern.

Die Sektoren 3, 4, 5, 6 und 7 auf Spur 0 sind noch leer. Haben Sie eine vortex RAM-Erweiterung, dann sind auch diese Sektoren belegt.

Alle Sektoren, die mit "CP/M" gekennzeichnet sind, enthalten das CP/M Betriebssystem. Genau diese Sektoren (und nur diese) werden von `SYSGEN` beschrieben.

```
A>SYSGEN<ENTER>

SYSGEN 2.0   (C)1985 vortex GmbH

Quelldiskette in Laufwerk A,B oder RETURN ? <ENTER>
Zieldiskette in Laufwerk A,B oder RETURN ? A
Zieldiskette in Laufwerk A einlegen und irgendeine Taste druecken
Noch eine Diskette J/N ? N
Diskette mit Systemspur in Laufwerk A einlegen und irgendeine Taste druecken
```

Durch das erste `<ENTER>` teilen wir `SYSGEN` mit, daß das neue CP/M im Speicher liegt und von dort geholt werden soll. Durch die Eingabe "A" bei der Frage "Zieldiskette Laufwerk A,B oder RETURN ?" legen wir fest, daß das neue CP/M auf die Systemspuren der Diskette in Laufwerk A geschrieben werden soll.

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

In diesem Beispiel ist das CP/M zuvor nicht mit `MOVCPM` geändert worden. Es wird hier einfach von den Systemspuren der Diskette in Laufwerk A gelesen und dann auf die Systemspuren der Diskette in Laufwerk B geschrieben.

```
A>SYSGEN<ENTER>

SYSGEN 2.0   (C)1985 vortex GmbH

Quelldiskette in Laufwerk A,B oder RETURN ? <ENTER>
Zieldiskette in Laufwerk A,B oder RETURN ? <ENTER>
Diskette mit Systemspur in Laufwerk A einlegen und irgendeine Taste druecken
```

Bei dieser `SYSGEN` Benutzung passiert gar nichts. Es wird zwar ein "neues" CP/M aus dem Speicher gelesen, aber dann nicht auf Systemspuren geschrieben.

---

## Der CP/M Befehl DISKTOOL

**Formatieren von Disketten, Kopieren ganzer Disketten, Kopieren der Systemspuren, Kopieren des Parametersektors**

Der CP/M Befehl `DISKTOOL` (transient) ist im wahrsten Sinne des Wortes ein "Disketten-Werkzeug". Er verfügt über eine Vielzahl von wichtigen Funktionen, die das Arbeiten mit den Disketten im Laufwerk erst möglich machen.

Wie `FILECOPY` ist auch `DISKTOOL` ein voll menügesteuertes Programm, das sozusagen auf Knopfdruck die gewünschten Funktionen ausführt.

Wenn Sie `DISKTOOL` mit `A>DISKTOOL<ENTER>` gestartet haben, wird der Bildschirm gelöscht und es wird folgendes Hauptmenü ausgegeben:

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

Wie Sie sehen, können Sie von hier aus in 4 Untermenüs verzweigen oder mit `<ESC>` `DISKTOOL` verlassen und nach CP/M zurückkehren.

Außerdem haben wir hier, wie bei `FILECOPY`, auch einen Laufbandtext, der uns zu etwaigen Aktionen aufruft, die im Zusammenhang mit einer angewählten Funktion stehen.

Der Bildschirm ist in zwei Fenster unterteilt: das obere Fenster zeigt an, welche Funktion wir gerade angewählt haben, das untere Fenster zeigt uns Informationen über den Start und den Ablauf der entsprechenden Funktion.

Gehen wir nun einmal Punkt für Punkt das Hauptmenü durch, um zu sehen, was sich hinter den einzelnen Funktionen verbirgt.

### 1 – Formatieren einer Diskette

Drücken wir die Taste "1", dann ändert sich der Bildschirm:

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

Es ist klar, daß wir hier nur Diskettenlaufwerke angeben können. Eine RAM-Floppy (vortex SP512) oder eine Festplatte (vortex WD10 oder WD20) können mit diesem "Formatierer" nicht bearbeitet werden. Die Auswahl des Laufwerks erfolgt über die entsprechende Laufwerkskennung (normalerweise A oder B). Einfach Taste `A` oder Taste `B` drücken.

Wollten Sie ein mit `DISKTOOL` nicht formatierbares Laufwerk (C-RAM-Floppy oder die Festplatte) anwählen, dann bringt das Laufband folgenden Fehlertext:

```
Kein Diskettenlaufwerk - irgendeine Taste druecken!
```

Haben Sie z.B. nur ein Laufwerk zur Verfügung (z.B. F1-S) und wählen Sie dann Laufwerk B an, dann ist dieses schlicht und ergreifend nicht vorhanden (ein Grund mehr, Ihre F1-S zur F1-D aufzurüsten). `DISKTOOL` antwortet darauf mit folgendem Laufband:

```
Laufwerk nicht verfügbar - irgendeine Taste druecken!
```

Ist die Eingabe korrekt, dann können je nachdem, ob ein 3"-Laufwerk angeschlossen ist (bei X-Laufwerken automatisch, S/D Stationen über das vortex Adapterkabel FDA-1), zwei weitere Untermenüs kommen. Für das 3"-Laufwerk gibt es nämlich verschiedene Formate. Trifft die von Ihnen eingegebene Laufwerkskennung auf das 3"-Laufwerk zu, dann erhalten wir diesen Bildschirm:

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

Wir können hier zwischen drei Formaten wählen, weil genau diese drei Formate auch vom DDI-1 Schneider 3"-Controller beherrscht werden und wir wollen ja kompatibel bleiben. Diese drei Formate haben dort allerdings nur den Sinn, ein paar KiloByte mehr Speicherkapazität aus der 3"-Diskette herauszukitzeln, denn die Speicherkapazität einer 3"-Diskette ist nicht gerade üppig (ca. 170 KB). Da sehen die satten 700 KB einer vortex Diskette schon anders aus, deshalb reicht hier auch ein Format aus.

Das "Herauskitzeln" wird dadurch erreicht, daß man z.B. die Systemspuren wegläßt und damit 2 Spuren mehr mit Daten füllen kann. Nun noch kurz etwas zum Aussehen dieser Formate:

**Systemformat mit CP/M:**

- 512 Byte pro Sektor
- 40 Spuren (0…39)
- 64 Directory-Einträge
- 9 Sektoren pro Spur (`41HEX`…`49HEX`)
- 2 reservierte Spuren, mit CP/M

**Systemformat ohne CP/M (auch Vendorformat genannt):**

- 512 Byte pro Sektor
- 40 Spuren (0…39)
- 64 Directory-Einträge
- 9 Sektoren pro Spur (`41HEX`…`49HEX`)
- 2 reservierte Spuren, aber ohne CP/M

**Data-Only Format:**

- 512 Byte pro Sektor
- 40 Spuren (0…39)
- 64 Directory-Einträge
- 9 Sektoren pro Spur (`C1HEX`…`C9HEX`)
- keine reservierten Spuren

Drücken Sie die entsprechende Zahl für das gewünschte Format und fertig. Es erfolgen die Meldungen:

```
mit testen der Zieldiskette (J/N) ?

Formatieren Spur 039
```

Die Frage "mit testen..." sollten wir mit "J" beantworten, damit sich keine Schreibfehler "einschleichen" können.

Haben Sie mit der eingegebenen Laufwerkskennung ein vortex Laufwerk ausgewählt, dann erhalten Sie folgenden Bildschirm:

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

- Mit "1" wird auf die neu formatierte Diskette gleich das CP/M kopiert. Liegt das 62K CP/M 2.2 der vortex RAM-Erweiterung vor, so wird auch automatisch die Datei `$OSC.SYS` mitkopiert.
- Mit "2" wird nur formatiert.

Das vortex Format ist ein Standard Format:

- 9 Sektoren pro Spur (1…9)
- 512 Bytes pro Sektor
- 80 Spuren pro Seite (0…79)
- 2 Seiten
- 2 reservierte Spuren
- 128 Directory-Einträge

Haben Sie das Formatieren gestartet, dann erhalten wir die Meldungen:

```
mit testen der Zieldiskette (J/N) ?

Formatieren Spur 159
```

Die Frage "mit testen..." sollten wir mit "J" beantworten, damit sich keine Schreibfehler "einschleichen" können.

### 2 – Komplettkopie erstellen

Drücken wir im Hauptmenü die Taste "2", dann ändert sich der Bildschirm:

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

Mit dieser Funktion sind wir in der Lage, ganze Disketten zu kopieren. Im Gegenteil zum Kopieren einzelner Dateien, wo "dateiorientiert" gelesen und geschrieben wird, wird bei diesem Vorgang Spur für Spur gelesen und Spur für Spur geschrieben. Man nennt diesen Kopiervorgang oft auch "physikalisch".

> **(!) Hinweis:** Beachten Sie bitte, daß ein Komplettkopiervorgang immer voraussetzt, daß Quelldiskette und Zieldiskette das gleiche Format haben. Kopieren von 3" auf 5,25" und umgekehrt ist also nicht zulässig.

Auf die Fragen "Quell-Laufwerk ?" und "Ziel-Laufwerk ?" antworten Sie mit den entsprechenden Laufwerkskennungen.

Wenn Sie eine vollkommen neue Diskette (noch nicht formatiert) verwenden wollen, dann geben Sie bei der Frage "mit formatieren..." ein "J" ein. Wenn die Diskette bereits formatiert ist, dann geben Sie "N" ein.

> **(!) Wichtig:** Kopieren Sie von Laufwerk A nach Laufwerk A mit Formatieren und vergessen Sie, die Quell- und Zieldiskette zu tauschen, so wird die Quelldiskette zerstört!!!!!!

Die Frage "mit testen..." sollte mit "J" beantwortet werden. Es wird hier nämlich permanent überprüft, ob alle Daten fehlerfrei übertragen wurden (man nennt das auch "verify").

### 3 – CP/M-System kopieren

Drücken wir im Hauptmenü die Taste "3", dann ändert sich der Bildschirm:

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

Wir haben bei der Erklärung des CP/M Befehls `SYSGEN` (weiter vorne) bereits das "Aussehen" der CP/M Systemspuren (Spur 0 und Spur 1) erklärt. Sie erinnern sich, daß mit `SYSGEN` nicht komplett Spur 0 und Spur 1 kopiert wurde, sondern nur ein Teil, wenn auch der größte. Es handelte sich hierbei um die reinen CP/M Sektoren. Wie wir gesehen haben, gibt es aber auch noch einen BOOT-Sektor (er enthält den CP/M-Lader) und den Parametersektor (enthält z.B. Tastaturübersetzungstabellen). Dann sind da noch ein paar leere Sektoren, die aber im Falle des 62K CP/M's in Verbindung mit unserer RAM-Erweiterung auch "voll" sind.

Will man die kompletten Systemspuren kopieren, also ein funktionsfähiges CP/M kopieren, dann braucht man eine spezielle Funktion und genau diese haben wir hier. Das Quell-Laufwerk enthält die Diskette, von der das komplette CP/M gelesen werden soll. Das Ziel-Laufwerk enthält die Diskette, auf die dieses CP/M kopiert werden soll. Haben wir nur ein Laufwerk, so zeigt uns das Laufband an, wann wir die Disketten tauschen müssen.

Bitte beachten Sie, daß diese Funktion auch die `$OSC.SYS` Datei eines 62K CP/M's kopiert. In jedem Fall erhalten wir nach dem Kopieren ein bootfähiges CP/M.

### 4 – Parametersektor kopieren

Drücken wir im Hauptmenü die Taste "4", dann ändert sich der Bildschirm:

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

Wie schon vorhin erwähnt, ist der Parametersektor ein Teil der Bootspuren (genauer Sektor 2 Spur 0). Er enthält z.B. Tastaturumdefinitionen, Autostart-Strings… Der Inhalt dieses Sektors kann mit dem CP/M Befehl `INSTALL` geändert werden. Oft will man eine bestimmte "CP/M-Einstellung" auch auf andere Disketten übertragen. Man braucht gar nicht das ganze CP/M zu kopieren, es reicht der Parametersektor.

Der zu kopierende Parametersektor wird von der Diskette im Quell-Laufwerk gelesen und auf die Diskette im Ziel-Laufwerk geschrieben. Haben wir nur ein Laufwerk, dann zeigt uns das Laufband an, wann wir die Diskette tauschen müssen.

---

## Der CP/M Befehl INSTALL

**Tastaturbelegung ändern**

In Sektor 2 der Spur 0 einer vortex Diskette befinden sich gewisse Parameter, die z.B. eine andere Tastaturbelegung oder die Floppy Disk Zeitkonstanten beinhalten. Diese Werte können mit dem Befehl `INSTALL` geändert (installiert) werden. `INSTALL` ist menügesteuert und in mehrere "Ebenen" unterteilt. Anschließend finden Sie für jede Ebene ein Beispiel, das Ihnen zeigen soll, wie mit `INSTALL` gearbeitet wird. `INSTALL` ist ein transienter Befehl, d.h. auf Ihrer Diskette muß die Datei `INSTALL.COM` vorhanden sein.

### Beispiel: Floppy Disk Zeitkonstanten ändern

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

| Nr | Parameter | Bereich | Default |
|----|-----------|---------|---------|
| 1 | Motor on Delay | 1,2,…,99 sec | 01 sec |
| 2 | Motor off Delay | 1,2,…,99 sec | 03 sec |
| 3 | Steprate 5,25" vortex Laufwerke | 2,4,…,14 msec | 04 msec |
| 4 | Steprate 3" Schneider Laufwerk | 2,4,…,14 msec | 12 msec |
| 5 | Hauptmenue | | |

```
Ihre Wahl: 1
Neuer Wert: 4 <ENTER>
Ihre Wahl: 5

Neue Parameter installieren J/N ? J
CP/M neu starten J/N ? J

44k CP/M vers. 2.2 - 03/86 vortex GmbH
A>
```

Wir sind in diesem Beispiel vom Hauptmenü in das Untermenü "Floppy Disk Zeitkonstanten" gegangen und haben dort die Zeit "Motor on Delay" von 1 sec auf 4 sec erhöht. Wir haben den neuen Parameter gleich installiert (d.h. er wurde in den Parametersektor geschrieben) und das CP/M neu gestartet.

Durch den CP/M Neustart ist gewährleistet, daß der neue Parameter gleich zum Tragen kommt. Der Inhalt des Parametersektors wird nämlich nur beim Laden des CP/M's ausgelesen.

- Das **"Motor on Delay"** ist die Zeit (Verzögerung) zwischen dem Anlaufen des Laufwerksmotors und der Schreib-/Leseoperation.
- Das **"Motor off Delay"** ist die Zeit, die der Motor nach einem Schreib-/Lesezugriff noch läuft. Wäre diese Zeit 0 sec, so würde sich ein äußerst unruhiger Laufwerkszugriff ergeben. Stellen Sie sich vor, wir hätten einen periodischen Laufwerkszugriff, z.B. pro Sekunde einer: andauernd würde der Motor an- und ausgehen. Stellt man hingegen jetzt eine "Motor aus Verzögerung" ein, die größer als eine Sekunde ist (z.B. 3 sec), dann bleibt der Motor an und wir haben einen sehr "ruhigen" Zugriff, der letztendlich natürlich auch die Lebensdauer der Laufwerke steigert.
- Die **"Steprate"**, auch Spurwechselzeit genannt, ist die Zeit, die der Schreib-/Lesekopf, angetrieben durch einen Schrittmotor (Stepper), von einer Spur zur direkt daneben liegenden Spur braucht. Diese Zeit läßt sich nicht beliebig ändern. Der kleinste Wert ist durch die maximale "Flinkheit" des Steppers festgelegt, der größte Wert durch Schwingungen der Schreib-/Leseköpfe, da bei größer werdender Steprate der Betrieb der Schreib-/Leseköpfe immer "ruppiger" wird.

Diese ganzen Funktionen sind primär für all diejenigen Benutzer gedacht, die sich den vortex Floppy Controller separat, also ohne Laufwerke, gekauft haben und vielleicht andere Laufwerke (z.B. TEAC oder EPSON) als wir einsetzen wollen (brauchen vielleicht etwas andere Werte). Ansonsten dürften Sie nie in eine Situation kommen, wo Sie hier etwas verstellen müßten.

### Beispiel: Tastaturbelegung

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

44k CP/M vers. 2.2 - 03/86   vortex GmbH

A>
```

In diesem Beispiel haben wir von der Möglichkeit Gebrauch gemacht, eine Taste mit einer Funktion (Starten des Programms `STAT`) zu belegen.

Wie Sie gesehen haben, kann neben der Funktionszuordnung auch einfach ein anderer Wert einer beliebigen Taste zugeordnet werden. Man kann z.B. auf die Taste "Y" ein großes "Z" legen und umgekehrt.

Es taucht hier immer wieder der Begriff "Token" auf. Das Token ist nichts anderes als das Zeichen, das wir einer bestimmten Taste zugeordnet haben. Wollen wir einer Taste mehrere Zeichen, also eine Funktion zuordnen, dann brauchen wir die sogenannten "Expansion Tokens" (erweiterte Tokens). Das Zeichen `<80>` in unserem Beispiel ist z.B. ein solches Expansion Token.

Taste 64 ist übrigens die Taste direkt rechts von der `ESC`-Taste. Die Tasten und zugehörigen Nummern können Sie Ihrem Schneider CPC Handbuch entnehmen.

In unserem Beispiel haben wir der Taste 64 nur in der NORM-Ebene eine andere Bedeutung gegeben. Benutzen wir die Taste in Verbindung mit der `SHIFT`-Taste (SHIFT-Ebene) oder der `CTRL`-Taste (CTRL-Ebene), so hat sie dieselbe Funktion wie zuvor.

`<0D>` hat dieselbe Bedeutung wie das Drücken der `ENTER`-Taste.

Haben wir `INSTALL` verlassen und drücken dann die Taste 64, so wird `STAT` gestartet.

Mit Hilfe von `INSTALL` lassen sich also alle Tasten (auch die Cursortasten und der Numerik-Block) anders belegen. Mit der Möglichkeit der Expansion Tokens lassen sich ganze Funktionen einer Taste zuordnen.

> **(!) Hinweis:** Beachten Sie bitte, daß nicht beliebig viele Umbelegungen vorgenommen werden können. Sie sehen, daß mit jeder Neubelegung der freie Platz im Parametersektor kleiner wird.

Die Möglichkeit der freien Tastaturbelegung wird z.B. dann wichtig, wenn Sie ein Programm wie WordStar auf Ihren CPC anpassen wollen. Anstatt hier umständlich mit den Control-Codes zu arbeiten (z.B. `CTRL`+`S` bewegt den Cursor ein Zeichen nach links), belegen wir einfach die Tasten mit den Codes (z.B. Taste "Cursor nach links" mit `CTRL`+`S`).

### Beispiel: Autostart-String

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

44k CP/M vers. 2.2 - 03/86   vortex GmbH

A>
```

Bei jedem Starten von CP/M wird nachgeschaut, ob es einen Autostart-String gibt. Ist er vorhanden, dann werden die Befehle, die in ihm stehen, nacheinander ausgeführt.

Brauchen Sie z.B. CP/M nur, damit Sie mit WordStar arbeiten wollen, dann können Sie einen Autostart-String wie folgt definieren:

```
WS TEXT.TXT<0D>
```

Hiermit wird automatisch WordStar gestartet und die Textdatei `TEXT.TXT` hereingeladen. Das `<0D>` hat dieselbe Bedeutung wie das Drücken der `ENTER`-Taste.

### Beispiel: Communication Interface Parameter

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

Haben Sie eine vortex RS232C Schnittstelle (serielle Schnittstelle) an Ihrem CPC, dann können Sie mit diesem Menüpunkt Parameter wie z.B. die Baudrate einstellen.

### Spezialanwendung: Bildschirmfarben ändern

Zum Schluß möchte ich Ihnen noch eine ganz spezielle Anwendung der Funktion "Autostart String" zeigen. Es geht darum, die Bildschirmfarben beim Laden von CP/M zu ändern.

Wir wählen als Hintergrundfarbe "Grau" und als Schreibstiftfarbe "Schwarz". Für Farbmonitorbesitzer ergibt sich mit diesem Farbenpaar vor allem im 80-Zeichen-Modus ein sehr guter Kontrast.

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

44k CP/M vers. 2.2 - 03/86   vortex GmbH

A> ^\@ww^a@@^]ww^M
?
A>
```

Sofort nachdem obiger String abgeschickt wurde, ändern sich die Bildschirmfarben.

> **(!) Hinweis:** Bitte beachten Sie, daß bei der Eingabe der Stringkette im `INSTALL` die "<" und ">" nicht miteingegeben werden müssen.

---

## Der CP/M Befehl CASCOPY

**Kopieren zwischen Diskette und Cassette**

Im Falle eines CPC464 oder eines CPC664 und CPC6128 mit Datenrekorder verfügen Sie neben der Floppy noch über den Datenrekorder, der keinesfalls vergessen werden sollte, obwohl CP/M im Zusammenhang mit einem Datenrekorder so gut wie nie gesehen wird.

Der Datenrekorder mit seinen handelsüblichen Musikcassetten ist ein sehr billiges Speichermedium, das z.B. zu Sicherungszwecken (Back Up) nicht all zu wichtiger Daten durchaus verwendet werden kann.

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

In diesem Beispiel wird gezeigt, wie wir die Datei `ED.COM` von Diskette nach Cassette (`>`) übertragen können. Als Namen der Datei auf der Cassette haben wir `E1.COM` gewählt. Hätten wir anstatt `E1.COM` nur `<ENTER>` eingegeben, so hätte die Datei auf der Cassette ebenfalls die Bezeichnung `ED.COM` erhalten.

Die Übertragung erfolgt mit hoher Geschwindigkeit (geht schneller). Der Rekorder wird, wie wir das von einem normalen Musikrekorder gewohnt sind, durch das gleichzeitige Drücken der REC- und PLAY-Taste auf "Aufnahme" geschaltet.

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

Genau der reverse Fall: Übertragen einer Datei von Cassette auf Diskette. Die Datei wird auf der Diskette auch den Namen `TEST` bekommen (kein Dateityp). Hätten wir bei der Frage "Name der Cassettendatei:" einfach die `ENTER`-Taste gedrückt, so wäre die nächste Datei, die gefunden worden wäre, übertragen worden.

Existiert die übertragene Datei bereits auf der Diskette, so wird gefragt, ob sie gelöscht werden soll oder nicht.

---

## Der CP/M Befehl VDOS

**Zurückschalten auf VDOS/BASIC**

Mit diesem CP/M Befehl wird das CP/M Betriebssystem ordnungsgemäß verlassen.

Es gibt auch die Möglichkeit des Resets: durch gleichzeitiges Drücken der `CTRL`+`SHIFT`+`ESC`-Tasten wird Ihr CPC zurückgesetzt.

```
A>VDOS<ENTER>
```

Hierauf wird der Bildschirm gelöscht und es erscheinen die Einschaltmeldungen des CPC's.

---

## Der CP/M Befehl FAST

**Bildschirmverschleierung**

Wenn Sie schon auf anderen Rechnern mit CP/M gearbeitet haben, dann werden Sie vielleicht festgestellt haben, daß die CP/M Bildschirmausgabe auf Ihrem CPC nicht die allerschnellste ist. Die manchmal beinahe schon "quälend" langsame Ausgabe hat Sie sicherlich auch schon geärgert.

Die geringe Ausgabegeschwindigkeit liegt nicht etwa an einer schlechten Programmierung des Video-Controllers, sondern an der Tatsache, daß der Bildspeicher des CPC punktorientiert ist. Für die vielfältigen Grafikmöglichkeiten, die der CPC hat, ist das unerläßlich. Außerdem können 3 verschiedene Modi (20, 40 und 80 Zeichen) eingestellt werden. Die damit verbundenen ständig "durchlaufenen" Programmteile machen die Bildschirmausgabe langsam.

Beachtet man aber, daß unter CP/M eigentlich nur die 80-Zeichen-Darstellung gebraucht wird und daß man auf den ganzen "Grafikzauber" verzichten kann, dann könnte die Bildschirmausgabe wesentlich schneller sein. Das kleine Programm `FAST`, übrigens auch ein transienter Befehl, sorgt unter der Ausnutzung dieser Fakten für eine gewisse Verschleierung (ca. Faktor 2).

Bitte beachten Sie, daß von `FAST`, trotz dieser Einschränkungen, die komplette "Windowtechnik" unterstützt wird.

`FAST` wirkt wie ein Schalter.

```
A>FAST<ENTER>
```

`FAST` ist eingeschaltet.

```
A>FAST<ENTER>
```

`FAST` ist wieder ausgeschaltet.

> **(!) Hinweis:** Bitte beachten Sie, daß ein Reset auch die "FAST-Routine" ausschaltet.

---

## CP/M Fehlermeldungen und ihre eventuelle Beseitigung

Die deutschen Meldungen werden alle vom BIOS aus erzeugt. Es kann deshalb vorkommen, daß einer deutschen Fehlermeldung noch eine englische folgen kann. Bitte beachten, daß die Ausgabe der deutschen Meldungen mit Hilfe des Befehls `INSTALL` (siehe weiter vorne) unterbunden werden kann.

### `Laufwerk d: Schreibfehler – Wiederholen J/N ?`

Die Schreiboperation, die die Diskette in dem durch `d:` definierten Laufwerk betrifft, ist durch einen Fehler unterbrochen worden. Antwortet man mit "J", so wird es noch einmal versucht. Gibt man "N" ein, so wird die Operation abgebrochen.

### `Laufwerk d: Lesefehler – Wiederholen J/N ?`

Beim Lesen der Daten von der Diskette in Laufwerk `d:` ist ein Fehler aufgetaucht. Antwortet man mit "J", so wird es noch einmal versucht. Gibt man "N" ein, so wird die Operation abgebrochen.

### `Laufwerk d: Diskette fehlt – Wiederholen J/N ?`

Das Laufwerk, das angesprochen wurde, enthält keine Diskette, oder ist nicht richtig verriegelt. Legen Sie eine Diskette ein, oder drücken Sie den Druckknopf richtig ein und geben Sie "J" ein.

### `Laufwerk d: Diskette hat Schreibschutz – Wiederholen J/N ?`

Sie wollten Daten auf eine Diskette schreiben, die mit einem Schreibschutzkleber versehen ist. Nehmen Sie die Diskette heraus, entfernen Sie den Kleber und legen Sie die Diskette wieder ein. Geben Sie "J" ein und die Operation wird wiederholt. Möchten Sie nicht, daß auf diese Diskette geschrieben wird, dann geben Sie einfach "N" ein und brechen damit die Operation ab.

### `keine CP/M Diskette – Wiederholen J/N`

Sie wollten von dieser Diskette mit `|CPM<ENTER>` CP/M starten. Diese Diskette ist aber keine Systemdiskette. Entweder fehlt ihr der Bootsektor (Spur 0 Sektor 1), oder sie besitzt kein CP/M. Sie können es eventuell noch mit einer anderen Diskette versuchen, indem Sie sie tauschen und "J" eingeben.

### `Laufwerk d: Formatierfehler – Wiederholen J/N`

Beim Formatieren dieser Diskette ist ein Fehler aufgetaucht. Vielleicht ist die Diskette schadhaft, oder Sie probieren es einfach noch einmal.

### `Drucker nicht bereit - Wiederholen J/N`

Sie wollen mit `CTRL`+`P` etwas auf den Drucker ausgeben oder haben ein Programm, das auf den Drucker zugreifen will. Vielleicht ist der Drucker noch ausgeschaltet, oder nicht selektiert. Haben Sie überhaupt einen Drucker angeschlossen? Können Sie einen dieser Punkte feststellen, dann beheben Sie den Fehler und geben Sie dann "J" ein.

### `Operation wird wiederholt`

Geben Sie bei der Frage "- Wiederholen J/N ?" ein "J" ein, dann quittiert das System mit "Operation wird wiederholt".

### `Operation wird abgebrochen`

Geben Sie bei der Frage "- Wiederholen J/N ?" ein "N" ein, dann quittiert das System mit "Operation wird abgebrochen". Es kann hierbei oft passieren, daß nach abgebrochener Operation noch ein BDOS Error (immer diese lästigen BDOS Errors!!) ausgegeben wird. Versuchen Sie ihn mit `CTRL`+`C` zu umgehen.

### `erlaubte Laufwerkskennungen sind A oder B!`

`SYSGEN`. Haben Sie hier ein anderes Laufwerk als A oder B angegeben, so erhalten Sie obige Fehlermeldung.

### `SYSGEN wurde durch ^C abgebrochen`

`SYSGEN`. Sie haben bei irgendeiner Eingabe in `SYSGEN` ein `CTRL`+`C` eingegeben und damit das Programm frühzeitig abgebrochen.

### `Die Directory ist voll!`

`CASCOPY`. Sie wollen durch den gerade durchgeführten Kopiervorgang (von Cassette nach Diskette) auf dieser Diskette mehr als 128 Einträge ins Inhaltsverzeichnis der Diskette schreiben. Löschen Sie unnütze Dateien, und starten Sie `CASCOPY` noch einmal.

### `Die Diskette ist voll!`

`CASCOPY`. Mit diesem Kopiervorgang (Cassette nach Diskette) wird die Diskette voll. Löschen Sie unnütze Dateien, oder legen Sie eine neue Diskette ein.

### `Fehler! Cassettenstream war nicht offen.`

`CASCOPY`. Bei der Übertragung der Daten ist ein Fehler aufgetreten.

### `Geschützte Datei! Kann nicht gelesen werden.`

`CASCOPY`. Kopiergeschützte Cassettendateien können mit `CASCOPY` nicht auf Diskette übertragen werden.

### `File konnte auf Diskette nicht gefunden werden.`

`CASCOPY`. Die Datei, die von Diskette auf Cassette übertragen werden sollte, kann auf der Diskette nicht gefunden werden. Vielleicht haben Sie sich verschrieben, oder Sie haben die falsche Diskette eingelegt.

### `Fehler! CASCOPY wird abgebrochen`

`CASCOPY`. Bei der Übertragung ist ein fataler Fehler aufgetreten.

### `Ungültiger Dateiname:`

`CASCOPY`. Die Dateibezeichnung der Datei, die übertragen werden soll, ist ungültig. Vielleicht ist sie zu lang, oder sie enthält unzulässige Zeichen.

### `<DATEI> ist bereits vorhanden. Löschen J/N ?`

`CASCOPY`. Die Dateibezeichnung der Datei, die auf Cassette oder Diskette kopiert werden soll, ist dort bereits vorhanden. Sie kann gelöscht werden ("J") oder belassen werden ("N").

### `Parametersector konnte nicht geladen werden`

Beim Laden von CP/M ist der Parametersektor als schadhaft entdeckt worden. Überprüfen Sie diesen Sektor und installieren Sie, wenn nötig, einen neuen.

### `Falscher Parametersector`

Der Inhalt des Parametersektors ist für CP/M "unverständlich".

### `Expansion Buffer voll oder unerlaubtes Token`

In der Tastaturumbelegungstabelle sind Fehler. Sie haben vielleicht ein unerlaubtes Token verwendet.

### `Druckerstring konnte nicht abgeschickt werden.!`

Der Drucker ist wahrscheinlich nicht eingeschaltet, nicht angeschlossen, oder nicht selektiert. Beheben Sie die Ursache und laden Sie CP/M neu.

### `Loader: 3" Laufwerk=Laufwerk B.`

Diese zusätzliche Lademeldung zeigt an, daß das 3"-Laufwerk unter CP/M permanent Laufwerk B ist. Diese Einstellung kann mit `INSTALL` fest eingestellt werden.

### `Parametersektor overflow! Installation nicht möglich! Abbrechen J/N?`

`INSTALL`. Sie wollen in den Parametersektor mehr als 512 Byte Daten packen. Das ist zu viel!

### `INSTALL wird abgebrochen, da Parametersector nicht lesbar!`

`INSTALL`. Beim Starten von `INSTALL` wird der Parametersektor gelesen. Irgendetwas stimmt aber an diesem Sektor nicht, er kann nicht oder nicht richtig gelesen werden.

### `Achtung! Parametersector konnte nicht korrekt geschrieben werden`

`INSTALL`. Beim Verlassen von `INSTALL` wird der neue Parametersektor auf die Diskette geschrieben. Diesmal hat es leider nicht geklappt. Beim Schreiben ist ein Fehler aufgetaucht.

### `Diskette nicht eingelegt - Wiederholen J/N ?`

`DISKTOOL`. Sie haben vergessen, eine Zieldiskette einzulegen oder den Laufwerksknopf richtig zu verriegeln. Beheben Sie den Fehler und geben Sie "J" ein.

### `Diskette hat Schreibschutz - Wiederholen J/N ?`

`DISKTOOL`. Die eingelegte Zieldiskette hat eine Schreibschutzmarke. Entfernen Sie diese, wenn zulässig, und geben Sie ein "J" ein.

### `Kein Diskettenlaufwerk!`

`DISKTOOL`. Sie wollten die RAM-Floppy oder die Festplatte mit einer DISKTOOL-Funktion bearbeiten. Das geht nicht! Mit `DISKTOOL` können nur Diskettenlaufwerke bedient werden.

### `Disketten haben unterschiedliche Formate!`

`DISKTOOL`. Sie haben versucht, eine komplette vortex Diskette auf eine 3"-Diskette zu kopieren, oder die Systemspuren einer vortex Diskette auf eine 3"-Diskette zu übertragen. Diese Funktionen arbeiten nur, wenn wir Laufwerke gleichen Formats haben.

### `Laufwerk nicht verfügbar!`

`DISKTOOL`. Sie haben versucht, ein Laufwerk zu selektieren, das nicht vorhanden ist (z.B. Laufwerk D).

### `Diskette hat keine reservierten Systemspuren`

`DISKTOOL`. Nehmen wir an, Sie möchten die Systemspuren einer 3"-Diskette auf eine andere 3"-Diskette übertragen. Hat diese Diskette das Data-Only Format, erhalten wir diese Meldung.

### `DISKTOOL 1.0 benoetigt unter dem RAM-Karten CP/M aktive System-Vektoren !`

`DISKTOOL`. Wollen Sie mit `DISKTOOL` auch unter dem 62K CP/M der vortex RAM-Karten arbeiten, dann müssen Sie beim "Patchen" die System-Vektoren einschalten.

### `Laufwerk d: Diskette hat Schreibschutz - Wiederholen J/N ?`

`FILECOPY`. Die Zieldiskette hat eine Schreibschutzmarke. Wenn Sie sie entfernt haben – falls zulässig –, dann können Sie mit "J" den Kopiervorgang starten.

### `<datei> existiert bereits ! Ueberschreiben J/N ?`

`FILECOPY`. Die Datei, die unter dieser Dateibezeichnung gerade auf die Zieldiskette kopiert werden soll, existiert bereits auf der Zieldiskette. Wenn Sie sie einfach überschreiben wollen, dann geben Sie "J" ein. Im anderen Fall antworten Sie hier mit "N".

### `FILECOPY 3.0 benoetigt unter dem RAM-Karten CP/M aktive System-Vektoren !`

`FILECOPY`. Wollen Sie mit `FILECOPY` auch unter dem 62K CP/M der vortex RAM-Karten arbeiten, dann müssen Sie beim "Patchen" die System-Vektoren einschalten.

---

## VDOS und CP/M intern

Der VDOS 2.0 ROM läßt sich stark vereinfachend in folgende Teile untergliedern:

```
FFFF
+---------------------+
| Graphikbefehle      |
| Fast-Routine        |
| Monitor             |
+---------------------+  ca. E900
| D O S               |  Disk Operating System
+---------------------+  ca. D000
| B I O S             |  Basic Input Output System
+---------------------+  C000
```

Alle drei Bereiche stellen mehr oder weniger unabhängige Einheiten dar. Vor allem der Monitor und die Graphikbefehle lassen sich klar abgrenzen, wohingegen zwischen DOS und BIOS enge Beziehungen bestehen.

### BIOS – Basic Input Output System

Zunächst, lassen Sie sich nicht verwirren – Basic hat nichts mit der Programmiersprache BASIC zu tun, sondern bedeutet hier "grundlegend" oder "eigentlich". Das BIOS stellt die eigentliche Verbindung zwischen dem Floppy Controller (Hardware) und Ihrem CPC (Software) dar. Es zerfällt selbst wieder in zwei logische Blöcke:

1. Module zur Laufwerksansteuerung
2. Module zur Drucker-, Tastatur-, Bildschirm-, kurz zur Peripherieansteuerung

Die Unterprogramme (Module) aus Punkt 2 haben mit den Laufwerken eigentlich nichts zu tun, werden allerdings für die Installation eines CP/M Betriebssystems benötigt (siehe auch Anhang: CP/M unter der Lupe).

Block 1 – die Laufwerksansteuerung – läßt sich seinerseits wieder in drei hierarchisch aufeinanderfolgende Ebenen gliedern:

- 1.0 Floppy Disk Treiberroutinen
- 1.1 Grundfunktionen
- 1.2 Recordverwaltung (Blocking/Deblockingroutine)

Die Floppy Disk Treiberroutinen sprechen direkt über entsprechende PORTS den Floppy Disk Controller an. Möchte man ihre Funktionsweise und Strukturierung verstehen, so muß man sich eingehend mit der Hardware des eigentlichen Controllers und der Laufwerke befassen. Dies würde hier jedoch zu weit führen und wir verweisen deshalb auf entsprechende Spezialliteratur und Datenblätter.

Die Grundfunktionen sind Unterprogramme, die ihrerseits die Floppy Disk Treiberroutinen benutzen und bereits vom Anwender oder versierten Maschinensprach-Programmierer angesprungen werden können. Folgende Grundfunktionen sind im BIOS des VDOS ROMs realisiert:

- 1.10 Lese einen physikalischen Sektor
- 1.11 Schreibe einen physikalischen Sektor
- 1.12 Formatiere eine ganze Spur
- 1.13 Positioniere den Kopfschlitten
- 1.14 Prüfe den Laufwerksstatus
- 1.15 Schalte den Laufwerksmotor aus

Eingabegrößen werden gemäß folgender Konvention übergeben (die Buchstaben bezeichnen die internen Z80 Register):

| Register | Bedeutung |
|----------|-----------|
| C  | Sektornummer |
| D  | Spurnummer |
| E  | Laufwerksnummer |
| HL | Pufferadresse |

Über den Erfolg oder Mißerfolg einer Laufwerksoperation klärt das Carry Flag auf:

- **Carry gesetzt** bedeutet, daß die Operation erfolgreich war
- **Carry=0** sagt uns, daß etwas "schief" gelaufen ist

Der kleinste Datenblock, den sowohl CP/M als auch das DOS verwalten können, ist nun nicht etwa ein physikalischer Sektor (512 Bytes), sondern ein sogenannter **Record** (128 Bytes). Jeder physikalische Sektor kann vier solche Records aufnehmen. Der Record ist eigentlich eine "historische Größe" und stammt noch aus den Floppy-Pionierzeiten. Damals war die physikalische Sektorgröße ebenfalls 128 Bytes, eben ein Record. Mit dem zunehmenden Aufkommen von integrierten Controller-Chips war man bald in der Lage, auch größere Sektoren (256, 512,… Bytes) zu lesen/schreiben und konnte dadurch die Zugriffszeiten drastisch verringern. Zu diesem Zeitpunkt hatten sich jedoch bestimmte Betriebssysteme – vornehmlich CP/M – bereits etabliert und der Record war das geläufige Datenformat. Das BIOS wurde deshalb um sogenannte Blocking/Deblocking-Routinen erweitert. Dies sind Unterprogramme, die den physikalischen Sektor kontrolliert in Records zerlegen oder aus Records zusammensetzen und entsprechend den Zugriff steuern. Denn bei einer physikalischen Sektorgröße von 512 Bytes müssen wir im günstigsten Fall nur alle vier Records tatsächlich auf die Diskette zugreifen.

In den Themenkomplex der Recordverwaltung gehören folgende BIOS Routinen:

- 1.20 Setze Spurnummer
- 1.21 Setze Recordnummer
- 1.22 Setze Recordpuffer-(DMA-)Adresse
- 1.23 Lese Record in Recordpuffer
- 1.24 Schreibe Record aus Recordpuffer
- 1.25 Übersetze Spurnummer falls nötig

Jeder dieser Routinen entspricht ein Einsprung im sogenannten CP/M BIOS Vektor (siehe Anhang: CP/M unter der Lupe).

Das BIOS beherbergt noch einige zusätzliche Funktionen, die hier nur kurz aufgezählt werden sollen:

- `SELDSK` wählt ein bestimmtes Laufwerk an
- `BOOT` führt einen CP/M Kaltstart durch
- `WBOOT` führt einen CP/M Warmstart durch

### DOS – Disk Operating System

Das DOS ist das eigentliche Herz des VDOS ROMs. Wie wir gesehen haben, ist das BIOS nur dazu in der Lage, Diskettendaten record- oder sektorweise zu verwalten. Von Dateien (Files) war nirgendwo die Rede. Aus diesem Grunde sind auch gewisse Grundkenntnisse erforderlich, um "zerstörungsfrei" mit dem BIOS zu arbeiten, wohingegen Direktzugriffe aufs DOS meist mit einem "blauen Auge" abgehen.

VDOS ist genau wie auch CP/M ein dateiorientiertes Diskettenbetriebssystem. Ähnlich den Karteikarten in einem Karteikasten werden die Daten nicht als einzelne Bytes (Buchstaben), sondern als logische Übereinheiten (Dateien) verwaltet. Wie findet nun das DOS eine bestimmte Datei auf der Diskette wieder? Schütten wir alle Karteikarten in eine große Schachtel und rühren gut durch, so haben wir kaum eine Chance, eine bestimmte Karte schnell zu finden. Was machen wir also? Wir ordnen die Karten in einem Karteikasten und legen ein Inhaltsverzeichnis an. Genauso macht es auch das DOS: Jede Datei erhält zur eindeutigen(!) Kennzeichnung einen Namen. Diese Namen werden zusammen mit der Stelle auf der Diskette, an der die Datei zu finden ist, im sogenannten Directory – dem Inhaltsverzeichnis der Diskette – gespeichert. Diese Darstellung ist zwar stark vereinfacht, trifft den Sachverhalt aber genau auf den Kopf.

Bevor wir nun näher auf das DOS eingehen, noch ein paar grundlegende Worte zu Datenstrukturen – unerläßlich für ein tiefergehendes Verständnis:

Wie Sie vielleicht bereits wissen oder aber sehr bald selbst feststellen werden, können Sie dieselben Disketten, die Sie unter BASIC einsetzen, auch für CP/M verwenden. Dies ist keine Selbstverständlichkeit, sondern hat seinen Grund darin, daß VDOS Dateien in derselben Art und Weise verwaltet wie CP/M. Das nimmt Ihnen die Sorgfalt ab, sauber zwischen "CP/M-Disketten" und "BASIC-Disketten" zu trennen – es kann eigentlich nichts schief gehen. Die folgenden Erklärungen gelten also für VDOS und CP/M gleichermaßen:

**Record:** Datenblock mit 128 Bytes. Kleinste Datenmenge im Datenaustausch mit der Floppy.

**Block:** Das DOS muß ja gewissermaßen Buch führen über die Daten, die auf einer Diskette stehen. Dies geht so: Man zerlege die Diskette in ihre Spuren, schneide die Spuren auf und hänge eine Spur an die andere. Auf diese Weise entsteht ein langes Band, in dem Byte auf Byte folgt – wir erhalten so eine lineare Abbildung der Diskette. Eine Möglichkeit der Datenverwaltung wäre nun, jedem Byte gemäß seiner Position im Band eine Nummer zu geben. Der Verwaltungsaufwand wäre immens. Bei einer Kapazität von 708 KB müßte sich das DOS 724992 Nummern merken – dies ist in der Praxis nicht durchführbar. Man unterteilt deshalb das Band (die Diskette) in größere Untereinheiten: die Blöcke, und gibt diesen Blöcken Nummern. Die Blockgröße auf den vortex Floppies ist 4 KB (= 4096 Bytes). Wie man leicht einsieht, braucht man in diesem Fall – der Blockunterteilung – wesentlich weniger Nummern, nämlich nur knapp 200. Egal wie klein eine Datei ist, sie belegt immer mindestens einen Block auf der Diskette. Einen kleinen Schönheitsfehler hat die Sache leider: man verschenkt zwangsläufig immer Speicherplatz. Stellen Sie sich vor, Sie haben 20 Dateien auf der Diskette, wovon jede nur 1 KB Daten enthält. Jede Datei belegt aber einen Block und so verlieren wir 20·3 KB = 60 KB, obwohl wir eigentlich nur 20·1 KB = 20 KB bräuchten. Damit muß man leben. Ein Ausweg wäre, die Blockgröße kleiner zu machen, dies hätte jedoch wiederum zur Folge, daß wir mehr Nummern zur Durchnummerierung der Blöcke brauchen. Man muß also Kompromisse schließen.

Um die Bedeutung des Blocks als Datenstruktur im DOS noch besser verstehen zu können, wollen wir etwas näher auf die Directory und ihren Aufbau eingehen:

Die Directory – das Inhaltsverzeichnis der Diskette – zerfällt in sogenannte **Entries**. Jeder Entry ist genau 32 Bytes lang und hat folgenden Aufbau:

| Byte | Bedeutung |
|------|-----------|
| 0 | User Nummer |
| 1-8 | Dateiname |
| 9-11 | Extension |
| 12 | Extentnummer |
| 13,14 | DOS Arbeitsvariablen |
| 15 | Record Count (Anzahl der Records im augenblicklichen Extent) |
| 16-31 | Blockbelegungstabelle |

Unser Augenmerk gilt hier Byte 16-31 – der Blockbelegungstabelle. Hier stehen der Reihe nach die Nummern der Blöcke, die die Datei belegt. Stellen wir uns einmal vor, wir möchten eine bestimmte Datei auf der Diskette finden. So geht das DOS vor: Es sucht die Directory nach einem Eintrag ab, der den Namen der gesuchten Datei enthält. Findet es einen solchen Eintrag, so kann es der Blockbelegungstabelle sofort entnehmen, wo die Datei liegt. So weit so schön. Wie wir leicht nachrechnen können, haben in der Blockbelegungstabelle eines Directoryeintrags maximal 16 Blocknummern Platz. Bei einer Blockgröße von 4 KB können wir also maximal eine Datei der Länge 64 KB auf der Diskette eindeutig platzieren. Was nun aber, wenn die Datei 65 KB oder größer ist? Hier kommt nun die letzte Datenstruktur in unserem kleinen Exkurs ins Spiel: der **Extent**.

**Extent:** Der Extent kennzeichnet einen Datenblock der Größe 16 KB. Wieso gerade 16 KB? Nun, dies resultiert wiederum aus der "Geschichte": Bei Diskettenstationen mit kleiner Kapazität ist es sinnvoll, kleine Blöcke zu wählen, dies deshalb, um möglichst wenig Platz zu verschwenden. Die kleinste mögliche Blockgröße ist 1 KB (alle CPC's mit 3"-Laufwerk "fahren" 1 KB Blöcke). Bei dieser Blockgröße können wir in einem Directoryeintrag genau 16 Blocknummern unterbringen, d.h. ein Eintrag kann in diesem Fall genau 16 KB Daten platzieren. Ist eine Datei größer, so legt das DOS einfach weitere Einträge (Extents = Erweiterungen) mit demselben Dateinamen an und merkt sich in Byte 12 die Nummer des augenblicklichen Extents. Verwaltet das DOS Dateien über größere Blöcke, so ändert sich an diesem Mechanismus praktisch nichts, nur gehen dann mehrere Extents in einen Directoryeintrag (4 KB Blöcke -> 4 Extents).

Wir wissen nun also, was ein Record, was ein Block, was ein Extent ist, und haben gelernt, daß Dateien blockweise auf der Diskette abgelegt werden. Jetzt noch einige Worte zu einem weiteren sehr wichtigen Eintrag in einem Directoryentry: dem **Record Count** (s.o. Byte 15). Dieser hat die Aufgabe, das genaue Ende einer Datei und somit ihre genaue Größe (in Records) festzulegen. Ein Beispiel: Blockgröße 4 KB, Datei der Länge 8 Records (= 1 KB). Diese Datei belegt genau einen Block, genaugenommen aber nur dessen erstes Viertel. Woher weiß das DOS nun also, wo die Datei innerhalb des Blocks endet? Genau hierzu dient der Record Count, er zählt die Records innerhalb eines Extents (läuft also von 0..127, da genau 128 Records in einen Extent gehen) und erlaubt es dadurch, das absolute Ende einer Datei unabhängig von der Blockgröße zu bestimmen. Außerdem kann das DOS über den Record Count feststellen, ob noch ein weiterer Extent folgt oder nicht (es folgt immer dann ein weiterer Extent, wenn der Record Count 127 ist).

Nun also zum eigentlichen Klassenziel dieses Abschnitts: der Funktionsweise des DOS.

Das DOS – mehr oder weniger eine Programmbibliothek – zerfällt grob gesagt in zwei Gruppen von Modulen:

- 2.0 Routinen zur fileorientierten Directory- und Datenmanipulation
- 2.1 Anpassungsmodule

Beide Gruppen sind zum Teil wieder hierarchisch verknüpft. Die Routinen der zweiten Gruppe – wir haben sie Anpassungsmodul genannt, der Grund wird bald ersichtlich sein – referenzieren Routinen aus der ersten Gruppe und diese wiederum greifen auf die Diskette über das BIOS zu.

Zunächst zur ersten Gruppe und ihrer Untergliederung:

- 2.01 Öffne Datei
- 2.02 Schließe Datei
- 2.03 Schreibe Record sequentiell in Datei
- 2.04 Lese Record sequentiell aus Datei
- 2.05 Schreibe Record random in Datei
- 2.06 Lese Record random aus Datei
- 2.07 Lösche Datei
- 2.08 Gebe Datei einen neuen Namen
- 2.09 Gebe Inhaltsverzeichnis auf Bildschirm aus
- 2.010 Manipuliere Dateiattribute

Wir sehen, Gruppe 1 der DOS Funktionen stellt Grundoperationen zur Datei-/Directorymanipulation zur Verfügung. VDOS unterstützt im Gegensatz zum AMSDOS zwei Zugriffarten auf die Diskette: den sequentiellen und den random Zugriff. Beim sequentiellen Zugriff kann eine Datei immer nur der Reihe nach gelesen/geschrieben werden. Der random- oder auch relative Zugriff erlaubt es, beliebige Records der Datei in beliebiger Reihenfolge zu lesen und auch zu beschreiben.

Gruppe 1 sitzt immer noch im Kern des DOS, d.h. es sind keine standardisierten Einsprünge in diese Routinen vorgesehen. Möchten Sie diese Routinen dennoch benutzen, so können Sie sie nur erreichen, indem Sie direkt ins ROM einspringen. Beachten Sie dabei jedoch unbedingt, daß sich nichtstandardisierte Einsprünge von ROM-Revision zu ROM-Revision ändern können. Man sollte also derartige Einsprünge, vor allem dann, wenn man kommerzielle Software erstellt, tunlichst vermeiden.

Gruppe 2 – die Anpassungsmodule – besitzen im Gegensatz zu Gruppe 1 alle standardisierte Einsprünge und sind deshalb revisionsunabhängig immer über dieselben Einsprünge zu erreichen. Nun zum Begriff "Anpassungsmodul": dazu müssen wir etwas weiter ausholen.

Das CPC BASIC (1.0 und 1.1) unterstützt über eine eigene sogenannte Streamnummer (siehe BASIC Handbuch) einen externen Massenspeicher. Beim 464 ist dies der eingebaute Datenrecorder, beim 664/6128 das eingebaute 3"-Laufwerk. BASIC spricht diesen Massenspeicher nun nicht etwa direkt an, sondern benutzt dazu den sogenannten "Main Jump Vector". Dies ist eine Leiste sogenannter standardisierter Modulaufrufe, die im Speicher ab der Adresse `BB00H` liegt, sie ist versionsunabhängig und deshalb bei allen CPC's gleich. Mit "gleich" ist hier keinesfalls gemeint, daß die entsprechenden Sprungleisten Byte für Byte übereinstimmen müssen, vielmehr soll damit gesagt werden, daß jeder Einsprung definierte Einsprung- und Aussprungparameter hat und eine bestimmte Funktion erfüllt – man nennt dies auch ein "Black Box Verhalten".

Ein Beispiel: Nehmen wir einmal an, Sie möchten den Buchstaben A auf den Bildschirm ausgeben. Ein Blick ins CPC Firmware Handbuch sagt uns, daß hierzu die Funktion 30 namens `TXT OUTPUT` zuständig ist. Ihr Einsprung liegt bei `BB5AH`. Beim Einsprung muß im Akkumulator (= Z80 Register) das auszugebende Zeichen (hier ein A, ASCII Code `41H`) stehen. Eine Aussprungbedingung gibt es nicht. Es ist also absolut nebensächlich, welche Routine sich im einzelnen hinter dem Einsprung `BB5AH` verbirgt, wichtig ist nur, was sie bewirkt, mit welchen Daten sie gefüttert werden muß und was sie als Antwort (= Status, Aussprungbedingung) liefert. Man nennt dies auch eine (Software-)Schnittstelle (nicht zu verwechseln mit Hardware-Schnittstellen, z.B. Centronics, RS232C, …).

Noch ein Beispiel aus dem alltäglichen Leben: der Briefkasten. Ein Briefkasten ist gewissermaßen auch eine Schnittstelle mit wohldefinierten Ein- und Ausgangsbedingungen. Seine Aufgabe ist es, Briefe vom Ort x zum Ort y zu befördern. Was mit einem Brief jetzt im Einzelnen passiert, nachdem Sie ihn durch den Einwurfsschlitz geworfen haben, ist eigentlich Nebensache (es sei denn, er geht verloren).

Also, um den Begriffen eine konkrete Bedeutung zu geben: der Brief ist die Eingangsgröße (vgl. Zeichen im Akku bei `TXT OUTPUT`), die Beförderung von x nach y ist die Aufgabe, die Schnittstellenfunktion (vgl. Zeichen auf Bildschirm ausgeben). Eine Aussprungbedingung gibt es, solange alles gut geht, nicht. Wird der Brief auf dem Postweg beschädigt, so teilt Ihnen dies das Postamt mit, und dies wäre dann eine entsprechende Aussprungbedingung, sozusagen die Statusmeldung.

Nach diesem kleinen Exkurs ins Post(un)wesen nun zurück zu unserem Massenspeicher am CPC: BASIC kommuniziert mit diesem Massenspeicher über 13 Einsprünge im "Main Jump Vector", die Funktionen 125 bis 137 (siehe CPC Firmware Handbuch). Der Vollständigkeit halber wollen wir diese Funktionen hier aufzählen. Wichtig: Die Funktionsnamen folgen der Nomenklatur des Firmwarehandbuchs und beginnen deshalb immer mit `CAS...`. Dies soll allerdings nicht bedeuten, daß damit nur der Datenrecorder anzusprechen wäre, vielmehr kann ein beliebiger Massenspeicher angesprochen werden. Hierzu müssen wir nur die Einsprünge durch andere ersetzen (Vektor verbiegen), die zu Routinen führen mit denselben Ein-/Aussprungbedingungen und denselben Aufgaben, also z.B. ein Floppy Laufwerk.

Bevor wir in medias res steigen, noch ein lästiges, aber umso wichtigeres Detail, das die Verwirrung sicherlich komplett machen wird. Es wird bei der Funktionsbeschreibung öfters von einem sogenannten **Block** die Rede sein. Die damit gemeinten Blöcke haben nun aber (leider) überhaupt nichts mit den weiter oben beschriebenen Blöcken der Diskettenorganisation zu tun, vielmehr sind hiermit Datenportionen der Größe 2 KB gemeint, die eben BASIC in dieser Form benötigt.

#### Funktion 125: `CAS IN OPEN` – Einsprung `BC77H`

**Aufgabe:** Öffne eine Datei auf dem Lesekanal und lese ihren ersten Block.

**Einsprung:**
- `HL` = Zeiger auf Filename
- `B` = Länge des Filenamens
- `DE` = Zeiger auf 2 KB Blockpuffer

**Aussprung:**
- Datei konnte korrekt geöffnet werden: `Carry=1 Z=0`, `HL` = Zeiger auf File Header, `DE` = Daten-Zieladresse, `BC` = Filelänge, `A` = Filetyp
- Lesekanal war bereits in Benutzung: `Carry=0 Z=0`

#### Funktion 126: `CAS IN CLOSE` – Einsprung `BC7AH`

**Aufgabe:** Schließe Datei auf Lesekanal ordnungsgemäß.

**Einsprung:** keine

**Aussprung:**
- Datei konnte geschlossen werden: `Carry=1`
- Es war keine Datei in Benutzung: `Carry=0`

#### Funktion 127: `CAS IN ABANDON` – Einsprung `BC7DH`

**Aufgabe:** Schließe Lesekanal sofort.

**Einsprung:** keine. 

**Aussprung:** keine.

#### Funktion 128: `CAS IN CHAR` – Einsprung `BC80H`

**Aufgabe:** Hole das nächste Zeichen vom Lesekanal aus der Datei, die dort augenblicklich geöffnet ist.

**Einsprung:** keine

**Aussprung:**
- Zeichen konnte ordnungsgemäß abgeholt werden: `Carry=1 Z=0`, Zeichen im Akkumulator
- End of File wurde detektiert: `Carry=0 Z=0`

#### Funktion 129: `CAS IN DIRECT` – Einsprung `BC83H`

**Aufgabe:** Lese die auf dem Lesekanal augenblicklich geöffnete Datei auf einen Satz in den Speicher. Funktion 129 und 128 schließen sich gegenseitig aus. Man kann also z.B. nicht erst mal die ersten 5 Zeichen einzeln auslesen und dann den Rest am Stück abholen.

**Einsprung:** `HL` = Zieladresse, wo die Daten hingelesen werden sollen

**Aussprung:**
- Datei konnte ordnungsgemäß eingelesen werden: `Carry=1 Z=0`, `HL` = Einsprung in Datenbereich (nur sinnvoll, falls es sich um ein Maschinenprogramm handelt)
- Datei war gar nicht geöffnet: `Carry=0 Z=0`

#### Funktion 130: `CAS RETURN` – Einsprung `BC86H`

**Aufgabe:** Schicke das zuletzt mit `CAS IN CHAR` gelesene Zeichen wieder zurück in den Lesekanal.

**Einsprung:** keine. 

**Aussprung:** keine.

#### Funktion 131: `CAS TEST EOF` – Einsprung `BC89H`

**Aufgabe:** Teste, ob Dateiende erreicht.

**Einsprung:** keine

**Aussprung:**
- End of File noch nicht erreicht: `Carry=1 Z=0`
- End of File erreicht: `Carry=0 Z=0`

#### Funktion 132: `CAS OUT OPEN` – Einsprung `BC8CH`

**Aufgabe:** Öffne eine Datei auf dem Schreibkanal.

**Einsprung:**
- `HL` = Zeiger auf Dateiname
- `B` = Länge des Dateinamens
- `DE` = Zeiger auf 2 KB Blockpuffer

**Aussprung:**
- Datei konnte ordnungsgemäß geöffnet werden: `Carry=1 Z=0`, `HL` = Zeiger auf File Header
- Schreibkanal ist bereits in Benutzung: `Carry=0 Z=0`

#### Funktion 133: `CAS OUT CLOSE` – Einsprung `BC8FH`

**Aufgabe:** Schließe Schreibkanal ordnungsgemäß.

**Einsprung:** keine

**Aussprung:**
- Datei konnte ordnungsgemäß geschlossen werden: `Carry=1 Z=0`
- Es war gar keine Datei in Benutzung: `Carry=0 Z=0`

#### Funktion 134: `CAS OUT ABANDON` – Einsprung `BC92H`

**Aufgabe:** Schließe Schreibkanal sofort.

**Einsprung:** keine. 

**Aussprung:** keine.

#### Funktion 135: `CAS OUT CHAR` – Einsprung `BC95H`

**Aufgabe:** Sende ein Zeichen in den Schreibkanal.

**Einsprung:** Akkumulator enthält Zeichen

**Aussprung:**
- Zeichen konnte abgeliefert werden: `Carry=1 Z=0`
- Schreibdatei war gar nicht geöffnet: `Carry=0 Z=0`

#### Funktion 136: `CAS OUT DIRECT` – Einsprung `BC98H`

**Aufgabe:** Sende einen zusammenhängenden Speicherbereich in den Schreibkanal. Funktion 134 und 135 schließen sich wieder gegenseitig aus.

**Einsprung:**
- `HL` = Zeiger auf Speicherbereich
- `DE` = Länge des Speicherbereichs
- `BC` = Einsprungadresse (nur bei Maschinenprogrammen sinnvoll)
- `A` = Filetyp

**Aussprung:**
- Es konnte ordnungsgemäß geschrieben werden: `Carry=1 Z=0`
- Es war keine Datei zum Schreiben offen: `Carry=1 Z=0`

#### Funktion 137: `CAS CATALOG` – Einsprung `BC9BH`

**Aufgabe:** Bringe das Inhaltsverzeichnis auf den Bildschirm. Diese Funktion benutzt den Lesekanal und kann deshalb nicht benutzt werden, wenn dieser gerade anderweitig belegt ist.

**Einsprung:** `DE` = Zeiger auf 2k Arbeitspuffer

**Aussprung:**
- Alles OK: `Carry=1 Z=0`
- Lesekanal war in Benutzung: `Carry=0 Z=0`

Befindet sich nun beim Einschalten des CPC's eine Floppy am System, so wird beim sogenannten ROM WALK (das Betriebssystem klappert hierbei alle sogenannten Background-ROMs ab und stellt dadurch fest, welche Peripherie zur Verfügung steht) der Teil des "Main Jump Vectors", der die Massenspeicherschnittstelle in Richtung Datenrecorder leitet, zur Floppy umgebogen. Hierzu werden einfach die Einsprünge in die Datenrecorder-Routinen durch entsprechende Einsprünge in die Floppy-Routinen (Anpassungsmodule) ersetzt.

---

### RAM Variablen von BIOS und DOS

Sowohl BIOS als auch DOS benötigen, obwohl die Routinen selbst im ROM liegen, auch RAM zur Verwaltung. Dieser RAM zerfällt in zwei Gruppen:

- 3.0 nicht relokatibler RAM
- 3.1 relokatibler RAM

Wie der Name bereits sagt, ist der nicht relokatible RAM-Bereich nicht verschiebbar, d.h. er wird vom DOS/BIOS absolut adressiert. Der relokatible RAM-Bereich hingegen wird nur indiziert adressiert und ist deshalb frei verschieblich. Die Ursache dafür, daß dieser RAM-Bereich verschiebbar sein muß, ist in der Firmware-Architektur der CPC's zu suchen: Jeder Peripherie- (Background-)ROM kann nämlich während des ROM WALK's RAM für sich reservieren. Dies allein ist noch nicht weltbewegend, vielmehr besitzt jeder Background-ROM auch noch eine sogenannte ROM-Nummer. Der ROM WALK erfolgt von Nummer 7 -> 0 beim 464 und 15 -> 0 bei 664/6128. Die ROM-Nummer ist eine Hardwaregeschichte und wird durch die Elektronik bestimmt, die um den ROM herumsitzt.

Die RAM-Reservierung erfolgt nun folgendermaßen (hier nur 464; 664/6128 entsprechend): Zuerst reserviert sich ROM Nummer 7 seinen Platz im RAM, anschließend kann sich direkt darunter ROM Nummer 6 Platz reservieren usw. D.h. aber, daß ein ROM vor dem eigentlichen ROM WALK noch gar nicht wissen kann, wo sein RAM-Bereich im Speicher liegen wird, da er ja keine Ahnung hat, wieviel Platz die ROMs "über" ihm reservieren. Deshalb referenziert der ROM alle seine Variablen im verschieblichen RAM-Bereich indiziert, indem er vom Kernel die Basis-Adresse seines RAM-Bereichs übergeben bekommt (im IY Register) und er dazu einen entsprechenden Offset hinzuzählt.

Schreibt man ein Programm, welches später in einen (Background-)ROM "geschossen" werden soll, unter strenger Beachtung der indizierten Adressierung von RAM-Variablen, so kann der ROM später in eine beliebige ROM-Fassung gesteckt werden und wird auf Anhieb korrekt arbeiten. Die ganze Sache hat nur einen Haken, der sich aber meist nicht störend auswirkt: die indizierte Adressierung ist aufwendiger als die absolute, und dies wiederum bewirkt, daß das Programm etwas "langsamer" (meist nicht meßbar) und auch länger wird (meist schon störender, da im ROM nur beschränkt Platz ist).

Da der gesamte Speicheraufbau (unter BASIC) der CPC's auf diese dynamische Platzreservierung hin ausgerichtet wurde, ist "absoluter" RAM nur in sehr beschränktem Maße verfügbar (der größte Teil des "absoluten" RAM's wird vom BASIC Interpreter und vom Betriebssystem belegt). Einer der wenigen zusammenhängenden, großen, "absoluten" RAM-Bereiche liegt bei `BE80H` (bis zum Stack) und wird auch von der Floppy Firmware benutzt.

> **(!) Wichtig:** Nachfolgend finden Sie die vom VDOS 2.0 ROM belegten RAM-Bereiche ihrer Bedeutung nach aufgelistet. Selbstverständlich sind wir bemüht, diese Bereiche auch bei Revisionen nicht zu ändern, manchmal läßt sich dies jedoch nicht vermeiden. Seien Sie also vorsichtig, bevor Sie nach Lust und Laune "herumpoken" ("Peeken" ist natürlich erlaubt).

#### Nicht relokatibler RAM-Bereich des VDOS 2.0 ROM's

(alle Adressen hexadezimal)

> **(!) Hinweis:** Ein `*` in der zweiten Spalte bedeutet, daß an derselben Stelle dieselbe Variable auch unter AMSDOS zu finden ist. Die Zahl in der dritten Spalte gibt die Länge der Variablen in Bytes an.

| Adresse | AMSDOS | Länge | Bedeutung |
|---------|--------|-------|-----------|
| BE40 | * | 2 | DPH Adresse Laufwerk A |
| BE42 | * | 2 | DPB Adresse Laufwerk B |
| BE44 | * | 2 | Motor on counter: Zeit in 50msec-Einheiten nach dem Einschalten des Motors bis zum ersten Zugriff. Muß eingehalten werden, um eine konstante Rotationsgeschwindigkeit der Diskette zu haben. Defaultwert: 50 |
| BE46 | * | 2 | Motor off counter: Zeit in 50msec-Einheiten vom letzten Zugriff bis zum Ausschalten des Motors. Würde man den Motor gleich nach dem Zugriff abschalten, so müßte man, falls nur wenig später ein erneuter Zugriff erfolgt, wieder die Motor-on-Phase abwarten, d.h. der Zugriff wird drastisch verlangsamt. Defaultwert: 250 |
| BE49 | * | 1 | Kopfberuhigungszeit in 1msec-Einheiten. Nachdem eine Spur vom Kopfschlitten angefahren wurde, befindet sich der Schlitten noch eine gewisse Zeit in mechanischer Schwingung. Die Beruhigung des Schlittens muß abgewartet werden, um Schreib-/Lesefehler zu vermeiden. Defaultwert: 30 |
| BE4A | * | 1 | Kombinierte Steprate für 5,25"/3,5" und 3"-Laufwerk. Die oberen 4 Bits sind die Steprate des 3"-Laufwerks in 1msec-Einheiten und die unteren 4 die des 5,25"/3,5"-Laufwerks in 1msec-Einheiten. Defaultwert: 196 |
| BE4B | * | 8 | Resultpuffer für µPD 765 (siehe Datenblatt) |
| BE53 | * | 1 | Seek Disk number (logische Laufwerksnummer; wird durch BIOS Routine `SELDSK` gesetzt) |
| BE54 | * | 1 | Seek Track number (logische Spurnummer; wird durch BIOS Routine `SELTRK` gesetzt) |
| BE55 | * | 1 | Seek Sector number (logische Sektornummer = Recordnummer; wird durch BIOS Routine `SELSEK` gesetzt) |
| BE56 | * | 1 | Host disk number (Nummer des physikalischen Laufwerks; wird im BIOS ermittelt) |
| BE57 | * | 1 | Host Track number (physikalische Spurnummer; wird im BIOS ermittelt) |
| BE58 | * | 1 | Host Sektor number (physikalische Sektornummer; wird im BIOS ermittelt) |
| BE59 |   | 1 | Seek/Host Flag (siehe unten) |
| BE5A |   | 1 | unalloc record counter |
| BE5B |   | 1 | unalloc drive number |
| BE5C |   | 1 | unalloc track number |
| BE5D |   | 1 | unalloc sector number (logisch) |

**Bedeutung der Seek/Host Flag Bits (BE59):**

| Bit | Bedeutung |
|-----|-----------|
| 0–3 | Writetype: 0 = allocated, 1 = Directory, 2 = unallocated |
| 4 | 0 = write, 1 = read |
| 5 | 1 = Pre-read |
| 6 | Host active Flag |
| 7 | Host write Flag |

Die Bits 5–7 werden beim Blocking/Deblocking benötigt.

**Anmerkung zu den unalloc-Variablen:** Das BIOS hat grundsätzlich drei Möglichkeiten, einen Record zu schreiben:

1. Directory Write
2. Allocated Write
3. Unallocated Write

Wie wir bereits wissen, muß in einem "geblockten" BIOS nicht bei jedem Record Write unbedingt sofort auch die physikalische Schreiboperation durchgeführt werden. Hier gibt es jedoch eine sehr wichtige Ausnahme, und das sind Schreiboperationen in die Directory. Selbstverständlich muß die Directory laufend auf dem aktuellsten Stand sein, weshalb jeder zu schreibende Directory-Record auch sofort auf die Diskette gebracht werden muß (kein Blocking!).

Bevor ein Record gelesen oder geschrieben werden kann, müssen dem BIOS über `SELDSK`, `SELTRK`, `SELSEK` und `SETDMA` die "Koordinaten" des Records übergeben werden – ein derartiger Zugriff heißt auch **unallocated**, da der Block, in den der Record geschrieben/von dem er gelesen werden soll, vollständig definiert wird. Es gibt aber auch noch eine weitere Möglichkeit des Recordzugriffs, und zwar genau dann, wenn dem BIOS bereits die Blockkoordinaten übergeben (**allocated**) wurden und nun alle folgenden Records des Blocks gelesen/geschrieben werden sollen. Dieser Zugriff ist selbstredend schneller als der in einen neuen (unallocated) Block.

| Adresse | AMSDOS | Länge | Bedeutung |
|---------|--------|-------|-----------|
| BE5E |   | 1 | Seek/Recalibrate/ID-Flag |
| BE5F |   | 1 | Zwischenspeicher für die Steprate des momentan selektierten Laufwerks |
| BE60 | * | 2 | Adresse des augenblicklichen Recordpuffers; 128 Bytes (wird durch die BIOS Routine `SETDMA` gesetzt) |
| BE62 | * | 2 | Adresse des Hostbuffers (512 Bytes). Sektorpuffer für einen physikalischen Sektor. |
| BE64 |   | 1 | Retry Count: Anzahl der Versuche im Fehlerfall. Defaultwert: 16 |
| BE65 |   | 2 | Stackzwischenspeicher beim BIOS Einsprung |
| BE67 | * | 6 | Tick Block für Motor on/off Counter |
| BE6D | * | 7 | Event Block für Motor on/off Counter |
| BE74 |   | 1 | Zwischenspeicher für uPD-Kommando |
| BE75 |   | 2 | Basisadresse des relokatiblen DOS RAM-Bereichs. Defaultwert: `A700H`, wenn VDOS ROM Nummer 7 |
| BE77 |   | 2 | Adresse einer DOS-Routine im ROM. Defaultwert: 0 |
| BE79 |   | 2 | Codestring für P-Schutz (wird über RSX Kommando `|CODE` gesetzt) |
| BE7B |   | 1 | Message Flag: 0 = Fehlermeldungen werden angezeigt, FFH = Fehlermeldungen werden unterdrückt |
| BE7C |   | 1 | Unter BASIC: EOF-Flag (0 = teste EOF Marker, FFH = kein Test); unter CP/M: FAST-Flag (0 = normal, FFH = verschnellert) |
| BE7D |   | 2 | Keine Bedeutung unter BASIC; unter CP/M: Basisadresse des relokatiblen RAM-Bereichs |
| BE7F |   | 1 | Nur X-Laufwerk unter BASIC: Konfigurationsbyte (0 = 5,25" Laufwerk ist Laufwerk A, 1 = 5,25" Laufwerk ist Laufwerk B); wird durch RSX-Kommando `|X` gesetzt |

Die folgenden Variablen sind unter BASIC und CP/M sehr unterschiedlich und werden deshalb getrennt abgehandelt:

#### BASIC

| Adresse | Länge | Bedeutung |
|---------|-------|-----------|
| BE80 | 2 | Zwischenspeicher für Stackpointer |
| BE82 | 1 | Zwischenspeicher für Error Code |
| BE83-BE8E | | keine Bedeutung |
| BE8F | 3 | Select Disk DOS Indirection (springt BIOS Routine `SELDSK` an) |
| BE92 | 3 | Set Track DOS Indirection (springt BIOS Routine `SETTRK` an) |
| BE95 | 3 | Set Sector DOS Indirection (springt BIOS Routine `SETSEK` an) |
| BE98 | 3 | Set DMA DOS Indirection (springt BIOS Routine `SETDMA` an) |
| BE9B | 3 | Read Record DOS Indirection (springt BIOS Routine `READ` an) |
| BE9E | 3 | Write Record DOS Indirection (springt BIOS Routine `WRITE` an) |
| BEA1 | 3 | Position Head DOS Indirection. Einsprung: Akku = logische Spurnummer. Aussprung: Akku = physikalische Spurnummer |
| BEA2-BEB9 | | Routine für Error Patch |
| BEBA | 2 | Basis Adresse für relative Dateiverwaltung |
| BEBF | 1 | Nummer des ersten Sektors bei Disk I/O |
| BEC0 | 1 | Nummer des letzten Sektors bei Disk I/O |

Während des ROM WALKs bis zu dem Zeitpunkt, wo BASIC seinen READY Loop erreicht, haben beim CPC 464 folgende Variablen eine andere Bedeutung:

| Adresse | Länge | Bedeutung |
|---------|-------|-----------|
| BE80 | 6 | Tick Block für Hello Loader |
| BE86 | 7 | Event Block für Hello Loader |

**Ein paar Worte zur Bedeutung der DOS Indirections und zur Funktionsweise der Hello Sequenz:**

Die DOS Indirections stellen eine wohldefinierte Schnittstelle zwischen DOS und BIOS dar. Das DOS greift nur über diese Indirections auf das BIOS, also auf die Laufwerke, zu. Die Beschreibung der Übergabeparameter finden Sie im CP/M-Teil bei der Erklärung des BIOS Einsprung-Vektors.

Die Hello-Sequenz, der "Turn Key Mechanismus", in dessen Genuß allerdings nur 464-Besitzer kommen, basiert auf der Idee, das BASIC nach dem ROM WALK abzufangen, bevor es in den READY Loop einspringt. (Der Ready Patch ist nur beim 464/BASIC 1.0 möglich!) Es hat allerdings keinen Sinn, die BASIC READY Indirection bereits beim ROM WALK zu patchen, da BASIC, nachdem es den ROM WALK durchgeführt hat, erst einmal alle BASIC Indirections initialisiert (`C9H`) und somit den Patch löschen würde. Die ROM WALK Routine im VDOS ROM setzt deshalb die READY Indirection auf einen definierten Anfangszustand (`00`) und erzeugt dann einen Ticker, der die BASIC READY Indirection laufend auf `C9H` testet – während dessen läuft der ROM WALK weiter. Wird ein `C9H` gefunden, so wird der READY Patch durchgeführt und der Hello Lader in den RAM nach `BF00H` kopiert. Springt BASIC nun die READY Indirection an, so verzweigt das Programm nach `BF00H` in den Hello Lader. Dieser löscht den Ticker, setzt die READY Indirection auf `C9H`, testet, ob eine Taste gedrückt wurde und bricht ab, wenn dies der Fall war. Wenn nicht, prüft es den Laufwerksstatus von Laufwerk A. Befindet sich keine Diskette im Laufwerk, so wird auch abgebrochen. Liegt eine Diskette im Laufwerk, so sucht der Lader nach der Datei `HELLO.BAS`. Hat er sie gefunden, so lädt er sie ins BASIC Memory und startet.

#### CP/M

| Adresse | AMSDOS | Länge | Bedeutung |
|---------|--------|-------|-----------|
| BE80 | * | 3 | Message Flag: 0 = Meldungen an, FFH = Meldungen aus. Einsprung: Akku = neuer Wert. Aussprung: Akku = alter Wert |
| BE83 | * | 3 | Zeitkonstanten Initialisieren. `HL` = Zeiger auf Parameterbereich |
| BE86 |   | 3 | Verschiedene Funktionen: Akku = FFH und E = Laufwerksnummer (0,1) -> HL = Zeiger auf DPB Flag Byte; Akku = FEH -> Setzt bzw. löscht FAST Flag; Akku = 1 -> Laufwerk A=3", B=5,25"; Akku = 2 -> Laufwerk A=5,25", B=3"; Akku = 0 -> Laufwerk A=B=5,25" |
| BE89 | * | 3 | Lese einen physikalischen Sektor. Einsprung: HL=Sektorpuffer, C=erster Sektor, B=letzter Sektor (falls Multisektor), E=Laufwerk, D=Spur. Aussprung: Carry=1/Akku=0 erfolgreich, Carry=0/Akku=Error Code |
| BEAC | * | 3 | Schreibe einen physikalischen Sektor (Parameter wie Lesen) |
| BEAF | * | 3 | Formatiere eine ganze Spur. Einsprung: HL=Sektorpuffer, E=Laufwerk, D=Spur |
| BE92 | * | 3 | Positioniere den Kopfschlitten. Einsprung: E=Laufwerk, D=Spur |
| BE95 | * | 3 | Teste den Laufwerksstatus. Einsprung: Akku=Laufwerksnummer. Aussprung: Carry=1 -> Akku=ST3, Carry=0 -> HL=Zeiger in uPD Result Puffer |
| BE98 | * | 3 | Ändere Retry Count. Einsprung: Akku=neuer Wert. Aussprung: Akku=alter Wert |
| BE9B | * | 3 | BIOS Entry. Sichert Stack und sorgt für richtige ROM Konfiguration |
| BE9E |   | 3 | Schalte Motor sofort aus |
| BEA1 |   | 3 | Position Head Indirection |
| BEA4 | * | 3 | Initialisiere Console Puffer. Einsprung: HL=Zeiger auf String, A=Clear Flag |
| BEA7 |   | 3 | Eingabe Status SIO 1 |
| BEAA |   | 3 | Eingabe Status SIO 2 |
| BEAD |   | 3 | Ausgabe Status SIO 1 |
| BEB0 |   | 3 | Ausgabe Status SIO 2 |
| BEB3 |   | 3 | Hole Zeichen von SIO 1 |
| BEB6 |   | 3 | Hole Zeichen von SIO 2 |
| BEB9 |   | 3 | Sende Zeichen an SIO 1 |
| BEBC |   | 3 | Sende Zeichen an SIO 2 |

Die SIO Treiber sind im BIOS noch nicht vorhanden, und so führen die Routinen `BEA7`–`BEBC` in Dummy-Routinen (Schreiben) oder liefern einen EOF Marker (`1AH`, Lesen).

#### Variablen des Diskettenmonitors

| Adresse | Länge | Bedeutung |
|---------|-------|-----------|
| BEC1 | 1 | aktuelle Laufwerksnummer (laut L Kommando) |
| BEC2 | 1 | aktuelle Spurnummer (laut T Kommando) |
| BEC3 | 1 | aktuelle Sektornummer (laut S Kommando) |
| BEC4 | 2 | aktuelle Bufferadresse (laut B Kommando) |
| BEC6 | 1 | interne Variable |
| BEC7 | 1 | interne Variable |
| BEC8 | 1 | Nummer des oberen ROM's (laut Y Kommando) |
| BEC9 | 1 | 0 = Firmware ROM aus, FF = an (laut X Kommando) |

#### Variablen des Monitors

| Adresse | Länge | Bedeutung |
|---------|-------|-----------|
| BECD | 3 | Faradresse für FAST Indirection |
| BED0 | 3 | Faradresse für Breakpoint |
| BED3 | 2 | aktuelle Adresse für M Kommando |
| BED5 | 2 | aktuelle Adresse für L Kommando |
| BED7 | 2 | aktuelle Adresse für F Kommando |
| BED9 | 2 | aktuelle Adresse für D Kommando |
| BEDD | 1 | CP/M Flag: 0 = VDOS aktiv, FF = CP/M aktiv |
| BEDE | 2 | Stackpointer beim Einsprung in den Monitor |
| BEE0 | 1 | interne Variable |
| BEE1 | 1 | interne Variable |
| BEE2 | 1 | Opcode Zwischenspeicher |
| BEE3 | 2 | Zwischenspeicher für Programmverzweigungen |
| BEE5 | 2 | Zwischenspeicher für Stackpointer |
| BEE7 | 2 | Zwischenspeicher für HL |
| BEE9 | 2 | Anzahl Traceschritte |
| BEEB | 2 | Zwischenspeicher für AF |
| BEEC | 2 | User AF |
| BEEE | 2 | User BC |
| BEF0 | 2 | User DE |
| BEF2 | 2 | User HL |
| BEF4 | 2 | User IX |
| BEF6 | 2 | User IY |
| BEF8 | 2 | User SP |
| BEFA | 1 | interne Variable |
| BEFB | 2 | User PC |
| BEFD | 1 | Distanz bei relativen Z80 Befehlen |
| BEFE | 1 | internes Flag |
| BEFF | 1 | internes Flag |
| BF00 | 24 | Breakpoint Arbeitsbereich |
| BF80 |   | Monitorstack |

#### Relokatibler RAM-Bereich des VDOS 2.0 ROM's

Der relokatible RAM-Bereich des VDOS 2.0 ROM's unterscheidet sich weitgehend von dem des AMSDOS ROM. Alle angegebenen Adressen sind relativ und beziehen sich auf die Basis des RAM-Bereichs. Sitzt der ROM in einer Fassung mit der höchstmöglichen Background ROM Nummer, so ist diese Basis-Adresse `A700H`.

| Offset | Länge | Bedeutung |
|--------|-------|-----------|
| 0 | 1 | Login Flag Laufwerk A. 0 = Laufwerk noch nicht angemeldet, FFH = Laufwerk angemeldet |
| 1 | 1 | Login Flag Laufwerk B (s.o.) |
| 2 | 1 | interne Variable |
| 3 | 2 | DPH Adresse des Defaultlaufwerks |
| 5 | 1 | augenblickliche User Nummer |
| 6 | 1 | augenblickliche Laufwerksnummer |
| 7 | 2 | Zeiger auf momentanen FCB (File Control Block) |
| 9 | 1 | Reihenzähler für CAT/DIR Kommando |
| A | 2 | Directory Counter |
| C-12 | 7 | interne Variablen |
| 13 | 1 | Anzahl der Zeichen für FCB - Directory Entry Vergleich |
| 14 | 1 | Laufwerksnummer aus aktuellem FCB |
| 15 | 1 | DOS Flag 2: Bit 1 = Read/Write random (0 = read, 1 = write) |
| 16-18 | 3 | interne Variablen |
| 19 | 1 | DOS Flag 1: Bit 1: 0=random nicht aktiv, 1=random aktiv; Bit 2: 0=write, 1=read; Bit 3: 0=random, 1=sequentiell |
| 1A,1B | 2 | interne Variablen |
| 1C | 2 | Zwischenspeicher für DMA Adresse |
| 1E | 1 | Speicher für Anzahl der CAT-Entries |
| 1F | 2 | Zeiger in CAT RAM Puffer |
| 21,22 | 2 | interne Variablen |
| 23 | 2 | Speicher für Stackpointer für Fehlerfall |
| 25-44 | 32 | Arbeits-FCB |
| 45-68 | 36 | Input FCB |
| 69-8C | 36 | Output FCB |
| 92-B2 | 33 | Input Header |
| B3-D3 | 33 | Output Header |
| E0-15F | 128 | Record Puffer |
| 164-178 | 21 | CAS Input Vektor |
| 179-187 | 15 | CAS Output Vektor |
| 188 | 3 | CAS CAT Vektor |
| 18B | 3 | Far Adresse zum DOS Entry Handler |
| 190 | 23 | ALV 0 |
| 1A7 | 23 | ALV 1 |
| 1BE | 128 | Directory Puffer |
| 23E | 512 | Host Puffer |
| 43E | 16 | DPH 0 |
| 44E | 16 | DPH 1 |
| 45E | 39 | CSV 0 |
| 485 | 39 | CSV 1 |
| 4AC | 25 | DPB 0 |
| 4C5 | 25 | DPB 1 |

**Bemerkungen:** Der Input- und Output-FCB haben die CP/M Standardstruktur (siehe CP/M unter der Lupe).

Die Header haben folgenden Aufbau (alle Adressen beziehen sich auf den Headeranfang):

| Adresse | Länge | Bedeutung |
|---------|-------|-----------|
| 0 | 1 | Mode Byte: 1 = CHAR Mode, 2 = DIRECT Mode |
| 1 | 2 | Adresse des Blockpuffers |
| 3 | 2 | Zeiger auf nächstes Zeichen im Blockpuffer |
| 5 | 1 | User Byte |
| 6 | 8 | Dateiname |
| E | 3 | Extension |
| 11 | 4 | nicht benutzt |
| 15 | 1 | Nummer des aktuellen Blocks |
| 16 | 1 | 00 = noch nicht letzter Block |
| 17 | 1 | Filetyp |
| 18 | 2 | Dateilänge |
| 1A | 2 | Data Allocation Adresse |
| 1C | 1 | 00 = nicht erster Block |
| 1D | 2 | Länge |
| 1F | 2 | Startadresse für Maschinenprogramm |
| 21 | 3 | Byte Counter für DOS |
| 24 | 2 | Checksumme |

#### Relative Dateiverwaltung

VDOS 2.0 kann gleichzeitig 16 relative Dateien verwalten (16 Kanäle). Die Feldlänge auf jedem Kanal ist beliebig und nur durch den verfügbaren Speicher begrenzt. Die Manipulation des BASIC `HIMEM`'s erfolgt über das RSX Kommando `|FILES`.

Der BASIC RAM bei aktiver relativer Dateiverwaltung hat folgenden Aufbau:

![BASIC Ram Aufbau](basic_mem.png)

Die einzelnen Arbeitsbereiche hängen über Linkadressen zusammen, so muß sich das DOS nur die Basisadresse des Gesamtbereichs merken. Der Arbeitsbereich eines Kanals hat dabei folgende Struktur (alle Adressen beziehen sich auf die Basis-Adresse des Kanal-Arbeitsbereichs):

| Adresse | Bedeutung |
|---------|-----------|
| 0 | Kanal-Nummer (mögliche Nummern liegen zwischen 0 und 127 je einschließlich. Ist Bit 7 gesetzt, so ist der Kanal augenblicklich aktiv.) |
| 1 | Link-Adresse zum nächsten Kanalbereich |
| 3 | max. Feldlänge; wurde in `|FILES` definiert |
| 5 | aktuelle Feldlänge; wurde in `|OPEN` definiert |
| 7 | aktuelle Recordnummer |
| 9 | Zeiger auf Recordpuffer |
| B | unbenutzt |
| D | 36 FCB |
| 31 | Feldmasken (max. 16) |
| 51 | unbenutzt |
| 5A | Recordpuffer (Länge in `|FILES` definiert) |

#### Struktur des Zeitkonstanten-Bereichs

| Offset | Länge | Bedeutung |
|--------|-------|-----------|
| 0 | 2 | Motor on counter |
| 2 | 2 | Motor off counter |
| 4 | 1 | nicht benutzt |
| 5 | 1 | Kopfberuhigungszeit |
| 6 | 1 | kombinierte Steprate |
| 7 | 1 | HUT Byte (siehe uPD Datenblatt) |
| 8 | 1 | HLT Byte (siehe uPD Datenblatt) |

---

## CP/M unter der Lupe – CP/M-Betriebssystem

CP/M ist genauso wie das CPC BASIC ein eigenständiges Betriebssystem. Es besteht aus drei Komponenten:

- dem **Console Command Processor** – CCP
- dem **Basic Disk Operating System** – BDOS
- dem **Basic Input Output System** – BIOS

CP/M wurde von DRI (Digital Research Inc.) entwickelt und auch nur DRI hat das alleinige Recht, Lizenzen zu vergeben. Wenn Sie also auf einer Diskette eines Ihrer eigenen Programme weitergeben, achten Sie darauf, daß keine CP/M-Spuren drauf sind, sonst machen Sie sich einer Copyright-Verletzung schuldig.

Bevor wir auf die Einzelteile von CP/M näher eingehen, hier zunächst einmal die Speicheraufteilung:

![Speicheraufteilung von CP/M](cpm_memory.png)

### Zero Page

Die Zero Page (Seite 0; Adresse `00`–`FFH`) wird vom CP/M als Daten- und Arbeitsbereich benötigt. Fast jedes Byte hat eine Bedeutung, und eine unüberlegte Manipulation führt meist zum Absturz von CP/M.

| Adresse | Bedeutung |
|---------|-----------|
| 00H-02H | Warmstart; hier steht ein Sprung nach `biospage+3` |
| 03H | I/O Byte |
| 04H | Defaultlaufwerk |
| 05H-07H | BDOS Einsprung; hier steht ein Sprung nach `bdospage+6` |
| 08H-27H | Restart 1-5 |
| 30H-37H | Restart 6 |
| 38H-3AH | Restart 7 |
| 3BH-5BH | momentan unbenutzt; reserviert |
| 5CH-7CH | Default FCB |
| 7DH-7FH | random number (optional) |
| 80H-FFH | Default record Puffer |

Besonders interessant für den Anwender ist hier z.B. der Default FCB bei `5CH`. Nehmen wir einmal an, Sie rufen eine Kommandodatei (Extension `COM`) auf, indem Sie

```
DATEI filename.ext<ENTER>
```

eingeben, so legt der CCP automatisch einen FCB für die Datei `filename.ext` an – das nimmt Ihnen schon die Arbeit ab.

### TPA

Die TPA – **Transient Program Area** – ist der eigentliche "Nutzbereich" von CP/M. In der TPA läuft z.B. Ihr WordStar ab. Die TPA beginnt genau bei der Adresse `100H` und geht maximal bis zur `bdospage`, d.h. der CCP kann von einem Anwenderprogramm überladen werden, ohne die CP/M-Umgebung zu verlieren. Der CCP (und das BDOS) werden beim nächsten Warmstart nachgeladen. Ein Anwenderprogramm kann unter Umständen auch das BDOS überladen, darf dann aber auf keine einzige BDOS Funktion mehr zugreifen (sonst Crash) – dies scheint aber eher ein Spezialfall zu sein, der wohl in der Praxis so gut wie nie auftritt.

### CCP

Der CCP – **Console Command Processor** – ist sozusagen Ihr "Ansprechpartner", wenn Sie mit CP/M arbeiten. Der CCP ist in der Lage, Kommandos, die Sie unter Einhaltung einer strengen Syntax eingeben, durchzuführen. Neben der wichtigsten Fähigkeit, nämlich Programme in die TPA laden und dort starten zu können, beinhaltet der CCP auch noch sogenannte residente Kommandos wie z.B. `DIR`, `SAVE`, `TYPE` oder `REN`. Gerade die strenge Kommandosyntax – d.h. auf gut Deutsch der nur geringe Bedienungskomfort – hat dafür gesorgt, daß CP/M lange Zeit nur etwas für "Spezialisten" war und nicht die Popularität von BASIC Betriebssystemen erreicht hat. Doch auch Sie werden sehen, daß CP/M, wenn einmal ein Minimalverständnis erreicht ist, ein außerordentlich elegantes und vielseitiges "Tool" darstellt.

### BDOS

Das BDOS – **Basic Disk Operating System** – ist das eigentliche Herz von CP/M. Wie der Name bereits suggeriert, entspricht es seiner Funktion nach dem DOS im VDOS 2.0 ROM. Die einzelnen Funktionen im BDOS werden weiter unten tabellarisch aufgeführt. Es sei an dieser Stelle auch auf die einschlägige Literatur verwiesen – es gibt inzwischen schon etliche sehr gute Bücher über CP/M (auch für den Einsteiger).

CCP und BDOS befinden sich auf den sogenannten Systemspuren einer CP/M Diskette und werden während des Warmstarts immer wieder neu in den Speicher geladen.

### BIOS

Das BIOS – **Basic Input Output System** – ist das Verbindungsglied zwischen der Hardware und dem BDOS. Bei einer Standard CP/M Implementation befindet sich das BIOS ebenfalls wie das BDOS und der CCP auf der Diskette und wird einmal beim Kaltstart gebootet (Bootstrap = an den Haaren aus dem Dreck ziehen -> Münchhausen). Bei den CP/M Implementationen auf den CPC's wurde das BIOS aus Gründen der Effizienz in einen ROM (VDOS oder AMSDOS) übernommen, denn nur so kann das DOS in einfacher Art und Weise auf die Floppy zugreifen. Das BIOS ist ebenfalls eine Programmbibliothek, die grob gesehen in zwei logische Gruppen zerfällt:

- Nicht-Disk Input Output
- Disk Input Output

Die erste Gruppe ermöglicht es CP/M, mit der Außenwelt – das sind in diesem Fall Sie – zu kommunizieren, während die zweite Gruppe Ihre Daten verwaltet.

### Der RAM unter CP/M

Da der nicht-relokatible RAM-Bereich weitgehend vom BIOS genutzt wird, wird er in derselben Art und Weise auch unter CP/M genutzt. Zusätzlich benutzt CP/M noch folgende Variablen (alle Adressen hexadezimal):

| Adresse | Länge | Bedeutung |
|---------|-------|-----------|
| ACF8 | 23 | ALV 0 |
| AD0F | 23 | ALV 1 |
| AD26 | 128 | Directory Puffer |
| ADA6 | 512 | Host Puffer |
| AFA6 | 16 | DPH 0 |
| AFB6 | 16 | DPH 1 |
| AFC6 | 39 | CSV 0 |
| AFED | 39 | CSV 1 |
| B014 | 25 | DPB 0 |
| B02D | 25 | DPB 1 |
| B046 | 3 | Bios Entry Handler |
| B049 | 2 | Original Interrupt Entry |
| B04B | 2 | Gate Array Status |
| B04D | 1 | Cursor Flag |
| B04E | 1 | Console Puffer Flag |
| B04F | 2 | Console Puffer Zeiger |
| B051 | 1 | Console Puffer Counter |
| B052 | 128 | Console Puffer |
| B0D2 | 2 | Zwischenspeicher für Stack |

### Struktur des Disk Parameter Blocks (DPB)

Der Disk Parameter Block einer vortex Floppy besteht aus zwei Teilen: dem Standard CP/M Teil und einer VDOS-spezifischen Erweiterung. Bedeutung der einzelnen Einträge (Struktur der Tabelle: Defaultwert, Anzahl Bytes, Kurzbezeichnung, Erklärung; alle Werte dezimal):

**Standardteil:**

| Default | Bytes | Kurzbezeichnung | Erklärung |
|---------|-------|-----------------|-----------|
| 36 | 2 | SPT | Anzahl der Records pro Spur |
| 5  | 1 | BSH | Block Shift Faktor |
| 31 | 1 | BLM | Block Maske |
| 3  | 1 | EXM | Extent Maske |
| 176 | 2 | DSM | Gesamtzahl der Blöcke-1 |
| 127 | 2 | DRM | Gesamtzahl der Directoryeinträge-1 |
| 128 | 2 | AL0,1 | erste zwei Bytes des ALV |
| 32 | 2 | CKS | Länge des CSV |
| 2  | 2 | OFF | Anzahl der Systemspuren |

**vortex-spezifische Erweiterung:**

| Default | Bytes | Kurzbezeichnung | Erklärung |
|---------|-------|-----------------|-----------|
| 1   | 1 | MASK | Sektormaske = Nummer des 1. Sektors |
| 9   | 1 | ST   | Anzahl der physikalischen Sektoren pro Spur |
| 42  | 1 | GP0  | Länge von GAP0 (Schreiben/Lesen) |
| 82  | 1 | GP1  | Länge von GAP1 (Formatieren) |
| 229 | 1 | FILL | Filler Byte für Format Kommando |
| 2   | 1 | N    | Bytes/Sektor (-> 512) |
| 4   | 1 | BLK  | Blocking Faktor; 4 Records pro Sektor |
| 79  | 1 | ATRK | aktuelle physikalische Spurnummer |
| 79  | 1 | MTRK | max. Anzahl Spuren pro Seite -1 |
| 1   | 1 | FLAG | Flag Byte |

**Bedeutung der einzelnen Bits im Flag Byte:**

| Bit | Funktion |
|-----|----------|
| *nur Flag von Laufwerk A* | |
| 1 | Boot Flag: 0 = Bootmessage eingeschaltet, 1 = Bootmessage ausgeschaltet |
| 2 | nicht benutzt (unter VDOS 1.0: Message Flag) |
| 3 | Motor Flag: 0 = Motor aus, 1 = Motor an |
| *beide Laufwerke* | |
| 0 | Anzahl der Köpfe -1 |
| 4 | Multi Sektor Flag: 0 = ein Sektor I/O, 1 = Multi Sektor I/O |
| 5 | Laufwerk Typ: 0 = 5,25"/3,5", 1 = 3" |
| 6 | Recalibrate Flag: 0 = recalibriere Kopfschlitten vor nächstem Positionieren, 1 = kein Recalibrate |

### Struktur des Disk Parameter Headers (DPH)

(Aufbau der Tabelle: Defaultwert, Anzahl Bytes, Erklärung; alle Werte dezimal)

| Default | Bytes | Erklärung |
|---------|-------|-----------|
| 0 | 2 | Arbeitsvariable (Adresse der Sektorübersetzung) |
| 0 | 2 | "-" |
| 0 | 2 | "-" |
| 0 | 2 | "-" |
| DIRBUFF | 2 | Adresse des Directory Puffers |
| DPB | 2 | Adresse des Disk Parameter Blocks |
| CSV | 2 | Adresse des Check Size Vektors |
| ALV | 2 | Adresse des Allocation Vektors |

### Aufbau eines File Control Blocks (FCB)

CP/M – respektive sein BDOS – kann auf Dateien nur zugreifen, wenn diesen zuvor ein sogenannter File Control Block, kurz FCB, zugeordnet wurde. Der FCB enthält alle Angaben über die Datei, die das BDOS benötigt, um eindeutig auf sie zugreifen zu können. Der Standard FCB ist 33 Bytes, der random FCB 36 Bytes lang.

Hier nun die Bedeutung der einzelnen Bytes der Reihe nach (erste Spalte = Kurzbezeichnung, zweite Spalte = Länge in Bytes/dezimal, dritte Spalte Erklärung):

| Kurzbez. | Länge | Erklärung |
|----------|-------|-----------|
| DR | 1 | Laufwerks Code. 0 = Defaultlaufwerk, 1-16 = Autoselect Laufwerk A-P |
| FN | 8 | Dateiname |
| EXT | 3 | Extension |
| EX | 1 | Nummer des augenblicklichen Extents |
| S1,S2 | 2 | interne Variable |
| RC | 1 | Record Counter innerhalb des augenblicklichen Extents |
| ALLT | 16 | Blockbelegungstabelle (wird vom BDOS geladen) |
| CR | 1 | momentane Recordnummer für Schreib-/Leseoperation |
| R0,R1,R2 | 3 | Random Record Nummer (optional) |

### Der Allocation Vektor

Der ALV – Allocation Vektor (Belegungstabelle) – spielt eine zentrale Rolle bei der Diskettenverwaltung CP/M-ähnlicher Betriebssysteme. Sein Aufbau ist sehr einfach:

```
Byte 0   | Byte 1   | Byte 2   ...........

Bit:    76543210   76543210   76543210
```

Jedes Bit steht für einen Block auf der Diskette (die Zählung beginnt bei 0). Ist ein Block belegt, so wird das entsprechende Bit gesetzt. Das DOS muß den ALV laufend auf dem aktuellen Stand halten, da ansonsten Daten falsch auf der Diskette abgelegt werden. Legt man eine neue Diskette ein und meldet diese durch `^C` an, so veranlaßt das DOS die Neuanlage des ALV. Ob eine Diskette gewechselt wurde, stellt das DOS mithilfe des sogenannten CSV fest.

Die Länge des ALV ist im wesentlichen die Gesamtzahl der Blöcke geteilt durch 8.

### Der Check Size Vektor

Der CSV – Check Size Vektor – hat die einzige Aufgabe, dem DOS zu sagen, ob eine Diskette gewechselt wurde. Dies funktioniert folgendermaßen: Das DOS berechnet über jeden Directory-Record (128 Bytes; 4 Einträge à 32 Bytes) eine Einbyte-Checksumme und legt diese Checkbytes geordnet im CSV ab. Der CSV wird bei der Arbeit mit der Diskette laufend aktualisiert. Ein `^C` erzwingt die Neuanlage des CSV. Wird eine Diskette nun gewechselt, ohne daß man sie angemeldet hat (`^C`), so erkennt dies das DOS in 99,9% aller Fälle an einer Inkompatibilität des CSV. Es könnte aber durchaus einmal der Fall sein, daß zwei Directory-Records dieselbe Checksumme bei verschiedenem Inhalt haben. Mit diesem Risiko muß/kann man leben.

Die Länge des CSV erhält man, indem man die Gesamtzahl der Directoryeinträge durch 4 teilt.

### Der BIOS Jump Vektor

Der BIOS Jump Vektor hat die nachfolgende Struktur. Sie können den BIOS Vektor unter CP/M folgendermaßen finden: Starten Sie einen Debugger, z.B. den `DDT`, und sehen Sie nach, welche Adresse in der Speicherstelle 1 steht. Sie finden dort die Adresse `wboot` der Warmstart-Routine im Jump Vektor.

Einsprünge in den BIOS Vektor auf nicht Disk I/O Geräte (z.B. Console, List, …) sind meist harmlos und führen allerhöchstens zum Absturz, wenn Sie etwas falsch machen. Sprünge auf Disk-Routinen können da schon wesentlich mehr Unheil anrichten. Also: immer erst Diskette raus und "wertlose" Diskette rein.

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

| Routine | Einsprung | Aussprung |
|---------|-----------|-----------|
| CONST   | — | A=FF Zeichen bereit; A=00 kein Zeichen bereit |
| CONIN   | — | A = eingelesenes Zeichen |
| CONOUT  | C = Zeichen | — |
| LIST    | C = Zeichen | — |
| PUNCH   | C = Zeichen | — |
| READER  | — | A = Zeichen (=1AH wenn EOF) |
| HOME    | — | — |
| SELDSK  | C = Laufwerk | HL = DPH-Adresse; HL = 0 Laufwerk nicht vorhanden |
| SETTRK  | BC = Spurnummer | — |
| SETSEC  | BC = Recordnummer | — |
| SETDMA  | BC = DMA-Adresse | — |
| READ    | — | A=0 alles OK, sonst Fehler |
| WRITE   | C = Write Modus | A=0 alles OK, sonst Fehler |
| LISTST  | — | A=0 Drucker nicht bereit; A=FF Drucker bereit |
| SECTRAN | BC = Recordnummer, DE = Transtable | HL = übersetzte Recordnummer |

### BDOS Einsprünge

Wie wir ja bereits wissen, ist das BDOS ein wesentlicher Bestandteil des CP/M Betriebssystems. Das BDOS ist eigentlich nur eine Programmbibliothek. Wollen Sie selbst unter CP/M Maschinenprogramme machen, so können Sie die BDOS Funktionen mitbenutzen – und das Schöne: der Aufruf einer BDOS Funktion ist systemunabhängig, d.h. wenn Sie jetzt auf Ihrem CPC ein CP/M Programm schreiben, das streng mit BDOS Funktionen arbeitet, so wird dies (abgesehen vielleicht von einer Videoanpassung) z.B. auch auf einem KAYPRO sofort und uneingeschränkt laufen – der BDOS Einsprung bei `5` ist eben auch eine standardisierte Schnittstelle.

Die Nummer der BDOS Funktion muß beim Aufruf im `C`-Register übergeben werden.

#### BDOS Funktionen

| Nr. | Funktion | Einsprung | Aussprung |
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

Genauere Informationen sind der einschlägigen Literatur zu entnehmen.

---

## Abschließend noch ein paar Worte zur Hardware

### X-Laufwerke

Die Hardware der X-Laufwerke besteht lediglich aus einem ROM Modul mit RS232C (optional) Schnittstelle. Die ROM Nummer ist frei einstellbar (zweireihige 16-polige Stiftleiste). Die ROM Fassung ist in der Lage, sowohl 16 KB- als auch 32 KB-ROMs aufzunehmen. Letztere werden als zwei ROMs à 16 KB verwaltet -> eigene ROM-Nummer.

Die Steuerports der seriellen Schnittstelle:

| Port | Funktion |
|------|----------|
| FADC | SIO Daten |
| FADD | SIO Control |
| FBDC | Counter 0 |
| FBDD | Counter 1 |
| FBDF | Mode Wort |

### Laufwerke + Controller

Laufwerke mit eigenem Controller belegen standardmäßig die Ports:

**CPC 464:**

| Port | Funktion |
|------|----------|
| FB7E | µPD Control |
| FB7F | µPD Daten |
| FA7E | Motor |

**CPC 664 / 6128:**

| Port | Funktion |
|------|----------|
| FBF6 | µPD Control |
| FBF7 | µPD Daten |
| FA7E | Motor |

für die Laufwerkssteuerung.

Beim Controller mit integriertem ROM Modul/Eprommer sind die Portadressen über einen Dekoder-ROM frei einstellbar.

---

## Pinbelegung der Connectoren

### Floppy Disk Schnittstellen-Connector(en) am Controller

#### 5,25" Connector

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

Stromversorgung:

- Pin 1: +12V (Input) oder Ground
- Pin 3, 5, 7: +5V (Input)
- alle anderen ungeraden Pins: Ground

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

Stromversorgung:

- Pin 21, 29, 31, 33: +5V (Input)
- alle geraden Pins: Ground

### RS 232C Connector

Grundsätzlich besitzen alle vortex RS 232C Schnittstellen einen 25-poligen "männlichen" DTE Connector.

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

### DIN Buchse am X-Laufwerk

(Buchse von hinten gesehen)

```
      3
      •
  2 •   • 4
  1 •   • 5
```

| Pin | Funktion |
|-----|----------|
| 1, 2 | +5V (bei dreipoliger Buchse nur 1) |
| 4, 5 | +12V (bei dreipoliger Buchse nur 5) |
| 3 | Ground |

Sowohl Controller mit RS-Schnittstelle als auch X/RS-Platine besitzen ebenfalls eine DIN Buchse, dort ist die Pinbelegung gerade umgekehrt:

| Pin | Funktion |
|-----|----------|
| 1, 2 | +12V |
| 4, 5 | +5V |
| 3 | Ground |

### Spannungsversorgung vortex Floppy Controller (nicht X-Laufwerke)

Der Floppy Controller erhält über die Buchsenleiste B3 im Laufwerksgehäuse (d.h. über 34-poliges Flachbandkabel) +5V.

![Power Connector](power_connector.png)

Stromversorgung an den Kartensteckern:

- Pin 3, 5, 7: +5V
- alle anderen ungeraden Pins: Ground

Beschriftung gilt bei Blick in die Öffnung der Buchsenleiste. Die Buchsenleiste kommt in ca. 12 cm Abstand von den 2 (1) Kartensteckern, die auf die Drives gesteckt werden.

### Laufwerke

Das an den vortex Controller angeschlossene Laufwerk erfüllt folgende Spezifikationen:

| Parameter | Wert |
|-----------|------|
| Kapazität (unformatiert) | 1 MB |
| Datenübertragungsrate    | 250K Bits/sec |
| Spurwechselzeit          | min. 4 msec |
| Kopfberuhigungszeit      | max. 20 msec |
| Motorhochlaufzeit        | max. 1 sec |
| Drehzahl                 | 300 rpm |
| Anzahl Köpfe             | 2 |
| Spuren/Oberfläche        | min. 80 |
| Modulation               | FM/MFM |
| Spurdichte               | 96 tpi |

> *Alle Änderungen vorbehalten.*

---

## Stichwortverzeichnis

> **(!) Hinweis:** Die Seitenzahlen beziehen sich auf die Originalausgabe des Handbuchs. In dieser markdown-Version sollten Sie die Inline-Suche oder das Inhaltsverzeichnis benutzen.

### A

- `|A` – 16, 21, 22, 23, 26, 27, 28, 32, 43, 56
- ALV – 4, 125, 130, 132, 133, 134
- `|AMSDOS` – 32, 43
- `|ATTRIBUT` – 26, 27, 28, 56
- Akku – 113, 114, 116, 120, 122, 123
- Ausgabekanal – 33, 34, 44
- Autostart – 60, 89, 94, 95, 97, 98

### B

- `|B` – 16, 21, 22, 23, 29
- BAK – 20, 21, 24, 25, 27
- BDOS – 72, 103, 129, 130, 131, 134, 136, 137
- BIOS – 6, 36, 94, 97, 98, 102, 107, 108, 109, 112, 117, 118, 119, 120, 121, 123, 129, 131, 132, 135
- BOOTGEN – 17, 64
- BOS – 43
- Back Up – 99
- Background – 43, 116, 117, 125
- Bdospage – 129, 130
- Betriebssystem – 1, 2, 5, 6, 12, 13, 14, 15, 16, 17, 32, 44, 57, 61, 62, 66, 67, 68, 70, 81, 100, 107, 108, 116, 117, 130, 134, 136
- Binär – 19, 20, 39, 40, 58
- Biospage – 129
- Blockbelegung – 57, 110, 111, 134
- Blocking – 107, 108, 119, 133
- Bootsektor – 68, 102
- Breakpoint – 35, 37, 38, 40, 123, 124
- Bug – 35, 135
- Bytefolgen – 42

### C

- `|CAS` – 33, 34, 39, 44
- CAS CATALOG – 116
- CAS IN ABANDON – 114
- CAS IN CHAR – 114, 115
- CAS IN CLOSE – 114
- CAS IN DIRECT – 115
- CAS IN OPEN – 114
- CAS OUT ABANDON – 116
- CAS OUT CLOSE – 115
- CAS OUT DIRECT – 116
- CAS OUT OPEN – 115
- CAS RETURN – 115
- CAS TEST EOF – 115
- `|CAS.OUT` – 34
- CASCOPY – 68, 99, 103, 104
- CAT – 18, 22, 23, 24, 26, 27, 30, 33, 54, 55, 58, 89, 90, 91, 93, 94, 95, 96, 97, 98, 116, 119, 125, 126, 133, 134
- CCP – 129, 130, 131
- `|CLOSE` – 31, 46, 49, 50, 51, 56, 57
- CLOSEIN – 45, 53, 57
- CLOSEOUT – 31, 45, 52, 55, 57
- `|CODE` – 31
- CP/M 2.2 – 2, 3, 5, 6, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 80, 86
- CP/M 2.2 Systemdiskette – 61, 63, 64, 66, 67, 68
- CP/M BIOS Vektor – 109
- CP/M Kaltstart – 109, 135
- CP/M Warmstart – 109, 135
- CP/M plus – 2, 3, 4, 5, 6, 61, 66, 67, 68, 69, 71
- CP/M plus Diskette – 66, 67, 68, 71
- CP/M-Lader – 88
- `|CPM` – 60, 61, 62, 64, 66, 67, 68, 70, 71, 72, 73, 76, 81, 102
- `|CPM,1` – 62, 67, 68, 70, 72, 73
- `|CPM,2` – 64, 66, 68, 71, 72, 73, 76, 81
- CRC Fehler – 58
- CSV – 125, 132, 133, 134, 135
- CTRL C – 91, 94, 97, 103
- Cassetten-Rekorder – 33
- Catalog – 24, 30, 116
- Centronics – 113
- Connectoren – 138

### D

- DATA-Only – 17, 85, 106
- `|DERROR` – 54, 55, 58, 59
- DIN Buchse – 139, 140
- `|DIR` – 14, 15, 16, 21, 24, 25, 26, 27
- `|DISC` – 33, 34, 44
- `|DISC.IN` – 33, 34
- `|DISC.OUT` – 34
- DISKTOOL – 17, 64, 65, 66, 68, 69, 83, 84, 86, 87, 88, 105, 106
- DPB – 118, 122, 125, 132, 133, 137
- DPH – 118, 125, 132, 133, 136
- DRI – 2, 9, 19, 40, 55, 62, 69, 118, 119, 129, 134, 137, 140
- Datei – 2, 6, 12, 14, 15, 16, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 34, 39, 40, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 60, 64, 67, 69, 72, 74, 75, 77, 78, 79, 80, 81, 86, 87, 88, 89, 95, 99, 100, 103, 104, 106, 109, 110, 111, 112, 114, 115, 116, 121, 126, 127, 130, 134
- Dateibezeichnung – 19, 20, 29, 40, 55, 104, 106
- Dateiname – 20, 25, 29, 39, 40, 74, 75, 78, 80, 104, 110, 111, 115, 126, 134
- Dateityp – 20, 39, 40, 75, 100
- Datenrekorder – 33, 99
- Deblocking – 107, 108, 119
- Debugger – 35, 135
- Directory – 2, 6, 8, 9, 22, 24, 27, 55, 56, 64, 71, 85, 86, 103, 109, 110, 111, 112, 119, 125, 132, 133, 135
- Disk Parameter – 132, 133
- Diskettenfehler – 37, 54, 59
- Diskettenmonitor – 35, 36, 37, 123

### E

- EOF – 45, 115, 120, 123, 136
- EOF Problem – 59, 149
- `|ERA` – 27, 28, 29, 56
- Eingabekanal – 33, 34
- Entwanzer – 35
- Extension – 20, 67, 110, 126, 130, 134
- Extent – 110, 111, 132, 134

### F

- F1-X – siehe X-Laufwerke
- FAST – 24, 25, 27, 68, 100, 101, 107, 120, 122, 123, 129
- FCB – 46, 125, 126, 127, 130, 134, 137
- FDA-1 – 84
- FDC – 55, 57, 58
- `|FIELD` – 46, 47, 48, 49, 50, 51, 52, 56, 57
- FILECOPY – 68, 72, 73, 74, 75, 76, 77, 78, 79, 83, 106
- `|FILES` – 46, 47, 48, 49, 50, 51, 52, 56, 57
- `|FORMAT` – 15, 16, 18, 28
- Fehlerbyte – 58
- Fehlercode – 54, 55, 57, 58
- File – 19, 46, 47, 48, 49, 50, 51, 52, 55, 56, 57, 68, 72, 73, 74, 75, 76, 77, 78, 79, 83, 104, 106, 109, 112, 114, 115, 116, 125, 126, 127, 130, 134, 137
- Firmware ROM – 41, 123
- Floppy Disk Station – 1, 12

### G

- `|GET` – 15, 46, 48, 49, 50, 51, 52, 56, 57

### H

- HEX/ASCII – 35, 37, 38
- HIMEM – 46, 127
- Hardware – 12, 107, 108, 117, 131, 138
- Hello-Datei – 60
- Hostbuffer – 36, 120

### I

- I/O Byte – 89, 90, 91, 93, 94, 95, 96, 97, 98, 129, 137
- ID-Feld – 58
- INPUT#9 – 45, 52
- INSTALL – 14, 60, 68, 77, 78, 81, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 102, 104, 105, 107
- Indirection – 120, 121, 123

### R

- RAM Variablen – 117
- RAM-Karte – 43, 66, 106
- `|REN` – 29, 56
- `|RESET` – 31
- ROM WALK – 117, 121
- `|ROMOFF` – 43
- `|ROMS` – 43
- RS232C – 2, 5, 8, 96, 113, 138
- RSX – 14, 42, 43, 120, 127
- Random File – 46
- Rekordpuffer – 46, 47, 48, 49, 56, 57
- Relative Datei – 2, 12, 45, 121, 127
- Reservierte Spuren – 16, 85, 86
- Reset – 6, 31, 32, 43, 60, 100, 101, 137
- Rücksetzen – 31, 32

### S

- SAVE – 18, 19, 20, 31, 34, 40, 56, 60, 62, 80, 130
- `|SELECT` – 26, 28, 29, 30
- SIO – 2, 8, 9, 12, 20, 42, 43, 52, 67, 91, 93, 104, 110, 112, 113, 117, 123, 126, 130, 134, 137, 138
- SYSGEN – 17, 62, 63, 64, 68, 81, 82, 88, 103
- Schreib/Lesekopf – 32, 90
- Segment – 47, 48, 49, 52, 56
- Sektor – 15, 16, 17, 36, 37, 58, 65, 68, 81, 83, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 102, 104, 105, 108, 109, 119, 120, 121, 122, 123, 133
- Sektorgröße – 108
- Sektornummer – 16, 17, 36, 108, 119, 123
- Sequentielle Datei – 44, 45
- Software – 1, 2, 16, 17, 70, 107, 112, 113
- Spuren – 10, 15, 16, 17, 32, 62, 65, 70, 81, 82, 83, 85, 86, 88, 105, 106, 110, 129, 131, 132, 133, 141
- Stepper – 90
- Steprate – 89, 90, 118, 119, 128
- Streamnummer – 112
- Stringvariablen – 46, 47
- Systemdiskette – 61, 63, 64, 65, 66, 67, 68, 70, 71, 81, 102
- Systemformat – 16, 85
- Systemspuren – 17, 62, 65, 81, 82, 83, 85, 88, 105, 106, 131, 132

### T

- TPA – 69, 129, 130
- Tracer – 35
- Track – 10, 15, 118, 119, 120, 139
- Transient – 81, 83, 89, 100, 130
- Treiber – 107, 108, 123
- Turnkey – 6, 60

### U

- µPD 765 – 57, 118
- USER – 14, 16, 18, 21, 24, 25, 26, 27, 28, 29, 30, 72, 73, 74, 76, 78, 110, 124, 125, 126, 137
- USER Bereiche – 26

### V

- VDOS 2.0 – 2, 17, 62, 64, 107, 117, 118, 125, 131
- VDOS Modul – 5, 7, 8, 9
- Vendorformat – 16, 17, 85

### W

- WBOOT – 109, 135
- WRITE#9 – 45
- Wanze – 35
- Wildcard – 25, 26, 28, 29, 74, 75, 78

### X

- `|X` – 16, 18, 22, 23, 35, 41, 71, 120
- `|XMON` – 35, 41
- XMON – 35, 36, 39, 41, 68, 80
- XPATCH30 – 67, 68

### Z

- Z80 – 2, 4, 12, 35, 39, 41, 68, 80, 108, 113, 124
- Z80 Register – 108, 113
- Zero Page – 129
- Ziel – 12, 15, 26, 63, 65, 66, 70, 72, 73, 74, 75, 76, 77, 79, 81, 82, 85, 86, 87, 88, 89, 97, 105, 106, 112, 114, 115
- Ziel-Laufwerk – 65, 72, 73, 74, 76, 87, 88, 89
- Zieldiskette – 63, 66, 81, 82, 85, 86, 87, 105, 106
- Zugriff – 12, 46, 52, 54, 63, 90, 108, 109, 112, 118, 119

### Sonderzeichen / Zahlen

- `^C` – 103, 134, 135
- `$OSC.SYS` – 86, 88
- 3" Laufwerk – 2, 6, 8, 9, 16, 18, 21, 22, 23, 36, 44, 57, 60, 61, 62, 64, 67, 68, 70, 71, 76, 84, 94, 97, 98, 105, 112, 118
- 62K CP/M – 66, 86, 88, 106

---

## Anhang: Das EOF Problem

VDOS 2.0 hat wie auch schon VDOS 1.0 eine "Schwachstelle", die allerdings nicht auf Programmierfehler oder Unnachsichtigkeit zurückzuführen ist, sondern weitgehend in der Struktur des CPC BASICs und in der angestrebten 3"-Kompatibilität zu suchen ist.

Wie Sie ja vielleicht bereits wissen, hat das AMSDOS unter anderem auch den sogenannten "MERGE-Fehler". Dieser äußert sich darin, daß Sie plötzlich beim "Zumergen" eines BASIC Programms auf einen "EOF met" Fehler stoßen können, ohne daß jedoch das Ende der Datei tatsächlich auch erreicht worden wäre. So einfach die Diagnose des Fehlers auch ist, so schwer ist er zu beseitigen. Richtig, es gibt zwar z.B. den "DATA Becker Patch", der dieses Problem anscheinend beseitigt, aber dafür andere Fehler erzeugt.

Um es nicht bei bloßen Worten zu belassen, hier einige Hintergrundinformationen:

Das Ende einer ASCII-Datei wird vereinbarungsgemäß durch ein `CTRL`+`Z` (= `1A` hexadezimal) markiert. Dies ist immer dann wichtig, wenn es nicht ausreicht, das Ende nur modulo 128, d.h. recordweise erkennen zu können (dies ist das sogenannte **Hard end** einer Datei), sondern wenn es darauf ankommt, dieses wirklich auf ein Byte genau wieder zu finden.

Aus diesem Grund wird auch im AMSDOS und aus Kompatibilitätsgründen selbstverständlich auch im VDOS das `1A` als EOF Marker eingesetzt. Das ist soweit auch schön und gut, wenn nur sichergestellt ist, daß `1A` wirklich nur am Ende und nicht auch irgendwo in der Datei selbst vorkommen kann.

Hier beginnen aber bereits die Schwierigkeiten: Die Firmware im CPC sieht zum Einlesen der Daten von der Peripherie (Cassette/Diskette) zwei standardisierte Möglichkeiten vor:

1. **Funktion 128 (`BC80h`): CAS/DISC IN CHAR** – liest einzelne Zeichen ein
2. **Funktion 129 (`BC83h`): CAS/DISC IN DIRECT** – liest ganze Speicherblöcke ein

Probleme macht Funktion 128, haben wir hier doch folgende Return-Bedingungen (Carry und Zero sind Prozessorflags des Z80):

```
Carry true
Zero false
```

wenn ein Zeichen von der Peripherie-Einheit gelesen werden konnte, und

```
Carry false
Zero false
```

falls dies nicht möglich war, d.h. das Dateiende wurde erreicht.

Es gibt nun aber leider zwei Kriterien für das Ende einer Datei:

- **Kriterium 1:** `CTRL`+`Z` (`1Ah`) wurde detektiert (Soft end).
- **Kriterium 2:** Das physikalische Ende wurde erreicht, d.h. das war der letzte Record (Hard end).

Das CPC BASIC testet nun genau über Funktion 128 das Dateiende, und zwar egal, ob eine reine ASCII-Datei oder aber eine Binärdatei (z.B. ein BASIC Programm) geladen wird.

Deshalb können Sie z.B. mitten im "Mergen" eines BASIC Programms ein "EOF met" bekommen – z.B. wenn eine Zeilennummer 26 (= `1Ah`) vorkommt. EOF Kriterium 1 schlägt da unerbittlich zu. Der "DATA Becker Patch" z.B. beseitigt nun diesen Mißstand, sorgt aber andererseits dafür, daß nunmehr das Ende einer ASCII-Datei nicht mehr richtig erkannt wird. (Der Patch eliminiert einfach Kriterium 1.)

Das Dilemma liegt einfach darin, daß sich über ein und dieselbe Routine, nämlich Firmware Funktion 128, nicht ASCII- und Binärdateien mit demselben EOF Marker laden lassen, dies führt unweigerlich zu einem Widerspruch, der immer nur mit einem "Entweder… Oder" zu lösen ist. Leider wurde dies im CPC BASIC und/oder AMSDOS nicht bedacht.

Nun zum VDOS: In der 1.0 Version wurde nur Kriterium 1 berücksichtigt, weshalb es auch möglich war, nach Lust und Laune zu "mergen". Allerdings mit dem Erkennen des Dateiendes einer sequentiellen ASCII-Datei gab es Schwierigkeiten; es wurden u.U. 127 Zeichen zu viel eingelesen.

VDOS 2.0 löst den Gordischen Knoten folgendermaßen: Der Benutzer entscheidet, welche EOF Kriterien er benötigt. Hierzu dient die RSX Funktion `|DERROR`.

- `|DERROR,2<ENTER>` aktiviert sowohl die reine Hard-end-Erkennung als auch das Testen auf den EOF Marker `1Ah` (Soft end) und ist vornehmlich dafür gedacht, das Ende sequentieller Textdateien richtig erkennen zu können. Selbstverständlich taucht hier unerbittlich beim "Mergen" das "EOF met" Problem auf.

- Deshalb gibt es auch noch `|DERROR,3<ENTER>` – dies ist im Übrigen der Defaultzustand nach dem Einschalten oder nach einem RESET und entspricht VDOS 1.0 – hier wird nur auf das physikalische Dateiende (Hard end) getestet, d.h. es gibt kein "EOF met" Problem beim "Mergen", dafür aber Schwierigkeiten bei sequentiellen Textdateien.

Entscheiden Sie also in Ihrem Programm selbst, was Sie weniger stört.

---

*Ende des Handbuchs*
