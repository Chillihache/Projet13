ARG DJANGO_SECRET_KEY
ARG DNS_SENTRY

FROM python:3.12

WORKDIR /app

COPY . .

ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV DNS_SENTRY=${DNS_SENTRY}

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

RUN unset DJANGO_SECRET_KEY DNS_SENTRY

ENV DATABASE_URL=sqlite:///oc-lettings-site.sqlite3

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
