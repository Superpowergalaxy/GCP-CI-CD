  install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

deploy:
	gcloud app deploy 

lint:
	pylint --disable=R,C main.py

all: install lint deploy
