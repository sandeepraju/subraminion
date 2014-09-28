.PHONY: all clean build install uninstall test reinstall

all: clean

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	find . -name \*~ -delete
	rm -rf dist Subraminion.egg-info

build:
	python setup.py sdist

install:
	pip install dist/Subraminion-*.tar.gz

uninstall:
	yes | pip uninstall subraminion

reinstall:
	make uninstall && make clean && make build && make install
