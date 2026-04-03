# AGENTS.md

Guide for agentic coding assistants operating in this repository.

## Repository snapshot
- Language: Python 3.x.
- Entry point: `main.py` (console app).
- Main packages: `modelos/`, `servicios/`, `interfaces/`, `implementaciones/`.
- Current repository state: no `tests/`, no `requirements*.txt`, no `pyproject.toml` detected.
- Imports are package-relative from repo root (for example `from modelos...`).

## Cursor and Copilot rules
- Cursor rules checked in `.cursor/rules/`: none found.
- Cursor single-file rules checked in `.cursorrules`: none found.
- Copilot rules checked in `.github/copilot-instructions.md`: none found.
- If any of those files are added later, update this section and follow them as highest-priority repo conventions.

## Build, lint, and test commands

### Environment setup
1. Create virtual environment:
   - Windows: `python -m venv .venv && .venv\\Scripts\\activate`
   - Unix/macOS: `python -m venv .venv && source .venv/bin/activate`
2. Upgrade pip: `python -m pip install --upgrade pip`
3. Install runtime deps (if file exists): `python -m pip install -r requirements.txt`
4. Install dev deps (recommended, if file exists): `python -m pip install -r requirements-dev.txt`
5. If no requirement files exist, install baseline tools manually:
   - `python -m pip install pytest black isort flake8 mypy build`

### Run the application
- Start console app: `python main.py`

### Tests
- Run all tests: `pytest -q`
- Run with verbose output: `pytest -vv`
- Run by keyword: `pytest -k "orden" -q`

Preferred single-test patterns (use these whenever possible):
- Single test function:
  - `pytest tests/test_servicio_orden.py::test_confirma_orden_valida -q`
- Single test method in class:
  - `pytest tests/test_servicio_orden.py::TestServicioOrden::test_confirma_orden_valida -q`
- Single file only:
  - `pytest tests/test_servicio_orden.py -q`

Optional focused runs:
- Stop on first failure: `pytest -x -q`
- Show print/log output: `pytest -s -q`
- Coverage for this project shape:
  - `pytest --cov=modelos --cov=servicios --cov=implementaciones --cov=interfaces -q`

### Lint, format, and typing
- Format code: `black .`
- Check formatting only: `black --check .`
- Sort imports: `isort .`
- Check import order only: `isort --check-only .`
- Lint: `flake8 .`
- Type check: `mypy .`

### Build/package
- Build artifacts (if packaging is configured): `python -m build --sdist --wheel`
- Inspect build output:
  - Windows: `dir dist`
  - Unix/macOS: `ls dist`

### Suggested local pre-PR pipeline
1. `black .`
2. `isort .`
3. `flake8 .`
4. `mypy .`
5. `pytest -q`

## Code style guidelines

### General principles
- Prefer simple, explicit code over clever abstractions.
- Keep changes minimal, reversible, and localized.
- Preserve domain language in Spanish when extending existing modules/classes.

### Imports
- Use absolute imports from repo packages (`modelos`, `servicios`, `interfaces`, `implementaciones`).
- Group imports in this order: standard library, third-party, local packages.
- Separate import groups with one blank line.
- Avoid wildcard imports.
- Keep imports alphabetized within each group when practical.

### Formatting
- Use Black defaults for formatting.
- Keep one statement per line unless clarity clearly improves.
- Prefer trailing commas in multiline literals/calls to reduce diff noise.
- Keep functions short and cohesive; extract helpers rather than nesting deeply.

### Typing
- Add type hints for new/modified public functions and methods.
- Annotate return types explicitly.
- Prefer concrete types (`list[str]`, `dict[str, int]`) over `Any`.
- Use `Optional[T]`/`T | None` when `None` is a valid value.
- For interfaces/ABCs, annotate contract methods strictly.

### Naming conventions
- Variables/functions/methods: `snake_case`.
- Classes/enums: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- File names: lowercase with underscores.
- Use descriptive names aligned to domain concepts (`orden_compra`, `servicio_quejas`, etc.).

### Error handling
- Never use bare `except:`.
- Catch specific exceptions (`ValueError`, `TypeError`, etc.).
- Validate inputs at boundaries (service methods, constructors, interactive input adapters).
- Raise `ValueError` for business-rule violations, with actionable messages.
- Re-raise with context using `raise ... from exc` when wrapping exceptions.

### Logging and console output
- In library/domain modules, prefer `logging` over `print`.
- `print` is acceptable in `main.py` CLI flow.
- Do not log secrets or sensitive identifiers.

### Object-oriented and architecture guidance
- Keep `interfaces/` as abstract contracts only.
- Keep business rules in `modelos/` and orchestration in `servicios/`.
- Keep `implementaciones/` for external integrations/adapters.
- Avoid circular imports; depend on interfaces where possible.

### Docstrings and documentation
- Add module docstrings and concise docstrings for public classes/methods.
- Update docstrings when behavior changes.
- Prefer short, direct descriptions over verbose prose.

### Testing expectations
- Add tests for every bug fix and non-trivial feature.
- Test both happy path and rule/validation failures.
- Prefer deterministic tests with no network or real external services.
- Use fixtures/factories to reduce setup duplication.
- Keep tests readable: arrange, act, assert.

### Git and commit hygiene
- Do not commit generated artifacts (`dist/`, caches, virtual envs).
- Keep commits focused and explain why the change is needed.
- Avoid unrelated refactors in the same commit.

## Quick command cheat sheet
- Run app: `python main.py`
- Run all tests: `pytest -q`
- Run one test: `pytest tests/test_x.py::test_y -q`
- Format: `black . && isort .`
- Lint/type-check: `flake8 . && mypy .`
- Build: `python -m build --sdist --wheel`
