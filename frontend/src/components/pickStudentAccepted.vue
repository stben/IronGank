<template>
  <div id="PickStuAccepted">
    <teacherFrame :selected="'1'" :title="'房间 '+roomNo+'：可排队学生列表'" :roomNo="roomNo"></teacherFrame>
    <pickStudentTabsAccepted v-bind:acceptedList="acceptedList" :roomNo="roomNo"></pickStudentTabsAccepted>
  </div>
</template>

<script>
import teacherFrame from './teacherFrame'
import pickStudentTabsAccepted from './pickStudentTabsAccepted'
export default {
  name: 'pickStudentAccepted',
  components: {
    teacherFrame,
    pickStudentTabsAccepted
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
