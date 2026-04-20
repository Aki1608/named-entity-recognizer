import spacy

class NEREngine:
    # Load the spaCy model
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Model not found. Please ensure en_core_web_sm is downloaded.")
        nlp = None

    @staticmethod
    def extract_entities(text):
        if NEREngine.nlp is None:
            return [("Model not loaded.", None)]
        
        # Process the text through the spaCy model
        doc = NEREngine.nlp(text)
        
        # Format the output specifically for Gradio's HighlightedText
        formatted_output = []
        for token in doc:
            # If the token has an entity type (like ORG, PERSON, DATE), attach it
            if token.ent_type_:
                formatted_output.append((token.text, token.ent_type_))
            # Otherwise, attach None so it displays as normal text
            else:
                formatted_output.append((token.text, None))
                
        # 4. Return the list back to the UI
        return formatted_output
