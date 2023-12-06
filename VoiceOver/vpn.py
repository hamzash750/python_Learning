import ipaddress

network = ipaddress.IPv4Network("192.168.1.0/24")

print("Network", network)

print("Network mask:", network.netmask)

print("Broadcast address:", network.broadcast_address)

print("Number of hosts under", str(network), ":", network.num_addresses)


print("Hosts under", str(network), ":")
# for host in network.hosts():
#     print(host)
#     print("Subnets:")
# for subnet in network.subnets(prefixlen_diff=2):
#     print(subnet)

print("Supernet:", network.supernet(prefixlen_diff=1))


print("Overlaps 192.168.0.0/16:", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))