include "ClientServerInterface.iol"
include "console.iol"
include "time.iol"

inputPort In {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: ClientServerInterface
}

init{
    global.t=1
    global.count=0
}

execution { concurrent }

main{
    [getToken(client)(x){
        println@Console("Getting request from client" + client + " for the token" + global.count)();
        token=true 
        while (token){
            synchronized( a ){
             if (global.t==1){
                 sleep@Time( 250 )();
                 getCurrentTimeMillis@Time( )( response );
                 println@Console("Server has the token, giving it to client " + client + " Time is " + response)();
                 sleep@Time( 250 )();
                 global.t=0;
                 x=global.count++;
                 token=false
                }else{
                 sleep@Time( 250 )()
                }
            }
        }
    }]{nullProcess}
    
    [releaseToken(client)]{
        getCurrentTimeMillis@Time( )( response );
        println@Console("Server got the token back from client " + client + " Time is " + response)();
        println@Console( " \n ")();
        synchronized( a ){
            global.t=1
        }
    }
        
}