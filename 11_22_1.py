'''
AWS wants to increase the reliability of their network by upgrading crucial data center routers. Each data center has a single router that is connected to every other data center through a direct link or some other data center.

To increase the fault tolerance of the network, AWS wants to identify routers which would result in a disconnected network if they went down and replace then with upgraded versions.

Write an algorithm to identify all such routers.

Input:

The input to the function/method consists of three arguments:

    numRouters, an integer representing the number of routers in the data center.
    numLinks, an integer representing the number of links between the pair of routers.
    Links, the list of pair of integers - A, B representing a link between the routers A and B. The network will be connected.

Output:

Return a list of integers representing the routers with need to be connected to the network all the time.

Example:

Input:

numRouters = 7
numLinks = 7
Links = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]

Output:

[2, 3, 5]

Explanation:

On disconnecting router 2, a packet may be routed either to the routers- 0, 1, 3, 4 or the routers - 5, 6, but not to all.

On disconnecting router 3, a packet may be routed either to the routers - 0,1,2,5,6 or to the router - 4, but not to all.

On disconnecting router 5, a packet may be routed either to the routers - 0,1,2,3,4 or to the router - 6, but not to all.

'''
def get_critical_routers(links, num_routers, num_links):

    critical_routers = set()

    # For each router, make a map of the incoming links to it, and another map of outgoing links
    incoming_links_dict = collections.defaultdict(list)
    outgoing_links_dict = collections.defaultdict(list)

    for link in links:
        incoming_links_dict[link[1]] += [link[0]]
        outgoing_links_dict[link[0]] += [link[1]]


    # for routers that may not have any incoming or outgoing links, add them
    # to the dict as well
    for i in range(0, num_routers):
        if i not in incoming_links_dict:
            incoming_links_dict[i] = []
        if i not in outgoing_links_dict:
            outgoing_links_dict[i] = []


    for router in range(0, num_routers):
        # if router has no incoming link, skip that
        if len(incoming_links_dict[router]) == 0:
            continue

        # check if router has any outgoing links
        outgoing_routers = outgoing_links_dict[router]
        if len(outgoing_routers) > 0:
            # for each of these outgoing routers, get their incoming routers
            for receiver_router in outgoing_routers:
                all_incoming_of_receiver = incoming_links_dict[receiver_router]

                # if length is 1, then router is critical
                if len(all_incoming_of_receiver) == 1:
                    critical_routers.add(router)

    return critical_routers



numRouters = 7
numLinks = 7
links = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]
print(get_critical_routers(links, numRouters, numLinks))
