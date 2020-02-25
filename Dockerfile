### BASE IMAGE ###
FROM python:3.7-alpine

# # Install lxml dependencies
# RUN apk add --update --no-cache --virtual .build-deps \
#         g++ \
#         python-dev \
#         libxml2 \
#         libxml2-dev && \
#     apk add libxslt-dev && \
#     apk del .build-deps


RUN apk --no-cache add \
        bash \
        build-base \
        curl \
        gcc \
        git \
        libffi-dev \
        linux-headers \
        musl-dev \
        vim \
        tini

# ENVIRONMENTS
ENV APP_DIR=/home/appuser/app \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true

# Install python system requirements
RUN pip install --upgrade pip && pip install pipenv

# Copy requirements files
COPY ./Pipfile $APP_DIR/
COPY ./Pipfile.lock $APP_DIR/


# Change workdir to app
WORKDIR $APP_DIR

# Install requirements
RUN pipenv install --deploy --system --ignore-pipfile

# Copy package information
COPY ./setup.py $APP_DIR/

# Copy sources
COPY ./app $APP_DIR/app

RUN pip install -e .
