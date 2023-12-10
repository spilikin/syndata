requirements:
	poetry export --without-hashes --format=requirements.txt --output requirements.txt

dockerhub: requirements
	docker build -t spilikin/syndata:latest .
	docker push spilikin/syndata:latest
