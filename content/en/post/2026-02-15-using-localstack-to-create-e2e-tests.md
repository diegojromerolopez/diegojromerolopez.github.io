---
title: Using localstack to create end-to-end tests
date: "2026-02-01T00:00:00+02:00"
draft: true
tags: ["testing"]
---

# Using localstack to create end-to-end tests
[LocalStack](https://www.localstack.cloud/) is a project that provides mock containers for
the most popular AWS services (including S3, SNS, SQS, and DynamoDB). In this post I will show how to create
end to end tests.

## Introduction
I wanted to play around with LocalStack and needed to create a project to simulate a cloud infrastructure,
so I did: [Isidorus Web Scraper](https://github.com/diegojromerolopez/isidorus-web-scraper).

## LocalStack
LocalStack is a company that provides mock services for popular [AWS](https://aws.amazon.com/) services: DynamoDB,
SQS, SNS, etc. It is a perfect tool for running the end to end tests (E2E) in the pipeline.

Their product is open source and provide a [docker image](https://hub.docker.com/r/localstack/localstack)
with the services. As of February 2026, you can run the containers freely, but from
[March 23, 2026 you will require to use an auth token to run the containers](https://blog.localstack.cloud/the-road-ahead-for-localstack/) even if you rely on the free version. The rationale (I think) is that they are going
to merge their Open Source and proprietary docker images. Anyway, it is a minor inconvenience, that they could avoided,
but I suppose that maintaining a lone codebase is easier for the team. In our case,
the [4.13 docker image](https://hub.docker.com/layers/localstack/localstack/4.13/images/sha256-dd503b7df421dd7e7f8c44503c2f31a7c6060cbb5ab35f983fb141cfd4e18db4)
still does not need any kind of authentication, so we will use that.

## Isidorus Web Scraper
This project is a simple web scraper based on microservices.

The system is built with a microservices approach:

### Auth Admin:
- Implemented in Python + Django.
- Management of users and their access to the API by means of API keys.
- Uses the PostgreSQL

### API
- Implemented in Python + FastAPI + async libraries.
- Entry point for users.
- Enforces API Key authentication.
- Allows starting the scraper and getting the results.
- Uses:
  - SQS: message to workers
  - Redis: pending URL counter (to check if we have completed the scraping).
  - DynamoDB: scraping status (pending or completed), start URL, and depth.

### Scraper Worker
- Implemented in Golang
- Consumer of scrape requests from SQS.
- Fetches and parses HTML: Extracts terms, links, and images.
- Uses:
  - Redis: to avoid cycles and to track job completion via the pending URL counter.
- Sends new messages to the queue for discovered links.
- Sends new messages to the Image Extractor and Page Summarizer.

### Image Extractor Worker (Optional)
- Implemented in Python.
- Consumer of image URLs.
- Send image explanation to the writer worker.
- Uses:
  - S3 to store the images to an AWS S3 bucket.
  - LLM providers (OpenAI, Anthropic, Ollama): to explain the image contents. **Optional**.
  - SQS: sends the image queue to the writer worker.

### Page Summarizer Worker (Optional)
- Implemented in Python.
- Consumes text content from page-summarizer-queue.
- Send web page summary to the writer worker.
- Uses:
  - LLM providers (OpenAI, Anthropic, Ollama): concise summaries of web pages.
  - SQS: sends the page summary to the writer worker.

### Writer Worker (Go):
- Implemented in Golang.
- Uses:
  - SQS: consumes structured data (pages, terms, links, images, job completion events).
  - PostgreSQL: Writes scraping data to PostgreSQL.
  - DynamoDB: to update status.

### E2E tests

## Our scenario

## Our solution

## Conclusion
