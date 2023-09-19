FROM python:3.11.4

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./app app
COPY --chown=${USER} ./tests tests

USER ${USER}

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload & pytest ./tests/test_main.py ; tail -f /dev/null"]