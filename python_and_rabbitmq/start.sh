#!/bin/bash -eu
docker run --detach --publish 15672:15672 --publish 5672:5672 --name my-rabbitmq rabbitmq
