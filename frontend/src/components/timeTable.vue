<template>
  <div id="timeTable">
    <TeacherFrame :selected="'3'" :title="'房间 '+roomNo+'：直播间日历'"></TeacherFrame>
    <mu-paper class="paper">
      <mu-list class="list">
        <mu-list-row v-for="item in timeTableList">
          <mu-list-item>
            <mu-list-item-title>{{item.week}}&nbsp;&nbsp;&nbsp;{{item.weekday}}&nbsp;&nbsp;&nbsp;{{item.begin}}-{{item.end}}：{{item.description}}</mu-list-item-title>
            <mu-button flat color="warning" to="">修改</mu-button>
          </mu-list-item>
          <mu-divider></mu-divider>
        </mu-list-row>
      </mu-list>
    </mu-paper>
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
      timeTableList: [
        {roomNo: '30150', timeNo: '1682', week: '第一周', weekday: '周五', begin: '10:00', end: '12:00', description: 'vue的问题解答'},
        {roomNo: '30150', timeNo: '1682', week: '第三周', weekday: '周二', begin: '9:00', end: '10:00', description: 'django的问题解答'},
        {roomNo: '30150', timeNo: '1682', week: '第三周', weekday: '周三', begin: '10:00', end: '12:00', description: '前后端连接的问题解答'},
        {roomNo: '30150', timeNo: '1682', week: '第四周', weekday: '周五', begin: '8:00', end: '10:00', description: '软件工程实训'},
        {roomNo: '30150', timeNo: '1682', week: '第五周', weekday: '周日', begin: '10:00', end: '12:00', description: '问题反馈'}
      ]
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
