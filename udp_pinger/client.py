#!/usr/env/python

import sys
import time
import socket

ip = '127.0.0.1'
port = 6789


def sendPing(timeoutInSecs):

    # start the timer
    start = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        message = b'This is the message.  It will be repeated.'

        try:

            send_time_ms = time.time()
            # Send data
            # print('Sending {!r}'.format(message))
            sent = sock.sendto(message, (ip, port))
            sock.settimeout(timeoutInSecs)

            # Receive response
            # print('Waiting for response...')
            data, server = sock.recvfrom(4096)
            # print('Received {!r}'.format(data))

            recv_time_ms = time.time()
            rtt_in_ms = round(recv_time_ms - send_time_ms, 3)
            print("RTT took " + str(rtt_in_ms) + "ms")

            return rtt_in_ms
        except Exception as e:
            print("Exception: " + str(e))
            return -1
        finally:
            # print('Closing socket')
            sock.close()


def sendPings(amt, timeoutInSecs):
    sent = 0
    send_times = []
    while(sent < amt):

        length = sendPing(timeoutInSecs)

        sent += 1

        if(length == -1):
            print("Timed out")
            continue

        lengthInMillis = length * 1000

        send_times.append(length)

        print("Packet #" + str(sent) +
              " sent in " + str(lengthInMillis) + "ms")
    return send_times


def main():

    if(len(sys.argv) < 2):
        print("You must specify an IP address")
        return

    ip = sys.argv[1]
    print("Connecting to " + ip)

    # send 10 pings with 1 second timeouts and get results
    times = sendPings(10, 1 )

    avg = sum(times) / float(len(times))
    print("Average round-trip time: " + str(avg))


if __name__ == "__main__":
    main()
