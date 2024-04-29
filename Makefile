prod-compose-bash:
	docker compose up -d && \
	docker compose exec crm-inventory /bin/bash && \
	docker compose down

flake8:
	flake8

test-compose-bash:
	docker compose -f tests/docker-compose.yml up -d && \
	docker compose -f tests/docker-compose.yml exec crm-inventory /bin/bash && \
	docker compose -f tests/docker-compose.yml down