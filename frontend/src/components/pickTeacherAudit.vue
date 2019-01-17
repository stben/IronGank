<template>
  <div id="pickTeacherAudit">
    <teacherFrame :selected="'3'" :title="'房间 '+roomNo+'：助教列表'" :roomNo="roomNo"></teacherFrame>
    <pickTeacherTabsAudit v-bind:auditList="auditList" :roomNo="roomNo"></pickTeacherTabsAudit>
  </div>
</template>

<script>
import teacherFrame from './teacherFrame'
import pickTeacherTabsAudit from './pickTeacherTabsAudit'
export default {
  name: 'pickTeacherAudit',
  components: {
    teacherFrame,
    pickTeacherTabsAudit
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
        url: '/api/teacher/pickTeacher',
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
