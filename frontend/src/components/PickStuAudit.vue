<template>
  <div id="PickStuAudit">
    <TeacherFrame :selected="'1'" :title="'房间 '+roomNo+'：可排队学生列表'"></TeacherFrame>
    <PickStuTabsAudit v-bind:auditList="auditList"></PickStuTabsAudit>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import PickStuTabsAudit from './PickStuTabsAudit'
export default {
  name: 'PickStuAudit',
  components: {
    TeacherFrame,
    PickStuTabsAudit
  },
  data() {
    return {
      roomNo: 30150, // 要把房间号改了
      auditList: [
        {stuName: '张三', stuNo: '20162358'}, {stuName: '李四', stuNo: '20162362'}, {stuName: '王五', stuNo: '20162351'}
      ]
    }
  }
}
</script>

<style scoped>

</style>
