OS := $(shell uname 2>/dev/null || echo Windows)
ifeq ($(OS), Windows)
    SET_ENV = set PYTHONDONTWRITEBYTECODE=1 &&
else
    SET_ENV = PYTHONDONTWRITEBYTECODE=1
endif

dev:
	$(SET_ENV) python -m robyn app/main.py --dev

init db:
	python migrations/bootstrap.py

start:
	python -m robyn app/main.py --fast
