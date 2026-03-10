# JAWS súgó szakfordítási prompt

## Feladat összefoglalása

JAWS képernyőolvasó súgófájljainak professzionális fordítása angolról magyarra, korábbi fordítási memóriák (PO fájlok) és terminológiai adatbázis (jaws.po) felhasználásával.

---

## Mappastruktúra

```
Fordítás/Help/
├── HTM/          ← Angol forrásfájlok (aktuális JAWS verzió, pl. 2026)
├── PO/           ← Fordítási memóriák (előző verzió, pl. 2024) – .po fájlok
├── HU/           ← Magyar célnyelvi fájlok (a te kimeneteid)
└── jaws.po       ← Fő terminológiai adatbázis (~180 000 sor)
```

---

## Alapszabályok (KÖTELEZŐ betartani)

### 1. Az angol HTM a forrás – TÖRÖLNI TILOS
- Az angol 2026-os HTM fájl határozza meg, mi legyen a magyar fordításban.
- Ami az angolban szerepel, annak a magyarban is szerepelnie KELL.
- Soha, semmilyen körülmények között ne törölj tartalmat a magyar vagy angol HTM fájlokból.
- Ha a PO fordítás rövidebb, mint az angol szöveg, a teljes angol tartalmat kell lefordítani.

### 2. PO fájlok = fordítási referencia
- Minden angol szegmenshez keresd meg a megfelelő PO bejegyzést (msgid → msgstr).
- Ha a PO msgid **pontosan egyezik** az aktuális angol szöveggel → használd a PO msgstr fordítást **karakterre pontosan**.
- Ha a PO msgid **hasonló, de változott** → a PO fordítás szolgál alapul, de a változásokat le kell fordítani.
- Ha **nincs PO egyezés** (teljesen új tartalom) → te fordítod, a jaws.po terminológia és a PO stílus alapján.

### 3. Terminológia: jaws.po
- A jaws.po fájl tartalmazza a JAWS program hivatalos magyar terminológiáját.
- Minden szakkifejezésnél, menünévnél, párbeszédpanel-névnél, billentyűparancsnál ellenőrizd a jaws.po-t.
- A jaws.po-ban található fordítások felülírják a te saját fordítási ötleteidet.
- Különösen figyelj a billentyűkiosztásokra – a magyar JAWS-ban eltérhetnek az angoltól (pl. ALT+H → ALT+S a Súgó menühöz).

### 4. HTML struktúra megőrzése
- Az eredeti HTML címkéket, attribútumokat, osztályneveket, stílusokat érintetlenül kell hagyni.
- A hivatkozásokat (href) frissítsd, ha az angol 2026-os forrásban változtak.
- Az `lang="en"` attribútumot változtasd `lang="hu"`-ra.
- A `<meta>` kulcsszavakat fordítsd le magyarra.

### 5. Verziófrissítés
- A verziószámot frissítsd az aktuális verzióra (pl. "JAWS 2025" → "JAWS 2026").
- Ez az egyetlen eset, ahol a PO-tól való eltérés automatikusan megengedett.

---

## Részletes munkafolyamat

### I. fázis: Elemzés és előkészítés

1. **Olvasd el a feladatleírást** (Feladat.txt), ha van.
2. **Listázd az összes fájlt** mindhárom mappában (HTM, PO, HU).
3. **Párosítsd a fájlokat**: minden angol HTM-hez keresd meg a megfelelő PO-t.
4. **Készíts feladatlistát** (TodoWrite) a fájlokról, és haladj egyesével.

### II. fázis: Fordítás fájlonként

Minden egyes fájlnál kövesd ezt a sorrendet:

#### 1. lépés: Angol forrás megértése
- Olvasd el az angol 2026-os HTM fájlt teljes egészében.
- Azonosítsd a fő szegmenseket (címek, bekezdések, listák, táblázatok).

#### 2. lépés: PO egyeztetés
- Olvasd be a megfelelő PO fájlt.
- Minden angol szegmenshez keresd meg a PO msgid-t.
- Jelöld meg:
  - ✅ **Pontos egyezés**: msgid = angol 2026 szöveg → msgstr pontosan használandó
  - ⚠️ **Részleges egyezés**: msgid hasonló, de változott → msgstr alapján fordítsd az újat
  - 🆕 **Nincs egyezés**: új tartalom → te fordítod

#### 3. lépés: Terminológia ellenőrzés (jaws.po)
- Keresd ki a szakkifejezéseket a jaws.po-ban.
- Különösen ellenőrizd:
  - Menünevek (pl. Help menu = Súgó menü)
  - Párbeszédpanel-nevek
  - Billentyűparancsok (INSERT, CTRL, ALT kombók)
  - Funkciók nevei (pl. Settings Center = Beállítási központ)

#### 4. lépés: Magyar HTM elkészítése
- Másold az angol 2026-os HTM struktúráját.
- Cseréld a tartalmat a megfelelő magyar fordításra.
- Ahol PO egyezés van → pontosan a PO szövege.
- Ahol nincs → saját fordítás a jaws.po és PO stílus alapján.
- **NE hagyj ki semmit az angolból!**

