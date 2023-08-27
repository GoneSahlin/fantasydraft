VENV = .venv
MODULE = fantasydraft

$(VENV): setup.cfg
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -e .[dev]
	touch $(VENV)

.PHONY: run
run: $(VENV)
	$(VENV)/bin/python3 $(MODULE)/main.py

.PHONY: collect
collect: $(VENV)
	$(VENV)/bin/python3 scripts/collect_data.py

.PHONY: test
test: $(VENV)
	$(VENV)/bin/pytest $(MODULE)

.PHONY: lint
lint: $(VENV)
	-$(VENV)/bin/flake8 --exclude $(VENV)

.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf *.eggs
	rm -rf *.egg
	rm -rf *.egg-info