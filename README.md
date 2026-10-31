# Metadata Inspector

Review exported text for metadata-like fields.

## Usage
```bash
python metadata_inspector.py sample.txt
python metadata_inspector.py sample.txt --output report.json
```

Python 3.10+; standard library only. Reads only a local UTF-8 text file. No network access, scraping, or source-file modification.

## Detection rules
- `author`: info heuristic
- `timestamp`: info heuristic
- `location`: review heuristic

Results are heuristic and require human validation. Use only public information or data you are authorized to review. Avoid committing personal or confidential data.

## Tests
`python -m unittest discover -s tests -v`
