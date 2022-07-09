"""module for all the redis connection related
functionalities"""
import os
import redis


redis_connection_pool = redis.ConnectionPool(
    host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0)


class RedisConnectionWrapper:
    """class for all the redis connection related
    functions"""

    def __init__(self) -> None:
        pass

    @classmethod
    def get_connection(cls) -> redis.Redis:
        """Returns the connection to the database"""
        return redis.Redis(connection_pool=redis_connection_pool)

    @classmethod
    def get_key(cls, key: str) -> str:
        """Returns the value of the key
        key: the key to get the value of"""
        return redis.Redis(connection_pool=redis_connection_pool).get(key)

    @classmethod
    def set_key(cls, key: str, value: str) -> None:
        """Sets the value of the key without expiration
        key: the key to set the value of
        value: the value to set"""
        redis.Redis(connection_pool=redis_connection_pool).set(key, value)

    @classmethod
    def set_key_with_expiry(cls, key: str, value: str, expiry: int) -> None:
        """Sets the value of the key with expiration
        key: the key to set the value of
        value: the value to set
        expiry: the number of seconds the key should be valid for"""
        redis.Redis(connection_pool=redis_connection_pool).set(
            key, value, ex=expiry)

    @classmethod
    def delete_key(cls, key: str) -> None:
        """Deletes the key
        key: the key to delete"""
        redis.Redis(connection_pool=redis_connection_pool).delete(key)

    @classmethod
    def get_all_keys(cls) -> list:
        """Returns all the keys in the database,
        ideally avoid using this function, will cause issues in large databases and can cause
        the entire server to crash"""
        return redis.Redis(connection_pool=redis_connection_pool).keys()

    @classmethod
    def zset_add(cls, key: str, value: str, score: int) -> None:
        """Adds a value to a sorted set
        key: the key to add the value to
        value: the value to add
        score: the score to assign to the value"""
        redis.Redis(connection_pool=redis_connection_pool).zadd(
            key, value, score)

    @classmethod
    def zset_pop(cls, key: str) -> str:
        """Pops a value from a sorted set
        key: the key to pop the value from"""
        return redis.Redis(connection_pool=redis_connection_pool).zpopmin(key)

    @classmethod
    def zset_score(cls, key: str, value: str) -> int:
        """Returns the score of the value in the sorted set
        key: the key to get the score of
        value: the value to get the score of"""
        return redis.Redis(connection_pool=redis_connection_pool).zscore(key, value)

    @classmethod
    def zset_remove(cls, key: str, value: str) -> None:
        """Removes a value from a sorted set
        key: the key to remove the value from
        value: the value to remove"""
        redis.Redis(connection_pool=redis_connection_pool).zrem(key, value)

    @classmethod
    def zset_range(cls, key: str, start: int, end: int) -> list:
        """Returns a range of values from a sorted set
        key: the key to get the values from
        start: the start index of the range
        end: the end index of the range"""
        return redis.Redis(connection_pool=redis_connection_pool).zrange(key, start, end)

    @classmethod
    def create_channel(cls, channel: str) -> None:
        """Creates a channel
        channel: the channel to create"""
        redis.Redis(connection_pool=redis_connection_pool).publish(
            channel, 'channel created{}'.format(channel))

    @classmethod
    def publish(cls, channel: str, message: str) -> None:
        """Publishes a message to a channel
        channel: the channel to publish the message to
        message: the message to publish"""
        redis.Redis(connection_pool=redis_connection_pool).publish(
            channel, message)

    @classmethod
    def subscribe(cls, channel: str, callback: callable) -> None:
        """Subscribes to a channel
        channel: the channel to subscribe to
        callback: the callback to call when a message is received"""
        redis.Redis(connection_pool=redis_connection_pool).pubsub().subscribe(
            channel, callback)

    @classmethod
    def unsubscribe(cls, channel: str) -> None:
        """Unsubscribes from a channel
        channel: the channel to unsubscribe from"""
        redis.Redis(connection_pool=redis_connection_pool).pubsub(
        ).unsubscribe(channel)

    @classmethod
    def get_all_channels(cls) -> list:
        """Returns all the channels in the database,
        ideally avoid using this function, will cause issues in large databases and can cause
        the entire server to crash"""
        return redis.Redis(connection_pool=redis_connection_pool).pubsub().channels

    @classmethod
    def zincrby(cls, key: str, value: str, increment: int) -> int:
        """Increments the score of a value in a sorted set
        key: the key to increment the score of
        value: the value to increment the score of
        increment: the amount to increment the score by"""
        return redis.Redis(connection_pool=redis_connection_pool).zincrby(key, increment, value)
