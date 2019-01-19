<template>
  <div id="studentLogin">
    <img src="../assets/background.jpg"
         class="img">
    <mu-paper :z-depth="4"
              class="board">
      <br />
      <span class="text">计算机课程答疑平台</span>
      <mu-tabs :value.sync="active"
               color="white"
               indicator-color="blue"
               center>
        <mu-tab style="color: #03a9f4">学生</mu-tab>
        <mu-tab style="color: #78909c"
                to="/teacher/login">教师</mu-tab>
      </mu-tabs>
      <div v-if="active===0">
        <mu-form ref="form0"
                 :model="validateForm0"
                 class="formstyle">
          <mu-form-item prop="username"
                        :rules="usernameRules0"
                        class="input">
            <mu-text-field v-model="validateForm0.username"
                           prop="username"
                           placeholder="手机号"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="password"
                        :rules="passwordRules0"
                        class="input">
            <mu-text-field type="password"
                           v-model="validateForm0.password"
                           prop="password"
                           placeholder="密码"></mu-text-field>
          </mu-form-item>
          <mu-form-item class="loginbutton">
            <mu-button color="primary"
                       @click="submitStudent">登录</mu-button>
          </mu-form-item>
          <mu-form-item class="signin">
            <mu-button flat
                       color="primary"
                       to="/register">注册</mu-button>
          </mu-form-item>
        </mu-form>
      </div>
    </mu-paper>
  </div>
</template>

<script>
export default {
  name: 'studentLogin',
  data () {
    return {
      active: 0,
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
    submitStudent: function () {
      if (!!this.validateForm0.username && !!this.validateForm0.password) {
        this.$axios.post('/api/student/studentLogin',
          this.$Qs.stringify(this.validateForm0)
        )
          .then((response) => {
            if (response.data.code === '0000') {
              this.$router.push('/student/index')
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
.img {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}
.board {
  margin: 120px auto;
  width: 390px;
  height: 360px;
}
.text {
  font-size: 28px;
  color: grey;
}
.formstyle {
  display: flex;
  flex-direction: column;
  width: 350px;
  margin: 50px auto;
}
.input {
  margin-left: 20px;
  width: 320px;
}
.loginbutton {
  margin: 0 auto;
}
.signin {
  margin: -60px 250px;
}
</style>
