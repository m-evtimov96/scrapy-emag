# scrapy-emag
Simple scrapy project

## Instalation
You will need python (3.10>) and scrapy(2.6.1>).
You can find all the packages in requirements.txt

## Usage
To use the spiders you can type the following command in the terminal:
scrapy crawl _spider_name_

For example: scrapy crawl gpu_spider

To save the output to a file add _-o filetype_ after the _spider_name_

Like this: scrapy crawl gpu_spider -o gpus.csv
