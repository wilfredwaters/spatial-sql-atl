"""Run every DuckDB spatial example and report which fail.

Usage (same folder as examples.py):
    pip3 install -U duckdb
    python3 test_examples.py
"""

import duckdb

from examples import EX

FILE_BASED = {"ST_Read", "ST_ReadOSM", "ST_ReadSHP", "ST_Read_Meta"}
EXPECTED_COUNT = 158


def main():
    con = duckdb.connect()
    con.sql("INSTALL spatial; LOAD spatial;")
    print(f"DuckDB {duckdb.__version__}")
    print(f"Examples: {len(EX)} (expected {EXPECTED_COUNT})\n")

    passed, failed, skipped = [], [], []
    for name, sql in EX.items():
        if name in FILE_BASED:
            skipped.append(name)
            continue
        try:
            con.sql(sql).fetchall()
            passed.append(name)
        except duckdb.Error as err:
            failed.append((name, str(err).splitlines()[0]))

    print(f"PASS {len(passed)}")
    print(f"SKIP {len(skipped)} (need a data file: {', '.join(sorted(skipped))})")
    print(f"FAIL {len(failed)}")
    for name, msg in failed:
        print(f"  {name}: {msg}")


if __name__ == "__main__":
    main()
