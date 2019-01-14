<template>
  <div id="timeTable">
    <TeacherFrame :selected="'3'" :title="'房间 '+roomNo+'：直播间日历'"></TeacherFrame>
    <mu-button color="primary" @click="showAlert">新建</mu-button>
    <mu-alert color="primary" @delete="isAlert = false" delete v-if="isAlert" transition="mu-scale-transition">
       <mu-form :model="validateForm1" >
         <mu-form-item>
           <mu-text-field v-model="item.week" prop="week" placeholder="第几周"></mu-text-field>
         </mu-form-item>
         <mu-form-item>
           <mu-text-field v-model="item.weekday" prop="weekday" placeholder="星期几"></mu-text-field>
         </mu-form-item>
         <mu-form-item>
           <mu-text-field v-model="item.begin" prop="begin" placeholder="开始时间"></mu-text-field>
         </mu-form-item>
         <mu-form-item>
           <mu-text-field v-model="item.end" prop="end" placeholder="结束时间"></mu-text-field>
         </mu-form-item>
         <mu-form-item>
           <mu-text-field v-model="item.description" prop="description" placeholder="描述"></mu-text-field>
         </mu-form-item>
         <mu-form-item>
           <mu-button color="success">新建</mu-button>
         </mu-form-item>
       </mu-form>
    </mu-alert>
    <mu-expansion-panel v-for="item in timeTableList" :key="item.timeNo">
      <div slot="header">{{item.week}}&nbsp;&nbsp;&nbsp;{{item.weekday}}&nbsp;&nbsp;&nbsp;{{item.begin}}-{{item.end}}：{{item.description}}</div>
      <mu-form :model="validateForm1" >
        <mu-form-item>
          <mu-text-field v-model="item.week" prop="week" placeholder="第几周"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.weekday" prop="weekday" placeholder="星期几"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.begin" prop="begin" placeholder="开始时间"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.end" prop="end" placeholder="结束时间"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.description" prop="description" placeholder="描述"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-button color="warning">修改</mu-button>
        </mu-form-item>
      </mu-form>
    </mu-expansion-panel>
  </div>
</template>

<script>
import TeacherFrame from './TeacherFrame'
export default {
  name: 'timeTable',
  components: {
    TeacherFrame
  },
  data() {
    return {
      roomNo: 30150, // 要把房间号改了
      isAlert: false,
      timeTableList: [
        { roomNo: '30150', timeNo: '1682', week: '第一周', weekday: '周五', begin: '10:00', end: '12:00', description: 'vue的问题解答' },
        { roomNo: '30150', timeNo: '1682', week: '第三周', weekday: '周二', begin: '9:00', end: '10:00', description: 'django的问题解答' },
        { roomNo: '30150', timeNo: '1682', week: '第三周', weekday: '周三', begin: '10:00', end: '12:00', description: '前后端连接的问题解答' },
        { roomNo: '30150', timeNo: '1682', week: '第四周', weekday: '周五', begin: '8:00', end: '10:00', description: '软件工程实训' },
        { roomNo: '30150', timeNo: '1682', week: '第五周', weekday: '周日', begin: '10:00', end: '12:00', description: '问题反馈' }
      ]
    }
  },
  methods: {
    showAlert () {
      this.isAlert = !this.isAlert
    }
  }
}
</script>

<style scoped>
  .paper{
    margin: -430px 300px;
  }
  .list{
    width: 600px;
    margin: 250px auto;
  }
</style>
