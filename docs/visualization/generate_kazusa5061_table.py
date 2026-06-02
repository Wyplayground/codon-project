"""Regenerate aspergillus_niger_5061.csv (observed_count only) from Kazusa CGI snapshot.

Run: python generate_kazusa5061_table.py
Output: aspergillus_niger_5061.csv next to this script.
"""
from __future__ import annotations

from pathlib import Path

# Snapshot: https://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi?species=5061
KAZUSA_BLOCK = """
UUU 12.8( 78285)  UCU 14.0( 86042)  UAU 12.3( 75100)  UGU  5.8( 35261)
UUC 23.8(145663)  UCC 19.0(116511)  UAC 17.1(104725)  UGC  8.3( 50889)
UUA  5.1( 31278)  UCA 10.6( 65095)  UAA  0.6( 3916)  UGA  0.9( 5689)
UUG 16.4(100325)  UCG 14.0( 85723)  UAG  0.7( 4444)  UGG 15.3( 93788)
CUU 15.4( 94490)  CCU 15.2( 93422)  CAU 12.3( 75191)  CGU 10.1( 61861)
CUC 22.4(137051)  CCC 17.8(109010)  CAC 12.8( 78227)  CGC 15.9( 97559)
CUA  8.9( 54445)  CCA 13.1( 80260)  CAA 15.8( 96611)  CGA  9.3( 57162)
CUG 23.0(141009)  CCG 14.2( 87312)  CAG 24.2(148296)  CGG 11.2( 68379)
AUU 16.7(102080)  ACU 13.6( 83396)  AAU 14.9( 91080)  AGU 10.6( 64937)
AUC 26.2(160337)  ACC 21.3(130788)  AAC 21.0(129023)  AGC 15.4( 94652)
AUA  6.9( 42354)  ACA 12.4( 76029)  AAA 14.1( 86447)  AGA  7.9( 48671)
AUG 22.0(134646)  ACG 12.9( 79289)  AAG 29.6(181722)  AGG  7.6( 46656)
GUU 14.7( 89946)  GCU 21.7(132918)  GAU 27.8(170550)  GGU 17.5(107274)
GUC 21.8(133437)  GCC 27.2(166685)  GAC 27.2(166885)  GGC 22.5(137915)
GUA  6.9( 42490)  GCA 17.4(106738)  GAA 24.8(151769)  GGA 16.1( 98975)
GUG 18.6(114235)  GCG 17.2(105173)  GAG 34.7(212844)  GGG 12.6( 77463)
"""

ORDER: list[tuple[str, str]] = [
    ("*", "TAA"),
    ("*", "TAG"),
    ("*", "TGA"),
    ("A", "GCA"),
    ("A", "GCC"),
    ("A", "GCG"),
    ("A", "GCT"),
    ("C", "TGC"),
    ("C", "TGT"),
    ("D", "GAC"),
    ("D", "GAT"),
    ("E", "GAA"),
    ("E", "GAG"),
    ("F", "TTC"),
    ("F", "TTT"),
    ("G", "GGA"),
    ("G", "GGC"),
    ("G", "GGG"),
    ("G", "GGT"),
    ("H", "CAC"),
    ("H", "CAT"),
    ("I", "ATA"),
    ("I", "ATC"),
    ("I", "ATT"),
    ("K", "AAA"),
    ("K", "AAG"),
    ("L", "CTA"),
    ("L", "CTC"),
    ("L", "CTG"),
    ("L", "CTT"),
    ("L", "TTA"),
    ("L", "TTG"),
    ("M", "ATG"),
    ("N", "AAC"),
    ("N", "AAT"),
    ("P", "CCA"),
    ("P", "CCC"),
    ("P", "CCG"),
    ("P", "CCT"),
    ("Q", "CAA"),
    ("Q", "CAG"),
    ("R", "AGA"),
    ("R", "AGG"),
    ("R", "CGA"),
    ("R", "CGC"),
    ("R", "CGG"),
    ("R", "CGT"),
    ("S", "AGC"),
    ("S", "AGT"),
    ("S", "TCA"),
    ("S", "TCC"),
    ("S", "TCG"),
    ("S", "TCT"),
    ("T", "ACA"),
    ("T", "ACC"),
    ("T", "ACG"),
    ("T", "ACT"),
    ("V", "GTA"),
    ("V", "GTC"),
    ("V", "GTG"),
    ("V", "GTT"),
    ("W", "TGG"),
    ("Y", "TAC"),
    ("Y", "TAT"),
]


def main() -> None:
    import re

    pat = re.compile(r"([ACGU]{3})\s+[\d.]+\(\s*(\d+)\)")
    counts: dict[str, int] = {}
    for m in pat.finditer(KAZUSA_BLOCK.replace("\n", " ")):
        counts[m.group(1).replace("U", "T")] = int(m.group(2))

    assert sum(counts.values()) == 6130423

    out = Path(__file__).resolve().parent / "aspergillus_niger_5061.csv"
    lines = ["amino_acid,codon,observed_count"]
    for aa, cod in ORDER:
        lines.append(f"{aa},{cod},{counts[cod]}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
