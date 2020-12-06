
FROM ijknabla/openmodelica-python3:omc1.13.0-py3.6-stretch

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN apt-get update \
    && apt install sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "/entrypoint.sh" ]
