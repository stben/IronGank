<template>
  <div id="roomManage">
    <teacherFrame :selected="'0'" :title="'房间 '+roomNo+'：房间信息管理'" :roomNo="roomNo"></teacherFrame>
    <mu-paper class="paper" z-depth="2">
      <mu-form class="form" label-position="top" label-width="80">
        <mu-row>
          <mu-text-field v-model="roomName" ref="roomName" label="房间名称" class="name"></mu-text-field>
          <mu-select v-model="form.select" ref="departmentName" label="所属院系" class="department">
            <mu-option v-for="option in options" :key="option" :label="option" :value="option"></mu-option>
          </mu-select>
        </mu-row>
        <mu-row>
          <mu-form-item label="白板" class="text-left">
            <mu-switch v-model="switchVal.isBoard" ref="isBoard" ></mu-switch>
          </mu-form-item>
          <mu-form-item label="代码编译区" class="switch">
            <mu-switch v-model="switchVal.isCode" ref="isCode"></mu-switch>
          </mu-form-item>
          <mu-form-item label="密码" class="switch">
            <mu-switch v-model="switchVal.isPassword" ref="isPassword"></mu-switch>
          </mu-form-item>
          <mu-text-field v-if="switchVal.isPassword===true" v-model="password" type="password" ref="password" label="房间密码" class="password"></mu-text-field>
        </mu-row>
        <mu-row>
          <mu-text-field v-model="roomDescription" multi-line :rows="3" :rows-max="6" ref="roomDescription" label="房间简介" class="description"></mu-text-field>
        </mu-row>
        <mu-row>
          <mu-form-item class="button">
            <mu-button color="primary" @click="postRoomInfo" flat>确认修改</mu-button>
          </mu-form-item>
        </mu-row>
      </mu-form>
    </mu-paper>
  </div>
</template>

<script>
import teacherFrame from '../components/teacherFrame'
export default {
  name: 'roomManage',
  components: {
    teacherFrame
  },
  data () {
    return {
      options: [
        '计算机',
        '软件工程',
        '通信'
      ],
      form: {
        select: ''
      },
      roomName: '',
      roomDescription: '',
      departmentName: '',
      password: '',
      switchVal: {
        isBoard: false,
        isCode: false,
        isPassword: false
      },
      roomNo: this.$route.params.roomNo
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
        'roomId': this.roomNo,
        'departmentName': this.$refs.departmentName.value
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
          'roomNo': this.$route.params.roomNo
        },
        method: 'get'
      }).then((response) => {
        this.roomName = response.data.roomName
        this.roomDescription = response.data.roomDescription
        this.password = response.data.password
        this.switchVal.isBoard = response.data.isWhiteboard
        this.switchVal.isCode = response.data.isCode
        this.switchVal.isPassword = response.data.isPassword
        this.form.select = response.data.departmentName
      })
    }
  }
}
</script>

<style scoped>
  .paper{
    margin: 120px 400px;
    width: 900px;
    height: 450px;
  }
  .form{
    margin: 50px 40px;
    width: 850px;
  }
  .text-left{
    text-align: left;
    margin-top: 30px;
  }
  .switch{
    text-align: left;
    margin-top: 30px;
    margin-left: 80px;
  }
  .password{
    margin-top: 30px;
    margin-left: 20px;
    width: 400px;
  }
  .name{
    margin-left: 0;
    margin-top: 20px;
    width: 400px;
  }
  .department{
    margin-left: 20px;
    margin-top: 20px;
    width: 400px;
  }
  .description {
    margin-top: 30px;
    width: 820px;
  }
  .button{
    margin-left: 350px;
  }
</style>
