include "console.iol"
include "serviceInterface.ol"

inputPort B {
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SendMessageIface
}

main{
    sendString( x );
    sendNumber( x )
    println@Console( x )(  )
}