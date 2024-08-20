init:
	python3 -m venv .venv

install:
	pip install -r requirements.txt

lint:
	flake8 .

format:
	black .
