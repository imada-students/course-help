include "common.iol"

outputPort A {
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SendNumberIface
}

main{
    sendNumber@A(7)
}

