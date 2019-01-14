<template>
  <div>
    <TeacherBar  :title="'新建房间'"></TeacherBar>
    <mu-paper class="paper3" z-depth="4">
      <mu-text-field v-model="value1" placeholder="请输入房间名称" ref="roomName"></mu-text-field><br/>
      <mu-text-field v-model="value2" placeholder="请输入房间密码" ref="password"></mu-text-field><br/>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value1" label="白板" ref="isBoard" ></mu-switch>
      </mu-flex>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value2" label="代码编译区" ref="isCode"></mu-switch>
      </mu-flex>
      <mu-flex class="select-control-row">
        <mu-switch v-model="switchVal.value3" label="密码" ref="isPassword"></mu-switch>
      </mu-flex>
      <mu-text-field v-model="value3" placeholder="房间简介" multi-line :rows="3" :rows-max="6" ref="roomDescription">
      </mu-text-field><br/>
      <mu-button color="primary" @click="postNewRoom">确认创建房间</mu-button>
    </mu-paper>
  </div>
</template>

<script>
import TeacherBar from '../components/TeacherBar'
export default {
  name: 'NewRoom',
  components: {
    TeacherBar
  },
  data () {
    return {
      value1: '',
      value2: '',
      value3: '',
      switchVal: {
        value1: false,
        value2: false,
        value3: false
      }
    }
  },
  methods: {
    postNewRoom() {
      let postData = {
        'roomName': this.$refs.roomName.value,
        'password': this.$refs.password.value,
        'isBoard': this.$refs.isBoard.value,
        'isPassword': this.$refs.isPassword.value,
        'roomDescription': this.$refs.roomDescription.value
      }
      this.$axios.post('http://127.0.0.1:8000/teacher/newRoom',
        this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code === '0000') {
            this.$router.push('/teacher/index')
          } else alert(response.data.msg)
        })
    }
  }
}
</script>

<style scoped>
.paper3{
    margin: 150px 300px;
  }
</style>
