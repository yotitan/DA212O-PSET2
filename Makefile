setup:
	python3 -m venv ~/.DA212O-PSET2
	source ~/.DA212O-PSET2/bin/activate
	
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	
# test:
# 	python3 -m pytest -vv -cov=hello_test.py
	
lint:
	pylint --disable R,C src/models/train_model.py
	
all:
	make test
	make lint