#### 5. lépés: Ellenőrzés
- Vesd össze az angol forrást és a magyar kimenetet szegmensenként.
- Ellenőrizd, hogy minden angol szegmensnek van magyar megfelelője.
- Ellenőrizd a HTML struktúra épségét.

### III. fázis: Minőségbiztosítás

Az összes fájl elkészülte után végezz egy végső ellenőrzést:
- Fájlonként vesd össze a PO-t és a HU HTML-t.
- Azonosítsd, hol használtad a PO-t pontosan, és hol tértél el (indokkal).
- Készíts összefoglalót a változásokról.

---

## Lokalizációs sajátosságok (magyar JAWS)

### Billentyűparancsok
- A magyar Windows-ban a menü-gyorsbillentyűk eltérhetnek az angoltól.
- Példa: az angol Help menü ALT+H, de a magyar Súgó menü ALT+S.
- Mindig a jaws.po-ból ellenőrizd a helyes billentyűt.

### Magyar specifikus linkek
- A magyar JAWS súgóban bizonyos szekciók (pl. "Webes források") lokalizált linkeket tartalmaznak.
- Ilyen linkek lehetnek például:
  - infoalap.hu (Informatika a Látássérültekért Alapítvány)
  - Profivox beszédszintetizátor letöltése
  - Magyar JAWS levelezőlista
  - Ország licenc weboldal (akadalymentes.magyarorszag.hu)
  - ZoomText, MAGic magyar információs lapok
- Ezeket a korábbi PO fordításból kell átvenni – pontosan azokat a linkeket és leírásokat használd, amelyek a PO-ban szerepelnek.

### Angol-specifikus tartalom
- Bizonyos funkciók csak angolul működnek (pl. Voice Assistant / "Hey Sharky" hangparancsok).
- Ezeknél a PO-ban kialakított megoldást kövesd (pl. "Az angol JAWS esetében használja a Hangvezérlést").

### Glosszárium-jelölők
- A PO fájlokban `<?rh-glo_start class="glossterm"?>` jelölők lehetnek.
- Az újabb HTML verzió ezeket nem feltétlenül használja – ez rendben van.
- A szöveges tartalom legyen ugyanaz, a jelölők megléte/hiánya nem probléma.

---

## Ismert PO hibák kezelése

A PO fájlok emberi munkával készültek, és tartalmazhatnak hibákat:
- **Billentyű-elírások**: pl. a layered_keystrokes.po-ban a "C" billentyű "B"-ként, a "B" billentyű "H"-ként szerepelt. Ilyenkor a jaws.po a mérvadó – abban a program tényleges billentyűkiosztása van.
- **Elírások**: pl. "Winddows" (dupla d) → javítsd "Windows"-ra.
- Ha PO hibát találsz, **jelezd a felhasználónak**, és használd a helyes verziót (jaws.po alapján).

---

## Példa szegmens-egyeztetésre

```
ANGOL 2026 (HTM):
"This menu item provides access to information on how to contact
Freedom Scientific Technical Support."

PO MSGID (2024):
"This menu item provides access to information on how to contact
Freedom Scientific Technical Support."

PO MSGSTR:
"E menüparancs segítségével megnyitható a JAWS súgójának
Technikai tanácsadás fejezete."

DÖNTÉS:
→ A PO msgid PONTOSAN egyezik az angol 2026-os szöveggel.
→ De a PO fordítás RÖVIDEBB, mint az angol (hiányzik a "contact" rész).
→ Mivel TÖRÖLNI TILOS: a PO fordítást használjuk ALAPKÉNT,
   de kiegészítjük a hiányzó tartalommal:

MAGYAR (HU):
"E menüparancs segítségével megnyitható a JAWS súgójának
Technikai tanácsadás fejezete, ahol a Freedom Scientific
technikai tanácsadó szolgálatának elérhetőségeiről tájékozódhat."
```

---

## Összefoglaló ellenőrzőlista

Minden fájl leadása előtt ellenőrizd:

- [ ] Minden angol szegmensnek van magyar megfelelője (nincs kihagyott tartalom)
- [ ] A PO fordítások pontosan lettek átvéve, ahol egyezés volt
- [ ] A jaws.po terminológia következetesen van alkalmazva
- [ ] A verziószámok frissítve vannak (pl. 2025 → 2026)
- [ ] Az URL-ek az angol 2026-os forrásnak megfelelnek
- [ ] A magyar specifikus linkek a PO-ból pontosan átvéve
- [ ] A billentyűparancsok a jaws.po szerint helyesek
- [ ] A HTML struktúra sértetlen (lang="hu", meta kulcsszavak lefordítva)
- [ ] Nem történt tartalom-törlés

---

## A fordításról – rövid összefoglaló

A JAWS súgó magyar szövegei **AI-alapú szakfordítással** készültek, a Cursor környezetben, a fenti szabályok és prompt alapján.

