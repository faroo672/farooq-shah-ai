def ai_chat_response(message, history):
    if not message:
        return "Hello! Welcome to Farooq Shah AI Classroom. How can I help you today?"
    
    msg = message.lower()
    if "hello" in msg or "hi" in msg or "سلام" in msg:
        return "Hello! Welcome to Farooq Shah AI. Let's start learning step-by-step. What would you like to study today?"
    else:
        return f"I received your message: '{message}'. Let's practice this step-by-step. Tell me if you have any questions."

def get_islamic_boards_info():
    return """
    # Islamic Information & Wafaq-ul-Madaris Boards
    * 1. Wafaq-ul-Madaris Al-Arabia Pakistan
    * 2. Tanzeem-ul-Madaris Ahl-e-Sunnat
    * 3. Wafaq-ul-Madaris Salafia
    * 4. Wafaq-ul-Madaris Shia Pakistan
    """

def get_computer_courses():
    return """
    # Computer Courses
    * Microsoft Office (MS Word & Excel)
    * Basic Computer & Windows Settings
    * Web Development (HTML, CSS, Python)
    """

def get_mobile_editing_courses():
    return """
    # Mobile Editing Courses
    * Canva Mobile Graphic Design
    * Video Editing & AI Avatar Creation
    * Poster & Certificate Designing
    """

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Farooq Shah AI & Educational Hub")
    gr.Markdown("Welcome to your interactive AI assistant and educational platform.")
    
    with gr.Tabs():
        with gr.TabItem("🤖 AI Classroom"):
            gr.ChatInterface(fn=ai_chat_response)
            
        with gr.TabItem("📚 Computer Courses"):
            gr.Markdown(get_computer_courses())
            
        with gr.TabItem("📱 Mobile Editing"):
            gr.Markdown(get_mobile_editing_courses())
            
        with gr.TabItem("🕌 Islamic Boards"):
            gr.Markdown(get_islamic_boards_info())

if __name__ == "__main__":
    demo.launch()
