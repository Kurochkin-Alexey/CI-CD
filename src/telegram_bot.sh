#!/bin/bash 

# Получаем значения переменных из Python-скрипта
config=$(python3 config.py)

# Разбиваем строку на переменные
BOT_TOKEN=$(echo $config | cut -d' ' -f1)
USER_ID=$(echo $config | cut -d' ' -f2)

API_URL="https://api.telegram.org/bot${BOT_TOKEN}/sendMessage"

if [ "$CI_JOB_STATUS" == "success" ]; then
  MESSAGE="Stage $CI_JOB_STAGE OK"
else
  MESSAGE="Stage $CI_JOB_STAGE FAIL"
fi

curl -s -X POST ${API_URL} -d chat_id=${USER_ID} -d text="${MESSAGE}" -d parse_mode="html"