# searchyourguru

Platform to connect tutors and students.

## Dependencies

- Python3
- Memcached

```
sudo apt-get install memcached
```

- Install node and npm
  [Installation Link](https://raturi.in/blog/nodejs-and-npm-proper-installation-and-uninstallation-ubuntu/) - Skip Uninstallation part fron starting of the article

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

- Now run migrations

```
python manage.py makemigrations
```

- Let's setup frontend

```
cd frontend/searchyourguru
```

- Install dependencies for node

```
npm install
```

- run development server

```
npm run serve
```

# Server Advice

- Run django server on port 8005 because its configuration is done in that way.

> That's all.
