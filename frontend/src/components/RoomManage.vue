<template>
  <div>
    <TeacherFrame :selected="'0'" :title="'房间 '+roomNo+'：房间信息管理'"></TeacherFrame>
    <mu-paper class="paper2" z-depth="4">
      <mu-text-field v-model="roomName" placeholder="请输入房间名称" ref="roomName"></mu-text-field><br/>
      <mu-text-field v-model="password" placeholder="请输入房间密码" ref="password"></mu-text-field><br/>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.isBoard" label="白板" ref="isBoard" ></mu-switch>
      </mu-flex>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.isCode" label="代码编译区" ref="isCode"></mu-switch>
      </mu-flex>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.isPassword" label="密码" ref="isPassword"></mu-switch>
      </mu-flex>
      <mu-text-field v-model="roomDescription" placeholder="房间简介" multi-line :rows="3" :rows-max="6" ref="roomDescription">
      </mu-text-field><br/>
      <mu-button color="primary" @click="postRoomInfo">确认</mu-button>
    </mu-paper>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
export default {
  name: 'RoomManage',
  components: {
    TeacherFrame
  },
  data () {
    return {
      roomName: '',
      password: '',
      roomDescription: '',
      switchVal: {
        isBoard: false,
        isCode: false,
        isPassword: false
      },
      roomNo: this.$route.params.roomId
    }
  },
  mounted () {
    this.getRoomInfo()
  },
  methods: {
    postRoomInfo() {
      let postData = {
        'roomName': this.$refs.roomName.value,
        'password': this.$refs.password.value,
        'isBoard': this.switchVal.isBoard,
        'isPassword': this.switchVal.isPassword,
        'roomDescription': this.$refs.roomDescription.value,
        'isCode': this.switchVal.isCode,
        'roomId': this.roomNo
      }
      this.$axios.post('api/teacher/roomInfo',
        this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code !== '0000') {
            alert(response.data.msg)
          }
        })
    },
    getRoomInfo() {
      this.$axios.request({
        url: '/api/teacher/roomInfo',
        params: {
          'roomNo': this.$route.params.roomId
        },
        method: 'get'
      }).then((response) => {
        this.roomName = response.data.roomName
        this.roomDescription = response.data.roomDescription
        this.password = response.data.password
        this.switchVal.isBoard = response.data.isWhiteboard
        this.switchVal.isCode = response.data.isCode
        this.switchVal.isPassword = response.data.isPassword
      })
    }
  }
}
</script>

<style scoped>
.paper2{
    margin: -200px 300px;
  }
</style>
