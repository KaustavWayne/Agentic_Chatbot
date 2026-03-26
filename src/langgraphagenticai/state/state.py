from typing_extensions import TypedDict, List
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represents the structure of the state used in graph
    """

    messages: Annotated[List, add_messages]

