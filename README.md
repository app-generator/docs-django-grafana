# [Django & Grafana Integration](https://app-generator.dev/docs/technologies/django/integrate-grafana.html)

Coding sample for **Django & Grafana Integration** documentation page. The postproduction step in software development is crucial to tracking performances, correcting bugs, and improving an application. 
With Django, you can integrate Grafana, a powerful tool to aggregate logs and view these logs on the dashboard.

> 👉 [Free Support](https://app-generator.dev/ticket/create/) via `email` & `Discord` 

<br />

## Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/docs-django-snowflake.git
$ cd docs-django-snowflake
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

> 👉 Install Grafana

For Linux 👇

```bash
$ sudo systemctl start grafana-server
$ sudo systemctl enable grafana-server
```

For macOS (using Homebrew):

```bash
$ brew services start grafana
```

Open Grafana by going to http://localhost:3000 in your browser. Use the default username and password (admin/admin) to log in. Change the password when prompted.

<br />

---
**[Django & Grafana Integration](https://app-generator.dev/docs/technologies/django/integrate-grafana.html)** - Coding sample provided by **[App Generator](https://app-generator.dev/)**
