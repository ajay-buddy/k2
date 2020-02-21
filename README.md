# k2

docker build .
docker-compose build
docker-compose run --rm app sh -c "python manage.py test"
docker-compose up


docker exec -it knowledge_app_1 sh
--> python commands