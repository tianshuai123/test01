import openai
import streamlit as st
from streamlit_chat import message
 
 
# 填写 API key
openai.api_key = ''
 
 
# 如果没有 prompts 这个 session_state，就初始化
if 'prompts' not in st.session_state:
    st.session_state['prompts'] = [{"role": "system", "content": "You are a helpful assistant. Answer as concisely as possible with a little humor expression."}]
# 如果没有 generated 这个 session_state，就初始化
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
# 如果没有 past 这个 session_state，就初始化
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
 
# 生成 ChatGPT API 的回答
def generate_response(prompt):
    # 把用户输入的消息加入到 prompts 中
    st.session_state['prompts'].append({"role": "user", "content":prompt})
    # 调用 ChatGPT API
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = st.session_state['prompts']
    )
    # 从 API 返回的结果中获取 ChatBot 的回答
    message=completion.choices[0].message.content
    return message
 
 
# 重置聊天界面
def end_click():
    st.session_state['prompts'] = [{"role": "system", "content": "You are a helpful assistant. Answer as concisely as possible with a little humor expression."}]
    st.session_state['past'] = []
    st.session_state['generated'] = []
    st.session_state['user'] = ""
 
 
# 处理聊天按钮点击事件
def chat_click():
    if st.session_state['user']!= '':
        # 获取用户输入的消息
        chat_input = st.session_state['user']
        # 调用 ChatGPT API 生成回答
        output=generate_response(chat_input)
        # 把生成的回答和用户输入的消息存储到 session_state 中
        st.session_state['past'].append(chat_input)
        st.session_state['generated'].append(output)
        st.session_state['prompts'].append({"role": "assistant", "content": output})
        st.session_state['user'] = ""
 
 
# 显示 ChatBot 界面
#st.image("logo.png", width=80)
st.title("My ChatBot")
 
 
# 显示用户输入框
user_input=st.text_input("You:", key="user")
 
 
# 显示聊天和重置按钮
chat_button=st.button("Send", on_click=chat_click)
end_button=st.button("New Chat", on_click=end_click)
 
 
# 显示 ChatBot 的回答和用户的输入
if st.session_state['generated']:
    # 倒序遍历已经生成的回答和用户的输入
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # 分别使用两种方式显示 ChatBot 的回答
        tab1, tab2 = st.tabs(["normal", "rich"])
        with tab1:
            message(st.session_state['generated'][i], key=str(i) + '_generated')
        with tab2:
            st.markdown(st.session_state['generated'][i])
        # 显示用户的输入
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_past')
