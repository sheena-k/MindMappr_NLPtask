from pydantic import BaseModel
from typing import List

class Node(BaseModel):
    id: str
    label: str

class Edge(BaseModel):
    source: str
    target: str
    label: str

class MindMapResponse(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
