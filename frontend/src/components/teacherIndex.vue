<template>
  <div id="teacherIndex">
    <teacherBar :title="'主页 '"></teacherBar>
    <mu-list class="button-list">
      <mu-list-item>
        <mu-button color="primary" to="/student/index" class="all-button">查看所有房间</mu-button>
        <mu-button color="success" @click="showAlert" class="new-button">新建房间</mu-button>
      </mu-list-item>
    </mu-list>
    <mu-alert @delete="isAlert = false" delete v-if="isAlert" transition="mu-scale-transition" color="white" class="alert">
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
              <mu-button color="primary" @click="postRoomInfo" flat>创建</mu-button>
            </mu-form-item>
          </mu-row>
        </mu-form>
      </mu-paper>
    </mu-alert>
    <mu-list class="list">
      <mu-list-item v-for="item in list" :key="item.roomId">
        <span class="point">●</span> 房间&nbsp;{{item.roomId}}：{{item.roomName}}
        <mu-button v-bind:id="item.roomId" color="primary" @click="getRoomInfo($event)" class="list-button1" flat>编辑</mu-button>
        <mu-button color="success" v-bind:id="item.roomId" @click="live" class="list-button2" flat>开播</mu-button>
      </mu-list-item>
    </mu-list>
  </div>
</template>

<script>
import teacherBar from '../components/teacherBar'
export default {
  name: 'teacherIndex',
  components: {
    teacherBar
  },
  data () {
    return {
      isAlert: false,
      shift: 'movies',
      list: [],
      options: [
        '计算机', '软件工程', '通信'
      ],
      form: {
        select: ''
      },
      roomName: '',
      roomDescription: '',
      password: '',
      switchVal: {
        isBoard: false,
        isCode: false,
        isPassword: false
      }
    }
  },
  mounted: function () {
    this.getTeacherRooms()
  },
  methods: {
    showAlert() {
      this.isAlert = !this.isAlert
    },
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    },
    getRoomInfo(e) {
      this.$router.push({ name: 'roomManage', params: {roomNo: e.currentTarget.id} })
    },
    getTeacherRooms: function() {
      this.$axios.get('/api/teacher/teacherIndex')
        .then((response) => {
          this.list = response.data.roomList
        })
    },
    postRoomInfo() {
      let postData = {
        'roomName': this.$refs.roomName.value,
        'password': this.$refs.password.value,
        'isBoard': this.switchVal.isBoard,
        'isPassword': this.switchVal.isPassword,
        'roomDescription': this.$refs.roomDescription.value,
        'isCode': this.switchVal.isCode,
        'roomId': this.roomNo,
        'departmentName': this.form.select
      }
      this.$axios.post('api/teacher/newRoom',
        this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code === '0000') {
            this.$router.push('index')
          } else {
            alert(response.data.msg)
          }
        })
    },
    live() {}
  }
}
</script>

<style scoped>
  .button-list{
    margin-top: 80px;
  }
  .all-button{
    margin-left: 420px;
  }
  .new-button{
    margin-left: 30px;
  }
  .alert{
    margin: 0 auto;
    width: 700px;
    height: 450px;
  }
  .paper{
    margin-left: -30px;
    width: 900px;
    height: 450px;
  }
  .form{
    margin: 0 40px;
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
  .list{
    margin: 10px auto;
    width: 700px;
  }
  .point{
    color: #cfd8dc;
    font-size: 16px;
  }
  .list-button1{
    position: absolute;
    margin-left: 500px;
  }
  .list-button2{
    position: absolute;
    margin-left: 580px;
  }
</style>
