import grpc
from concurrent import futures
import time

import greet_pb2_grpc
import greet_pb2

class GreeterServicer(greet_pb2_grpc.GreaterServicer):
    def SayHello(self, request, context):
        print("Request SayHello feito: ")
        print(request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"
        return hello_reply

    def ParrotSaysHello(self, request, context):
        print("Pedido ParrotSaysHello feito")
        print(request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i+1}"
            yield hello_reply
            time.sleep(3)


    def ChattyClientSayHello(self, request_iterator, context):
        delayed_reply = greet_pb2.DelayedReply
        for request in request_iterator:
            print("Pedido ChattyClientSayHello feito:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"Você enviou {len(delayed_reply.request)} mensagens. Espere um atraso na resposta"
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print("Pedido InteractingHello feito")
            print(request)

            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f'{request.greeting} {request.name}'

            yield hello_reply

def serve():
    server grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()