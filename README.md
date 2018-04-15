# SpiderBill
Crawl and gather bill information from: https://www.gpo.gov/fdsys/bulkdata

## Basic Usage:
```
docker run --rm -d -v `pwd`/out:/spider/out brycethomsen/scrapy
```

### Todos:
- multistage build
- unit tests