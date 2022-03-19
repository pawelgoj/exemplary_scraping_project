# Exemplary scraping project

## Description

Program scraping the https://www.oryxspioenkop.com/. Collect data about destroyed military equipment of Russia and Ukraine.

## Tools

1. Python 3.9
2. Scrapy
3. sqlite3
4. click
5. pandas

## Use

Run following commands:

```
#create database 
python cli_client.py create_database --name name_your_database

#run scraping. Data are collected to database 
python cli_client.py scraping

#process data and get simplified data for a given day
python cli_client.py data_processing --date yyyy-mm-dd --file your_csv_file_with_processed_data

#If you want drop database
python cli_client.py drop_database

```