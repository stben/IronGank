<template>
  <div class="wrap">
    <div class="wrap-main">
      <div class="msg-list">
        <ul class="msg-cont">
          <li v-for="item in getNewMsg" >
            <span>{{item.myName}}</span>
            <span class="msg-cont-item" >{{item.msg}}</span>
          </li>
        </ul>
      </div>
      <div class="msg-input">
        <div style="height: 100%; position: relative;" >
          <mu-text-field v-model='myMsg'
                         placeholder="在这儿发射弹幕"
                         autocomplete="off"
                         onkeyup.enter="sendMsg"
          ></mu-text-field>
          <div class="btn-group btn-group-custom" >
            <mu-button type="button" class="btn btn-primary" @click='sendMsg' >发送</mu-button>
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
  /* props: [, 'myName', 'myNo', 'roomNo', 'roomName', 'videoStatus'], */
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
      e.preventDefault() // prevents page reloading
    },
    sendMsg: function (e) {
      SocketInsatnce.emit('sendChatMsg', { 'roomNo': this.roomNo, 'myName': this.myName, 'msg': this.myMsg })
      e.preventDefault() // prevents page reloading
      let data = {
        'myName': this.myName + '1',
        'msg': this.myMsg
      }
      this.getNewMsg.push(data)
      console.log(this.getNewMsg)
    }
  }
}
</script>

<style scoped >
  .wrap{
    height: 300px;
  }

  .wrap-main{
    float:right;
    padding-left: 200px;
    height:300px;
    width:500px;
    text-align:left;
    margin-top: 60px;
    margin-left: 100px;
  }
  .msg-list{
    height: 600px;
    border: 10px solid #58B7FF;
    overflow: auto;
  }
  .msg-input{
    height: 100px;
    border: 10px solid #58B7FF;
  }
  .btn-group-custom{
    position: absolute;
    width: 100%;
    bottom: 0;
    left: 0;
    padding: 10px;
  }
  .btn-group-custom .btn {
    float: right;
  }
  .msg-cont{
    list-style-type: none;
    margin: 0px;
    padding: 0px;
  }
  .msg-cont > li{
    margin: 0px;
    padding: 5px;
  }
  .msg-cont-item{
    background: #8492A6;
    padding: 5px 10px;
    border-radius: 2px;
  }
</style>
