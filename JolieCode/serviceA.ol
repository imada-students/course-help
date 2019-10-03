include "serviceInterface.ol"

outputPort B{
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SendMessageIface
}

main{
    sendString@B( "42" )
}