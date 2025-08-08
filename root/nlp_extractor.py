import spacy
from root.model import Node, Edge, MindMapResponse
from typing import Set

nlp = spacy.load("en_core_web_sm")

def extract_mind_map(text: str) -> MindMapResponse:
    doc = nlp(text)
    nodes = {}
    edges = []

    for chunk in doc.noun_chunks:
        nodes[chunk.root.text] = {"id": chunk.root.text, "label": chunk.text}

    for token in doc:
        if token.pos_ == "VERB" and token.dep_ != "aux":
            subj = [w.text for w in token.lefts if w.dep_ in ("nsubj", "nsubjpass")]
            obj = [w.text for w in token.rights if w.dep_ in ("dobj", "attr", "prep")]
            for s in subj:
                for o in obj:
                    edges.append(Edge(source=s, target=o, label=token.lemma_))
                    nodes[s] = {"id": s, "label": s}
                    nodes[o] = {"id": o, "label": o}

    return MindMapResponse(
        nodes=[Node(**v) for v in nodes.values()],
        edges=edges
    )