**Ki indította:** Herczeg Lajos összeállította a 2024 és 2026 közötti különbségeket, és 9 HTM fájlt jelölt ki tesztre. Szuhaj Mihály és Farkas Márk vették kézbe az AI-alapú szakfordítás kipróbálását.

**Források:**
- **HTM (angol):** A JAWS 2026 legfrissebb angol súgófájljai – ezek a lefordítandó források.
- **PO fájlok:** Korábbi (2024-es) fordítási memória, Poedit-tel készült angol–magyar fordítási egységekkel. Ahol az angol egyezik, a PO magyar szövegét pontosan használjuk; ahol változott, onnan folytatjuk a fordítást.
- **jaws.po:** A JAWS program hivatalos magyar felületi és terminológiai fordításai – ezt kell követni menüneveknél, billentyűparancsoknál, párbeszédpaneleknél.

**Folyamat:** Fájlonként haladtunk: angol HTM → PO egyeztetés → jaws.po terminológia → magyar HTM (HU) kimenet. A HTML struktúra és a tartalom teljessége megmaradt; ahol a PO rövidebb volt, a hiányzó részt pótoltuk. A billentyűkiosztásokat és a magyar specifikus linkeket a jaws.po és a PO alapján igazítottuk.

**Cél:** Ha ez a technika beválik, jelentősen csökkentheti a súgó-frissítés terheit a következő JAWS verzióknál.

**Volt magyar nyelvű előzmény?** Igen. A fordítás nem nulláról indult. A **PO fájlok** már tartalmazták a 2024-es magyar szövegeket (msgstr), tehát volt hivatkozási magyar anyag, stílus és kifejezésvilág. A **jaws.po** pedig a program hivatalos magyar felületi szövegeit adta (menük, gombok, billentyűk). Ezekre az előzményekre támaszkodva a feladat az volt: az új angol (2026) szöveget ehhez a meglévő magyar kontextushoz igazítani – ahol az angol változatlan, a PO fordítását pontosan átvenni; ahol változott vagy új a szöveg, onnan a PO és a jaws.po stílusát követve folytatni.

**Hogyan végeztem el (AI / Cursor):** A fenti prompt és szabályok alapján fájlonként dolgoztam. Minden HTM-nél: (1) beolvastam az angol forrást és a megfelelő PO fájlt, (2) szegmensenként összevetettem az angol 2026 szöveget a PO msgid-vel – pontosan egyező helyen a msgstr-t használtam, hasonlónál a PO magyar szövegét alapul véve pótoltam a változást, új szövegnél a jaws.po-t és a PO stílusát követve fordítottam, (3) a jaws.po-ból kikeresettem a szakkifejezéseket és billentyűparancsokat, (4) a magyar HTM-t az angol struktúra másolásával állítottam össze, a tartalmat a kapott magyar szöveggel helyettesítve, (5) ellenőriztem, hogy ne maradjon ki angol szegmens és hogy a HTML sértetlen maradjon. A TodoWrite-pal a haladást követtem fájlonként. Tehát a fordítás szisztematikus, szabályvezérelt folyamat volt, a meglévő magyar előzményre építve.

---

## Fordítási statisztika (előzmény)

A PO fájlok alapján (a `po_stat.py` scripttel számolva):

| | Szegmensek | Volt magyar előzmény (msgstr nem üres) | Nem volt előzmény (msgstr üres) |
|--|--|--|--|
| **Összesen** | **2 143** | **481 (22,4%)** | **1 662 (77,6%)** |

**Volt előzménye (2024-es magyar PO):** csak a **Main Help** 9 fájlja – ezekben a PO fájlokban már szerepelt a korábbi magyar fordítás (msgstr kitöltve). Fájlok: `Help/PO/` – Message_Center, convenient_ocr, help_menu_overview, layered_keystrokes, network_authorization_instructions, overview_of_the_jaws_utilities, start, system_requirements, technical_support. Összesen 481 szegmens ezekben; ezeknek szinte mindegyikének volt magyar előzménye (a fejlécen kívül).

**Nem volt előzménye:** a **Tovabbi_anyagok** mind az 57 PO fájlja – itt a msgstr üres, a szövegeket az AI nulláról (a jaws.po terminológia és a PO stílus alapján) fordította. Mappák: `Help/Tovabbi_anyagok/PO_us/` (50 fájl) és `Help/Tovabbi_anyagok/new/PO_us/` (3 fájl: Accessing_Math_Content, Braille_Math_Editor, FSCompanion). Összesen 1 662 szegmens; ezeknek egyikének sem volt korábbi magyar fordítása a PO-ban.

A statisztika újraszámolható a `Fordítás/po_stat.py` futtatásával.

---

## A prompt használata

Másold be ezt a promptot egy új Cursor/AI chat elejére, és add hozzá:

```
Kérlek végezd el a fordítást a fenti szabályok szerint.
A fájlok itt találhatók: @Fordítás/Help
A feladatleírás: @Fordítás/Feladat.txt
Haladj fájlonként, használj TodoWrite-ot a haladás követéséhez.
```
