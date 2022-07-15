import greet_pb2_grpc
import greet_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("Digite um nome (ou nada para parar o chat")
        if name == "":
            break

        hello_request = greet__pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("1. ParrotSayHello - Streaming Lado do Servidor")
        print("1. ChattyClientSayHello - Streaming Lado do Cliente")
        print("1. InteractingHello - Bidirecional")
        rpc_call = input("Qual RPC você deseja utilizar?")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "Youtube")
            hello_reply = stub.SayHello(hello_request)
            print("Resposta SayHello recebida:")
            print(hello_reply)

        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "Youtube")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("Resposta SayHello recebida:")
                print(hello_reply)

        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSayHello(get_client_stream_requests())

            print("Resposta ChattyClientSayHello recebida:")
            print(delayed_reply)

        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("Pedido InteractingHello feito")
                print(response)

if __name__ == "__main__":
    run()