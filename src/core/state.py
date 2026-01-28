from enum import Enum, auto
from typing import TypedDict, Optional
class AgentState(Enum):

    INITIALIZED = auto()
    WAITING_FOR_INPUT = auto()
    INPUT_CLARIFICATION = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    VALIDATING = auto()
    RETRYING = auto()
    FAILED = ()
    TERMINATED = auto()


ALLOWED_TRANSITIONS = {
    AgentState.INITIALIZED:{AgentState.WAITING_FOR_INPUT},
    AgentState.WAITING_FOR_INPUT:{AgentState.PROCESSING, AgentState.INPUT_CLARIFICATION},
    AgentState.INPUT_CLARIFICATION:{AgentState.PROCESSING},
    AgentState.PROCESSING:{AgentState.VALIDATING},
    AgentState.VALIDATING:{AgentState.RETRYING, AgentState.COMPLETED},
    AgentState.RETRYING:{AgentState.INPUT_CLARIFICATION, AgentState.COMPLETED, AgentState.FAILED, AgentState.TERMINATED},
    AgentState.FAILED:set(),
    AgentState.TERMINATED:set(),
    AgentState.COMPLETED: set(),
}

