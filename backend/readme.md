# backend

## `api`

The `api` module serves as the Django app for the backend. Other modules describe their models and views, but this is the one that actually serves the API. Additionally, settings are configured out of this module.

## `companies`, `contacts`, `lead`

These are example models and views. Using `APIView` is necessary in order for [schema generation](https://www.django-rest-framework.org/api-guide/schemas/) to work.

## Schema generation

`make schema`