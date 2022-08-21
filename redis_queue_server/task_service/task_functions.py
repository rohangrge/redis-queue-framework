from datetime import datetime
import json
from redis_utils.lib.connection_utils import RedisConnectionWrapper
from datetime import datetime

class TaskFunctions:
    """
        functions to enqueue and dequeue tasks on demand
    """
    def __init__(self) -> None:
        pass
    
    @classmethod
    def enqueue_task():
        RedisConnectionWrapper.zset_add(key="test", value="test", score=datetime.now())
    
    @classmethod
    def dequeue_task():
        RedisConnectionWrapper.zset_pop("test")