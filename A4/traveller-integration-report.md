### Re: Outsourced Implementation Review
#### To the manager:

Upon receiving the implementation of our specification, we have found it to contain all of the details we have outlined along with some additions. We found the module suitable for our `traveller-client` and with intuitive structure.
As we had requested, the programmers implemented our high-level specification using their discretion for the finer details. The functionality was given using Classes. Each function in our specification was found as a method in the appropriate class. They have added to our outline a `to_string` method, a `connect` method which adjoins two Towns, and a `disconnect_town` method which removes a Town from all of its neighbors. The former two were a welcome oversight however the latter was undesignated and potentially dangerous. Additionally, they did not follow the specification for `passage-safe?`, as the method was placed in the Town class rather than in the TownNetwork.

Our estimate for the integration of the received implementation with the traveller-client module we created in Task #3 Warm-Up #3 is about 4 hours. Given that the received implementation was tested and it functions as is expected, integration of the two modules is possible. However, in order to do so, function names need to be changed on the client side and variable names need to be adapted. In addition, we would also need to create Town and Character objects to pass into different functions as we identify them with strings in our client program. For this, we estimate upwards of 4 hours of work to integrate the two modules successfully.

In retrospect, our specification was not free of ambiguity. There are some further details that we would have liked to clarify for our implementers that would have helped both their code and a smooth integration of the server and client. Our specification could have been much more precise in its declarations of variable names, function names, function signatures, and data structures. While we had initially set out to describe an implementation in the functional style (similar to the `NumJSON` specification we implemented that you may have heard of), but our specification did read as an object-oriented server, which was not the original intention. Instead, we would have made more clear the desire for a module of functions with inherent properties. Stating what variables and functions were to be public or private was also a detail we did not define. Overall, our aim was to give the implementers some freedom, but in doing so, we definitely could have been more specific to prevent conflicts with our integration. But, given the specification we had given, we had a pretty good idea of what we were expecting to receive.