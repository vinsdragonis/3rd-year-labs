class LeakyBucket:
    def __init__(self, bucket_size, input_stream, output_rate):
        self.size = bucket_size
        self.queue = input_stream
        self.flow = output_rate

    def control_congestion(self):
        buffer = 0
        for i, packet in enumerate(self.queue):
            print("\nPacket:", i+1)
            print(f"Incoming packet: {packet}")
            x = self.size - buffer

            if packet < x:
                print("Bucket successful")
                buffer += packet
                print(f"Packets sent: {self.flow}\nBuffer: {buffer}")
            else:
                print("BUCKET OVERFLOW")
                print(
                    f"Packet loss: {packet - x} \t Packets sent: {self.flow}")
            buffer -= self.flow


# driver code
input_stream = [int(x) for x in input(
    "Input stream of packets: ").split(' ')]
bucket_size = int(input("Bucket size: "))
output_rate = int(input("Output data rate: "))

network = LeakyBucket(bucket_size, input_stream, output_rate)
network.control_congestion()
