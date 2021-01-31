FROM python:3.8-slim as server
ENV APPDIR /opt/app/
WORKDIR ${APPDIR}
COPY flask_app/ ${APPDIR}flask_app/
COPY Pipfile* ${APPDIR}
COPY config.yml ${APPDIR}
COPY entrypoint.sh ${APPDIR}
RUN pip install pipenv
RUN pipenv install --system --deploy
# for local test only
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]