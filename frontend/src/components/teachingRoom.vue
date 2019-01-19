<template>
  <div>
    <teacherBar :title="'直播'"
                class="bar"></teacherBar>
    <div class="video-div">
      <teacherVideo v-bind:stuList="stuList"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
    <div class="queue-div">
      <teacherQueue v-bind:stuList="stuList"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
    <mu-switch v-model="isCode"
               class="code-switch"></mu-switch>
    <codemirror :roomNo="roomNo"
                v-bind:status="status"
                v-if="isCode===true"
                class="code-mirror" />
    <hr class="divider" />
    <mu-switch v-model="isBoard"
               class="board-switch"></mu-switch>
    <div class="board-div"
         v-if="isBoard===true">
      <WhiteBoard label="白板"
                  v-bind:roomNo="roomNo" />
    </div>
    <div class="chat-div">
      <chattingRoom></chattingRoom>
    </div>
  </div>
</template>

<script>
import chattingRoom from '../components/chattingRoom'
import teacherVideo from '../components/teacherVideo'
import AgoraRTC from 'agora-rtc-sdk'
import codemirror from '../components/codemirror'
import WhiteBoard from '../components/whiteBoard'
import teacherQueue from '../components/teacherQueue'
import teacherBar from '../components/teacherBar'

if (!AgoraRTC.checkSystemRequirements()) {
  alert('Your browser does not support WebRTC!')
}
export default {
  name: 'teachingRoom',
  components: {
    teacherBar,
    chattingRoom,
    teacherVideo,
    teacherQueue,
    WhiteBoard,
    codemirror
  },
  data () {
    return {
      videoStatus: true,
      queueStatus: true,
      myStatus: false,
      codemirror,
      status: false,
      isCode: true,
      isBoard: true,
      roomName: this.$route.params.roomName,
      roomNo: this.$route.params.roomNo,
      stuList: []
    }
  },
}
</script>

<style scoped>
.bar {
  height: 9%;
}
.video-div {
  width: 15%;
  height: 42%;
  position: fixed;
  top: 9%;
  left: 0;
  background-color: black;
  align-items: center;
}
.queue-div {
  width: 15%;
  height: 49%;
  position: fixed;
  top: 51%;
  left: 0;
  overflow: auto;
  border: 1px solid #58b7ff;
}
.code-mirror {
  position: fixed;
  top: 9%;
  left: 15%;
  width: 65%;
  z-index: -1;
}
.divider {
  position: fixed;
  top: 360px;
  left: 15%;
  width: 65%;
  height: 1px;
  background-color: #58b7ff;
}
.chat-div {
  position: fixed;
  top: 9%;
  right: 0;
  width: 20%;
  height: 91%;
}
.board-div {
  position: fixed;
  top: 360px;
  left: 15%;
  width: 65%;
  height: 310px;
  z-index: -1;
  background-color: rgb(255, 255, 255);
}
.code-switch {
  position: fixed;
  top: 60px;
  left: 15%;
}
.board-switch {
  position: fixed;
  top: 370px;
  left: 15%;
}
</style>
