var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)
var port = 3000
let listCatch = []
let haveList = false

io.on('connection', function (socket) {
  console.log('a user connected')
  socket.on('disconnect', function () {
    console.log('user disconnected')
  })
  socket.on('chat message', function (msg) {
    io.broadcast.emit('chat message', msg)
  })
  socket.on('joinRoom', function (roomNo) {
    socket.join(roomNo, () => {
      let rooms = Object.keys(socket.rooms)
      console.log(rooms)
    })
  })
  socket.on('sendMsg', function (data) {
    if (data.msg !== '') {
      haveList = false
      for (let i = 0; i < listCatch.length; i++) {
        if (listCatch[i].roomNo === data.roomNo) {
          listCatch[i] = data
          haveList = false
        }
      }
      if (haveList === false) {
        listCatch.push(data)
      }
      socket.broadcast.to(data.roomNo).emit('updateList', data.msg)
      console.log('发送到房间号为：' + data.roomNo + '的房间，信息为：' + data.msg)
    }
  })
  socket.on('removeMyList', function(data) {
    for (let i = 0; i < listCatch.length; i++) {
      if (listCatch[i].roomNo === data.roomNo) {
        listCatch.splice(i, 1)
      }
    }
  })
  socket.on('updateMyList', function(roomNo) {
    for (let i = 0; i < listCatch.length; i++) {
      if (listCatch[i].roomNo === roomNo) {
        return listCatch[i].msg
      }
    }
    return []
  })
  socket.on('codeMsg', function (msg) {
    io.broadcast.emit('codeMsg', msg)
  })
  socket.on('sendCode', function(data) {
    socket.broadcast.to(data.roomNo).emit('getCode', data.msg)
  })

  socket.on('drawing', function(data) {
    socket.broadcast.emit('drawing', data)
  })
  socket.on('clear', function(data) {
    socket.broadcast.emit('clear', data)
  })
  socket.on('drawRec', function(data) {
    socket.broadcast.emit('drawRec', data)
  })

  socket.on('sendChatMsg', function (data) {
    if (data !== '') {
      socket.broadcast.to(data.roomNo).emit('getChatMsg', data)
      console.log(data)
    }
  })
})

http.listen(port, function () {
  console.log('listening on *:' + port)
})
