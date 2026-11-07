# syntax=docker/dockerfile:1
FROM python:3.12-alpine AS build
ARG NEXT_PUBLIC_API_URL
ARG NEXT_PUBLIC_LABEL=initial
WORKDIR /build
RUN test -n "$NEXT_PUBLIC_API_URL" && printf '%s' "$NEXT_PUBLIC_API_URL" > api-url && printf '%s' "$NEXT_PUBLIC_LABEL" > label
RUN --mount=type=secret,id=BUILD_TOKEN,required=true test -s /run/secrets/BUILD_TOKEN
FROM python:3.12-alpine
WORKDIR /app
COPY --from=build /build/api-url /app/api-url
COPY --from=build /build/label /app/label
COPY server.py /app/server.py
EXPOSE 3000
CMD ["python", "server.py"]
