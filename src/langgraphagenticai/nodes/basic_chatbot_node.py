from src.langgraphagenticai.state.state import State

class BasicChatbotNode:

    """
    Basic Chatbot login implementation

    """

    def __init__(self, model): 
        self.llm = model 

    def process(self, state: State) -> State:
        """
        This method processes the input state by invoking the language model (LLM) with the messages contained in the state. It takes the 'messages' from the input state, passes them to the LLM's `invoke` method, and returns a new state containing the response from the LLM.
        """
        return {'messages': self.llm.invoke(state['messages'])}
        