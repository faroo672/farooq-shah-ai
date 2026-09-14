
import gradio as gr
import spaces

@spaces.GPU
def ai_chat_response(message, history):
    if not message:
        return "Hello! Welcome to Farooq Shah AI Classroom. How can I help you today?"
    
    msg = message.lower()
    if "hello" in msg or "hi" in msg or "سلام" in msg:
        return "Hello! Welcome to Farooq Shah AI. Let's start learning step-by-step. What would you like to study today?"
    else:
        return f"I received your message: '{message}'. Let's practice this step-by-step. Tell me if you have any questions!"

def get_islamic_boards_info():
    return """
    # 🕌 Islamic Information & Wafaq-ul-Madaris Boards
    * **1. Wafaq-ul-Madaris Al-Arabia Pakistan**
    * **2. Tanzeem-ul-Madaris Ahl-e-Sunnat**
    * **3. Wafaq-ul-Madaris Salafia**
    * **4. Wafaq-ul-Madaris Shia Pakistan**
    """

def get_computer_courses():
    return """
    # 💻 Computer Courses
    * Microsoft Office (MS Word & Excel)
    * Basic Computer & Windows Settings
    * Web Development (HTML, CSS, Python)
    """

def get_mobile_editing_courses():
    return """
    # 📱 Mobile Editing & Photoshop
    * Canva Mobile Editing
    * Adobe Photoshop (Retouching & Layers)
    * Adobe Illustrator (Vector Graphics)
    """

def get_language_courses():
    return """
    # 🌐 100+ Languages Learning Hub
    * Step-by-step daily classes, grammar correction, and vocabulary building.
    """

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    
    gr.Markdown("""
    <div style='text-align: center; background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); padding: 20px; border-radius: 10px; color: white;'>
        <h1>🤖💬 Farooq Shah AI & Educational Hub 🌐✨</h1>
        <p>Professional Step-by-Step Learning & AI Platform</p>
    </div>
    """)
    
    with gr.Tabs() as tabs:
        
        with gr.TabItem("🏠 Home Page", id=0):
            gr.Markdown("### Please select an option below or use the top menu:")
            with gr.Row():
                btn_islamic = gr.Button("🕌 Islamic & Boards Info", size="lg")
                btn_computer = gr.Button("💻 Computer Courses", size="lg")
            with gr.Row():
                btn_mobile = gr.Button("📱 Mobile & Photoshop", size="lg")
                btn_language = gr.Button("🌐 100+ Language Courses", size="lg")
            with gr.Row():
                btn_ai = gr.Button("🤖💬 AI Tutor & Chat (ChatGPT Style)", size="lg")

        with gr.TabItem("🕌 Islamic Info", id=1):
            gr.Markdown(get_islamic_boards_info())
            
        with gr.TabItem("💻 Computer Courses", id=2):
            gr.Markdown(get_computer_courses())
            
        with gr.TabItem("📱 Mobile Editing", id=3):
            gr.Markdown(get_mobile_editing_courses())
            
        with gr.TabItem("🌐 Language Courses", id=4):
            gr.Markdown(get_language_courses())
            
        with gr.TabItem("🤖 AI Tutor & Chat", id=5):
            gr.ChatInterface(
                fn=ai_chat_response,
                title="Farooq Shah AI Classroom",
                description="Type your questions below (ChatGPT-style interface)."
            )

    btn_islamic.click(lambda: 1, None, tabs)
    btn_computer.click(lambda: 2, None, tabs)
    btn_mobile.click(lambda: 3, None, tabs)
    btn_language.click(lambda: 4, None, tabs)
    btn_ai.click(lambda: 5, None, tabs)

if __name__ == "__main__":
    demo.launch()
