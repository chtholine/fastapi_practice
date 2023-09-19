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

COPY --chown=${USER} --chmod=755 ./docker/entrypoint.sh /entrypoint.sh

USER ${USER}

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]