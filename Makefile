lint:
	uv run ruff check gendiff
install:
	uv sync
test:
	pytest
build:
	uv build
package-install:
	uv tool install --force dist/*.whl
gendiff:
	uv run gendiff
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml
