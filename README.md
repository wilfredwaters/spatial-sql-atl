# Spatial SQL ATL

Syntax examples for every DuckDB spatial function, worked through at the
[Spatial SQL ATL meetup](https://www.meetup.com/spatial-sql-atl/) in Atlanta.

One meetup every two weeks covers one topic's set of functions, through April 2027.

## Run the examples

Install [DuckDB](https://duckdb.org/docs/installation/) (examples tested on 1.4.3 and 1.5.6), then in any session:

```sql
INSTALL spatial;
LOAD spatial;
```

## Map output

Dekart draws only a geometry column named exactly `geometry` (lowercase). Every example and
challenge returns its geometry under that name.

Some functions return a 2D, 3D or 4D point, or a box, not a `GEOMETRY`. Those examples have a
`MAP` entry in `examples.py` that casts the output with `::GEOMETRY` so it can be drawn.

## License

MIT — see [LICENSE](LICENSE).
