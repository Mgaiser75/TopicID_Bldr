import gradio as gr
from backend.topicid_engine import run_engine

def run_all(q, mode):
    return run_engine(q, mode)

with gr.Blocks(theme="soft") as app:
    gr.Markdown("# 🔍 TopicID_Bldr — Full Engine 10.2.1")

    q = gr.Textbox(label="Enter Topic")
    mode = gr.Dropdown(["multi","youtube","reddit","google","amazon"], value="multi")
    btn = gr.Button("Run Engine")

    output = gr.JSON()

    btn.click(run_all, [q, mode], output)

app.launch()
