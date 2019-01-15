<template>
  <div id="PickStuAccepted">
    <TeacherFrame :selected="'1'" :title="'房间 '+roomNo+'：可排队学生列表'" :roomNo="roomNo"></TeacherFrame>
    <PickStuTabsAccepted v-bind:acceptedList="acceptedList" :roomNo="roomNo"></PickStuTabsAccepted>
  </div>
</template>

<script>
import TeacherFrame from '../components/TeacherFrame'
import PickStuTabsAccepted from '../components/PickStuTabsAccepted'
export default {
  name: 'PickStuAccepted',
  components: {
    TeacherFrame,
    PickStuTabsAccepted
  },
  data() {
    return {
      roomNo: this.$route.params.roomNo,
      acceptedList: []
    }
  },
  mounted () {
    this.getPickStudents()
  },
  methods: {
    getPickStudents() {
      this.$axios.request({
        url: '/api/teacher/pickStudent',
        params: {
          'roomNo': this.$route.params.roomNo
        },
        method: 'get'
      }).then((response) => {
        this.acceptedList = response.data.acceptedList
      })
    }
  }
}
</script>

<style scoped>

</style>
