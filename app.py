with gr.Blocks() as demo:
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

