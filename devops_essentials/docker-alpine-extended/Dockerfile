# Give alpine image
FROM alpine:latest

# Run install curl
RUN apk add --no-cache curl

# adding text using copy
COPY config.txt /app/config.txt

# keep container active
CMD ["sh"]
