type response: void {
    .message: string
}

interface SyncInterface {
    RequestResponse: sendMessage( void )( response )
}