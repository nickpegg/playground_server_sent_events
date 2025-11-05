all: fmt lint

node_modules:
	npm install

fmt:
	uv run black .

lint:
	uv run mypy .

run: node_modules
	uv run python server.py
