<template>
  <div id="pickStudentAudit">
    <teacherFrame :selected="'1'" :title="'房间 '+roomNo+'：可排队学生列表'" :roomNo="roomNo"></teacherFrame>
    <pickStudentTabsAudit v-bind:auditList="auditList" :roomNo="roomNo"></pickStudentTabsAudit>
  </div>
</template>

<script>
import teacherFrame from './teacherFrame'
import pickStudentTabsAudit from './pickStudentTabsAudit'
export default {
  name: 'pickStudentAudit',
  components: {
    teacherFrame,
    pickStudentTabsAudit
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
