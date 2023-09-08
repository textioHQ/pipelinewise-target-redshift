.PHONY: help clean clean-all clean-assets dev lint

codedir := . # location of code
testdir := ./*/tests
scriptdir := .

syspython := python3

pip := venv/bin/pip
aws := aws # awscli v2 should be installed via homebrew or pipx

code-files := $(shell find $(codedir) -name '*.py' -not \( -path '*__pycache__*' \))
test-files := $(shell find $(testdir) -name '*.py' -not \( -path '*__pycache__*' \))
python-script-files := $(shell find $(scriptdir) -name '*.py' -not \( -path '*__pycache__*' \))
gitish := $(shell git rev-parse --short HEAD)

clean: ## Clean build artifacts but NOT downloaded assets
	# Python build
	find $ . -name '__pycache__' -exec rm -Rf {} +
	find $ . -name '*.py[co]' -delete
	rm -rf dist
	rm -rf *.egg-info
	rm -rf *.egg
	rm -rf *.eggs
	rm -rf *.whl
	rm -rf *.tar.gz

	rm -rf venv
	rm -f .venv
	rm -f .dev
	rm -f .assets
	rm -f .lint

	# Test
	rm -rf .cache/
	rm -f .coverage
	rm -rf htmlcov/
	rm -f pytest-out.xml

clean-all: clean clean-assets ## Clean everything

venv:
	$(syspython) -m venv venv

.venv: venv
	venv/bin/pip install --progress-bar off --upgrade pip wheel setuptools pip-tools
	touch .venv

%.txt: %.in
	venv/bin/pip-compile \
		--no-emit-index-url \
		--no-emit-options \
		--resolver=backtracking \
		$^ \
		-o "$@"

## update all python requirements*.txt files based on the corresponding requirements*.in file
upgrade-dev-deps: .venv
	rm -f requirements_dev.txt
	$(MAKE) -sB requirements_dev.txt

.dev: .venv requirements_dev.txt
	$(pip) install --progress-bar off --upgrade -r requirements_dev.txt
	touch .dev

.assets: .dev
	touch .assets

clean-assets: ## Clean only assets so they will be re-downloaded
	rm -f .assets

.lint: .dev $(code-files) $(test-files)
ifeq ($(ci), true)
	venv/bin/black --line-length=101 --safe -v --check $(code-files) $(test-files) $(python-script-files)
else
	venv/bin/ruff -v check --fix $(code-files) $(test-files) $(python-script-files)
endif
	venv/bin/flake8 --max-line-length=101 $(code-files) $(test-files) $(python-script-files)
	touch .lint


dev: .dev ## Setup the local dev environment

lint: .lint ## Run flake8 and black linting
