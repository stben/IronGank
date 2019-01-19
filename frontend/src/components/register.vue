<template>
  <mu-container>
    <link rel="stylesheet"
          href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css">
    <div class="img-div">
      <mu-appbar style="width: 100%;"
                 color="#29b6f6">
        注册
        <mu-button flat
                   slot="right" to="/">登录</mu-button>
      </mu-appbar>
      <div v-if="active===0">
        <mu-row>
          <mu-col span="12"
                  class="hint">&nbsp;{{error0}}</mu-col>
        </mu-row>
        <mu-form ref="form"
                 :model="validateForm"
                 class="formstyle">
          <mu-form-item prop="firstName"
                        :rules="firstnameRules">
            <mu-text-field v-model="validateForm.firstName"
                           prop="firstName"
                           ref="stuName"
                           placeholder="请输入名字">
            </mu-text-field><br />
          </mu-form-item>
          <mu-form-item prop="sid"
                        :rules="usernameRules">
            <mu-text-field v-model="validateForm.sid"
                           prop="sid"
                           ref="stu"
                           placeholder="请输入学号">
            </mu-text-field><br />
          </mu-form-item>
          <mu-form-item prop="password"
                        :rules="passwordRules">
            <mu-text-field v-model="validateForm.password"
                           prop="password"
                           ref="password"
                           :action-icon="visibility ? 'visibility_off' : 'visibility'"
                           :action-click="() => (visibility = !visibility)"
                           :type="visibility ? 'text' : 'password'"
                           placeholder="请输入密码">
            </mu-text-field><br />
          </mu-form-item>
          <mu-form-item prop="tel"
                        :rules="telRules">
            <div style="width:350px">
              <div style="float:left">
                <mu-text-field class="tel-text"
                               v-model="validateForm.tel"
                               prop="tel"
                               ref="phone"
                               placeholder="请输入手机号码"></mu-text-field>
              </div>
              <div style="float:right">
                <mu-button color="#29b6f6"
                           class="button-wrapper"
                           @click="postCode">发送验证码</mu-button>
              </div>
            </div>
          </mu-form-item>
          <mu-form-item prop="verificationCode"
                        :rules="verificationCodeRules">
            <mu-text-field v-model="validateForm.verificationCode"
                           prop="verificationCode"
                           placeholder="请输入手机验证码.">
            </mu-text-field><br />
          </mu-form-item>
          <mu-form-item class="button-wrapper">
            <mu-button color="#29b6f6"
                       @click="postRegister">注册</mu-button>
            <mu-button @click="clear">重置</mu-button>
          </mu-form-item>
        </mu-form>
      </div>
    </div>
  </mu-container>
</template>
<script>
export default {
  data () {
    return {
      active: 0,
      error0: '',
      error1: '',
      firstnameRules: [
        { validate: (val) => !!val, message: '必须填写名字' }
      ],
      usernameRules: [
        { validate: (val) => !!val, message: '必须填写学号' }
      ],
      passwordRules: [
        { validate: (val) => !!val, message: '必须填写密码' }
      ],
      telRules: [
        { validate: (val) => !!val, message: '必须填写手机号码' },
        { validate: (val) => val.length === 11, message: '请输入正确的电话号码' }
      ],
      verificationCodeRules: [
        { validate: (val) => !!val, message: '必须填写验证码' },
        { validate: (val) => val === this.code, message: '请输入正确的验证码' }

      ],
      validateForm: {
        firstName: '',
        sid: '',
        password: '',
        tel: '',
        verificationCode: ''
      },
      visibility: false,
      code: ''
    }
  },
  methods: {
    postRegister: function () {
      this.$refs.form.validate().then((result) => {
        if (result === true) {
          let postData = {
            'student_id': this.validateForm.sid,
            'tel': this.validateForm.tel,
            'password': this.validateForm.password,
            'firstName': this.validateForm.firstName
          }
          this.$axios.post('/api/student/register',
            this.$Qs.stringify(postData)
          )
            .then((response) => {
              if (response.data.code === '0000') {
                this.$router.push('/Login')
              } else {
                alert(response.data.msg)
              }
            })
        }
      })
    },
    postCode () {
      let postData = {
        'mobile': this.validateForm.tel
      }
      this.$axios.post('/api/sendMsg', this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code === '0000') {
            this.code = response.data.msg
          } else {
            alert(response.data.msg)
          }
        })
    },
    clear () {
      this.$refs.form.clear()
      this.validateForm = {
        firstname: '',
        lastname: '',
        username: '',
        password: '',
        tel: '',
        verificationCode: ''
      }
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
.formstyle {
  display: flex;
  flex-direction: column;
  width: 350px;
  margin: -10px auto;
}
.hint {
  color: #ff0c16;
  margin: 30px auto;
}
.tel-text {
  width: 230px;
}
.img-div {
  -moz-box-shadow: 2px 2px 10px #909090;
  box-shadow: 2px 2px 10px #909090;
  background-image: url("../assets/7.jpg");
  background-size: 100%100%;
}
</style>
