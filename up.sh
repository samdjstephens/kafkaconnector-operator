#!/usr/bin/env bash
helm upgrade kafkalocal --install -f local/cp-values.yml confluentinc/cp-helm-charts
kubectl --context docker-for-desktop expose deployment kafkalocal-cp-kafka-connect --type=LoadBalancer --port=8083 --name=kafkaconnectlb