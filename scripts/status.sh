#!/bin/bash

if ss -ltn | grep -q ":5000 "; then
    echo "Blockchain application is RUNNING on port 5000."
else
    echo "Blockchain application is STOPPED."
fi
