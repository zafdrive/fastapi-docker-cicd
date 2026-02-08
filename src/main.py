from fastapi import FastAPI
app = FastAPI(title="FastAPI Docker CI/CD")

@app.get("/")
def read_root():
    return {"message": "🚀 FastAPI + Docker + GitHub Actions + Trivy listo!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
