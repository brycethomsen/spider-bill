FROM python:alpine
MAINTAINER Bryce
WORKDIR /spider
ENV \
  RUNTIME_PACKAGES libxslt libxml2 git curl libpq
ENV \
  BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev python3-dev openssl-dev git curl
RUN apk update
RUN apk add ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip install scrapy ipython && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache
COPY bill/ /spider
CMD ["entrypoint.sh"]
