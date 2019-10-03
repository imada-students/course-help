include "console.iol"
include "semaInterface.iol"
include "time.iol"


outputPort Server {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: SemaInterface
}
main{
    {
        println@Console( "Client 1: I am awake." )(  )
        getLock@Server()( token )
        println@Console( "The lock is currently: " + token )(  )
        println@Console( "Client 1: I have made a request to the server." )(  )
        while( token != 0 ){
            println@Console( "Client 1: Resource not available yet." )(  )
            sleep@Time( 1000 )()
            getLock@Server()( token )
        }
        if( token == 0 ){
            println@Console( "Client 1: Hurray! I have a lock on the resource." )(  )
            sleep@Time( 3000 )()
            releaseLock@Server( 1 )()
            println@Console( "Client 1: My work is done, the lock is released." )(  )
        }
    }
    |
    {
        sleep@Time( 500 )()
        println@Console( "Client 2: I am awake." )(  )
        getLock@Server()( token )
        println@Console( "The lock is currently: " + token )(  )
        println@Console( "Client 2: I have made a request to the server." )(  )
        while( token != 0 ){
            println@Console( "Client 2: Resource not available yet." )(  )
            sleep@Time( 3000 )()
            getLock@Server()( token )
        }
        if( token == 0 ){
            println@Console( "Client 2: Hurray! I have a lock on the resource." )(  )
            sleep@Time( 3000 )()
            releaseLock@Server( 1 )()
            println@Console( "Client 2: My work is done, the lock is released." )(  )
        }
    }
}