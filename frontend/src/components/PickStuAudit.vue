<template>
  <div id="PickStuAudit">
    <TeacherFrame :selected="'1'" :title="'房间 '+roomNo+'：可排队学生列表'" :roomNo="roomNo"></TeacherFrame>
    <PickStuTabsAudit v-bind:auditList="auditList" :roomNo="roomNo"></PickStuTabsAudit>
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
      roomNo: this.$route.params.roomNo,
      auditList: []
    }
  },
  mounted () {
    this.getPickAudit()
  },
  methods: {
    getPickAudit() {
      this.$axios.request({
        url: '/api/teacher/pickStudent',
        params: {
          'roomNo': this.$route.params.roomNo
        },
        method: 'get'
      }).then((response) => {
        this.auditList = response.data.auditList
      })
    }
  }
}
</script>

<style scoped>

</style>
