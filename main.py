from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/pira")
def test():
    return [{"empresa":"PIRACICABANA","cartao":"3587921","tipo":"FUNCIONARIO"},{"empresa":"BR MOBILIDADE","cartao":"290963","tipo":"PASSE LIVRE"},{"empresa":"BR MOBILIDADE","cartao":"8566978","tipo":"COMUM"}]

@app.get("/br")
def test2():
    return {"cpf": "48227829805","cpf-valid": "true", "cartoes" : [{"empresa":"PIRACICABANA","cartao":"3587921","tipo":"FUNCIONARIO"},{"empresa":"BR MOBILIDADE","cartao":"290963","tipo":"PASSE LIVRE"},{"empresa":"BR MOBILIDADE","cartao":"8566978","tipo":"COMUM"}]}
    # return {{"empresa":"PIRACICABANA","cartao":"3587921","tipo":"FUNCIONARIO"},{"empresa":"BR MOBILIDADE","cartao":"290963","tipo":"PASSE LIVRE"},{"empresa":"BR MOBILIDADE","cartao":"8566978","tipo":"COMUM"}}
