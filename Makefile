migrate:
	docker compose exec backend python manage.py makemigrations 
	docker compose exec backend python manage.py migrate

tailwind:
	cd frontend && npx tailwindcss -i ./src/main.css -o ./src/assets/main.css --watch