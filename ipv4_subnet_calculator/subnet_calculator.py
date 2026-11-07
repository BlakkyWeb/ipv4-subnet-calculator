import ipaddress

def calculate_subnet(ip_address, prefix):

    # Calculate IPv4 subnet information.
    network = ipaddress.IPv4Network(
        f"{ip_address}/{prefix}",
        strict=False
    )

    total_addresses = network.num_addresses

    if network.prefixlen <= 30:
        usable_hosts = total_addresses - 2
        first_host = network.network_address + 1
        last_host = network.broadcast_address - 1

    elif network.prefixlen == 31:
        usable_hosts = 2
        first_host = network.network_address
        last_host = network.broadcast_address

    else:
        usable_hosts = 1
        first_host = network.network_address
        last_host = network.broadcast_address

    return{
        "IP Address": ip_address,
        "Subnet Mask": network.netmask,
        "Network Address": network.network_address,
        "Broadcast Address": network.broadcast_address,
        "First Host": first_host,
        "Last Host": last_host,
        "Total Addresses": total_addresses,
        "Usable Hosts": usable_hosts,
        "CIDR Prefix": network.prefixlen
    }
