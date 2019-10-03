include "semaphore_utils.iol"
include "console.iol"

main{
    acquire@SemaphoreUtils(request)(response)
    println@Console(response.name + " " + response.permits)()

}