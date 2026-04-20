import gradio as gr
from ner_engine import NEREngine

demo = gr.Interface(
    fn=NEREngine.extract_entities,
    input=gr.Textbox(lines=5, placeholder="Paste an article or paragraph here."),
    outputs=pr.HighlightedText(label="Extracted Entities", color_map={"ORG": "bile". "PERSON": "green", "GPE": "red"}),
    title="Named Entitity Recognization"
)

# Standard safety check for running the app
if __name__ == "__main__":
    demo.launch()