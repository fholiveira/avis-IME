REQUIREMENTS_DEV=requirements-dev.txt
REQUIREMENTS=requirements.txt
PYTHON=python3.4
VENV=.web

ACTIVE_VENV=. $(VENV)/bin/activate

all: serve

serve: export AVISIME_ENV=DEV
serve: 
	@$(ACTIVE_VENV) && ./src/application.py

notify: export AVISIME_ENV=DEV
notify: 
	@$(ACTIVE_VENV) && ./src/notify.py

test: export AVISIME_ENV=TEST
test:
	@cd tests && $(MAKE)

configure: 
	@rm -rf $(VENV)
	@$(PYTHON) -m venv $(VENV)

	@$(ACTIVE_VENV) && pip install -r $(REQUIREMENTS_DEV)
	@$(ACTIVE_VENV) && pip install -r $(REQUIREMENTS)

	@cat /dev/null > avis-ime.db
	@cat /dev/null > avis-ime-test.db

deps:
	@$(ACTIVE_VENV) && pip freeze > $(REQUIREMENTS)
