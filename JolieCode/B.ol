include "common.iol"
include "console.iol"
include "SendString.iol"

inputPort B {
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SendNumberIface, SendString
}

main{
    //sendNumber(x);
    //println@Console(x)()

    //task parallel 1
    //sendString(x)
    //sendString(y)
    //println@Console(x)()
    //println@Console(y)()

    //parallel task 2
    [ sendNumber(x)]
    { println@Console(x)()
     sendString(y)
      println@Console(y)()
      }
    [ sendString(y)]
    { println@Console(y)() 
    sendNumber(x)
    println@Console(x)()}
}