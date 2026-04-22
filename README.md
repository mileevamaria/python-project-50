### Hexlet tests and linter status:
[![Actions Status](https://github.com/mileevamaria/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mileevamaria/python-project-50/actions)
[![Python package](https://github.com/mileevamaria/python-project-50/actions/workflows/python-package.yml/badge.svg)](https://github.com/mileevamaria/python-project-50/actions/workflows/python-package.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mileevamaria_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=mileevamaria_python-project-50)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mileevamaria_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mileevamaria_python-project-50)

# Вычислитель отличий
СLI-утилита, которая сравнивает два конфигурационных файла. ЭРезультат сравнения файлов может выводиться в разных форматах, например: stylish ("наглядный"), plain ("плоский") или json ("JSON-формат").
```shell
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options::
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## Установка
```shell
git clone git@github.com:mileevamaria/python-project-50.git
brew install uv
make build
make package-install
```

## Парсинг json
[![asciicast](https://asciinema.org/a/xpr29XHK1E2tPILF.svg)](https://asciinema.org/a/xpr29XHK1E2tPILF)

## Парсинг yaml/yml
[![asciicast](https://asciinema.org/a/TdzlSUPCr9KLLvHg.svg)](https://asciinema.org/a/TdzlSUPCr9KLLvHg)

## Форматирование stylish
[![asciicast](https://asciinema.org/a/MgEtLGu4UAHllhQi.svg)](https://asciinema.org/a/MgEtLGu4UAHllhQi)

## Форматировани plain
[![asciicast](https://asciinema.org/a/brkbetRi88X8KbB2.svg)](https://asciinema.org/a/brkbetRi88X8KbB2)

## Форматирование json
[![asciicast](https://asciinema.org/a/vjYu8y9zzokrsIij.svg)](https://asciinema.org/a/vjYu8y9zzokrsIij)
