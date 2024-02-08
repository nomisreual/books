FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY apis apis
COPY app app
COPY data data
COPY main main
COPY migrations migrations

COPY app.py /
COPY extensions.py /
RUN echo '#!/bin/bash' > /boot.sh \
    && echo 'while true; do' >> boot.sh \
    && echo '    flask seeding 10000' >> boot.sh \
    && echo '    if [[ "$?" == "0" ]]; then' >> boot.sh \
    && echo '        break' >> /boot.sh \
    && echo '    fi' >> /boot.sh \
    && echo '    echo Upgrade command failed, retrying in 5 secs...' >> /boot.sh \
    && echo '    sleep 5' >> /boot.sh \
    && echo 'done' >> /boot.sh \
    && echo 'exec gunicorn -b :5000 --access-logfile - --error-logfile - "app:create_app()"' >> /boot.sh
RUN chmod a+x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
