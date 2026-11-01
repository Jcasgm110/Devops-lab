FROM debian:stable-slim
COPY ola.sh /ola.sh
CMD ["bash", "/ola.sh"]
