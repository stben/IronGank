<template>
  <div id="queue">
    {{stuList}}
    <mu-list class="badge-list-wrap">
      <mu-list-item v-for="(item, index) in stuList"
                    :key="index">
        <mu-list-item-content>
          <mu-list-item-title>{{item}}</mu-list-item-title>
        </mu-list-item-content>
      </mu-list-item>
    </mu-list>
    <mu-button font
               color="primary"
               @click="changeMyStatus">{{buttonInfo}}</mu-button>
  </div>
</template>

<script>
import socket from 'socket.io-client'
const SocketInsatnce = socket('http://localhost:3000')

export default {
  name: 'studentQueue',
  components: {
  },
  data () {
    return {
      stuInfoList: [],
      inQueue: false,
      buttonInfo: '加入队列',
      activeStyle: this.queueStatus ? 'disable' : ' color="primary" '
    }
  },
  watch: {
    inQueue: {
      handler (newName) {
        this.buttonInfo = this.inQueue ? '离开队列' : '加入队列'
      }
    }
  },
  mounted () {
    SocketInsatnce.emit('updateMyList', this.roomNo)
    let self = this
    this.buttonInfo = this.inQueue ? '离开队列' : '加入队列'
    SocketInsatnce.emit('joinRoom', this.roomNo)
    SocketInsatnce.on('updateList', (data) => {
      if (data.indexOf(self.myName) !== -1) {
        self.inQueue = true
      } else {
        self.inQueue = false
      }
      self.stuList = data
    })
  },
  props: ['stuList', 'myName', 'myNo', 'roomNo', 'roomName', 'queueStatus'],
  methods: {
    updateOurList: function () {
      let data = { 'roomNo': this.roomNo, 'msg': this.stuList }
      SocketInsatnce.emit('sendMsg', data)
      console.log(data)
    },
    changeMyStatus: function () {
      if (this.inQueue) {
        let index = this.stuList.indexOf(this.myName)
        if (index > -1) {
          this.stuList.splice(index, 1)
        }
        this.inQueue = !this.inQueue
      } else {
        this.inQueue = !this.inQueue
        this.stuList.push(this.myName)
      }
      this.updateOurList()
      this.sendMsgToParent(this.stuList)
    },
    sendMsgToParent: function (data) {
      this.$emit('listenToChildEvent', data)
    }
  }
}
</script>
