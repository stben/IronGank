<template>
  <mu-container>
    <mu-text-field v-model="value1"
                   placeholder="请输入姓名"
                   ref="stuName"></mu-text-field><br />
    <mu-text-field v-model="value2"
                   placeholder="请输入学号"
                   ref="stuNo"></mu-text-field><br />
    <mu-text-field v-model="value3"
                   placeholder="请输入密码"
                   ref="password"></mu-text-field><br />
    <mu-text-field v-model="value4"
                   placeholder="请输入手机号码"
                   ref="phone"></mu-text-field>
    <mu-button color="primary">发送验证码</mu-button><br />
    <mu-text-field v-model="value5"
                   placeholder="请输入手机验证码."></mu-text-field><br />
    <mu-flex justify-content="center">
      <mu-button @click="postRegister">注册</mu-button>
    </mu-flex>
    <mu-dialog title="提示信息"
               width="360"
               :open.sync="openSimple">
      注册成功
      <mu-button slot="actions"
                 flat
                 color="primary"
                 @click="closeSimpleDialog">Close</mu-button>
    </mu-dialog>
  </mu-container>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      value1: '',
      value2: '',
      value3: '',
      value4: '',
      value5: '',
      openSimple: false
    }
  },
  methods: {
    openSimpleDialog () {
      this.openSimple = true
    },
    closeSimpleDialog () {
      this.$router.push('Login')
    },
    postRegister () {
      let postData = {
        'student_id': this.$refs.stuNo.value,
        'tel': this.$refs.phone.value,
        'password': this.$refs.password.value,
        'lastname': this.$refs.stuName.value,
        'firstname': ' '
      }
      axios.post('http://127.0.0.1:8000/student/register', {
        params: {
          postData
        }
      })
        .then(function (response) {
          if (response.data.code === '0000') { this.openSimpleDialog() }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }

}
</script>

<style scoped>
.button-wrapper {
  text-align: center;
}
.mu-button {
  margin: 8px;
}
</style>
