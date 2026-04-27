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
	uv run pytest --cov=gendiff --cov-report xml:coverage.xml
shell-rec:
	asciinema rec demo.cast
shell-upload:
	asciinema upload demo.cast

gendiff-plain:
	gendiff tests/test_data/cli/plain/file1.json tests/test_data/cli/plain/file2.json
gendiff-plain-yaml:
	gendiff tests/test_data/cli/plain/file1.yaml tests/test_data/cli/plain/file2.yaml
gendiff-nested:
	gendiff tests/test_data/cli/nested/file1.json tests/test_data/cli/nested/file2.json
gendiff-nested-yaml:
	gendiff tests/test_data/cli/nested/file1.yaml tests/test_data/cli/nested/file2.yaml