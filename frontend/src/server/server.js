var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)
var port = 3000
let list_catch = []

io.on('connection', function (socket) {
    console.log('a user connected')
    
    socket.on('disconnect', function () {
        console.log('user disconnected')
    })
    
    socket.on('chat message', function (msg) {
        io.broadcast.emit('chat message', msg)
    })

    socket.on('joinRoom', function (roomNo) { // 加入以roomNo命名的房间
        socket.join(roomNo, () => {
            let rooms = Object.keys(socket.rooms);
            console.log(rooms); // [ <socket.id>, 'room 237' ]
        })
    })
    
    socket.on('sendMsg', function (data) {
        if(data.msg!==''){
            have = false
            for(let i =0; i < list_catch.length; i++) {
                if(list_catch[i].roomNo == data.roomNo) {
                    list_catch[i] = data
                    have = false
                }
            }
            if(have=false){
                list_catch.push(data)
            }
            socket.broadcast.to(data.roomNo).emit('updateList', data.msg)
            //socket.to('others').emit('an event', { some: 'data' })
            console.log('发送到房间号为：'+data.roomNo + '的房间，信息为：'+ data.msg); // [ <socket.id>, 'room 237' ]
        }
    })
    
    socket.on('removeMyList', function(data){
        for(let i =0; i < list_catch.length; i++) {
            if(list_catch[i].roomNo == data.roomNo) {
                list_catch.splice(i,1)
            }
        }
    })
    
    socket.on('updateMyList', function(roomNo){
        for(let i =0; i < list_catch.length; i++) {
            if(list_catch[i].roomNo == data.roomNo) {
                return list_catch[i].msg
            }
        }
        return []
    })
    
    socket.on('codeMsg', function (msg) { 
        io.broadcast.emit('codeMsg', msg)
    })
    
    socket.on('sendCode', function(data) {
        socket.broadcast.to(data.roomNo).emit('getCode', data.msg)
        }
    )
    
    socket.on('sendChatMsg', function (data) {
        if(data!==''){
            socket.broadcast.to(data.roomNo).emit('getChatMsg', data)
            //socket.to('others').emit('an event', { some: 'data' })
            console.log(data); // [ <socket.id>, 'room 237' ]
        }
    })
})

http.listen(port, function () {
  console.log('listening on *:' + port)
})
