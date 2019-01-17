<template>
  <div id="teacherLogin">
    <img src="../assets/background.jpg" class="img">
    <mu-paper :z-depth="4" class="board">
      <span class="text">Iron Gank</span>
      <mu-tabs :value.sync="active" color="white" indicator-color="blue" center>
        <mu-tab style="color: #78909c" to="/student/login">学生</mu-tab>
        <mu-tab style="color: #03a9f4">教师</mu-tab>
      </mu-tabs>
      <div v-if="active===1">
        <mu-form ref="form1" :model="validateForm1" class="formstyle">
          <mu-form-item prop="username" :rules="usernameRules1">
            <mu-text-field v-model="validateForm1.username" prop="username" placeholder="工号/邮箱" class="input"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="password" :rules="passwordRules1">
            <mu-text-field type="password" v-model="validateForm1.password" prop="password" placeholder="密码" class="input"></mu-text-field>
          </mu-form-item>
          <mu-form-item class="loginbutton">
            <mu-button color="primary" @click="submitTeacher">登录</mu-button>
          </mu-form-item>
        </mu-form>
      </div>
    </mu-paper>
  </div>
</template>

<script>
export default {
  name: 'teacherLogin',
  data () {
    return {
      active: 1,
      error0: '',
      error1: '',
      usernameRules0: [
        { validate: (val) => !!val, message: '必须填写用户名' }
      ],
      passwordRules0: [
        { validate: (val) => !!val, message: '必须填写密码' }
      ],
      usernameRules1: [
        { validate: (val) => !!val, message: '必须填写用户名' }
      ],
      passwordRules1: [
        { validate: (val) => !!val, message: '必须填写密码' }
      ],
      validateForm0: {
        username: '',
        password: ''
      },
      validateForm1: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    submitTeacher: function () {
      if (this.validateForm1.username && this.validateForm1.password) {
        this.$axios.post('/api/teacher/teacherLogin',
          this.$Qs.stringify(this.validateForm1)
        )
          .then((response) => {
            if (response.data.code === '0000') {
              this.$router.push('/teacher/index')
            } else {
              alert(response.data.msg)
            }
          })
      }
    }
  }
}
</script>

<style scoped>
  .img{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
  }
  .board{
    margin: 120px auto;
    width: 390px;
    height: 380px;
  }
  .text{
    font-size: 40px;
    color: grey;
  }
  .formstyle{
    display:flex;
    flex-direction: column;
    width:350px;
    margin: 50px auto;
  }
  .input{
    margin-left: 20px;
    width: 320px;
  }
  .loginbutton{
    margin:30px auto;
  }
</style>
