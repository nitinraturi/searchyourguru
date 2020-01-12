# searchyourguru
Platform to connect tutors and students.

## Dependencies
- Python3
- Memcached
```
sudo apt-get install memcached
```

# Usage
- Create and activate your virtual environment
```
virtualenv -p python3 venv
source venv/bin/activate
```
- Now install **requirements.txt**
```
pip install -r requirements.txt
```
- Create a file **.env** where **manage.py** is located similar to **.env-sample** and set your environment variables later.
```
cp .env-sample .env
```
- Let's create required directories now, run
```
mkdir -p static/{css,js,img} static_cdn/{static_root,media_root} templates/{snippets,layouts} apps logs locale
```

> That's all.

