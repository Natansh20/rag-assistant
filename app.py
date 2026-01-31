import gradio as gr
from rag import ask

def chat_with_rag(question):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)
    answer = result["answer"]
    sources = ", ".join(result["sources"])

    return answer, sources


with gr.Blocks(title="RAG Assistant") as demo:
    gr.Markdown("# 📄 RAG-based PDF Assistant")
    gr.Markdown("Ask questions based on uploaded documents.")

    with gr.Row():
        question = gr.Textbox(
            label="Your Question",
            placeholder="Ask something from the documents...",
            lines=2
        )

    with gr.Row():
        answer = gr.Markdown(label="Answer")   # ✅ Markdown renderer
        sources = gr.Textbox(label="Sources")

    ask_btn = gr.Button("Ask")

    ask_btn.click(
        fn=chat_with_rag,
        inputs=question,
        outputs=[answer, sources]
    )

demo.launch()
