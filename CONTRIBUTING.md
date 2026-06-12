# Contributing to Brihaspati

We welcome contributions! This document outlines the process.

## Getting Started

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://code.swecha.org/your-username/brihaspati.git
   cd brihaspati
   ```
3. Set up the development environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   pip install -r backend/requirements-dev.txt
   ```
4. Install pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Development Workflow

1. Create a feature branch: `git checkout -b feat/your-feature`
2. Make your changes with clear, descriptive commits.
3. Run tests: `pytest tests/`
4. Run linters: `ruff check backend/`
5. Push and open a Merge Request.

## Code Standards

- Follow PEP 8 style (enforced by Ruff).
- Type hints required for all function signatures.
- Write tests for new functionality.
- Keep functions focused and single-purpose.
- Use descriptive variable names (Telugu context terms welcome).

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `refactor:` code restructuring
- `test:` adding tests
- `chore:` maintenance

## Merge Request Process

1. Ensure CI passes (lint, typecheck, tests).
2. Update documentation if APIs change.
3. Request review from maintainers.
4. Squash commits before merging.

## Code of Conduct

All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

Open an issue or contact maintainers at maintainers@swecha.org.
