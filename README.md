# turangga
Get data "inspiriasi nama bayi berdasarkan nama hewan" with scrapy and pandas


### First after clone the project

Make a virtual environment (depending your operating system)
```python
python3 -m virtualenv venv
source ./venv/bin/activate      # Linux
source .\venv\Scripts\activate  # Windows
```

Install scrapy library after get in new environment
```python
pip install scrapy
```

Crawl the spider (in this project is nama)
```python
scrapy crawl nama
```

To export to json file using -o option
```python
scrapy crawl nama -o json
```

Happy Coding!
