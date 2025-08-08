from fastapi import FastAPI
from pydantic import BaseModel
from root.nlp_extractor import extract_mind_map
from root.model import MindMapResponse

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/mindmap", response_model=MindMapResponse)
def mindmap_endpoint(input: InputText):
    return extract_mind_map(input.text)
