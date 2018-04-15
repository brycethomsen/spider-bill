FROM python:3.6.5-alpine
WORKDIR /spider
ENV \
  RUNTIME_PACKAGES libxslt libxml2 git curl libpq
ENV \
  BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev python3-dev openssl-dev git curl
RUN apk update
RUN apk add ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip install scrapy scrapyd && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache
COPY scrapy.cfg /spider
COPY bills/ /spider/bills
EXPOSE 6800
CMD ["scrapy", "crawl", "gpo", "-o", "out/gpo_items.json"]
