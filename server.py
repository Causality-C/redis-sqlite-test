import sqlite3
import grpc
from concurrent import futures
import users_pb2
import users_pb2_grpc


DATABASE = "users.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            preferred_os TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


class UserService(users_pb2_grpc.UserServiceServicer):
    def GetUsers(self, request, context):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("Select id, name, email, preferred_os FROM users")
        rows = cursor.fetchall()
        users_list = [
            users_pb2.User(id=row[0], name=row[1], email=row[2], preferred_os=row[3])
            for row in rows
        ]
        return users_pb2.UsersList(users=users_list)

    def AddUser(self, request: users_pb2.NewUser, context):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, preferred_os) VALUES (?, ?, ?)",
            (request.name, request.email, request.preferred_os),
        )
        conn.commit()
        new_user_id = cursor.lastrowid
        conn.close()
        return users_pb2.User(
            id=new_user_id,
            name=request.name,
            email=request.email,
            preferred_os=request.preferred_os,
        )

    def GetUserByOS(self, request: users_pb2.OSRequest, context):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "Select id, name, email, preferred_os FROM users where preferred_os = ?",
            (request.preferred_os,),
        )
        rows = cursor.fetchall()
        users_list = [
            users_pb2.User(id=row[0], name=row[1], email=row[2], preferred_os=row[3])
            for row in rows
        ]
        return users_pb2.UsersList(users=users_list)


def serve():
    init_db()  # initialize sqlite database
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server is running on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
