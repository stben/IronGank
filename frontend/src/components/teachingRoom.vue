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
    <codemirror :roomNo='123'
                v-bind:status="status" />
  </div>
</template>

<script>
import stuFrame from '../components/studentFrame'
import chattingRoom from '../components/chattingRoom'
import teacherVideo from '../components/teacherVideo'
import AgoraRTC from 'agora-rtc-sdk'
import codemirror from '../components/codemirror'

if (!AgoraRTC.checkSystemRequirements()) {
  alert('Your browser does not support WebRTC!')
}
export default {
  name: 'teachingRoom',
  components: {
    stuFrame,
    chattingRoom,
    teacherVideo
  },
  data () {
    return {
      stuList: ['123123'],
      videoStatus: true,
      queueStatus: true,
      myNo: 123,
      myName: 'asdsad',
      myStatus: false,
      roomNo: 12332113,
      roomName: '123123',
      codemirror,
      status: false
    }
  }
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
  width: 210px;
  height: 280px;
  position: absolute;
  top: 368px;
  left: 0;
  overflow: auto;
}
</style>
