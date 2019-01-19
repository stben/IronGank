<template>
  <div>
    <teacherBar :title="'直播'"></teacherBar>
    <div class="video-div">
      <teacherVideo v-bind:stuList="stuList"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
    <mu-switch v-model="isCode"
               class="code-switch"></mu-switch>
    <codemirror :roomNo="roomNo"
                v-bind:status="status"
                v-if="isCode===true"
                class="code-mirror" />
    <!-- <mu-switch v-model="isBoard"
               class="board-switch"></mu-switch>
    <div v-if="isBoard===true"
         class="board-div">
    </div> -->
    <!-- <el-tab-pane label="白板" name="whiteboard">
      <whiteboard/>
    </el-tab-pane> -->
    <div class="board-div">
      <WhiteBoard label="白板"  />
    </div>
    <div class="queue-div">
      <teacherQueue v-bind:stuList="stuList"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
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
