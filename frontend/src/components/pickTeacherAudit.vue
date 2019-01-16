<template>
  <div id="pickTeacherAudit">
    <TeacherFrame :selected="'3'" :title="'房间 '+roomNo+'：助教列表'" :roomNo="roomNo"></TeacherFrame>
    <PickTeacherTabsAudit v-bind:auditList="auditList" :roomNo="roomNo"></PickTeacherTabsAudit>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import PickTeacherTabsAudit from './PickTeacherTabsAudit'
export default {
  name: 'pickTeacherAudit',
  components: {
    TeacherFrame,
    PickTeacherTabsAudit
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
