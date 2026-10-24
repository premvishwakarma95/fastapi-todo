from fastapi import FastAPI;

app = FastAPI();

@app.get("/")
def handshake():
    return 'app is working fine'