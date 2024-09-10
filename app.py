from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from generate import generate_paraphrases  # Import the function to generate paraphrases

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve the homepage (index.html)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint for generating paraphrases
@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, input_text: str = Form(...), num_paraphrases: int = Form(...)):
    # Call the generate_paraphrases function from generate.py
    generated_responses = generate_paraphrases(input_text, num_paraphrases)
    
    # Return the page with the generated paraphrase response
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "input_text": input_text, 
        "num_paraphrases": num_paraphrases,
        "generated_responses": generated_responses
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# 