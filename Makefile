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
	gendiff data/plain/file1.json data/plain/file2.json
gendiff-plain-yaml:
	gendiff data/plain/file1.yaml data/plain/file2.yaml
gendiff-nested:
	gendiff data/nested/file1.json data/nested/file2.json
gendiff-nested-yaml:
	gendiff data/nested/file1.yaml data/nested/file2.yaml