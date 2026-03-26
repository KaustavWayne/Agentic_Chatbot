from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder: 
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGrapg.
        This method initializes a chatbot node using the `BasicChatbotNode` class, and 
        integrates it into the graph structure. The chatbot node is set as both
        the entry and exit point of the graph.

        """
        
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the specified use case.
        This method checks the provided use case and calls the corresponding graph building method. If the use case is not recognized, it raises a ValueError.

        Args:
            usecase (str): The name of the use case for which to set up the graph.
        Returns:
            StateGraph: The configured graph for the specified use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()
