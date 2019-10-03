include "syncInterface.iol"
include "time.iol"

inputPort Server {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: SyncInterface
}

execution{ concurrent }



main{
    sendMessage()( response ){ //Gets a message from client
        synchronized( syncToken ) { //Syncronised such that only one messaged can be proccessed at a time
            response.message = "some message for now" //Adds a response message to response
            sleep@Time( 1000 )() //Simulates computation time
        }
    } //When done, sends a response to client with the respond message, and fetches the next message to be processed.

    
}



