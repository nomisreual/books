FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api api
COPY apis apis
COPY app app
COPY data data
COPY main main
COPY migrations migrations

COPY app.py extensions.py ./
RUN echo '#!/bin/bash\nflask seeding 1000\nexec gunicorn -b :5000 "app:create_app()"' > boot.sh
RUN chmod a+x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
