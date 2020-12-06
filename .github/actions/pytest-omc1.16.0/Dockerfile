
FROM ijknabla/openmodelica-python3:omc1.16.0-py3.6-buster

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV USER user

ENTRYPOINT [ "/entrypoint.sh" ]
