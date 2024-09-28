import grpc
import redis
import users_pb2
import users_pb2_grpc
import json

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)
SERVER = "<YOUR_SERVER>:50051"


# Helper function to cache data
def cache_data(key, data, expiration=3600):
    redis_client.set(key, json.dumps(data), ex=expiration)


# Helper function to retrieve data from cache
def get_cached_data(key):
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None


# Fetch users from gRPC, with Redis caching
def get_users_from_grpc(stub):
    cache_key = "all_users"

    # Check if data is cached
    cached_users = get_cached_data(cache_key)
    if cached_users:
        print("Returning cached users")
        return cached_users

    # If not cached, call gRPC service
    response = stub.GetUsers(users_pb2.Empty())

    # Cache the users for future requests
    users_list = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "preferred_os": user.preferred_os,
        }
        for user in response.users
    ]
    cache_data(cache_key, users_list)

    return users_list


# Fetch users by OS, with Redis caching
def get_users_by_os_from_grpc(stub, preferred_os):
    cache_key = f"users_by_os_{preferred_os}"

    # Check if data is cached
    cached_users = get_cached_data(cache_key)
    if cached_users:
        print(f"Returning cached users for OS: {preferred_os}")
        return cached_users

    # If not cached, call gRPC service
    os_request = users_pb2.OSRequest(preferred_os=preferred_os)
    response = stub.GetUserByOS(os_request)

    # Cache the users for future requests
    users_list = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "preferred_os": user.preferred_os,
        }
        for user in response.users
    ]
    cache_data(cache_key, users_list)

    return users_list


def run():
    # Connect to the gRPC server
    channel = grpc.insecure_channel(SERVER)
    stub = users_pb2_grpc.UserServiceStub(channel)

    # Get all users
    print("Fetching all users")
    users = get_users_from_grpc(stub)
    for user in users:
        print(user)

    # Get users by preferred OS (e.g., "Linux")
    print("\nFetching users who prefer Linux")
    linux_users = get_users_by_os_from_grpc(stub, "Linux")
    for user in linux_users:
        print(user)


if __name__ == "__main__":
    run()
