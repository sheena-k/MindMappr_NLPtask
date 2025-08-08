## MindMapr – Automatic Concept Mapper

**Problem Statement**


 To build an API that turns text into a JSON mind‑map and renders it in a browser 

**Goal**


 MindMapr extracts noun chunks and simple relations, returns a node‑edge JSON, and displays it with Cytoscape.js.

### System Architecture:  Root

**nlp extracor.py:**

    Processes user text and extracts concepts (noun chunks) and their relationships.

    Converts extracted data into a structured format suitable for visualization.
    
**model.py:**

    Schema enforcement, structured output, and strict validation across all components.
    
**main.py:**

    FastAPI app that takes text input, runs it through extract_mind_map, and returns a structured MindMapResponse.



### Framework and Tools:  

    Pydantic-ai for schema enforcement, output structuring and strict validation across components.
    
    Open-source Models Spacy for natural language understanding and and displays it with Cytoscape.js.
  
    Streamlit  Web application framework for the front-end interface.


### File structure    

Root --->>

    main.py
    
    model.py
    
    nlp_extractor.py
    
streamlit_app --->>

    app.py
    

