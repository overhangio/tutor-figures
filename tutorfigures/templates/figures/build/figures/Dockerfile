#--------- Base image with cloned repo
FROM python:3.7-bullseye as base

RUN apt update \
    && apt install -y git \
    && rm -rf /var/lib/apt/lists/*

# Clone repo
ARG FIGURES_REPOSITORY=https://github.com/Dicey-Tech/figures.git
ARG FIGURES_VERSION={{ FIGURES_RELEASE_VERSION }}
RUN git clone $FIGURES_REPOSITORY --branch $FIGURES_VERSION --depth 1 /figures

#--------- Front-end builder image
FROM node:14 as frontend-builder

COPY --from=base /figures/frontend /app/figures/frontend
WORKDIR /app/figures/frontend
RUN yarn && \
    yarn build

#--------- devsite image
FROM python:3.7-bullseye as devsite

RUN apt update \
    && apt install -y gettext git default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# User creation
RUN useradd --home-dir /app --create-home --uid=1000 openedx
USER openedx

COPY --from=base --chown=openedx:openedx /figures /app/figures

# Collect static assets
COPY --from=frontend-builder --chown=openedx:openedx \
    /app/figures/figures/static/figures \
    /app/figures/figures/static/figures

WORKDIR /app/figures/devsite

# Install project (with requirements)
RUN python -m venv /app/venv
ENV PATH /app/venv/bin:${PATH}
RUN pip install pip==21.3.1 setuptools==60.0.1 wheel==0.37.0

RUN pip install -r requirements/community.txt

EXPOSE 8000
