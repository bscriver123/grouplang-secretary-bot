# Updated by aider provider

.PHONY: docs

docs:
	sphinx-apidoc -o docs/source .
	cd docs && make html
