run:
	feedpapers --interactive

ignore:
	feedpapers --interactive --ignore_all

# pytest test_foo.py
test:
	pytest -v --ignore=scratch --ignore=build_dashboard.py

dashboard:
	echo dashboard created
	python build_dashboard.py
	pandoc dashboard.md -o dashboard.html	

install:
	pip install --upgrade -e .

keywords:
	git pull && git add keywords.csv && git commit -m "stash keywords [skip ci]" && git push

log:
	git pull && git add log.csv && git commit -m "stash log [skip ci]" && git push