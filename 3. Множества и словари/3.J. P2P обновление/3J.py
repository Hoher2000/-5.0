# 3 J. P2P обновление https://contest.yandex.ru/contest/59541/problems/J/

def main():

    class Device:
        def __init__(self, id: int, peers: int, segments: int) -> None:
            self.id: int = id
            self.segments_num: int = segments
            self.update_segments: list = [1 for j in range(segments)]
            self.status = 0
            self.unupdate_segments = set(range(segments))
            self.peers_grade: list = [0 for j in range(peers)]
            self.slots = 0
            self.requests = []

        def __repr__(self) -> str:
            return f'{self.update_segments}'


    class Network:
        def __init__(self, peers: int, segments: int) -> None:
            self.segments_num: int = segments
            self.peers_num: int = peers
            self.devices: list = [Device(i, peers, segments) for i in range(peers)]
            self.devices[0].update_segments = [True for j in range(segments)]
            self.devices[0].status = 100
            self.status = 200 / peers
            self.filled_segment_counter = [[1, set((0,))] for j in range(segments)]
            self.prime_by_dev = [[None, None] for i in range(peers)]

        def prior_pockets(self):
            return sorted((i[0], j) for j, i in enumerate(self.filled_segment_counter))

        def __repr__(self) -> str:
            return f'{tuple(device.update_status() for device in self.devices)}'


    n, k = map(input().split())
    net = Network(n, k)

    while round(net.status, 5) != 200:

        gen_prime_pockets = net.prior_pockets()

        for i in range(net.peers_num):
            del net.devices[i].requests[:]
            if round(net.devices[i].status, 5) != 100:
                net.devices[i].slots += 1
                for count, pocket in gen_prime_pockets:
                    if pocket in net.devices[i].unupdate_segments:  # для каждого устройства выбираем необновленный пакет, который встречается реже всего среди всех устройств
                        net.prime_by_dev[i][0] = pocket
                        break
            else:
                net.prime_by_dev[i] = [None, None]

        for i in range(net.peers_num):
            segment = net.prime_by_dev[i][0]
            if segment != None:
                dev = min(net.filled_segment_counter[segment][1], key=lambda x: (net.devices[x].status, x))
                net.prime_by_dev[i][1] = dev
                net.devices[dev].requests.append(i)

        cache = []

        for i in range(net.peers_num):
            if net.devices[i].requests:
                acceptor = min(net.devices[i].requests, key=lambda x: (-net.devices[i].peers_grade[x], net.devices[x].status, x))
                segment = net.prime_by_dev[acceptor][0]
                cache.append((acceptor, segment,i))
       
        for acceptor, segment, donor in cache:
            net.devices[acceptor].update_segments[segment] = True
            net.devices[acceptor].status += 100 / net.segments_num
            net.devices[acceptor].unupdate_segments.remove(segment)
            net.status += 200 / (net.segments_num * net.peers_num)
            net.filled_segment_counter[segment][0] += 1
            net.filled_segment_counter[segment][1].add(acceptor)
            net.devices[acceptor].peers_grade[donor] += 1

        
    for i in range(1, net.peers_num):
        print(net.devices[i].slots, end=' ')

if __name__ == '__main__':
    main()      