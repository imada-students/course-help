include "console.iol"
include "time.iol"
include "ClientServerInterface.iol"

outputPort Token {
    Location: "socket://localhost:8000"
    Protocol: sodep
    Interfaces: ClientServerInterface
}

main{
    while (true){
         getToken@Token()(token);
        if (token==1){
            print@Console("Hurray, Client 2 got the token \n")(  );
            sleep@Time(1000)()
            releaseToken@Token()
            sleep@Time(500)()
        }
        else{print@Console("Client 2 waiting\n")(  );
        sleep@Time(1000)()
        }
    }

}

