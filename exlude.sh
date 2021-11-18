#!/usr/bin/env bash

string=$1
filter=$2
if [[ $string == *"$filter"* ]]; then
  echo "true"
fi