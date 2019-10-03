interface SendMessageIface {
    OneWay:
        sendNumber( int ),
        sendString( string ),
        sendAny( any )
}