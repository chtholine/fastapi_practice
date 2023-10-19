# FastAPI project

### Getting Started
#### Run using Docker
* Run app 
  * Build the app container: <code> docker build -t fastapi-app -f Dockerfile .</code>
  * Run the app container: <code>docker run -p 8000:8000 fastapi-app</code>

* Run tests
  - Build the test container: <code> docker build -t fastapi-test -f Dockerfile.test .</code>
  - Run the test container: <code>docker run --rm fastapi-test</code>

#### Run using Make
* Run app | `make run-app`
* Run tests | `make run-test`
* Purge | `make purge`
* Available commands | `make help`
### Data Base
Access postgreSQL: `docker-compose exec postgres psql -U postgres -d postgres`</br>
Remove alembic version table `DROP TABLE alembic_version;`
>check tables with `\dt` and quit using `\q`
### Migrations
Create initial migration: `docker-compose exec app alembic revision --autogenerate -m "initial migration"`</br>
Create Subsequent Migrations: `docker-compose exec app alembic revision -m "description of migration"`</br>
Apply Subsequent Migrations: `docker-compose exec app alembic upgrade head`
