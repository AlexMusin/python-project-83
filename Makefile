install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

dev:
	poetry run flask --app page_analyzer:app run

lint:
	poetry run flake8 page_analyzer