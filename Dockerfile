FROM debian:stable-slim
COPY ola2.sh /ola.sh
CMD ["bash", "/ola.sh"]
