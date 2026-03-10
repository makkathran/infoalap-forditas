# JAWS súgó fordítás – infoalap-forditas repo

## GitHub ágak

- **`master`** – alap ág, teljes tartalom (HTM, PO, HU, HU2, SettingsCenter, dokumentáció).
- **`cursor/jaws-s-g-ford-t-s-kieg-sz-t-s-ec32`** – **Cursor ág**: ugyanaz a tartalom, mint a master (HU, HU2, SettingsCenter, po_stat.py, friss dokumentáció). Ezt az ágat érdemes használni, ha Cursorral dolgozol a fordítás mappán: klónozáskor vagy pullnál ezt az ágat vedd le, hogy a Cursor minden aktuális mappával (pl. SettingsCenter) tudjon dolgozni.

**Utolsó feltöltés (cursor ágra):** 2026.03.08 – HU, HU2, Help/SettingsCenter, po_stat.py, JAWS_forditas_prompt.md bővítések.

### Cursorral dolgozás

```bash
git clone https://github.com/makkathran/infoalap-forditas.git
cd infoalap-forditas
git checkout cursor/jaws-s-g-ford-t-s-kieg-sz-t-s-ec32
```

Vagy ha már klónoztad a repót:

```bash
git fetch origin
git checkout cursor/jaws-s-g-ford-t-s-kieg-sz-t-s-ec32
git pull
```

---

A fordítási szabályok és a prompt: **JAWS_forditas_prompt.md**.
