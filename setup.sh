#!/usr/bin/env bash
# Script for setting up everything

rm -rf lib/!(README.md)
pip install -r requirements.txt -t lib/