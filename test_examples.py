"""Run every DuckDB spatial example and report which fail.

Usage (same folder as examples.py):
    pip3 install -U duckdb
    python3 test_examples.py
"""

import duckdb

from examples import EX

FILE_BASED = {"ST_Read", "ST_ReadOSM", "ST_ReadSHP", "ST_Read_Meta"}
# Fail on DuckDB 1.4.1: no WKB input form is accepted by these 2D functions.
KNOWN_BROKEN = {
    "ST_LineString2DFromWKB": "no WKB input accepted in DuckDB 1.4.1",
    "ST_Point2DFromWKB": "no WKB input accepted in DuckDB 1.4.1",
    "ST_Polygon2DFromWKB": "no WKB input accepted in DuckDB 1.4.1",
}
EXPECTED_COUNT = 158


def main():
    con = duckdb.connect()
    con.sql("INSTALL spatial; LOAD spatial;")
    print(f"DuckDB {duckdb.__version__}")
    print(f"Examples: {len(EX)} (expected {EXPECTED_COUNT})\n")

    passed, failed, skipped, known = [], [], [], []
    for name, sql in EX.items():
        if name in FILE_BASED:
            skipped.append(name)
            continue
        if name in KNOWN_BROKEN:
            known.append(name)
            continue
        try:
            con.sql(sql).fetchall()
            passed.append(name)
        except duckdb.Error as err:
            failed.append((name, str(err).splitlines()[0]))

    print(f"PASS {len(passed)}")
    print(f"SKIP {len(skipped)} (need a data file: {', '.join(sorted(skipped))})")
    print(f"KNOWN BROKEN {len(known)} ({', '.join(sorted(known))})")
    print(f"FAIL {len(failed)}")
    for name, msg in failed:
        print(f"  {name}: {msg}")


if __name__ == "__main__":
    main()
