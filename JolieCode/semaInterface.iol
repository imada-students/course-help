type request: void {
    .message: string
    .number: int
}
type response: void {
    .message: string
    .number: int
}


interface SemaInterface{
    RequestResponse: sendMessage( request )( response ),
                     getLock( void )( int ),
                     releaseLock( int )( void )
}
