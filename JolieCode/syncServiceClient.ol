include "syncInterface.iol"
include "console.iol"

outputPort Server{
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SyncInterface
}

main{
    {
        sendMessage@Server()( response1 );
        println@Console( response1.message )()
    }
    |
    {
        sendMessage@Server()( response2 );
        println@Console( response2.message )()
    }
    |
    {
        sendMessage@Server()( response3 );
        println@Console( response3.message )()
    }
    |
    {
        sendMessage@Server()( response4 );
        println@Console( response4.message )()
    }
    |
    {
        sendMessage@Server()( response5 );
        println@Console( response5.message )()
    }
    

    }