include "console.iol"
main{
a.b = 0
a.b[1] = 1
a.b.c = 2
a = 3
println@Console(#a)()
println@Console(#a.b)()
println@Console(#a.b.c)()


a[0] = 3

}