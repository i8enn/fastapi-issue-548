"""Run with python module"""

if __name__ == '__main__':
    import uvicorn
    from .main import create_app
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
    create_app()
