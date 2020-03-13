#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    locations = [None] * length  

    """
    YOUR CODE HERE
    tickets = [
        Ticket{ source: "PIT", destination: "ORD" },
        Ticket{ source: "XNA", destination: "CID" },
        Ticket{ source: "SFO", destination: "BHM" },
        Ticket{ source: "FLG", destination: "XNA" },
        Ticket{ source: "NONE", destination: "LAX" },
        Ticket{ source: "LAX", destination: "SFO" },
        Ticket{ source: "CID", destination: "SLC" },
        Ticket{ source: "ORD", destination: "NONE" },
        Ticket{ source: "SLC", destination: "PIT" },
        Ticket{ source: "BHM", destination: "FLG" }
    ]

    """
    for ticket in tickets:
        # creating map with starting location as key and destination as value
        hash_table_insert(ht, ticket.source, ticket.destination)

    print(ht)

    for i in range(length):
        if locations[i - 1] is not None:
            locations[i] = hash_table_retrieve(ht, locations[i - 1])
            print(locations[i - 1])
        else:
            locations[i] = hash_table_retrieve(ht, "NONE")

    # slicing off the NONE
    # print(locations)
    return locations[:-1]
