interface ClientServerInterface {
    RequestResponse: getToken(int)(int),
    OneWay: releaseToken(int)
}