<template>
  <mu-container>
    <mu-tabs :value.sync="active" inverse color="blue" indicator-color="blue" center>
      <mu-tab>学生</mu-tab>
      <mu-tab>教师</mu-tab>
    </mu-tabs>
    <div v-if="active===0">
      <mu-row>
        <mu-col span="12" class="hint">&nbsp;{{error0}}</mu-col>
      </mu-row>
      <mu-form ref="form0" :model="validateForm0" class="formstyle">
        <mu-form-item prop="username" :rules="usernameRules0">
          <mu-text-field v-model="validateForm0.username" prop="username" placeholder="学号/手机号"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="password" :rules="passwordRules0">
          <mu-text-field type="password" v-model="validateForm0.password" prop="password" placeholder="密码"></mu-text-field>
        </mu-form-item>
        <mu-form-item class="loginbutton">
          <mu-button color="primary" @click="submitStudent">登录</mu-button>
        </mu-form-item>
        <mu-form-item class="signin">
          <mu-button flat color="primary" to="/register" small>注册</mu-button>
        </mu-form-item>
      </mu-form>
    </div>
   <div v-if="active===1">
     <mu-row>
       <mu-col span="12" class="hint">&nbsp;{{error1}}</mu-col>
     </mu-row>
     <mu-form ref="form1" :model="validateForm1" class="formstyle">
       <mu-form-item :rules="usernameRules1">
         <mu-text-field v-model="validateForm1.username" prop="username" rules="passwordRules0" placeholder="工号/邮箱"></mu-text-field>
       </mu-form-item>
       <mu-form-item prop="password" :rules="passwordRules1">
         <mu-text-field type="password" v-model="validateForm1.password" prop="password" rules="passwordRules0" placeholder="密码"></mu-text-field>
       </mu-form-item>
       <mu-form-item class="loginbutton">
         <mu-button color="primary" @click="submitTeacher">登录</mu-button>
       </mu-form-item>
     </mu-form>
   </div>
  </mu-container>
</template>

<script>
export default {
  name: 'Login',
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
      if (this.validateForm0.username && this.validateForm0.password) {
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
    },
    submitTeacher: function () {
      if (this.validateForm0.username && this.validateForm0.password) {
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
  .formstyle{
    display:flex;
    flex-direction: column;
    width:350px;
    margin: -10px auto;
  }
  .hint{
    color: red;
    margin: 30px auto;
  }
  .loginbutton{
    margin:30px auto;
  }
  .signin{
    margin: -78px 250px;
  }
</style>
