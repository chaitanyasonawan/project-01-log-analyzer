FROM ubuntu:22.04


RUN apt-get update && apt-get install -y curl

COPY ./check.sh /check.sh
COPY ./urls.txt /urls.txt

RUN chmod +x /check.sh


CMD ["/check.sh"]
