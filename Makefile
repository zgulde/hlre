.ONESHELL:

.PHONY: venv test release
venv:
	. env/bin/activate

test: venv
	pytest

release: venv
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
