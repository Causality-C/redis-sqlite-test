import grpc
import users_pb2
import users_pb2_grpc


def run_os_request():
    channel = grpc.insecure_channel("localhost:50051")
    stub = users_pb2_grpc.UserServiceStub(channel)

    os_request = users_pb2.OSRequest(preferred_os="Linux")
    response = stub.GetUserByOS(os_request)

    print("Users who prefer Linux:")
    for user in response.users:
        print(
            f"ID: {user.id}, Name: {user.name}, Email: {user.email}, OS: {user.preferred_os}"
        )


def run_insert():
    channel = grpc.insecure_channel("localhost:50051")
    stub = users_pb2_grpc.UserServiceStub(channel)

    insert_request = users_pb2.NewUser(
        name="Jaime Lannister", email="jaime@lannister.com", preferred_os="LionOS"
    )

    response = stub.AddUser(insert_request)
    print(
        f"ID: {response.id}, Name: {response.name}, Email: {response.email}, OS: {response.preferred_os}"
    )


if __name__ == "__main__":
    run_insert()
