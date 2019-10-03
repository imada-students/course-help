include "console.iol"
include "serviceInterface.ol"

inputPort B {
    Location: "socket://localhost:8000/"
    Protocol: sodep
    Interfaces: SendMessageIface
}

main{
    //sendString( x )|
    //sendNumber( y );
    //println@Console( x )(  )|
    //println@Console( y )(  )

    [sendNumber( x )]{ 
        println@Console( x )()
        sendString( y )
        println@Console( y )()
    }
    [sendString( y )]{ 
        println@Console( y )()
        sendNumber( x )
        println@Console( x )()

    
    }
}