include "console.iol"
include "time.iol"
include "ClientServerInterface.iol"

outputPort Out {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: ClientServerInterface
}

main{
    {getToken@Out( 1 )(x);
    println@Console( "Client1 gets the token " + x)();
    sleep@Time( 2000 )();
    println@Console( "Client1 realeses token " + x)();
    releaseToken@Out(1);
    println@Console( "Client1 is done ")();
    println@Console( " \n ")()
    }
    |
    {getToken@Out( 2 )(y);
    println@Console( "Client2 gets the token " + y)();
    sleep@Time( 2000 )();
    println@Console( "Client2 realeses token " + y)();
    releaseToken@Out(2);
    println@Console( "Client2 is done ")();
    println@Console( " \n ")()
    }
    |
    {getToken@Out( 3 )(q);
    println@Console( "Client3 gets the token " + q)();
    sleep@Time( 2000 )();
    println@Console( "Client3 realeses token " + q)();
    releaseToken@Out(3);
    println@Console( "Client3 is done ")();
    println@Console( " \n ")()
    }

}