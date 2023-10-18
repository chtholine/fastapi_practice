# FastAPI project

<h3> Getting Started</h3>
Build the app container: <code> docker build -t fastapi-app -f Dockerfile .</code><br>
Run the app container: <code>docker run -p 8000:8000 fastapi-app</code>

Build the test container: <code> docker build -t fastapi-test -f Dockerfile.test .</code><br>
Run the test container: <code>docker run --rm fastapi-test</code></br>
### Data Base
Access postgreSQL: `docker-compose exec postgres psql -U postgres -d postgres`</br>
Remove alembic version table `DROP TABLE alembic_version;`
>check tables with `\dt` and quit using `\q`
### Migrations
Create initial migration: `docker-compose exec app alembic revision --autogenerate -m "initial migration"`</br>
Create Subsequent Migrations: `docker-compose exec app alembic revision -m "description of migration"`</br>
Apply Subsequent Migrations: `docker-compose exec app alembic upgrade head`


