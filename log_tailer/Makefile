all: fmt lint

fmt:
	poetry run black .

lint:
	poetry run pycodestyle .
	poetry run mypy .

run:
	poetry run python server.py
