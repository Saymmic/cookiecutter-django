black:
	poetry run black . --check --verbose --diff --color

flake8:
	poetry run flake8 .

isort:
	poetry run isort . --diff --check-only

mypy:
	poetry run mypy .

radon:
	poetry run radon cc . -nc -a
	poetry run radon mi . -nc

test:
	poetry run pytest . --create-db -vv
