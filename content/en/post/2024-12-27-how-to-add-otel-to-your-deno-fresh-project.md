---
title: How to add OTEL to your deno fresh project
date: "2024-12-27T00:00:00+02:00"
draft: true
tags: ["deno", "fresh", "otel"]
---

# How to add OTEL to your deno fresh project
[OpenTelemetry](https://opentelemetry.io/) is a standard for adding telemetry to your application.
There are a myriad of implementations for almost all the programming languages.
But you need to be aware that the particularities of each language can make integrating
with OTEL very different in one case or other.

## Introduction
This post assumes you know what
[observability](https://opentelemetry.io/docs/concepts/observability-primer/#what-is-observability)
is, the best practices and the bare minimum that is
accepted nowadays in modern applications. We would also suppose that you know what OpenTelemetry is,
how it works and the best practices when adding OTEL to an application.
We will not delve in explanations about those concepts, we will only show some examples
about how to add OTEL to a [deno fresh](https://fresh.deno.dev/) application.

So if you have a grasp of what OTEL is, and maybe you have worked with it in the past in
other programming language, *you are golden*. Otherwise, better to start from
[the basics](https://opentelemetry.io/docs/what-is-opentelemetry/).

This post is a inspired on
[Leveraging OpenTelemetry in Deno](https://dev.to/grunet/leveraging-opentelemetry-in-deno-45bj)
by [Grunet](https://dev.to/grunet).

## Configure your OTEL environment variables
You need to set where the telemetry data will be sent, and the name where it would be
grouped (application or service name):

```shell
# Environment variables needed for OTEL
OTEL_EXPORTER_OTLP_ENDPOINT="https://your.otel.collector.server.example.com"
OTEL_SERVICE_NAME="your-project"
```

## Configure OTEL for deno fresh
Let me tell you a secret, I do not like using the deno HTTP imports.
You could end up with a mess of versions in your software project. I like having
seamless and crystal-clear things.
That is why I use [import maps](https://deno.land/x/manual@v1.12.2/npm_nodejs/import_maps.md)
always:

```typescript
// deno.json

{
    "imports": {
        "otel/api": "npm:@opentelemetry/api@1.9.0"
        "otel/exporter": "npm:@opentelemetry/exporter-trace-otlp-proto@0.52.1"
        "otel/instrumentation": "npm:@opentelemetry/instrumentation@0.52.1"
        "otel/resources": "npm:@opentelemetry/resources@1.25.1",
        "otel/sdk-trace-base": "npm:@opentelemetry/sdk-trace-base@1.25.1",
        "otel/sdk-trace-node": "npm:@opentelemetry/sdk-trace-node@1.25.1",
        "otel/semantic-conventions": "npm:@opentelemetry/semantic-conventions@1.25.1",
    }
}
```

## Configure what span exporters you need

This could be included with the OTEL tracer, but I tend to like to separate
the configuration from the start of the OTEL engine. So this method allow us to
configure all the different ways of sending information to a collector.

```typescript
// lib/otel/OtelTracing.ts

import { NodeTracerProvider } from "otel/sdk-trace-node";
import {
    SEMREATTRS_SERVICE_NAME,
    SEMREATTRS_SERVICE_VERSION,
} from "otel/semantic-conventions"
import { BatchSpanProcessor } from "otel/sdk-trace-base";
import { OTLPTraceExporter } from "otel/exporter";

class OtelTracing {
  constructor(name: string, version: string){
    this.name = name;
    this.version = version;
  }

  register(){
    const resource = Resource.default().merge({
      new Resource({
        [SEMREATTRS_SERVICE_NAME]: name,
        [SEMREATTRS_SERVICE_VERSION]: version,
      })
    });

    const tracerProvider = NodeTracerProvider({ resource });

    const traceExporter = new OTLPTraceExporter();

    // You can also add other span processors like ConsoleSpanExporter or InMemorySpanExporter
    tracerProvider.addSpanProcessor(new BatchProcessor(traceExporter))

    tracerProvider.register();

    // In case you want to call directly to the tracer provider methods (e.g. shutdown)
    return tracerProvider;
  }
}
```

## Get the OTEL tracer
The OTEL tracer will be the entrypoint of the telemetry in our routes, and will allow
us to decorate them with the OTEL utilities:

```typescript
// lib/otel/otel.ts
import opentelemetry from "otel/api";
import opentelemetry from "lib/otel/OtelTracing.ts";

OtelTracing("my-project", "1.0").register();

export const OTEL_TRACER = opentelemetry.trace.getTracer('my-tracer')
```

## Add telemetry to your routes

Adding telemetry to your routes is a bit cumbersome. You will need to decorate
the specific handler in the route with an OTEL span, and that is done by wrapping
all the functionality in the second parameter of a function.

The methods `setAttribute` and `setAttributes` from the Span object should be used
when we need to add information to the span.

The method `setStatus` from the Span class is useful for marking a piece of code as erroneous.

Hence the code:

```typescript
// routes/api/tasks.ts
import { Handlers } from "$fresh/server.ts";
import { OTEL_TRACER } from "lib/otel/otel.ts";
import { Span, SpanStatusCode } from "otel/api";

// other imports like the Task model, not relevant to this example

export const handler: Handlers<null, StateContext> = {
  async GET(req, ctx) {
    return await OTEL_TRACER.startActiveSpan("/routes/api/tasks.ts",
      async (span: Span) => {
        try {
          span.setAttributes({requestId: ctx.state.requestId});
            
          // Access to the list of tasks (dummy code)
          tasks = Task.loadAll();

          span.setAttributes({"tasks.count": tasks.length});
            
          return Response.json({status: "ok", tasks})
        }catch(exception){
          if(exception instanceof Error){
            span.setStatus({ code: SpanStatusCode.ERROR, message: exception.message });
          }else {
            span.setStatus({ code: SpanStatusCode.ERROR });    
          }
        } finally {
          span.end();
        }
      }
    )
  }
};
```

It looks counter-intuitive, but once you repeat this patter in your routes, you only need
to be careful with the braces at the end :)

Of course, this could be avoided if there was something like the Python's context manager
in TypeScript, but there is no such thing. So we need to wrap the code manually with a
higher-order function.

## Conclusion
We have shown a simple example on how to configure a OpenTelemetry with typescript.
From the span processor to the tracer, adding spans to the routes and adding attributes
to the spans.
