<template>
  <div>
    <div>
      <stuFrame :selected="''"
                :title="'学生 ' + ''"></stuFrame>
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
  </div>
</template>

<script>
import stuFrame from '../components/studentFrame'
import studentVideo from '../components/studentVideo'
import studentQueue from '../components/studentQueue'

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
    studentQueue
  },
  data () {
    return {
      videoStatus: true,
      queueStatus: true
    }
  },
  props: ['stuList', 'myName', 'myNo', 'roomNo', 'roomName', 'myStatus'],
  methods: {
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
}
</style>
