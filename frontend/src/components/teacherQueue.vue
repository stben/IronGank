<template>
  <div id="queue">
    <mu-list v-for="(item, index) in stuInfoList"
             :key="item">
      <mu-paper :z-depth="3"
                class="box">
        <mu-list-item-title>
          {{item}}<mu-badge :content=index+1
                    class="tag"></mu-badge>
        </mu-list-item-title>
        <mu-button @click="upThisStudent(item)"
                   fab
                   small
                   class="up-button">上</mu-button>
        <mu-button @click="downThisStudent(item)"
                   fab
                   small>下</mu-button>
        <mu-button @click="removeThisStudent(item)"
                   fab
                   small>出</mu-button>
        <mu-button @click="goTopThisStudent(item)"
                   fab
                   small>顶</mu-button>
      </mu-paper>
    </mu-list>
  </div>
</template>

<script>
import socket from 'socket.io-client'
const SocketInsatnce = socket('http://localhost:3000')
export default {
  name: 'teacherQueue',
  components: {
  },
  created: function () {
    console.log(this.roomNo)
    SocketInsatnce.emit('joinRoom', this.roomNo)
    SocketInsatnce.emit('updateMyList', this.roomNo)
    this.stuInfoList = this.stuList
  },
  mounted () {
    let self = this
    /* this.stuList */
    SocketInsatnce.on('updateList', (data) => {
      self.stuInfoList = data
    })
  },
  data () {
    return {
      stuInfoList: ['asdasd']
    }
  },
  props: ['stuList', 'roomNo', 'roomName'],
  methods: {
    sendMsg (data, e) {
      SocketInsatnce.emit('sendMsg', { 'roomNo': this.roomNo, 'msg': this.myMsg, 'command': data.command })
      e.preventDefault() // prevents page reloading
    },
    updateOurList: function () {
      let data = { 'roomNo': this.roomNo, 'msg': this.stuInfoList }
      SocketInsatnce.emit('sendMsg', data)
    },
    upThisStudent (stuName) {
      let hisIndex = this.stuInfoList.indexOf(stuName)
      if (hisIndex !== 0) {
        // 交换第x个和第y个元素
        // x < y
        let x = hisIndex
        let y = hisIndex + 1
        this.stuInfoList.splice(x - 1, 1, ...this.stuInfoList.splice(y - 1, 1, this.stuInfoList[x - 1]))
        console.log(this.stuInfoList) /// [1,2,4,3,5]
        this.updateOurList()
      } else {
        this.goTopThisStudent(stuName)
      }
    },
    downThisStudent (stuName) {
      let hisIndex = this.stuInfoList.indexOf(stuName)
      // 交换第x个和第y个元素
      // x < y
      let x = hisIndex + 1
      let y = hisIndex + 2
      this.stuInfoList.splice(x - 1, 1, ...this.stuInfoList.splice(y - 1, 1, this.stuInfoList[x - 1]))
      console.log(this.stuInfoList) /// [1,2,4,3,5]
      this.updateOurList()
    },
    goTopThisStudent (stuName) {
      let hisIndex = this.stuInfoList.indexOf(stuName)
      this.stuInfoList.splice(hisIndex, 1)
      this.stuInfoList.unshift(stuName)
    },
    removeThisStudent (stuName) {
      let hisIndex = this.stuInfoList.indexOf(stuName)
      this.stuInfoList.splice(hisIndex, 1)
      this.updateOurList()
    }
  }
}
</script>

<style scoped>
.can-enter-queue {
  color: primary;
}
.small-button {
  width: 15px;
  height: 15px;
}
.tag {
  position: absolute;
  right: 5px;
}
.up-button {
  margin-left: -20px;
}
.box {
  width: 200px;
  margin-top: -7px;
  margin-left: 3px;
}
</style>
