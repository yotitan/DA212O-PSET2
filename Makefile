setup:
	python3 -m venv ~/.MLOps-Dagshub-Demo
	source ~/.MLOps-Dagshub-Demo/bin/activate
	
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	
# test:
# 	python3 -m pytest -vv -cov=hello_test.py
	
lint:
	pylint --disable R,C src/models/train_model.py &&\
	pylint --disable R,C src/models/predict_model.py
	
all:
	make test
	make lint