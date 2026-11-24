# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `rsconstruct.toml:21` - only shellcheck covers `python_and_rabbitmq/`; the two Python files are never linted. Add `[processor.ruff]` with `src_dirs = ["python_and_rabbitmq"]` (as `demos-lang-d` and `demos-bd-spark` do); `ruff check` currently reports 4 findings, listed below. If ruff runs from a repo venv, add a `pyproject.toml` with a dev group declaring `ruff` (plus `pika` as the demo's dependency).
- `python_and_rabbitmq/consumer.py:3` - `sys` and `os` are imported but unused (ruff F401), and the import line is unsorted (I001, also `python_and_rabbitmq/producer.py:3`); import only `pika`, one import per line.
- `python_and_rabbitmq/producer.py:18` - closes the channel but never the `BlockingConnection`; call `connection.close()` (which also closes the channel) so the AMQP connection is shut down cleanly.
- `python_and_rabbitmq/producer.py:10` - `sys.argv[1]` raises `IndexError` with a traceback when run without an argument; check `len(sys.argv) != 2` and print a usage line.

## Low

- `python_and_rabbitmq/consumer.py:16` - CTRL+C (which line 15 tells the user to press) ends in a `KeyboardInterrupt` traceback; wrap `start_consuming()` in `try/except KeyboardInterrupt` and close the connection.
- `python_and_rabbitmq/consumer.py:11` - tab-indented while `producer.py` uses spaces; use 4 spaces.
- `README.md:1` - the README is only a heading; it does not say how to run the demo (`start.sh`, then `consumer.py`, then `producer.py <message>`, then `stop.sh`) or point at `exercise.txt`.
- `python_and_rabbitmq/exercise.txt:5` - typo "Demostrate" -> "Demonstrate"; line 14 recommends `pip install --user`, which fails on PEP 668 distros, suggest a venv instead.
