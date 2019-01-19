<template>
  <div class="wrap">
    <div class="wrap-main">
      <div class="msg-list">
        <ul class="msg-cont">
          <li v-for="item in getNewMsg"
              :key="item">
            <span>{{item.myName}}</span>
            <span class="msg-cont-item">{{item.msg}}</span>
          </li>
        </ul>
      </div>
      <div class="msg-input">
        <div style="height: 100%; position: relative;">
          <mu-text-field v-model='myMsg'
                         placeholder="在这儿发射弹幕"
                         autocomplete="off"
                         onkeyup.enter="sendMsg"
                         multi-line
                         :rows="3"
                         :rows-max="6"
                         class="text"></mu-text-field>
          <div class="btn-group btn-group-custom">
            <mu-button type="button"
                       class="btn btn-primary"
                       @click='sendMsg'>发送</mu-button>
            <mu-button @click="joinRoom">joinARoom</mu-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import socket from 'socket.io-client'
const SocketInsatnce = socket('http://localhost:3000')
export default {
  name: 'chattingRoom',
  components: {
  },
  mounted () {
    SocketInsatnce.on('getChatMsg', (msg) => {
      this.getNewMsg.push(msg)
      console.log(this.getNewMsg)
    })
  },
  data () {
    return {
      getNewMsg: [],
      roomNo: '123',
      myMsg: '',
      stuNo: 1,
      myName: 'name'
    }
  },
  methods: {
    joinRoom: function (e) {
      SocketInsatnce.emit('joinRoom', this.roomNo)
      e.preventDefault()
    },
    sendMsg: function (e) {
      SocketInsatnce.emit('sendChatMsg', { 'roomNo': this.roomNo,
        'myName': this.myName,
        'msg': this.myMsg })
      e.preventDefault()
      let data = {
        'myName': this.myName + '1',
        'msg': this.myMsg
      }
      this.getNewMsg.push(data)
      console.log(this.getNewMsg)
      this.myMsg = ''
    }
  }
}
</script>

<style scoped >
.wrap {
  height: 100%;
}

.wrap-main {
  height: 100%;
  width: 100%;
  text-align: left;
}
.msg-list {
  height: 70%;
  border: 1px solid #58b7ff;
  overflow: auto;
}
.msg-input {
  height: 30%;
  border: 1px solid #58b7ff;
}
.btn-group-custom {
  position: absolute;
  width: 100%;
  bottom: 0;
  left: 0;
  padding: 10px;
}
.btn-group-custom .btn {
  float: right;
}
.msg-cont {
  list-style-type: none;
  margin: 0px;
  padding: 0px;
}
.msg-cont > li {
  margin: 0px;
  padding: 5px;
}
.msg-cont-item {
  background: #8492a6;
  padding: 5px 10px;
  border-radius: 2px;
}
.text {
  margin-top: 10px;
  margin-left: 20px;
  width: 85%;
}
</style>
