# FastAPI project

<h3> Getting Started</h3>
Build the app container: <code> docker build -t fastapi-app -f Dockerfile .</code><br>
Run the app container: <code>docker run -p 8000:8000 fastapi-app</code>

Build the test container: <code> docker build -t fastapi-test -f Dockerfile.test .</code><br>
Run the test container: <code>docker run --rm fastapi-test</code>
