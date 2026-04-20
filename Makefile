lint:
	uv run ruff check gendiff
install:
	uv sync
build:
	uv build
package-install:
	uv tool install --force dist/*.whl
gendiff:
	uv run gendiff
