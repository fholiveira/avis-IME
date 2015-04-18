REQUIREMENTS_DEV=requirements-dev.txt
REQUIREMENTS=requirements.txt
PYTHON=python3.4
VENV=.web

ACTIVE_VENV=. $(VENV)/bin/activate

all: serve

serve: export AVISIME_ENV=DEV
serve: 
	@$(ACTIVE_VENV) && ./src/application.py

test: export AVISIME_ENV=TEST
test:
	@cd tests && $(MAKE)

configure: 
	@rm -rf $(VENV)
	@$(PYTHON) -m venv $(VENV)

	@$(ACTIVE_VENV) && pip install -r $(REQUIREMENTS_DEV)
	@$(ACTIVE_VENV) && pip install -r $(REQUIREMENTS)

deps:
	@$(ACTIVE_VENV) && pip freeze > $(REQUIREMENTS)
