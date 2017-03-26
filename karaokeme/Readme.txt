Architecture's Final Overview

Client-server Architecture
The chosen architecture for the system is the Client-server architecture, 
as customers in the system are making requests for a service to a server
which is the service provider. 
In the web application this is performed in a very simple way:
    1. First customers have to create their account.
    2. Then, when they are logged in the system, they can see the list 
    of songs and make a song petition, this is the request for the service.
    3. Finally the Song Manager or DJ satisfies this petition by playig
    the song that appears on the Petition List, this is the service
    providing.

As we can observe it is a simple application that can grow in the future
according to customer needs and that is why this architecture was chosen 
for too as scalability and modifiability can be supported and give ease
to the maintainability process.


Design Patterns

There are two architecture design patterns I would like to stress and 
show that were considered:
    - The client-server pattern
        The pattern was considered as we will have many clients maybe 
        not so many but they will be requesting a type of service that 
        will be provided by the Song Managers. 
        Petition system is explained above in the document.

    -The MVC pattern
        As we are working with a web application and mainly with the
        web development framework known as Django we consider dividing
        the system into 3 different modules of subparts. 
            Model part: where all of the system's data structure is
            created and controlled. 
            View part: where all the visual aspects of the system are
            included and mainly the user interface, by which the customers
            will alter data in this case make petitions and the song
            managers will add, edit, delete songs and delete petitions
            once the song has been played.
            Controller part: that will basically work as an intermediary 
            between the model and view parts and contains the main logic 
            of the system.
