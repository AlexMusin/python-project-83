install:
	poetry install

build:
	./build.sh

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

dev:
	poetry run flask --app page_analyzer:app run

lint:
	poetry run flake8 page_analyzer

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

test:
	poetry run pytest