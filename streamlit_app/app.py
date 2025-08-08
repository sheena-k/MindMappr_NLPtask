import streamlit as st
import requests
from streamlit_cytoscapejs import st_cytoscapejs

st.set_page_config(page_title="MindMapr", layout="wide")
st.title("MindMapr: Text to Mind Map")

api_url = "http://127.0.0.1:8000/mindmap"  

# Input from user
text = st.text_area("Enter your topic:")

if st.button("Generate Mind Map"):
    if text.strip():
        try:
            res = requests.post(api_url, json={"text": text})
            res.raise_for_status()
            data = res.json()

            cyto_elements = []

            # central node 
            central_id = "central"
            central_label = text.strip()
            cyto_elements.append({
                "data": {"id": central_id, "label": central_label}
            })

            #  other nodes
            for idx, node in enumerate(data.get("nodes", []), start=1):
                node_id = f"node_{idx}"
                node_label = node["label"]
                cyto_elements.append({
                    "data": {"id": node_id, "label": node_label}
                })

                # Edge from central node
                cyto_elements.append({
                    "data": {
                        "source": central_id,
                        "target": node_id,
                        "label": node.get("relation", "")
                    }
                })

            # Add original edges 
            for edge in data.get("edges", []):
                cyto_elements.append({
                    "data": {
                        "source": edge["source"],
                        "target": edge["target"],
                        "id": f'{edge["source"]}➞{edge["target"]}',
                        "label": edge.get("label", "")
                    }
                })

            # Style to show labels
            stylesheet = [
                {
                    "selector": "node",
                    "style": {
                        "content": "data(label)",
                        "text-valign": "center",
                        "color": "#000",
                        "background-color": "#89CFF0",
                        "font-size": "14px",
                        "text-outline-color": "#555",
                        "text-outline-width": 1
                    }
                },
                {
                    "selector": "edge",
                    "style": {
                        "label": "data(label)",
                        "curve-style": "bezier",
                        "target-arrow-shape": "triangle",
                        "arrow-scale": 1,
                        "font-size": "12px",
                        "color": "#555",
                        "text-background-color": "#fff",
                        "text-background-opacity": 1
                    }
                }
            ]

            st_cytoscapejs(
                cyto_elements,
                stylesheet=stylesheet,
                width='100%',
                height='800px',
                key="mindmap"
            )

        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
