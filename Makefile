compose-bash:
	docker compose up -d
	docker compose exec crm-inventory /bin/bash