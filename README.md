# IdentifierPy

Sample program to teach software testing concepts.

## Pre-requirements

Create virtual environment

```bash
pyenv virtualenv mlp-esbd
```

```bash
pyenv activate mlp-esbd
```

```bash
cd IdentifierPy
```

```bash
pip install -r requirements.txt
```

```bash
pip install -e .
```

## Running `IdentifierMain.py`

```bash
python src/IdentifierMain.py abc
```

## Running `test_validate.py`

```bash
python -m pytest -v tests/src/test_validate.py
```

```bash
pytest -v tests/src/test_validate.py
```

## Creating a distribution package

```bash
pyinstaller --onefile src/IdentifierMain.py
```

## Measuring Coverage

```bash
coverage run --source=Identifier -m pytest tests
coverage report
coverage html -d coverage
coverage run --source=Identifier --branch -m pytest tests
```

## Coverage in GitHub Actions

```yaml
      # Run pytest with coverage (fail if coverage < 80%). Include "--cov-branch \" below to use branch coverage
      - name: Run tests with coverage  
        run: |
          pytest --cov=./ \
                --cov-report=xml \
                --cov-fail-under=60 \
                test_pipeline.py

      - name: Upload to Codecov
        if: success()  # Only run if previous steps succeed
        uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.CODECOV_TOKEN }}  # Uses the secret
          file: ./coverage.xml  # Explicit path to coverage file
          flags: github-actions  # Optional: tag this upload
          override_commit: ${{ github.event.pull_request.head.sha }}
          override_branch: ${{ github.event.pull_request.head.ref }}
```

# Run Mutation Tool

Berofe run this tool, make sure to install `requirements.txt` dependencies.

```bash
mut.py -t src/Identifier.py -u tests/test_validate.py --runner pytest --report-html mutpy
```