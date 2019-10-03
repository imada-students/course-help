include "common.iol"
include "SendString.iol"

outputPort A {
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SendNumberIface, SendString
}

main{
    //sendNumber@A("hi")
    
    //task parallel 1
    //sendString@A("hi")|
    //sendString@A("hello")

    //parallel task 2
    sendString@A("hello")|
    sendNumber@A(42)
}

