include "time.iol"
include "semaInterface.iol"
include "console.iol"

inputPort Server {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: SemaInterface
}
execution { concurrent }

init{
    println@Console( "The service startede as expected." )(  )
    global.token = 0
    println@Console( "The current lock is: " + global.token )(  )
}
main{
    [getLock()( global.token )]{
        println@Console( "The service recieved a request to lock a resource from a client." )(  )
            if ( global.token == 0 ){
                println@Console( "The resource can be given to the current client." )(  )
                global.token = 1
                println@Console( "The current lock is: " + global.token )(  )
                sleep@Time( 1000 )()
                while( global.token == 1 ){
                    println@Console( "I must wait for the client to finish with the resource." )(  )
                    sleep@Time( 1000 )()
                }
                println@Console( "The lock is released and the resource can be used by another client." )(  )
                println@Console( "The current lock is now: " + global.token )(  )
                
            } else {
                println@Console( "The resource is unavailable, the client must wait." )(  )
            }
    }
    [releaseLock( token )()]{
        if( token == 1){
            println@Console( "The service recieved a request to release the lock of the resource from the client." )(  )
            global.token = 0
        }
    }
    

}