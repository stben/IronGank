<template>
<mu-container>
  <mu-text-field v-model="value1" placeholder="请输入姓名"></mu-text-field><br/>
  <mu-text-field v-model="value2" placeholder="请输入学号"></mu-text-field><br/>
  <mu-text-field v-model="value3" placeholder="请输入密码"></mu-text-field><br/>
  <mu-text-field v-model="value4" placeholder="请输入手机号码"></mu-text-field>
  <mu-button color="primary">发送验证码</mu-button><br/>
  <mu-text-field v-model="value5" placeholder="请输入手机验证码."></mu-text-field><br/>
    <mu-flex justify-content="center">
    <mu-button @click="openSimpleDialog">注册</mu-button>
  </mu-flex>
  <mu-dialog title="提示信息" width="360" :open.sync="openSimple">
    注册成功
   <mu-button slot="actions" flat color="primary" @click="closeSimpleDialog">Close</mu-button>
  </mu-dialog>
</mu-container>
</template>
<script>
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
    openSimpleDialog (){
      this.openSimple = true;
    },
    closeSimpleDialog (){
      this.openSimple = false;
    }
  }
}
</script>

<style scoped>
.button-wrapper {
  text-align: center;
  .mu-button{
    margin: 8px;
  }
}
</style>
