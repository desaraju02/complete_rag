from langchain_openai import ChatOpenAI
from langchain_community.tools import tool

@tool
def get_capital(country: str) -> str:
    """Return the capital city for Germany"""
    capitals = {"India": "New Delhi", "France": "Paris", "Germany": "Berlin"}
    return capitals.get(country, "Capital not found")

chat_model = ChatOpenAI(model="gpt-4o-mini")
chat_model_with_tools = chat_model.bind_tools([get_capital])
response = chat_model_with_tools.invoke("What is the capital of Germany?")
print('response type:', type(response))
print('response content repr:', repr(response.content))
print('response tool_calls len:', len(response.tool_calls))
for i, tc in enumerate(response.tool_calls):
    print('--- tool call', i)
    print('type:', type(tc))
    print('dir subset:', [n for n in dir(tc) if n in ('name','args','result','output','raw','tool_output','response','tool_name') or 'tool' in n])
    print('name:', getattr(tc, 'name', None))
    print('args:', getattr(tc, 'args', None))
    print('result:', getattr(tc, 'result', None))
    print('output:', getattr(tc, 'output', None))
    print('tool_output:', getattr(tc, 'tool_output', None))
    print('raw:', getattr(tc, 'raw', None))
    print('response:', getattr(tc, 'response', None))
    print('dict:', getattr(tc, '__dict__', None))
