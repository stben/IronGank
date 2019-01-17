<template>
  <div>
    <div>
      <stuFrame :selected="''"
                :title="'教师 ' + ''"></stuFrame>
    </div>
    <chattingRoom></chattingRoom>
    <div class="video-div">
      <teacherVideo v-bind:stuList="stuList"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
    <codemirror :roomNo="roomNo"
                v-bind:status="status" />
    <div class="queue-div">
      <teacherQueue v-bind:stuList="stuList"
                    v-bind:roomNo="roomNo"
                    v-bind:roomName="roomName" />
    </div>
  </div>
</template>

<script>
import stuFrame from '../components/studentFrame'
import chattingRoom from '../components/chattingRoom'
import teacherVideo from '../components/teacherVideo'
import AgoraRTC from 'agora-rtc-sdk'
import codemirror from '../components/codemirror'
import teacherQueue from '../components/teacherQueue'

if (!AgoraRTC.checkSystemRequirements()) {
  alert('Your browser does not support WebRTC!')
}
export default {
  name: 'teachingRoom',
  components: {
    stuFrame,
    chattingRoom,
    teacherVideo,
    teacherQueue
  },
  data () {
    return {
      videoStatus: true,
      queueStatus: true,
      myNo: 123,
      myName: 'asdsad',
      myStatus: false,
      codemirror,
      status: false
    }
  },
  props: ['stuList', 'roomNo', 'roomName']
}
</script>

<style scoped>
.video-div {
  width: 210px;
  height: 304px;
  float: left;
  position: absolute;
  top: 64px;
  left: auto;
  right: auto;
}
.queue-div {
  width: 220px;
  height: 385px;
  position: absolute;
  top: 368px;
  left: 0;
  overflow: auto;
  border: 1px solid black;
}
</style>
