# A Simple Content Manage System

![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![buildstatus](https://travis-ci.org/hjlarry/flask-vue-cms.svg?branch=master)](https://travis-ci.org/hjlarry/flask-vue-cms)
![pyversions](https://img.shields.io/badge/python%20-3.6%2B-blue.svg)
![vueversions](https://img.shields.io/badge/Vue-2.9.3-4fc08d.svg)
![flaskversions](https://img.shields.io/badge/flask-0.12.2-4fc08d.svg)
![License](https://img.shields.io/cocoapods/l/AFNetworking.svg)


# Preview
![效果图](Screenshots/1.png)
![效果图](Screenshots/2.png)
![效果图](Screenshots/3.png)
![效果图](Screenshots/4.png)
![效果图](Screenshots/5.png)


# How to use
* `python3 install pipenv`
* `pipenv install && pipenv shell`
*  modify `/flask_server/config.py` 
* `invoke db init`: run flask-migrate db init
* `invoke db migrate`: run flask-migrate db migrate
* `invoke db upgrade`: run flask-migrate db upgrade
* `invoke create-admin`: create an administrator with username and password both `admin`, you can add `--username=what --password=what` params
* `invoke rundev`: run develop environment both front-end and back-end
* `invoke test`: run unittests
* `invoke deploy`: you should edit `tasks.py` first, and then can deploy product environment
* `invoke freeze`: to freeze static files


# Instruction
* In Front-End, the dir `admin_with_vue` is based on [vue-element-admin](https://github.com/PanJiaChen/vue-element-admin), you can follow to develop. When you run `npm run build`, need to copy `/admin_with_vue/dist` to `/flask_server/static`
* In `config.py` , You can choose Redis to cache or not, and edit db connection
* When you run webserver, you also can see http://your host/apidocs/ to an Api doc, this is supported by [flasgger](https://github.com/rochacbruno/flasgger)