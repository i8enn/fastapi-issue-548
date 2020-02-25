# FastAPI Issue 548
*This repository created for reproduce [FastAPI](https://github.com/tiangolo/fastapi) Swagger [bug](https://github.com/tiangolo/fastapi/issues/548)*

## Local run (required Docker)

Clone project

`git clone git@github.com:i8enn/fastapi-issue-548.git`

Build docker images and up app containers

`docker-compose up`

See browser:

http://localhost:8000 - Application **without** uvicorn reload (Swagger not working)

http://localhost:8001 - Application **with** uvicorn reload (Swagger normal working)

## Bug details

If application working **without** uvicorn `--reload` and using `Body(embed=True)`, OpenAPI raise `KeyError` exception ([view code](https://github.com/i8enn/fastapi-issue-548/blob/master/app/api/users/auth.py#L18)).

<details>
<summary>Traceback</summary>
```python
  File "/usr/local/lib/python3.7/site-packages/uvicorn/protocols/http/httptools_impl.py", line 385, in run_asgi
    result = await app(self.scope, self.receive, self.send)
  File "/usr/local/lib/python3.7/site-packages/fastapi/applications.py", line 140, in __call__
    await super().__call__(scope, receive, send)
  File "/usr/local/lib/python3.7/site-packages/starlette/applications.py", line 134, in __call__
    await self.error_middleware(scope, receive, send)
  File "/usr/local/lib/python3.7/site-packages/starlette/middleware/errors.py", line 178, in __call__
    raise exc from None
  File "/usr/local/lib/python3.7/site-packages/starlette/middleware/errors.py", line 156, in __call__
    await self.app(scope, receive, _send)
  File "/usr/local/lib/python3.7/site-packages/starlette/middleware/cors.py", line 76, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/lib/python3.7/site-packages/starlette/middleware/cors.py", line 76, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/lib/python3.7/site-packages/starlette/exceptions.py", line 73, in __call__
    raise exc from None
  File "/usr/local/lib/python3.7/site-packages/starlette/exceptions.py", line 62, in __call__
    await self.app(scope, receive, sender)
  File "/usr/local/lib/python3.7/site-packages/starlette/routing.py", line 590, in __call__
    await route(scope, receive, send)
  File "/usr/local/lib/python3.7/site-packages/starlette/routing.py", line 208, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/lib/python3.7/site-packages/starlette/routing.py", line 41, in app
    response = await func(request)
  File "/usr/local/lib/python3.7/site-packages/fastapi/applications.py", line 97, in openapi
    return JSONResponse(self.openapi())
  File "/usr/local/lib/python3.7/site-packages/fastapi/applications.py", line 89, in openapi
    openapi_prefix=self.openapi_prefix,
  File "/usr/local/lib/python3.7/site-packages/fastapi/openapi/utils.py", line 289, in get_openapi
    flat_models=flat_models, model_name_map=model_name_map
  File "/usr/local/lib/python3.7/site-packages/fastapi/utils.py", line 80, in get_model_definitions
    model_name = model_name_map[model]
KeyError: <class 'Body_password_reset_users_password_reset__reset_token__post'>
```
</details>

## Remove docker images

`docker-compose down --rmi all`
