FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y python3-dev libffi-dev

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash admin@gmail.com && chmod 777 /opt /run

WORKDIR /Blog

RUN mkdir /Blog/static && mkdir /Blog/media && chown -R admin@gmail.com /Blog/ && chmod 755 /Blog

COPY --chown=admin@gmail.com:admin@gmail.com . .

RUN pip install -r requirements.txt

USER admin@gmail.com

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]