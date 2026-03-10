# -*- coding: utf-8 -*-
"""PO fájlok statisztikája: volt-e magyar előzmény (msgstr nem üres)."""
import re
import os

def parse_po(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Üres msgstr: msgstr "" és utána nincs folytatósor (nincs \n" )
    # Egy bejegyzés: msgstr "" VAGY msgstr "x" VAGY msgstr ""\n"x"\n"y"
    parts = re.split(r'\n(?=#:|msgid\s+)', content)
    total = 0
    with_prior = 0
    for part in parts:
        if 'msgstr' not in part:
            continue
        # Egy msgstr blokk ebben a részben
        after_msgid = part.split('msgstr', 1)
        if len(after_msgid) < 2:
            continue
        msgstr_rest = after_msgid[1].lstrip()
        if not msgstr_rest.startswith('"'):
            continue
        # Üres: msgstr "" és a következő nem " karakterrel kezdődő sor
        first_line = msgstr_rest.split('\n')[0]
        if first_line.strip() == '""':
            # Többsoros lehet: ""\n" szöveg "
            rest = msgstr_rest[len(first_line):].strip()
            if rest.startswith('"'):
                val = rest.strip('"').split('"')[0][:50]
                if not val.startswith('Project-Id-Version:'):
                    with_prior += 1
            total += 1
        else:
            # msgstr "valami" - nem üres (kivéve header)
            val = first_line.strip().strip('"')[:30]
            if not val.startswith('Project-Id-Version:'):
                with_prior += 1
            total += 1
    return total, with_prior

def main():
    base = os.path.join(os.path.dirname(__file__), 'Help')
    totals = {}
    for root, dirs, files in os.walk(base):
        po_files = [f for f in files if f.endswith('.po') and f != 'jaws.po']
        for f in po_files:
            path = os.path.join(root, f)
            try:
                total, with_prior = parse_po(path)
            except Exception as e:
                print(path, e)
                continue
            key = path.replace(base, 'Help').replace('\\', '/')
            totals[key] = (total, with_prior)

    total_entries = sum(t[0] for t in totals.values())
    total_prior = sum(t[1] for t in totals.values())
    total_no_prior = total_entries - total_prior

    print("=== PO szegmens statisztika ===\n")
    print(f"Összesen vizsgált fájl: {len(totals)}")
    print(f"Összes szegmens: {total_entries}")
    print(f"  Volt magyar előzmény (msgstr nem üres): {total_prior} ({100*total_prior/total_entries if total_entries else 0:.1f}%)")
    print(f"  Nem volt előzmény (msgstr üres):        {total_no_prior} ({100*total_no_prior/total_entries if total_entries else 0:.1f}%)")
    print("\n--- Fájlonként (előzmény / összes) ---")
    for k in sorted(totals.keys()):
        t, p = totals[k]
        no_p = t - p
        print(f"  {k}: {p} / {t}  (nincs előzmény: {no_p})")

if __name__ == '__main__':
    main()
