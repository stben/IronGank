<template>
  <div>
    <div>
      <stuFrame :selected="''"
                :title="'学生 ' + ''" />
    </div>
    <mu-switch v-model="isCode"
               class="code-switch" />
    <codemirror :roomNo="roomNo"
                v-bind:status="status"
                v-if="isCode===true"
                class="code-mirror" />
    <mu-switch v-model="isBoard"
               class="board-switch" />
    <div v-if="isBoard===true"
         class="board-div">
    </div>
    <div class="video-div">
      <studentVideo v-bind:videoStatus="videoStatus"
                    v-bind:stuList="stuList"
                    v-bind:myName="myName"
                    v-bind:myNo="myNo"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
    <div class="queue-div">
      <studentQueue v-bind:queueStatus="queueStatus"
                    v-bind:stuList="stuList"
                    v-bind:myName="myName"
                    v-bind:myNo="myNo"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
    <div class="chat-div">
      <chattingRoom></chattingRoom>
    </div>
  </div>
</template>

<script>
import stuFrame from '../components/studentFrame'
import studentVideo from '../components/studentVideo'
import studentQueue from '../components/studentQueue'
import chattingRoom from '../components/chattingRoom'
import codemirror from '../components/codemirror'

export default {
  name: 'stuStudyRoom',
  created: function () {
    if (this.myStatus) {
      this.videoStatus = false
      this.queueStatus = false
    }
  },
  mounted () {
  },
  components: {
    stuFrame,
    studentVideo,
    studentQueue,
    codemirror,
    chattingRoom
  },
  data () {
    return {
      videoStatus: true,
      queueStatus: true,
      isCode: true,
      isBoard: true
    }
  },
  props: ['stuList', 'myName', 'myNo', 'roomName', 'myStatus', 'roomNo'],
  methods: {
  }
}
</script>

<style scoped>
.video-div {
  width: 210px;
  height: 285px;
  position: fixed;
  top: 60px;
  left: 0;
  background-color: black;
}
.queue-div {
  width: 210px;
  height: 325px;
  position: fixed;
  top: 345px;
  left: 0;
  overflow: auto;
  border: 1px solid black;
}
.code-mirror {
  position: fixed;
  top: 60px;
  left: 210px;
  height: 290px;
  width: 855px;
  z-index: -1;
}
.chat-div {
  position: fixed;
  top: 0;
  right: 0;
}
.board-div {
  position: fixed;
  top: 360px;
  left: 210px;
  width: 855px;
  height: 310px;
  z-index: -1;
  background-color: gray;
}
.code-switch {
  position: fixed;
  top: 65px;
  left: 210px;
}
.board-switch {
  position: fixed;
  top: 360px;
  left: 210px;
}
</style>
