include "console.iol"
include "syncInterface.iol"
include "time.iol"


inputPort Register {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: SyncInterface
}

execution { concurrent }

init
{
    global.registered_users=0;
    response.message = "Successful registration.\nYou are the user number "
}

main
{
    sendMessage()( response ){
        /* the synchronized section allows to access syncToken scope in mutual exclusion */
        synchronized( syncToken ) {
            response.message = response.message + ++global.registered_users;
            sleep@Time( 1000 )()
        }
    }
}



    //tokenLock = 0
    //0 = Lock is free
    //1 = Lock is in use
    //[sendString(x)]{
    //     if(tokenLock == 0){
    //         tokenLock = 1
    //         println@Console( "some stuff" )(  )
    //         sleep@Time(1000)()
    //         tokenLock = 0
    //     }else{

    //     }
    // }
