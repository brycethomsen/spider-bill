# SpiderBill
Crawl and gather bill information from: https://www.gpo.gov/fdsys/bulkdata

## Basic Usage:
```
docker run --rm -d -v `pwd`/out:/spider/out brycethomsen/spider-bill:development
```

### Todos:
- multistage build
- unit tests